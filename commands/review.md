---
allowed-tools: Bash(*), Read, Write, Edit
description: Review code changes critically. Auto-detects scope, checks guidelines, assesses system health, enables ownership transfer.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

Senior architect reviewing code. Lens: system health, simplicity, and ownership transfer. Good code acknowledged briefly — problems get attention.

## Process

**1 — Detect scope** (unless directed):
```bash
git status --porcelain
git log --oneline main..HEAD 2>/dev/null || git log --oneline master..HEAD 2>/dev/null
ls -t "${story_path}sessions/"*-plan-*.md 2>/dev/null | head -3
```
Correlate plans with changed files. Form a scope hypothesis.

**2 — Confirm scope:** Present branch, uncommitted changes, commits ahead of main, recent plans, correlation, proposed scope. Wait for confirmation.

**3 — Load context:** Guidelines for file extensions/paths/concepts in scope. Read plan if changes correlate to one. Gather full diffs. Read all changed files completely.

**4 — Understand:** Approach taken, key components, design decisions, non-obvious behavior. Note plan deviations.

**5 — Review:**
- **System health:** Clean codebase? Architecture coherent? Patterns followed? Logic duplicated? Responsibilities separated?
- **Simplicity:** Simplest solution? Abstractions justified? Control flow clear?
- **Guidelines:** Principles followed? Anti-patterns avoided?
- **Security:** Input validation, auth, injection risks, sensitive data, no hardcoded secrets.
- **Robustness:** Edge cases, error handling, no silent failures.
- **Readability:** Self-documenting? Names clear?
- **Plan alignment:** Intent matched? Deviations justified? All steps done?
- **Done criteria:** Read `docs/process/done-criteria.md`. Verify each applicable item.

**Graph-assisted system health** (if a fresh Code Graph Context was emitted by `bob:code-graph` via the context protocol):
- **God-nodes / hubs:** cross-check the community-hub list from `GRAPH_REPORT.md` (read during familiarity). Do the changed files touch, grow, or worsen an architectural hub? Flag coupling that concentrates on a god-node.
- **Diff impact (LOCAL GIT ONLY):** derive changed symbols from `git diff` (working tree, or `main..HEAD`), never from a hosted PR, then run `graphify affected "X"` per changed symbol to see the blast radius the change actually touches. Cite the `source_location` graphify returns as the file:line reference.
- **Hard constraint - no GitHub:** stay on local git throughout. Do NOT use `graphify prs` (it reads GitHub PRs via the `gh` CLI). `graphify affected` is pure `graph.json` traversal (no network, no GitHub) and is the correct impact tool here. Nothing in this flow may call `gh`.

If no Code Graph Context is present (graphify absent, no graph, or stale), skip this and assess system health as above; the flow is otherwise unchanged.

**Over-engineering pass:** If the Ponytail plugin is installed (its `/ponytail-review` command is available), run it on the same diff and fold its findings into the Simplicity assessment — deduplicate, don't double-report. If not installed, skip silently.

**PM step:** Before discussing findings, invoke `bob:work-routing` for any discovered issues, technical debt, or improvement opportunities that are clearly out of scope for this story. In-scope findings go into the report — only route items that belong elsewhere.

**6 — Discuss:** One topic at a time. 🔴 Critical (must fix) · 🟡 Important (should fix) · 🟢 Suggestion. Briefly acknowledge good work.

Before writing the report: identify any patterns in the findings that should become guidelines — especially if the same type of issue appeared more than once or reflects a convention worth codifying. If found, name the pattern and suggest `/bob:guidelines` with a specific topic.

Ask before writing report.

**7 — Save.**

## Rules

Direct. File:line for all findings. **DO NOT FIX THE CODE.**

## Output

`{story_path}/sessions/{date}-review-{slug}.md`

Use the path resolved by `bob:story-context`. The `story_path` was established earlier in this session.

```markdown
# Review: {Feature/Change}
**Date:** {YYYY-MM-DD} | **Scope:** {what reviewed} | **Plan:** {path or N/A}
**Verdict:** ✓ Approve | ⚠ Approve with concerns | ✗ Needs work | 🛑 Significant issues

## What Was Done
**Approach:** {How implemented — patterns and key design decisions.}
**Key points:**
- `{file}:{lines}` — {what the core logic does}
- {Non-obvious behavior, dependencies, gotchas}

## Plan Alignment
{Omit if no plan.}
| Aspect | Planned | Implemented | ✓/⚠/✗ |

## System Health
| Dimension | Assessment |
|-----------|------------|
| Architecture | |
| Maintainability | |
| Consistency | |
| Technical Debt | |

## Findings

### 🔴 Critical
**{Title}** · `{file}:{line}`
{Issue and why it matters.} **Fix:** {action}

### 🟡 Important
**{Title}** · `{file}:{line}`
{Issue.} **Fix:** {suggestion}

### 🟢 Suggestions
**{Title}** · `{file}:{line}` · {suggestion}

## What Was Done Well
- {thing}

## Guideline Compliance
| Guideline | ✓/⚠/✗ | Notes |

## Action Items
1. [Critical] {action}
2. [Important] {action}
3. [Suggestion] {action}
```

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
