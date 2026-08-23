---
name: work-routing
description: Routes discovered work items to the correct kanban column. Invoked mid-session by engineering commands when issues, deferred ideas, or out-of-scope findings surface.
user-invokable: false
---

# Work Routing

Invoked mid-session when any command discovers work (issues, deferred ideas, out-of-scope findings, new dependencies).

**Inputs:** a list of work items, each with: description, severity (🔴/🟡/🟢), type, and context (how it was discovered).

**Item types:**
- **Implementation issue** — a bug or defect found while implementing or reviewing.
- **Deferred feature** — in-scope idea explicitly pushed out.
- **Design Feedback** — evidence that the current Design Record no longer fits reality.
- **Architectural insight** — a durable structural observation not tied to a single defect.
- **Understanding gap** — a place the human's mental model diverges from the code.
- **Harness lesson candidate** — a correction, interruption, or repeated failure that might warrant a change to BOB itself.

**If target `_kanban.md` does not exist:**
Create it before writing, using the story-level kanban template from `bob:project-tracking` (frontmatter with `kanban-plugin: board`, story-level columns, and `new-note-folder` settings block pointing to the story's `tasks/` folder). A file without the `kanban-plugin: board` frontmatter will not render as a kanban in Obsidian.

**Before any kanban edit:**
1. Read the full target kanban file.
2. Extract all existing column headers (`## Column Name` lines). Matching is case-insensitive (`## done` = `## Done`).
3. Add items inside an existing column — never create a duplicate column header.
4. If the target column does not exist: create it in a logical position (Issues near top, done near bottom).

**Decision tree:**

For each item, route by type first, then by scope:

1. **Design Feedback affecting current work** — return it to the current Design Record (or hand it to `/bob:design` if none is open) instead of filing it as generic backlog. Do not put it on a kanban board at all unless it also implies scheduled tooling work.

2. **Architectural insight** — route through Reflect/Learn classification before it becomes documentation. Do not write it directly to `docs/` or a kanban card; hand it to `/bob:reflect` or `/bob:learn` as a candidate.

3. **Understanding gap** — not automatically kanban work. It may be resolved inside `/bob:reflect` directly; only route to kanban if it also names concrete follow-up work (e.g. "add a comment explaining X").

4. **Harness lesson candidate** — goes to `/bob:learn` (via `docs/process/learnings.md` staging), not project INBOX, unless it also requires scheduling actual tooling/config work — in that case file the tooling work to INBOX and leave the lesson itself with Learn.

5. **Implementation issue / deferred feature — this story's scope?** — If clearly within the current story's scope (same feature, same files, direct consequence of current work): plan to add to `{story_path}/_kanban.md` under `## Issues` as `- [ ] {emoji} {description}`.

6. **Default — INBOX:** Plan to add to `projects/{subproject}/_kanban.md` under `## INBOX`. If it looks like a standalone new story, prefix: `[Story candidate] {description}`.

**Never route the same discovery twice.** Before filing, check whether this item (by description/evidence, not exact wording) was already routed earlier in this session — e.g. by a mid-session PM step that already invoked this skill. An item already routed mid-session must not be routed again from a Done Criteria end-of-session pass. When in doubt, prefer the earlier routing and skip the later one.

**After compiling the full list**, ask user: "Should I file these N items to the kanban? (yes / no / specify which ones)"
- **yes** → file all as planned above
- **no** → discard, items appear in command output only
- **specify** → user excludes or redirects individual items, then file the rest

For 🔴 Critical items: name them explicitly in the prompt regardless of count.

**After filing**: confirm what was filed: "Filed N items: {story-id} Issues (+N), INBOX (+N)."
