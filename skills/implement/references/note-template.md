# Implementation Note template

File: `{story_path}sessions/{date}-implement-{slug}.md`.

```markdown
# Implementation Note: {Feature}
**Date:** {YYYY-MM-DD} | **Plan:** `{path}` | **Review:** reviewed / skipped | **Status:** Completed / Partial / Blocked

## TL;DR
{3-6 bullets: what this is, what was decided, what is open.}

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
{One row per signal at "continue and record" or higher. "None raised" is a valid and common row.}

## Discoveries
{Insights for later. New, changed or competing codebase patterns for the `document` skill.}

## Intent Coverage
{Per plan row: ✅ / gap, with file evidence.}

## Test Results
{Summary. New tests added.}

## Files Modified

## Blockers / Next Steps

## Input for /bob:handover
{Critical code paths carrying the architectural meaning, signals and how they resolved, anything surprising worth a closer look together. Concise, not a walkthrough.}
```
