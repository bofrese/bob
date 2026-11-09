# Done criteria

## Bootstrap

If `docs/process/done-criteria.md` is missing, copy `assets/done-criteria.md` there (create `docs/process/`) and set the date on its last lines.

## Verify

Check every item in `docs/process/done-criteria.md` that applies to this phase. Flag anything unmet in your output. Do not ship it silently.

| Phase | Section |
|---|---|
| implement, dev | Code changes |
| plan | Plans |
| review, review-plan | Reviews |
| design | Design. Uncertainty marked safe to defer is a valid result |
| reflect | Reflection. A short "no gap" record is valid |
| learn | Harness learning. "No persistent lesson" is valid |
| document | Documentation |
| ui-review | Reviews |
| explain | Explainers |
| investigate, brainstorm | Investigation and ideas |
| handover | Handover |
| product, brand-design, linkedin | Output is self-contained and readable without prior context |

A phase that changed code or a durable artifact never skips this step.

New artifact type not in the file: add a DONE subsection for it. Criteria are generic ("tests pass"), never feature-specific ("login tests pass").

## Knowledge candidates

List what emerged this session and is not yet in your artifact:
- Terminology, architecture decisions and codebase patterns: name each, say why it matters, recommend `document` (decisions, terms, patterns) or `guidelines` (technology pitfalls).
- Decisions and insights not in `knowledge/`: if `knowledge/` exists, write each to `knowledge/_INBOX/{date}-{slug}.md` (frontmatter `title`, `type: inbox`, `timestamp`; body = the insight). Then say "N item(s) captured to `knowledge/_INBOX/`. Run `library process` to file them."
- Repeated corrections or interruptions: append to `docs/process/learnings.md` per the `learn` skill's `references/persistence-map.md`. Stage only; `learn` classifies. A lesson about how bob itself should work goes there too, never into agent memory.

Persist nothing durable without the user's confirmation. Nothing found: say nothing.

## Daily note

If `personal/daily/` exists, append one entry per phase run to `personal/daily/{date}.md` under `## Sessions` (once per run):

```text
### {phase} ({STORY-ID}) HH:MM
1-2 sentences on what was done.
```

Omit `({STORY-ID})` without a story. A new daily file gets frontmatter `title`, `type: daily`, `date`, the heading `# {date}` and the sections `## Sessions`, `## Wrap-up`, `## Notes`.

## Missing infrastructure

No `personal/daily/`, no story, no kanban: skip that step silently. It never blocks a finished result.
