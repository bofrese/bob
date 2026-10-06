#!/usr/bin/env python3
"""Gather the change set for a bob handover, across the story repo and its nested repos.

Usage:
    gather.py STORY_PATH STORY_ID [--full]
    gather.py --selftest

Prints JSON. One entry per repo (the repo holding the story, its submodules, and any
other nested git repos under its root). Per repo:
    baseline      commit the change set starts after (null = no baseline)
    reliable      true when the baseline can be trusted without asking the user
    commits       commits in scope: since baseline, or story-ID commits when no baseline
    staged        staged files (staged = "intend to commit, read the handover first")
    candidates    unstaged/untracked files the story artifacts reference (offer to stage)
    unattributed  other dirty files

Baseline = the commit that added the newest *-handover-*.md in STORY_PATH/sessions.
Other repos map it via the submodule pointer when that pointer moved in the baseline
commit, otherwise by commit time (reliable only when no commits are near that time).
"""
import json
import os
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


def dirty(repo, story_repo, story_path, text, nested):
    staged = lines(git(repo, "diff", "--cached", "--name-only", check=False))
    unstaged = lines(git(repo, "diff", "--name-only", check=False))
    untracked = lines(git(repo, "ls-files", "--others", "--exclude-standard", check=False))
    nested_rel = {os.path.relpath(n, repo) for n in nested}
    keep = lambda f: not any(f == n or f.startswith(n + "/") for n in nested_rel)
    candidates, unattributed = [], []
    for f in sorted(set(unstaged + untracked) - set(staged)):
        if not keep(f):
            continue
        absf = os.path.join(repo, f)
        from_root = os.path.relpath(absf, story_repo)
        in_story = os.path.commonpath([absf, story_path]) == story_path
        (candidates if in_story or f in text or from_root in text else unattributed).append(f)
    return [f for f in staged if keep(f)], candidates, unattributed


def gather(story_path, story_id, full=False):
    story_path = os.path.realpath(story_path)
    story_repo = os.path.realpath(git(story_path, "rev-parse", "--show-toplevel"))
    repos = [os.path.realpath(r) for r in find_repos(story_repo)]
    handover = None if full else newest_handover(story_path)
    base, reliable, note = story_baseline(story_repo, handover)
    base_time = int(git(story_repo, "show", "-s", "--format=%ct", base)) if base else None
    text = story_text(story_path)
    out = {"story_repo": story_repo, "story_id": story_id, "full": full,
           "handover": os.path.relpath(handover, story_repo) if handover else None, "repos": []}
    for repo in repos:
        if repo == story_repo:
            r_base, r_rel, r_note = base, reliable, note
        elif base:
            r_base, r_rel, r_note = map_baseline(story_repo, base, base_time, repo)
        else:
            r_base, r_rel, r_note = None, False, note
        nested = [n for n in repos if n != repo and n.startswith(repo + os.sep)]
        staged, candidates, unattributed = dirty(repo, story_repo, story_path, text, nested)
        out["repos"].append({
            "repo": os.path.relpath(repo, story_repo),
            "baseline": r_base, "reliable": r_rel, "note": r_note,
            "commits": commit_list(repo, rng=r_base) if r_base else commit_list(repo, story_id=story_id),
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
        write(os.path.join(story, "_index.md"), "# S-1\nTouches `src/ref.py`.\n")
        run(root, "add", ".")
        run(root, "commit", "-qm", "S-1: story")
        sub = os.path.join(root, "code")

        # no handover -> baseline null, story-ID commits listed
        res = gather(story, "S-1")
        r = by_repo(res, ".")
        assert r["baseline"] is None and r["reliable"] is False, r
        assert any("S-1: story" in c for c in r["commits"]), r
        assert any("S-1: first code" in c for c in by_repo(res, "code")["commits"]), res

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
        r = by_repo(gather(story, "S-1"), ".")
        assert r["staged"] == ["staged.txt"], r
        assert "src/ref.py" in r["candidates"], r
        assert "other.txt" in r["unattributed"], r
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
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("selftest ok")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv == ["--selftest"]:
        selftest()
    elif len(argv) in (2, 3) and (len(argv) == 2 or argv[2] == "--full"):
        print(json.dumps(gather(argv[0], argv[1], full="--full" in argv), indent=2))
    else:
        sys.exit(__doc__)
