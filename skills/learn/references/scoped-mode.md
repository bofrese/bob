# Scoped mode - improve one skill or command

Extract learnings from a session to improve one skill or command for future use, in any project, language or stack. The classification policy and the staging log (`docs/process/learnings.md`) apply unchanged; scoped mode narrows the evidence to one target and adds the improvement report.

## Principles

- Generic over specific: "ask about the authentication method", yes; "check the JWT implementation", no.
- High-signal additions only: content that changes AI behaviour or gives critical context, no "nice to have" prose.
- Pattern over instance: what question or guidance prevents the problem recurring?
- Preserve simplicity: the target stays focused. A suggestion that diverges from its purpose may belong elsewhere.
- If the target worked well, say so briefly. Do not manufacture improvements, and challenge suggestions that bloat it without clear benefit.
- Project-specific knowledge belongs in `docs/guidelines/`, not in the target.

## Process

1. **Identify the target.** Which skill or command did we use? Ask if unclear.
2. **Read it** where it lives: a bob skill (`skills/{name}/SKILL.md` in the bob plugin), or a project-local skill or command (`.claude/skills/`, `.claude/commands/`).
3. **Extract learnings** from this conversation, about the target only. Log first occurrences to `docs/process/learnings.md`; only a second credible occurrence, or a high-severity single one, becomes a proposal. Categories, one at a time, asking the user to confirm or add:
   - Missing questions it should have asked upfront.
   - Assumptions it made that should have been verified.
   - Output gaps in the artifact.
   - Process steps skipped or needing more structure.
   - Edge cases its guidance does not cover.
4. **Propose** per finding: exact text to add, modify or remove and where; new steps or template sections if needed.
5. **Validate** against the `prompt-engineering` skill (token efficiency, clarity, actionability), bob's design principles (coaching style, simplicity first) and generic applicability. Flag proposals that fail.
6. **Ask** whether to edit the target now or only write the report. Edit it where it lives; a generic bob skill needs explicit approval.

## Output

Write the report into the current project, never into the plugin directory: `{story_path}sessions/{date}-improve-{name}.md`, or `docs/process/sessions/{date}-improve-{name}.md` without a story.

```markdown
# Improvement: {name}
**Date:** {YYYY-MM-DD}
**Session Context:** {what we did}

## Current Assessment
{2-3 sentences: what worked, what gaps were found.}

## Proposed Improvements

### 1. {Missing Questions / Output Gaps / Process / Edge Cases}
**Issue:** {problem addressed}
**Proposed Change:** {exact text to add or modify, with its section}
**Rationale:** {brief}

## Changes Summary
- [ ] {Section} - {change type} - {one line}

## Validation
- [ ] Generic (any project, language, stack)
- [ ] High-signal (changes AI behaviour)
- [ ] Follows prompt engineering principles
- [ ] Preserves the target's focus and simplicity

## Notes
```
