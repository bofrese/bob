#!/usr/bin/env python3
"""Check bob's structural rules. Prints one line per problem, exits 1 if any.

Usage: python3 scripts/check.py [extra paths to scan for em dashes, e.g. ../docs]
       python3 scripts/check.py --write-readme   (regenerate the skill table in README.md)
Rules: skills/new-skill/references/authoring-rules.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUB = "bob"
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
MAX_DESC = 300
FINISH_LINE = "Finish with the hub's finish checklist."
HUB_REF = re.compile(r"`bob:bob`|`bob` skill|`bob` hub")
# Skills that teach a way of thinking and do not run the hub checklists.
PRINCIPLE = {"architect", "bdd", "ui-design", "obsidian"}
# Quick capture: deliberately skips the hub checklists.
HUB_EXEMPT = PRINCIPLE | {"remember"}
# README skill table groups; anything not listed lands in "Knowledge and meta".
GROUPS = [
    ("Hub", {HUB}),
    ("Engineering phases", {"brainstorm", "design", "plan", "review-plan", "implement", "review", "document",
                            "handover", "reflect", "learn", "investigate", "dev", "ui-review", "explain", "autopilot"}),
    ("Product", {"product", "brand-design", "linkedin"}),
    ("Principles", PRINCIPLE),
]
OTHER = "Knowledge and meta"
README = ROOT / "README.md"
TABLE_RE = re.compile(r"(<!-- skills:start -->\n).*?(<!-- skills:end -->)", re.S)
EM_DASH = chr(0x2014)
SKIP_DIRS = {".git", "node_modules"}


def frontmatter(text):
    """Return frontmatter as {key: value}, or None if missing or unclosed. Folds '>' and '|' blocks."""
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    fm, key, blocks = {}, None, set()
    for line in lines[1:end]:
        m = re.match(r"([A-Za-z][\w-]*):\s*(.*)", line)
        if m:
            key, fm[m[1]] = m[1], m[2]
            if m[2][:1] in (">", "|"):
                blocks.add(key)
                fm[key] = ""
        elif key in blocks and line.startswith(" "):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


def unquoted_colons(text):
    """Top-level frontmatter keys whose plain value contains ': ' (invalid YAML)."""
    head = text.split("\n---", 1)[0]
    return re.findall(r"^([A-Za-z][\w-]*): (?![\"'>|]).*: ", head, re.M)


def check_skill(path, problems):
    rel = path.relative_to(ROOT)
    name = path.parent.name
    text = path.read_text()
    fm = frontmatter(text)
    if fm is None:
        problems.append(f"{rel}: missing or unclosed frontmatter")
        return
    for key in unquoted_colons(text):
        problems.append(f"{rel}: '{key}' value contains ': ' and must be quoted")
    extra = set(fm) - SPEC_KEYS
    if extra:
        problems.append(f"{rel}: non-spec frontmatter keys {sorted(extra)}")
    if fm.get("name") != name or not NAME_RE.fullmatch(name) or len(name) > 64:
        problems.append(f"{rel}: name must equal the folder name, lowercase-hyphenated")
    desc = fm.get("description", "").strip("\"'")
    if not 0 < len(desc) <= MAX_DESC:
        problems.append(f"{rel}: description must be 1-{MAX_DESC} characters, is {len(desc)}")
    if len(text.split("\n")) > 500:
        problems.append(f"{rel}: over 500 lines")
    if name != HUB and name not in HUB_EXEMPT:
        if not HUB_REF.search(text):
            problems.append(f"{rel}: does not invoke the `bob` hub skill")
        if FINISH_LINE not in text:
            problems.append(f"{rel}: lacks the closing line '{FINISH_LINE}'")


def skill_table():
    """Markdown skill table built from the skill frontmatter, grouped."""
    skills = {p.parent.name: (frontmatter(p.read_text()) or {}).get("description", "").strip("\"'")
              for p in ROOT.glob("skills/*/SKILL.md")}
    grouped = [(g, sorted(n for n in skills if n in names)) for g, names in GROUPS]
    listed = {n for _, ns in grouped for n in ns}
    grouped.insert(3, (OTHER, sorted(set(skills) - listed)))
    out = []
    for group, names in grouped:
        out += [f"**{group}**", "", "| Skill | Description |", "|---|---|"]
        out += [f"| `{n}` | {skills[n].replace('|', '/')} |" for n in names] + [""]
    return "\n".join(out)


def readme_with_table(text):
    """text with the generated table between the skills markers, or None if markers are missing."""
    if not TABLE_RE.search(text):
        return None
    return TABLE_RE.sub(lambda m: m[1] + "\n" + skill_table() + "\n" + m[2], text)


def iter_text(base):
    for p in base.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".py", ".sh", ".json"} and not SKIP_DIRS & set(p.parts):
            yield p


def main(extra):
    problems = []
    if (ROOT / "commands").exists():
        problems.append("commands/: bob ships skills only")
    for d in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        if not (d / "SKILL.md").exists():
            problems.append(f"skills/{d.name}: folder without SKILL.md")
    for s in sorted(ROOT.glob("skills/*/SKILL.md")):
        check_skill(s, problems)

    text = README.read_text()
    fresh = readme_with_table(text)
    if fresh is None:
        problems.append("README.md: missing <!-- skills:start --> / <!-- skills:end --> markers")
    elif fresh != text:
        problems.append("README.md: skill table is stale, run: python3 scripts/check.py --write-readme")

    for base in [ROOT, *map(Path, extra)]:
        for p in iter_text(base.resolve()):
            for n, line in enumerate(p.read_text(errors="ignore").split("\n"), 1):
                if EM_DASH in line:
                    problems.append(f"{p}:{n}: em dash")

    print("\n".join(problems) or "ok")
    return 1 if problems else 0


def selftest():
    fm = frontmatter("---\nname: x\ndescription: >\n  Folded: text\n  more\nmetadata:\n  a: b\n---\nbody")
    assert fm == {"name": "x", "description": "Folded: text more", "metadata": ""}, fm
    assert unquoted_colons("---\nname: x\ndescription: a: b\nother: \"a: b\"\n---") == ["description"]
    assert frontmatter("no frontmatter") is None and frontmatter("---\nname: x") is None
    t = readme_with_table("a\n<!-- skills:start -->\nSTALE\n<!-- skills:end -->\nb")
    assert t.startswith("a\n<!-- skills:start -->\n\n**Hub**") and t.endswith("<!-- skills:end -->\nb") and "STALE" not in t
    assert readme_with_table(t) == t and readme_with_table("none") is None
    assert "| `bob` |" in t and "**Principles**" in t and "**Knowledge and meta**" in t
    print("ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--write-readme" in sys.argv:
        new = readme_with_table(README.read_text())
        if new is None:
            sys.exit("README.md: missing skills markers")
        README.write_text(new)
        sys.exit(0)
    sys.exit(main(sys.argv[1:]))
