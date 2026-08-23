---
name: Context Loading Protocol
description: Invoke this skill at the start of every bob command. Defines what project files each command should load before proceeding. Follow the protocol exactly.
user-invocable: false
---

# Context Loading Protocol

Follow this protocol at the start of every bob command.

Load the minimum context required for this phase's independent judgment. More context is not automatically better. Preserve decisions and evidence; avoid importing the previous agent's entire reasoning path.

---

## Universal (All Commands)

**Date:** Run `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
If that fails, determine today's date in YYYY-MM-DD via any available command. Use this date in all output filenames and document timestamps.

**Project familiarity:** Get oriented before starting. If `graphify-out/GRAPH_REPORT.md` exists, read only its `## Community Hubs (Navigation)` section (a few hundred tokens, not the whole report) for a cheap map of the project instead of blind exploration. Otherwise, silently explore the project structure. Commands with specific focus areas note them in their Context block.

---

## Per-Command Loading

Read each listed file if it exists. Skip silently if missing. Skip any file already read in this conversation.

| Command | Load at start |
|---------|--------------|
| `product-vision` | `docs/product/vision.md` |
| `personas` | `docs/product/vision.md`, `docs/product/problem-space.md` |
| `design-brief` | `docs/product/vision.md`, `docs/product/personas.md` |
| `problem-space` | `docs/product/vision.md`, `docs/product/problem-space.md` |
| `business-plan` | `docs/product/vision.md`, `docs/product/business-plan.md` |
| `positioning` | `docs/product/vision.md`, `docs/product/positioning.md` |
| `validation-plan` | `docs/product/vision.md`, `docs/product/validation-plan.md` |
| `product-coach` | `docs/product/vision.md`, `docs/product/README.md` |
| `art-director` | `docs/product/vision.md` |
| `brainstorm` | `docs/product/vision.md` |
| `design` | Brainstorm Brief or accepted requirement, relevant domain knowledge, repository structure and similar capabilities. Deliberately excludes full prior conversation. |
| `plan` | `docs/product/vision.md` |
| `review-plan` | `docs/product/vision.md` |
| `implement` | `docs/product/vision.md` |
| `review` | `docs/product/vision.md` |
| `reflect` | Design Record, Implementation Note, Review verdict, selected critical code. Deliberately excludes a generic guideline dump. |
| `learn` | Corrections, interruptions, artifacts, accepted/rejected findings from this session, plus `docs/process/learnings.md` (prior staged occurrences) and existing harness rules the candidate might conflict with. Deliberately excludes unrelated product context. |
| `ui-review` | `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md`, then invoke the `bob:ui-design` skill |
| `new-command` | invoke the `bob:prompt-engineering` skill |
| `review-command` | invoke the `bob:prompt-engineering` skill |
| `improve-command` | invoke the `bob:prompt-engineering` skill |
| `investigate` | — |
| `document` | — |
| `guidelines` | — |
| `docker-setup` | — |
| `bob` | — |
| `linkedin` | `docs/product/positioning.md`, `docs/product/personas.md`, `docs/product/vision.md` |
| `knowledge` | — |
| `remember`  | — |
| `setup`     | — |
| `user-guide` | `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md` |

---

## Story Context (Engineering commands)

For `brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `learn`, `investigate`, `ui-review`:

After loading the files above, invoke the `bob:story-context` skill.
Follow its protocol exactly. Do not proceed until story context is confirmed.
Use the resolved `Path:` from the story-context output block for all artifact placement.

---

## Kanban Sync (Engineering commands, after story context confirmed)

For `brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `learn`, `investigate`, `ui-review`:

After story context is confirmed (and before Guidelines and Knowledge Retrieval), check `{story_path}/_kanban.md`:

- **Does not exist:** create it using the story-level kanban template from `bob:project-tracking` (frontmatter with `kanban-plugin: board`, story-level columns, and `new-note-folder` settings block pointing to the story's `tasks/` folder). Then read it.
- **Exists:** read it and proceed with task matching below.

**Task matching:**
- Scan the `todo`, `Ready`, and `in progress` columns for task cards
- Task cards use markdown link format: `- [ ] [Task title](tasks/file.md)` — match against the title portion only
- Semantically match task titles against: (a) the current command being run, (b) any arguments the user provided, (c) what the user said they want to do. Exact match not required — semantic equivalence is sufficient.
- **High-confidence match** (title clearly describes what we're doing): move the card from its current column to `## in progress` in the kanban file, and inform user: "Task marked in-progress: [title] on {STORY-ID} kanban."
- **Uncertain match** (multiple candidates or none align clearly): ask user: "Which task does this session target? [list task titles] — or 'none' to skip."
- **No kanban or no tasks:** proceed silently without comment.

Do not block or delay if no match is found. This step is informational — it syncs state, it does not gate work.

---

## Guidelines (Engineering commands, after scope is clear)

For `brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `investigate`, `ui-review`:

Reflect deliberately excludes this section — it does not load a generic guideline dump; see its per-command row above.

**If `docs/guidelines/` exists:**
1. Read `docs/guidelines/README.md` as the navigation index — do not load all guideline files.
2. Load guideline files matching the current scope. Match against the "Applies When" or "Triggers" column:
   - File extensions in play (e.g., ext: `.ts` → typescript.md)
   - Paths involved (e.g., path: `Frontend/` → angular.md)
   - Concepts being touched (e.g., auth changes → authentication.md)
   - Always load `markdown.md` if it exists — all engineering commands produce markdown output.
   - Load `mermaid.md` if it exists and the command produces diagrams (`plan`, `review-plan`, `brainstorm`).
3. If a loaded guideline recommends a tool that is not installed: offer to install it before proceeding (for `implement` and `review` only).

**If `docs/guidelines/` does not exist:**
Notify the user: "No project guidelines found — run `/bob:guidelines` to create them." Then apply these built-in fallback rules for the remainder of this session:

**Markdown (all engineering commands produce markdown output):**
- Always specify language on code blocks: ` ```typescript ` not ` ``` `
- Blank lines required before/after code blocks, headings, and lists
- No skipped heading levels — h1 → h2 → h3, never h1 → h3
- Frontmatter YAML: quote strings containing colons or special characters
- Tables require aligned pipes and a header separator row (`|---|`)

**Mermaid (applies when producing diagrams — `plan`, `review-plan`, `brainstorm`):**
- Node IDs: alphanumeric and underscores only — no spaces, colons, or parentheses in the ID
- Labels with spaces or special chars: `A["my label: value"]` — double quotes inside square brackets
- Arrow labels: `A -->|label| B` with no space before the pipe
- Subgraph IDs: no spaces — use `subgraph myGroup["My Group"]`
- Valid diagram types: `flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `gantt`, `pie`, `gitGraph`
- Flowchart direction: `LR`, `TD`, `TB`, `BT`, `RL`
- Validate Mermaid syntax before saving — it fails silently in many renderers

---

## Knowledge Retrieval (Engineering commands)

For `brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `learn`, `investigate`, `ui-review`:

After resolving story context and loading applicable guidelines, invoke the `bob:knowledge` skill (read-only, automatic retrieval) and follow its protocol. This is the retrieval skill, distinct from the `/bob:library` command (interactive vault management).

---

## Code Graph (Engineering commands)

For `brainstorm`, `design`, `plan`, `review-plan`, `implement`, `review`, `reflect`, `learn`, `investigate`, `ui-review`:

After resolving story context and loading applicable guidelines, invoke the `bob:code-graph` skill (read-only, automatic retrieval) and follow its protocol. It skips silently if graphify or the graph is absent.
