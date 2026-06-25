---
name: work-routing
description: Routes discovered work items to the correct kanban column. Invoked mid-session by engineering commands when issues, deferred ideas, or out-of-scope findings surface.
user-invokable: false
---

# Work Routing

Invoked mid-session when any command discovers work (issues, deferred ideas, out-of-scope findings, new dependencies).

**Inputs:** a list of work items, each with: description, severity (🔴/🟡/🟢), and context (how it was discovered).

**If target `_kanban.md` does not exist:**
Create it before writing, using the story-level kanban template from `bob:project-tracking` (frontmatter with `kanban-plugin: board`, story-level columns, and `new-note-folder` settings block pointing to the story's `tasks/` folder). A file without the `kanban-plugin: board` frontmatter will not render as a kanban in Obsidian.

**Before any kanban edit:**
1. Read the full target kanban file.
2. Extract all existing column headers (`## Column Name` lines). Matching is case-insensitive (`## done` = `## Done`).
3. Add items inside an existing column — never create a duplicate column header.
4. If the target column does not exist: create it in a logical position (Issues near top, done near bottom).

**Decision tree:**

For each item:

1. **This story's scope?** — If clearly within the current story's scope (same feature, same files, direct consequence of current work): plan to add to `{story_path}/_kanban.md` under `## Issues` as `- [ ] {emoji} {description}`.

2. **Default — INBOX:** Plan to add to `projects/{subproject}/_kanban.md` under `## INBOX`. If it looks like a standalone new story, prefix: `[Story candidate] {description}`.

**After compiling the full list**, ask user: "Should I file these N items to the kanban? (yes / no / specify which ones)"
- **yes** → file all as planned above
- **no** → discard, items appear in command output only
- **specify** → user excludes or redirects individual items, then file the rest

For 🔴 Critical items: name them explicitly in the prompt regardless of count.

**After filing**: confirm what was filed: "Filed N items: {story-id} Issues (+N), INBOX (+N)."
