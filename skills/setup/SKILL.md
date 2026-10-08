---
name: setup
description: Bob's project setup. Bootstraps and upgrades bob infrastructure in a project - projects/, knowledge vault, done criteria, story structure repairs, recommended tools. Idempotent and non-destructive. Use only when the user asks to set up, install or upgrade bob in a project.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Setup

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: nothing beyond the hub's Always rules

Paths to `references/` are relative to this skill's folder (the base directory shown when it loads). Sibling skills are one folder up (`../library/`, `../learn/`).

## Rules

- Audit before acting. Never modify anything before showing the plan.
- One confirmation covers all changes. Do not prompt per item.
- Never overwrite or truncate existing files: only create missing files or append. The one exception is the `.graphifyignore` managed block, regenerated between its markers on each run; content outside the markers is always kept.
- Never silent-install third-party tools (graphify, Mermaid CLI, plugins). Recommend them; for graphify, offer the build and hook only with explicit confirmation.
- Never remove or reorder existing done-criteria sections.
- If `projects/` exists but has no subdirectories, still offer to create the first subproject.
- Skip silently any step whose target already exists and is up to date.

## Role

Project infrastructure specialist. Make every bob feature work: create what is missing, upgrade what is stale, leave everything else untouched.

## Process

1. **Audit**: run the checks in `references/audit.md`.
2. **Report and confirm**: present the status table and tool recommendations from `references/report.md`. Everything present and current: say "All bob infrastructure is present and up to date. Nothing to do." and stop. Otherwise list what will change and ask "Ready to apply?".
3. **Repair and bootstrap**: execute only the missing or partial items, per `references/repairs.md`.
4. **Upgrade done criteria**:
   - Missing: create `docs/process/` if needed, copy the hub's `assets/done-criteria.md` to `docs/process/done-criteria.md` and set today's date.
   - Exists: read it and the hub's `assets/done-criteria.md`. From the template's `## DONE` block, collect every `### ` section (heading plus all lines up to the next `### ` or `---`). Insert each section not found verbatim in the project file before its `*Last updated:*` line. Update that line to today. Report the added sections, or "already up to date".
5. **Unmanaged files**: setup does not judge or rearrange `docs/`; the `document` skill's Audit mode owns that. Orphan `.md` files found by the audit: list them and say "These files are outside bob's managed locations. To migrate: move them to `knowledge/_INBOX/` manually, then run `library process` to classify and file them." None: skip silently.
6. **Summary**: the summary table in `references/report.md`, then any manual steps left (for example the Obsidian wikilinks setting).

## Output

Changes in the project only. No report file.

Finish with the hub's finish checklist.
