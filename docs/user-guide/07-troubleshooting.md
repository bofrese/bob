# Troubleshooting
*Last updated: 2026-10-14*

Known problems and how to fix them.

## Installation and setup

| Symptom | Fix |
|---|---|
| The skills do not show up | Restart Claude Code after installing. Then run `/plugin` and check that `bob` is installed. |
| Old names like `/bob:pm` or `/bob:product-coach` do not work | They were renamed in bob 4.0. Run `/bob:setup`: it finds old names in your project files and offers to fix them. |
| Bob ignores the project when you do not name a skill | The primer runs only in projects that use bob. Run `/bob:setup` so that `projects/` and `docs/process/done-criteria.md` exist. |
| Artifacts ignore the writing rules | Check that the `plain-writing` plugin is installed. Bob depends on it. |

## Stories

| Symptom | Fix |
|---|---|
| Bob asks for a story and you have none | Say "new story". Bob creates the story folder and its files. |
| Bob picked the wrong story | Name the story ID or a file in its folder in your request. A named story always wins over the Obsidian guess. |
| Bob cannot find a story you made by hand | Stories must be at `projects/{sub}/stories/{ID}/` with an `_index.md`. Let bob create stories, so all files exist. |
| You forgot what you were working on | Run `/bob:bob`. It shows what is in progress. |

## Phases

| Symptom | Fix |
|---|---|
| The brainstorm does not converge | Name your criteria (effort, impact, user value, fit), rank the options, pick one or two. "Good enough to design" is the bar. |
| The plan is too detailed | Plans describe approach and steps, not every line of code. Ask for a shorter plan. |
| You disagree with the plan's Questions & Decisions | Change the answers. The plan is yours. Ask bob to record why. |
| The plan review and the plan disagree | Read both. Fix whichever is wrong, then review again if the change was large. |
| Implementation keeps pausing | Each pause is a design signal: the code does not fit the design. Answer it, or go back to `/bob:design`. |
| The review is very long | Big changes get long reviews. Split work into smaller changes. |

## Documentation and knowledge

| Symptom | Fix |
|---|---|
| Architecture notes are out of date | Run `/bob:document` in Audit mode. |
| No architecture notes exist yet | Run `/bob:document`. It starts in Discover mode and asks you to confirm the concept list. |
| A guideline is not applied | Check that it is in `docs/guidelines/README.md` and that its "Applies When" matches the files you work on. |
| Bob loaded the wrong file | Check for duplicates, for example two vision files. Bob loads from fixed paths, so keep one copy at the standard place. |
| You want bob to read a specific file | Say so in the request: "Read `path/to/file.md` for context." |

## Process

| Symptom | Fix |
|---|---|
| It feels like too much ceremony | Use `/bob:dev` for small, settled changes. Start standard work at the phase where the open question is. The full loop is for conceptually significant work. |
| The skills are slow | Large codebases and broad scope load more. Narrow the scope in your request. A code graph (graphify) helps the AI find code faster. |

## Report a problem

Open an issue on [GitHub](https://github.com/bofrese/bob) with:

1. What you ran, for example `/bob:plan`.
2. What happened.
3. What you expected.
4. Whether it happens again.

If the problem is about how bob should behave, you can also run `/bob:learn` on the session. It records the lesson in `docs/process/learnings.md`.
