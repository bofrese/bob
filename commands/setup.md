---
allowed-tools: Bash(*), Read, Write, Edit
description: Bootstrap and upgrade bob infrastructure on any project. Idempotent — safe to run on new or existing projects, old or new bob versions.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

You are a project infrastructure specialist. Your job is to make all bob features work correctly — creating what's missing, upgrading what's stale, leaving everything else untouched. Non-destructive by default. One confirmation covers all changes.

## Process

### Step 1 — Audit

Run all checks silently before presenting anything.

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
# Recommended external tool: Ponytail plugin (used by /bob:review for a lean/over-engineering pass)
grep -q '"ponytail@ponytail"' "$HOME/.claude/plugins/installed_plugins.json" 2>/dev/null && echo "ponytail: installed" || echo "ponytail: NOT installed"
# Recommended external tool: Obsidian Skills plugin (authoring skills for Obsidian-flavored markdown/bases/canvas)
grep -q '"obsidian@obsidian-skills"' "$HOME/.claude/plugins/installed_plugins.json" 2>/dev/null && echo "obsidian-skills: installed" || echo "obsidian-skills: NOT installed"

# Recommended external tool: graphify (code knowledge graph - powers bob:code-graph; min version 0.9.11)
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
[ -d website/src ] && echo "b2 website: present" || echo "b2 website: absent"

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

# Unstructured docs: .md files in docs/ but outside bob's known subfolders
find ./docs -name "*.md" \
  -not -path "./docs/product/*" \
  -not -path "./docs/guidelines/*" \
  -not -path "./docs/domain/*" \
  -not -path "./docs/process/*" \
  ! -name "README.md" \
  2>/dev/null
```

### Step 2 — Report and Confirm

Present a concise status table. No changes yet.

```
## Bob Setup — {date}

| Component              | Status          | Action needed               |
|------------------------|-----------------|------------------------------|
| projects/              | ✓ / ✗           | Create subproject            |
| knowledge/ vault       | ✓ / ✗           | Bootstrap                    |
| personal/ notes        | ✓ / ✗           | Create                       |
| .gitignore entries     | ✓ / ⚠ Partial / ✗ | Add missing entries       |
| docs/process/done-criteria.md | ✓ / ⚠ Upgrade / ✗ | Create / Patch        |
| docs/process/learnings.md | ✓ / ✗           | Create (Learn's cross-session staging log) |
| personal/interaction-profile.md | ✓ / ✗ (optional) | Offer to create      |
| Story kanbans          | ✓ / ⚠ N missing Obsidian frontmatter | Repair          |
| _index.md links        | ✓ / ⚠ N missing tasks/notes link     | Repair          |
| _index.md titles       | ✓ / ⚠ N missing title frontmatter    | Repair          |
| Story folder structure | ✓ / ⚠ N missing _notes.md/_kanban.md/tasks/sessions | Repair   |
| Kanban new-line-trigger | ✓ / ⚠ N missing                     | Repair          |
| Session files at story root | ✓ / ⚠ N found                   | Move to sessions/ |
| Orphan .md files       | N found         | Review manually              |
| Ponytail plugin (recommended) | ✓ installed / ✗ not installed | Recommend install |
| Obsidian Skills plugin (recommended) | ✓ installed / ✗ not installed | Recommend install |
| graphify (recommended) | ✓ installed vX.Y.Z / ⚠ below 0.9.11 / ✗ not installed | Recommend install/upgrade |
| graphify graph + hook | ✓ built + hook / ⚠ built, no hook / ✗ not built | Offer build + hook |
| .graphifyignore corpus scope | ✓ current / ⚠ stale / ✗ absent | Write/refresh scope |
```

Recommendations only - never install anything automatically.

**If Ponytail is not installed:** a "lazy senior developer" reviewer that `/bob:review` uses for an over-engineering pass. Install with `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` — more at https://ponytail.dev.

**If Obsidian Skills is not installed:** authoring skills for Obsidian-flavored markdown, Bases, and Canvas — bob is optimized for Obsidian and produces better-formatted notes when it is present. Install with `/plugin marketplace add kepano/obsidian-skills` then `/plugin install obsidian@obsidian-skills`. Note: bob's own `bob:obsidian` skill remains authoritative for vault mutations (rename/move) — its approval-gated workflow takes precedence over the plugin's generic `obsidian-cli` skill.

**If graphify is not installed (or older than 0.9.11):** graphify builds a persistent code knowledge graph that `bob:code-graph` queries so engineering commands orient from real structure instead of blind exploration. It is a separate third-party tool - recommend, never silent-install. Install with `uv tool install graphifyy` (the PyPI package is `graphifyy`, double-y, not a typo); upgrade a too-old copy with `uv tool upgrade graphifyy`. bob requires **>= 0.9.11**. Everything degrades gracefully when it is absent - bob behaves exactly as today.

If everything is ✓: say "All bob infrastructure is present and up to date. Nothing to do." and stop.

Otherwise: list what will change and ask "Ready to apply?" — one confirmation covers everything.

### Step 3 — Bootstrap missing infrastructure

Execute only items marked as missing or partial. Skip items already present.

**projects/ missing:**

Try to derive a subproject name: check `package.json` `.name`, git remote URL, or current directory name. Offer the derived name as a default. Ask: "Subproject name? (default: {derived})"

Create `projects/{name}/stories/` and `projects/{name}/_kanban.md` using the Bootstrap procedure in `bob:project-tracking` (project-level columns, `prefix`, `last-id: "000"`, `new-note-folder`, `new-line-trigger`).

**Story kanbans missing Obsidian frontmatter:**
For each story `_kanban.md` missing `kanban-plugin: board` frontmatter: prepend the frontmatter block (`kanban-plugin: board`, `title: [STORY-ID] Tasks`) and append the `%% kanban:settings %%` block with `new-note-folder` pointing to the story's `tasks/` folder and `new-line-trigger: shift-enter`. Existing column content is preserved.

**`_index.md` files missing tasks/notes link:**
For each story `_index.md` missing the `##### 📋 [Tasks](_kanban.md)` line: insert it after the opening description paragraph.

**`_index.md` files missing title frontmatter:**
For each story `_index.md` missing `title:`: add `title: "[STORY-ID] Story: [Story Name]"` to the frontmatter block, reading the story name from the `# [STORY-ID] - [Story Name]` heading.

**Story folders missing `_notes.md`, `_kanban.md`, `tasks/`, or `sessions/`:**
For each story missing any of these, create the missing pieces using the templates in `bob:project-tracking` (Story Index, `_notes.md`, story-level kanban templates). Never overwrite files that already exist.

**Kanban files missing `new-line-trigger`:**
For each `_kanban.md` whose settings block lacks `new-line-trigger`, add `"new-line-trigger":"shift-enter"` to the existing settings JSON. Preserve all other settings keys.

**Session files at story root:**
For each dated file (`YYYY-MM-DD-*.md`) found directly in a story folder: move it into that story's `sessions/` subfolder (create if missing), then update every link to it — in the story's `_index.md` history table, `_kanban.md` cards, and cross-links between session files — to `sessions/[filename]`.

**knowledge/ missing:**

Locate `library.md` in the same `commands/` folder as this file (the plugin install path is not guaranteed to be `bob/`). Read it and locate the Bootstrap section (steps 1-7). Execute it exactly.

**personal/ missing:**

Create `personal/daily/` and `personal/weekly/`.
Write `personal/scratchpad.md` if it doesn't exist:
```markdown
---
title: Scratchpad
---
# Scratchpad
```

**.gitignore entries missing:**

For each of `knowledge/_INBOX/` and `personal/` not already present in `.gitignore`: append to `.gitignore`.

**graphify corpus scope and provisioning (only when graphify is installed):**

Skip this entire item if `graphify` is not installed - the Step 2 recommendation already covers that case, and there is nothing to consume a scope file yet. If the installed version is below `0.9.11`, print the upgrade recommendation (`uv tool upgrade graphifyy`) and skip the build/hook offers, but still write the scope file below.

1. **Write / refresh `.graphifyignore`** at the project root. This is bob-managed and idempotent: regenerate the block between the managed markers on every run so the scope tracks folders as they come and go; preserve anything the user added outside the markers. `.graphifyignore` uses gitignore semantics (merged with `.gitignore`, `!` negation, last-match-wins), so excluding the historical tiers leaves everything else (code + authoritative content) in the corpus. Add the `website/dist/` line **only when `website/src/` exists** (the b2 website signal) so the generated site does not duplicate its source; never add website lines otherwise (no bob-to-b2 coupling). Content:

   ```gitignore
   # >>> bob:graphify corpus scope (managed by /bob:setup - regenerated on each run) >>>
   # gitignore semantics: merged with .gitignore, ! negates, last-match-wins.
   # A .graphifyinclude allowlist can opt hidden paths back in if ever needed.
   #
   # Corpus tiers:
   #   Code                  - application/source files (kept)
   #   Authoritative content - docs/, knowledge/, website/src/ (kept)
   #   Historical (excluded) - projects/, ai/ (~74% of observed semantic cost, low authority)

   # Historical: excluded
   projects/
   ai/

   # Website: keep src/ as authoritative content, drop the generated build (b2 only)
   website/dist/
   # <<< bob:graphify corpus scope <<<
   ```

2. **Offer to build the graph** - only if `graphify-out/graph.json` does not yet exist. Surface the first-build cost for large corpora ("large repos can be expensive: hundreds of files / millions of words on the first pass"), and note the scope file above already trims the historical tiers. Offer to run `/graphify .` (initial build) and `graphify hook install` (post-commit auto-rebuild so the graph stays fresh). Never run either without confirmation.

3. **Idempotent re-run:** if the graph already exists, do not rebuild. If the hook is missing, offer `graphify hook install`. Always refresh the managed `.graphifyignore` block so the scope stays current as project folders change.

### Step 3b — Bootstrap new skill artifacts (Design/Reflect/Learn rollout)

**`docs/process/learnings.md` missing:** Locate `learn/references/persistence-map.md` in the plugin's `skills/` folder (same parent directory as this file's `commands/` folder). Read its Bootstrap section and create the file exactly as specified there.

**`personal/interaction-profile.md` missing:** This is optional and personal (gitignored) — never auto-create silently. Offer once: "Want a personal interaction-profile file? It lets you set your preferred verbosity/experience-level defaults once instead of restating them per session." If yes, create `personal/` (if missing) and write a minimal starter:
```markdown
---
title: Interaction Profile
---
# Interaction Profile

<!-- Personal, gitignored. Notes on your preferred interaction style — verbosity, question pacing, experience level — read by bob:context-protocol at session start. -->
```
Ensure `personal/` is already covered by the `.gitignore` entries step above.

### Step 4 — Upgrade done-criteria

**Missing:** Create `docs/process/` if needed. Locate `done-criteria/SKILL.md` in the plugin's `skills/` folder (same parent directory as this file's `commands/` folder). Read it and copy the Bootstrap Template (content after the final `---` separator) into `docs/process/done-criteria.md`. Replace `{date}` with today.

**Exists (upgrade path):**

1. Read `docs/process/done-criteria.md`
2. Locate `done-criteria/SKILL.md` in the plugin's `skills/` folder (same parent directory as this file's `commands/` folder). Read it and extract the Bootstrap Template (after the final `---` separator).
3. From the template's `## DONE` block: collect every `### ` section heading and its full content (heading + all lines until the next `### ` or `---`)
4. For each section not found verbatim in the project file: insert it before the `*Last updated:*` footer line
5. Update `*Last updated:*` to today's date
6. Report which sections were added (or "already up to date" if none)

Never remove, reorder, or modify existing sections.

### Step 5 — Unmanaged file report

**Orphan files** (outside all managed locations):
If found: list them. Say: "These files are outside bob's managed locations. To migrate: move them to `knowledge/_INBOX/` manually, then run `/bob:library process` to classify and file them."
If none: skip silently.

**Unstructured docs** (in `docs/` but outside bob's known subfolders):
If found: list them. Say: "These files are in `docs/` but outside bob's structured subfolders. They may be candidates to migrate to `knowledge/` if they contain decisions, concepts, or research. Review manually — no action required."
If none: skip silently.

### Step 6 — Summary

One compact table:

| Item | Result |
|------|--------|
| projects/ | Created `projects/{name}/` / Already present |
| knowledge/ | Bootstrapped / Already present |
| personal/ | Created / Already present |
| .gitignore | Added N entries / Already complete |
| done-criteria | Created / Added N sections: {list} / Already up to date |
| learnings.md | Created / Already present |
| interaction-profile.md | Created / Declined / Already present |
| Story kanbans | Repaired N / Already correct |
| _index.md links | Repaired N / Already correct |
| _index.md titles | Repaired N / Already correct |
| Story folder structure | Repaired N / Already correct |
| Kanban new-line-trigger | Repaired N / Already correct |
| Session files at story root | Moved N / None found |
| Orphan files | N found (see above) / None |
| Unstructured docs | N found (see above) / None |
| Ponytail plugin | Installed / Recommended (not installed) |
| Obsidian Skills plugin | Installed / Recommended (not installed) |
| graphify | Installed vX.Y.Z / Recommended (install or upgrade to >= 0.9.11) |
| graphify graph + hook | Offered build/hook / Already built / N/A (not installed) |
| .graphifyignore corpus scope | Written / Refreshed / Unchanged / N/A (not installed) |

List any manual steps remaining (e.g., Obsidian wikilinks setting).

## Rules

- Audit before acting. Never modify without showing the plan first.
- One confirmation covers all changes — don't prompt per item.
- Never overwrite or truncate existing files - only create missing files or append to existing ones. The one exception is the `.graphifyignore` managed block, which is regenerated between its markers each run; content outside the markers is always preserved.
- Never silent-install third-party tools (graphify, plugins). Recommend and, for graphify, offer to run the build/hook only with explicit confirmation.
- Never remove or reorder existing done-criteria sections.
- If `projects/` exists but has no subdirectories, still offer to create the first subproject.
- Skip silently any step where the target already exists and is up to date.

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
