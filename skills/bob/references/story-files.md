# Story files and templates

Contents: layout, create a story, story for existing work, bootstrap, story index, notes, story kanban, project kanban, task file.

## Layout

```text
projects/
  _index.md                  lists all projects
  {sub}/_kanban.md           project kanban (stories, INBOX), frontmatter prefix + last-id
  {sub}/archive/done/  archive/dismissed/
  {sub}/stories/{ID}/
    _index.md  _notes.md  _kanban.md
    input/  sessions/  tasks/
```

Names: story IDs `{PREFIX}-{NNN}`; session artifacts `sessions/{date}-{type}-{slug}.md`; task files kebab-case, no date.

INBOX cards are uncommitted ideas: plain text, no files. They stay until the user decides: move to an existing story as a task, make a new story, or archive.

## Create a story

Create all of this in one go. A story folder with missing files makes Obsidian resolve links to the wrong file.
1. Read `last-id` from the project kanban frontmatter, increment it (`001` -> `002`), write it back.
2. Create `projects/{sub}/stories/{ID}/` with `_index.md`, `_notes.md`, `_kanban.md`, `input/`, `sessions/`, `tasks/`.
3. Put the story card in `ToDo` on the project kanban (move it there if it came from INBOX), linking `_index.md`.

## Story for existing work

1. Find related documents in sibling story folders and under `projects/{sub}/`. Move them into `sessions/` and add a History row for each.
2. Create the missing story files as above. Set `status: In Progress`.
3. Put the story card in `In Progress`, not `ToDo`.

## Bootstrap (no `projects/`)

Ask for the project name if it is not obvious. Create `projects/_index.md` listing it, `projects/{name}/_kanban.md` from the project template (`last-id: "000"`, `prefix` = project abbreviation), and `projects/{name}/stories/`.

## Story index (`_index.md`)

Readable on its own by a future agent or developer. History rows come from write-time registration (`references/tracking.md`). No open-issues table: issues live in `_kanban.md`. Keep the blockquote current.

```markdown
---
id: {ID}
title: "{ID} Story: {Name}"
status: ToDo
domain: {Area}
started: {date}
---
# {ID} - {Name}

> {What the story is, why it matters, current state, known blockers.}

##### 📋 [Tasks](_kanban.md)  📘 [Notes](_notes.md)

## Intent Sources

Originals, never summaries. Rules: bob hub `references/intent.md`.

## History

| Date | Type | Summary | Outcome |
|------|------|---------|---------|
```

`status` is one of ToDo, Refining, Ready, In Progress, Verify, Done.

## Notes (`_notes.md`)

```markdown
---
title: "{ID} Developer Notes"
---
# {ID} Developer Notes
```

## Story kanban (`_kanban.md`)

Cards link to task files: `- [ ] [Title](tasks/title.md)`. Issues are plain checkboxes with a severity emoji. `new-line-trigger: shift-enter` is required on every board.

````markdown
---
kanban-plugin: board
title: {ID} Tasks
---

## Issues

## todo

## Ready

## in progress

## Verify

## done

%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"projects/{sub}/stories/{ID}/tasks","new-line-trigger":"shift-enter"}
```
%%
````

## Project kanban

Same format as the story kanban, with:
- frontmatter `title: {Project}`, `prefix: {PREFIX}`, `last-id: "000"`; `new-note-folder` = `projects/{sub}/stories`.
- columns INBOX (uncommitted), ToDo (committed), Refining (brainstorm or design in progress), Ready (design settled), In Progress, Verify (handover written, waiting for the developer), Done, ARCHIVE. Boards may add columns; bob uses only these.
- story cards as wiki links: `- [ ] [[stories/{ID}/_index|{ID} Title]]`.

## Task file (`tasks/{name}.md`)

`status`: todo, in progress or done. Acceptance criteria are testable checkboxes. Code references as `file:line`. No placeholders left in the body.

```markdown
---
status: todo
---
# {Task title}

{One sentence: what it achieves and why.}

## Context
{Link to the investigation or plan; omit if none.}

## Acceptance Criteria
- [ ] {Verifiable condition}

## Notes
{Approach, code references, open questions.}
```

Bug tasks replace `## Notes` with `## Problem`, `## Root Cause`, `## Solution` and a `## Code References` table (File | Location | Role).
