# Investigation report template

File: `{story_path}sessions/{date}-investigate-{slug}.md`.

````markdown
# Investigation: {Issue Title}
**Date:** {YYYY-MM-DD}
**Status:** {Root cause identified / Needs more data / Hypothesis tested}

## TL;DR
{3-6 bullets: what this is, what was decided, what is open.}

## Problem Statement
{Observed vs. expected behaviour, conditions, symptoms.}

## Root Cause
{1-3 sentences: the fundamental issue, not the symptom.}
**Classification:** {verified fact / supported hypothesis / unresolved possibility / design implication}

## DESIGN FEEDBACK
{Omit unless the root cause exposes a missing concept, confused responsibility, semantic contract problem or boundary failure. When present: repository evidence and a recommendation to run `design` before a structural fix.}

## Investigation Path

### Hypotheses Considered
1. {Hypothesis} - {tested / ruled out / confirmed}

### Code Analysis
**Relevant Files:**
- [{file.ext:lines}]({file.ext}) - {role in issue}

**How It Works (Current State):** {flow with code references}
**Where It Breaks:** {point of failure with code reference}
**Why It Breaks:** {causal chain from root cause to symptom}

### System Context
**Call Chain:**
```
caller() -> problemFunction() -> dependency()
```
**State Dependencies:** {external state or services}
**Similar Patterns:** {other code that works similarly, correctly or not}

## Impact Scope
- {Affected area, side effects, other code at risk}

## Solution Options
### Option 1: {Approach Name}
**Changes:** ... **Pros:** ... **Cons:** ... **Effort:** ...

## Recommendation
{Preferred approach and why.}

## Code References
{Key files and line ranges for further exploration.}

## Notes
{Missing tests, architectural considerations, patterns to watch.}
````
