---
allowed-tools: Bash(*), Read, Write, Edit
description: Manage the project knowledge vault. Five modes: process (inbox to notes), retrieve (search), organise (vault health), weekly (personal digest), status (no args). Bootstraps knowledge/ if it doesn't exist.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Mode Detection

Determine mode from args:
- `process` → Process mode
- `retrieve [query]` → Retrieve mode
- `organise` → Organise mode
- `weekly` → Weekly mode
- No args (or unrecognised args) → Status mode

If `knowledge/` does not exist: run Bootstrap first, then enter the requested mode (or Status if no args given).

## Bootstrap

Run when `knowledge/` does not exist. Steps:

1. Create folders: `knowledge/decisions/`, `knowledge/concepts/`, `knowledge/research/`, `knowledge/patterns/`, `knowledge/_INBOX/`, `knowledge/_INBOX/_processed/`, `knowledge/_MOC/`, `knowledge/sources/`

2. Write `knowledge/_schema.md`:
   ```markdown
   ---
   title: Knowledge Schema
   ---
   # Knowledge Schema

   ## Note Types

   | Type | Subfolder | When to use |
   |------|-----------|-------------|
   | `decision` | `decisions/` | An architectural, design, or process decision with rationale |
   | `concept` | `concepts/` | A technology, framework, or domain concept worth defining |
   | `research` | `research/` | External findings, benchmarks, tool evaluations |
   | `pattern` | `patterns/` | A reusable solution pattern or anti-pattern |

   ## Tag Taxonomy

   Tags are free-form but should be drawn from this list first. Add new tags here as they emerge.

   - `ai` - AI/LLM-related
   - `obsidian` - Obsidian tooling
   - `architecture` - system design decisions
   - `tooling` - developer tools and configuration
   - `process` - workflow and process patterns
   - `cli-tooling` - command-line interfaces and tooling

   ## Naming Conventions

   - Filenames: kebab-case, no spaces, no special characters, valid unix
   - All notes must have `title:` frontmatter
   - No wikilinks anywhere — use relative markdown links: `[Title](../concepts/file.md)`
   - No date prefix for processed notes (date is in `created:` frontmatter)
   - Inbox files: `YYYY-MM-DD-slug.md`
   - MOC files: `_MOC/kebab-case-topic.md` with `title:` property
   - Source files: `YYYY-MM-DD-{short-slug}.{ext}` (e.g. `2026-06-17-spec-upgrade.md`)

   ## Sources Guidelines

   The `sources/` folder stores *raw* source materials before they are broken down into atomic notes. Include in sources/:
   - Research papers, articles (PDF or markdown excerpt)
   - Specification documents
   - Authoritative reference material you might cite or return to
   - Book chapters or excerpts you have synthesized

   Keep *out* of sources/:
   - Your own notes or summaries (those are atomic notes — they belong in the typed folders)
   - One-off sources you will not reference again
   - Duplicate copies (use URLs in notes instead)

   Organisation: file flat initially. Create a topic subfolder when 3+ source files cover the same topic (e.g. `sources/ai-memory/`, `sources/auth-patterns/`). Never use type-based names (decisions/, patterns/, research/) in sources/.

   When you extract atomic notes from a source file, add `source: sources/{path}` to those notes' frontmatter.

   ## Link Rules

   - Notes in `knowledge/`, `docs/`, `projects/` may link to each other freely
   - Notes in `personal/` may link outward to any of the above
   - Notes outside `personal/` must never link into `personal/`
   ```

3. Write `knowledge/README.md`:
   ```markdown
   ---
   title: Knowledge Index
   ---
   # Knowledge Index
   *Updated: YYYY-MM-DD*

   ## About this vault
   [2-3 sentence description of what knowledge has been accumulated here]

   ## Folders

   | Folder | What you'll find |
   |--------|-----------------|
   | [decisions/](decisions/_index.md) | The "why" behind choices — architectural, design, and process decisions with rationale |
   | [concepts/](concepts/_index.md) | Shared vocabulary — technology and domain concepts worth defining |
   | [research/](research/_index.md) | What we learned from outside — external findings, benchmarks, tool evaluations |
   | [patterns/](patterns/_index.md) | How to do it right — reusable solution patterns and anti-patterns |
   | [sources/](sources/) | Originals before decomposition — raw articles, papers, specs. Topic subfolders emerge at 3+ files per topic. |

   ## Tags

   Tags are the cross-cutting discovery layer. Click any tag to see all notes with that tag. Every note must use tags from this list only — new tags are proposed and confirmed here before use.

   | Tag | Covers |
   |-----|--------|
   | #ai | AI/LLM concepts, tools, and patterns |
   | #architecture | System design decisions and structural choices |
   | #process | Workflow patterns and process design |
   | #tooling | Developer tools, configuration, CLI |
   | #knowledge-management | Knowledge systems, PKM, memory architecture, vault design |
   | #naming | Naming conventions and disambiguation |
   | #writing | Documentation and prose guidelines |
   | #context-loading | AI context management and loading strategies |
   | #obsidian | Obsidian-specific tooling and integration |

   ## Maps of Content

   | MOC | Description |
   |-----|-------------|
   | (none yet) | |
   ```

4. Write subfolder indexes (heading and frontmatter only, empty list):
   - `knowledge/decisions/_index.md` (title: Decisions)
   - `knowledge/concepts/_index.md` (title: Concepts)
   - `knowledge/research/_index.md` (title: Research)
   - `knowledge/patterns/_index.md` (title: Patterns)

5. Write `knowledge/_suggestions.md`:
   ```markdown
   ---
   title: Knowledge Suggestions
   ---
   # Knowledge Suggestions

   Items for the next organise run. Cleared after organise processes them.
   ```

6. Append to `.gitignore` (check entries don't already exist first):
   ```
   knowledge/_INBOX/
   personal/
   ```

7. Create `personal/daily/`, `personal/weekly/` (skip if exists). Write `personal/scratchpad.md` if it doesn't exist:
   ```markdown
   ---
   title: Scratchpad
   ---
   # Scratchpad
   ```

Report: "Knowledge vault created at `knowledge/`. Continuing..."

## Status Mode

1. Count: inbox items (files in `knowledge/_INBOX/` excluding `_processed/`), files per typed subfolder, MOC count, source files, pending suggestions (non-empty lines in `_suggestions.md` after the heading), tag count from README Tags table
2. Show last modified date of `knowledge/README.md`
3. Present summary and ask what to do next

## Process Mode

Processes `knowledge/_INBOX/` items into atomic notes, one file at a time.

1. List all files in `knowledge/_INBOX/` (excluding `_processed/`). If empty: "Inbox is empty."
2. For each file, in order:
   a. Read the file
   b. Identify distinct atomic concepts it contains — one inbox file may yield multiple notes
   c. For each candidate note:
      - Propose: title, type, tags, filename (kebab-case slug, no date), target subfolder, one-line description for index
      - Tags: read the Tags table in `knowledge/README.md` first — select from existing tags only. If no existing tag fits well, propose a new tag with a one-line description; get confirmation; add it to the README Tags table before using it on the note. The description is the curation — it must be precise enough that future notes land on the right tag without inventing near-duplicates.
      - Present proposal. Wait for approval — user may correct any field before confirming
      - On approval:
        - Write to `knowledge/<type-subfolder>/<slug>.md` using the note format
        - Append entry with description to subfolder `_index.md`
        - Check existing MOCs; add entry to any that apply
        - Check `_suggestions.md` for related MOC candidates; increment mention count if present
   d. Assess the original file:
      - Authoritative source (article, research paper, major spec): move to `sources/` using `obsidian move "path=<from>" "to=<to>"` if vault is active (`obsidian vault info=path 2>/dev/null` matches `$PWD`), else `mv`. Name it: `{YYYY-MM-DD}-{short-slug}.{ext}`. Choose a topic subfolder if 3+ source files already cover the same topic (e.g. `sources/ai-memory/`); otherwise file flat. Never use the typed folder names (decisions/, patterns/, research/) in sources/. Add `source: sources/{path}` to atomic notes derived from it.
      - Ephemeral capture (rough notes, quick thought): move to `_INBOX/_processed/` using `obsidian move` (vault active) or `mv` (vault offline).
   e. Append any new patterns noticed to `_suggestions.md` (MOC candidates, tag inconsistencies, schema gaps)

3. Update `knowledge/README.md` if needed: if new tags were added during this run, add them to the Tags table. The Folders table needs no count updates — counts are not tracked.
4. Report: files processed, notes created, moved to sources, moved to `_processed/`

Note format for written notes:
```markdown
---
title: <title>
type: <decision|concept|research|pattern>
tags: [tag1, tag2]
created: YYYY-MM-DD
story: <STORY-ID>  # if captured in story context
---

# <title>

[Content — atomic, self-contained, 5-15 lines]

**Why it matters:** [one sentence]
```

## Retrieve Mode

1. Read `knowledge/README.md`
2. If Obsidian vault is active for this project (`obsidian vault info=path 2>/dev/null` returns a path matching `$PWD`): `obsidian search query="<user terms>"` — returns excerpts, token-efficient
3. Otherwise: `grep -rl "<user terms>" knowledge/` to find files, then read relevant excerpts
4. Present matching excerpts with file paths
5. Ask if any should be opened in full

## Organise Mode

0. **Vault integrity audit** (always run first, before reading suggestions):
   a. **Inbox stubs in typed folders** — find `.md` files in `decisions/`, `concepts/`, `research/`, `patterns/` with `type: inbox` in frontmatter. Move each to `_INBOX/_processed/` using `obsidian move` (vault active) or `mv` (vault offline). These are inbox originals that were never properly processed.
   b. **Orphaned notes** — for each typed subfolder, compare files on disk against entries in `_index.md`. Files present on disk but absent from the index are orphaned. Present proposed index entries and add after confirmation.
   c. **README consistency** — verify the Folders table lists all typed subfolders. Verify `_schema.md` tag governance rule points to README (no mirrored tag list). Rebuild README if Folders table is incomplete.
   d. **Dead source: references** — scan all notes for `source:` frontmatter values. For each, verify the referenced path exists. Report dead references (do not auto-fix — ask user).
   Present audit findings. If all clean, say so and continue.

1. Read `knowledge/_suggestions.md` as the agenda. If empty: note "No pending suggestions."
2. For each agenda item: load relevant vault context and decide action
3. For each structural change (new MOC, tag rename, type fix, schema update): show proposed change and wait for confirmation before executing

4. **Active librarian maintenance** (propose each action, confirm before executing):
   a. **Cross-linking** — for newly indexed or recently modified notes, scan for related notes sharing tags or overlapping keywords. Propose adding relative markdown links where they would aid discovery. Show candidate pairs before adding.
   b. **Tag consistency** — run `grep -rh "^tags:" knowledge/decisions/ knowledge/concepts/ knowledge/research/ knowledge/patterns/ 2>/dev/null` to collect all used tags. Read the Tags table from `knowledge/README.md`. For each tag found in notes but absent from the README table: either propose adding it with a description (if it names a genuinely new domain) or propose renaming it to the closest canonical tag (if it overlaps an existing one). Use `obsidian search "query=tag:<old-tag>"` (vault active) or `grep -rl "<old-tag>" knowledge/` to find all affected notes. After any additions or renames, update `knowledge/README.md` Tags table only — do not mirror in `_schema.md`.
   c. **Sources hierarchy** — if `sources/` contains 3+ ungrouped files clearly sharing a topic, propose creating a topic subfolder and moving them via `obsidian move`.
   d. **MOC candidates** — if 4+ notes share tags or topic keywords not yet covered by an existing MOC, append to `_suggestions.md`: `MOC candidate: <topic> (N notes)`.

5. If Tags table, Folders table, or MOC list changed: rebuild root `knowledge/README.md`
6. Clear resolved items from `_suggestions.md`; keep unresolved with a note
7. Report changes made

## Weekly Mode

1. Read all `personal/daily/YYYY-MM-DD.md` files for the current week (Monday-Sunday)
2. Compile summary: stories worked on, key decisions made, sessions logged
3. Present summary
4. Run guided retrospective: what went well, what to improve, what to carry forward, energy and focus observations
5. Write to `personal/weekly/YYYY-WXX.md` (e.g. `2026-W23.md`)

## Rules
- Never delete files — move to `_INBOX/_processed/` or `sources/` only
- For all moves and renames: if vault is active (`obsidian vault info=path 2>/dev/null` returns a path matching `$PWD`), use `obsidian move "path=<from>" "to=<to>"` — Obsidian updates all backlinks automatically. Fall back to `mv` if vault is offline (warn user: backlinks will not be updated).
- Never add a note to any index without user confirmation (process mode)
- Filenames: kebab-case, no date prefix for processed notes; `YYYY-MM-DD-slug.md` for inbox only
- All notes must have `title:` in frontmatter
- Progressive disclosure: load only what the current mode needs; do not load the entire vault upfront

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
