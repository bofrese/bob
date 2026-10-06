---
allowed-tools: Bash(*), Read, Write, Edit
description: Write and maintain canonical architecture notes (concepts and patterns) in docs/architecture/. Discover, Update after Review, or Audit for drift.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:document` skill. It owns the role, principles, rules, layout, modes and note templates.

## Process

### 1 - Detect mode
- `docs/architecture/` missing → **Discover**.
- A story is active and its Review is done, or I name a story or change → **Update**.
- I ask to check, refresh, sync or audit docs → **Audit**.
- Unclear → ask, with your recommendation.

State the mode in one line, then load only that mode's reference from `bob:document` plus `references/note-templates.md`.

### 2 - Load design judgment
Invoke the `bob:architect` skill. Load the references the mode names (concepts, patterns).

### 3 - Run the mode
Follow the mode reference. Every list of notes to write, migrate, move or delete is confirmed by me before any file changes. Pattern status `established` is set only on my word.

### 4 - Write
Write the confirmed notes and `docs/architecture/README.md`. Add or fix doc comments in source files where a fact is file-local. Do not change application code.

### 5 - Route and register
- Code problems, drift outside scope, and deferred notes: invoke the `bob:work-routing` skill.
- Update mode: add one row to `{story_path}/_index.md` History (type Documentation, listing the notes changed), using `bob:done-criteria` Responsibility 4 as the format authority.

If I say "save", write what is confirmed so far regardless of phase.

## Output

Notes in `docs/architecture/concepts/` and `docs/architecture/patterns/`, index in `docs/architecture/README.md`.

After writing, report: notes created or changed, patterns with status changes, drift found, open design questions.

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
