---
name: bob:code-graph
description: Load code-graph query capability and freshness state into context from a graphify-built graph. Invoked silently by context-protocol at the start of every engineering command. Distinct from the graphify skill (the build/query engine) and from context-protocol's familiarity step (which owns the hub list). Returns a Code Graph Context block. Skip silently if graphify is absent, no graph is built, or the version is too old.
user-invocable: false
---

# Code Graph Skill

Read-only capability skill for a graphify-built code graph. Invoked silently by context-protocol at the start of every engineering command. Owns all graphify policy (detection, freshness, and query delegation) so commands stay thin. Returns a Code Graph Context block with the freshness state and a standing query instruction.

**Note:** This skill is distinct from the `graphify` skill/CLI, which builds and traverses the graph. This skill never loads or traverses `graph.json` itself; it delegates every dynamic query to graphify's narrow tools. It also does not emit the community-hub list: context-protocol's familiarity step reads `GRAPH_REPORT.md` for orientation. This skill only handles freshness plus query policy.

## Protocol

### Step 1 - Detect capability
Two self-describing signals, no bespoke flag store:
- `command -v graphify` - graphify installed?
- `graphify-out/graph.json` exists - graph built?

Then assert the minimum version: `graphify --version` must report **>= 0.9.11** (pre-1.0 surfaces can move; bob depends on `path`/`explain`/`affected`/`query`/`hook`/`detect_incremental`).

If graphify is absent, no graph is built, the version is older, or any graphify call fails: **skip silently. Output nothing.** bob degrades to today's behaviour (grep/Explore).

### Step 2 - Freshness gate (hook-aware layered)
Determine whether the graph reflects the current code. **Never auto-rebuild mid-command** (no surprise `graph.json` writes).

Check `graphify hook status`:

**Hook installed** - trust it for committed code (the post-commit/post-checkout hook keeps it current). Only cover the gap it cannot see: run `git status --porcelain` for uncommitted code edits. If any exist, note in the freshness line that *the graph excludes uncommitted edits*.

**No hook** - run graphify's deterministic incremental detection (`detect_incremental`, no LLM; delegate to the graphify skill, do not reimplement). If it reports changed / new / deleted files, warn *stale* with the count and suggest `/graphify . --update`. Do not run the update.

### Step 3 - Output Code Graph Context block
Emit the block below: a freshness line plus the standing query instruction with scoping defaults. Do **not** include the hub list; the familiarity step owns orientation.

```
**Code Graph Context**

**Graph:** fresh - reflects current code.
(or: fresh, but excludes uncommitted edits - commit or note them when querying)
(or: STALE - N files changed since last build; run `/graphify . --update` before relying on graph answers)

**Querying (standing instruction - prefer the graph over grep/Explore for code-relationship questions):**
- "What depends on X / blast radius / reverse impact" -> `graphify affected "X"` (the standing tool; returns a clean directional subgraph).
- "How does A reach B / connection" -> `graphify path "A" "B"`.
- "What is X / its neighbours" -> `graphify explain "X"`.
- Open-ended / exploratory only -> `graphify query "<question>"`.
- Always pass `--budget N` and scope with `--context` (repeatable); exclude test nodes for architecture questions. graphify also auto-infers context filters, so the defaults complement that inference rather than fight it.
- Symbol-level questions -> call the CLI directly. Fuzzy / natural-language / cross-vocabulary questions -> route through the graphify skill (it adds vocab-expansion; do not reimplement).
```

## Rules

- Read-only. Never writes to `graphify-out/`. Never triggers a rebuild.
- Never loads or traverses `graph.json`; all dynamic queries delegate to graphify's tools.
- All query tools used (`path`, `explain`, `affected`, `query`) are pure `graph.json` traversal: no network, no GitHub. (`detect_incremental` is a freshness probe, not a traversal - see the freshness gate above.) `graphify prs` is never used (it is GitHub-coupled).
- `graphify affected "X"` is the standing tool for depends-on / blast-radius; reserve open-ended `query` for genuinely open questions.
- Fully silent when graphify is absent, no graph is built, the version is older than 0.9.11, or any call fails. bob must behave exactly as today, with no graphify mentions leaking.
