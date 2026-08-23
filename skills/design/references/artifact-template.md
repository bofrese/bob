# Design Record — Artifact Template

**Filename:** `{date}-design-{slug}.md`, written to `{story_path}/sessions/`.

The Design Record is the authoritative intent handed to Plan, Review Plan, Implement, Review, and Reflect. Keep it decision-dense and self-contained — someone who wasn't in the conversation must be able to plan from it.

```
# Design: {Capability}
**Date:** {YYYY-MM-DD}
**Status:** {Ready for Plan / Return to Brainstorm / Investigate First / Do Not Build}

## Accepted Capability

## Repository Evidence Inspected
| Area | Finding | Source |
|------|---------|--------|

## Existing Concepts Reused

## New Concepts Introduced

## Concepts Deliberately Not Introduced

## Domain Vocabulary & Naming

## Stable vs. Volatile Dimensions

## Boundaries & Responsibility Ownership

## Important Data/Control Flow

## Expected Reading/Navigation Path

## Alternatives Rejected (and why)

## Complexity Removed / Introduced / Moved

## Risks & Pressure Points

## Human-Owned Decisions

## AI Assumptions

## Unresolved Questions

## Revisit-If Triggers

## Argument for Whole-System Simplicity
```

Exclude from this record: implementation plans, file-by-file steps, and repeated product rationale already captured in the Brainstorm Brief — those belong to `/bob:plan`.
