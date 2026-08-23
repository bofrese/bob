# Bob Skills — Dense Reference

Skills are thinking frameworks loaded into context when commands need them. Most are read-only reference frameworks (no file I/O). Exceptions noted.

---

## `bob:context-protocol` — Session Bootstrap

**File I/O:** Reads per-command file list (see table below). No writes.

**Invoked by:** Every bob command, as the first action.

**What it does:**
1. Get current date via `python3 -c "import datetime; print(datetime.date.today())"`
2. Load project familiarization (README, package.json/pyproject.toml, project structure); if `graphify-out/GRAPH_REPORT.md` exists, read only its `## Community Hubs (Navigation)` section for a cheap project map instead of blind exploration
3. Load per-command files from the loading table
4. For engineering commands: invoke `bob:story-context` to resolve the active story
5. **Kanban Sync** (engineering commands, after story context): read `{story_path}/_kanban.md`, semantically match a task card to the current session, and move it to `## in progress` if confident. Ask user if multiple candidates. Skip silently if no match or no kanban.
6. For engineering commands: load `docs/guidelines/` selectively once scope is clear
7. For engineering commands: invoke `bob:knowledge` for relevant vault retrieval
8. For engineering commands: invoke `bob:code-graph` for graph freshness + query capability (skips silently if graphify/graph absent)

**Per-command loading table (selected):**

| Command | Files loaded |
|---|---|
| `product-vision` | `docs/product/vision.md` |
| `problem-space` | `docs/product/vision.md`, `docs/product/problem-space.md` |
| `personas` | `docs/product/vision.md`, `docs/product/personas.md` |
| `business-plan` | vision + positioning + business-plan |
| `plan` | `docs/product/vision.md` |
| `review` | Changed files + associated plan + relevant guidelines |
| `implement` | Plan + review + prior implements (all from story folder) |
| `bob` | All product docs + project structure |

**Engineering commands:** Load `docs/guidelines/` selectively after scope is clear.

---

## `bob:story-context` — Active Story Resolution

**File I/O:**
- **Reads:** `projects/*/stories/*/` (via scripts); Obsidian workspace state (tiers 3-4)
- **Writes:** None (sets `story_path` in working memory only)

**Invoked by:** Every engineering command (via context-protocol), after file loading.

**Resolution chain (4 tiers + fallback):**
1. **Tier 1 — Path-derived (certain):** File arg contains `projects/[sub]/stories/[ID]/` → extract via `detect-story-from-path.sh`
2. **Tier 2 — Explicit mention (certain):** Args/conversation contain `[A-Z]+-[0-9]+` pattern → resolve path and verify directory exists
3. **Tier 3 — Obsidian open tabs (probable):** Query open markdown tabs via `obsidian eval`; filter for story paths; ask if one match, list if multiple
4. **Tier 4 — Obsidian recents (uncertain):** Query recents via `obsidian recents`; take most recent story path; ask for confirmation
5. **Fallback:** Stop and ask user; offer to create new story or bootstrap `projects/` via project-tracking skill

**Output contract:** Prints a `**Story Context**` block with Path, Story ID, Subproject (and optionally Task ID). Downstream commands use `story_path` from the Path line for all artifact placement.

**Scripts:** `detect-story-from-path.sh`, `get-open-obsidian-files.sh`, `get-recent-obsidian-files.sh`, `filter-story-paths.sh` — located in `skills/story-context/scripts/`.

---

## `bob:done-criteria` — Completion Protocol

**File I/O:**
- **Reads:** `docs/process/done-criteria.md`
- **Writes:** `docs/process/done-criteria.md` (bootstrap if missing), `{story_path}/_kanban.md` (issues, if user confirms), `projects/{subproject}/_kanban.md` INBOX (general issues), `{story_path}/_index.md` (history row)

**Invoked by:** Every output-producing bob command, as the last action.

**Seven behaviors every command performs:**
1. **Bootstrap:** If `docs/process/done-criteria.md` doesn't exist, create it with the default template
2. **Check:** Verify all applicable done criteria for the artifact type are met before finishing
3. **Register:** If a new artifact type was produced, add it to `done-criteria.md`
4. **Flag:** Identify terminology, architectural decisions, or patterns worth persisting; write knowledge candidates to `knowledge/_INBOX/`
5. **Update daily note:** Append session summary to `personal/daily/YYYY-MM-DD.md` if directory exists; skip silently if not
6. **Track issues:** For each discovered issue/debt/improvement: invoke `bob:work-routing` to compile routing destinations, then ask user once whether to file. Skip if a mid-session PM step already ran and routed all items.
7. **Update history:** Add one row to `{story_path}/_index.md` history table for the artifact just produced

**Bootstrap template includes:** Artifact types, quality criteria per type, process requirements (no `ai/` references).

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

**Invoked by:** `plan` (step 4)

**Core discipline:**
- Let domain drive design — not database schema, not UI structure
- Identify bounded contexts before naming anything
- Use ubiquitous language: code reads like a domain conversation
- Golden check: can a domain expert read the code without translation?

**When applied in `plan`:** Verify that proposed names and structures reflect domain language, not technical convenience.

---

## `bob:design` — Conceptual Design Framework

**File I/O:** None (reference framework — the `/bob:design` command owns artifact I/O).

**Invoked by:** `/bob:design`

**Core discipline:** Socratic, evidence-based conceptual design for an experienced developer. The human is the architect; the skill's job is to investigate, expose pressure points, and make weak reasoning visible — not to hand over a finished architecture.

- `references/interaction-policy.md` — pacing and when brevity is sufficient vs. when to push back (the six conditions that make a short answer insufficient)
- `references/design-lenses.md` — whole-system comprehensibility lenses (SOLID/DRY/DDD etc. as diagnostics, never a scorecard) and the semantic-vs-syntactic generalization policy
- `references/artifact-template.md` — the Design Record field list and filename convention

**Human decision boundary:** Never silently decide domain meaning, boundaries, semantic contracts, generalization, irreversible migrations, or major trade-offs — record human decisions and AI assumptions separately.

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

## `bob:linkedin-expert` — LinkedIn Marketing

**File I/O:** None (reference framework).

**Invoked by:** `linkedin` command (hidden knowledge base — not user-facing).

**Covers:**
- **Core mental model:** Trust accumulation engine; algorithm mechanics; personal brand vs company page
- **Content formats:** Short/long posts, carousels, LinkedIn Articles, video, polls — with purpose, frequency, and mechanics for each
- **Link strategy:** Why external links kill reach; when/how to link to your own site; LinkedIn Articles vs your blog
- **Monthly architecture:** Content pillar system, week-by-week rhythm, 6-month compound strategy
- **Comments strategy:** Anatomy of a great comment, targeting tiers, timing, dos/don'ts
- **DM strategy:** Four valid reasons to DM, anatomy, worked examples, follow-up rules, pipeline system
- **Profile optimisation:** Headline, About, Featured, Experience — as a conversion page
- **Engagement system:** Daily comment cadence, strategic targets, metrics that actually matter

**Reference files:**
- `references/content-strategy.md` — formats, link strategy, monthly architecture, 6-month arc, dos/don'ts
- `references/comments.md` — comment anatomy, targeting, timing, dos/don'ts
- `references/dms.md` — DM anatomy, examples, follow-up rules, pipeline system
- `references/profile-and-engagement.md` — profile structure, daily engagement system, tracking

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


---

## `bob:knowledge` — Knowledge Vault Retrieval

**File I/O:** Reads `knowledge/README.md`, selected `_index.md` files, and at most 5 individual notes. Never writes.

**Invoked by:** `bob:context-protocol` at the start of every engineering command.

**What it does:**
1. Check for vault (`knowledge/README.md`) — skip silently if missing
2. Load root README in full (small, always relevant)
3. Identify and load relevant notes (at most 5; progressive disclosure via Obsidian search or `_index.md` scanning)
4. Output Knowledge Context block with full MOC list and pre-loaded notes
5. Add standing retrieval instruction that stays active for the rest of the session

**Skip conditions:** `knowledge/README.md` not found; file already loaded this session (no duplicate loads).

---

## `bob:code-graph` - Code Graph Query Capability

**File I/O:** Read-only capability detection. Never loads or traverses `graph.json`; all dynamic queries delegate to graphify's CLI/skill. Never writes; never rebuilds.

**Invoked by:** `bob:context-protocol` at the start of every engineering command (symmetrical with `bob:knowledge`).

**What it does:**
1. Detect capability via two self-describing signals (`command -v graphify` for installed, `graphify-out/graph.json` for built) and assert version >= 0.9.11. Skip silently if any is missing/older or a call fails.
2. Freshness gate (hook-aware layered): if `graphify hook status` shows the hook installed, trust it for committed code and only `git status --porcelain` for uncommitted edits; if no hook, run graphify's deterministic `detect_incremental` (no LLM) and warn if stale. Never auto-rebuilds.
3. Output a Code Graph Context block: freshness line + standing query instruction with scoping defaults. Does not include the hub list (context-protocol's familiarity step owns orientation).

**Query policy (standing instruction to the command):** prefer narrow tools such as `graphify affected "X"` (depends-on / blast radius), `graphify path A B`, and `graphify explain X`; reserve `graphify query` for open-ended questions. Always pass `--budget` and scope via `--context`; exclude test nodes for architecture questions. All tools are pure `graph.json` traversal, with no network and no GitHub; `graphify prs` is never used.

**Skip conditions:** graphify absent; no graph built; version older than 0.9.11; any graphify call fails. Degrades to today's grep/Explore behaviour with nothing emitted.

---

## `bob:vault` — Vault Management Controller

**File I/O:** Reads and writes `knowledge/` notes, indexes, MOCs, `log.md`, `sources/`. Executes Python scripts in `bob/skills/vault/scripts/`.

**Invoked by:** `/bob:library` command (for all modes except retrieve).

**What it does:**
Receives a mode from the library command and loads only the relevant sub-file:
- `process` → `skills/vault/process.md` — reconcile-gated inbox processing, subagent batching for large inboxes
- `ingest` → `skills/vault/ingest.md` — fetch/extract from URL or local file, reconcile, save source
- `organise` → `skills/vault/organise.md` — incremental (git_scope.py), lint, integrity audit, active maintenance
- `bootstrap` → `skills/vault/bootstrap.md` — vault initialisation
- `status` → inline — counts and last-modified date

**Python scripts** (`bob/skills/vault/scripts/`):
- `lint.py` — frontmatter audit (required fields, old field names), broken links
- `git_scope.py` — files changed since a timestamp; supplements with `git status --porcelain` for untracked
- `log_append.py` — append operation entry to `knowledge/log.md`; creates file on first write
- `orphan.py` — notes with no inbound links from other vault notes

**Shared:** `reconcile.md` — discovery-classify-confirm procedure, read by process and ingest before any note write. Mirrors `bob:knowledge` discovery traversal.

---

## `bob:obsidian` — Obsidian Vault File Operations

**File I/O:** No reads or writes directly. Executes `obsidian rename` / `obsidian move` via the Obsidian CLI, which modifies files inside the vault.

**Invoked by:** Automatically via PreToolUse hook when `mv` or `git mv` is used on `.md` files. Also triggers when user asks to rename or move a markdown file.

**Purpose:** Prevent wikilink breakage by routing all `.md` file moves and renames through the Obsidian CLI instead of the filesystem directly.

**Workflow:**
1. Detect vault: walk up from CWD for `.obsidian/` folder
2. Detect CLI: `which obsidian`
3. If either missing: stop, tell user what to set up (no fallback to `mv`)
4. Show plan, wait for user approval
5. Execute `obsidian rename` or `obsidian move`
6. Verify file exists at new path

**Requirements:**
- Obsidian 1.12.7+ installed and CLI registered (Settings → General → Command line interface)
- "Automatically update internal links" enabled (Settings → Files & Links)
- Obsidian app running (auto-launches on first CLI call)

---

## `bob:work-routing` — Discovered Work Item Routing

**File I/O:**
- **Reads:** `{story_path}/_kanban.md`, `projects/{subproject}/_kanban.md`
- **Writes:** `{story_path}/_kanban.md` (Issues column), `projects/{subproject}/_kanban.md` (INBOX column) — only after user confirms

**User-invokable:** No — invoked mid-session by engineering commands.

**Invoked by:** All engineering commands (`implement`, `review`, `review-plan`, `plan`, `brainstorm`, `investigate`, `ui-review`) mid-session when they surface issues, deferred ideas, out-of-scope findings, or new dependencies. Also invoked by `bob:done-criteria` (Behaviour 6) for end-of-session routing.

**What it does:**
- Accepts a list of work items with description, severity (🔴/🟡/🟢), and discovery context
- Classifies each item: in-scope for current story → story Issues column; otherwise → project INBOX
- Asks user for confirmation before filing; names 🔴 Critical items explicitly
- After filing, confirms counts: "Filed N items: {story-id} Issues (+N), INBOX (+N)."

**Key rule:** Routing logic lives here — individual commands must not embed their own routing decisions.
