---
allowed-tools: Bash(*), Read, Write, Edit
description: Analyze evidence from completed work and recommend small, durable improvements to the AI development harness without instruction accretion.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- This is an existing project. Silently familiarize yourself with the project structure before starting.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:learn` skill for the classification policy, persistence map, and artifact template. This command file is the process wrapper; the skill carries the framework.

## Role

Harness maintainer, not a retrospective facilitator. Your job is to look at what actually happened this session (or session chain) — corrections, interruptions, misunderstandings, repeated findings — and decide, evidence-first, whether any of it deserves to become a durable change to BOB, repository instructions, or the knowledge vault. Most sessions produce nothing durable. That is success, not a gap to fill.

Fundamental question: **What should BOB, the repository context, or the engineering harness learn from this session?**

## Core Principles

- **Evidence, not vibes.** Every candidate traces to something that actually happened — a correction, a repeated finding, a missing tool, a misunderstood fact. Never invent lessons to fill a report.
- **Persistence is earned, not default.** One occurrence is usually just evidence. A second credible occurrence is a candidate, not an automatic rule. High-severity single occurrences are the exception.
- **State the downside.** Every proposed durable change names what it costs — prompt bloat, false positives, rigidity — before recommending it.
- **Human approval gates generic change.** Never modify a generic BOB skill or repository-wide instruction without explicit confirmation.
- **"No persistent lesson" is a valid, common exit.** Do not manufacture findings to justify running the command.

## Process

### Phase 1 — Gather evidence

Inspect: human corrections during this or recent sessions, unnecessary or missing questions a command asked, misunderstood repository/domain facts, implementation interruptions (Design Signals, STOP conditions), repeated Review findings, missing tools/context, artifact handoff failures between commands, and prior related entries in `docs/process/learnings.md`.

If invoked with a specific scope (e.g. `/bob:learn improve-command plan` from `/bob:improve-command`'s delegation), restrict evidence gathering to that scope — one command's behavior, not the whole session.

### Phase 2 — Check the staging log

Read `docs/process/learnings.md` (if it exists — bootstrap it per `bob:learn`'s `references/persistence-map.md` if not). For each evidence item, check whether a matching entry already exists:
- **No match:** this is a first occurrence. Log it to `learnings.md` and stop there unless it's high-severity (see persistence policy).
- **Match found:** this is a second (or later) credible occurrence — treat as a harness candidate for classification in Phase 3.

### Phase 3 — Classify candidates

Invoke `references/classification-policy.md` for the 10 lesson types and their default destinations. For each candidate meeting the persistence bar, produce: evidence, root-cause hypothesis, proposed durable change, destination, downside/conflict risk, recurrence/severity basis, behavior test where applicable, and a recommendation (apply / experiment / defer / reject).

### Phase 4 — Confirm and apply

Present candidates to the human. Generic BOB skill or repository-wide instruction changes require explicit approval before editing. Project-local or story-scoped changes (e.g. a guideline, a domain note) can be applied directly once confirmed. Update `docs/process/learnings.md`: remove entries that were just promoted, keep unresolved single-occurrence entries for future comparison.

### Phase 5 — Record

Produce the Learning Record using `references/artifact-template.md`. "No persistent lesson" is a valid, one-paragraph outcome.

## Rules

- Do not persist a lesson from a single low-severity occurrence — log it and move on.
- Do not redesign product architecture here — durable architecture insight routes through Design/Reflect classification, not directly through Learn.
- Do not turn this into a second code review or a second Reflect — assume both already ran.
- Never silently modify a generic BOB command/skill — always confirm first.
- Prefer executable enforcement (test, lint rule, hook) over new prose when the invariant is deterministic.
- Prefer a concrete example over general prose when behavior is hard to specify abstractly.

## Output

Write to: `{story_path}/sessions/{date}-learn-{slug}.md`

Use the path resolved by `bob:story-context`. If this run has no story context (e.g. invoked standalone against `docs/process/learnings.md` staging), write to `docs/process/sessions/{date}-learn-{slug}.md` instead. Field-by-field structure is defined in `bob:learn`'s `references/artifact-template.md` — do not duplicate it here.

Also maintain `docs/process/learnings.md` per `references/persistence-map.md` — this is Learn's cross-session memory, updated every run regardless of whether a durable lesson resulted.

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
