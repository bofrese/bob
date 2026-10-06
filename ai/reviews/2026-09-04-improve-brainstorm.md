# Command Improvement: /bob:brainstorm
**Date:** 2026-09-04
**Session Context:** Ran `/bob:brainstorm` on BRC-001 through all four phases, produced
`docs/product/user-guide.md` as a verification artifact and a 190-line brainstorm report at
`projects/brace/stories/BRC-001/sessions/`. The story's History table stayed empty.

## Current Command Assessment

The command itself ran well. Phase structure held, the "save" escape hatch was honoured, routing
to `/bob:design` versus `/bob:plan` was offered. The gap is not in the brainstorm process, it is
in the handoff to `bob:done-criteria`: the artifact was written and the story's audit trail was
not updated. Nothing in the session surfaced the omission, which is the part that matters.

## Root cause

The mechanism exists and is correctly placed. `bob:done-criteria` Responsibility 4 says:

> **Update story history:** After producing any output artifact, add one row to
> `{story_path}/_index.md` history table

That is an **event trigger**: artifact written, row added. But it sits inside a skill whose own
trigger is a **deferral gate**:

> **Invoke `bob:done-criteria` before responding to any new request.**

An event trigger nested inside a deferral gate never fires on its event. Writing the artifact does
not invoke done-criteria. Only a subsequent user request does, and by then the model has moved on.

In this session the next user message was in fact a new request, `/bob:improve-command`, so the
gate should have fired. It did not, because the new command's own Context block sent the model
straight into `bob:context-protocol`. The gate has no artifact, no checklist, and nothing that
notices its own absence. It depends entirely on the model remembering an instruction across a turn
boundary while a competing instruction is arriving.

That is a fragile rule, and its failure mode is silent.

## Proposed Improvements

### 1. Process — make the history row fire at artifact write, not at next request

**Issue:** The only reliable moment to record an artifact is immediately after writing it, while
the path, type, summary and outcome are all in hand.

**Proposed Change** to `commands/brainstorm.md`, in the `## Report` section, directly after the
`Write to:` line:

```markdown
Write to: `{story_path}/sessions/{date}-brainstorm-{slug}.md`

After writing the file, immediately add its row to `{story_path}/_index.md` History and update
`{story_path}/_kanban.md`. Do not defer this to the end-of-session gate. Use the Story History
and Kanban steps of `bob:done-criteria` Responsibility 4 as the format authority — this is a
trigger point, not a second copy of the rule.
```

**Rationale:** Moves the trigger to the event, keeps the format defined in exactly one place. The
same three lines belong at the artifact-write point of every command that produces one:
`design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `investigate`, `ui-review`.

---

### 2. Process — strengthen the deferral gate in `bob:done-criteria`

**Issue:** "Before responding to any new request" is the weakest possible trigger. It fires on an
event the model is not looking for, competes with the incoming request's own instructions, and
leaves no trace when skipped.

**Proposed Change** to `skills/done-criteria/SKILL.md`, in the `## Done — Non-Deferrable` framing
and in Responsibility 4:

```markdown
A new slash command arriving is a new request. Run this skill before that command's own
Context block, not after it.

If Responsibility 4's story-history step runs and finds the previous artifact's row already
present, that is the expected case, not a duplicate. Say nothing and move on. A missing row for
an artifact produced this session is a defect: add it and tell the user it was late.
```

**Rationale:** Makes the gate idempotent, so the artifact-write trigger and the end-of-session
gate can both run without conflict. Also names the specific case that was missed here, a slash
command arriving with its own Context block.

---

### 3. Output — the Directions Considered table shape

**Issue:** The template specifies `| Option | Summary | Pros | Cons |`. In this session the useful
shape was `| # | Direction | Verdict |`, where the verdict records who decided and why. Pros and
Cons columns invite a balanced survey of options that were in fact decided, which is padding.

**Proposed Change** to the `## Report` template in `commands/brainstorm.md`:

```markdown
## Directions Considered
| Direction | Summary | Verdict |
|-----------|---------|---------|
| ... | ... | Accepted / Rejected, and why. Name who decided when the user overruled a recommendation. |
```

**Rationale:** A brainstorm report is read later to answer "why not X?". A verdict answers that.
Pros and Cons do not, and they grow without bound. Recording who overruled whom is what makes a
rejected direction safe to revisit.

**Severity note:** First occurrence, single session. Logged, not urgent.

---

## Changes Summary
- [x] All 10 story-artifact commands — add — write-time registration line at each `Write to:`
  (`brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `learn`,
  `investigate`, `ui-review`). The other 21 commands with the done gate write outside a story,
  where Responsibility 4 already skips.
- [x] `skills/done-criteria/SKILL.md` § Responsibility 4 — add — two entry points, idempotent,
  missing row for a this-session artifact is a defect; same rule stated for the daily note
- [ ] `commands/brainstorm.md` § Report template — modify — Directions Considered gets a Verdict
  column (not applied; ordinary severity, first occurrence)

## Rejected alternative

Putting the trigger once in `bob:context-protocol`, which every engineering command already loads
at start. One edit instead of ten, and guaranteed in context. Rejected because it reproduces the
exact defect being fixed: an instruction loaded at session start and needed a hundred thousand
tokens later is what failed here. The trigger has to sit next to the action. Ten copies of a
pointer is not duplication; the format still lives in one place.

## Validation
- [x] Generic (applies to any project/language/stack)
- [x] High-signal (the first two change whether the audit trail exists at all)
- [x] Follows prompt engineering principles (trigger at the event; format defined once)
- [x] Preserves command focus and simplicity (three lines added to the command, logic stays in the skill)

## Notes

The centralisation in `bob:done-criteria` is right and should not be undone. The problem is purely
that a centralised rule still needs a trigger at each call site. Three lines pointing at the skill
is not duplication; it is the pointer that makes the skill reachable.

Worth checking whether other Responsibility 4 steps have the same latent problem. The daily-note
append has an identical trigger and the same silent failure mode, and nobody would notice a missing
daily entry either.

The severity split is deliberate. The first two proposals are a single occurrence but
high-severity: silent, systematic, and they break the exact thing the tracking system exists for.
The table-shape proposal is a first occurrence at ordinary severity and is logged in
`docs/process/learnings.md` rather than pushed.
