---
allowed-tools: Bash(*), Read, Write, Edit
description: Analyze evidence from completed work and recommend small, durable improvements to the AI development harness without instruction accretion.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- This is an existing project. Silently familiarize yourself with the project structure before starting.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:learn` skill. It owns the role, principles, rules, classification policy, persistence map and artifact template.

## Process

### Phase 1 - Gather evidence

Inspect: human corrections during this or recent sessions, unnecessary or missing questions a command asked, misunderstood repository or domain facts, implementation interruptions (Design Signals, STOP conditions), repeated Review findings, missing tools or context, artifact handoff failures between commands, and prior related entries in `docs/process/learnings.md`.

If invoked with a specific scope (e.g. `/bob:learn improve-command plan` from `/bob:improve-command`), restrict evidence gathering to that scope.

### Phase 2 - Check the staging log

Read `docs/process/learnings.md` (bootstrap it per `bob:learn` `references/persistence-map.md` if missing). For each evidence item:
- **No match:** first occurrence. Log it to `learnings.md` and stop there unless it is high-severity.
- **Match found:** second or later credible occurrence. Classify it in Phase 3.

### Phase 3 - Classify candidates

Use `references/classification-policy.md`. For each candidate that meets the persistence bar, produce: evidence, root-cause hypothesis, proposed durable change, destination, downside or conflict risk, recurrence or severity basis, behavior test where applicable, and a recommendation (apply / experiment / defer / reject).

### Phase 4 - Confirm and apply

Present candidates to me. Generic bob skill or repository-wide instruction changes need my explicit approval before editing. Project-local or story-scoped changes (a guideline, a domain note) can be applied once confirmed. Update `docs/process/learnings.md`: mark promoted entries `status: promoted` (keep them as history), keep unresolved single-occurrence entries.

### Phase 5 - Record

Write the Learning Record using `references/artifact-template.md`.

## Output

Write to: `{story_path}/sessions/{date}-learn-{slug}.md`. Without story context (standalone run against `docs/process/learnings.md`), write to `docs/process/sessions/{date}-learn-{slug}.md`.

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.

Also maintain `docs/process/learnings.md` per `references/persistence-map.md`, every run.

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
