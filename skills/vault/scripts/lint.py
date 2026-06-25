#!/usr/bin/env python3
"""Audit vault notes for frontmatter issues and broken internal links.

Usage: python3 lint.py [vault_root]
  vault_root: path to knowledge/ directory (default: knowledge/)

Output: JSON list of issues, one per file.
Each issue: {"file": "...", "issues": ["..."]}
"""
import json
import os
import re
import sys

REQUIRED_FIELDS = {"type", "title", "tags", "timestamp"}
OLD_FIELDS = {"source", "created"}
TYPED_DIRS = {"decisions", "concepts", "research", "patterns"}


def parse_frontmatter(content):
    """Return (frontmatter_dict, body) from markdown content."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 4:]
    fields = {}
    for line in fm_text.splitlines():
        m = re.match(r"^(\w[\w-]*):", line)
        if m:
            fields[m.group(1)] = True
    return fields, body


def find_internal_links(body):
    """Return list of relative markdown link targets from body."""
    return re.findall(r"\[.*?\]\((\.\./[^)]+\.md)\)", body)


def lint_vault(vault_root):
    issues = []
    for dir_name in TYPED_DIRS:
        dir_path = os.path.join(vault_root, dir_name)
        if not os.path.isdir(dir_path):
            continue
        for fname in os.listdir(dir_path):
            if not fname.endswith(".md") or fname.startswith("_"):
                continue
            fpath = os.path.join(dir_path, fname)
            rel_path = os.path.relpath(fpath, os.path.dirname(vault_root))
            with open(fpath, encoding="utf-8") as f:
                content = f.read()
            fields, body = parse_frontmatter(content)
            file_issues = []

            for req in REQUIRED_FIELDS:
                if req not in fields:
                    file_issues.append(f"missing required field: {req}:")

            for old in OLD_FIELDS:
                if old in fields:
                    new = "resource" if old == "source" else "timestamp"
                    file_issues.append(f"old field name: {old}: (should be {new}:)")

            for link_target in find_internal_links(body):
                link_abs = os.path.normpath(os.path.join(dir_path, link_target))
                if not os.path.exists(link_abs):
                    file_issues.append(f"broken link: {link_target}")

            if file_issues:
                issues.append({"file": rel_path, "issues": file_issues})

    return issues


if __name__ == "__main__":
    vault_root = sys.argv[1] if len(sys.argv) > 1 else "knowledge"
    if not os.path.isdir(vault_root):
        print(json.dumps({"error": f"vault not found: {vault_root}"}))
        sys.exit(1)
    result = lint_vault(vault_root)
    print(json.dumps(result, indent=2))
