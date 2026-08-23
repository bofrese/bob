# Bootstrap

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

   ## Evidence and Validation Frontmatter

   Notes recording a decision, pattern, or claim likely to go stale should carry:

   ```yaml
   evidence:
     - path or experiment reference
   status: proposed | validated | superseded
   last_validated: YYYY-MM-DD
   supersedes: optional-note-link
   ```

   - `evidence` — path(s) or experiment references backing the claim. Distinguishes observed evidence from inferred lesson; a note with no `evidence` entries is an inference, not an observation, and should be treated as `proposed`.
   - `status` — `proposed` (not yet confirmed by use), `validated` (confirmed by real use or review), `superseded` (replaced — keep `supersedes` pointing at what replaced it, or note what replaces this one).
   - `last_validated` — the date this note's claim was last confirmed still true. Retrieval prefers notes with a recent `last_validated` over stale ones when several conflict.
   - `supersedes` — relative link to the note this one replaces, when applicable.

   These fields are optional for concept notes with no claim to go stale (pure definitions), required for `decision` and `pattern` notes that make a durable claim.

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
   - No date prefix for processed notes (date is in `timestamp:` frontmatter)
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

   When you extract atomic notes from a source file, add `resource: sources/{path}` to those notes' frontmatter.

   ## OKF Alignment

   This schema follows the Open Knowledge Format (OKF) conventions with one deviation:
   - `_index.md` naming deviates from OKF's `index.md` — retained for Obsidian sort-order benefit (underscore sorts before alphabetical entries)

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
