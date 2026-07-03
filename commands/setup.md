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
| Story kanbans          | ✓ / ⚠ N missing Obsidian frontmatter | Repair          |
| _index.md links        | ✓ / ⚠ N missing tasks/notes link     | Repair          |
| _index.md titles       | ✓ / ⚠ N missing title frontmatter    | Repair          |
| Story folder structure | ✓ / ⚠ N missing _notes.md/_kanban.md/tasks/sessions | Repair   |
| Kanban new-line-trigger | ✓ / ⚠ N missing                     | Repair          |
| Session files at story root | ✓ / ⚠ N found                   | Move to sessions/ |
| Orphan .md files       | N found         | Review manually              |
```

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
| Story kanbans | Repaired N / Already correct |
| _index.md links | Repaired N / Already correct |
| _index.md titles | Repaired N / Already correct |
| Story folder structure | Repaired N / Already correct |
| Kanban new-line-trigger | Repaired N / Already correct |
| Session files at story root | Moved N / None found |
| Orphan files | N found (see above) / None |
| Unstructured docs | N found (see above) / None |

List any manual steps remaining (e.g., Obsidian wikilinks setting).

## Rules

- Audit before acting. Never modify without showing the plan first.
- One confirmation covers all changes — don't prompt per item.
- Never overwrite or truncate existing files — only create missing files or append to existing ones.
- Never remove or reorder existing done-criteria sections.
- If `projects/` exists but has no subdirectories, still offer to create the first subproject.
- Skip silently any step where the target already exists and is up to date.

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
