# Bob Skills — Dense Reference

Skills are thinking frameworks loaded into context when commands need them. Most are read-only reference frameworks (no file I/O). Exceptions noted.

---

## `bob:context-protocol` — Session Bootstrap

**File I/O:** Reads per-command file list (see table below). No writes.

**Invoked by:** Every bob command, as the first action.

**What it does:**
1. Get current date via `python3 -c "import datetime; print(datetime.date.today())"`
2. Load project familiarization (README, package.json/pyproject.toml, project structure)
3. Load per-command files from the loading table

**Per-command loading table (selected):**

| Command | Files loaded |
|---|---|
| `product-vision` | `docs/product/vision.md` |
| `problem-space` | `docs/product/vision.md`, `docs/product/problem-space.md` |
| `personas` | `docs/product/vision.md`, `docs/product/personas.md` |
| `business-plan` | vision + positioning + business-plan |
| `plan` | `docs/product/vision.md` |
| `review` | Changed files + associated plan + relevant guidelines |
| `implement` | Plan + review + prior implementations |
| `bob` | All product docs + plans + implementations + reviews |

**Engineering commands:** Load `docs/guidelines/` selectively after scope is clear.

---

## `bob:done-criteria` — Completion Protocol

**File I/O:**
- **Reads:** `docs/process/done-criteria.md`, `ai/issues/backlog.md`
- **Writes:** `docs/process/done-criteria.md` (bootstrap if missing), `ai/issues/backlog.md` (if user confirms)

**Invoked by:** Every output-producing bob command, as the last action.

**Four behaviors every command performs:**
1. **Bootstrap:** If `docs/process/done-criteria.md` doesn't exist, create it with the default template
2. **Check:** Verify all applicable done criteria for the artifact type are met before finishing
3. **Register:** If a new artifact type was produced, add it to `done-criteria.md`
4. **Flag:** Identify decisions or issues worth persisting to `backlog.md`

**Bootstrap template includes:** Artifact types, quality criteria per type, process requirements.

---

## `bob:bdd` — Behavior-Driven Development

**File I/O:** None (reference framework).

**Invoked by:** `plan` (step 5), `implement` (step 3 per implementation step), `review-plan`

**Core discipline:**
- Write Given/When/Then acceptance criteria **before** writing code
- Test observable behavior, not implementation details
- Every implementation step in a plan must have BDD criteria
- Before shipping: verify every criterion is covered

**Format:**
```
Given [context]
When [action]
Then [observable outcome]
```

**Red flags:** Criteria that test internal state, mock calls, or file paths rather than observable behavior.

---

## `bob:ddd` — Domain-Driven Design

**File I/O:** None (reference framework).

**Invoked by:** `brainstorm` (phase 5), `plan` (step 4)

**Core discipline:**
- Let domain drive design — not database schema, not UI structure
- Identify bounded contexts before naming anything
- Use ubiquitous language: code reads like a domain conversation
- Golden check: can a domain expert read the code without translation?

**When applied in `plan`:** Verify that proposed names and structures reflect domain language, not technical convenience.

**When applied in `brainstorm`:** Validate that the winning idea fits the domain model without requiring awkward workarounds.

---

## `bob:assumption-testing` — Risk-Based Validation

**File I/O:** None (reference framework).

**Invoked by:** `validation-plan` (phases 2–6), `product-coach`

**Covers:**
- **Assumption stack:** Problem (does it exist?), Solution (does it solve it?), Market (will they pay?), Business (can we make money?)
- **Risk matrix:** Impact × Uncertainty scoring (1–5 each); priority = highest combined score
- **Validation hierarchy:** Conversations → Smoke tests → Prototypes → Concierge MVP → Actual MVP
- **MVP scope formula:** Minimum to test the top 2–3 critical assumptions
- **Success criteria (commitment ladder):** Define pass/fail before running experiments
- **Build-Measure-Learn loop** integration

---

## `bob:business-model` — Revenue and Economics

**File I/O:** None (reference framework).

**Invoked by:** `business-plan` (phases 2/4/5/6), `product-coach`

**Covers:**
- **Value Equation:** Value created − Price = Customer surplus; Price − Cost = Margin
- **Revenue model patterns:** Subscription, transaction, freemium, usage-based, marketplace, licensing, services — with trade-offs for each
- **Unit economics:** CAC, LTV, LTV:CAC ratio (target: 3:1+), payback period (target: <12 months), gross margin benchmarks
- **Pricing strategy:** Value-based vs cost-plus vs competitive; anchoring, decoy pricing, price psychology
- **Business Model Canvas:** 9-block reference
- **Red flags:** LTV:CAC <1, payback >24 months, no clear path to positive unit economics
- **Validation checklist:** What to test before scaling spend

---

## `bob:positioning-strategy` — Market Differentiation

**File I/O:** None (reference framework).

**Invoked by:** `positioning` (phases 2/3/5/7), `product-coach`

**Covers:**
- **Five-component positioning framework:** (1) competitive alternatives, (2) unique attributes, (3) value to customer, (4) target customer, (5) market category
- **Three differentiation strategies:** Best product, best price, best relationship — pick one
- **Wedge strategy:** Enter with a narrow beachhead; expand from a position of strength
- **Messaging hierarchy:** Internal positioning statement → external one-sentence → content pillars
- **2×2 competitive matrix:** Choose axes that put you in the upper-right; avoid axes your competitors own
- **Repositioning signals:** When to change position vs. when to stay the course

---

## `bob:go-to-market` — Channel Strategy

**File I/O:** None (reference framework).

**Invoked by:** `business-plan` (phase 7), `positioning` (phase 8), `product-coach`

**Covers:**
- **Channel categories:** Owned (content, SEO, email), earned (PR, word-of-mouth, community), paid (ads, sponsorships)
- **Channel selection by customer type:** B2C vs B2B vs developer vs enterprise
- **Bullseye framework:** Brainstorm all channels → test cheaply → double down on what works → ignore the rest
- **CAC economics:** How channel cost affects unit economics viability
- **Growth loops:** Viral, content, paid, sales — design them before spending money
- **Launch strategy options:** Product Hunt, community launch, direct outreach, waitlist, press
- **Distribution moats:** What makes your channel hard to copy (network effects, content moat, relationships)

---

## `bob:problem-validation` — Problem-Space Discipline

**File I/O:** None (reference framework).

**Invoked by:** `problem-space` (phases 2–8), `product-coach`

**Covers:**
- **Problem vs solution separation:** Stay in problem space; prohibit solution framing until validation is complete
- **Jobs-to-be-Done:** Functional (what they're trying to accomplish), emotional (how they want to feel), social (how they want to be perceived)
- **Problem severity matrix:** Frequency × Intensity → Urgent (high/high), Latent (low/high), Frequent (high/low), Background noise (low/low)
- **Current alternatives taxonomy:** Direct competitors, indirect alternatives, DIY, doing nothing
- **Evidence hierarchy:** Paying customers > active workarounds > complaints > agreement > "sounds nice" — only the first two matter
- **Mom Test questions:** Ask about their life (not your idea); get specifics, not hypotheticals
- **Kill criteria:** Conditions under which to stop and pivot the problem framing

---

## `bob:ui-design` — 13-Lens Evaluation

**File I/O:** None (reference framework).

**Invoked by:** `ui-review` (at start), `art-director`, `design-brief` (via context-protocol)

**The 13 lenses (each includes red flags):**

1. **Visual Hierarchy** — Does the eye know where to go? F-pattern, Z-pattern, size/weight/color to guide attention
2. **Cognitive Load** — Hick's Law (fewer options → faster decisions), Miller's Law (7±2 chunks), progressive disclosure
3. **States** — Empty state, loading state, error state, success state — all must be designed
4. **Typography as Architecture** — Scale, weight, spacing, line length (45–75 chars), leading as structure
5. **Gestalt Principles** — Proximity, similarity, closure, continuity — do groupings communicate relationships?
6. **Fitts's Law** — Target size and distance; critical actions must be large and close; destructive actions must be distant
7. **Microinteractions** — Feedback on every action; transitions that communicate cause → effect
8. **Signal/Noise** — Every element must earn its place; decorative elements are noise
9. **Consistency** — Identical elements for identical actions; predictability as trust
10. **Emotional Design (Norman's 3 levels)** — Visceral (first impression), behavioral (ease of use), reflective (meaning)
11. **Platform Fluency** — Does it feel native? Uses platform conventions unless there's a strong reason not to
12. **Context Design** — Stress conditions (tired, distracted, time pressure, one hand); accessibility
13. **Brand Voice in Interface** — Microcopy, labels, error messages — do they sound like the product?

---

## `bob:prompt-engineering` — Command Writing Principles

**File I/O:** None (reference framework).

**Invoked by:** `new-command`, `review-command`, `improve-command` (via context-protocol)

**Principles:**
- **Be explicit:** State exactly what to do, not what to think
- **Structure clearly:** Context → Role → Process → Output (every command)
- **Minimize tokens:** Every word should earn its place; target 30–50% below naive draft
- **Load just-in-time:** Don't front-load all context; load files when the step needs them
- **One question at a time:** Never ask more than one clarifying question per turn
- **Avoid aggressive language:** "never", "always", "must" — use sparingly; they inflate and get ignored
- **Standalone outputs:** A new session should be able to read the output without conversation context

**Anti-patterns:** Padding with philosophy, restating the obvious, front-loaded disclaimers, vague output instructions ("produce a comprehensive analysis").

**Command structure template:**
```
---
description: [one line, what and when]
---
# [Command Name]

## Context
[What to load and when]

## Role
[Who you are in 1 sentence]

## Process
[Numbered phases with clear actions]

## Output
[Exact file, format, and required sections]
```

---

## `bob:domain-knowledge` — Project-Specific Terminology

**File I/O:**
- **Reads:** `docs/domain/README.md`, `docs/domain/{slug}.md` (if exists)
- **Writes:** `docs/domain/{slug}.md` (new or updated), `docs/domain/README.md` (index)

**Invoked by:** `brainstorm`, `plan` — when the user corrects a domain misunderstanding

**Purpose:** Capture project-specific nuance that an informed developer wouldn't assume. One concept per invocation.

**What qualifies:**
- Terms that mean something different in this project than in general usage
- Non-obvious distinctions between similar concepts
- Corrections from the user about how something actually works

**What doesn't qualify:**
- General language/framework patterns (those go in guidelines)
- Architecture decisions (those go in docs)
- Tooling preferences (those go in guidelines)

**Always verify with user before saving.**
