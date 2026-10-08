#!/usr/bin/env python3
"""PreToolUse hook: block mv/git mv of .md files in an Obsidian vault when the obsidian CLI exists."""
import json, os, re, shutil, sys, tempfile

MV = re.compile(r"(?:^|[;&|])\s*(?:git\s+mv|mv)\s+[^\n;&|]*\.md\b")
MSG = ("BLOCKED: Moving .md files must go through the Obsidian CLI to preserve wikilinks. "
       "Invoke the bob:obsidian skill.")


def should_block(cmd, project_dir):
    return bool(MV.search(cmd)
                and os.path.isdir(os.path.join(project_dir, ".obsidian"))
                and shutil.which("obsidian"))


def selftest():
    real = shutil.which
    with tempfile.TemporaryDirectory() as d:
        shutil.which = lambda _: None
        assert not should_block("mv a.md b.md", d)  # no vault
        os.mkdir(os.path.join(d, ".obsidian"))
        assert not should_block("mv a.md b.md", d)  # vault, no CLI
        shutil.which = lambda _: "/usr/bin/obsidian"
        assert should_block("mv a.md b.md", d)
        assert should_block("git mv a.md b.md", d)
        assert should_block("cd x && mv a.md b.md", d)
        assert not should_block("rmvx.md", d)
        assert not should_block("echo mv a.md", d)
        assert not should_block("mv a.txt b.txt", d)
    shutil.which = real
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit(0)
    try:
        cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    except Exception:
        sys.exit(0)
    if should_block(cmd, os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()):
        print(MSG, file=sys.stderr)
        sys.exit(2)
