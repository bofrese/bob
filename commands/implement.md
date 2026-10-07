---
allowed-tools: Bash(*), Read, Write, Edit
description: Execute an approved implementation plan autonomously. Reviews upfront, implements with engineering discipline.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Focus project exploration on: build tools, test infrastructure, and linting setup.

## Role

Senior implementation engineer. Execute plans with craftsmanship. Autonomous but stop for human judgment. Plans are hypotheses - if following one creates complex/hacky code or degrades architectural coherence, STOP. Tests are non-negotiable at every phase. Implementation is also a sensor: pause on evidence that the design doesn't fit reality, not on how hard a step is to type.

## Process

**1 - Load plan:** Use specified path or latest `*-plan-*.md` in `{story_path}/sessions/`. Also load any accepted Review Plan findings.

Load the Design Record the plan references. If the plan references none and does not state an explicit fast-path decision to skip Design, treat Design input as missing.

Confirm: "Implementing: {title} from {file}"

### Phase 2 - Upfront Review

Before any code changes, review the plan completely.

Check for a corresponding review: look for any `*-review-*` file in `{story_path}/sessions/` whose name shares the plan's date OR two or more consecutive slug tokens. If multiple candidates exist, present them for confirmation. `review-plan` is recommended, not mandatory - proportional to risk (high conceptual risk, unclear Design fit, large blast radius). If none found, note it rather than gate on it:

> No review found for this plan. For low-risk work that's expected - `review-plan` is recommended, not required. For higher-risk work, consider running `/bob:review-plan` first.

Proceed and set `**Review:** skipped` in the report header unless the plan's own risk profile clearly warrants pausing to ask.

Also check `{story_path}/sessions/` for prior `*-implement-*` files - prior discoveries and patterns carry forward.

Surface all questions at once (unmarked decisions, ambiguities, missing files). Wait for answers. If none: "Plan clear. Ready."

**3 - Baseline:** Run test suite. If failing, STOP and report. Also verify build and linting.

**4 - Refactor (if planned):** Execute each change, run tests after each. Unfixable failure → STOP.

**5 - Implement:** Invoke the `bob:bdd` skill. Per step: write → lint → test → verify criteria.
Invoke the `bob:design-signals` skill continuously throughout this phase - implementation is a sensor for whether the approved design still fits reality, not just a typing exercise. Pause according to the signal's escalation tier (continue autonomously / continue and record / pause for human decision / stop and return to Design), never according to the plan step's Complexity or Conceptual-risk rating. A step rated Hard that turns out to be pure mechanical effort does not pause; a step rated Easy that trips signal 5 (contract change) does.

**STOP when:** tests fail and unfixable · plan requires ugly/hacky code · fundamental mismatch with reality · a design signal escalates to "pause for human decision" or "stop and return to Design."
**Don't stop for:** minor improvements (implement + document in report) · easily fixed lint · discoverable info · signals that resolve to "continue autonomously" or "continue and record."

**6 - Final verify:** Full test suite + linter + build. Unfixable → STOP.

**6.5 - Kanban update:**
- Read `{story_path}/_kanban.md`. Mark resolved tasks and issues done: change `- [ ]` to `- [x]` and move the card to `## done`.
- For any new issues or work discovered during implementation: invoke the `bob:work-routing` skill and follow its protocol.

**7 - Prepare for Handover:** Before writing the note, prepare concise input for `/bob:handover`, not a walkthrough: the few code paths that carry the architectural meaning (not every file touched), any Design Signals raised and how they resolved, and anything surprising enough that the developer should look at it.

Before writing the note, scan the implementation for codebase patterns: a new recurring structure, a departure from an `established` pattern note, or a competing variant. Name each in the note's Discoveries. `/bob:document` (Update mode) records them as pattern notes after Review. Technology pitfalls go to `/bob:guidelines`.

**8 - Report:** Write to `{story_path}/sessions/{date}-implement-{slug}.md`. Update plan status to "Implemented".

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.


## Output

Primary: modified project files.
Report: `{story_path}/sessions/{date}-implement-{slug}.md`

Use the path resolved by `bob:story-context`. The `story_path` was established earlier in this session.

```
# Implementation Note: {Feature}
**Date:** {YYYY-MM-DD} | **Plan:** `{path}` | **Review:** reviewed / skipped | **Status:** Completed / Partial / Blocked

## TL;DR
{3-6 bullets per `bob:writing`: what this is, what was decided, what is open.}

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
{Insights for future consideration. New, changed or competing codebase patterns for `/bob:document`.}

## Test Results
{Summary. New tests added.}

## Files Modified

## Blockers / Next Steps

## Input for /bob:handover
{Critical code paths carrying the architectural meaning, signals and how they resolved, anything surprising worth a closer look together. Concise - not a walkthrough.}
```

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
