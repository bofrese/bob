# Skills reference
*Last updated: 2026-10-14*

Every bob skill on one page. Call a skill as `/bob:<name>`, or describe your work and the `bob` hub picks the skill.

`{story}` below means the story folder, `projects/{sub}/stories/{ID}/`. Skills that write a report without a story write it to `docs/process/sessions/` instead.

## Hub

| Skill | Use when | Writes |
|---|---|---|
| `/bob:bob` | "Where are we, what next?", "which skill fits?", or a status report. Every phase also runs its start and finish checklists. | Optional status report or daily-note entry |

## Engineering phases

In loop order. Details: [Engineering workflows](02-engineering-workflows.md).

| Skill | Use when | Writes |
|---|---|---|
| `/bob:brainstorm` | The value, outcome or framing of an idea is open | `{story}/sessions/{date}-brainstorm-{slug}.md` |
| `/bob:design` | Concepts, boundaries, naming or system fit are open | `{story}/sessions/{date}-design-{slug}.md` |
| `/bob:plan` | The design is owned and you need the execution shape | `{story}/sessions/{date}-plan-{slug}.md` |
| `/bob:review-plan` | The risk justifies an independent check of the plan | `{story}/sessions/{date}-review-plan-{slug}.md` |
| `/bob:implement` | You ask to build an approved plan | Code + `{story}/sessions/{date}-implement-{slug}.md` |
| `/bob:review` | The change must be checked independently | `{story}/sessions/{date}-review-{slug}.md` |
| `/bob:document` | Architecture notes must match the code | `docs/architecture/` |
| `/bob:handover` | You must approve and own delegated work | `{story}/sessions/{date}-handover-{slug}.md` |
| `/bob:reflect` | After reading the Handover, or when implementation surprised you | `{story}/sessions/{date}-reflect-{slug}.md` |
| `/bob:learn` | A session showed a lesson for the AI harness. Name a skill for scoped mode. | `{story}/sessions/{date}-learn-{slug}.md`, `docs/process/learnings.md` |

## Beside the loop

| Skill | Use when | Writes |
|---|---|---|
| `/bob:dev` | A quick fix or direct change that is local, reversible and settled | Code only |
| `/bob:investigate` | A bug needs a root cause. It never fixes. | `{story}/sessions/{date}-investigate-{slug}.md` |
| `/bob:ui-review` | A screen, flow or app needs an expert UI/UX review | `{story}/sessions/{date}-ui-review-{slug}.md` |
| `/bob:ui-mockup` | Screens, pages or flows must be designed visually before they are built | `docs/design/{name}/`, `{story}/spec.md`, `{story}/input/{date}-mockup-requests.md` |

## Product

Details: [Discovery workflows](03-discovery-workflows.md).

| Skill | Use when | Writes |
|---|---|---|
| `/bob:product` | Vision, personas, problem space, validation, business plan, positioning, or "what am I missing?" | `docs/product/*.md` |
| `/bob:brand-design` | Design brief, or art direction for UI, brand and web | `docs/product/design-brief.md`, `docs/guidelines/visual-design.md` |
| `/bob:linkedin` | LinkedIn strategy, posts and profile for consultants, founders and B2B services | - |

## Knowledge

Details: [Knowledge management](05-knowledge-management.md).

| Skill | Use when | Writes |
|---|---|---|
| `/bob:document` | Architecture notes: Discover, Update or Audit | `docs/architecture/` |
| `/bob:guidelines` | You want technology guidelines or linter setup written down | `docs/guidelines/{topic}.md` |
| `/bob:user-guide` | You want an end-user guide written or checked for drift | The user guide + a findings report for the team |
| `/bob:remember` | Capture a thought now, file it later | `knowledge/_INBOX/{date}-{slug}.md` |
| `/bob:library` | File the inbox, ingest a source, search or check the vault | `knowledge/` |

## Setup and meta

| Skill | Use when | Writes |
|---|---|---|
| `/bob:setup` | Install or upgrade bob in a project. Safe to run again. | `projects/`, `knowledge/`, `personal/`, `.gitignore`, done criteria, `AGENTS.md` block |
| `/bob:docker-setup` | You ask for a Docker development environment | `Dockerfile`, Makefile targets, install docs |
| `/bob:new-skill` | Bob is missing a workflow you need | A new skill folder |
| `/bob:review-skill` | A skill triggers wrongly, is slow or gives uneven results. It proposes, never edits. | `{story}/sessions/{date}-skill-review-{name}.md` |

## Principle skills

Ways of thinking that the phases load. You can also call them directly.

| Skill | Holds |
|---|---|
| `/bob:architect` | Architecture judgment: concepts, placement, interfaces, design smells, patterns and drift |
| `/bob:bdd` | Given/When/Then acceptance criteria, testing behaviour instead of implementation |
| `/bob:ui-design` | 14 UI design lenses and a final check |
| `/bob:obsidian` | Moves and renames of markdown files that keep links intact |

## Next steps

- [Engineering workflows](02-engineering-workflows.md): how the phases work together.
