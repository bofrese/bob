---
name: library
description: Bob's knowledge vault librarian for knowledge/. Processes the inbox into atomic notes, ingests external sources (URL or file), searches notes, runs vault health checks, shows status, and bootstraps the vault. Use when the user wants to file, find or organise project knowledge.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Library

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: files knowledge/README.md

Paths to `references/`, `scripts/` and `assets/` are relative to this skill's folder (the base directory shown when it loads). Run scripts with `python3` from the project root.

## Rules

- Never create or change a note without running `references/reconcile.md` first and getting the user's confirmation.
- Never delete files. Move them to `knowledge/_INBOX/_processed/` or `knowledge/sources/`.
- Move `.md` files with `obsidian move "path=<from>" "to=<to>"`. Obsidian is required for vault moves: check that `obsidian vault info=path 2>/dev/null` matches the project root, else stop and ask the user to open the vault.
- Tags come from the Tags table in `knowledge/README.md`, the only canonical list. Propose a new tag with a description and add it to the table before using it.
- Never add a note to an index without the user's confirmation.

## Modes

The first argument picks the mode. No argument, or one not listed: status.

| Mode | Use when | How |
|---|---|---|
| status (default) | What is in the vault, what to do next | Status below |
| process | File the inbox (`knowledge/_INBOX/`) into atomic notes | `references/mode-process.md` |
| ingest `<url-or-file>` | Turn an external source into notes | `references/mode-ingest.md` |
| retrieve `<query>` | Search the vault | Retrieve below |
| organise | Vault health: lint, integrity audit, cross-links, tags, MOCs | `references/mode-organise.md` |
| bootstrap | `knowledge/` does not exist | `python3 scripts/bootstrap.py` |

If `knowledge/` does not exist, run bootstrap first, say "Knowledge vault created at `knowledge/`. Continuing...", then run the requested mode. Bootstrap creates the typed folders, `_INBOX/`, `_MOC/`, `sources/`, `_schema.md` (note types, evidence fields, tag and naming rules, from `assets/`), `README.md`, the folder indexes, `_suggestions.md`, the `.gitignore` entries `knowledge/_INBOX/` and `personal/`, and `personal/daily/`, `personal/weekly/`, `personal/scratchpad.md`. It never overwrites a file.

## Status

1. Count: inbox items (files in `knowledge/_INBOX/` except `_processed/`), files per typed folder, MOCs, source files, pending suggestions (non-empty lines in `_suggestions.md` after the heading), tags in the README Tags table.
2. Show the last modified date of `knowledge/README.md`.
3. Present the summary and ask what to do next.

## Retrieve

1. Read `knowledge/README.md`.
2. Obsidian vault active for this project (`obsidian vault info=path 2>/dev/null` matches the project root): `obsidian search query="<user terms>"`. It returns excerpts.
3. Otherwise `grep -rl "<user terms>" knowledge/`, then read the relevant excerpts.
4. Present the matching excerpts with file paths. Ask whether to open any in full.

The automatic, read-only retrieval at the start of every phase is the hub's `project-knowledge` loader.

## Scripts

| Script | Does |
|---|---|
| `scripts/bootstrap.py [root]` | Create the vault; idempotent |
| `scripts/log_append.py <mode> "<summary>"` | Append a run entry to `knowledge/log.md` |
| `scripts/git_scope.py "<since>" knowledge` | Notes changed since a timestamp |
| `scripts/lint.py knowledge` | Frontmatter and broken-link audit (JSON) |
| `scripts/orphan.py knowledge` | Notes with no inbound links (JSON) |

Finish with the hub's finish checklist.
