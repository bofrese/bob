# Bob Commands — Dense Reference

Each entry covers: purpose, inputs read, outputs written, process phases, and skills invoked.

---

## `/bob:pm` — Project Mentor

**Purpose:** Assess where the project is, identify gaps in artifacts and process, and recommend concrete next steps. Also optimizes context loading for new sessions.

**Reads:** `docs/product/` (all product docs), `docs/guidelines/`, `ai/plans/`, `ai/implementations/`, `ai/reviews/`, project structure, git history.

**Writes:** Conversational guidance (primary). Optionally `ai/{date}-project-status.md`.

**Process:**
1. Load context per `context-protocol`
2. Scan what product docs, plans, and reviews exist
3. Identify the most critical gap or next step
4. Recommend one concrete action
5. Answer follow-up questions about the workflow

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

**Purpose:** Structured feature brainstorm using a 6-phase process. Pushes toward simpler and more generic solutions. Validates fit against the codebase before committing.

**Reads:** `docs/product/vision.md` (optional), project codebase (Phase 5).

**Writes:** `ai/ideas/{date}-brainstorm-{slug}.md`

**Process:**
1. Seed: problem statement and constraints
2. Diverge: generate quantity without filtering (min 8 ideas)
3. Converge: cluster and score (impact × effort × fit)
4. Detail: flesh out top 1–2 ideas
5. Validate: check fit against codebase (DDD lens)
6. Commit: decision with rationale

**Skills:** `context-protocol`, `ddd` (phase 5), `domain-knowledge` (on correction), `done-criteria`

---

## `/bob:plan` — Implementation Planning

**Purpose:** Turn a feature idea into a concrete, reviewable implementation plan with BDD acceptance criteria, AI difficulty ratings, and open questions. Planning only — no implementation.

**Reads:** User-provided idea, project codebase, `ai/plans/` and `ai/implementations/` (prior work in same domain), `docs/product/vision.md`.

**Writes:** `ai/plans/{date}-{slug}.md`

**Plan structure:**
1. Problem statement
2. Current system analysis (relevant files and patterns)
3. Preparatory refactoring (if any)
4. Design and architecture (Mermaid diagram if non-trivial)
5. Implementation steps with BDD acceptance criteria and AI difficulty rating (1–5)
6. Testing strategy
7. Open questions

**Skills:** `context-protocol`, `domain-knowledge` (on correction), `ddd` (step 4), `bdd` (step 5), `done-criteria`

---

## `/bob:review-plan` — Plan Review

**Purpose:** Independent, skeptical review of an implementation plan. Verifies plan assumptions against actual code. Proposes simpler alternatives if warranted. Review only — no modifications.

**Reads:** Specified plan from `ai/plans/`, project codebase (to verify plan assumptions).

**Writes:** `ai/reviews/{date}-review-{slug}.md`

**Review dimensions:**
- Assumption verification (does the plan match what's actually in the code?)
- Architecture and design fit
- Complexity assessment
- Gap detection (missing steps, edge cases)
- Security implications
- Maintainability
- BDD acceptance criteria quality
- Simpler alternative if warranted

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:implement` — Plan Execution

**Purpose:** Execute an approved implementation plan with engineering discipline. BDD-driven per step. Stops for human judgment at hard steps (AI difficulty 4–5) or unexpected complexity. Includes ownership transfer walkthrough.

**Reads:** Specified plan from `ai/plans/`, review from `ai/reviews/`, prior implementations in same domain from `ai/implementations/`, project codebase, test suite, linter.

**Writes:** Project source files (primary), `ai/implementations/{date}-{slug}.md`, updates plan status to "Implemented".

**Process:**
1. Read plan + review; note deviations required
2. Confirm scope before starting
3. Per step: implement → verify BDD criteria → commit
4. Escalate to human at difficulty 4–5 or unexpected complexity
5. Ownership transfer walkthrough (what changed, how to test, what to watch)
6. Write implementation report

**Skills:** `context-protocol`, `bdd` (step 3), `done-criteria`

---

## `/bob:review` — Code Review

**Purpose:** Review code changes against guidelines, system health, simplicity, security, robustness, plan alignment, and done criteria. Auto-detects scope from git state. Never modifies code.

**Reads:** Git diff (staged/unstaged/commits ahead of main), changed files (read completely), associated plan from `ai/plans/`, matched guidelines from `docs/guidelines/`, `docs/process/done-criteria.md`.

**Writes:** `ai/reviews/{date}-review-{slug}.md`

**Review dimensions:**
- Critical (must fix before merge)
- Important (should fix)
- Suggestion (optional improvement)

**Checks:** System health, simplicity/DRY, security (OWASP top 10), robustness, plan alignment, done criteria compliance.

**Skills:** `context-protocol`, `done-criteria`

---

## `/bob:investigate` — Root Cause Analysis

**Purpose:** Systematic root-cause investigation using a 7-phase process. Investigation only — no fixes proposed (that's for `/bob:plan`).

**Reads:** Project codebase (relevant files, call chains, test coverage), user-provided problem description.

**Writes:** `ai/investigations/{date}-{slug}.md`

**Process:**
1. Problem statement (observable symptoms, reproduction steps)
2. Hypothesis formation (3–5 candidates, ordered by likelihood)
3. Code exploration (trace call chains, read tests)
4. 5-Whys root cause analysis
5. Impact analysis (what else is affected?)
6. Solution options (trade-offs, not recommendation)
7. Recommendation with rationale

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

**Writes:** `ai/reviews/{date}-ui-review-{slug}.md`

**13 lenses:** Visual Hierarchy, Cognitive Load, States (empty/error/loading), Typography, Gestalt, Fitts's Law, Microinteractions, Signal/Noise, Consistency, Emotional Design, Platform Fluency, Context/Stress, Brand Voice.

**Skills:** `context-protocol`, `ui-design` (invoked at start), `done-criteria`

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
