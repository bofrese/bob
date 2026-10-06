# Narrative Template - Handover Artifact

**Filename:** `{date}-handover-{slug}.md`, written to `{story_path}/sessions/`.

## Reading-order policy

Order the reading guide so each step only needs what came before it:
1. Start at the concept or interface that explains the change (often the new public surface, or the rule that changed).
2. Then what depends on it, in dependency order.
3. Then wiring and integration.
4. Tests last, unless a test is the clearest statement of the behavior; then put it next to the code it specifies.

Each step names the file or symbol in backticks, says what to look for, and why it matters. Skip files that are mechanical (renames, generated code, catalog updates); list them in one line at the end.

## Template

```markdown
# Handover: {Change}
**Date:** {YYYY-MM-DD} | **Story:** {STORY-ID} | **Scope:** {since last handover {date} / whole story / range} | **Repos:** {repo: N commits, ...}
**Design:** [{name}]({path}) | **Implementation:** [{name}]({path}) | **Review:** [{name}]({path})

## TL;DR
{3-6 bullets: the problem, the main design idea, what changed, what to watch.}

## Problem
{What was being solved, in 2-4 sentences.}

## Main design ideas
{The few ideas that shape the change. Where the built system departs from the Design Record, say so and why.}

## What changed and why
| Change | Why |
|---|---|

## Reading order
1. `{path or symbol}` - {what to look for, why it matters}
2. ...

Mechanical changes, no need to read: {one line}

## Future impact
- New abstractions or interfaces:
- Changed assumptions:
- New or changed patterns (with status):
- Provisional parts:
- Follow-ups:

## Architecture notes updated
- [{note}]({path}) - {what changed}
```
