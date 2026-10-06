---
allowed-tools: Bash(*), Read, Write, Edit
description: Help the accountable developer recover implementation insight and close ownership gaps after reading the Handover. Short, non-quizzy, peer-to-peer.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:reflect` skill. It owns the role, principles, rules, reflection policy, ownership standard and artifact template.

## Process

### Gate
Confirm both before starting:
- Review has established sufficient correctness.
- I have read the Handover for this change. If none exists, recommend `/bob:handover` first. If I choose to continue without one, note it in the record header.

### Phase 1 - Load evidence
Read the Handover, the Design Record and the Review verdict. Load the architecture notes the Handover links to, and nothing wider. Open the few code paths the Handover's reading order marks as carrying the design.

### Phase 2 - Select questions
Use `references/reflection-policy.md`. Pick two to five questions from the evidence. Ask none when the evidence gives none.

### Phase 3 - Explore together
Use `references/ownership-signals.md`. Only where a question exposed a gap, work through:
- expectation versus implementation reality;
- concepts clarified, split, merged or newly discovered;
- assumptions validated or weakened;
- complexity removed, introduced or moved, and simplifications missed;
- design smells or drift the change introduced or exposed;
- the actual reading and navigation path;
- future pressure points and fragile assumptions;
- understanding that stayed inside the AI session.

If an answer is vague, inspect that area together instead of supplying the answer.

### Phase 4 - Route
- Backlog work: invoke the `bob:work-routing` skill.
- Name candidates for `/bob:learn`, stale or missing architecture notes for `/bob:document`, and design revisits for `/bob:design`. Do not write those here.

### Phase 5 - Record
Write the Reflection Record using `references/artifact-template.md`. If I say "save", write what is established so far.

## Output

Write to: `{story_path}/sessions/{date}-reflect-{slug}.md`

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.

Use the path resolved by `bob:story-context`.

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
