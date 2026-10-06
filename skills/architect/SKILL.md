---
name: architect
description: What good architecture means in bob - whole-system comprehensibility lenses, semantic generalization, domain placement, deep modules and developer-facing interfaces, source readability, concept identification, design smells, codebase patterns and drift. Invoked by /bob:design, /bob:plan, /bob:review and bob:document; not user-invocable.
user-invocable: false
---

# Architect - What Good Design Means

The single source of design judgment in bob. Callers own process and file I/O; this skill owns how to see concepts, patterns and quality. It does not own note templates or where notes live (`bob:document` owns those).

## Fundamental question

Can an experienced developer understand this system concept by concept, and does this change keep it that way?

## Stance

- Lenses, not a scorecard. SOLID, DRY, DDD and similar ideas are diagnostics, never objectives.
- Concept first, framework second.
- Surface smells, competing patterns and drift as questions with evidence. Never fix them silently. The human decides.
- Prefer a system that gets simpler as it grows: later features can reveal the deeper concept behind earlier special cases.

## References

Load only the reference for the job at hand.

| Job | Reference |
|---|---|
| Judge a design or abstraction for whole-system simplicity | `references/design-lenses.md` |
| Name things, find boundaries, decide where code belongs | `references/placement.md` |
| Shape an interface, judge a source file's reading order | `references/interfaces-and-readability.md` |
| Find the concepts of a system, test note atomicity, spot design smells | `references/concepts.md` |
| Recognize codebase patterns, assign status, detect drift | `references/patterns.md` |
