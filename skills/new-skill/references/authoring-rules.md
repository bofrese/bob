# bob skill authoring rules

The single source of truth for how bob skills are written. Paths are relative to the bob plugin root.

## Layout

```text
skills/{name}/
  SKILL.md          the skill; name = folder name
  references/*.md   loaded on demand, one level deep
  scripts/*.py      deterministic steps, Python 3 stdlib only
  assets/           templates copied into projects
hooks/hooks.json    Claude Code adapter (SessionStart, md-move guard)
.claude-plugin/     Claude Code adapter
scripts/check.py    structural validator
```

The `bob` hub (`skills/bob/`) holds the start and finish checklists, story resolution, intent rules, the project-knowledge loader, done criteria, tracking and work routing, domain capture, code-graph policy, writing rules and the mentor ("where am I, what next").

## Rules for every skill

- Frontmatter: only `name` (= folder name), `description`, and optionally `license` (bob uses `Apache-2.0`), `compatibility`, `metadata`, `allowed-tools`.
- Description: third person, what + when, key trigger words first, names bob, at most 300 characters (count with a script; `scripts/check.py` does). Quote it if it contains `: `. No "Invoke this skill", no "Used by", no "not user-invocable". Side-effect skills (`implement`, `setup`, `docker-setup`) say "Use only when the user asks to ...".
- SKILL.md under ~150 lines (spec max 500). Put the most important rules at the top: after compaction only the start of an invoked SKILL.md is re-attached. References read from disk are not.
- References one level deep inside the skill's own folder, each under ~150 lines, with a contents list when longer than 100 lines. No reference is loaded unconditionally unless it is tiny.
- Exception: a skill may read a sibling skill's file (`../<skill>/scripts/...`, `../<skill>/references/...`), because bob installs as one plugin. Keep it to a shared script or reference with one owner. Current uses: `remember` and `setup` run `../library/scripts/bootstrap.py`; `setup` runs `../bob/scripts/primer.py --agents-md` and reads `../learn/references/persistence-map.md` and the hub's `assets/done-criteria.md`; `review-skill` and `learn` (scoped mode) read `../new-skill/references/`.
- Deterministic steps are Python scripts, stdlib only, referenced relative to the skill folder and run from the project root. Each script has an assert-based `--selftest`.
- Name other skills by their plain name (`plan`, the `library` skill). The hub line is the one place with the platform name (`bob:bob`).
- Design rationale lives in `docs/architecture/`, never in runtime files.
- No urgency wording ("exactly", "non-deferrable", ALL CAPS). State the behaviour once.
- No history: describe current behaviour only. Git holds the history.
- No back-compat: when an artifact shape changes, the old shape is no longer accepted.
- No em dashes anywhere. Plain international English. Artifacts follow the hub's `references/writing.md`.
- Reports and artifacts go into the user's project (story `sessions/`, else `docs/process/sessions/`), never into the plugin folder.

## Phase skill shape

```markdown
---
name: plan
description: Bob's plan phase. Turns a Design Record into an implementation plan ...
license: Apache-2.0
---

# Plan

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge, code-graph; files docs/product/vision.md

## Rules
## Role
## Process
## Output

Finish with the hub's finish checklist.
```

- `Loads:` follows the hub's `references/context.md`: `hub <name>` reads a hub reference, `files <path>` reads a project file if it exists, `story <type>` reads the newest `{date}-{type}-*.md` session artifact. There is no central load table.
- Invoke the hub with the Skill tool, not by reading its files, so its checklists survive compaction.
- Do not repeat what the hub states: write-time registration, work routing, graph-first queries, done criteria.
- Multi-mode skill: SKILL.md holds the shared rules and a Modes table (mode, use when, reference, output); each mode is `references/mode-<name>.md` with its role, process, rules and template. Per-mode file loads go in an "Also reads" column, loaded by the `files` rule.
- Principle skills (`architect`, `bdd`, `ui-design`, `obsidian`) teach a way of thinking and do not invoke the hub. `remember` skips the hub on purpose (quick capture). `scripts/check.py` lists both exemptions.

## Design principles

- Coach, not just executor: one question at a time, challenge assumptions, offer alternatives.
- Simplicity first: generic solutions over special cases, existing patterns over new abstractions.
- No bolted-on features, legacy fallbacks or "clean up later" debt.
- Honest assessment: current state, not aspirations; do not soften critical findings.
- Standalone outputs: a reader who missed the conversation can act on them.
- Analysis skills (plan, review, document, product) say clearly that they do not implement. Execution skills (implement, docker-setup) verify their result, handle failure, and list changed files.

## Before committing

1. `python3 scripts/check.py`: spec frontmatter, description length, hub and finish lines, no em dashes.
2. `uvx --from skills-ref agentskills validate skills/{name}` for each changed skill.
3. `claude plugin validate .` from the plugin root.
4. Selftests of changed scripts: `python3 skills/{name}/scripts/{script}.py --selftest`.
5. Sync `README.md` and `docs/user-guide/` when user-visible behaviour changes. Bump `version` in `.claude-plugin/plugin.json`: patch for fixes, minor for new or changed skills, major for workflow changes.
