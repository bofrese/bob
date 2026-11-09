# Run file template

`docs/process/sessions/{date}-autopilot-{slug}.md`. Update it after every phase. Keep rows short: the artifacts hold the detail.

```markdown
# Autopilot run: {slug}

**Date:** {date} · **Branch:** {branch} · **Base:** {SHA at start} · **Status:** running | stopped | completed
**Stories:** {ID}, {ID}
**Stop reason:** {phase, story, one line, link to the artifact} (only when stopped)

## {ID} {title}

| # | Phase | Status | Agent ID | Artifact / SHA | Answers |
|---|---|---|---|---|---|
| 1 | plan | todo | | | |
| 2 | review-plan | todo | | | |
| 3 | integrate | todo | | | |
| 4 | implement | todo | | | |
| 5 | review | todo | | | |
| 6 | fix | todo | | | |
| 7 | document | todo | | | |
| 8 | commit | todo | | | |
| 9 | handover | todo | | | |
| 10 | close | todo | | | |

Status values: todo, running, done, skipped, pause, design, fail.
```
