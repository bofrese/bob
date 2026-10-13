# Audit

Run every check from the project root, silently, before presenting anything. Script paths are relative to this skill's folder.

```bash
# Infrastructure
ls projects/ 2>/dev/null | head -10
# Story kanbans missing Obsidian frontmatter
find projects -name "_kanban.md" -path "*/stories/*" | xargs grep -rL "kanban-plugin: board" 2>/dev/null
# Story _index.md files missing tasks/notes nav link
find projects -path "*/stories/*/_index.md" | xargs grep -rL "_kanban.md" 2>/dev/null
# Story _index.md files missing title frontmatter
find projects -path "*/stories/*/_index.md" | xargs grep -rL "^title:" 2>/dev/null
# Story folders missing _notes.md, _kanban.md, tasks/, or sessions/
for d in projects/*/stories/*/; do
  [ -f "${d}_notes.md" ] || echo "MISSING _notes.md: $d"
  [ -f "${d}_kanban.md" ] || echo "MISSING _kanban.md: $d"
  [ -d "${d}tasks" ] || echo "MISSING tasks/: $d"
  [ -d "${d}sessions" ] || echo "MISSING sessions/: $d"
done
# Kanban files missing new-line-trigger setting
find projects -name "_kanban.md" | xargs grep -rL "new-line-trigger" 2>/dev/null
# Dated session files sitting at story root instead of sessions/
find projects -regex ".*/stories/[^/]+/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-.*\.md" 2>/dev/null
ls knowledge/README.md 2>/dev/null
ls personal/daily/ 2>/dev/null
grep -c "knowledge/_INBOX/" .gitignore 2>/dev/null || echo 0
grep -c "^personal/" .gitignore 2>/dev/null || echo 0
ls docs/process/done-criteria.md 2>/dev/null
ls docs/process/learnings.md 2>/dev/null
ls personal/interaction-profile.md 2>/dev/null
# Recommended external tool: Ponytail plugin (used by the review skill for a lean/over-engineering pass)
grep -q '"ponytail@ponytail"' "$HOME/.claude/plugins/installed_plugins.json" 2>/dev/null && echo "ponytail: installed" || echo "ponytail: NOT installed"
# Obsidian vault config (bootstrappable from bofrese/obsidian-for-bob)
[ -d .obsidian ] && echo ".obsidian: present" || echo ".obsidian: absent"
# Recommended external tool: Obsidian Skills plugin (authoring skills for Obsidian-flavored markdown/bases/canvas)
grep -q '"obsidian@obsidian-skills"' "$HOME/.claude/plugins/installed_plugins.json" 2>/dev/null && echo "obsidian-skills: installed" || echo "obsidian-skills: NOT installed"

# Recommended external tool: graphify (code knowledge graph - powers the hub's code-graph loader; min version 0.9.11)
if command -v graphify >/dev/null 2>&1; then
  gv=$(graphify --version 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
  echo "graphify: installed ${gv:-unknown}"
  [ -f graphify-out/graph.json ] && echo "graphify graph: built" || echo "graphify graph: NOT built"
  # `graphify hook status` always exits 0, so parse its text, not the exit code
  graphify hook status 2>/dev/null | grep -q 'post-commit: installed' && echo "graphify hook: installed" || echo "graphify hook: not installed"
else
  echo "graphify: NOT installed"
fi
[ -f .graphifyignore ] && echo ".graphifyignore: present" || echo ".graphifyignore: absent"

# Recommended external tool: Mermaid CLI (validates diagrams in bob artifacts before saving)
command -v mmdc >/dev/null 2>&1 && echo "mermaid-cli: installed $(mmdc --version 2>/dev/null)" || echo "mermaid-cli: NOT installed"
[ -d website/src ] && echo "b2 website: present" || echo "b2 website: absent"

# Always-on primer for other agents: AGENTS.md bob block and CLAUDE.md import (dry run)
python3 <skill-dir>/../bob/scripts/primer.py --agents-md
# bob 3.x entry-point names in CLAUDE.md, AGENTS.md, docs/process/*.md, docs/guidelines/ (dry run)
python3 <skill-dir>/scripts/rename_scan.py

# Orphan markdown: .md files outside all managed locations (including docs/)
find . -name "*.md" \
  -not -path "./.git/*" \
  -not -path "./bob/*" \
  -not -path "./projects/*" \
  -not -path "./knowledge/*" \
  -not -path "./personal/*" \
  -not -path "./.obsidian/*" \
  -not -path "./node_modules/*" \
  -not -path "./docs/*" \
  ! -name "README.md" ! -name "CLAUDE.md" ! -name "LICENSE.md" ! -name "CHANGELOG.md" \
  2>/dev/null
```
