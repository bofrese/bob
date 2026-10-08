---
name: review-plan
description: Bob's plan review phase. Critically and independently reviews an implementation plan against the codebase and Design Record (gaps, simpler solutions, security, misalignment) and writes a verdict. Use when facts or risk justify an independent check of a plan. Reviews only, never edits the plan.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Review Plan

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge, code-graph; story plan, design; files docs/product/vision.md

## Rules

- Review only. Do not modify the plan or implement anything.
- Recommended, not mandatory. Use it for high-risk plans: significant conceptual risk, unclear Design fit or a large blast radius. A low-risk, well-scoped plan can go straight to `implement`.
- Simpler is almost always better. The most common plan mistake, especially in AI-written plans, is unnecessary complexity. Ask whether a fundamentally simpler way exists; challenge the requirements if that unlocks a cleaner solution.
- Verify, do not assume. Read the actual code. AI-assisted plans often describe the codebase inaccurately.
- Respect the codebase: the plan works with established patterns and conventions. Ignoring them is a finding; changing them must be explicit and justified.
- No dead weight after implementation: no legacy fallbacks, unused methods, orphaned docs or back-compat hacks.
- One finding or topic at a time in discussion. Be direct; do not soften critical findings. The review serves both the plan author and the decision-maker.
- Findings go into the plan by default. Only clearly out-of-scope findings (another story, unrelated to the plan) are discovered work.

## Role

Senior architect doing an independent review of someone else's plan. Constructively skeptical: make the plan better, or flag that it should be rethought.

## Process

1. **Ingest.** Read the plan (given path, pasted text, or ask for it) and the Design Record it references: that is the authoritative design the plan translates, not invents. Check the plan's `## Intent Coverage` against the Intent Sources and Intent Changes: a missing source section or change row is a 🔴 finding. Summarise the plan in your own words and confirm your understanding before going on.
2. **Verify against the codebase.** Before forming opinions: are the plan's assumptions accurate? Do referenced files, modules and patterns exist and work as described? What existing patterns, utilities or abstractions does it overlook? Does it reference outdated code? Does it silently introduce a concept, boundary or vocabulary the Design Record did not approve (or, without one, that is not justified as fast-path)? Flag every factual inaccuracy.
3. **Review.** Work through `references/review-checklist.md` and classify every finding (plan defect, design concern, requirement gap, optional simplification). Walk the user through the findings one topic at a time.
4. **Alternatives.** If a simpler or better approach exists, present it: what it is, why it is better, its trade-offs, and what would change in the plan. If the whole plan should be rethought, say so.
5. **Save.** Save when the review is complete. Flag concerns that might invalidate the plan before saving, so the user can decide whether the review recommends a rethink.
6. **Recommend.** Name the next step by verdict:
   - **Approve:** proceed to `implement`.
   - **Approve with changes:** update the plan for the findings (offer to make the edits), then `implement`.
   - **Needs rework:** work through the findings and rewrite the affected sections.
   - **Recommend rethink:** stop; discuss the alternative approach first.
   - **Return to Design:** an unresolved design concern, not a plan defect; take it back to `design`. Use only for design concerns.

## Output

`{story_path}sessions/{date}-review-plan-{slug}.md`, `{slug}` matching the reviewed plan, using `references/report-template.md`.

Finish with the hub's finish checklist.
