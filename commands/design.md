---
allowed-tools: Bash(*), Read, Write, Edit
description: Form and defend the simplest coherent conceptual design for a capability, grounded in repository evidence. Socratic, human-owned.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- This is an existing project. Silently familiarize yourself with the project structure, key architectural patterns, and UI conventions before starting.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol. It loads the architecture index (`docs/architecture/README.md`) and the scope-matched concept and pattern notes.
- Use the Skill tool to invoke the `bob:design` skill. It owns the role, principles, rules, design prompts, required challenges and the Design Record template.

## Process

### Phase 1 - Start with evidence
Load the Brainstorm Brief (if one exists) or the accepted requirement from the user. Invoke the `bob:architect` skill. Then inspect the repository before asking broad questions:

**Graph first.** If the Code Graph Context (emitted by `bob:code-graph` via the context protocol) reports a fresh graph, use `graphify query "<question>"` to survey what already exists: relevant concepts, naming, boundaries, similar capabilities, data/control flow. Cite the `source_location` it returns as the file:line reference. Fall back to grep/Explore for anything the graph does not answer. Without a Code Graph Context, examine the repository manually.

Use the loaded architecture notes as the map of existing concepts and patterns. Cite evidence for every architectural claim.

### Phase 2 - Socratic design conversation
Run it per `bob:design` `references/interaction-policy.md`:
- One question, or one tightly related batch, at a time. Start with the decision carrying the largest conceptual consequence.
- Raise the skill's design prompts where they apply: ideal interface for the developer as user, reading order of new modules, which pattern applies or whether a competing one is forced, refactor first?
- Summarize the emerging model periodically.
- Propose concrete alternatives only after the human has engaged with the core decision.
- Stop when further questions no longer change the model.

### Phase 3 - Required challenges
Work through the skill's required challenges explicitly before closing.

### Phase 4 - PM step
Route any out-of-scope findings or deferred ideas: invoke the `bob:work-routing` skill and follow its protocol.

### Phase 5 - Exit and record
If the outcome is "return to Brainstorm", "investigate first" or "do not build", say so and stop. Otherwise check the skill's readiness criteria, then write the Design Record. If I say "save", write the record regardless of phase.

## Output

Write to: `{story_path}/sessions/{date}-design-{slug}.md`, using `bob:design` `references/artifact-template.md`.

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.

Use the path resolved by `bob:story-context`.

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
