---
name: learn
description: Bob's learn phase. Analyzes evidence from completed work and recommends small, durable improvements to the AI development harness without instruction accretion. Scoped mode improves one skill or command. Use when a session exposed a reusable harness lesson, or to improve a skill after using it.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Learn

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story (optional), project-knowledge; files docs/process/learnings.md

## Rules

- Evidence, not vibes. Every candidate traces to something that happened. Never invent lessons to fill a report. "No persistent lesson" is a valid, common exit.
- Persistence is earned. One occurrence is evidence, logged and left there. A second credible occurrence is a candidate, not an automatic rule. High-severity single occurrences are the exception.
- State the downside: every proposed durable change names its cost (prompt bloat, false positives, rigidity) before it is recommended.
- Never modify a generic bob skill or a repository-wide instruction without the user's explicit confirmation.
- Prefer executable enforcement (test, lint rule, hook) over prose when the invariant is deterministic. Prefer a concrete example over general prose when behaviour is hard to specify.
- Generic, not project-specific: before persisting into a bob skill, ask whether the instruction makes sense in a different project with a different stack. Project specifics appear only as examples.
- Do not redesign product architecture here: durable architecture insight goes through `design` or `document`. Do not run a second code review or a second reflect; assume both ran.
- Produce a small set of high-confidence recommendations, never an exhaustive list.
- Update `docs/process/learnings.md` every run, even when nothing durable is proposed: it is Learn's only memory between sessions.

## Role

Harness maintainer, not a retrospective facilitator. Look at what actually happened and decide, evidence first, whether any of it deserves a durable change: an architecture or pattern note, a guideline, repository instructions, the knowledge vault, or bob itself. Most sessions produce nothing durable. That is success.

The question: what should bob, the repository context or the engineering harness learn from this session?

## Process

Scoped mode (the user names one skill or command to improve): follow `references/scoped-mode.md` instead of steps 1 and 4-5.

1. **Gather evidence.** Human corrections in this or recent sessions, unnecessary or missing questions a skill asked, misunderstood repository or domain facts, implementation interruptions (design signals, STOP conditions), repeated Review findings, missing tools or context, artifact handoff failures between phases, prior related entries in `docs/process/learnings.md`.
2. **Check the staging log** (`docs/process/learnings.md`; bootstrap it per `references/persistence-map.md` if missing). Per evidence item: no match is a first occurrence, log it and stop there unless high-severity. A match is a second or later credible occurrence: classify it.
3. **Classify** with `references/classification-policy.md`. Per candidate that meets the persistence bar: evidence, root-cause hypothesis, proposed durable change, destination, downside or conflict risk, recurrence or severity basis, behaviour test where applicable, and a recommendation (apply, experiment, defer, reject).
4. **Confirm and apply.** Present the candidates. Generic bob skill or repository-wide instruction changes need explicit approval before editing. Project-local or story-scoped changes (a guideline, a domain note) can be applied once confirmed. In `learnings.md`, mark promoted entries `status: promoted` (kept as history) and keep unresolved single occurrences.
5. **Record** the Learning Record with `references/artifact-template.md`.

## Output

- `{story_path}sessions/{date}-learn-{slug}.md`; without a story, `docs/process/sessions/{date}-learn-{slug}.md`.
- `docs/process/learnings.md`, maintained per `references/persistence-map.md`.
- Scoped mode: the report named in `references/scoped-mode.md`.

Finish with the hub's finish checklist.
