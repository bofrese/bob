#!/usr/bin/env python3
"""Create the knowledge vault in the current project. Idempotent: never overwrites a file.

Usage: python3 bootstrap.py [project_root]   (default: current directory)
       python3 bootstrap.py --selftest
Prints one line per created path.
"""
import sys
import tempfile
from datetime import date
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FOLDERS = ["decisions", "concepts", "research", "practices", "_INBOX/_processed", "_MOC", "sources"]
INDEXES = {"decisions": "Decisions", "concepts": "Concepts", "research": "Research", "practices": "Practices"}
GITIGNORE = ["knowledge/_INBOX/", "personal/"]


def write_new(path, text, created):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        created.append(str(path))


def bootstrap(root):
    root, created = Path(root), []
    k = root / "knowledge"
    for f in FOLDERS:
        if not (k / f).is_dir():
            (k / f).mkdir(parents=True)
            created.append(str(k / f))
    asset = lambda n: (ASSETS / n).read_text(encoding="utf-8")
    write_new(k / "_schema.md", asset("_schema.md"), created)
    write_new(k / "README.md", asset("knowledge-readme.md").replace("YYYY-MM-DD", date.today().isoformat()), created)
    write_new(k / "_suggestions.md", asset("_suggestions.md"), created)
    for folder, title in INDEXES.items():
        write_new(k / folder / "_index.md", f"---\ntitle: {title}\n---\n# {title}\n", created)
    gi = root / ".gitignore"
    lines = gi.read_text(encoding="utf-8").splitlines() if gi.exists() else []
    missing = [e for e in GITIGNORE if e not in lines]
    if missing:
        prefix = "\n" if lines and not gi.read_text(encoding="utf-8").endswith("\n") else ""
        with gi.open("a", encoding="utf-8") as f:
            f.write(prefix + "\n".join(missing) + "\n")
        created.append(f".gitignore: {', '.join(missing)}")
    for d in ("personal/daily", "personal/weekly"):
        (root / d).mkdir(parents=True, exist_ok=True)
    write_new(root / "personal/scratchpad.md", asset("scratchpad.md"), created)
    return created


def selftest():
    with tempfile.TemporaryDirectory() as t:
        Path(t, ".gitignore").write_text("node_modules/")
        first = bootstrap(t)
        assert Path(t, "knowledge/_INBOX/_processed").is_dir()
        assert "YYYY" not in Path(t, "knowledge/README.md").read_text()
        assert Path(t, ".gitignore").read_text() == "node_modules/\nknowledge/_INBOX/\npersonal/\n"
        assert Path(t, "knowledge/concepts/_index.md").read_text().startswith("---\ntitle: Concepts")
        assert first and bootstrap(t) == [], "second run must create nothing"
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    for line in bootstrap(sys.argv[1] if len(sys.argv) > 1 else "."):
        print(line)
