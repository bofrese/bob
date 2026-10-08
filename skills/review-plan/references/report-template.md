# Plan review template

File: `{story_path}sessions/{date}-review-plan-{slug}.md`.

```markdown
# Plan Review: {Plan Title}
**Date:** {YYYY-MM-DD}
**Plan reviewed:** {path or name of the plan}
**Verdict:** {Approve / Approve with changes / Needs rework / Recommend rethink / Return to Design}

## TL;DR
{3-6 bullets: what this is, what was decided, what is open.}

## Summary
{2-3 paragraphs: what is good, what is concerning, the recommendation.}

## Codebase Verification
| Claim in Plan | Actual State | Issue |
|--------------|-------------|-------|

## Findings

### 🔴 Critical
{Must be addressed before implementation.}

#### {Finding Title}
**Type:** plan defect / design concern / requirement gap / optional simplification
**Issue:** ...
**Impact:** ...
**Recommendation:** ...

### 🟡 Important
{Same fields as Critical.}

### 🟢 Suggestions
#### {Finding Title}
**Type:** optional simplification
**Suggestion:** ...
**Benefit:** ...

## Complexity Assessment
{Is the plan more complex than it needs to be? What could be simplified?}

## Alternative Approach
{Skip if the current approach is sound.}
### Proposed Alternative
### Why It's Better
### Trade-offs

## Missing Considerations

## Recommendations
{Ordered: fix, rethink or proceed.}
```
