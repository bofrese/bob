---
name: bob
description: This skill should be used when the user talks to Bob by name ("what does Bob do", "explain Bob", "how does Bob work", "what commands does Bob have", "what is Bob", "how do I use Bob", "what can Bob do", "Bob's workflow", "show me Bob's commands", "Bob skills", "walk me through Bob", "I don't understand Bob", "what's the difference between these Bob commands"), or when the user asks a general question about the bob plugin, its commands, skills, workflow, or file conventions.
user-invocable: true
---

# Bob — Plugin Reference

Bob is a Claude Code plugin covering the full product development lifecycle — from raw idea to shipped code. It imposes structured thinking at every stage rather than letting AI free-wheel. Bob is organized into three layers:

- **Discovery** — product strategy, market validation, personas, positioning
- **Engineering** — planning, implementing, reviewing, documenting code
- **Knowledge** — guidelines, domain capture, command quality improvement

All commands share two mandatory protocols:
- `bob:context-protocol` — loads current date and the right project files before starting
- `bob:done-criteria` — checks `docs/process/done-criteria.md` and logs issues on finish

---

## File Conventions

Bob reads and writes to predictable locations:

| Location | Purpose |
|---|---|
| `docs/product/` | Product strategy artifacts (vision, personas, design-brief, etc.) |
| `docs/guidelines/` | Technology best-practice guides |
| `docs/domain/` | Project-specific domain knowledge |
| `docs/process/done-criteria.md` | What "done" means per artifact type |
| `projects/{name}/stories/{ID}/` | Engineering session artifacts (plans, reviews, implementations, investigations, brainstorms) and story-specific reference materials (specs, external docs, source inputs) while being worked on. |
| `projects/{name}/_kanban.md` | Project-level kanban (stories as cards) |
| `knowledge/` | Validated project knowledge: decisions made, confirmed patterns, defined concepts, synthesised research. Not for in-flight specs, drafts, or rough ideas. |
| `knowledge/_INBOX/` | Staging area for rough captures not yet classified — gitignored. Run `/bob:library process` to file. |
| `personal/` | Personal daily/weekly notes and scratchpad — gitignored, never committed |
| `bob/commands/` | Command definitions (slash commands) |
| `bob/skills/` | Thinking frameworks invoked by commands |

---

## Commands — Quick Reference

**Discovery layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:product-vision` | `docs/product/vision.md` | Foundation: what it is, who it's for, what changes |
| `/bob:problem-space` | `docs/product/problem-space.md` | Validate the problem before building the solution |
| `/bob:personas` | `docs/product/personas.md` | User archetypes with genuine design implications |
| `/bob:business-plan` | `docs/product/business-plan.md` | Revenue model, unit economics, GTM |
| `/bob:positioning` | `docs/product/positioning.md` | Market category, differentiation, messaging |
| `/bob:validation-plan` | `docs/product/validation-plan.md` | Assumption stack, ranked experiments, kill criteria |
| `/bob:design-brief` | `docs/product/design-brief.md` | Design principles and constraints (not a UI spec) |
| `/bob:product-coach` | `docs/product/README.md` + above docs | Orchestrator: gaps, what to do next |
| `/bob:linkedin` | `docs/product/linkedin-strategy.md` | LinkedIn growth strategy advisor |

**Engineering layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:brainstorm` | `{story_path}/{date}-brainstorm-{slug}.md` | Feature ideation: diverge → converge → commit; routes to Design |
| `/bob:design` | `{story_path}/{date}-design-{slug}.md` | Socratic conceptual design: concepts, boundaries, trade-offs, human-owned decisions |
| `/bob:plan` | `{story_path}/{date}-plan-{slug}.md` | Translate a Design Record into a reviewable implementation plan |
| `/bob:review-plan` | `{story_path}/{date}-review-plan-{slug}.md` | Skeptical review of a plan against Design and the codebase (recommended for high-risk work) |
| `/bob:implement` | Project files + `{story_path}/{date}-implement-{slug}.md` | Execute an approved plan with engineering discipline |
| `/bob:review` | `{story_path}/{date}-review-{slug}.md` | Code review: git diff → Critical/Important/Suggestion |
| `/bob:investigate` | `{story_path}/{date}-investigate-{slug}.md` | Root-cause analysis (investigation only, no fixes) |
| `/bob:dev` | Project files (in place) | Quick working session: discuss code, make fixes, no pipeline |
| `/bob:document` | `docs/{concept}.md` + `docs/README.md` | Generate/update dev docs; detect doc drift |
| `/bob:user-guide` | `docs/user-guide.md` (configurable) + `{story_path}/{date}-user-guide-findings-{slug}.md` | Create/maintain end-user guide; surfaces UX gaps as findings report |
| `/bob:guidelines` | `docs/guidelines/{topic}.md` | Best-practice guidelines, research-first |
| `/bob:docker-setup` | `Dockerfile`, `Makefile`, `INSTALL.md` | Docker dev environment, standard `make` interface |
| `/bob:ui-review` | `{story_path}/{date}-ui-review-{slug}.md` | 13-lens UI/UX expert review |
| `/bob:art-director` | `docs/guidelines/visual-design.md` (opt.) | Brand tone, color, typography direction |

**Knowledge layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:library` | `knowledge/` notes, indexes, MOCs, `log.md`, `sources/` | Librarian: process inbox, ingest external sources, retrieve, organise vault, status |
| `/bob:remember` | `knowledge/_INBOX/YYYY-MM-DD-*.md` | Quick mid-session capture to inbox |

**Meta layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:pm` | Conversational (opt. status doc) | Project mentor: assess state, recommend next step |
| `/bob:setup` | `projects/`, `knowledge/`, `personal/`, `.gitignore`, `docs/process/done-criteria.md` | Bootstrap and upgrade bob infrastructure; idempotent |
| `/bob:new-command` | `bob/commands/{name}.md` + README | Create a new bob command |
| `/bob:improve-command` | `ai/reviews/{date}-improve-{name}.md` | Extract session learnings to improve a command |
| `/bob:review-command` | `ai/reviews/{date}-command-review-{slug}.md` | Prompt-engineering quality review of a command |

> Note: `{story_path}` is resolved by the `bob:story-context` skill at the start of each engineering command session.

---

## Skills — Quick Reference

Skills are thinking frameworks invoked by commands. They carry no file I/O of their own (except `done-criteria`, `domain-knowledge`, `knowledge` retrieval, and `code-graph` detection).

| Skill | Invoked by | Role |
|---|---|---|
| `bob:context-protocol` | Every command | Load current date + right project files; kanban sync for engineering commands; wire story-context |
| `bob:story-context` | Every engineering command (via context-protocol) | Resolve active story via 4-tier chain; establish `{story_path}` for artifact placement |
| `bob:done-criteria` | Every output command | Check done criteria; delegate issue routing to work-routing; update story history |
| `bob:work-routing` | All engineering commands (mid-session) + `done-criteria` (Behaviour 6) | Route discovered issues/ideas to story Issues column or project INBOX; single user confirmation |
| `bob:bdd` | `plan`, `implement`, `review-plan` | Write acceptance criteria before code |
| `bob:ddd` | `plan` | Domain-driven naming and bounded contexts |
| `bob:design` | `/bob:design` | Socratic, evidence-based conceptual design framework: interaction policy, comprehensibility lenses, Design Record template |
| `bob:assumption-testing` | `validation-plan`, `product-coach` | Risk matrix, validation hierarchy, MVP scope |
| `bob:business-model` | `business-plan`, `product-coach` | Unit economics, revenue patterns, pricing |
| `bob:positioning-strategy` | `positioning`, `product-coach` | Five-component positioning, differentiation |
| `bob:go-to-market` | `business-plan`, `positioning`, `product-coach` | Channel selection, Bullseye framework, growth loops |
| `bob:problem-validation` | `problem-space`, `product-coach` | JTBD, severity, evidence hierarchy, Mom Test |
| `bob:ui-design` | `ui-review`, `art-director` | 13-lens evaluation framework |
| `bob:prompt-engineering` | `new-command`, `review-command`, `improve-command` | Principles for effective Claude commands |
| `bob:domain-knowledge` | `brainstorm`, `plan` (on correction) | Capture project-specific domain nuance to `docs/domain/` |
| `bob:linkedin-expert` | `linkedin` | LinkedIn domain knowledge: algorithm, formats, DMs, comments, profile |
| `bob:obsidian` | Auto (hook) + any `.md` rename/move | Route `.md` file moves through Obsidian CLI to preserve wikilinks |
| `bob:knowledge` | `context-protocol` (every engineering command) | Retrieval skill: load relevant vault notes into context silently; distinct from `/bob:library` command |
| `bob:code-graph` | `context-protocol` (every engineering command) | Detect a graphify code graph, gate freshness, emit query policy silently; delegates all traversal to graphify. Degrades silently if graphify absent |
| `bob:vault` | `/bob:library` | Vault management controller: routes to process, ingest, organise, bootstrap sub-files; owns Python scripts |

---

## Typical Workflows

**New product idea:**
`product-vision` → `problem-space` → `personas` → `validation-plan` → `business-plan` → `positioning` → `design-brief`

**New feature:**
`brainstorm` → `design` → `plan` → `review-plan` → `implement` → `review`

**Bug:**
`investigate` → `plan` → `implement` → `review`

**Not sure what to do next:**
`/bob:pm` or `product-coach`

---

## Additional Resources

- **`references/commands.md`** — dense per-command descriptions: inputs, outputs, process phases, skills invoked
- **`references/skills.md`** — dense per-skill descriptions: what each framework covers and when to use it
