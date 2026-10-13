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
| `practice` | `practices/` | A reusable way of working, or an anti-practice to avoid |

## Evidence and Validation Frontmatter

Notes recording a decision, pattern, or claim likely to go stale should carry:

```yaml
evidence:
  - path or experiment reference
status: proposed | validated | superseded
last_validated: YYYY-MM-DD
supersedes: optional-note-link
```

- `evidence` - path(s) or experiment references backing the claim. Distinguishes observed evidence from inferred lesson; a note with no `evidence` entries is an inference, not an observation, and should be treated as `proposed`.
- `status` - `proposed` (not yet confirmed by use), `validated` (confirmed by real use or review), `superseded` (replaced - keep `supersedes` pointing at what replaced it, or note what replaces this one).
- `last_validated` - the date this note's claim was last confirmed still true. When validated notes conflict, retrieval reports all of them, leading with the most recent `last_validated`.
- `supersedes` - relative link to the note this one replaces, when applicable.

These fields are optional for concept notes with no claim to go stale (pure definitions), required for `decision` and `practice` notes that make a durable claim.

## Tags

The Tags table in `README.md` is the only tag list. Use tags from it; propose a new tag there before using it.

## Naming Conventions

- Filenames: kebab-case, no spaces, no special characters, valid unix
- All notes must have `title:` frontmatter
- No wikilinks anywhere - use relative markdown links: `[Title](../concepts/file.md)`
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
- Your own notes or summaries (those are atomic notes - they belong in the typed folders)
- One-off sources you will not reference again
- Duplicate copies (use URLs in notes instead)

Organisation: file flat initially. Create a topic subfolder when 3+ source files cover the same topic (e.g. `sources/ai-memory/`, `sources/auth-patterns/`). Never use type-based names (decisions/, practices/, research/) in sources/.

When you extract atomic notes from a source file, add `resource: sources/{path}` to those notes' frontmatter.

## OKF Alignment

This schema follows the Open Knowledge Format (OKF) conventions with one deviation:
- `_index.md` naming deviates from OKF's `index.md` - retained for Obsidian sort-order benefit (underscore sorts before alphabetical entries)

## Link Rules

- Notes in `knowledge/`, `docs/`, `projects/` may link to each other freely
- Notes in `personal/` may link outward to any of the above
- Notes outside `personal/` must never link into `personal/`
