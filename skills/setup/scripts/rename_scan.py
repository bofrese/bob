#!/usr/bin/env python3
"""Find bob 3.x entry-point names (`/bob:<name>`, `bob:<name>`) that no longer exist, and their replacements.

Usage: rename_scan.py [--fix] [--root DIR] | rename_scan.py --selftest
Scans CLAUDE.md, AGENTS.md, docs/process/*.md and docs/guidelines/**/*.md under the project root (default: cwd).
Prints one line per hit: file:line: old -> new. --fix rewrites only hits with a replacement.
"""
import re
import sys
from pathlib import Path

SKILLS = {p.name for p in Path(__file__).resolve().parents[2].iterdir() if (p / "SKILL.md").is_file()}
RENAMES = {
    **dict.fromkeys(["product-coach", "product-vision", "personas", "problem-space", "validation-plan",
                     "business-plan", "positioning", "assumption-testing", "business-model", "go-to-market",
                     "positioning-strategy", "problem-validation"], "product"),
    **dict.fromkeys(["design-brief", "art-director"], "brand-design"),
    **dict.fromkeys(["pm", "context-protocol", "story-context", "writing", "knowledge", "code-graph",
                     "done-criteria", "work-routing", "project-tracking", "domain-knowledge"], "bob"),
    "new-command": "new-skill", "review-command": "review-skill", "prompt-engineering": "new-skill",
    "improve-command": "learn", "design-signals": "implement", "linkedin-expert": "linkedin", "vault": "library",
}
NAME_RE = re.compile(r"(?<![\w-])(/?bob:)([a-z0-9]+(?:-[a-z0-9]+)*)(?![\w-])")
GLOBS = ["CLAUDE.md", "AGENTS.md", "docs/process/*.md", "docs/guidelines/**/*.md"]


def files(root):
    return sorted({p for g in GLOBS for p in root.glob(g) if p.is_file()})


def hits(text):
    """(line number, old, new or None) for each stale name in text."""
    found = []
    for n, line in enumerate(text.splitlines(), 1):
        for m in NAME_RE.finditer(line):
            if m[2] not in SKILLS:
                new = RENAMES.get(m[2])
                found.append((n, m[0], m[1] + new if new else None))
    return found


def fix(text):
    def sub(m):
        new = RENAMES.get(m[2]) if m[2] not in SKILLS else None
        return m[1] + new if new else m[0]
    return NAME_RE.sub(sub, text)


def scan(root, apply=False):
    lines = []
    for path in files(root):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for n, old, new in hits(text):
            lines.append(f"{rel}:{n}: {old} -> {new or '(no replacement, fix by hand)'}")
        if apply and fix(text) != text:
            path.write_text(fix(text), encoding="utf-8")
    return lines


def selftest():
    import tempfile
    assert {"plan", "product", "bob", "library"} <= SKILLS, SKILLS
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "docs/guidelines/lang").mkdir(parents=True)
        (root / "docs/other").mkdir(parents=True)
        (root / "CLAUDE.md").write_text("Run /bob:product-coach, then /bob:plan.\nUse bob:context-protocol and /bob:create-prompt.\n")
        (root / "docs/guidelines/lang/x.md").write_text("See `bob:vault` and /bob:pm-tools.\n")
        (root / "docs/other/y.md").write_text("/bob:pm\n")
        assert scan(root) == [
            "CLAUDE.md:1: /bob:product-coach -> /bob:product",
            "CLAUDE.md:2: bob:context-protocol -> bob:bob",
            "CLAUDE.md:2: /bob:create-prompt -> (no replacement, fix by hand)",
            "docs/guidelines/lang/x.md:1: bob:vault -> bob:library",
            "docs/guidelines/lang/x.md:1: /bob:pm-tools -> (no replacement, fix by hand)",
        ], scan(root)
        scan(root, apply=True)
        assert (root / "CLAUDE.md").read_text() == "Run /bob:product, then /bob:plan.\nUse bob:bob and /bob:create-prompt.\n"
        assert len(scan(root)) == 2 and (root / "docs/other/y.md").read_text() == "/bob:pm\n"
    print("ok")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--selftest" in argv:
        selftest()
        sys.exit(0)
    root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else Path(".")
    result = scan(root.resolve(), apply="--fix" in argv)
    print("\n".join(result) if result else "No old bob names found.")
