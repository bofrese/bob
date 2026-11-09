# Story resolution

## Does this work need a story?

- Yes: durable brainstorm, design, plan, review-plan, implement, review, handover, reflect or learn artifacts.
- No: read-only analysis, a short reflection, or `dev` fast-path work, unless the user asks for tracking. Skip this file.
- Unclear: ask the user once.

Never create a story only to satisfy this protocol.

## Resolve

Pass any file arguments and the user's request text:

```bash
python3 <skill-dir>/scripts/story.py "<file arg>" "<request text>"
```

The JSON names a `tier`, whether it is `certain`, and `candidates`.

| Tier | Meaning | Action |
|---|---|---|
| `path` | A file argument lies inside a story folder | Proceed |
| `id` | The text names an existing story ID | Proceed if `certain`; else ask which one |
| `open` | Story files open in Obsidian | Ask: "I see `{ID}` open in Obsidian. Is that the story?" List all if several |
| `recent` | Most recent story file in Obsidian | Ask: "The most recent story I see is `{ID}`. Is that the story?" |
| `none` | Nothing found | Ask for a path or story ID, or offer "new story" |

- "New story": create it per `references/story-files.md`, then resolve again.
- The user confirms a candidate, names a story, or switches to another story during the phase: run `story.py "<ID>"` again. The status line shows only a story that `story.py` resolved as certain.
- Work routed to another story does not change the story of the session. Do not resolve for it.
- No `projects/` folder: bootstrap it per `references/story-files.md`.
- Resolve fresh in each phase. Do not reuse a story from an earlier phase without checking.

## Output

Print, then use `story_path` for every artifact path:

```text
**Story Context**
- Path: `projects/{sub}/stories/{ID}/`
- Story ID: `{ID}`
- Subproject: `{sub}`
- Task ID: `{task}`   (only when the JSON has task_id)
```

Session artifacts go to `{story_path}sessions/`, named `{date}-{type}-{slug}.md`.

## Kanban sync

1. If `{story_path}_kanban.md` is missing, create it from the story kanban template in `references/story-files.md`.
2. Match task cards in `todo`, `Ready` and `in progress` against the phase, its arguments and the user's request. Match the link title, by meaning, not exact words.
3. One clear match: move the card to `## in progress` and say "Task marked in-progress: {title} on {ID} kanban."
4. Several or unclear: ask "Which task does this session target? {titles}, or 'none'." No tasks: say nothing.

This step syncs state. It never blocks work.
