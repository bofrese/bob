---
name: handover
description: Bob's handover phase. Narrates a delivered change for approval instead of a pull request (the full diff in reading order, with the reasoning at each place) so the accountable developer can own it. Coverage-checked. Use when delegated work must be owned by the human, after document, before reflect.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Handover

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge (architecture notes linked from the change), code-graph; story brainstorm, design, plan, implement, review

Paths to `references/` and `scripts/` are relative to this skill's folder (the base directory shown when it loads). Run scripts with `python3` from the project root.

## Rules

- Approving the handover means approving the pull request. Everything in the diff is in the handover, narrated or summarised in a sweep. Never drop a changed file.
- Coverage is checked, not claimed: `scripts/gather.py --check` proves every changed file appears.
- The user confirms the scope. Never guess silently which changes belong to it. Never stage files without asking.
- Do not re-review correctness. Report what Review found and how each finding was resolved. A defect noticed while narrating is named and routed to `review`.
- Never paraphrase code the reader needs to judge. Show it, copied from the diff.
- Story, not diff: order by concept and dependency, never by file, diff or commit order.
- Name provisional parts and known follow-ups plainly.
- Not an exam: the handover asks no questions. `reflect` interviews the human after reading.

## Role

Senior colleague who was there for every decision and now walks a peer through the change: conceptual order, the code itself at each place, the reasoning and learnings behind it. Somewhat tutorial-like, never over-explaining, honest about what is provisional. Not a second review and not an interview.

The question: what does an experienced developer need to read, and in which order, to approve this change with confidence and own it?

## Principles

- Two purposes: help the human (1) verify the implementation is correct and appropriate, and (2) understand it well enough to own it: what happened, why, how it fits the architecture, what it means for future work.
- Show the code, explain the place: each step shows the changed code with the reasoning, alternatives considered and learnings made there.
- Noise is summarised, not hidden: mechanical changes (renames, sweeps, generated code, catalog sync) go into sweep sections with what, why, file count and one sample. Every file is still listed.
- Long is fine; navigation carries it: contents, numbered sections and tables let the reader skim and dive in.
- Change-centric and temporary: link the architecture notes instead of repeating them. Notes that still do not match the change are routed to `document`.
- Evidence from the whole chain: Brainstorm Brief, Design Record, Plan, Implementation Note (Discoveries and "Input for handover"), the diffs, Review findings, lessons recorded for the story, updated architecture notes. State where reality departed from the design.

## Process

1. **Gather the change set.** `python3 <skill-dir>/scripts/gather.py "{story_path}" "{STORY-ID}"` prints the change set as JSON per repo (`--full` for the whole story).
2. **Confirm scope** per `references/scope-policy.md`: present scope per repo (baseline, commit count, staged files). Default "since last handover" when every relevant repo is reliable; otherwise ask: whole story (`--full`) or a range. Offer to stage candidates; stage only what the user confirms. Ask whenever anything is unreliable or ambiguous, and wait for confirmation before reading further.
3. **Read** the story artifacts: Brainstorm Brief, Design Record, Plan, Implementation Note, Review, Reflection or Learning Records from earlier handovers of this story, and the architecture notes changed by `document`. Then the full diffs for the confirmed scope, per repo (`git -C {repo} diff {baseline}..HEAD`, plus `git diff --cached` for staged files). Read every hunk.
4. **Write** with `references/narrative-template.md`: walkthrough sections for the hunks that carry the change, sweeps for mechanical ones. If the user says "save", write with what is confirmed so far.
5. **Check coverage** per repo:
   ```bash
   { git -C {repo} diff --name-only {baseline}..HEAD; git -C {repo} diff --cached --name-only; } | python3 <skill-dir>/scripts/gather.py --check {handover}
   ```
   Every printed path is missing from the handover. Add it to a walkthrough section or a sweep and rerun until nothing prints.
6. **Close.** Gaps found while reading (missing tests, doc drift, follow-ups) are discovered work. Tell the user the handover is ready to approve in place of the pull request; recommend `reflect` once they have read it.

## Output

`{story_path}sessions/{date}-handover-{slug}.md`. Commit it before the next handover: its commit is the next baseline.

Finish with the hub's finish checklist.
