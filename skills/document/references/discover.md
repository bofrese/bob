# Discover Mode

Build the first architecture map of a project. Runs when `docs/architecture/` does not exist.

## Steps

1. **Read existing docs as input.** If older concept docs exist in `docs/` (outside `product/`, `guidelines/`, `domain/`, `process/`), read them. They are evidence, not truth: check their claims against the code.
2. **Map concepts from the code.** Use `bob:architect` `references/concepts.md`. Prefer the code graph if one is fresh. List concepts, not modules: one line each, with the main code location.
3. **Map patterns.** Use `bob:architect` `references/patterns.md`. For each candidate: short local name, 2-3 example locations, proposed status (`established`, `emerging` or `competing`; only the human confirms `established`).
4. **Propose, do not write.** Present the concept list and the pattern list (with proposed status) as tables. Note design smells found on the way as open questions. The human confirms, renames, merges or drops entries, and decides which patterns are `established`.
5. **Discuss intent for the confirmed set.** One topic at a time: why a concept exists, non-obvious decisions, what trips up newcomers. These answers are the most valuable content.
6. **Write** the confirmed notes and `README.md` using `note-templates.md`.
7. **Migrate older docs.** For each older `docs/*.md` concept doc, propose one of: migrate into atomic notes (then delete the original), keep as is, or delete. Confirm per file.

## Scope control

For a large codebase, propose a first slice (the concepts most often touched, or the area of the current story) instead of mapping everything at once. The map grows through Update mode.
