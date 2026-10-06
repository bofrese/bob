---
allowed-tools: Bash(*), Read, Write, Edit
description: Explain a delivered change as a logical story - problem, design ideas, what changed and why, reading order, future impact. Run after Document, before Reflect.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:handover` skill. It owns the role, principles, rules, scope policy and narrative template.

## Process

### 1 - Gather the change set
Locate `handover/scripts/gather.py` in the plugin's `skills/` folder (same parent directory as this file's `commands/` folder). Run:

```bash
python3 <plugin>/skills/handover/scripts/gather.py "{story_path}" "{STORY-ID}"
```

### 2 - Confirm scope
Apply `bob:handover` `references/scope-policy.md`:
- Present the scope per repo: baseline, commit count, staged files.
- Default "since last handover" when every relevant repo is reliable. Otherwise ask: whole story (re-run with `--full`) or a range.
- Offer to stage candidates. Stage only what I confirm.
- Ask whenever anything is unreliable or ambiguous. Wait for confirmation before reading further.

### 3 - Read
Read the story artifacts: Brainstorm Brief, Design Record, Plan, Implementation Note (Discoveries and "Input for /bob:handover"), Review, any Reflection or Learning Records from earlier handovers of this story, and the architecture notes changed by `/bob:document`. Then read the diffs for the confirmed scope, per repo (`git -C {repo} diff {baseline}..HEAD`, plus `git diff --cached` for staged files).

### 4 - Write
Write the handover using `references/narrative-template.md`. If I say "save", write with what is confirmed so far.

### 5 - Route and register
- Gaps found while reading (missing tests, doc drift, follow-ups): invoke the `bob:work-routing` skill.
- Recommend `/bob:reflect` once I have read the handover.

## Output

Write to: `{story_path}/sessions/{date}-handover-{slug}.md`

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.

Commit the handover file before the next handover: its commit is the next baseline.

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
