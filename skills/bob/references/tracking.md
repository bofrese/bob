# Tracking and work routing

Story files, templates and the bootstrap live in `references/story-files.md`. Read it only to create a story, a task or a kanban.

## Register an artifact (at write time)

Every session artifact gets exactly one row in `{story_path}_index.md` `## History`, added when the file is written:

```text
| {date} | [{Type}](sessions/{file}.md) | {one-line summary} | {outcome} |
```

- Type: Brainstorm, Design, Plan, Plan Review, Implementation, Code Review, Documentation, Handover, Reflection, Harness Learning, Investigation, UI Review.
- Outcome: the result (Draft, Ready, Approve with changes, Completed, Root cause identified).
- At finish, check the row exists. A missing row is a defect: add it and tell the user it was late. Never add a second row for the same file.
- Then update the story kanban: tasks done move to `## done` as `- [x]`, the task in work sits in `## in progress`.

## Edit a kanban

1. Read the whole file. Collect its `## Column` headers (match case-insensitively).
2. Add cards inside existing columns. Never add a duplicate header.
3. Missing column: add it in a logical place (Issues near the top, done near the bottom).
4. A file without `kanban-plugin: board` frontmatter does not render. Create missing boards from the templates.
5. Never write a link to a file that does not exist yet.

## When to update what

| Event | Action |
|---|---|
| Task started | Move card from `todo`/`Issues` to `in progress` |
| Task done | Move card to `done` |
| Issue found | Plain checkbox in story `Issues`, or project `INBOX` |
| Story in progress | Move story card to `In Progress` on the project kanban, set `status` in `_index.md` |
| Story done | Move card to `Done`; move the story folder to `archive/done/` |
| Story dismissed | Move the folder to `archive/dismissed/`; remove the card from active columns |
| Action items from any phase | One `tasks/{kebab-title}.md` per item, linked card in `todo` (planned) or `Issues` (problems) |

## Route discovered work

Route work when it surfaces, not only at the end. Each item: description, severity (🔴 🟡 🟢), type, how it was found.

Route by type first:
1. Design feedback (the design no longer fits reality): return it to the current Design Record, or to `design` if none is open. Not a kanban card, unless it also needs scheduled tooling work.
2. Architectural insight: hand it to `reflect` or `learn` as a candidate. Do not write it to `docs/` or the kanban.
3. Understanding gap: resolve it in `reflect`. Kanban only if it names concrete follow-up work.
4. Harness lesson: stage it for `learn` in `docs/process/learnings.md`. Scheduled tooling work goes to INBOX; the lesson stays with `learn`.
5. Issue or deferred feature in this story's scope (same feature, same files, direct consequence): `{story_path}_kanban.md` `## Issues` as `- [ ] {emoji} {description}`.
6. Anything else: `projects/{sub}/_kanban.md` `## INBOX`. Prefix a likely new story with `[Story candidate]`.

Then:
- Skip items already routed this session, matched by meaning, not wording.
- Ask once: "Should I file these N items to the kanban? (yes / no / specify which ones)". Name every 🔴 item in the question.
- yes: file all. no: they stay in the artifact only. specify: apply the user's changes, file the rest.
- Confirm: "Filed N items: {ID} Issues (+N), INBOX (+N)."

Product phases (vision, personas, design brief) do not route work.
