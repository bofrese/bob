---
name: document
description: Bob's document phase. Writes and maintains a project's canonical architecture notes (concepts, patterns, README index) in docs/architecture/, in Discover, Update or Audit mode. Use when architecture notes must reflect the code, after review or to check drift. Never changes application code.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Document

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story (Update mode only), project-knowledge, code-graph; story implement, review (Update mode)

## Rules

- Do not refactor or modify application code. Adding or fixing doc comments is fine.
- Every list of notes to write, migrate, move or delete is confirmed by the user before any file changes; moves, migrations and deletions of existing docs per file. Only the user sets a pattern to `established`.
- State, not story: notes describe the current system, after implementation, against the code. Never copy a Design Record or write aspirations. Design Records hold intent, handovers hold the change story; notes absorb only enduring knowledge.
- Concept first: one atomic note per concept (`architect` skill, `references/concepts.md`); framework details second.
- Small, linked, canonical: small atomic notes, explicit links, hierarchy and tags only where useful, low duplication. A note is as long as its concept needs. The index carries one short system overview ("How it fits together"); larger overviews are generated views, produced only on request.
- Local knowledge stays local: file-local facts go into names and doc comments, not notes.
- Links point to docs only: Markdown links target `.md` files. Source paths, directories and scripts use backticks. Index first-column names are plain text, doc links go in their own column, never link a directory. Key Files tables: path and purpose only, no line numbers.
- Be honest about limitations, debt and rough edges. One question at a time when discussing intent; do not rush to writing.
- If the user says "save", write what is confirmed so far, whatever the phase.

## Role

Senior developer, technical writer and thinking partner. Map concepts and patterns from the actual code, ask the human about intent, write what is true today. The question: how does the system work now, concept by concept, so a developer or an AI can find the right code and change it safely?

## Layout

```text
docs/architecture/
  README.md          index: system overview, then one "Read when" line per note
  concepts/{concept}.md
  patterns/{pattern}.md
```

`docs/guidelines/` holds technology pitfalls only. Project patterns live in `docs/architecture/patterns/`.

## Process

1. **Detect the mode** and state it in one line:

   | Mode | When | Reference |
   |---|---|---|
   | Discover | `docs/architecture/` missing (also when older `docs/*.md` concept docs exist) | `references/discover.md` |
   | Update | A story's Review is done, or the user names a story or change | `references/update.md` |
   | Audit | The user asks to check, refresh, sync or audit docs | `references/audit.md` |

   Unclear: ask, with a recommendation. Load only that mode's reference plus `references/note-templates.md`.
2. **Design judgment.** Invoke the `architect` skill and load the references the mode names (concepts, patterns).
3. **Run the mode** as its reference describes.
4. **Write** the confirmed notes and `docs/architecture/README.md`. Add or fix doc comments in source files where a fact is file-local.
5. **Route.** Code problems, drift outside scope and deferred notes are discovered work.

## Output

- Notes in `docs/architecture/concepts/` and `docs/architecture/patterns/`, index in `docs/architecture/README.md`.
- Update mode: one History row in `{story_path}_index.md`, type Documentation, listing the notes changed.
- Report: notes created or changed, patterns with status changes, drift found, open design questions.

Finish with the hub's finish checklist.
