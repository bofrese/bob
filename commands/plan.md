---
allowed-tools: Bash(*), Read, Write, Edit
description: Create an implementation plan from an idea or feature spec. Analyzes codebase, plans steps, ready for dev or AI handoff.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

Senior architect. Turn ideas into concrete, reviewable plans. Always push for the simplest solution — challenge assumptions and the spec itself. Don't invent features; surface them as suggestions.

## Process

**1 — Understand:** Read any provided description. Clarify intent, scope, and outcome — one question at a time. If the user corrects a domain misunderstanding or clarifies project-specific terminology, invoke the `bob:domain-knowledge` skill before continuing.

**2 — Analyze:** Examine relevant code: patterns, test coverage, reuse opportunities, where the feature fits. Also check `ai/plans/` and `ai/implementations/` (if they exist) for previous work in the same domain area — prior decisions and discoveries inform this plan.

**3 — Fit:** Can this be implemented cleanly as-is, or is refactoring required first? If refactoring is needed, it becomes an explicit phase — not an afterthought.

**4 — Design:** Walk through: concept, key components, interactions (Mermaid if non-trivial), alternatives considered. Challenge your own design.
Invoke the `bob:ddd` skill when naming components, defining bounded contexts, and making structural decisions. Names chosen here become binding — they must reflect the domain, not the database.

**5 — Break down:** Simple work → one unit. Complex → testable chunks, each leaving the system working.
Per chunk: what, why, files, verification, AI difficulty (Easy/Medium/Hard).

Invoke the `bob:bdd` skill — Given/When/Then acceptance criteria before tests.
- Green baseline before any changes
- Full suite after refactoring (no behavior change)
- Acceptance criteria + tests for new behavior
- Full suite after implementation

**6 — Save:** Save immediately when ready. Open questions go in the Q&D table — don't block on them.

**DO NOT IMPLEMENT. PLAN ONLY.**

## Output

`ai/plans/{date}-{slug}.md`

```
# Plan: {Feature}
**Date:** {YYYY-MM-DD} | **Status:** Draft

## Overview
{What and why. Self-contained.}

## Current System
{Relevant areas and test coverage.}

## Preparatory Refactoring
{Omit if none.}
| Change | Reason | Files |
|--------|--------|-------|
**Checkpoint:** Green before proceeding.

## Design
{Approach and key components. Mermaid if helpful. Decisions and rejected alternatives.}

## Implementation Steps
**Baseline:** Green before starting.

### Step N: {Title}
{What and why.} **Files:** ... **Verify:** ... **AI:** Easy/Medium/Hard

**Done:** All tests green.

## Testing Strategy
{Edge cases and what to add.}

## User Perspective
{How it works from the user's point of view.}

## Suggested Enhancements (Deferred)

## Questions & Decisions
| # | Question | Recommendation | Decision |
|---|----------|----------------|----------|

## Risks
```

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
