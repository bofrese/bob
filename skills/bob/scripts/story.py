#!/usr/bin/env python3
"""Find the active bob story. Prints JSON: {"tier", "certain", "candidates": [...]}.

Usage: story.py [ARG ...] [--root DIR] | story.py --selftest
ARGs are file paths or text (the user's request). Tiers, first hit wins:
  path   - an ARG path contains projects/<sub>/stories/<ID>/   (certain)
  id     - an ARG names a story ID whose folder exists          (certain)
  open   - story files open in Obsidian                          (ask the user)
  recent - most recent story file in Obsidian                    (ask the user)
  none   - nothing found
"""
import json
import re
import subprocess
import sys
from pathlib import Path

STORY_RE = re.compile(r"projects/([^/\s]+)/stories/([A-Z]+-[0-9]+)(?:/tasks/([^/\s]+?)(?:\.md)?(?:/|$|\s))?")
ID_RE = re.compile(r"\b[A-Z]+-[0-9]+\b")
OPEN_JS = "app.workspace.getLeavesOfType('markdown').map(l => l.view?.file?.path).filter(Boolean).join('\\n')"


def from_path(text):
    """Story dict from the first story path in text, else None."""
    m = STORY_RE.search(text)
    if not m:
        return None
    sub, sid, task = m.groups()
    story = {"path": f"projects/{sub}/stories/{sid}/", "story_id": sid, "subproject": sub}
    if task:
        story["task_id"] = task
    return story


def from_ids(text, root):
    """Stories whose ID appears in text and whose folder exists under root."""
    found = []
    for sid in dict.fromkeys(ID_RE.findall(text)):
        for d in sorted(root.glob(f"projects/*/stories/{sid}")):
            if d.is_dir():
                found.append(from_path(f"{d.relative_to(root).as_posix()}/"))
    return found


def obsidian(args):
    """Lines printed by the obsidian CLI, or [] if it is missing or fails."""
    try:
        out = subprocess.run(["obsidian", *args], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return []
    if out.returncode:
        return []
    return [line.removeprefix("=> ").strip() for line in out.stdout.splitlines() if line.strip()]


def stories_in(lines, root):
    """Unique existing stories found in a list of paths, in order."""
    seen = {}
    for line in lines:
        s = from_path(line)
        if s and s["path"] not in seen and (root / s["path"]).is_dir():
            seen[s["path"]] = s
    return list(seen.values())


def resolve(args, root, run=obsidian):
    for a in args:
        s = from_path(a)
        if s:
            return {"tier": "path", "certain": True, "candidates": [s]}
    ids = from_ids(" ".join(args), root)
    if ids:
        return {"tier": "id", "certain": len(ids) == 1, "candidates": ids}
    opened = stories_in(run(["eval", f"code={OPEN_JS}"]), root)
    if opened:
        return {"tier": "open", "certain": False, "candidates": opened}
    recent = stories_in(run(["recents"]), root)[:1]
    if recent:
        return {"tier": "recent", "certain": False, "candidates": recent}
    return {"tier": "none", "certain": False, "candidates": []}


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "projects/app/stories/APP-001").mkdir(parents=True)
        (root / "projects/app/stories/APP-002").mkdir(parents=True)
        no_obsidian = lambda args: []
        r = resolve(["projects/app/stories/APP-001/tasks/fix-login.md"], root, no_obsidian)
        assert r["tier"] == "path" and r["certain"], r
        assert r["candidates"][0] == {"path": "projects/app/stories/APP-001/", "story_id": "APP-001",
                                      "subproject": "app", "task_id": "fix-login"}, r
        r = resolve(["vault/projects/app/stories/APP-002/sessions/x.md"], root, no_obsidian)
        assert r["candidates"][0]["story_id"] == "APP-002" and "task_id" not in r["candidates"][0], r
        r = resolve(["please plan APP-002 using UTF-8"], root, no_obsidian)
        assert r["tier"] == "id" and r["certain"] and r["candidates"][0]["subproject"] == "app", r
        assert resolve(["APP-001 and APP-002"], root, no_obsidian)["certain"] is False
        fake = lambda args: (["notes/a.md", "projects/app/stories/APP-002/_index.md",
                              "projects/x/stories/GONE-1/_index.md"] if args[0] == "eval" else [])
        r = resolve(["no story here"], root, fake)
        assert r["tier"] == "open" and [c["story_id"] for c in r["candidates"]] == ["APP-002"], r
        fake = lambda args: ["projects/app/stories/APP-001/a.md", "projects/app/stories/APP-002/b.md"] if args[0] == "recents" else []
        r = resolve([], root, fake)
        assert r["tier"] == "recent" and r["candidates"][0]["story_id"] == "APP-001", r
        assert resolve([], root, no_obsidian)["tier"] == "none"
    print("ok")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--selftest" in argv:
        selftest()
        sys.exit(0)
    root = Path(".")
    if "--root" in argv:
        i = argv.index("--root")
        root = Path(argv[i + 1])
        del argv[i:i + 2]
    print(json.dumps(resolve(argv, root.resolve()), indent=1))
