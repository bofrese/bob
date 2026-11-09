---
name: autopilot
description: "Bob's autopilot. Runs stories whose design is settled end to end without the developer: plan, review-plan, implement, review, document, commit, handover, each phase in its own subagent. Use only when the user asks to autopilot, auto-run or resume an autopilot run."
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit, Agent, SendMessage
---

# Autopilot

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, tracking; files projects/*/_kanban.md

Paths to `references/` are relative to this skill's folder (the base directory shown when it loads).

## Rules

- Autopilot is the exception. It fits only stories whose big questions were settled in brainstorm and design, or that are small and simple. Say so when a candidate does not fit.
- The human gate is the start: nothing runs before the user confirms the stories. After that, run without asking.
- Every phase runs the existing bob skill in its own subagent, with the brief in `references/subagent-brief.md`. The orchestrator never does phase work itself; it only selects, checks, commits, moves cards and writes the run file. This keeps its context small.
- One story at a time. The next story starts only after the current one is committed and handed over.
- Stop rule: any subagent that returns `pause`, `design` or `fail` stops the whole run. Do not commit, do not roll back, do not start another story. Later stories would build on half-done work.
- Auto-answers only from sources: a subagent may answer a question that the Design Record, intent or plan already settles, and logs it. Everything else is a `pause`.
- The run file is updated after every phase, before the next starts. It is the resume source.
- Cards end in Verify, never Done. The developer still owns the handover and `reflect`.

## Role

Delivery lead running settled work while the developer is away: strict about readiness, strict about stopping, no judgment calls that belong to the human.

## Process

1. **Select.** Use the story IDs the user gave, else the cards in the project kanban's `Ready` column (design settled). Boards with extra columns are fine; if there is no `Ready` column, ask. For each story check:
   - a Design Record with status "Ready for Plan" (`{story_path}sessions/*-design-*.md`)
   - Intent Sources in `_index.md`
   - a Brainstorm Brief, or the Design Record says none was needed
   - no 🔴 item in the story `Issues`

   Show one table: story, title, each check ✅/❌, verdict. Ask the user to confirm the list. Stories with a ❌ are excluded unless the user overrides. Nothing ready: list what each story lacks and stop.
2. **Preflight.**
   - Branch: the current branch, unless the user names another.
   - `git status --porcelain`. Changes in files the stories' plans or designs name: stop and report. Unrelated changes (bob markdown, notes): list them, flag anything suspicious, and offer to commit them first. Proceed only on a clean or user-accepted tree.
   - Write the run file `docs/process/sessions/{date}-autopilot-{slug}.md` from `references/run-template.md`, with every phase row `todo`.
3. **Run each story.** Move its card to `In Progress`. Then run the phases in order. For each: spawn the subagent, record its agent ID in the run file, wait for its return, record status, artifact and auto-answers.

   | # | Phase | Subagent task |
   |---|---|---|
   | 1 | plan | `plan` from the Design Record |
   | 2 | review-plan | `review-plan` on that plan |
   | 3 | integrate | `plan`: apply the review findings to the plan. A finding that changes the design returns `design`. |
   | 4 | implement | `implement` the reviewed plan |
   | 5 | review | `review`, scope: the uncommitted changes of this story |
   | 6 | fix | `implement`, scoped to the review findings. Skip if none. Any 🔴 fixed: one more `review`; still 🔴: `fail`. |
   | 7 | document | `document` in Update mode for this change |
   | 8 | commit | Orchestrator: stage the story's code and artifacts, commit `{ID}: {title}`, record the SHA |
   | 9 | handover | `handover`, scope "since last handover" (the commit from step 8) |
   | 10 | close | Orchestrator: commit the handover and kanban (`{ID}: handover`), move the card to `Verify` |

4. **Stop.** On `pause`, `design` or `fail`: set the run status to `stopped` with the reason, the phase and the subagent's evidence. Leave the working tree and the card (`In Progress`) as they are. Report what is done, what is uncommitted and the decision the developer must make. End the run.
5. **Finish.** Run status `completed`. Report one table per story: commits, handover link, auto-answers, signals recorded. Recommend reading each handover, then `reflect`.

## Resume

When the user says "resume" (autopilot) or the session restarts mid-run:

1. Read the newest `docs/process/sessions/*-autopilot-*.md` with status `running` or `stopped`.
2. Check that `git rev-parse HEAD` matches the last recorded SHA, or the run's base SHA if none yet. A mismatch means someone changed the branch: show the difference and ask.
3. `stopped` runs: confirm the developer resolved the stop reason before continuing.
4. Continue at the first phase row that is not `done` or `skipped`. If it has an agent ID, try `SendMessage` to that ID first ("continue where you stopped"). If that fails, spawn a fresh subagent for the same phase; for `implement` and `fix`, give it the current `git diff` as partial work.
5. A phase counts as done only when its artifact is registered in the story `_index.md` History (steps 8 and 10: when the commit exists).

Waiting for a usage limit to reset is the harness's job, not this skill's: Desktop has "Auto-continue when limits reset"; for unattended CLI runs, see the user guide.

## Output

- The commits on the branch, the phase artifacts in each story's `sessions/`, cards moved to `Verify`.
- The run file `docs/process/sessions/{date}-autopilot-{slug}.md`. Register it in the History of each story in the run.

Finish with the hub's finish checklist.
