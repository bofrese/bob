#!/usr/bin/env python3
"""Short always-on bob primer for projects that use bob. One source for the hook and AGENTS.md.

Usage: primer.py                      print the primer (SessionStart hook); prints nothing outside bob projects
       primer.py --agents-md          report what --apply would change in AGENTS.md and CLAUDE.md
       primer.py --agents-md --apply  write the marked block in AGENTS.md; make CLAUDE.md import it
       primer.py --selftest
Project root: $CLAUDE_PROJECT_DIR, else the current directory. The hook mode never fails: it always exits 0.
"""
import os
import re
import sys
from pathlib import Path

START, END = "<!-- bob:start -->", "<!-- bob:end -->"
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
IMPORT = "@AGENTS.md"
KNOWLEDGE = ["docs/domain", "docs/architecture", "docs/guidelines", "docs/product", "knowledge"]


def uses_bob(root):
    return (root / "docs/process/done-criteria.md").is_file() or any(root.glob("projects/*/_kanban.md")) \
        or (root / "projects/_kanban.md").is_file()


def primer(root):
    """Primer text for root, or "" if the project does not use bob."""
    if not uses_bob(root):
        return ""
    lines = [
        "This repository uses bob, a product development workflow delivered as agent skills.",
        "Engineering or product work here (plan, design, fix, review, implement, product docs) starts with "
        "the `bob` skill's start checklist: it resolves the story, loads project knowledge and names the fitting phase. "
        "The work ends with its finish checklist (story History, done criteria, next step).",
    ]
    found = [f"{k}/" for k in KNOWLEDGE if (root / k).is_dir()]
    if found:
        lines.append("Project knowledge: " + ", ".join(found) + " (read each folder's README.md index first).")
    if (root / "docs/process/done-criteria.md").is_file():
        lines.append("Done criteria: docs/process/done-criteria.md.")
    if (root / "projects").is_dir():
        lines.append("Stories and kanban boards: projects/.")
    return "\n".join(lines)


def agents_block(root):
    return f"{START}\n## bob\n\n{primer(root)}\n{END}"


def sync_agents_md(root, apply):
    """Bring the AGENTS.md block and the CLAUDE.md import up to date. Returns a list of changes."""
    if not uses_bob(root):  # no primer to write yet; never report "up to date" here
        return ["AGENTS.md and CLAUDE.md: pending, written once projects/ or docs/process/done-criteria.md exists"]
    changes = []
    agents, claude = root / "AGENTS.md", root / "CLAUDE.md"
    block = agents_block(root)
    old = agents.read_text(encoding="utf-8") if agents.is_file() else ""
    if BLOCK_RE.search(old):
        new = BLOCK_RE.sub(lambda m: block, old, count=1)
    else:
        new = (old.rstrip("\n") + "\n\n" if old.strip() else "") + block + "\n"
    if new != old:
        changes.append("AGENTS.md: " + ("update bob block" if BLOCK_RE.search(old) else "add bob block"))
        if apply:
            agents.write_text(new, encoding="utf-8")
    text = claude.read_text(encoding="utf-8") if claude.is_file() else None
    if text is None:
        changes.append("CLAUDE.md: create with @AGENTS.md import")
        if apply:
            claude.write_text(IMPORT + "\n", encoding="utf-8")
    elif not re.search(r"^\s*" + re.escape(IMPORT) + r"\s*$", text, re.M):
        changes.append("CLAUDE.md: add @AGENTS.md import")
        if apply:
            claude.write_text(text.rstrip("\n") + "\n\n" + IMPORT + "\n" if text.strip() else IMPORT + "\n",
                              encoding="utf-8")
    return changes


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        assert primer(root) == "" and sync_agents_md(root, True)[0].endswith("exists") and not (root / "AGENTS.md").exists()
        (root / "projects/app").mkdir(parents=True)
        (root / "projects/app/_kanban.md").write_text("x")
        (root / "docs/domain").mkdir(parents=True)
        text = primer(root)
        assert "uses bob" in text and "docs/domain/" in text and "docs/architecture/" not in text, text
        assert "projects/" in text and "done-criteria" not in text and len(text.split()) < 120, text
        (root / "AGENTS.md").write_text("# Agents\n\nKeep me.\n")
        (root / "CLAUDE.md").write_text("# Mine\n")
        assert sync_agents_md(root, False) == ["AGENTS.md: add bob block", "CLAUDE.md: add @AGENTS.md import"]
        assert (root / "AGENTS.md").read_text() == "# Agents\n\nKeep me.\n"
        sync_agents_md(root, True)
        assert sync_agents_md(root, True) == [], "not idempotent"
        (root / "docs/architecture").mkdir()
        (root / "AGENTS.md").write_text((root / "AGENTS.md").read_text() + "\nAfter.\n")
        assert sync_agents_md(root, True) == ["AGENTS.md: update bob block"]
        agents = (root / "AGENTS.md").read_text()
        assert agents.startswith("# Agents\n\nKeep me.\n\n" + START) and agents.endswith(END + "\n\nAfter.\n"), agents
        assert "docs/architecture/" in agents and agents.count(START) == 1
        assert (root / "CLAUDE.md").read_text() == "# Mine\n\n@AGENTS.md\n"
        (root / "CLAUDE.md").unlink()
        assert sync_agents_md(root, True) == ["CLAUDE.md: create with @AGENTS.md import"]
    print("ok")


def main(argv):
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or ".").resolve()
    if "--selftest" in argv:
        selftest()
    elif "--agents-md" in argv:
        for change in sync_agents_md(root, "--apply" in argv) or ["AGENTS.md and CLAUDE.md: up to date"]:
            print(change)
    else:
        try:
            text = primer(root)
            if text:
                print(text)
        except Exception:  # the SessionStart hook must never fail the session
            pass


if __name__ == "__main__":
    main(sys.argv[1:])
