# Commands Reference
*Last updated: 2026-08-23*

Quick lookup for all bob commands, organized by layer.

## Quick Find

**Looking for a command? Use search (Cmd+F / Ctrl+F) or scroll to your layer:**
- [Discovery Commands](#discovery-commands)
- [Engineering Commands](#engineering-commands)
- [Knowledge Commands](#knowledge-commands)
- [Meta Commands](#meta-commands)

---

## Discovery Commands

Use these to figure out what to build and why. All optional—skip if you have clear strategy already.

### `/bob:product-coach`
**The entry point for product strategy work.**

Your guide through the full discovery process. Assess what exists, identify gaps, recommend next steps. Maintains `docs/product/README.md` so you always know what's been done.

| | |
|---|---|
| **Start here when** | You want comprehensive guidance through discovery, or you're filling gaps in existing product docs |
| **Output** | Product artifacts in `docs/product/` as needed |
| **Time** | Varies by mode (30min to 2hrs per artifact) |

---

### `/bob:product-vision`
**Establish what you're building, who it's for, why it matters.**

Creates or updates your strategic north star. Everything else flows from this.

| | |
|---|---|
| **Reads** | Existing `docs/product/vision.md` if updating |
| **Writes** | `docs/product/vision.md` |
| **Start here when** | New product, or strategy needs revisiting |
| **Output includes** | Problem statement, market opportunity, target persona, solution approach, success metrics |
| **Time** | 45min – 2hrs |

---

### `/bob:personas`
**Define the real people you're building for.**

Detailed characters with goals, behaviors, frustrations—not demographics.

| | |
|---|---|
| **Reads** | `docs/product/vision.md` |
| **Writes** | `docs/product/personas.md` |
| **Start here when** | After vision is set, before design or detailed planning |
| **Time** | 30 – 60min |

---

### `/bob:design-brief`
**The visual and interactive direction.**

How should this product look and feel? What interaction patterns?

| | |
|---|---|
| **Reads** | `docs/product/vision.md`, `docs/product/personas.md` |
| **Writes** | `docs/product/design-brief.md` |
| **Start here when** | After vision and personas |
| **Time** | 20 – 45min |

---

### `/bob:problem-space`
**Validate the problem before building solutions.**

Is this real? Painful enough? Why hasn't it been solved?

| | |
|---|---|
| **Reads** | `docs/product/vision.md` |
| **Writes** | `docs/product/problem-space.md` |
| **Start here when** | After vision, before major resource commitment |
| **Time** | 30 – 60min |

---

### `/bob:business-plan`
**How do you create and capture value?**

Pricing, revenue model, unit economics.

| | |
|---|---|
| **Reads** | `docs/product/vision.md`, `docs/product/personas.md` |
| **Writes** | `docs/product/business-plan.md` |
| **Start here when** | Strategy solidifying, need business model clarity |
| **Time** | 45min – 1.5hrs |

---

### `/bob:positioning`
**How you win in the market.**

Competitive strategy, differentiation, go-to-market.

| | |
|---|---|
| **Reads** | `docs/product/vision.md`, `docs/product/business-plan.md` (if exists) |
| **Writes** | `docs/product/positioning.md` |
| **Start here when** | After business model, before launch |
| **Time** | 1 – 2hrs |

---

### `/bob:validation-plan`
**Test your biggest assumptions before building.**

What are you betting on? How will you validate?

| | |
|---|---|
| **Reads** | All existing `docs/product/` artifacts |
| **Writes** | `docs/product/validation-plan.md` |
| **Start here when** | After strategy defined, before major development commitment |
| **Time** | 30 – 75min |

---

## Engineering Commands

The core pipeline: idea → plan → code → review → shipped.

### `/bob:brainstorm`
**Structured ideation for a feature.**

Coaches you through diverge → converge → detail → commit. Challenges the idea for value — does not decide architecture.

| | |
|---|---|
| **Reads** | `docs/product/vision.md` (if present) |
| **Writes** | `{story_path}/{date}-brainstorm-{slug}.md` (a Brainstorm Brief) |
| **Start here when** | You have an idea and want to think it through properly |
| **Process** | Seed → Diverge → Converge → Detail → Commit |
| **Time** | 30min – 1.5hrs |

---

### `/bob:design`
**Form the simplest coherent conceptual design for a capability.**

Socratic, evidence-based, and human-owned. Investigates the repository first, then runs a Socratic conversation about concepts, boundaries, and trade-offs — one question or tightly-related batch at a time.

| | |
|---|---|
| **Reads** | Brainstorm Brief or accepted requirement, repository evidence (code graph when fresh, else manual exploration) |
| **Writes** | `{story_path}/{date}-design-{slug}.md` (a Design Record) |
| **Start here when** | After brainstorm, for conceptually meaningful work; skip for stable, simple requirements |
| **Output includes** | Existing/new concepts, boundaries, trade-offs, alternatives rejected, human-owned decisions, AI assumptions, unresolved questions |
| **Time** | 20min – 1hr |

---

### `/bob:plan`
**Turn a Design Record (or a simple accepted requirement) into a concrete implementation plan.**

Self-contained so someone without the conversation context can execute it. Loads BDD principles for testing.

| | |
|---|---|
| **Reads** | Design Record (or brainstorm/requirement for simple work), `docs/guidelines/`, BDD principles |
| **Writes** | `{story_path}/{date}-plan-{slug}.md` |
| **Start here when** | After design (or after brainstorm/a known requirement, for simple work), before code |
| **Output includes** | Approach, test strategy, implementation steps, questions & decisions, risks |
| **Time** | 30min – 1hr |

---

### `/bob:review-plan`
**Independent critical review of a plan.**

Fresh context. Doesn't trust the plan's assumptions—re-reads the codebase. Looks for gaps, oversimplifications, security issues, simpler alternatives.

| | |
|---|---|
| **Reads** | The plan file + actual codebase |
| **Writes** | `{story_path}/{date}-review-plan-{slug}.md` |
| **Start here when** | Plan is written, before implementation begins |
| **Why separate** | Session boundaries kill the "pleaser" instinct. Honest critique instead of polite agreement |
| **Time** | 20 – 40min |

---

### `/bob:implement`
**Execute an approved plan.**

Runs full test suite first (green baseline). Implements step by step. Loads BDD for test writing. Stops when it hits decisions you need to make.

| | |
|---|---|
| **Reads** | The approved plan, BDD principles |
| **Writes** | Modified code + `{story_path}/{date}-implement-{slug}.md` |
| **Start here when** | Plan reviewed and approved |
| **Output includes** | What was built, deviations from plan, discoveries, test results |
| **Time** | Varies (30min – several hours) |

---

### `/bob:review`
**Code review of what was built.**

Auto-detects scope from git (uncommitted changes, branch commits, range). Loads guidelines. Assesses system health. Produces handoff document.

| | |
|---|---|
| **Reads** | Changed files, the plan (if exists), applicable guidelines |
| **Writes** | `{story_path}/{date}-review-{slug}.md` |
| **Start here when** | Implementation done, before merging |
| **Checks** | Does code do what plan said? Is it clean? Do tests verify behavior? Follow guidelines? Codebase healthy? |
| **Time** | 20 – 60min |

---

### `/bob:reflect`
**Recover ownership after correctness is established.**

Short, non-quizzy peer conversation. Assumes `/bob:review` already settled correctness — picks two to five questions from actual Design/Implement/Review evidence, lets you answer first, and inspects vague areas together. A brief "no gap" record is a valid outcome.

| | |
|---|---|
| **Reads** | Design Record, Implementation Note, Review verdict, selected critical code |
| **Writes** | `{story_path}/{date}-reflect-{slug}.md` (a Reflection Record) |
| **Start here when** | After review, for significant agent-implemented changes |
| **Output includes** | Expectation vs. reality, ownership gaps (if any), candidates for `/bob:learn` and the backlog |
| **Time** | 5 – 20min |

---

### `/bob:learn`
**Extract durable harness lessons, or none.**

Runs at the end of a session (typically after Reflect). Classifies evidence — corrections, interruptions, repeated Review findings, missing tools — into destinations: a durable bob prompt/skill improvement, a staged occurrence (not yet a pattern), or nothing. "No lesson this time" is a valid, common outcome.

| | |
|---|---|
| **Reads** | Session evidence (corrections, interruptions, artifacts, accepted/rejected findings), `docs/process/learnings.md` |
| **Writes** | `{story_path}/{date}-learn-{slug}.md` + updates `docs/process/learnings.md` |
| **Start here when** | End of a session that exposed a reusable harness lesson |
| **Time** | 5 – 15min |

`/bob:improve-command` is now a thin, scoped wrapper over this — limited to a single command's improvement.

---

### `/bob:ui-review`
**UI/UX review against design principles.**

Uses 13 design lenses. If vision/personas/design-brief exist, checks alignment. Connects findings to user impact.

| | |
|---|---|
| **Reads** | `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md` (if present) |
| **Writes** | `{story_path}/{date}-ui-review-{slug}.md` |
| **Start here when** | Before shipping UI changes, or when something feels off |
| **Time** | 20 – 45min |

---

### `/bob:investigate`
**Systematic investigation of bugs and issues.**

Root cause analysis, not quick fixes. Explores thoroughly. Identifies contributing factors.

| | |
|---|---|
| **Reads** | Relevant codebase, error logs, related code |
| **Writes** | `{story_path}/{date}-investigate-{slug}.md` |
| **Start here when** | Bug or issue that needs proper diagnosis before fixing |
| **Output includes** | Problem statement, root cause, contributing factors, solution direction |
| **Time** | 20 – 60min depending on complexity |

---

## Knowledge Commands

Build and maintain the knowledge base that makes every future session better.

### `/bob:document`
**Generate or update developer documentation.**

Two modes: **new** (docs for undocumented features) or **maintenance** (detect drift).

| | |
|---|---|
| **Reads** | The codebase, existing docs |
| **Writes** | `docs/{concept}.md`, updates `docs/README.md` |
| **Start here when** | After new features ship, or quarterly for maintenance |
| **Modes** | new (document something), maintenance (find drift) |
| **Time** | 20 – 45min |

---

### `/bob:guidelines`
**Create best-practice guidelines for your tech.**

Research-first: official style guides and standards, *then* your code. Elevates code quality automatically.

| | |
|---|---|
| **Reads** | Official sources, then the codebase |
| **Writes** | `docs/guidelines/{topic}.md` |
| **Start here when** | Setting up a project, adopting new tech, need consistency |
| **Time** | 30 – 60min |

---

### `/bob:remember`
**Quick capture to the knowledge vault inbox.**

No phases, no overhead. Call it mid-session without breaking flow.

```
/bob:remember We should avoid X because of Y — discovered in AUTH-002
```

With no arguments: asks "What should I remember?" — one question, done. Writes to `knowledge/_INBOX/`. Bootstraps the vault on first use.

| | |
|---|---|
| **Writes** | `knowledge/_INBOX/YYYY-MM-DD-{slug}.md` |
| **Start here when** | You want to capture something now and file it properly later |
| **Time** | Under 1min |

---

### `/bob:library`
**Manage the project knowledge vault.**

| | |
|---|---|
| **Reads** | `knowledge/` vault |
| **Writes** | Typed vault notes, vault indexes |
| **Start here when** | Processing inbox items, searching the vault, or running a vault health check |

**Modes:**

| Command | What it does |
|---------|-------------|
| `/bob:library` | Vault status: inbox count, note counts, pending suggestions |
| `/bob:library process` | Work through inbox items interactively — propose type, tags, filename; file on approval |
| `/bob:library ingest <url-or-file>` | Ingest an external source directly into a typed note |
| `/bob:library retrieve <query>` | Search vault for notes matching a query |
| `/bob:library organise` | Vault health check: orphaned notes, tag consistency, MOC candidates |

---

## Meta Commands

The toolkit maintains itself. Build, review, improve commands.

### `/bob:pm`
**Project mentor and manager.**

Reads your kanban boards, assesses project state, recommends what to work on next. Also helps start sessions efficiently and recommends the right command for what you're trying to do.

| | |
|---|---|
| **Reads** | `projects/_index.md`, sub-project and story kanban boards |
| **Writes** | Optional summary to `personal/daily/YYYY-MM-DD.md`, or full report to `ai/{date}-project-status.md` |
| **Start here when** | New session, unsure what to do, want project overview |
| **Time** | 10 – 20min |

**Modes:**
- **Default:** First checks `bob:story-context` — if you're resuming a specific story, it summarizes that story's state and recommends the next command directly instead of a generic dashboard. Otherwise it treats this as new work, risk-classifies it, recommends fast/standard/full, and only creates a story if tracking is actually needed. Falls through to the kanban dashboard either way.
- **Context optimization:** "Help me start a session on [feature]" — tells you exactly which files to load and which command to run.
- **Command recommendation:** Describe what you want to do and pm identifies the right command.
- **Status report:** Writes a structured report covering discovery foundation, recent activity, guidelines coverage, open plans, and gaps.

---

### `/bob:new-command`
**Create a new slash command.**

Guides you through design. Creates file. Updates README. Use when the toolkit is missing something.

| | |
|---|---|
| **Writes** | `commands/{command-name}.md`, updates README |
| **Start here when** | Toolkit missing a workflow you need |
| **Time** | 30 – 60min |

---

### `/bob:review-command`
**Optimize an existing command.**

Finds bloat, ambiguity, missing guardrails. Proposes leaner version.

| | |
|---|---|
| **Reads** | Command file |
| **Writes** | Improved command file |
| **Start here when** | Command feels slow or produces inconsistent results |
| **Time** | 15 – 30min |

---

### `/bob:improve-command`
**Extract learnings from a completed session — scoped to one command.**

A thin wrapper over `/bob:learn`, scoped to a single command's design/process/output. Kept available during the transition; `/bob:learn` is now the primary, session-wide version of this.

| | |
|---|---|
| **Reads** | Session history, command file, outputs produced |
| **Writes** | `ai/reviews/{date}-improve-{command-name}.md` |
| **Start here when** | After using a command and identifying improvements |
| **Time** | 20 – 40min |

---

### `/bob:setup`
**Bootstrap or upgrade Bob infrastructure on any project.**

Idempotent — safe to run on new or existing projects. Creates what's missing, upgrades stale infrastructure, leaves everything else untouched. The right starting point for a new project.

What it creates/checks:
- `projects/{name}/` with initial kanban board
- `knowledge/` vault structure
- `personal/daily/` and `personal/weekly/` folders
- `.gitignore` entries for private/local folders
- `docs/process/done-criteria.md`

| | |
|---|---|
| **Checks** | `projects/`, `knowledge/`, `personal/`, `.gitignore`, done-criteria |
| **Writes** | Missing infrastructure — one confirmation covers all changes |
| **Start here when** | Setting up a new project, or after installing bob on an existing project |
| **Time** | 5 – 10min |

---

## DevOps Commands

### `/bob:docker-setup`
**Set up or update Docker development environment.**

Creates Dockerfile, Makefile, install docs. Verifies it works.

| | |
|---|---|
| **Reads** | Project structure, dependencies |
| **Writes** | `Dockerfile`, `Makefile`, `docs/install.md`, `ai/docker/{date}-docker-setup.md` |
| **Start here when** | Setting up containerized dev environment |
| **Time** | 20 – 45min |

---

## Other Commands

### `/bob:art-director`
Art direction coaching for visual design, UI, brand. Works as a creative partner to develop visual identity and design language.

| | |
|---|---|
| **Reads** | `docs/product/vision.md`, `docs/product/design-brief.md` (if exists) |
| **Start here when** | You need visual design direction or creative feedback |

### `/bob:dev`
**Fast path — no pipeline.** Working session for code discussion, quick fixes, and direct changes: no brainstorm/design/plan/review cycle. Checks each change against a four-question escalation test (new concept? contract change? boundary crossing? hard to reverse?) — any "yes" means it recommends `/bob:design` instead of proceeding.

| | |
|---|---|
| **Start here when** | Work is local, reversible, conceptually settled, and easily verified |
| **Time** | Minutes |

### `/bob:user-guide`
Create or maintain the user-facing documentation for this project.

---

## Using Commands Effectively

**One command per session.** Don't try to brainstorm, plan, and implement in one go. Each command is focused.

**Read the output carefully.** It's your first draft, not gospel. Engage with it. Push back. Edit before committing.

**Follow session boundaries.** They exist for a reason: clean context, explicit decisions, honest critique.

**Read the reports before the next phase.** They're not just logs—they're context the next command builds on and your chance to catch problems early.

**Edit the plans.** Plans include a "Questions & Decisions" table. Your job is to review it, approve, override, add context.

**Trust done-criteria.** If a command flags something as not done, it probably is right. The criteria exist because something slipped before.

---

## Next Steps

- [Engineering Workflows](02-engineering-workflows.md) — How to use these commands together
- [Project Management](04-project-management.md) — How work is organized
