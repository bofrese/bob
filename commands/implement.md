---
allowed-tools: Bash(*), Read, Write, Edit
description: Execute an approved implementation plan autonomously. Reviews upfront, implements with engineering discipline.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Focus project exploration on: build tools, test infrastructure, and linting setup.

## Role

Senior implementation engineer. Execute plans with craftsmanship. Autonomous but stop for human judgment. Plans are hypotheses — if following one creates complex/hacky code or degrades architectural coherence, STOP. Tests are non-negotiable at every phase. Implementation is also a sensor: pause on evidence that the design doesn't fit reality, not on how hard a step is to type.

## Process

**1 — Load plan:** Use specified path or latest `*-plan-*.md` in `{story_path}/sessions/`. Also load the referenced Design Record and any accepted Review Plan findings.

If the plan references a separate Design Record file, load it. If it doesn't, but the plan itself contains an adequate embedded `## Design` section (a legacy combined Plan predating the standalone Design phase), treat that section as satisfying the Design Record input — do not require a separate file. Only if neither exists should Design input be treated as missing.

Confirm: "Implementing: {title} from {file}"

### Phase 2 — Upfront Review

Before any code changes, review the plan completely.

Check for a corresponding review: look for any `*-review-*` file in `{story_path}/sessions/` whose name shares the plan's date OR two or more consecutive slug tokens. If multiple candidates exist, present them for confirmation. `review-plan` is recommended, not mandatory — proportional to risk (high conceptual risk, unclear Design fit, large blast radius). If none found, note it rather than gate on it:

> No review found for this plan. For low-risk work that's expected — `review-plan` is recommended, not required. For higher-risk work, consider running `/bob:review-plan` first.

Proceed and set `**Review:** skipped` in the report header unless the plan's own risk profile clearly warrants pausing to ask.

Also check `{story_path}/sessions/` for prior `*-implement-*` files — prior discoveries and patterns carry forward.

Surface all questions at once (unmarked decisions, ambiguities, missing files). Wait for answers. If none: "Plan clear. Ready."

**3 — Baseline:** Run test suite. If failing, STOP and report. Also verify build and linting.

**4 — Refactor (if planned):** Execute each change, run tests after each. Unfixable failure → STOP.

**5 — Implement:** Invoke the `bob:bdd` skill. Per step: write → lint → test → verify criteria.
Invoke the `bob:design-signals` skill continuously throughout this phase — implementation is a sensor for whether the approved design still fits reality, not just a typing exercise. Pause according to the signal's escalation tier (continue autonomously / continue and record / pause for human decision / stop and return to Design), never according to the plan step's Complexity or Conceptual-risk rating. A step rated Hard that turns out to be pure mechanical effort does not pause; a step rated Easy that trips signal 5 (contract change) does.

**STOP when:** tests fail and unfixable · plan requires ugly/hacky code · fundamental mismatch with reality · a design signal escalates to "pause for human decision" or "stop and return to Design."
**Don't stop for:** minor improvements (implement + document in report) · easily fixed lint · discoverable info · signals that resolve to "continue autonomously" or "continue and record."

**6 — Final verify:** Full test suite + linter + build. Unfixable → STOP.

**6.5 — Kanban update:**
- Read `{story_path}/_kanban.md`. Mark resolved tasks and issues done: change `- [ ]` to `- [x]` and move the card to `## done`.
- For any new issues or work discovered during implementation: invoke the `bob:work-routing` skill and follow its protocol.

**7 — Prepare for Reflect:** Before writing the note, prepare concise input for `/bob:reflect` — not a full walkthrough. Identify the few code paths that carry the architectural meaning (not every file touched), any Design Signals raised and how they resolved, and anything surprising enough that the developer should specifically look at it. This replaces the AI-led ownership-transfer narrative that used to run here: recovering ownership is `/bob:reflect`'s job, done with the developer, not a monologue Implement delivers to them.

Before writing the note, scan the implementation for patterns worth capturing as guidelines — recurring structures, conventions established, non-obvious decisions likely to repeat. If found, name each and suggest `/bob:guidelines` with a specific topic.

**8 — Report:** Write to `{story_path}/sessions/{date}-implement-{slug}.md`. Update plan status to "Implemented".

## Output

Primary: modified project files.
Report: `{story_path}/sessions/{date}-implement-{slug}.md`

Use the path resolved by `bob:story-context`. The `story_path` was established earlier in this session.

```
# Implementation Note: {Feature}
**Date:** {YYYY-MM-DD} | **Plan:** `{path}` | **Review:** reviewed / skipped | **Status:** Completed / Partial / Blocked

## Summary
{2-3 sentences.}

## Steps
| Step | Description | Status | Notes |
|------|-------------|--------|-------|

## Deviations
| Deviation | Reason |
|-----------|--------|

## Design Signals Raised
| Signal | Resolution | Evidence |
|--------|------------|----------|
{One row per signal that reached "continue and record" or higher. "None raised" is a valid, and common, row when implementation stayed within the approved design.}

## Discoveries
{Insights for future consideration. Patterns worth capturing as guidelines.}

## Test Results
{Summary. New tests added.}

## Files Modified

## Blockers / Next Steps

## Input for /bob:reflect
{Critical code paths carrying the architectural meaning, signals and how they resolved, anything surprising worth a closer look together. Concise — not a walkthrough.}
```

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
