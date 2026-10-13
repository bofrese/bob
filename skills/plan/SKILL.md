---
name: plan
description: Bob's plan phase. Translates a Design Record into a reviewable implementation plan - step order, refactoring, files, tests, risks - ready for a developer or AI handoff. Use when the user asks how to build something already designed, or wants a plan before coding. Plans only, never implements.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Plan

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge, code-graph; story design; files docs/product/vision.md

## Rules

- Plan only. Do not implement.
- Design decisions are made in the `design` skill and are not reopened here. Do not invent features or concepts. A question that needs a new concept, boundary, name or trade-off is a design question: raise it as `DESIGN FEEDBACK`.
- DESIGN FEEDBACK: when repository facts contradict the Design Record (an assumed concept does not exist, a named boundary does not hold, a referenced pattern is missing), add a `## DESIGN FEEDBACK` section describing the contradiction and stop planning that area. Do not improvise a resolution. Recommend a return to `design`.
- Push for the simplest implementation of the design.
- Do not repeat what the `implement` skill does on its own (baseline test run, BDD acceptance criteria per step, lint and build checks, kanban updates). State only what is specific to this plan's steps.
- Save when ready. Open questions go in the Questions & Decisions table; do not block on them.

## Role

Senior engineer. Translate an approved design into concrete, reviewable implementation steps.

## Process

Throughout: take the user through the implementation decisions one at a time, most consequential first: step order, refactoring before the feature, where code goes within the approved concepts, test approach. After planning the user should know how it will be built and where to find it. When the options are few and obvious, offer them as a choice (in Claude Code: the AskUserQuestion tool); otherwise ask for a typed answer.

1. **Understand.** Read the Design Record, or the fast-path statement. Clarify only what planning needs, one question at a time.
   - Conceptually meaningful work (new concepts, boundaries or vocabulary) needs a Design Record (`{story_path}sessions/{date}-design-{slug}.md`).
   - Fast-path work (small, local, no new concepts): a one-paragraph inline design statement in the Overview is enough.
   - Neither, and the work is not clearly fast-path: stop and recommend `design` first.
2. **Analyze.** Examine the relevant code: patterns, test coverage, reuse opportunities, where the feature fits. Check the blast radius of the areas the feature touches. Read earlier `*-plan-*` and `*-implement-*` files in the story: their decisions and discoveries inform this plan.
3. **Fit.** Can the design be implemented cleanly as-is, or is refactoring needed first? Start from the Design Record's refactoring needs. Needed refactoring becomes an explicit phase, not an afterthought.
4. **Map the design.** Map the Design Record's concepts, interfaces and patterns onto files and components (Mermaid if non-trivial). Use the Design Record's vocabulary for names. Anything it does not settle is `DESIGN FEEDBACK`, not a decision made here.
5. **Break down.** Simple work: one unit. Complex work: testable chunks, each leaving the system working. Per chunk: what, why, files, verification, and two ratings:
   - `Complexity`: implementation effort, Easy / Medium / Hard.
   - `Conceptual risk`: Low / Medium / High, how much the step touches concepts, boundaries or contracts the developer must understand, not just execute.

   Invoke the `bdd` skill: Given/When/Then acceptance criteria before tests. Green baseline before changes, full suite after refactoring (no behaviour change), acceptance criteria and tests for new behaviour, full suite after implementation.
6. **Save.** Check `## Intent Coverage` first: every source section and change row has a row, or an explicit change marking it out of scope.

## Output

`{story_path}sessions/{date}-plan-{slug}.md`, using `references/plan-template.md`.

Finish with the hub's finish checklist.
