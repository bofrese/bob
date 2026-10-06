# Note Templates

All notes follow `bob:writing`. Headings that do not apply to a concept are left out. Links per the rules in the `bob:document` skill.

## Concept note - `docs/architecture/concepts/{concept}.md`

```markdown
# {Concept name}
*Last verified: {YYYY-MM-DD}*

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

## Depends on / used by
- Depends on: [Other concept](other-concept.md)
- Used by: [Other concept](other-concept.md)

## Patterns
- [Pattern name](../patterns/pattern-name.md)

## Gotchas
{What trips up a developer or AI working here the first time.}

**Verified by:** {optional: tests, BDD scenarios or executable specs, as backticked paths}
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

```markdown
# Architecture

## TL;DR
{2-3 bullets: what the system does and where to start.}

## Concepts
| Concept | Summary | Note |
|---|---|---|
| Authorization policy | Who may do what, checked at the service boundary | [authorization-policy.md](concepts/authorization-policy.md) |

## Patterns
| Pattern | Status | Summary | Note |
|---|---|---|---|
| Wrapped integrations | established | External APIs behind one adapter per provider | [wrapped-integrations.md](patterns/wrapped-integrations.md) |
```
