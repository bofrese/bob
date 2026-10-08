---
name: bob
description: Hub of bob, the product development workflow. Start and finish checklists for every bob phase (story tracking, project knowledge, done criteria, next step). Use when a bob skill says so, when the user asks about bob, or for engineering or product work in a repo using bob, even if bob is not named.
license: Apache-2.0
---

# bob

Paths to `references/`, `scripts/` and `assets/` are relative to this skill's folder: the base directory shown when it loads (in Claude Code `${CLAUDE_PLUGIN_ROOT}/skills/bob`). Run scripts with `python3` from the project root. Do each step once per conversation; skip what is already done.

## Start checklist

1. Date: `python3 scripts/today.py`. Use it in file names and timestamps.
2. Load what your phase skill's `Loads:` line lists, by the rules in `references/context.md`. No phase skill (the user just describes work): use the defaults there. Hub loads:
   - `story`: resolve the story with `references/story.md`. No confirmation when the story is certain.
   - `intent`: original intent and its changes, `references/intent.md`.
   - `project-knowledge`: domain, architecture, guidelines, product, vault via `references/project-knowledge.md`. Use domain terms as defined there.
   - `code-graph`: if `references/code-graph.md` finds a usable graph, ask the graph before grep for code relationships.
3. Writing: every artifact follows `references/writing.md`.
4. No phase chosen yet: name the one fitting phase in one line (see Phases), then continue. "Where am I, what next" and status requests: `references/mentor.md`.

## Finish checklist

Run before you answer the next user request. It applies after compaction too.

1. Register at write time: the moment you write a session artifact, add its History row to `{story_path}/_index.md` and update the story kanban. Format: `references/tracking.md`.
2. Done criteria: check the items for this phase in `docs/process/done-criteria.md`; create the file if missing. `references/done.md`.
3. Discovered work (issues, debt, deferred ideas): route it when it surfaces, and here only what is not routed yet. One question to the user per item set. `references/tracking.md`.
4. Domain terms corrected or clarified this session: `references/domain-capture.md`.
5. Knowledge candidates and repeated corrections: stage them per `references/done.md`.
6. Daily note, if `personal/daily/` exists: `references/done.md`.
7. Name the next phase and why, in one line.

Fast-path work without a story skips story History and kanban steps.

## Phases

Recommend a phase for the question it answers, never because it is next in a pipeline. Name the risk or uncertainty that justifies it.

| Phase | Use when |
|---|---|
| brainstorm | Value, outcome or problem framing is open |
| design | Concepts, boundaries, naming or whole-system fit are open |
| plan | Design is owned and the execution shape is needed |
| review-plan | Facts or risk justify an independent check of the plan |
| implement | Intent and execution path are explicit (only when the user asks) |
| review | Correctness must be established independently |
| document | Architecture notes must reflect the change |
| handover | Delegated work must be owned by the human |
| reflect | After reading the Handover, or when implementation surprised |
| learn | The session exposed a reusable harness lesson |
| investigate | A bug needs a root cause, not a fix |
| dev | Work is local, reversible, settled and easy to verify |
| ui-review | A UI needs an expert review |

Product, knowledge vault and meta skills describe themselves in the skill listing.

## Files bob uses

| Path | Holds |
|---|---|
| `docs/product/` | Product artifacts, updated in place |
| `docs/domain/`, `docs/architecture/`, `docs/guidelines/` | Domain terms, architecture notes, guidelines |
| `docs/process/done-criteria.md` | What done means per artifact type |
| `projects/{sub}/_kanban.md` | Project kanban: stories and INBOX |
| `projects/{sub}/stories/{ID}/` | Story: `_index.md`, `_kanban.md`, `input/`, `sessions/`, `tasks/` |
| `knowledge/` | Validated knowledge vault; `_INBOX/` is staging |
| `personal/` | Gitignored personal notes and daily log |
