# Discover Mode

Build the first architecture map of a project. Runs when `docs/architecture/` does not exist.

## Steps

1. **Read existing docs as input.** If older concept docs exist in `docs/` (outside `product/`, `guidelines/`, `domain/`, `process/`), read them. They are evidence, not truth: check their claims against the code.
2. **Map concepts from the code.** Use the `architect` skill, `references/concepts.md`. Prefer the code graph if one is fresh. List concepts, not modules: one line each, with the main code location, or several locations when the concept is spread out.
   - **Find spread-out concepts.** A concept with no single home is still a concept. Trace each entry point end to end (user actions, API endpoints, jobs, startup, external events) and list the side effects per path in a table. Grep each domain rule and cross-cutting duty (thresholds, formatting, localization, error presentation, loading state) for divergent copies. Paths that differ for no stated reason, or a rule with several copies, are candidate concepts marked inconsistent.
3. **Map patterns.** Use the `architect` skill, `references/patterns.md`. For each candidate: short local name, 2-3 example locations, proposed status (`established`, `emerging` or `competing`; only the human confirms `established`).
4. **Propose, do not write.** Present the concept list (inconsistent ones marked ⚠️) and the pattern list (with proposed status) as tables. A design smell on a confirmed concept is recorded in that concept's note (`## Inconsistencies`), not only raised as a question. The human confirms, renames, merges or drops entries, and decides which patterns are `established`.
5. **Discuss intent for the confirmed set.** One topic at a time: why a concept exists, non-obvious decisions, what trips up newcomers. These answers are the most valuable content.
6. **Write** the confirmed notes and `README.md` using `note-templates.md`. Write the "How it fits together" overview last, from the confirmed notes: it shows how they connect, it does not repeat them. Every index row gets a "Read when" trigger.
7. **Migrate older docs.** For each older `docs/*.md` concept doc, propose one of: migrate into atomic notes (then delete the original), keep as is, or delete. Confirm per file.
   - Before deleting, list each fact in the old doc (decision, rule, gotcha, limitation, reason) and name the note that now holds it. Carry over any fact without a home, or keep the doc.
   - Retarget every inbound link to the note that holds the linked fact, never to the index, and update link text that names the old doc.

## Scope control

For a large codebase, propose a first slice (the concepts most often touched, or the area of the current story) instead of mapping everything at once. The map grows through Update mode.
