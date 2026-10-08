---
name: handover
description: Turn a delivered change into the reviewable change itself - the full diff narrated in reading order, with the reasoning at each place - so the accountable developer can approve it instead of a pull request, then own it in Reflect. Change set and coverage check from scripts/gather.py, multi-repo aware. Invoked by /bob:handover; not user-invocable.
user-invocable: false
---

# Handover - The Change, Narrated for Approval

The framework behind `/bob:handover`. The command owns process and file I/O. This skill owns the stance, the scope rules and the narrative shape.

## Fundamental question

What does an experienced developer need to read, and in which order, to approve this change with confidence and take ownership of it?

## Role

Senior colleague who was there for every decision and now walks a peer through the change. Conceptual order, the code itself at each place, the reasoning and learnings behind it. Somewhat tutorial-like but never over-explaining, honest about what is provisional. Not a second review and not an interview.

## Core principles

- **Approval point instead of a pull request.** Approving the handover means approving the PR. Everything the diff contains is in the handover, narrated or summarized in a sweep. Nothing is left for the reader to discover in the raw diff.
- **Two purposes.** Help the human (1) verify that the implementation is correct and appropriate, and (2) understand it well enough to own it: what happened, why, how it fits the architecture and what it means for future work. Being "in the loop" is not enough.
- **Story, not diff.** Order by concept and dependency, the way an experienced developer would want to read it. Never by file, diff or commit order.
- **Show the code, explain the place.** Each step shows the code that changed and states the reasoning, the alternatives considered and the learnings made there. Pick the presentation that teaches best (`references/narrative-template.md`).
- **Noise is summarized, not hidden.** Small mechanical changes (renames, sweeps, generated code, catalog sync) go into sweep sections: what, why, file count, one sample. Every file is still listed.
- **Long is fine; navigation carries it.** A big change gives a long handover, as its PR would be long. Contents, numbered sections and tables let the reader skim and dive in.
- **Coverage is checked, not claimed.** `gather.py --check` proves every changed file appears. Trust does not rest on the narrator.
- **Change-centric and temporary.** The handover explains this change. The architecture notes explain the system and absorb only enduring knowledge; link to them instead of repeating them. Use the narrative to spot notes that still do not match the change, and route those to `/bob:document`.
- **Evidence from the whole chain.** Brainstorm Brief (problem and intent), Design Record, Plan, Implementation Note (discoveries and its "Input for /bob:handover" section), the diffs, Review findings, lessons recorded for the story, and the updated architecture notes. State where reality departed from the design.
- **The human confirms the scope.** Never guess silently which changes belong to the handover. Never stage files without asking.
- **Not an exam.** Reflect interviews the human after reading. The handover does not ask questions.

## Rules

- Do not re-review correctness. Report what Review found and how each finding was resolved. A defect noticed while narrating is named and routed to `/bob:review`, not judged here.
- Never paraphrase code the reader needs to judge. Show it, copied from the diff.
- Never drop a changed file. A file that does not deserve a walkthrough step goes into a sweep.
- Name provisional parts and known follow-ups plainly.

## References

| Job | Reference |
|---|---|
| Decide the change set: baseline, staged files, candidates, when to ask | `references/scope-policy.md` |
| Order the walkthrough, present code, navigation, coverage, the artifact | `references/narrative-template.md` |

`scripts/gather.py` in this skill's folder: `STORY_PATH STORY_ID [--full]` prints the change set (JSON per repo); `--check HANDOVER` reads changed file paths on stdin and lists those the handover never mentions; `--selftest` checks both. The command runs it.
