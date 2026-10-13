#!/usr/bin/env python3
"""Move or rename one .md file and keep relative markdown links to and from it intact.

Fallback for when the Obsidian app is not running this project as the active vault.
Usage: md_move.py <from.md> <to.md | to-folder/> [--dry-run]
       md_move.py --selftest
Paths are relative to the project root ($CLAUDE_PROJECT_DIR, else the current directory).
ponytail: rewrites [text](relative/path.md) links only, not [[wikilinks]] (bob writes markdown links); single files, not folders.
"""
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote, unquote

LINK = re.compile(r"(\]\()([^)\s]+)")
SKIP = {".git", ".obsidian", "node_modules"}


def relative(target):
    return not (target.startswith(("#", "/", "<")) or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I))


def rewrite(text, old_dir, new_dir, mapping):
    """Re-point relative links in text written at old_dir so they work from new_dir; mapping redirects moved files."""
    def sub(m):
        target = m.group(2)
        if not relative(target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = os.path.normpath(os.path.join(old_dir, unquote(path)))
        if old_dir == new_dir and resolved not in mapping:
            return m.group(0)
        new = os.path.relpath(mapping.get(resolved, resolved), new_dir)
        if "%20" in path:
            new = quote(new)
        return m.group(1) + new + ("#" + anchor if anchor else "")
    return LINK.sub(sub, text)


def plan(root, src, dst):
    """Return {path: new_text} for every file whose links change, with the moved file keyed by dst."""
    src_abs, dst_abs = str((root / src).resolve()), str((root / dst).resolve())
    mapping = {src_abs: dst_abs}
    edits = {}
    for f in root.rglob("*.md"):
        if SKIP & set(f.relative_to(root).parts):
            continue
        fa = str(f.resolve())
        text = f.read_text(encoding="utf-8")
        if fa == src_abs:
            edits[dst_abs] = rewrite(text, os.path.dirname(fa), os.path.dirname(dst_abs), mapping)
        else:
            new = rewrite(text, os.path.dirname(fa), os.path.dirname(fa), mapping)
            if new != text:
                edits[fa] = new
    return src_abs, dst_abs, edits


def move(root, src, dst, dry_run=False):
    if dst.endswith("/") or (root / dst).is_dir():
        dst = str(Path(dst) / Path(src).name)
    if not (root / src).is_file():
        sys.exit(f"not a file: {src}")
    if (root / dst).exists():
        sys.exit(f"already exists: {dst}")
    src_abs, dst_abs, edits = plan(root, src, dst)
    others = sorted(os.path.relpath(p, root) for p in edits if p != dst_abs)
    print(f"{'would move' if dry_run else 'moved'}: {src} -> {dst}")
    print(f"links updated in {len(others)} file(s)" + "".join(f"\n  {p}" for p in others))
    if dry_run:
        return
    Path(dst_abs).parent.mkdir(parents=True, exist_ok=True)
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", src_abs], cwd=root,
                             capture_output=True).returncode == 0
    if tracked:
        subprocess.run(["git", "mv", src_abs, dst_abs], cwd=root, check=True)
    else:
        os.rename(src_abs, dst_abs)
    for path, text in edits.items():
        Path(path).write_text(text, encoding="utf-8")


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        root = Path(t).resolve()
        (root / "a").mkdir()
        (root / "a/note.md").write_text("[up](../index.md) [web](https://x.io/a.md) [self](#top) [s](../b/s.md#h)")
        (root / "index.md").write_text("[n](a/note.md) [n2](a/note.md#sec) [other](a/other.md)")
        (root / "a/other.md").write_text("[n](note.md)")
        move(root, "a/note.md", "b/c/", dry_run=True)
        assert (root / "a/note.md").exists()
        move(root, "a/note.md", "b/c/")
        assert not (root / "a/note.md").exists()
        assert (root / "b/c/note.md").read_text() == \
            "[up](../../index.md) [web](https://x.io/a.md) [self](#top) [s](../s.md#h)"
        assert (root / "index.md").read_text() == "[n](b/c/note.md) [n2](b/c/note.md#sec) [other](a/other.md)"
        assert (root / "a/other.md").read_text() == "[n](../b/c/note.md)"
        move(root, "b/c/note.md", "b/c/renamed.md")
        assert (root / "index.md").read_text().startswith("[n](b/c/renamed.md)")
    print("selftest ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--selftest" in args:
        selftest()
    elif len([a for a in args if not a.startswith("--")]) == 2:
        src, dst = [a for a in args if not a.startswith("--")]
        move(Path(os.environ.get("CLAUDE_PROJECT_DIR") or ".").resolve(), src, dst, "--dry-run" in args)
    else:
        sys.exit(__doc__)
