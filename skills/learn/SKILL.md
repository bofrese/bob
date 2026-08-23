---
name: learn
description: Analyze evidence from completed work and recommend small, durable improvements to the AI development harness without instruction accretion. Invoked by /bob:learn and by /bob:improve-command's scoped delegation.
user-invocable: false
---

# Learn — Harness Learning Framework

The thinking framework behind `/bob:learn`. The command file owns process and file I/O; this skill owns the classification policy, the persistence-across-sessions mechanism, and the artifact shape.

## Fundamental question

What should BOB, the repository context, or the engineering harness learn from this session?

## Evidence

Inspect human corrections, unnecessary or missing questions, misunderstood repository/domain facts, implementation interruptions, repeated Review findings, missing tools/context, artifact handoff failures, and prior similar lessons staged in `docs/process/learnings.md`.

## References

- `references/classification-policy.md` — the 10 lesson-type/destination table and the persistence policy (when one occurrence is enough, when it isn't).
- `references/persistence-map.md` — how `docs/process/learnings.md` works as Learn's cross-session staging log: what gets logged, when a logged item graduates to a harness candidate, and the bootstrap format.
- `references/artifact-template.md` — the Learning Record field list and filename convention.

Load the reference file relevant to the phase you're in — don't load all three into every turn.

## Scoped invocation

`/bob:improve-command` delegates here with scope restricted to one command. When scoped, gather evidence only from that command's behavior in the current/recent session — do not widen to the whole session's evidence pool.

## Exit condition

A valid result is "no persistent lesson." Produce a small set of high-confidence recommendations, never an exhaustive suggestion list.

## Output

Produce the Learning Record. Update `docs/process/learnings.md` every run — even when the run itself proposes nothing durable — since that log is the only memory Learn has between sessions.
