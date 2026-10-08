#!/usr/bin/env python3
"""Append an operation entry to knowledge/log.md. Creates the file if missing.

Usage: python3 log_append.py <mode> <summary> [log_path]
  mode:     operation mode (process, organise, ingest, etc.)
  summary:  one-line summary of what happened
  log_path: path to log file (default: knowledge/log.md)

Output: prints the appended entry to stdout.
"""
import sys
from datetime import datetime, timezone


def append_entry(mode, summary, log_path="knowledge/log.md"):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f"\n## [{timestamp}] {mode}\n{summary}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)
    print(entry.strip())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: log_append.py <mode> <summary> [log_path]", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    summary = sys.argv[2]
    log_path = sys.argv[3] if len(sys.argv) > 3 else "knowledge/log.md"
    append_entry(mode, summary, log_path)
