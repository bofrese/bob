# Plan template

File: `{story_path}sessions/{date}-plan-{slug}.md`.

```markdown
# Plan: {Feature}
**Date:** {YYYY-MM-DD} | **Status:** Draft | **Design:** {path to Design Record, or "inline - fast path"}

## TL;DR
{3-6 bullets: what this is, what was decided, what is open.}

## Overview
{What and why. Self-contained. Fast path: include the one-paragraph inline design statement here.}

## Current System
{Relevant areas and test coverage.}

## Preparatory Refactoring
{Omit if none.}
| Change | Reason | Files |
|--------|--------|-------|
**Checkpoint:** Green before proceeding.

## Intent Changes
{Only if planning changed intent, per the hub's `references/intent.md`. Omit otherwise.}

## Intent Coverage
| Intent item (source section or change row) | Must be present | Step / target |
|---|---|---|

## Design Mapping
{How the Design Record's concepts and interfaces map to components and files. Mermaid if helpful. No new concepts.}

## Implementation Steps
**Baseline:** Green before starting.

### Step N: {Title}
{What and why.} **Files:** ... **Verify:** ... **Complexity:** Easy/Medium/Hard **Conceptual risk:** Low/Medium/High

**Done:** All tests green.

## Structural Diff Summary
| File/Module | Symbol | Change |
|-------------|--------|--------|

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

Add a `## DESIGN FEEDBACK` section when repository facts contradict the Design Record.
