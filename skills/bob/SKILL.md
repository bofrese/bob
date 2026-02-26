---
name: bob
description: This skill should be used when the user talks to Bob by name ("what does Bob do", "explain Bob", "how does Bob work", "what commands does Bob have", "what is Bob", "how do I use Bob", "what can Bob do", "Bob's workflow", "show me Bob's commands", "Bob skills", "walk me through Bob", "I don't understand Bob", "what's the difference between these Bob commands"), or when the user asks a general question about the bob plugin, its commands, skills, workflow, or file conventions.
version: 0.1.0
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
| `ai/plans/` | Implementation plans |
| `ai/reviews/` | Code reviews, plan reviews, command reviews, UI reviews |
| `ai/implementations/` | Post-implementation reports |
| `ai/investigations/` | Bug investigation reports |
| `ai/ideas/` | Brainstorm outputs |
| `ai/issues/backlog.md` | Discovered issues and backlog items |
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

**Engineering layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:brainstorm` | `ai/ideas/{date}-brainstorm-{slug}.md` | Feature ideation: diverge → converge → commit |
| `/bob:plan` | `ai/plans/{date}-{slug}.md` | Turn idea into reviewable implementation plan |
| `/bob:review-plan` | `ai/reviews/{date}-review-{slug}.md` | Skeptical review of a plan against the codebase |
| `/bob:implement` | Project files + `ai/implementations/{date}-{slug}.md` | Execute an approved plan with engineering discipline |
| `/bob:review` | `ai/reviews/{date}-review-{slug}.md` | Code review: git diff → Critical/Important/Suggestion |
| `/bob:investigate` | `ai/investigations/{date}-{slug}.md` | Root-cause analysis (investigation only, no fixes) |
| `/bob:document` | `docs/{concept}.md` + `docs/README.md` | Generate/update dev docs; detect doc drift |
| `/bob:guidelines` | `docs/guidelines/{topic}.md` | Best-practice guidelines, research-first |
| `/bob:docker-setup` | `Dockerfile`, `Makefile`, `INSTALL.md` | Docker dev environment, standard `make` interface |
| `/bob:ui-review` | `ai/reviews/{date}-ui-review-{slug}.md` | 13-lens UI/UX expert review |
| `/bob:art-director` | `docs/guidelines/visual-design.md` (opt.) | Brand tone, color, typography direction |

**Knowledge / meta layer**

| Command | Writes | Purpose |
|---|---|---|
| `/bob:pm` | Conversational (opt. status doc) | Project mentor: assess state, recommend next step |
| `/bob:new-command` | `bob/commands/{name}.md` + README | Create a new bob command |
| `/bob:improve-command` | `ai/reviews/{date}-improve-{name}.md` | Extract session learnings to improve a command |
| `/bob:review-command` | `ai/reviews/{date}-command-review-{slug}.md` | Prompt-engineering quality review of a command |

---

## Skills — Quick Reference

Skills are thinking frameworks invoked by commands. They carry no file I/O of their own (except `done-criteria` and `domain-knowledge`).

| Skill | Invoked by | Role |
|---|---|---|
| `bob:context-protocol` | Every command | Load current date + right project files |
| `bob:done-criteria` | Every output command | Check done criteria; log issues |
| `bob:bdd` | `plan`, `implement`, `review-plan` | Write acceptance criteria before code |
| `bob:ddd` | `brainstorm`, `plan` | Domain-driven naming and bounded contexts |
| `bob:assumption-testing` | `validation-plan`, `product-coach` | Risk matrix, validation hierarchy, MVP scope |
| `bob:business-model` | `business-plan`, `product-coach` | Unit economics, revenue patterns, pricing |
| `bob:positioning-strategy` | `positioning`, `product-coach` | Five-component positioning, differentiation |
| `bob:go-to-market` | `business-plan`, `positioning`, `product-coach` | Channel selection, Bullseye framework, growth loops |
| `bob:problem-validation` | `problem-space`, `product-coach` | JTBD, severity, evidence hierarchy, Mom Test |
| `bob:ui-design` | `ui-review`, `art-director` | 13-lens evaluation framework |
| `bob:prompt-engineering` | `new-command`, `review-command`, `improve-command` | Principles for effective Claude commands |
| `bob:domain-knowledge` | `brainstorm`, `plan` (on correction) | Capture project-specific domain nuance to `docs/domain/` |

---

## Typical Workflows

**New product idea:**
`product-vision` → `problem-space` → `personas` → `validation-plan` → `business-plan` → `positioning` → `design-brief`

**New feature:**
`brainstorm` → `plan` → `review-plan` → `implement` → `review`

**Bug:**
`investigate` → `plan` → `implement` → `review`

**Not sure what to do next:**
`/bob:pm` or `product-coach`

---

## Additional Resources

- **`references/commands.md`** — dense per-command descriptions: inputs, outputs, process phases, skills invoked
- **`references/skills.md`** — dense per-skill descriptions: what each framework covers and when to use it
