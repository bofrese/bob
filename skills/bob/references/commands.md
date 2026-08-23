# Bob Commands — Dense Reference

Each entry covers: purpose, inputs read, outputs written, process phases, and skills invoked.

---

## `/bob:setup` — Infrastructure Bootstrap

**Purpose:** Bootstrap and upgrade bob's working infrastructure on any project. Idempotent — safe to run on new projects, existing projects, and after bob version upgrades. Creates what's missing, patches done-criteria with new sections, never removes or overwrites existing content.

**Reads:** `.gitignore`, `docs/process/done-criteria.md`, `bob/commands/knowledge.md` (if knowledge vault missing), `bob/skills/done-criteria/SKILL.md` (for template comparison), `package.json` / git remote (to derive subproject name); graphify presence/version, `graphify-out/graph.json`, `graphify hook status`, `website/src/` (b2 signal).

**Writes:** `projects/{name}/stories/` + `_kanban.md` (if missing); full knowledge vault structure (if missing); `personal/daily/`, `personal/weekly/`, `personal/scratchpad.md` (if missing); `.gitignore` entries; `docs/process/done-criteria.md` (create or patch); `.graphifyignore` (managed corpus-scope block, when graphify installed).

**Process:**
1. Audit — check all infrastructure silently; scan for orphan markdown files
2. Report — present status table; confirm before touching anything
3. Bootstrap — create only what's missing (projects/, knowledge/, personal/, gitignore entries)
4. Upgrade done-criteria — detect missing sections by comparing project file against current bootstrap template; append only absent sections; update date
5. Orphan report — list markdown files outside managed locations; suggest migration path via `knowledge/_INBOX/`
6. Summary — compact table of what was created, patched, or already present

Bootstrap (step 3) also handles **graphify provisioning** when graphify is installed: recommends install/upgrade to `>= 0.9.11` if absent or old (`uv tool install graphifyy`, double-y, never silent-installed), offers to build the graph (`/graphify .`) and install the post-commit hook (`graphify hook install`) with a first-build cost warning, and writes/refreshes the plugin-aware `.graphifyignore` corpus scope. Scope tiers: Code + authoritative content (`docs/`, `knowledge/`, `website/src/`) kept; Historical (`projects/`, `ai/`) excluded (~74% of observed semantic cost). `website/dist/` excluded only when the b2 `website/src/` structure is present.

**Rules:** Never overwrites existing files (the `.graphifyignore` managed block is the one regenerated-in-place exception). Never removes or reorders done-criteria sections. Never silent-installs third-party tools. One confirmation for all changes.

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:pm` — Project Mentor

**Purpose:** Assess where the project is, identify gaps in artifacts and process, and recommend concrete next steps. Also optimizes context loading for new sessions.

**Reads:** `docs/product/` (all product docs), `docs/guidelines/`, `projects/` (story folders and kanbans), project structure, git history.

**Writes:** Conversational guidance (primary). Optionally `ai/{date}-project-status.md`.

**Process (Mode 1 — Workflow Guidance, default):**
1. Load context per `context-protocol`
2. Read `projects/_index.md` to identify all sub-projects
3. For each sub-project: read `projects/{sub}/_kanban.md`; for each story in `In Progress` or `Ready`: read `projects/{sub}/stories/{id}/_kanban.md`
4. Synthesise: what's in-flight, what's ready to start, what's blocked, INBOX count
5. Present one concrete recommendation; offer to save summary to `personal/daily/`
6. Answer follow-up questions about priorities, story details, or next steps

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:product-vision` — Vision Foundation

**Purpose:** Establish or refine the single strategic foundation: what the product is, who it's for, what changes for them, what it is not, and how you know you're on track. Challenges vague or aspirational language throughout.

**Reads:** `docs/product/vision.md` (if exists, for Refine mode).

**Writes:** `docs/product/vision.md` (living document, updated in place).

**Process:**
1. Create/Refine mode detection
2. Problem & solution framing
3. Target user (specific, not demographic)
4. Value proposition (concrete before/after)
5. Anti-scope (what it is not)
6. Success signals (observable evidence)
7. Reality-check against codebase if it exists

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:problem-space` — Problem Validation

**Purpose:** Validate the problem before building anything. Stays strictly in problem space — prohibits solution proposals during exploration.

**Reads:** `docs/product/vision.md`, `docs/product/problem-space.md` (if exists).

**Writes:** `docs/product/problem-space.md` (living document).

**Process:**
1. Problem statement (symptom vs root cause)
2. Jobs-to-be-Done (functional, emotional, social)
3. Severity scoring (frequency × intensity matrix)
4. Current alternatives (what people do today)
5. Validation evidence (evidence hierarchy: paying > workaround > complaint > agreement)
6. Mom Test question generation
7. Kill-or-proceed decision with explicit criteria

**Skills:** `context-protocol`, `problem-validation`, `done-criteria`

---

## `/bob:personas` — User Archetypes

**Purpose:** Define minimum necessary personas with genuinely different design implications. Challenges vague archetypes; pushes for specificity. Includes "Who This Is NOT For."

**Reads:** `docs/product/vision.md`, `docs/product/personas.md` (if exists).

**Writes:** `docs/product/personas.md` (living document).

**Process:**
1. Identify candidate personas from vision
2. Challenge: do they have different needs that affect design decisions?
3. Collapse where overlap is superficial
4. Per persona: name, context, JTBD, frustrations, success criteria, anti-patterns
5. Explicit "Not For" section

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:business-plan` — Business Model

**Purpose:** Build a complete, challenged business model with revenue mechanics, unit economics, GTM strategy, and a validation plan.

**Reads:** `docs/product/vision.md`, `docs/product/positioning.md`, `docs/product/business-plan.md` (if exists).

**Writes:** `docs/product/business-plan.md` (living document).

**Process:**
1. Value proposition (what pain, for whom, why now)
2. Revenue model selection with trade-offs
3. Pricing strategy and psychology
4. Unit economics (CAC, LTV, LTV:CAC, payback period)
5. Cost structure
6. GTM strategy (channels, sequence)
7. Validation plan (cheapest test of each assumption)

**Skills:** `context-protocol`, `business-model` (phases 2/4/5/6), `go-to-market` (phase 7), `done-criteria`

---

## `/bob:positioning` — Market Positioning

**Purpose:** Define market category, differentiation, and messaging. Uses the five-component positioning framework. Optionally produces a competitive 2×2 matrix.

**Reads:** `docs/product/vision.md`, `docs/product/problem-space.md`, `docs/product/business-plan.md`, `docs/product/positioning.md` (if exists).

**Writes:** `docs/product/positioning.md` (living document).

**Process:**
1. Competitive alternatives (what customers actually do today)
2. Unique attributes (capabilities, not marketing)
3. Value translation (attribute → customer outcome)
4. Target customer definition
5. Market category decision
6. Internal positioning statement
7. External one-sentence version
8. GTM channel implications
9. Content pillar derivation
10. Optional: 2×2 competitive matrix

**Skills:** `context-protocol`, `positioning-strategy` (phases 2/3/5/7), `go-to-market` (phase 8), `done-criteria`

---

## `/bob:validation-plan` — Assumption Testing

**Purpose:** Build a prioritized assumption stack, rank by impact × uncertainty, design cheap experiments (cheapest first), define success criteria before running anything, scope the MVP, sequence the validation plan.

**Reads:** `docs/product/vision.md`, `docs/product/problem-space.md`, `docs/product/business-plan.md`, `docs/product/positioning.md`, `docs/product/validation-plan.md` (if exists).

**Writes:** `docs/product/validation-plan.md` (living document).

**Process:**
1. List all assumptions (problem, solution, market, business model)
2. Risk matrix: Impact × Uncertainty scoring
3. Prioritize top 3–5 critical assumptions
4. Design validation experiments (cheapest first)
5. Define success/fail criteria before running
6. MVP scope: minimum to test critical assumptions
7. Sequenced validation roadmap with kill criteria

**Skills:** `context-protocol`, `assumption-testing` (phases 2–6), `done-criteria`

---

## `/bob:design-brief` — Design Direction

**Purpose:** Translate product intent into design direction: principles, constraints, tone, voice. Explicitly not a UI spec — the frame within which design decisions are made.

**Reads:** `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md` (if exists).

**Writes:** `docs/product/design-brief.md` (living document).

**Requires:** Vision and personas must exist. Flags their absence and stops.

**Process:**
1. Validate prerequisites (vision + personas)
2. Core design principles (3–5, not generic)
3. Constraints (technical, platform, accessibility, time)
4. Tone and voice (with do/don't examples)
5. What success looks/feels like
6. What this design is NOT

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:product-coach` — Discovery Orchestrator

**Purpose:** Manages the entire product discovery process. Maintains a status README. Operates in four modes: Comprehensive Discovery (full sequence), Targeted Session (specific gap), Gap Analysis (what's missing/stale), Maintenance (keep existing docs current).

**Reads:** `docs/product/vision.md`, `docs/product/README.md`, all other product docs as relevant.

**Writes:** `docs/product/README.md` (always), plus any of: `vision.md`, `problem-space.md`, `personas.md`, `business-plan.md`, `positioning.md`, `validation-plan.md`, `design-brief.md`.

**Process:**
1. Load all existing product docs
2. Build status map (exists / stale / missing)
3. Identify highest-priority gap
4. Work through that gap with the relevant skill
5. Update README status

**Skills:** `context-protocol`, `problem-validation`, `business-model`, `positioning-strategy`, `go-to-market`, `assumption-testing`, `done-criteria`

---

## `/bob:brainstorm` — Feature Ideation

**Purpose:** Structured feature brainstorm using a 5-phase process. Challenges the idea for value and explores outcome-level alternatives — does not decide architecture. Routes to `/bob:design` for conceptually meaningful work.

**Reads:** `docs/product/vision.md` (optional).

**Writes:** `{story_path}/{date}-brainstorm-{slug}.md` (a Brainstorm Brief)

**Process:**
1. Seed: problem statement and constraints
2. Diverge: generate quantity without filtering (min 8 ideas)
3. Converge: cluster and score (impact × effort × fit)
4. Detail: flesh out top 1–2 ideas (concept level only)
5. Commit: accepted capability statement, open questions; route to `/bob:design` or `/bob:plan`
6. **PM step:** Route any rejected alternatives or deferred ideas worth pursuing separately — invoke `bob:work-routing`

**Skills:** `context-protocol`, `domain-knowledge` (on correction), `work-routing` (step 6), `done-criteria`

---

## `/bob:design` — Conceptual Design

**Purpose:** Socratic, evidence-based session to form the simplest coherent conceptual design for a capability — concepts, boundaries, vocabulary, trade-offs — before any implementation planning starts. The human owns every material decision; the command investigates, challenges, and exposes pressure points rather than handing over a finished architecture.

**Reads:** Brainstorm Brief or accepted requirement, repository evidence (code graph query when fresh, else manual exploration), relevant domain knowledge.

**Writes:** `{story_path}/{date}-design-{slug}.md` (a Design Record) — the authoritative intent consumed by Plan, Review Plan, Implement, Review, and Reflect.

**Process:**
1. Start with evidence: load requirement, survey the repository (graph-first) before asking broad questions
2. Socratic design conversation: one question/batch at a time, evidence-consistent brevity accepted, alternatives proposed only after the human has engaged
3. Required challenges: existing concept reuse, new concepts, complexity removed/introduced/moved, reading path, future pressure, remaining awkwardness
4. **PM step:** Route out-of-scope findings — invoke `bob:work-routing`
5. Exit and record: may conclude "return to Brainstorm," "investigate first," "do not build," or a completed Design Record

**Skills:** `context-protocol`, `design` (interaction policy, lenses, artifact template), `code-graph` (phase 1 evidence), `domain-knowledge` (on correction), `work-routing` (step 4), `done-criteria`

---

## `/bob:plan` — Implementation Planning

**Purpose:** Turn a feature idea into a concrete, reviewable implementation plan with BDD acceptance criteria, AI difficulty ratings, and open questions. Planning only — no implementation.

**Reads:** User-provided idea, project codebase, `{story_path}/*-plan-*` and `{story_path}/*-implement-*` (prior work in same story), `docs/product/vision.md`.

**Writes:** `{story_path}/{date}-plan-{slug}.md`

**Plan structure:**
1. Problem statement
2. Current system analysis (blast-radius via the code graph first when fresh - `graphify affected`; else manual exploration; relevant files and patterns)
3. Preparatory refactoring (if any)
4. Design and architecture (Mermaid diagram if non-trivial)
5. Implementation steps with BDD acceptance criteria and AI difficulty rating (1–5)
5.5. **PM step:** Route out-of-scope work that surfaced during planning — invoke `bob:work-routing`
6. Testing strategy
7. Open questions

**Skills:** `context-protocol`, `code-graph` (step 2 blast-radius), `domain-knowledge` (on correction), `ddd` (step 4), `bdd` (step 5), `work-routing` (step 5.5), `done-criteria`

---

## `/bob:review-plan` — Plan Review

**Purpose:** Independent, skeptical review of an implementation plan. Verifies plan assumptions against actual code. Proposes simpler alternatives if warranted. Review only — no modifications.

**Reads:** Specified plan from story folder, project codebase (to verify plan assumptions).

**Writes:** `{story_path}/{date}-review-plan-{slug}.md`

**Review dimensions:**
- Assumption verification (does the plan match what's actually in the code?)
- Architecture and design fit
- Complexity assessment
- Gap detection (missing steps, edge cases)
- Security implications
- Maintainability
- BDD acceptance criteria quality
- Simpler alternative if warranted

**PM step:** Route findings clearly out of scope for this story — invoke `bob:work-routing`. Do not route ordinary plan gaps (those go in the report).

**Skills:** `context-protocol`, `work-routing` (PM step), `done-criteria`

---

## `/bob:implement` — Plan Execution

**Purpose:** Execute an approved implementation plan with engineering discipline. BDD-driven per step. Stops for human judgment at hard steps (AI difficulty 4–5) or unexpected complexity. Includes ownership transfer walkthrough.

**Reads:** Specified plan from `{story_path}/`, review from `{story_path}/`, prior `*-implement-*` files from `{story_path}/`, project codebase, test suite, linter.

**Writes:** Project source files (primary), `{story_path}/{date}-implement-{slug}.md`, updates plan status to "Implemented", updates `{story_path}/_kanban.md`.

**Process:**
1. Read plan + review; note deviations required
2. Confirm scope before starting
3. Per step: implement → verify BDD criteria → commit
4. Escalate to human at difficulty 4–5 or unexpected complexity
5. Kanban update: mark resolved issues/tasks done
6. **PM step (step 6.5):** For new issues or work discovered during implementation — invoke `bob:work-routing`
7. Ownership transfer walkthrough (what changed, how to test, what to watch)
8. Write implementation report

**Skills:** `context-protocol`, `bdd` (step 3), `work-routing` (step 6.5), `done-criteria`

---

## `/bob:review` — Code Review

**Purpose:** Review code changes against guidelines, system health, simplicity, security, robustness, plan alignment, and done criteria. Auto-detects scope from git state. Never modifies code.

**Reads:** Git diff (staged/unstaged/commits ahead of main), changed files (read completely), associated plan from `{story_path}/`, matched guidelines from `docs/guidelines/`, `docs/process/done-criteria.md`.

**Writes:** `{story_path}/{date}-review-{slug}.md`

**Review dimensions:**
- Critical (must fix before merge)
- Important (should fix)
- Suggestion (optional improvement)

**Checks:** System health, simplicity/DRY, security (OWASP top 10), robustness, plan alignment, done criteria compliance.

**System health via the code graph** (when fresh): cross-check changed files against the `GRAPH_REPORT.md` community-hub list for god-node coupling, and derive diff impact from **local git only** (`git diff` changed symbols -> `graphify affected`). No GitHub / `gh` dependency - `graphify prs` is deliberately unused.

**PM step:** Before discussing findings, invoke `bob:work-routing` for any discovered issues/debt that are clearly out of scope for this story. In-scope findings go in the report.

**Skills:** `context-protocol`, `code-graph` (system-health hubs + diff impact), `work-routing` (PM step), `done-criteria`

---

## `/bob:investigate` — Root Cause Analysis

**Purpose:** Systematic root-cause investigation using a 7-phase process. Investigation only — no fixes proposed (that's for `/bob:plan`).

**Reads:** Project codebase (relevant files, call chains, test coverage), user-provided problem description.

**Writes:** `{story_path}/{date}-investigate-{slug}.md`

**Process:**
1. Problem statement (observable symptoms, reproduction steps)
2. Hypothesis formation (3–5 candidates, ordered by likelihood)
3. Code exploration (query the code graph first when fresh - `path`/`explain`/`affected`; else trace call chains, read tests)
4. 5-Whys root cause analysis
5. Impact analysis (what else is affected?)
6. Solution options (trade-offs, not recommendation)
7. Recommendation with rationale

**PM step:** If the investigation uncovered related issues in adjacent code or other stories, invoke `bob:work-routing` to file them.

**Skills:** `context-protocol`, `code-graph` (graph-first exploration), `work-routing` (PM step), `done-criteria`

---

## `/bob:dev` — Working Session

**Purpose:** Quick working session for code discussion, fixes, and direct changes. Skips the brainstorm/plan/review pipeline. For ad-hoc work where the scope is clear and small.

**Reads:** Project files as needed.

**Writes:** Project files in place (direct code edits).

**Process:**
Unstructured — driven by the user. Claude acts as a peer developer: reads code, discusses, makes changes, pushes back on quality issues. Flags scope creep. Suggests switching to a formal bob command if the task grows too large.

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:document` — Developer Documentation

**Purpose:** Generate or update developer documentation at L2 (system map) or L3 (subsystem) zoom. Has drift detection mode that compares existing docs against current codebase.

**Reads:** Project codebase (source files, existing docs), `docs/README.md`, `git log` (drift detection).

**Writes:** `docs/{concept}.md` (new or updated), `docs/README.md` (index update).

**Modes:**
- **Generate:** New documentation for a concept or subsystem
- **Update:** Bring an existing doc current
- **Drift:** Scan existing docs and flag stale/missing/accurate claims

**Zoom levels:**
- L2: System map (components, relationships, boundaries)
- L3: Subsystem deep-dive (flows, APIs, data shapes)

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:user-guide` — End-User Guide

**Purpose:** Create or maintain an end-user guide for the project. Reads the codebase to verify what actually exists before documenting it. Surfaces UX gaps, missing features, and friction points as a separate findings report.

**Reads:** `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md`, project codebase (source files, UI, routes, CLI), existing guide (if updating), `git log` (maintenance mode), CLAUDE.md (for configured guide path).

**Writes:** `docs/user-guide.md` (or CLAUDE.md-configured path), `{story_path}/{date}-user-guide-findings-{slug}.md` (findings report), CLAUDE.md root entry (user-guide path + maintenance reminder, first run only).

**Modes:**
- **New:** No guide exists — full discovery and write process
- **Maintenance:** Guide exists — drift detection against codebase, then update

**Key constraint:** Never documents a feature that cannot be verified in the codebase. Gaps go into findings, not the guide.

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:guidelines` — Best Practice Guides

**Purpose:** Create and maintain technology-specific best practice guidelines. Research-first (official style guides, tools, OWASP, etc.) before touching the codebase.

**Reads:** Project codebase (technology scan), `docs/guidelines/README.md` (if exists), authoritative external sources (WebSearch/WebFetch).

**Writes:** `docs/guidelines/{topic}.md`, `docs/guidelines/README.md` (index).

**Structure per guideline:**
- Principles (why, not just what)
- Patterns (with examples)
- Anti-patterns (with examples)
- Tooling with configs
- Quick-reference table

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:docker-setup` — Docker Environment

**Purpose:** Set up or maintain a Docker-based development environment with a standard `make` interface. Verifies the environment actually works after setup.

**Reads:** Project codebase (build system, dependencies, existing Docker files, README, config, ports).

**Writes:** `Dockerfile`, `docker-compose.yml` (if needed), `.dockerignore`, `Makefile`, `INSTALL.md` (all modified in-place); `ai/docker/{date}-docker-setup.md` (setup log).

**Standard Makefile targets:** `make setup`, `make run`, `make test`, `make build`, `make clean`

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:ui-review` — UI/UX Expert Review

**Purpose:** Expert UI/UX review using the 13-lens framework from `ui-design` skill. Can optionally implement fixes after review with explicit user confirmation.

**Reads:** Screenshot and/or UI source files (user-provided), `docs/product/vision.md`, `docs/product/personas.md`, `docs/product/design-brief.md`.

**Writes:** `{story_path}/{date}-ui-review-{slug}.md`

**13 lenses:** Visual Hierarchy, Cognitive Load, States (empty/error/loading), Typography, Gestalt, Fitts's Law, Microinteractions, Signal/Noise, Consistency, Emotional Design, Platform Fluency, Context/Stress, Brand Voice.

**PM step:** For findings out of scope for this story (shared component issues, design system inconsistencies affecting other areas): invoke `bob:work-routing`. In-scope findings stay in the action plan.

**Skills:** `context-protocol`, `ui-design` (invoked at start), `work-routing` (PM step), `done-criteria`

---

## `/bob:art-director` — Visual Direction

**Purpose:** Art direction coaching for UI, brand, and marketing materials. Conversational by default — documents only on explicit request.

**Reads:** `docs/product/vision.md` (optional), screenshots/mockups (user-provided).

**Writes:** `docs/guidelines/visual-design.md` (optional, only if documenting).

**Covers:** Brand tone, direction proposals, color systems, typography, component patterns, visual language.

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:new-command` — Create Bob Command

**Purpose:** Guided creation of a new bob slash command. Works through need, design, and structure conversationally. Enforces structural consistency with existing commands.

**Reads:** `bob/CLAUDE.md` (command dev guidelines), `bob/README.md` (inventory), 1–2 similar existing commands for reference.

**Writes:** `bob/commands/{command-name}.md` (new command), updated `bob/README.md`.

**Process:**
1. What need does this command address?
2. What existing commands overlap? (prevent duplication)
3. Design: process phases, inputs, outputs
4. Write command file following structural template
5. Update README command table

**Skills:** `context-protocol`, `prompt-engineering` (via context-protocol)

---

## `/bob:improve-command` — Command Improvement

**Purpose:** Extract reusable learnings from a completed session to improve a specific bob command. Keeps all improvements generic (project-agnostic).

**Reads:** Current session conversation, `bob/commands/{name}.md`.

**Writes:** `ai/reviews/{date}-improve-{command-name}.md`

**Extracts:**
- Questions the command should have asked but didn't
- Output gaps (what was missing from the result)
- Process improvements (wrong order, missing phases)
- Edge cases not handled

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:review-command` — Command Quality Review

**Purpose:** Prompt engineering quality review of a bob command. Targets 30–50% token reduction. Produces an optimized version.

**Reads:** Specified command file from `bob/commands/`.

**Writes:** `ai/reviews/{date}-command-review-{slug}.md`

**Checks:**
- Token efficiency (signal-to-noise)
- Structural clarity (Context/Role/Process/Output)
- Required protocol lines (context-protocol + done-criteria)
- Completeness
- Contradictions
- Output instruction conciseness

**Skills:** `context-protocol`, `prompt-engineering` (via context-protocol), `done-criteria`

---

## `/bob:library` — Knowledge Vault Librarian

**Purpose:** Thin dispatcher over the `bob:vault` skill. Manages the project knowledge vault (`knowledge/`). Bootstraps the vault on first run. Five modes: status (no args), process (inbox to atomic notes), ingest (external source to notes), retrieve (search), organise (vault health).

**Reads:** `knowledge/README.md`, `knowledge/_suggestions.md`, `knowledge/_INBOX/` (process mode), subfolder `_index.md` files, individual notes (retrieve/organise), external URL or local file (ingest mode).

**Writes:** `knowledge/` notes, indexes, MOCs (process/organise/ingest modes); `knowledge/_suggestions.md` (process/organise/ingest); `knowledge/log.md` (process/organise/ingest — appended via `log_append.py`); `sources/` raw materials (process/ingest).

**Bootstrap:** Runs automatically if `knowledge/` doesn't exist. Delegates to `bob:vault` bootstrap mode: creates folder structure, `_schema.md`, `README.md`, subfolder indexes, `_suggestions.md`, gitignore entries, and `personal/` structure.

**Modes:**
- **Status:** Count inbox items, notes per subfolder, MOCs, pending suggestions. Show last README modified date.
- **Process:** Run reconcile on each `_INBOX/` item before writing. Subagent batching for large inboxes (≥20K tokens). Appends to `knowledge/log.md` on completion.
- **Ingest:** Fetch URL or read local file, extract atomic concepts, run reconcile on each, save raw source to `sources/`. Appends to `knowledge/log.md`.
- **Retrieve:** Search vault via Obsidian search (if running) or `grep -rl`. Present excerpts. Offer to open in full.
- **Organise:** Incremental (scoped to changed files via `git_scope.py`). Runs `lint.py` on changed files, surfaces field renames as batch proposals, runs integrity audit, active maintenance. Appends to `knowledge/log.md`.

**Python scripts** (`bob/skills/vault/scripts/`): `lint.py` (frontmatter audit, broken links), `git_scope.py` (changed files since last organise), `log_append.py` (append to `knowledge/log.md`), `orphan.py` (notes with no inbound links).

**Rules:** Never deletes files (moves only); uses `obsidian move` if vault active, falls back to `mv`; never writes to indexes without user confirmation (process mode); reconcile runs before every note write.

**Skills:** `context-protocol`, `bob:vault`, `done-criteria`

---

## `/bob:remember` — Quick Knowledge Capture

**Purpose:** Instant capture to `knowledge/_INBOX/`. No context loading, no phases — must be immediate. Takes content from args or asks once.

**Reads:** Nothing (invokes `bob:vault` bootstrap skill if vault missing).

**Writes:** `knowledge/_INBOX/YYYY-MM-DD-<slug>.md`

**Process:**
1. Use args as content, or ask "What should I remember?" (single question only)
2. If vault missing: bootstrap it (reads bootstrap procedure from `bob/commands/library.md`), then continue
3. Derive slug from content (first 4-5 significant words, kebab-case, skip stop words)
4. Write inbox file with `title:`, `type: inbox`, `timestamp:` frontmatter
5. Confirm with filename and reminder to run `/bob:library process`

**Rules:** No done-criteria. No context-protocol. No modification of existing notes or indexes.

**Skills:** None

---

## `/bob:linkedin` — LinkedIn Strategy Advisor

**Purpose:** LinkedIn growth strategy advisor for consultants, founders, and B2B service businesses. Grounds strategy in the product's actual positioning and personas — not generic tips. Operates as a persistent expert mode: opens with a mode signal and reminds users to return with `/bob:linkedin`.

**Reads:** `docs/product/positioning.md`, `docs/product/personas.md`, `docs/product/vision.md` (all optional; falls back to generic guidance if missing).

**Writes:** `docs/product/linkedin-strategy.md` (optional, only if substantive strategy emerged and user agrees).

**Process:**
1. Load context (invoke `bob:linkedin-expert` skill; read available product docs)
2. Establish starting point (from scratch / early stage / optimising / specific problem)
3. Ground strategy in product context: derive content pillars from positioning, map personas to targeting tiers
4. Land concrete plan: 3 pillars, weekly cadence, first 4 posts, 5–10 comment targets, profile quick wins
5. Offer to save strategy doc; remind user to return with `/bob:linkedin`

**Skills:** `context-protocol`, `linkedin-expert` (phase 1), `done-criteria`
