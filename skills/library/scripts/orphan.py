#!/usr/bin/env python3
"""Find vault notes with no inbound links from other vault notes.

Usage: python3 orphan.py [vault_root]
       python3 orphan.py --selftest
  vault_root: path to knowledge/ directory (default: knowledge/)

Output: JSON list of {"file": "...", "title": "..."} for orphaned notes.
"""
import json
import os
import re
import sys

TYPED_DIRS = {"decisions", "concepts", "research", "practices"}


def collect_notes(vault_root):
    """Return dict: rel_path -> absolute_path for all typed notes."""
    notes = {}
    for dir_name in TYPED_DIRS:
        dir_path = os.path.join(vault_root, dir_name)
        if not os.path.isdir(dir_path):
            continue
        for fname in os.listdir(dir_path):
            if fname.endswith(".md") and not fname.startswith("_"):
                abs_path = os.path.join(dir_path, fname)
                rel_path = os.path.relpath(abs_path)
                notes[rel_path] = abs_path
    return notes


def extract_title(content):
    m = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
    return m.group(1).strip() if m else ""


def find_link_targets(content, source_dir):
    """Return set of normalised absolute paths referenced by relative markdown links."""
    targets = set()
    for link in re.findall(r"\[.*?\]\((\.\./[^)]+\.md)\)", content):
        abs_target = os.path.normpath(os.path.join(source_dir, link))
        targets.add(os.path.relpath(abs_target))
    return targets


def find_orphans(vault_root):
    notes = collect_notes(vault_root)
    inbound = {rel: 0 for rel in notes}

    for rel_path, abs_path in notes.items():
        source_dir = os.path.dirname(abs_path)
        with open(abs_path, encoding="utf-8") as f:
            content = f.read()
        for target in find_link_targets(content, source_dir):
            if target in inbound:
                inbound[target] += 1

    orphans = []
    for rel_path, count in inbound.items():
        if count == 0:
            with open(notes[rel_path], encoding="utf-8") as f:
                content = f.read()
            orphans.append({"file": rel_path, "title": extract_title(content)})

    return sorted(orphans, key=lambda x: x["file"])


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            os.makedirs("knowledge/concepts")
            with open("knowledge/concepts/a.md", "w") as f:
                f.write("---\ntitle: A\n---\n[b](../concepts/b.md)\n")
            with open("knowledge/concepts/b.md", "w") as f:
                f.write("---\ntitle: B\n---\n")
            assert find_orphans("knowledge") == [{"file": os.path.join("knowledge", "concepts", "a.md"), "title": "A"}]
        finally:
            os.chdir(cwd)
    print("ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit(0)
    vault_root = sys.argv[1] if len(sys.argv) > 1 else "knowledge"
    if not os.path.isdir(vault_root):
        print(json.dumps({"error": f"vault not found: {vault_root}"}))
        sys.exit(1)
    result = find_orphans(vault_root)
    print(json.dumps(result, indent=2))
