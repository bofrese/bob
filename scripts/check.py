#!/usr/bin/env python3
"""Check bob's structural rules from CLAUDE.md. Prints one line per problem, exits 1 if any.

Usage: python3 scripts/check.py [extra paths to scan for em dashes, e.g. ../docs]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Commands that skip the protocol by design (fast capture, standalone prompt tool).
PROTOCOL_EXEMPT = {"remember", "create-prompt"}
PROTOCOL_LINES = ("bob:context-protocol", "bob:done-criteria")
EM_DASH = "—"
SKIP_DIRS = {".git", "node_modules", "ai"}  # ai/: legacy dated artifacts


def frontmatter(text):
    """Return frontmatter as {key: raw value}, or None if missing or unclosed."""
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    fm = {}
    for line in lines[1:end]:
        m = re.match(r"([A-Za-z][\w-]*):\s*(.*)", line)
        if m:
            fm[m[1]] = m[2]
    return fm


def check_frontmatter(path, required, problems):
    fm = frontmatter(path.read_text())
    rel = path.relative_to(ROOT)
    if fm is None:
        problems.append(f"{rel}: missing or unclosed frontmatter")
        return
    for key in required:
        if not fm.get(key):
            problems.append(f"{rel}: frontmatter lacks '{key}'")
    if "user-invokable" in fm:
        problems.append(f"{rel}: 'user-invokable' is a typo, use 'user-invocable'")
    for key, value in fm.items():
        if ": " in value and value[:1] not in "\"'>|":
            problems.append(f"{rel}: '{key}' value contains ': ' and must be quoted")


def iter_text(base):
    for p in base.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".py", ".sh", ".json"} and not SKIP_DIRS & set(p.parts):
            yield p


def main(extra):
    problems = []
    commands = sorted(ROOT.glob("commands/*.md"))
    skills = sorted(ROOT.glob("skills/*/SKILL.md"))
    catalog_cmds = (ROOT / "skills/bob/references/commands.md").read_text()
    catalog_skills = (ROOT / "skills/bob/references/skills.md").read_text()

    for c in commands:
        check_frontmatter(c, ["description"], problems)
        if c.stem not in PROTOCOL_EXEMPT:
            text = c.read_text()
            for line in PROTOCOL_LINES:
                if line not in text:
                    problems.append(f"{c.relative_to(ROOT)}: missing {line} invocation")
        if f"/bob:{c.stem}`" not in catalog_cmds:
            problems.append(f"{c.relative_to(ROOT)}: not in skills/bob/references/commands.md")

    for s in skills:
        check_frontmatter(s, ["name", "description"], problems)
        if s.parent.name != "bob" and f"`bob:{s.parent.name}`" not in catalog_skills:  # bob is the catalog
            problems.append(f"{s.relative_to(ROOT)}: not in skills/bob/references/skills.md")

    for base in [ROOT, *map(Path, extra)]:
        for p in iter_text(base.resolve()):
            for n, line in enumerate(p.read_text(errors="ignore").split("\n"), 1):
                if EM_DASH in line:
                    problems.append(f"{p}:{n}: em dash")

    print("\n".join(problems) or "ok")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
