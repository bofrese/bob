#!/usr/bin/env python3
"""Gather the change set for a bob handover, across the story repo and its nested repos.

Usage:
    gather.py STORY_PATH STORY_ID [--full]
    gather.py --check HANDOVER < changed-files.txt
    gather.py --selftest

Prints JSON. One entry per repo (the repo holding the story, its submodules, and any
other nested git repos under its root). Per repo:
    baseline      commit the change set starts after (null = no baseline)
    reliable      true when the baseline can be trusted without asking the user
    commits       commits in scope: since baseline, or story-ID commits when no baseline
    related       no baseline only: untagged commits since the story's `started:` date that
                  touch story-related files (inferred, so the user confirms them)
    staged        staged files (staged = "intend to commit, read the handover first")
    candidates    unstaged/untracked files the story artifacts reference (offer to stage)
    unattributed  other dirty files

--check reads changed file paths (one per line, as `git diff --name-only` prints them)
on stdin and prints those the handover never mentions. Exit 1 when any are missing.

Baseline = the commit that added the newest *-handover-*.md in STORY_PATH/sessions.
Other repos map it via the submodule pointer when that pointer moved in the baseline
commit, otherwise by commit time (reliable only when no commits are near that time).
"""
import json
import os
import re
import subprocess
import sys

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
AMBIGUITY_SECONDS = 3600  # ponytail: fixed 1h window; tune if time mapping misfires in trials


def git(repo, *args, check=True):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} in {repo}: {r.stderr.strip()}")
    return r.stdout.strip() if r.returncode == 0 else ""


def lines(text):
    return [l for l in text.splitlines() if l]


def find_repos(root):
    """Root repo first, then every nested dir holding a .git entry (submodules included)."""
    repos = [root]
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if dirpath != root and (".git" in filenames or os.path.isdir(os.path.join(dirpath, ".git"))):
            repos.append(dirpath)
    return repos


def newest_handover(story_path):
    sessions = os.path.join(story_path, "sessions")
    if not os.path.isdir(sessions):
        return None
    files = sorted(f for f in os.listdir(sessions) if "-handover-" in f and f.endswith(".md"))
    return os.path.join(sessions, files[-1]) if files else None


def story_baseline(repo, handover):
    """(commit, reliable, note) for the story repo."""
    if not handover:
        return None, False, "no previous handover"
    rel = os.path.relpath(handover, repo)
    head_add = git(repo, "log", "-1", "--diff-filter=A", "--format=%H", "--", rel, check=False)
    if head_add:
        return head_add, True, "commit that added the previous handover"
    other = git(repo, "log", "--all", "-1", "--diff-filter=A", "--format=%H", "--", rel, check=False)
    if other:
        return other, False, "previous handover was added in a commit that is not an ancestor of HEAD"
    return None, False, "previous handover is not committed"


def map_baseline(story_repo, base, base_time, repo):
    """(commit, reliable, note) for a nested repo, given the story repo baseline."""
    sub_rel = os.path.relpath(repo, story_repo)
    changed = lines(git(story_repo, "diff-tree", "--no-commit-id", "-r", "--name-only", base, check=False))
    if sub_rel in changed:
        entry = git(story_repo, "ls-tree", base, "--", sub_rel, check=False).split()
        if len(entry) >= 3 and entry[1] == "commit":
            ptr = entry[2]
            ok = subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", ptr, "HEAD"]).returncode == 0
            return ptr, ok, "submodule pointer set in the baseline commit"
    mapped = git(repo, "rev-list", "-1", f"--before={base_time}", "HEAD", check=False) or None
    near = lines(git(repo, "log", "--format=%ct", f"--since={base_time - AMBIGUITY_SECONDS}",
                     f"--until={base_time + AMBIGUITY_SECONDS}", "HEAD", check=False))
    return mapped, not near, "mapped by commit time" + (" (commits near baseline time)" if near else "")


def commit_list(repo, rng=None, story_id=None):
    args = ["log", "--format=%h %s"]
    args += [f"{rng}..HEAD"] if rng else ["HEAD", f"--grep={story_id}"]
    return lines(git(repo, *args, check=False))


def story_text(story_path):
    chunks = []
    for dirpath, _, filenames in os.walk(story_path):
        for f in filenames:
            if f.endswith(".md"):
                with open(os.path.join(dirpath, f), encoding="utf-8", errors="ignore") as fh:
                    chunks.append(fh.read())
    return "\n".join(chunks)


def mentioned(path, text, strict=False):
    """True if path appears in text on a path boundary (notes.md does not match _notes.md).
    strict: a preceding "/" also blocks the match (a.py does not match src/a.py)."""
    before = r"(?<![\w./-])" if strict else r"(?<![\w.-])"
    return re.search(before + re.escape(path) + r"(?![\w-])", text) is not None


def story_started(story_path):
    """The `started:` date from the story's _index.md frontmatter, or None."""
    try:
        with open(os.path.join(story_path, "_index.md"), encoding="utf-8") as fh:
            m = re.search(r"^started:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", fh.read(), re.M)
    except OSError:
        return None
    return m.group(1) if m else None


def own_file(nested_rel):
    """Filter: files that belong to this repo, not to a nested repo inside it."""
    return lambda f: not any(f == n or f.startswith(n + "/") for n in nested_rel)


def story_related(f, repo, story_repo, story_path, text):
    """True if repo-relative file f is in the story folder or referenced by its artifacts."""
    absf = os.path.join(repo, f)
    return (os.path.commonpath([absf, story_path]) == story_path
            or mentioned(f, text) or mentioned(os.path.relpath(absf, story_repo), text))


def related_commits(repo, story_repo, story_path, text, nested_rel, since, tagged):
    """Untagged commits since `since` that touch at least one story-related file."""
    if not since:
        return []
    keep, tagged_ids = own_file(nested_rel), {c.split(" ", 1)[0] for c in tagged}
    out, commit, hit = [], None, False
    log = git(repo, "log", f"--since={since}", "--format=@@%h %s", "--name-only", "HEAD", check=False)
    for line in log.splitlines() + ["@@"]:
        if line.startswith("@@"):
            if commit and hit and commit.split(" ", 1)[0] not in tagged_ids:
                out.append(commit)
            commit, hit = line[2:] or None, False
        elif line and not hit and keep(line):
            hit = story_related(line, repo, story_repo, story_path, text)
    return out


def check(handover, files):
    """Changed files the handover text never mentions."""
    with open(handover, encoding="utf-8") as fh:
        text = fh.read()
    return [f for f in files if not mentioned(f, text, strict=True)]


def dirty(repo, story_repo, story_path, text, nested_rel):
    staged = lines(git(repo, "diff", "--cached", "--name-only", check=False))
    unstaged = lines(git(repo, "diff", "--name-only", check=False))
    untracked = lines(git(repo, "ls-files", "--others", "--exclude-standard", check=False))
    keep = own_file(nested_rel)
    candidates, unattributed = [], []
    for f in sorted(set(unstaged + untracked) - set(staged)):
        if keep(f):
            related = story_related(f, repo, story_repo, story_path, text)
            (candidates if related else unattributed).append(f)
    return [f for f in staged if keep(f)], candidates, unattributed


def gather(story_path, story_id, full=False):
    story_path = os.path.realpath(story_path)
    story_repo = os.path.realpath(git(story_path, "rev-parse", "--show-toplevel"))
    repos = [os.path.realpath(r) for r in find_repos(story_repo)]
    handover = None if full else newest_handover(story_path)
    base, reliable, note = story_baseline(story_repo, handover)
    base_time = int(git(story_repo, "show", "-s", "--format=%ct", base)) if base else None
    text = story_text(story_path)
    started = story_started(story_path)
    out = {"story_repo": story_repo, "story_id": story_id, "full": full,
           "handover": os.path.relpath(handover, story_repo) if handover else None, "repos": []}
    for repo in repos:
        if repo == story_repo:
            r_base, r_rel, r_note = base, reliable, note
        elif base:
            r_base, r_rel, r_note = map_baseline(story_repo, base, base_time, repo)
        else:
            r_base, r_rel, r_note = None, False, note
        nested_rel = {os.path.relpath(n, repo) for n in repos if n != repo and n.startswith(repo + os.sep)}
        staged, candidates, unattributed = dirty(repo, story_repo, story_path, text, nested_rel)
        commits = commit_list(repo, rng=r_base) if r_base else commit_list(repo, story_id=story_id)
        related = [] if r_base else related_commits(repo, story_repo, story_path, text, nested_rel, started, commits)
        out["repos"].append({
            "repo": os.path.relpath(repo, story_repo),
            "baseline": r_base, "reliable": r_rel, "note": r_note,
            "commits": commits, "related": related,
            "staged": staged, "candidates": candidates, "unattributed": unattributed,
        })
    return out


def selftest():
    import shutil
    import tempfile
    env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@t"}
    os.environ.update(env)
    tmp = tempfile.mkdtemp()
    clock = [1_700_000_000]

    def run(repo, *args):
        clock[0] += 7200  # 2h apart, so time mapping is unambiguous
        stamp = f"{clock[0]} +0000"
        subprocess.run(["git", "-C", repo, "-c", "protocol.file.allow=always", *args], check=True,
                       capture_output=True, env={**os.environ, "GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp})

    def write(path, text="x"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as fh:
            fh.write(text)

    def by_repo(result, name):
        return next(r for r in result["repos"] if r["repo"] == name)

    try:
        code = os.path.join(tmp, "code")
        root = os.path.join(tmp, "root")
        for r in (code, root):
            os.makedirs(r)
            run(r, "init", "-q", "-b", "main")
        write(os.path.join(code, "a.py"))
        run(code, "add", ".")
        run(code, "commit", "-qm", "S-1: first code")
        run(root, "submodule", "add", "-q", code, "code")
        story = os.path.join(root, "stories", "S-1")
        write(os.path.join(story, "_index.md"),
              "---\nstarted: 2023-01-01\n---\n# S-1\nTouches `src/ref.py` and `lib/x.py`.\n")
        run(root, "add", ".")
        run(root, "commit", "-qm", "S-1: story")
        sub = os.path.join(root, "code")

        # untagged commits: one touches a story-referenced file, one does not
        write(os.path.join(sub, "lib", "x.py"))
        run(sub, "add", ".")
        run(sub, "commit", "-qm", "untagged related")
        write(os.path.join(sub, "lib", "y.py"))
        run(sub, "add", ".")
        run(sub, "commit", "-qm", "untagged unrelated")

        # no handover -> baseline null, story-ID commits listed, untagged related ones inferred
        res = gather(story, "S-1")
        r = by_repo(res, ".")
        assert r["baseline"] is None and r["reliable"] is False, r
        assert any("S-1: story" in c for c in r["commits"]), r
        s = by_repo(res, "code")
        assert any("S-1: first code" in c for c in s["commits"]), s
        assert [c.split(" ", 1)[1] for c in s["related"]] == ["untagged related"], s
        assert not any("first code" in c for c in s["related"]), s  # tagged ones not repeated

        # committed handover -> baseline is that commit; submodule anchored by pointer
        write(os.path.join(sub, "b.py"))
        run(sub, "add", ".")
        run(sub, "commit", "-qm", "S-1: second code")
        write(os.path.join(story, "sessions", "2026-01-01-handover-x.md"))
        run(root, "add", ".")
        run(root, "commit", "-qm", "S-1: handover")
        handover_commit = git(root, "rev-parse", "HEAD")
        pointer = git(sub, "rev-parse", "HEAD")
        write(os.path.join(sub, "c.py"))
        run(sub, "add", ".")
        run(sub, "commit", "-qm", "S-1: after handover")
        res = gather(story, "S-1")
        r = by_repo(res, ".")
        assert r["baseline"] == handover_commit and r["reliable"] is True, r
        s = by_repo(res, "code")
        assert s["baseline"] == pointer and s["reliable"] is True, s
        assert [c.split(" ", 1)[1] for c in s["commits"]] == ["S-1: after handover"], s

        # staged, candidates, unattributed
        write(os.path.join(root, "staged.txt"))
        run(root, "add", "staged.txt")
        write(os.path.join(root, "src", "ref.py"))
        write(os.path.join(root, "other.txt"))
        write(os.path.join(root, "notes.md"))  # story text only mentions _notes.md
        write(os.path.join(story, "sessions", "ref.md"), "See `_notes.md`.\n")
        r = by_repo(gather(story, "S-1"), ".")
        assert r["staged"] == ["staged.txt"], r
        assert "src/ref.py" in r["candidates"], r
        assert "other.txt" in r["unattributed"], r
        assert "notes.md" in r["unattributed"], r
        assert not any(f.startswith("code") for f in r["unattributed"] + r["candidates"]), r

        # --full ignores the baseline
        assert by_repo(gather(story, "S-1", full=True), ".")["baseline"] is None

        # baseline not an ancestor of HEAD -> reliable false
        run(root, "checkout", "-q", "-b", "side")
        write(os.path.join(story, "sessions", "2026-02-01-handover-y.md"))
        run(root, "add", os.path.join(story, "sessions"))
        run(root, "commit", "-qm", "S-1: handover on side")
        run(root, "checkout", "-q", "main")
        write(os.path.join(story, "sessions", "2026-02-01-handover-y.md"))
        r = by_repo(gather(story, "S-1"), ".")
        assert r["baseline"] is not None and r["reliable"] is False, r

        # submodule pointer NOT bumped in the handover commit -> time mapping
        def time_mapped(name, minutes_after):
            c, rt = os.path.join(tmp, name + "-code"), os.path.join(tmp, name + "-root")
            for r in (c, rt):
                os.makedirs(r)
                run(r, "init", "-q", "-b", "main")
            write(os.path.join(c, "a.py"))
            run(c, "add", ".")
            run(c, "commit", "-qm", "T-1: before")
            run(rt, "submodule", "add", "-q", c, "code")
            run(rt, "commit", "-qm", "T-1: add submodule")
            st = os.path.join(rt, "stories", "T-1")
            write(os.path.join(st, "sessions", "2026-03-01-handover-z.md"))
            run(rt, "add", "stories")
            run(rt, "commit", "-qm", "T-1: handover")  # pointer untouched
            handover_time = clock[0]
            c = os.path.join(rt, "code")  # the submodule checkout
            write(os.path.join(c, "b.py"))
            run(c, "add", ".")
            clock[0] = handover_time + minutes_after * 60 - 7200  # run() adds 7200 back
            run(c, "commit", "-qm", "T-1: after")
            return by_repo(gather(st, "T-1"), "code")

        far = time_mapped("far", 120)
        assert far["note"].startswith("mapped by commit time") and far["reliable"] is True, far
        assert [x.split(" ", 1)[1] for x in far["commits"]] == ["T-1: after"], far
        near = time_mapped("near", 30)
        assert near["note"].startswith("mapped by commit time") and near["reliable"] is False, near

        # --check lists files the handover never mentions
        h = os.path.join(tmp, "h.md")
        write(h, "| `src/a.py` | 1 |\n| `skills/x/SKILL.md` | S1 |\n")
        assert check(h, ["src/a.py", "src/b.py", "skills/x/SKILL.md", "a.py"]) == ["src/b.py", "a.py"]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("selftest ok")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv == ["--selftest"]:
        selftest()
    elif len(argv) == 2 and argv[0] == "--check":
        missing = check(argv[1], lines(sys.stdin.read()))
        print("\n".join(missing))
        sys.exit(1 if missing else 0)
    elif len(argv) in (2, 3) and (len(argv) == 2 or argv[2] == "--full"):
        print(json.dumps(gather(argv[0], argv[1], full="--full" in argv), indent=2))
    else:
        sys.exit(__doc__)
