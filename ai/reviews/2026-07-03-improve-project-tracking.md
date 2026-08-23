# Command Improvement: Project Tracking System
**Date:** 2026-07-03
**Session Context:** Audit of `bob:project-tracking`, `bob:story-context`, `bob:done-criteria`, and the 7 engineering commands that write story artifacts, followed by migration of `projects/bob/` to the corrected structure.

## Current Command Assessment

`bob:project-tracking` already documented most of the target structure correctly (task file template, story-for-existing-work procedure, INBOX conversion), but three things had drifted: no `title` frontmatter on `_index.md`/`_notes.md` (Obsidian's navigator fell back to filename), a `sessions/` subfolder drawn in the file-structure diagram but never actually used by any command, and no kanban settings standard for `new-line-trigger`. Real data confirmed the drift: 3 of 6 stories were missing `_kanban.md`/`_notes.md`/`tasks/` entirely, and BOB-001 had a stray `tasks/_notes.md` — Obsidian was silently resolving the `_notes.md` link in `_index.md` to the wrong file, exactly the failure mode `project-tracking`'s own "No Dangling Links" rule warns against. This bug was already self-reported in BOB-001's Issues column but not yet fixed.

## Proposed Improvements

### 1. Session artifacts were never actually routed to `sessions/`

**Issue:** The file-structure diagram in `project-tracking/SKILL.md` showed a `sessions/` folder, but `brainstorm.md`, `plan.md`, `review.md`, `review-plan.md`, `implement.md`, `investigate.md`, and `ui-review.md` all wrote directly to `{story_path}/{date}-{type}-{slug}.md`. Every story had its dated session files sitting at the story root.

**Change applied:**
- All 7 commands: `{story_path}/{date}-{type}-{slug}.md` → `{story_path}/sessions/{date}-{type}-{slug}.md`
- `review.md` and `implement.md` glob lookups (`ls -t "${story_path}"*-plan-*.md`, prior `*-review-*`/`*-implement-*` scans) now search `{story_path}sessions/`
- `done-criteria` Behaviour 7 history-row template: `{filename}` is now `sessions/[artifact-filename]`
- `bob/CLAUDE.md` Output Locations table and `project-tracking/SKILL.md` History table example updated to match

**Rationale:** Keeps the story root readable (just `_index.md`, `_notes.md`, `_kanban.md`, `tasks/`, `sessions/`) instead of accumulating a flat pile of dated files.

---

### 2. No `title` frontmatter on `_index.md` / `_notes.md`

**Issue:** Obsidian's navigator is configured to show frontmatter `title` instead of filename. `_index.md` and `_notes.md` had none — every story showed as "_index" / "_notes" in the sidebar, indistinguishable from each other.

**Change applied:** Story Index template now includes `title: "[STORY-ID] Story: [Story Name]"`. `_notes.md` template now includes `title: "[STORY-ID] Developer Notes"` plus a matching H1. Both templates and the "Naming Conventions" / rules sections in `project-tracking/SKILL.md` updated.

**Rationale:** Directly requested; also fixes a real usability problem (indistinguishable files in Obsidian's nav).

---

### 3. Kanban settings block was inconsistent

**Issue:** No documented requirement for `new-line-trigger`. Without it, pressing Enter inside a kanban card in Obsidian creates a new card instead of a newline — a real Obsidian UX bug, not cosmetic. Story-level kanban titles were also inconsistent (`BOB-001 Tasks` vs. full story name on BOB-002).

**Change applied:** `project-tracking/SKILL.md` and `kanban-syntax.md` now mandate `new-line-trigger: shift-enter` on every kanban settings block, and `title: [STORY-ID] Tasks` as the standard story-kanban title.

---

### 4. New-story creation didn't reliably create all required files together

**Issue:** "Converting INBOX to Story" was an 8-step list but nothing enforced atomicity — in practice, 3 of 6 real stories had only `_index.md` and no `_kanban.md`/`_notes.md`/`tasks/`.

**Change applied:** Added an explicit closing line to the procedure: all pieces are created in the same operation as the story directory, never deferred. `setup.md`'s audit step gained checks for missing `_notes.md`/`_kanban.md`/`tasks/`/`sessions/` per story folder, plus a repair step, so drift self-heals on the next `/bob:setup` run.

---

### 5. `setup.md`'s project-kanban bootstrap template was stale

**Issue:** It hardcoded a minimal 4-column kanban with no `prefix`/`last-id`, while `project-tracking`'s own Bootstrap section (and every real project kanban) uses 8 columns plus `prefix`/`last-id` frontmatter. Two sources of truth for the same template, one of them wrong.

**Change applied:** `setup.md` now delegates to `project-tracking`'s Bootstrap procedure instead of embedding its own template.

## Changes Summary
- [x] `bob/skills/project-tracking/SKILL.md` — templates, procedures — added `title` frontmatter, `sessions/` routing, `new-line-trigger` requirement
- [x] `bob/skills/project-tracking/references/kanban-syntax.md` — templates — aligned with SKILL.md, added missing `_kanban.md`/project templates
- [x] `bob/skills/done-criteria/SKILL.md` — Behaviour 7 — filename now `sessions/[filename]`
- [x] `bob/skills/story-context/SKILL.md` — output block note — clarified session artifacts live under `sessions/`
- [x] `bob/commands/{brainstorm,plan,review,review-plan,implement,investigate,ui-review}.md` — output paths — route to `sessions/`
- [x] `bob/commands/setup.md` — audit/repair — added checks + repairs for title/notes/kanban/sessions drift; delegated bootstrap template to project-tracking
- [x] `bob/CLAUDE.md` — Output Locations table — updated
- [x] `projects/bob/stories/BOB-001..006` — data migration — title frontmatter added to all `_index.md`/`_notes.md`; dated files moved to `sessions/` (BOB-001, BOB-002, BOB-004); missing `_notes.md`/`_kanban.md`/`tasks/`/`sessions/` backfilled (BOB-001, BOB-003, BOB-004, BOB-005, BOB-006); stray `BOB-001/tasks/_notes.md` moved to story root; kanban settings standardized

## Validation
- [x] Generic (applies to any project/language/stack) — all skill/command changes are structural, no bob-specific content
- [x] High-signal (meaningfully changes AI behavior) — fixes a real dangling-link bug and closes a documented-but-unimplemented gap
- [x] Follows prompt engineering principles — no new aggressive language, changes are surgical edits to existing templates
- [x] Preserves command focus and simplicity — no new commands or skills added; extended existing procedures

## Notes
Moves were done via the Obsidian CLI (`obsidian move`); its link-rewriting handled every standard markdown link automatically (history tables, kanban cards, task cross-links) — no manual link repair was needed, contrary to the `bob:obsidian` skill's caveat that only wikilinks are auto-updated. Worth re-verifying this on a future session in case it was a version-specific behavior.

BOB-003, BOB-005, BOB-006 are still `ToDo` (unstarted) — their `tasks/` and `sessions/` folders are empty and won't appear in git until a file lands in them.
