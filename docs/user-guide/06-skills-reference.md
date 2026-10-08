# Skills Reference
*Last updated: 2026-10-08*

Quick lookup for all bob skills, organized by layer. Each skill is invoked as `/bob:<name>`, or loads automatically when you describe matching work.

## Quick Find

**Looking for a skill? Use search (Cmd+F / Ctrl+F) or scroll to your layer:**
- [Product Skills](#product-skills)
- [Engineering Skills](#engineering-skills)
- [Knowledge Skills](#knowledge-skills)
- [Meta Skills](#meta-skills)
- [Principle Skills](#principle-skills)

---

## Product Skills

Use these to figure out what to build and why. All optional - skip if you have clear strategy already.

### `/bob:product`
**Product discovery coach and keeper of `docs/product/`.**

One skill, several modes. Name the mode in your request ("write the vision", "define personas") or leave it open: the default coach mode assesses what exists, finds gaps and moves into a mode when needed. Product work has no story; documents are updated in place.

| Mode | Use when | Writes (`docs/product/`) |
|---|---|---|
| coach (default) | Discovery from the start, "what am I missing", maintaining the product docs | `README.md` plus any document below |
| vision | What the product is, who it is for, why it matters | `vision.md` |
| personas | Who the users are | `personas.md` |
| problem-space | Is the problem real and painful enough? Kill or proceed | `problem-space.md` |
| validation | Biggest assumptions, experiments, MVP scope | `validation-plan.md` |
| business-plan | Business model, pricing, unit economics | `business-plan.md` |
| positioning | Market position, differentiation, go-to-market | `positioning.md` |

| | |
|---|---|
| **Reads** | Existing `docs/product/` documents; modes read the ones they depend on (vision first) |
| **Start here when** | New product, strategy needs revisiting, or product docs have gaps |
| **Time** | 30min to 2hrs per document |

---

### `/bob:brand-design`
**Design direction and art direction.**

| Mode | Use when | Writes |
|---|---|---|
| design-brief | The product's design goals, principles, tone and voice | `docs/product/design-brief.md` |
| art-director | Visual direction for UI, web, brand or marketing: palette, typography, layout, mockup critique | `docs/guidelines/visual-design.md` (optional) |

Grounds itself in `vision.md` and `personas.md`; flags them when missing. Direction only - it does not design screens.

| | |
|---|---|
| **Time** | 20 – 45min |

---

### `/bob:linkedin`
**LinkedIn growth advisor** for consultants, founders and B2B service businesses. Content pillars, posts, comments, DMs and profile, grounded in your positioning and personas.

---

## Engineering Skills

The core pipeline: idea → plan → code → review → shipped.

### `/bob:brainstorm`
**Structured ideation for a feature.**

Coaches you through diverge → converge → detail → commit. Challenges the idea for value - does not decide architecture.

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

Socratic, evidence-based, and human-owned. Investigates the repository first, then runs a Socratic conversation about concepts, boundaries, and trade-offs - one question or tightly-related batch at a time.

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

Fresh context. Doesn't trust the plan's assumptions - re-reads the codebase. Looks for gaps, oversimplifications, security issues, simpler alternatives.

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

### `/bob:handover`
**Narrate a delivered change for approval instead of a pull request.**

Gathers the change set since the last handover (story repo plus submodules), confirms the scope with you, and narrates the full diff for approval instead of a pull request: problem, main design ideas, a walkthrough in conceptual order with code excerpts and reasoning, sweeps for mechanical changes, future impact and a coverage table checked by script.

| | |
|---|---|
| **Reads** | Story artifacts (Brainstorm to Review), updated architecture notes, the diffs |
| **Writes** | `{story_path}/sessions/{date}-handover-{slug}.md` |
| **Start here when** | After Document, when delegated work must become yours |
| **Time** | 5 – 15min |

---

### `/bob:reflect`
**Recover ownership after reading the Handover.**

Short, non-quizzy peer conversation. Assumes `/bob:review` settled correctness and you read the Handover. Picks two to five questions from actual evidence (Handover gaps, Review deviations, smells, drift, missed simplifications), lets you answer first, and inspects vague areas together. A brief "no gap" record is a valid outcome.

| | |
|---|---|
| **Reads** | Handover, Design Record, Review verdict, notes the Handover links to, selected critical code |
| **Writes** | `{story_path}/sessions/{date}-reflect-{slug}.md` (a Reflection Record) |
| **Start here when** | After the Handover, for significant agent-implemented changes |
| **Output includes** | Expectation vs. reality, ownership gaps (if any), candidates for `/bob:learn`, `/bob:document` and the backlog |
| **Time** | 5 – 20min |

---

### `/bob:learn`
**Extract durable harness lessons, or none.**

Runs at the end of a session (typically after Reflect). Classifies evidence - corrections, interruptions, repeated Review findings, missing tools - into destinations: a durable bob prompt/skill improvement, a staged occurrence (not yet a pattern), or nothing. "No lesson this time" is a valid, common outcome.

| | |
|---|---|
| **Reads** | Session evidence (corrections, interruptions, artifacts, accepted/rejected findings), `docs/process/learnings.md` |
| **Writes** | `{story_path}/{date}-learn-{slug}.md` + updates `docs/process/learnings.md` |
| **Start here when** | End of a session that exposed a reusable harness lesson |
| **Time** | 5 – 15min |

**Scoped mode:** name one skill ("improve plan from this session") and `/bob:learn` limits itself to that skill. It writes a report into the story's `sessions/` folder, else `docs/process/`.

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

## Knowledge Skills

Build and maintain the knowledge base that makes every future session better.

### `/bob:document`
**Write and maintain canonical architecture notes.**

Concept-first, atomic notes for every important system concept and codebase pattern. Three modes: **Discover** (first map, you confirm the concept and pattern lists), **Update** (after Review, notes match what was built), **Audit** (drift check of notes and `docs/`).

| | |
|---|---|
| **Reads** | The codebase, the story's Design Record, Implementation Note and Review, existing notes and `docs/` |
| **Writes** | `docs/architecture/concepts/`, `docs/architecture/patterns/`, `docs/architecture/README.md` |
| **Start here when** | After Review, or on a project with no architecture notes yet |
| **Modes** | Discover, Update, Audit |
| **Time** | 10 – 45min |

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
/bob:remember We should avoid X because of Y - discovered in AUTH-002
```

With no arguments: asks "What should I remember?" - one question, done. Writes to `knowledge/_INBOX/`. Bootstraps the vault on first use.

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

| Call | What it does |
|---------|-------------|
| `/bob:library` | Vault status: inbox count, note counts, pending suggestions |
| `/bob:library process` | Work through inbox items interactively - propose type, tags, filename; file on approval |
| `/bob:library ingest <url-or-file>` | Ingest an external source directly into a typed note |
| `/bob:library retrieve <query>` | Search vault for notes matching a query |
| `/bob:library organise` | Vault health check: orphaned notes, tag consistency, MOC candidates |

---

## Meta Skills

The toolkit maintains itself. Orient, build and review skills.

### `/bob:bob`
**The hub: start and finish checklists, project mentor.**

Every bob phase invokes the hub at its start (resolve the story, load project knowledge, name the phase) and at its end (story History, done criteria, next step). You can also call it directly for "where am I, what next": it reads your kanban boards, assesses project state and recommends one next step.

| | |
|---|---|
| **Reads** | `projects/_index.md`, sub-project and story kanban boards |
| **Writes** | Optional summary to `personal/daily/YYYY-MM-DD.md`, or a status report in the story's `sessions/` folder (else `docs/process/`) |
| **Start here when** | New session, unsure what to do, want project overview |

**Modes:**
- **Where am I (default):** If you are resuming a story, it summarizes the story's state and recommends the next skill. Otherwise it treats this as new work, risk-classifies it, recommends fast/standard/full, and only creates a story if tracking is needed.
- **Which phase:** Describe what you want to do and it names the right skill and why.
- **Start a new session:** "Help me start a session on [feature]" - tells you which files to load.
- **Status report:** A structured report covering discovery foundation, recent activity, guidelines coverage, open plans and gaps.

---

### `/bob:new-skill`
**Create a new skill.**

Guides you through proposal questions and design, creates `SKILL.md` and references, validates, and updates the README skill table.

| | |
|---|---|
| **Writes** | `skills/{skill-name}/SKILL.md` (and references), README skill table |
| **Start here when** | Toolkit missing a workflow you need |
| **Time** | 30 – 60min |

---

### `/bob:review-skill`
**Optimize an existing skill.**

Checks spec compliance, description triggering, progressive disclosure and token efficiency. Proposes a leaner version; never edits the skill itself.

| | |
|---|---|
| **Reads** | The skill |
| **Writes** | Review report in the story's `sessions/` folder, else `docs/process/` |
| **Start here when** | A skill feels slow, triggers wrongly or produces inconsistent results |
| **Time** | 15 – 30min |

---

### `/bob:setup`
**Bootstrap or upgrade Bob infrastructure on any project.**

Idempotent - safe to run on new or existing projects. Creates what's missing, upgrades stale infrastructure, leaves everything else untouched. The right starting point for a new project.

What it creates/checks:
- `projects/{name}/` with initial kanban board
- `knowledge/` vault structure
- `personal/daily/` and `personal/weekly/` folders
- `.gitignore` entries for private/local folders
- `docs/process/done-criteria.md`

| | |
|---|---|
| **Checks** | `projects/`, `knowledge/`, `personal/`, `.gitignore`, done-criteria |
| **Writes** | Missing infrastructure - one confirmation covers all changes |
| **Start here when** | Setting up a new project, or after installing bob on an existing project |
| **Time** | 5 – 10min |

---

## DevOps Skills

### `/bob:docker-setup`
**Set up or update Docker development environment.**

Creates Dockerfile, Makefile, install docs. Verifies it works.

| | |
|---|---|
| **Reads** | Project structure, dependencies |
| **Writes** | `Dockerfile`, `Makefile`, `docs/install.md`, a setup note |
| **Start here when** | Setting up containerized dev environment |
| **Time** | 20 – 45min |

---

## Other Skills

### `/bob:dev`
**Fast path - no pipeline.** Working session for code discussion, quick fixes, and direct changes: no brainstorm/design/plan/review cycle. Checks each change against a four-question escalation test (new concept? contract change? boundary crossing? hard to reverse?) - any "yes" means it recommends `/bob:design` instead of proceeding.

| | |
|---|---|
| **Start here when** | Work is local, reversible, conceptually settled, and easily verified |
| **Time** | Minutes |

### `/bob:user-guide`
Create or maintain the user-facing documentation for this project. Also reports UX gaps and missing features as a separate findings report.

## Principle Skills

Ways of thinking that other skills load, and that you can call directly: `/bob:architect` (architecture judgment), `/bob:bdd` (acceptance criteria, testing behaviour), `/bob:ui-design` (14 UI lenses), `/bob:obsidian` (vault-safe moves and renames).

---

## Using Skills Effectively

**One phase per session.** Don't try to brainstorm, plan, and implement in one go. Each skill is focused.

**Read the output carefully.** It's your first draft, not gospel. Engage with it. Push back. Edit before committing.

**Follow session boundaries.** They exist for a reason: clean context, explicit decisions, honest critique.

**Read the reports before the next phase.** They're not just logs - they're context the next phase builds on and your chance to catch problems early.

**Edit the plans.** Plans include a "Questions & Decisions" table. Your job is to review it, approve, override, add context.

**Trust done-criteria.** If a phase flags something as not done, it probably is right. The criteria exist because something slipped before.

---

## Next Steps

- [Engineering Workflows](02-engineering-workflows.md) - How to use these skills together
- [Project Management](04-project-management.md) - How work is organized
