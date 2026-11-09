#!/usr/bin/env python3
"""Checks for explainer pages in docs/explainers/.

Usage:
  explainer.py check <page.html>   structural checks; prints problems, exit 1 if any
  explainer.py stale <page.html>   outline sources changed since the outline's commit
  explainer.py --selftest
"""
import re
import subprocess
import sys
from pathlib import Path

EM_DASH = chr(0x2014)


def outline(html):
    """Return the outline block as a dict, or None. Repeated keys (source) become lists."""
    m = re.search(r"<!--\s*explainer\b(.*?)-->", html, re.S)
    if not m:
        return None
    fields = {"source": []}
    for line in m.group(1).splitlines():
        k, sep, v = line.strip().partition(":")
        if not sep or not v.strip():
            continue
        k, v = k.strip().lower(), v.strip()
        if k == "source":
            fields["source"].append(v)
        else:
            fields.setdefault(k, v)
    return fields


def problems(html, page_name, index_html):
    out = []
    o = outline(html)
    if o is None:
        out.append("no <!-- explainer ... --> outline block")
    else:
        for key in ("goal", "commit", "date"):
            if key not in o:
                out.append(f"outline block has no '{key}:'")
        if not o["source"]:
            out.append("outline block has no 'source:' line")
    if "not a source of truth" not in html.lower():
        out.append("no 'not a source of truth' banner")
    # Self-contained: the page must open offline and survive library changes.
    external = re.findall(r"""<(?:script|link|img|iframe)[^>]+(?:src|href)\s*=\s*["']((?:https?:)?//[^"']+)""", html, re.I)
    external += re.findall(r"""@import\s+(?:url\()?["']?((?:https?:)?//[^"')]+)""", html, re.I)
    for url in external:
        out.append(f"external resource: {url}")
    if EM_DASH in html:
        out.append("contains an em dash")
    if index_html is None:
        out.append("docs/explainers/index.html is missing")
    elif page_name not in index_html:
        out.append(f"no card for {page_name} in index.html")
    return out


def sources_changed(sources, commit, git=None):
    """Repository sources changed since commit. URLs are skipped."""
    git = git or (lambda args: subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout)
    files = [s for s in sources if not re.match(r"https?://", s)]
    if not files:
        return []
    changed = git(["diff", "--name-only", f"{commit}..HEAD", "--", *files]).split()
    changed += git(["diff", "--name-only", "HEAD", "--", *files]).split()
    return sorted(set(changed))


def selftest():
    good = """<html><head><!-- explainer
goal: Understand sync.
commit: abc123
date: 2026-10-27
core ideas:
1. plan is pure.
   source: app/Manager.swift
   source: https://example.org/paper
--></head><body><p>Not a source of truth.</p><script>let x=1</script></body></html>"""
    o = outline(good)
    assert o["commit"] == "abc123" and o["source"] == ["app/Manager.swift", "https://example.org/paper"]
    assert problems(good, "sync.html", '<a href="sync.html">') == []
    bad = good.replace("Not a source of truth.", "Hi" + EM_DASH) + '<script src="https://cdn.x/lib.js"></script>'
    p = problems(bad, "sync.html", "")
    assert any("banner" in x for x in p) and any("em dash" in x for x in p)
    assert any("external resource" in x for x in p) and any("no card" in x for x in p)
    assert problems("<html></html>", "a.html", None)[0].startswith("no <!-- explainer")
    calls = []
    fake = lambda args: (calls.append(args), "app/Manager.swift\n")[1]
    assert sources_changed(o["source"], "abc123", fake) == ["app/Manager.swift"]
    assert all("https://example.org/paper" not in c for c in calls)
    assert sources_changed(["https://x.org"], "abc123", fake) == []
    print("ok")


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) != 3 or argv[1] not in ("check", "stale"):
        sys.exit(__doc__)
    page = Path(argv[2])
    html = page.read_text(encoding="utf-8")
    if argv[1] == "check":
        index = page.parent / "index.html"
        index_html = index.read_text(encoding="utf-8") if index.exists() and index != page else None
        found = problems(html, page.name, index_html)
        print("\n".join(found) or "ok")
        sys.exit(1 if found else 0)
    o = outline(html)
    if not o or "commit" not in o:
        sys.exit("no outline block with a commit")
    print("\n".join(sources_changed(o["source"], o["commit"])) or "current")


if __name__ == "__main__":
    main(sys.argv)
