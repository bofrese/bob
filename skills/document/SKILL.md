---
name: document
description: Write and maintain a project's canonical architecture knowledge as concept-first atomic notes in docs/architecture/ (concepts, patterns, README index). Modes Discover, Update, Audit. Invoked by /bob:document; uses bob:architect for design judgment; not user-invocable.
user-invocable: false
---

# Document - Canonical Architecture Notes

The framework behind `/bob:document`. The command owns process and file I/O. This skill owns the stance, the modes, the docs layout and the note templates. Design judgment (what a concept is, pattern status, smells, drift) comes from `bob:architect`.

## Fundamental question

How does the system work now, explained concept by concept, so that a developer or an AI can find the right code and change it safely?

## Role

Senior developer and technical writer, and a thinking partner. Map concepts and patterns from the actual code, ask the human about intent, and write what is true today. Never write aspirations.

## Core principles

- **State, not story.** Notes describe the current system. Design Records hold intent; handovers hold the change story. Notes absorb only enduring knowledge.
- **Concept first.** One atomic note per concept (`bob:architect` `references/concepts.md`). Framework details come second.
- **Small, linked, canonical.** Notes are the canonical architecture knowledge, organized like an Obsidian second brain: small atomic notes, explicit links, hierarchy and tags only where useful, low duplication, easy for humans to navigate and for AI to retrieve.
- **After implementation, against the code.** Notes describe the system that exists, never copied from a Design Record.
- **Local knowledge stays local.** File-local facts belong in names and doc comments, not in notes.
- **Human promotes.** Only the human sets a pattern to `established`, and confirms new notes before they are written in Discover.
- **No size budget, no zoom levels.** A note is as long as its concept needs. Large overview documents are generated views, produced only on request, never the source of truth.

## Rules

- One question at a time when discussing intent. Do not rush to writing.
- Do not refactor or modify application code. Adding or fixing doc comments is fine.
- Be honest about limitations, debt and rough edges.
- **Links point to docs only.** Markdown links `[text](path)` target `.md` files. Source paths, directories and scripts use backticks (`src/auth/policy.ts`).
- **Index first-column names are plain text.** Doc links go in a dedicated column. Never link to a directory.
- Key Files tables: path and purpose only. No line numbers.
- Every proposed move, migration or deletion of an existing doc is confirmed per file.

## Layout

```text
docs/architecture/
  README.md          index: one line per note, with link
  concepts/{concept}.md
  patterns/{pattern}.md
```

Guidelines (`docs/guidelines/`) hold technology pitfalls only. Project patterns live in `docs/architecture/patterns/`.

## Modes and references

| Mode | When | Reference |
|---|---|---|
| Discover | No `docs/architecture/` yet (also when older `docs/*.md` concept docs exist) | `references/discover.md` |
| Update | After Review, for a story: notes change to match what was built | `references/update.md` |
| Audit | Explicit drift or health check of existing notes and `docs/` | `references/audit.md` |

Note shapes for every mode: `references/note-templates.md`. Load only the mode reference in use.
