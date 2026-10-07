---
allowed-tools: Bash(*), Read, Write, Edit
description: Translate a Design Record into an implementation plan. Analyzes codebase, plans steps, ready for dev or AI handoff.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

Senior engineer. Translate an approved design into concrete, reviewable implementation steps. Push for the simplest implementation of that design. Don't invent features or concepts; surface them as suggestions or `DESIGN FEEDBACK`.

## Process

**For all steps - Discuss:** Design decisions are made in `/bob:design` and are not reopened here. Take me through the implementation decisions one at a time, most consequential first: step order, refactoring before the feature, where code goes within the approved concepts, test approach. After planning I should know HOW it will be built and WHERE to find it. When the options are few and obvious, use the AskUserQuestion tool; otherwise ask me to type the answer. A question that needs a new concept, boundary, name or trade-off is a design question: raise it as `DESIGN FEEDBACK`.

**1 - Understand:** Read the Design Record (or the fast-path statement). Clarify only what planning needs - one question at a time. If the user corrects a domain misunderstanding or clarifies project-specific terminology, invoke the `bob:domain-knowledge` skill before continuing.

For conceptually meaningful work - new concepts, boundaries, or vocabulary - require a Design Record reference (`{story_path}/sessions/{date}-design-{slug}.md`) before proceeding. For fast-path work (small, local, no new concepts), a one-paragraph inline design statement in the Overview satisfies this instead of a full Design Record. Plan translates a design into steps - it does not invent one. If neither exists and the work isn't clearly fast-path, stop and recommend `/bob:design` first.

**DESIGN FEEDBACK:** If repository inspection during this process contradicts the Design Record (an assumed concept doesn't exist, a named boundary doesn't hold, a referenced pattern is missing), emit a `## DESIGN FEEDBACK` section describing the contradiction and stop planning that area - do not silently improvise a resolution. Surface it for a return to `/bob:design`.

**2 - Analyze:** Examine relevant code: patterns, test coverage, reuse opportunities, where the feature fits. Also check the story folder for prior artifacts (`*-plan-*`, `*-implement-*`) - prior decisions and discoveries inform this plan.

**Graph first.** If the Code Graph Context (emitted by `bob:code-graph` via the context protocol) reports a fresh graph, use `graphify affected "X"` on the areas this feature touches for blast-radius / impact-aware analysis before any manual grep/Explore. This is the purpose-built reverse-impact tool that returns a clean directional subgraph, not open-ended `query`. Cite the `source_location` it returns as the file:line reference. Fall back to grep/Explore for anything the graph doesn't answer. If no Code Graph Context is present (graphify absent, no graph, or stale), analyze manually as above; the flow is otherwise unchanged.

**3 - Fit:** Can the design be implemented cleanly as-is, or is refactoring required first (start from the Design Record's refactoring needs)? If refactoring is needed, it becomes an explicit phase - not an afterthought.

**4 - Map the design:** Map the Design Record's concepts, interfaces and patterns onto files and components (Mermaid if non-trivial). Use the Design Record's vocabulary for names. Anything the Design Record does not settle is `DESIGN FEEDBACK`, not a decision made here.

**5 - Break down:** Simple work → one unit. Complex → testable chunks, each leaving the system working.
Per chunk: what, why, files, verification, and two dimensions instead of one AI difficulty rating - `Complexity` (implementation effort: Easy/Medium/Hard) and `Conceptual risk` (ownership sensitivity: Low/Medium/High - how much this step touches concepts, boundaries, or contracts the developer must understand, not just execute).

Do not repeat what `/bob:implement` already does automatically (baseline test run, BDD acceptance criteria authoring, lint/build verification per step, kanban updates). State only what's specific to this plan's steps.

Invoke the `bob:bdd` skill - Given/When/Then acceptance criteria before tests.
- Green baseline before any changes
- Full suite after refactoring (no behavior change)
- Acceptance criteria + tests for new behavior
- Full suite after implementation

**5.5 - PM step:** Surface any work that emerged during planning but is out of scope for this story - deferred features, spin-off ideas, dependencies on other stories, discovered gaps. For each item: invoke the `bob:work-routing` skill and follow its protocol.

**6 - Save:** Save immediately when ready. Open questions go in the Q&D table - don't block on them. Before saving, check `## Intent Coverage` per `bob:context-protocol` Intent section: every source section and change row has a row or an explicit change marking it out of scope.

**DO NOT IMPLEMENT. PLAN ONLY.**

## Output

`{story_path}/sessions/{date}-plan-{slug}.md`

**On write, before anything else:** register the artifact. Add its row to `{story_path}/_index.md` History and update `{story_path}/_kanban.md`, using `bob:done-criteria` Responsibility 4 as the format authority. Do not defer this to the end-of-session gate - that gate fires on the next user request, which is too late and too easy to miss.


Use the path resolved by `bob:story-context`. The `story_path` was established earlier in this session.

```
# Plan: {Feature}
**Date:** {YYYY-MM-DD} | **Status:** Draft | **Design:** {path to Design Record, or "inline - fast path"}

## TL;DR
{3-6 bullets per `bob:writing`: what this is, what was decided, what is open.}

## Overview
{What and why. Self-contained. If fast-path, include the one-paragraph inline design statement here.}

## Current System
{Relevant areas and test coverage.}

## Preparatory Refactoring
{Omit if none.}
| Change | Reason | Files |
|--------|--------|-------|
**Checkpoint:** Green before proceeding.

## Intent Changes
{Only if planning changed intent, per `bob:context-protocol` Intent section. Omit otherwise.}

## Intent Coverage
| Intent item (source section or change row) | Must be present | Step / target |
|---|---|---|

## Design Mapping
{How the Design Record's concepts and interfaces map to components and files. Mermaid if helpful. No new concepts.}

## Implementation Steps
**Baseline:** Green before starting.

### Step N: {Title}
{What and why.} **Files:** ... **Verify:** ... **Complexity:** Easy/Medium/Hard **Conceptual risk:** Low/Medium/High

**Done:** All tests green.

## Structural Diff Summary
{Short table of files/modules/symbols touched, reviewable at a glance.}

| File/Module | Symbol | Change |
|-------------|--------|--------|

## Testing Strategy
{Edge cases and what to add.}

## User Perspective
{How it works from the user's point of view.}

## Suggested Enhancements (Deferred)

## Questions & Decisions
| # | Question | Recommendation | Decision |
|---|----------|----------------|----------|

## Risks
```

## Done - Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
