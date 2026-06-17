# Project Management
*Last updated: 2026-06-17*

How Bob tracks work across the full lifecycle of a feature — from idea to shipped code.

---

## The Big Picture

Bob uses **stories** to organize work and **Obsidian kanban boards** to track progress. Everything is designed to be used inside Obsidian with the Kanban plugin, which renders `_kanban.md` files as interactive boards you can drag cards across.

> A template Obsidian vault with the right settings and plugins pre-configured will be available in a future release.

---

## Sub-Projects

The `projects/` folder doesn't represent one big backlog. It represents **a single product split into concerns**:

```
projects/
├── _index.md        ← lists all sub-projects
├── APP/             ← main app development
├── WEB/             ← promotional website
└── BUS/             ← business/marketing
```

One product, multiple sub-projects. Each sub-project is a separate backlog with its own kanban board and story sequence. This keeps concerns clean — you don't want app engineering stories mixed with marketing tasks.

Story IDs are prefixed per sub-project: `APP-001`, `WEB-002`, `BUS-001`. You don't have to use this model — a single `projects/[NAME]/` folder works fine for simpler products.

---

## Folder Structure

```
projects/
├── _index.md                              # Lists all sub-projects
└── [SUB-PROJECT]/
    ├── _kanban.md                         # Sub-project board (stories as cards)
    └── stories/
        └── [STORY-ID]/
            ├── _index.md                  # Story hub — description + history
            ├── _notes.md                  # Developer notes (grows organically)
            ├── _kanban.md                 # Task board for this story
            └── tasks/
                └── [task-name].md         # One file per task
```

Session artifacts (brainstorm reports, plans, reviews) live directly in the story folder:
```
            ├── 2026-06-15-brainstorm-auth.md
            ├── 2026-06-16-plan-auth.md
            └── 2026-06-17-review-auth.md
```

---

## Getting Started

Bob creates the entire structure for you. Run any engineering command (`/bob:brainstorm`, `/bob:plan`, etc.) and Bob will:

1. Look for an open story (from Obsidian tabs, recent files, or explicit mention)
2. If none found, offer to create a new story
3. Ask for the sub-project name and generate the next story ID automatically
4. Create the folder, `_index.md`, `_notes.md`, `_kanban.md`, and `tasks/`

**You don't create folder structures manually.** Once set up, you move cards in Obsidian and Bob populates the story folder with artifacts as you work.

---

## The Kanban Boards

### Sub-Project Board (`_kanban.md` at sub-project root)

Stories flow left to right through these columns:

| Column | Meaning |
|--------|---------|
| **INBOX** | Unreviewed ideas. Candidates, not commitments. |
| **ToDo** | Committed — decided but not started. |
| **Refining** | Being brainstormed or planned. |
| **Ready** | Has a reviewed plan. Ready to implement. |
| **In Progress** | Implementation underway. |
| **Verify** | Done, awaiting final sign-off. |
| **Done** | Shipped and verified. |
| **ARCHIVE** | Dismissed or deferred. |

### Story Board (`_kanban.md` inside each story folder)

Tasks and issues within a story:

| Column | Meaning |
|--------|---------|
| **Issues** | Bugs and problems found. Prefix: 🔴 critical, 🟡 important, 🟢 suggestion. |
| **todo** | Planned tasks, not started. |
| **Ready** | Tasks ready to start (dependencies resolved). |
| **in progress** | Active work. |
| **Verify** | Done, awaiting review. |
| **done** | Completed. |

Task cards link to files in `tasks/`. The card is just a title and link — all detail stays in the task file.

---

## How a Story Progresses

Bob drives the content, you drive the board.

| Bob command | What Bob does automatically | What you do in Obsidian |
|-------------|----------------------------|------------------------|
| `/bob:brainstorm` | Creates story folder + files; writes brainstorm report; adds history entry to `_index.md` | Move story card → **Refining** |
| `/bob:plan` | Writes plan; adds history entry | — |
| `/bob:review-plan` | Writes review; adds history entry | Move card → **Ready** |
| `/bob:implement` | Writes code + implementation report; updates task kanban | Move card → **In Progress**, then **Verify** |
| `/bob:review` | Writes code review; adds history entry | Move card → **Done** once merged |

The history table in `_index.md` is maintained automatically by Bob's done-criteria step — don't edit it by hand.

---

## Working in Obsidian

Once a story exists, your day-to-day workflow is in Obsidian:

- **Move story cards** across the sub-project kanban as work progresses
- **Move task cards** within the story kanban as tasks are picked up and completed
- **Add issues** to the Issues column as you discover them during implementation or review
- **Write in `_notes.md`** freely — gotchas, decisions, rabbit holes, code references
- **Open session artifacts** (plans, brainstorms) directly from the history table in `_index.md`

The Kanban plugin renders `_kanban.md` boards interactively. New task cards created in Obsidian automatically land in the story's `tasks/` folder via the `new-note-folder` setting.

---

## Discovered Issues

When you find a problem during implementation or review, add it to the story's **Issues** column with a severity prefix:

```markdown
## Issues
- [ ] 🔴 Auth token not cleared on logout
- [ ] 🟡 Replace hardcoded role strings with enum
- [ ] 🟢 Extract magic numbers to constants
```

Issues can be dealt with inline or converted to separate stories.

---

## Archive, Don't Delete

When a story is dismissed or deferred, move its folder to `archive/dismissed/`. When it ships, Bob may move it to `archive/done/`. On the sub-project kanban, move the card to **ARCHIVE**.

Why keep it? "Why didn't we do X?" — the archive has the answer.

---

## Cross-Story Dependencies

Document dependencies in `_index.md`:

```markdown
## Blocked By
- [APP-001](../APP-001/_index.md) — needs auth system first
```

Tracking: keep blocked stories in **ToDo** on the sub-project kanban until the dependency ships. Move them to **Ready** only when the plan is reviewed and dependencies are clear.

---

## Tips

**Let Bob build the structure.** The first command on a new story creates everything correctly. Don't create folders or templates by hand.

**`_notes.md` is yours.** It's free-form, personal, and not polished. Write in it liberally as you work. It's the place for gotchas, code pointers, and decisions that don't fit a formal artifact.

**The story folder is persistent context.** When you return to a story after weeks away, the `_index.md` history table is your entry point. Everything links from there.

**Sub-project prefixes clarify scope.** `APP-001` and `WEB-001` are different stories. Keep prefixes short (2-4 chars) and stable — renaming a prefix mid-project breaks links.

---

## Next Steps

- Read [Engineering Workflows](02-engineering-workflows.md) to understand how stories flow through phases.
- Ready to start? Run `/bob:brainstorm` — Bob will create the story structure and start the first session.
