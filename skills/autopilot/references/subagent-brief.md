# Subagent brief

The prompt for every phase subagent. Fill the braces; keep the rest as written.

```text
You run one bob phase inside an autopilot run. The developer is not available.

Story: {ID} at {story_path}
Phase: {phase} - invoke the `{skill}` skill (bob:{skill}) and follow it fully, including the hub's start and finish checklists.
Task: {subagent task from the phase table}
Inputs: {artifact paths from earlier phases, review findings, partial diff for a resumed implement}
Branch: {branch}. Do not commit; the orchestrator commits.

Questions the skill asks the user:
- Answer it yourself only when the Design Record, the intent sources or the plan settle it. Cite the source.
- Record every answer you gave in your own artifact under "Autopilot answers": question, answer, source.
- Scope confirmations: use the scope given in Task.
- Kanban filing questions: file the items, as the user would say "yes".
- Anything else, including any choice between options the sources do not settle: stop and return pause.

Design signals (implement): "continue autonomously" and "continue and record" continue.
"Pause for human decision" returns pause. "Stop and return to Design" returns design.

Return exactly this, nothing else:
STATUS: done | pause | design | fail
ARTIFACT: {path of the session artifact you wrote, or none}
ANSWERS: {count} (listed in the artifact)
SUMMARY: at most 10 lines. For pause/design/fail: the evidence, the location, and the decision the developer must make.
```
