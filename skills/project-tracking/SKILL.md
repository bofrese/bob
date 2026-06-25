---
name: project-tracking
description: This skill should be used when working on any project story or task that involves creating, updating, or referencing project management files. Triggers when: creating or updating a kanban board, adding tasks to a story, moving a task to "in progress" or "done", logging review findings from a plan-review or code-review, creating a new story, or when any other bob skill (brainstorm, plan, implement, review) produces output that should be captured in the project tracking system.
version: 0.3.0
---

# Project Tracking

Provides the rules for how projects, stories, and tasks are tracked using Obsidian kanban boards and linked markdown files. All other bob skills (brainstorm, plan, review, implement) produce content — this skill governs where and how that content is recorded and linked.

## File Structure

```
projects/
├── _index.md                          # Lists all projects
├── [PROJECT]/
│   ├── _kanban.md                     # Project-level kanban (stories as cards)
│   ├── archive/done/ and archive/dismissed/
│   └── stories/
│       └── [STORY-ID]/
│           ├── _index.md              # Story hub — context doc + history table
│           ├── _notes.md              # Developer notes (heading only — grows organically)
│           ├── _kanban.md             # Task-level kanban (tasks + issues)
│           └── tasks/                 # One .md file per task (linked from _kanban.md)
```

## Kanban Format

Kanban files use Obsidian kanban-plugin frontmatter:

```markdown
---
kanban-plugin: board
title: [Board Title]
---

## Column Name
- [ ] Card text
- [x] Completed card

%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"projects/[PROJECT]/stories"}
```
%%
```

### Project-Level Kanban Columns (`_kanban.md` at project root)

| Column | Used for |
|--------|----------|
| `INBOX` | Uncommitted input — ideas and captured work not yet sized, scoped, or decided on. Cards here are candidates, not commitments. |
| `ToDo` | Committed stories, not yet started — the user has decided to do this work |
| `Refining` | Stories being designed, planned, or scoped |
| `Ready` | Stories with a reviewed plan, ready to implement |
| `In Progress` | Stories actively being worked on |
| `Verify` | Implementation complete, awaiting verification |
| `Done` | Completed stories |
| `ARCHIVE` | Dismissed or deferred stories |

### Story-Level Kanban Columns (`_kanban.md` inside story folder)

| Column | Used for |
|--------|----------|
| `Issues` | Discovered bugs, problems, and open questions for this story |
| `todo` | Planned tasks not yet started |
| `Ready` | Tasks ready to start |
| `in progress` | Tasks actively being worked on |
| `Verify` | Tasks complete, awaiting verification |
| `done` | Completed tasks |

## Task Kanban (`_kanban.md` in story folder)

The `new-note-folder` setting must point to the story's `tasks/` folder so that cards added manually in Obsidian create files in the right place. Use the vault-root-relative path:

```markdown
%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"projects/[PROJECT]/stories/[STORY-ID]/tasks"}
```
%%
```

## Task Cards

Tasks in `_kanban.md` are Markdown checkbox links pointing to a file in `tasks/`:

```markdown
## todo
- [ ] [Short task title](tasks/short-task-title.md)
```

Each `tasks/[name].md` file holds the full detail. The card in the kanban is just the title and link — never inline detail.

Issues in the `Issues` column are plain checkboxes (no task file needed for brief items):

```markdown
## Issues
- [ ] Brief description of the problem
```

Priority emoji prefix on issue and review-finding cards:

| Emoji | Severity |
|-------|----------|
| 🔴 | Critical — must fix before ship |
| 🟡 | Important — fix soon |
| 🟢 | Suggestion — nice to have |

Example:
```markdown
## Issues
- [ ] 🔴 Fix daily nudge cancellation logic — see investigation report
- [ ] 🟡 Replace typeID string literals with enum
- [ ] 🟢 Extract threshold constants
```

## Task File Template

Every `tasks/[name].md` file follows this structure:

```markdown
---
status: todo
---
# [Task title]

[One sentence: what this task achieves and why it matters]

## Context
[Link to investigation, plan, or related doc — omit section if none]

## Acceptance Criteria
- [ ] [Specific, verifiable condition]
- [ ] [Specific, verifiable condition]

## Notes
[Optional: approach, code references (file:line), open questions]
```

For bug tasks, replace `## Notes` with explicit sections:

```markdown
## Problem
[What goes wrong and when]

## Root Cause
[Exact mechanism — file, line, why it fails]

## Solution
[Specific changes required, with code references]

## Acceptance Criteria
- [ ] ...

## Code References
| File | Location | Role |
|------|----------|------|
| `Path/File.swift` | line 42 | Where the bug lives |
```

Rules:
- `status` frontmatter: `todo`, `in progress`, or `done`
- Acceptance criteria are checkboxes — testable, not vague
- Code references use `File.swift:line` format
- Never leave placeholder text or TODOs in the file body

## Story Index (`_index.md`)

The `_index.md` is the story hub and context document. It must be readable standalone — a future AI or developer should be able to load it and understand the full story without reading the conversation that created it.

```markdown
---
id: [STORY-ID]
status: [backlog|in progress|done]
domain: [Area/Feature]
started: YYYY-MM-DD
---
# [STORY-ID] - [Story Name]

> [One paragraph: what the story is, why it matters, current state and any known blockers]

##### 📋 [Tasks](_kanban.md)  📘 [Notes](_notes.md)

## History

| Date | Type | Summary | Outcome |
|------|------|---------|---------|
| YYYY-MM-DD | [Brainstorm](file.md) | What was explored | Decision |
| YYYY-MM-DD | [Plan](file.md) | What was planned | Ready / Draft |
| YYYY-MM-DD | [Implementation](file.md) | What was built | Completed |
| YYYY-MM-DD | [Investigation](file.md) | What was investigated | Root cause identified |
| YYYY-MM-DD | [Code Review](file.md) | What was reviewed | Approved with concerns |

---

## Related Documents

- [link](relative/path)
```

Rules:
- The tasks/notes navigation line is required in every story index: `##### 📋 [Tasks](_kanban.md)  📘 [Notes](_notes.md)`. Place it immediately after the opening description paragraph, before `## History`.
- History rows are maintained automatically by done-criteria step 6. Do not add them manually except when bootstrapping a story for existing work.
- Type column links to the document; Outcome column summarizes the result, not the content
- Do NOT add an Open Issues or Open Questions table — those belong in `_kanban.md` Issues column
- The description blockquote must reflect current state; update it when blockers are resolved

## `_notes.md` Template

```markdown
# Developer notes
```

That's it — just the heading. Notes grow organically as investigation and design scraps accumulate. Don't pre-populate sections.

## INBOX and Story Creation

The `INBOX` column on the project kanban is the general capture point for ideas and work that hasn't been shaped into a story yet. Anything unreviewed or unsized goes here first.

**INBOX cards are uncommitted input.** They represent potential work — not prioritized, not scoped, not assigned. The user decides what to do with them. Cards stay in INBOX until the user explicitly commits:

- Small enough to be a task in an existing story → move it there
- New body of work → convert it to a story (see below)
- Not worth pursuing → archive it

Cards in INBOX are plain text — no linked files, no task breakdowns. Just enough to remember what the idea is.

### Converting INBOX to Story

When the user commits to an INBOX item and it becomes a story:

1. Determine the next story ID: read `last-id` from the project kanban frontmatter, increment it (e.g. `001` → `002`)
2. Update `last-id` in the project kanban frontmatter
3. Create the story directory: `projects/[PROJECT]/stories/[STORY-ID]/`
4. Create `_index.md` using the Story Index template above
5. Create `_notes.md` (heading only)
6. Create `_kanban.md` with story-level columns (Issues, todo, Ready, in progress, Verify, done) and correct `new-note-folder`
7. Create `tasks/` directory
8. Move the INBOX card to the `backlog` column on the project kanban, updating it to link to the new `_index.md`

## Bootstrap

When `projects/` does not exist at all (fresh project with no tracking structure):

1. Create `projects/[name]/` directory (ask user for project name if not obvious)
2. Create `projects/[name]/_kanban.md` using the kanban template with project-level columns (INBOX, ToDo, Refining, Ready, In Progress, Verify, Done, ARCHIVE). Set `new-note-folder` to `projects/[name]/stories`. Set `last-id` to `000` in frontmatter. Set `prefix` to the project abbreviation.
3. Create `projects/_index.md` listing the new project
4. Create `projects/[name]/stories/` directory

The story-context skill delegates here when `projects/` is not found.

## When to Update What

> History rows in `_index.md` are maintained automatically by done-criteria step 6. Do not add them here.

| Event | Action |
|-------|--------|
| New story created | Create story directory, `_index.md`, `_notes.md`, `_kanban.md`, `tasks/`; add story card to project kanban in `backlog`; increment `last-id` in project `_kanban.md` frontmatter |
| New story for existing work | Find related docs in the story folder or sibling story folders; move into story folder; populate history table manually; set status `in progress`; place story card in `in progress` on project kanban |
| Story moves to in progress | Move story card to `In Progress` on project kanban |
| Story completed | Move story card to `Done` on project kanban; move story directory to `archive/done/` |
| Task started | Move card from `todo`/`Issues` to `in progress` in story `_kanban.md` |
| Task completed | Move card to `done` in story `_kanban.md` |
| Issue discovered | Add plain checkbox to `Issues` column in story `_kanban.md` (or to `INBOX` on project kanban for general issues) |

## Story for Existing Work

If a story is being created to track work already underway:

1. Search for related documents in the project — check sibling story folders, root-level notes, and any other relevant locations under `projects/[subproject]/`
2. Move them into the story directory
3. Add each to the history table in `_index.md` with the correct date and outcome
4. Set `status: in progress` in `_index.md` frontmatter
5. Create `_kanban.md` with story-level columns (Issues, todo, Ready, in progress, Verify, done) and correct Obsidian frontmatter and `new-note-folder` setting pointing to `tasks/`
6. Add the tasks/notes navigation line to `_index.md` after the opening description paragraph if not already present: `##### 📋 [Tasks](_kanban.md)  📘 [Notes](_notes.md)`
7. Place the story card in `In Progress` on the project kanban — not `backlog`

## Creating Tasks from Any Source

When any prompt (plan, review, brainstorm, etc.) produces a list of action items:

1. For each item, create `tasks/[kebab-case-title].md` using the task file template above
2. Add a checkbox link in `_kanban.md` under the appropriate column (`todo` for planned work, `Issues` for discovered problems)
3. Never put detail text directly in the kanban card — only the title + link

## Naming Conventions

- Story IDs: `[PROJECT]-[NNN]` e.g. `APP-001`, `WEB-002`
- Dated docs: `YYYY-MM-DD-[type]-[topic].md` e.g. `2026-05-25-investigate-frameit-crash.md`
- Task files: kebab-case short title, no date prefix
- Kanban files: `_kanban.md` at both project level and story level

## Additional Resources

- **`references/kanban-syntax.md`** — Full Obsidian kanban-plugin field reference and edge cases
- **`bob:work-routing` skill** — Routes discovered work items to the correct kanban (Issues or INBOX). Invoke this skill mid-session; do not embed routing logic in individual commands.
