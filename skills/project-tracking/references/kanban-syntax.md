# Obsidian Kanban Plugin - Syntax Reference

## Frontmatter

```yaml
---
kanban-plugin: board
title: Board Title
---
```

Required fields: `kanban-plugin: board`. `title` is optional but recommended.

## Columns

Each column is an H2 heading. Cards are checkbox list items beneath it.

```markdown
## Column Name
- [ ] Unchecked card
- [x] Checked (done) card
```

Column names are free-form text. The plugin does not enforce column semantics — conventions are:
- `inbox`, `backlog`, `todo`, `in progress`, `done`, `archive`, `dismissed`
- Story-level boards add `Review findings` as the first column

## Card Formats

**Plain text card:**
```markdown
- [ ] Plain card title
```

**Card with link to a note:**
```markdown
- [ ] [Card title](relative/path/to/file.md)
```

**Card with priority emoji prefix:**
```markdown
- [ ] 🔴 [Critical issue title](tasks/critical-issue.md)
- [ ] 🟡 [Important issue title](tasks/important-issue.md)
- [ ] 🟢 [Suggestion title](tasks/suggestion.md)
```

**Completed card (checked):**
```markdown
- [x] [Done task](tasks/done-task.md)
```

## Column Dividers

Columns are separated by blank lines. An empty column still needs its H2 heading:

```markdown
## in progress

## done
- [x] [Completed thing](tasks/completed-thing.md)
```

## Settings Block

The settings block appears at the bottom of the file, inside a comment:

```markdown
%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"tasks","list-collapse":[false,false,false,false]}
```
%%
```

Key settings:

| Key | Type | Purpose |
|-----|------|---------|
| `kanban-plugin` | `"board"` | Required identifier |
| `new-note-folder` | string | Where new note-linked cards are filed (relative to the kanban file) |
| `list-collapse` | bool[] | One entry per column; true = collapsed by default |

## Minimal Valid Board

```markdown
---
kanban-plugin: board
title: My Board
---

## backlog

## in progress

## done

%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"tasks"}
```
%%
```

## Story-Level `_tasks.md` Template

```markdown
---
kanban-plugin: board
title: Tasks - [Story Name] ([STORY-ID])
---

## Review findings

## todo

## in progress

## done

%% kanban:settings
```
{"kanban-plugin":"board","new-note-folder":"tasks"}
```
%%
```

## Project-Level Kanban Template

```markdown
---
kanban-plugin: board
title: [Project Name]
---

## inbox

## backlog
- [ ] [[stories/[STORY-ID]/_index|[STORY-ID] Story Title]]

## in progress

## done

## archive

## dismissed

%% kanban:settings
```
{"kanban-plugin":"board"}
```
%%
```

Note: Project-level boards use Obsidian wiki-link syntax `[[path|label]]` for story cards; story-level `_tasks.md` uses standard markdown links `[title](path)` for task cards since they point to files in the `tasks/` subfolder.
