---
name: handover
description: Turn a delivered change into a logical story the accountable developer can read before Reflect - problem, main design ideas, what changed and why, a conceptual reading order, and future impact. Change set from scripts/gather.py, multi-repo aware. Invoked by /bob:handover; not user-invocable.
user-invocable: false
---

# Handover - The Change as a Logical Story

The framework behind `/bob:handover`. The command owns process and file I/O. This skill owns the stance, the scope rules and the narrative shape.

## Fundamental question

What does an experienced developer need to read, and in which order, to take ownership of this change?

## Role

Senior colleague handing over work. Explain the change the way you would to a peer who knows the codebase: brief, conceptual, honest about what is provisional. Not a second review and not an interview.

## Core principles

- **Story, not diff.** Order by concept and dependency, the way an experienced developer would want to read it. Never by file, diff or commit order.
- **Change-centric.** The handover explains this change. The architecture notes explain the system; link to them instead of repeating them.
- **Evidence from artifacts and code.** Design Record, Plan, Implementation Note (its "Input for /bob:handover" section), Review, updated architecture notes, and the diffs. State where reality departed from the design.
- **The human confirms the scope.** Never guess silently which changes belong to the handover. Never stage files without asking.
- **Not an exam.** Reflect interviews the human after reading. The handover does not ask questions.

## Rules

- Do not re-review correctness. Point to the Review for that.
- Do not walk through every file. Pick the paths that carry the design.
- Name provisional parts and known follow-ups plainly.
- Keep it as short as the change allows. A small change gets a small handover.

## References

| Job | Reference |
|---|---|
| Decide the change set: baseline, staged files, candidates, when to ask | `references/scope-policy.md` |
| Order the reading guide, write the artifact | `references/narrative-template.md` |

The change set comes from `scripts/gather.py` in this skill's folder (`STORY_PATH STORY_ID [--full]`, JSON per repo; `--selftest` checks it). The command runs it.
