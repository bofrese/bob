# Note Templates

All notes follow the hub's writing rules. Headings that do not apply to a concept are left out. Links per the rules in the `document` skill.

## Layout for scanning

Readers scan for the one fact they need. Prefer more lines over denser lines.

- Lists of links or names: one item per bullet, never a comma-separated line. "Depends on" and "Used by" are separate `##` sections; leave out an empty one.
- A table whose cells hold clauses: make it an icon matrix (✅ ⚠️ ❌, `-` for not needed) with numbered notes below.
- A section with more than about 8 bold-labelled bullets: split it into `###` subsections.
- A family of similar items (types, formats, launch arguments): a table, one row per item.
- A procedure: a numbered list, one action per step, never one long sentence.
- A Mermaid diagram where the code has a state machine, a branching decision or a pipeline with more than 3 steps. Not where a table already says it.
- Index tables with more than about 10 rows: group them under `###` headings (for example by context), not in one long table.
- ⚠️ in the index means "inconsistent"; inside a note it means a risk (hub icon table). Say which in the index legend.

## Concept note - `docs/architecture/concepts/{concept}.md`

```markdown
# {Concept name}
*Last verified: {YYYY-MM-DD}* · *Consistency: ⚠️ inconsistent* {only when the note has an Inconsistencies section}

## TL;DR
{2-4 bullets: what it is, why it exists, where to start reading.}

## What and why
{What the concept is in domain terms, and why the system needs it. Framework details later.}

## Behavior
{What it guarantees and enforces. Rules, states, edge cases that matter to callers.}

## Where it lives
| File | Purpose |
|---|---|
| `path/to/entry` | Start here |

To change it: {where to look first, and what else must change with it.}

## Depends on
- [Other concept](other-concept.md) {optional short reason in parentheses}

## Used by
- [Other concept](other-concept.md)

## Patterns
- [Pattern name](../patterns/pattern-name.md)

## Gotchas
{What trips up a developer or AI working here the first time.}

## Inconsistencies
{Only when the concept is implemented in several ways without a stated reason. Per item: what differs, where (paths), the risk. No ⚠️ per item (the section already says it); 🔴 only where users can lose data or see wrong values without knowing. Close with one ❓ open question: converge on what?}

**Verified by:** {tests, BDD scenarios or executable specs, as backticked paths; "none" when nothing tests it}
```

## Pattern note - `docs/architecture/patterns/{pattern}.md`

```markdown
# {Pattern name}
*Status: established | emerging | competing* · *Last verified: {YYYY-MM-DD}*

## TL;DR
{1-3 bullets: the problem and how this codebase solves it.}

## Context
{When this kind of problem appears.}

## Forces
{What makes it non-trivial.}

## Approach
{How this codebase resolves it. For `competing`: one subsection per variant.}

## Why
{The design reasoning.}

## Examples
- `path/to/example` - {what it shows}

## Exceptions
{When not to apply it.}

## Open question
{Only for `competing` or `emerging`: the design question the human must answer.}
```

## Index - `docs/architecture/README.md`

The index is how the hub's project-knowledge loader picks which notes to load. A "Read when" cell names the tasks, symptoms or changes that make the note relevant, not what the note is.

```markdown
# Architecture

## TL;DR
{2-4 bullets: what the system does, its main shape, and how to use this index. If any note is marked ⚠️: one bullet saying that ⚠️ marks an area implemented in several ways, and a change there is the moment to converge, not to add another variant.}

## How it fits together
{The one system overview. 40 lines or fewer. Only what no single note can show:}
{- the main layers or parts, and the role of each (a table)}
{- the shape most work shares, e.g. a request lifecycle or a pipeline}
{- where knowledge or data lives, if it is spread over several stores}
{At most 1-2 diagrams, only where a diagram is clearer than a table (hub writing rules, Diagrams). Link to notes for detail.}

## Concepts
| Concept | Read when | Note |
|---|---|---|
| Authorization policy ⚠️ | Adding an endpoint, changing roles, or a request is denied unexpectedly | [authorization-policy.md](concepts/authorization-policy.md) |

## Patterns
| Pattern | Status | Read when | Note |
|---|---|---|---|
| Wrapped integrations | established | Calling a new external API, or changing a provider | [wrapped-integrations.md](patterns/wrapped-integrations.md) |
```
