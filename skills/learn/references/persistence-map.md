# Persistence Map — `docs/process/learnings.md`

Learn runs once per session and has no memory of prior runs on its own. `docs/process/learnings.md` is the durable staging log that closes that gap — it tracks "seen once, not yet a pattern" occurrences across sessions so a second credible occurrence can be recognized instead of re-litigated from scratch.

## What goes in the staging log

Every candidate that surfaces during Phase 1-2 of `/bob:learn`, whether or not it clears the persistence bar this run:

- **First occurrence, low/medium severity:** log the entry, do not persist elsewhere. This is the common case.
- **First occurrence, high severity:** log the entry AND proceed to classification immediately (persistence policy allows single-occurrence action for high-severity items).
- **Second or later occurrence matching an existing entry:** promote to a harness candidate for classification (Phase 3). On promotion, mark the entry `status: promoted` rather than deleting it — the history stays visible.

## Bootstrap

If `docs/process/learnings.md` does not exist, create `docs/process/` if needed and write:

```markdown
---
title: Harness Learnings
---
# Harness Learnings

Staging log for `/bob:learn`. Entries here are observed once, not yet confirmed as patterns.
A second credible occurrence of the same entry is what turns it into a harness candidate —
see `bob/skills/learn/references/classification-policy.md` for the persistence policy this
log exists to support.

## Entries

<!-- one entry per occurrence, oldest first -->
```

## Entry format

Append under `## Entries`:

```markdown
### {date} — {short description}
- **Occurrences:** {N} ({dates})
- **Evidence:** {what happened, where}
- **Status:** open | promoted | rejected
- **Notes:** {optional — root-cause hunch, related entries}
```

Matching on re-read is semantic, not exact-string: compare the "short description" and evidence against new candidates for the same underlying cause before creating a duplicate entry — increment `Occurrences` on the existing entry instead.

## Maintenance

- Entries marked `promoted` stay in the log as history; do not delete them.
- Entries marked `rejected` (a human explicitly declined to persist a repeated pattern) stay too — this prevents Learn from re-proposing something already declined without new evidence.
- This file grows slowly by design — it holds candidates, not a general changelog. If it grows past a few dozen open entries, that itself is a signal worth flagging (likely too many single-occurrence items being logged that should just be dropped).
