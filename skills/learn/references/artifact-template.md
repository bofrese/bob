# Learning Record — Artifact Template

**Filename:** `{date}-learn-{slug}.md`, written to `{story_path}/sessions/` (or `docs/process/sessions/` when Learn runs without story context).

The Learning Record captures what this session's evidence justifies persisting — not a session recap. "No persistent lesson" is a valid, common, one-paragraph record.

```
# Learn: {Scope}
**Date:** {YYYY-MM-DD} | **Scope:** {full session / scoped command name}

## Evidence Reviewed
{Corrections, interruptions, repeated findings, missing tools/context inspected this run.}

## Staging Log Updates
{New entries added to docs/process/learnings.md, with occurrence count. "None" is valid.}

## Candidates
{One block per candidate that cleared the persistence bar. "No candidates this run" is valid and common.}

### {Candidate name}
- **Evidence:** {what happened, where}
- **Root cause:** {hypothesis}
- **Proposed change:** {the durable change}
- **Destination:** {file/location per classification-policy.md}
- **Downside/conflict risk:** {cost of persisting this}
- **Recurrence/severity basis:** {why this clears the bar}
- **Behavior test:** {if applicable}
- **Recommendation:** apply | experiment | defer | reject

## Applied This Session
{Which candidates were confirmed and actually edited, with file paths. "None — all deferred pending approval" is valid.}

## Rejected / Deferred
{Candidates not acted on, with reason.}
```

Exclude from this record: a full session recap, correctness findings (Review's job), and ownership/mental-model exploration (Reflect's job).
