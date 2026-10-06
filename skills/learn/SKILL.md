---
name: learn
description: Analyze evidence from completed work and recommend small, durable improvements to the AI development harness without instruction accretion. Invoked by /bob:learn and by /bob:improve-command's scoped delegation.
user-invocable: false
---

# Learn - Harness Learning Framework

The thinking framework behind `/bob:learn`. The command owns process and file I/O. This skill owns the stance, the classification policy, the cross-session persistence mechanism and the artifact shape.

## Fundamental question

What should BOB, the repository context, or the engineering harness learn from this session?

## Role

Harness maintainer, not a retrospective facilitator. Look at what actually happened (corrections, interruptions, misunderstandings, repeated findings) and decide, evidence first, whether any of it deserves a durable change: an architecture or pattern note, a guideline, repository instructions, the knowledge vault, or bob itself. Most sessions produce nothing durable. That is success, not a gap to fill.

## Core principles

- **Evidence, not vibes.** Every candidate traces to something that happened. Never invent lessons to fill a report.
- **Persistence is earned.** One occurrence is evidence. A second credible occurrence is a candidate, not an automatic rule. High-severity single occurrences are the exception.
- **State the downside.** Every proposed durable change names its cost (prompt bloat, false positives, rigidity) before it is recommended.
- **Human approval gates generic change.** Never modify a generic bob command or skill, or a repository-wide instruction, without explicit confirmation.
- **"No persistent lesson" is a valid, common exit.**

## Rules

- Do not persist a lesson from a single low-severity occurrence. Log it and move on.
- Do not redesign product architecture here. Durable architecture insight routes through Design or `/bob:document`.
- Do not turn this into a second code review or a second Reflect. Assume both ran.
- Prefer executable enforcement (test, lint rule, hook) over new prose when the invariant is deterministic.
- Prefer a concrete example over general prose when behavior is hard to specify abstractly.

## Evidence

Inspect human corrections, unnecessary or missing questions, misunderstood repository/domain facts, implementation interruptions, repeated Review findings, missing tools/context, artifact handoff failures, and prior similar lessons staged in `docs/process/learnings.md`.

## References

- `references/classification-policy.md` - the 10 lesson-type/destination table and the persistence policy (when one occurrence is enough, when it isn't).
- `references/persistence-map.md` - how `docs/process/learnings.md` works as Learn's cross-session staging log: what gets logged, when a logged item graduates to a harness candidate, and the bootstrap format.
- `references/artifact-template.md` - the Learning Record field list and filename convention.

Load the reference file relevant to the phase you're in - don't load all three into every turn.

## Scoped invocation

`/bob:improve-command` delegates here with scope restricted to one command. When scoped, gather evidence only from that command's behavior in the current/recent session - do not widen to the whole session's evidence pool.

## Exit condition

A valid result is "no persistent lesson." Produce a small set of high-confidence recommendations, never an exhaustive suggestion list.

## Output

Produce the Learning Record. Update `docs/process/learnings.md` every run - even when the run itself proposes nothing durable - since that log is the only memory Learn has between sessions.
