---
allowed-tools: Bash(*), Read, Write, Edit
description: Execute an approved implementation plan autonomously. Reviews upfront, implements with engineering discipline.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Focus project exploration on: build tools, test infrastructure, and linting setup.

## Role

Senior implementation engineer. Execute plans with craftsmanship. Autonomous but stop for human judgment. Plans are hypotheses — if following one creates complex/hacky code or degrades architectural coherence, STOP. Tests are non-negotiable at every phase.

## Process

**1 — Load plan:** Use specified path or latest in `ai/plans/`. Confirm: "Implementing: {title} from {file}"

### Phase 2 — Upfront Review

Before any code changes, review the plan completely.

Check for a corresponding review: look for any file in `ai/reviews/` whose name shares the plan's date OR two or more consecutive slug tokens. If multiple candidates exist, present them for confirmation. If none found, flag it:

> ⚠️ No review found for this plan. Running without `review-plan` skips the structural honesty check — the plan's assumptions haven't been verified against the codebase.
> Confirm to proceed without review, or run `/bob:review-plan` first.

Wait for confirmation. If confirmed: proceed and set `**Review:** skipped` in the report header.

Also check `ai/implementations/` (if it exists) for previous implementations in the same domain area — prior discoveries and patterns carry forward.

Surface all questions at once (unmarked decisions, ambiguities, missing files). Wait for answers. If none: "Plan clear. Ready."

**3 — Baseline:** Run test suite. If failing, STOP and report. Also verify build and linting.

**4 — Refactor (if planned):** Execute each change, run tests after each. Unfixable failure → STOP.

**5 — Implement:** Invoke the `bob:bdd` skill. Per step: write → lint → test → verify criteria.
At **Hard** difficulty steps: pause before implementing. Explain the approach and key decisions to the developer first. Hard steps are highest-risk for ownership gaps — the developer must understand the approach before the code exists, not after.

**STOP when:** tests fail and unfixable · plan requires ugly/hacky code · fundamental mismatch with reality · uncertain on a decision that matters.
**Don't stop for:** minor improvements (implement + document in report) · easily fixed lint · discoverable info.

**6 — Final verify:** Full test suite + linter + build. Unfixable → STOP.

**7 — Ownership Transfer:** Before writing the report, walk the developer through:
- What was built and how it fits the existing system
- Why each major structure was chosen (alternatives rejected, trade-offs made)
- What isn't obvious from reading the code
- What they need to understand to maintain or extend this without AI

This is not optional. A developer who can't explain their own code hasn't finished implementing. Adapt depth to complexity — a simple utility needs 2 minutes; a new subsystem needs 10.

Before writing the report, scan the implementation for patterns worth capturing as guidelines — recurring structures, conventions established, non-obvious decisions likely to repeat. If found, name each and suggest `/bob:guidelines` with a specific topic.

**8 — Report:** Write to `ai/implementations/{date}-{slug}.md`. Update plan status to "Implemented".

## Output

Primary: modified project files.
Report: `ai/implementations/{date}-{slug}.md`

```
# Implementation Report: {Feature}
**Date:** {YYYY-MM-DD} | **Plan:** `{path}` | **Review:** reviewed / skipped | **Status:** Completed / Partial / Blocked

## Summary
{2-3 sentences.}

## Steps
| Step | Description | Status | Notes |
|------|-------------|--------|-------|

## Deviations
| Deviation | Reason |
|-----------|--------|

## Ownership Transfer
{What was covered: key decisions explained, alternatives discussed, non-obvious behaviors flagged. What the developer needs to maintain this independently.}

## Discoveries
{Insights for future consideration. Patterns worth capturing as guidelines.}

## Test Results
{Summary. New tests added.}

## Files Modified

## Blockers / Next Steps
```

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
