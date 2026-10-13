---
name: architect
description: Bob's architecture judgment - whole-system comprehensibility lenses, domain placement, deep modules, interfaces, source readability, concept identification, design smells, codebase patterns and drift. Use when judging a design, an abstraction, where code belongs, or architectural fit.
license: Apache-2.0
---

# Architect - What Good Design Means

The single source of design judgment in bob. Callers own process and file I/O; this skill owns how to see concepts, patterns and quality. It does not own note templates or where notes live (the `document` skill owns those).

## Fundamental question

Can an experienced developer understand this system concept by concept, and does this change keep it that way?

## Stance

- **Strategic, not tactical** (Ousterhout). The question is not only "how do we make this work?" but "how does this change fit the system, and what does it do to the design over time?"
- Lenses, not a scorecard. SOLID, DRY, DDD and similar ideas are diagnostics, never objectives.
- Concept first, framework second.
- Surface smells, competing patterns and drift as questions with evidence. Never fix them silently. The human decides.
- Prefer a system that gets simpler as it grows: later features can reveal the deeper concept behind earlier special cases.

## Fit questions

Expose these for every change. The human answers them; the AI raises them with evidence.

- Does it extend an existing concept, change one, or introduce a new one?
- Does it reveal a more general pattern that was not visible before?
- Should an existing assumption be challenged?
- Can the system become simpler through generalization?
- Should refactoring happen before the feature?
- Do the implementation choices preserve or weaken the architecture?
- Does it touch an area documented as inconsistent (a ⚠️ concept note, a `competing` pattern)? Converge it now, or add one more variant?

## References

Load only the reference for the job at hand.

| Job | Reference |
|---|---|
| Judge a design or abstraction for whole-system simplicity | `references/design-lenses.md` |
| Name things, find boundaries, decide where code belongs | `references/placement.md` |
| Shape an interface, judge a source file's reading order | `references/interfaces-and-readability.md` |
| Find the concepts of a system, test note atomicity, spot design smells | `references/concepts.md` |
| Recognize codebase patterns, assign status, detect drift | `references/patterns.md` |
