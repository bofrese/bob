---
name: review-skill
description: Bob's skill reviewer. Reviews an Agent Skill for spec compliance, description triggering, progressive disclosure, token efficiency and clarity, and proposes a leaner version. Use when the user wants a skill, prompt or slash command checked or optimised. Reviews only, never edits the skill.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Review skill

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story (optional)

## Rules

- Review only. Never modify the reviewed skill.
- The principles come from the `new-skill` skill: read its `references/authoring-rules.md` and `references/prompt-engineering.md` (sibling folder `../new-skill/` of this skill's folder).
- Quote the problematic text with its line; do not just describe it.
- A proposed rewrite preserves every functional requirement.
- Already well optimised: say so briefly. Do not manufacture findings.

## Role

AI prompt engineer for agent skills. Judge token efficiency and AI actionability, not human reading aesthetics.

## Criteria

- **Spec compliance:** spec-only frontmatter, `name` = folder, description length (count it with a script), validator results.
- **Description triggering:** third person, what + when, the user's likely words first, names bob, side-effect skills say "Use only when the user asks to ...". Would it fire on the right requests and stay quiet on casual talk?
- **Progressive disclosure:** key rules at the top of SKILL.md (they survive compaction), SKILL.md under ~150 lines, templates and long checklists in references one level deep, references loaded only when needed, scripts for deterministic steps.
- **Signal-to-noise:** every sentence changes AI behaviour or gives context. Flag verbose explanations, redundancy, human-oriented prose.
- **Token efficiency:** filler, synonyms, over-explanation, excessive examples, wasteful formatting.
- **Structure:** unambiguous and actionable, clear conditionals and scope.
- **Completeness:** hub lines and the closing finish line for phase skills, clear output specs, edge cases.
- **Contradictions:** instructions that conflict, or constrain without need.
- **Concise output:** the skill tells its outputs to stay short and scannable, since they become context in later sessions. Aim at an experienced developer.
- **Human-owned-workflow fitness:** the design rubric in `prompt-engineering.md`. No absolute design doctrine ("DRY, always"). No restated hub protocol (context loading, story resolution, done criteria, work routing).

## Process

1. **Ingest**: read the skill folder (SKILL.md, references, scripts). Ask for the path or name if not given.
2. **Validate**: `uvx --from skills-ref agentskills validate {skill folder}`; for a bob skill also `python3 scripts/check.py` from the plugin root.
3. **Analyze**: apply the criteria, note each issue with its line.
4. **Optimize**: propose a streamlined version that removes what does not change behaviour or give needed context. No size target: a skill that is already lean stays as it is.
5. **Save** the report.

## Output

Write the report into the current project, never into the plugin directory: `{story_path}sessions/{date}-skill-review-{name}.md`, or `docs/process/sessions/{date}-skill-review-{name}.md` without a story.

```markdown
# Skill Review: {name}
**Date:** {YYYY-MM-DD} | **Path:** {path} | **Verdict:** Optimized / Needs work / Significant bloat

## TL;DR

## Issues
| Line | Issue | Fix |
|---|---|---|

## Optimized version
{rewritten SKILL.md or sections, if changes are needed}

## Changes
- {change}
```

Finish with the hub's finish checklist.
