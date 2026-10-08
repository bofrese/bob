#!/usr/bin/env python3
"""Return vault notes changed since a given date, via git log + untracked files.

Usage: python3 git_scope.py [since_date] [vault_dir]
  since_date: ISO date string, e.g. 2026-06-18T10:45:00Z (optional)
              If omitted or log.md missing, returns all notes in vault_dir.
  vault_dir:  path to vault directory (default: knowledge)

Falls back to all notes when since_date is not provided.
Supplements git log with git status --porcelain to catch untracked files.

Output: newline-delimited list of relative file paths.
"""
import os
import subprocess
import sys


def get_all_notes(vault_dir):
    notes = []
    for root, _, files in os.walk(vault_dir):
        for f in files:
            if f.endswith(".md"):
                notes.append(os.path.relpath(os.path.join(root, f)))
    return notes


def get_changed_notes(since_date, vault_dir):
    changed = set()

    # Committed changes via git log
    try:
        result = subprocess.run(
            ["git", "log", f"--since={since_date}", "--name-only", "--pretty=format:", "--", vault_dir],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            line = line.strip()
            if line.endswith(".md"):
                changed.add(line)
    except subprocess.CalledProcessError:
        pass

    # Untracked and modified files via git status
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", vault_dir],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            status = line[:2].strip()
            path = line[3:].strip()
            if path.endswith(".md") and status in {"?", "M", "A", "??"}:
                changed.add(path)
    except subprocess.CalledProcessError:
        pass

    return sorted(changed)


if __name__ == "__main__":
    since_date = sys.argv[1] if len(sys.argv) > 1 else None
    vault_dir = sys.argv[2] if len(sys.argv) > 2 else "knowledge"

    if not since_date:
        notes = get_all_notes(vault_dir)
    else:
        notes = get_changed_notes(since_date, vault_dir)
        if not notes:
            notes = []

    for note in notes:
        print(note)
