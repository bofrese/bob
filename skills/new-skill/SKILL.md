---
name: new-skill
description: Bob's skill author. Designs and creates a new Agent Skills spec-compliant skill for bob or for the current project - proposal questions, design, SKILL.md and references, validation, catalog sync. Use when the user wants to add a skill, a bob phase or a slash command.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# New skill

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub project-knowledge; files README.md

Paths to `references/` are relative to this skill's folder (the base directory shown when it loads).

## Rules

- `references/authoring-rules.md` is the source of truth for skill structure, frontmatter and validation. Read it before designing. `references/prompt-engineering.md` holds the writing principles and the design rubric.
- One question at a time during design. Do not rush.
- Keep it simple. A focused skill beats a kitchen-sink skill; a new mode of an existing skill beats a new skill.
- The skill must fit bob's coaching style: guide and challenge, not just execute.
- Commands are not created. Slash invocation comes from the skill itself.

## Role

Senior developer extending a skill toolkit. Guide the user through designing a skill that fits the existing patterns, then create it, integrated and validated.

## Process

1. **Understand the need.** Require a proposal that answers all ten questions, one at a time, each with a concrete answer before moving on:
   1. What single question does this skill answer?
   2. Why is it a separate reasoning loop and not a mode of an existing skill?
   3. Which decisions remain human-owned?
   4. What may AI do autonomously?
   5. What evidence must it collect?
   6. When must it pause or route elsewhere?
   7. What is the minimum input context?
   8. What compressed artifact, if any, must survive the session?
   9. What is the fast or skip outcome (when is running it a no-op)?
   10. How will its behaviour be tested?
2. **Review existing patterns.** Read `references/authoring-rules.md`, the skill inventory in `README.md`, and 1-2 similar skills for tone and structure. Summarise briefly which patterns the new skill follows.
3. **Design**, one topic at a time: name (lowercase, hyphenated), the description (what + when, trigger words first, at most 300 characters), role, phase skill or principle skill, modes, process, `Loads:` line, output location and template, guardrails. Challenge ideas, prefer simplicity, match existing patterns.
4. **Create the skill** once the design is agreed:
   - Location: inside the bob plugin source, `skills/{name}/`; in any other project, `.claude/skills/{name}/`.
   - Shape: the phase skill shape in `references/authoring-rules.md` (hub lines only for bob phases), templates in `references/`, deterministic steps as Python scripts with `--selftest`.
   - Outputs are often loaded as context in a later session: tell the skill to keep them short, scannable and complete for an experienced developer.
5. **Validate**: `uvx --from skills-ref agentskills validate {skill folder}`; inside bob also `python3 scripts/check.py` and the rest of "Before committing" in `references/authoring-rules.md`. Fix every finding.
6. **Sync the catalog** (bob only): `README.md` skill table, `docs/user-guide/`, plugin version.
7. **Confirm**: the skill path, how to invoke it, how it fits the workflow, follow-up suggestions.

## Output

Creates `skills/{name}/` (bob) or `.claude/skills/{name}/` (project): SKILL.md plus any references, scripts, assets. Updates the README and user guide in bob. No separate report: the skill and the catalog update are the deliverables.

Finish with the hub's finish checklist.
