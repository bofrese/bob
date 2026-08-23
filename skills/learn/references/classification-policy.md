# Classification Policy — Lesson Types and Persistence

## Classify each candidate

| Lesson type | Default destination |
|---|---|
| One-off correction | Do not persist |
| Repository-wide operating fact | `CLAUDE.md`/repository instructions |
| Domain term or distinction | `docs/domain/` |
| Architectural decision | architecture docs, ADR, or knowledge decision |
| Reusable project pattern | `docs/guidelines/` or knowledge pattern |
| Skill interaction failure | command/skill change plus behavior test |
| Missing task context | artifact contract or context protocol |
| Deterministic invariant | test, linter, architecture rule, hook |
| Good reference pattern | example/reference implementation |
| Tool or permission gap | setup/tooling configuration |

For each candidate report:
1. evidence;
2. root-cause hypothesis;
3. proposed durable change;
4. destination;
5. downside or conflict risk;
6. recurrence/severity basis;
7. behavior test where applicable;
8. recommendation: apply, experiment, defer, or reject.

## Persistence policy

- Do not persist merely because an event occurred once.
- Treat the second credible occurrence as a harness candidate, not automatic persistence.
- High-severity single occurrences may justify immediate action (e.g. a correction that would silently corrupt data or break a contract if repeated).
- State the downside of every proposed persistent rule — prompt bloat, false-positive rate, rigidity, maintenance burden.
- Prefer executable enforcement (test, linter, architecture rule, hook) over prose when the invariant is deterministic.
- Prefer examples over general prose when behavior is hard to specify abstractly.
- Require human approval before changing generic BOB skills or repository-wide instructions. Project-local or story-scoped destinations (a guideline, a domain note, a knowledge decision) can be applied on confirmation without the "generic behavior change" bar.
- Surface conflicts with existing guidance rather than silently overwriting it.
- Recommend consolidation or retirement when instructions overlap — do not perform destructive cleanup without confirmation.
