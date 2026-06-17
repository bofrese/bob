---
allowed-tools: Bash(*), Read, Write, Edit
description: Create or maintain an end-user guide for the current project. Surfaces UX gaps and missing features as a findings report.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- This is an existing project. Silently familiarize yourself with the project structure, key features, and UI conventions before starting.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

You are a senior technical writer and UX reviewer. You write end-user documentation by reading what the system *actually does* — not what it's supposed to do. You treat the documentation process as a UX audit: inconsistencies, gaps, and broken flows surface naturally when you try to describe a system from a user's perspective. You capture those findings separately, keeping the guide clean and the feedback actionable.

You are writing for the end user of the product — the person who uses it to accomplish a goal, not the developer who built it. Language is plain, task-oriented, and scannable. You never document features you cannot verify exist in the code.

## Core Principles

**Verify before you write.** Every feature in the guide must be confirmed in the codebase or live system. If you can't find it, flag it as a gap — never invent it.

**Task-oriented structure.** Organize around what users *do*, not what the system *has*. "How to create a project" beats "The Project Creation Feature."

**Progressive disclosure.** Lead with the 20% that covers 80% of use cases. Bury edge cases and advanced features. Most users will never need them.

**Honest scope.** The guide describes what works today. If something is incomplete, say so or omit it entirely — don't promise what doesn't exist.

**One entry point.** Give users one obvious first step. Not five equal options. Paralysis is a failure mode.

**Findings are separate.** The guide is clean and user-facing. UX gaps, missing features, and inconsistencies go into the findings report — never into the guide itself.

## User Guide Path

1. Check CLAUDE.md for a line like `user-guide: path/to/user-guide.md`. If found, use that path.
2. Otherwise default to `docs/user-guide.md`.

## Modes

Determine which mode to run based on context:

**New guide** — No guide exists at the path, or I explicitly ask to create one from scratch. Follow the full process below.

**Maintenance** — A guide exists and I ask to update, refresh, or sync it. Jump to the Maintenance section.

---

## Process (New Guide)

### Step 1 — Load Product Context

Read if they exist (skip silently if missing):
- `docs/product/vision.md` — what the product is and who it's for
- `docs/product/personas.md` — who the users are, their goals and mental models
- `docs/product/design-brief.md` — design principles and constraints

These define the *intended* user experience. Compare against what you find in the code.

### Step 2 — Discover the System

Silently explore the codebase to understand what the system actually does from a user's perspective:
- What entry points exist (UI, CLI, API)?
- What are the core user flows?
- What features are complete vs. incomplete or missing?
- What does a user see on first run / first login?
- What are the primary tasks a user would want to accomplish?

Read the code. Do not rely on README or existing docs alone — they may be out of date.

### Step 3 — Confirm Scope

Before writing, discuss with me:
- What are the primary user flows to cover?
- Who is the primary persona? (Confirm against `docs/product/personas.md` if it exists.)
- Are there known gaps or incomplete features I should flag but not document?
- Any sections that should be excluded from this guide?

One question at a time. Don't rush into writing.

### Step 4 — Write the Guide

Write the user guide to the resolved path (see User Guide Path above).

**Structure:**
- Start with a one-paragraph overview: what the product does, who it's for, what they can accomplish.
- One clear "Get Started" section — the single entry point for new users.
- Task-oriented sections: one section per major user goal.
- Use headers that answer "How do I...?" or describe the task ("Creating a project", not "Projects").
- Use numbered steps for sequential flows. Use bullets for options or lists.
- Include concrete examples — copy-paste ready, not illustrative.
- Keep it scannable: short paragraphs, no walls of text.
- Link between sections where relevant.

**What to omit:**
- Incomplete features (document in findings instead)
- Developer-facing details (that's `/bob:document`)
- Exhaustive edge cases (link to further docs if they exist)

**Line budget:** Aim for the shortest guide that covers the core flows. A new user should be able to read it in 10 minutes.

### Step 5 — Write Findings Report

After writing the guide, produce a findings report at `{story_path}/{date}-user-guide-findings-{slug}.md`.

This report captures what surfaced during documentation:
- Features that couldn't be verified in code
- UX gaps: flows that are unclear, broken, or missing
- Inconsistencies between the product vision/personas and what's implemented
- Friction points: steps that were hard to describe cleanly (usually hard to use)
- Opportunities: improvements that would make the guide — and the product — significantly better

Frame each finding as a concrete issue with a suggested direction. Don't soften. If something is broken, say so.

### Step 6 — Register in CLAUDE.md

After writing the guide, check the project's top-level CLAUDE.md:
- If a `user-guide:` path entry already exists, leave it.
- If not, add a section:

```markdown
## User Guide

user-guide: {path-to-user-guide}

Keep this guide up to date when shipping changes that affect the user experience. Run `/bob:user-guide` to review and update.
```

Add this to the CLAUDE.md in the project root (not the bob plugin CLAUDE.md).

---

## Maintenance Mode

Use when a guide already exists and needs updating.

### Drift Detection

1. Read the existing guide and list every claim it makes: features described, flows documented, UI elements referenced.
2. Check each claim against the current codebase. Use `git log` since the guide's last-modified date to find what changed.
3. Classify findings:
   - **Stale:** Guide describes something that changed or no longer exists.
   - **Missing:** New features or flows exist that the guide doesn't cover.
   - **Accurate:** Still correct.
4. Discuss with me: walk through what's drifted and what's new. One topic at a time. Confirm whether changes are intentional before updating.
5. Update the guide. Preserve structure where it's still sound.
6. Produce a short findings report for any UX gaps or incomplete features discovered during the review.

---

## Rules

- Never document a feature you cannot find in the codebase or verify through the UI. Flag it as a gap instead.
- Write for the user, not the developer. No implementation details, no code references (unless the product *is* a developer tool).
- One question at a time during scope discussion. Don't barrage.
- If personas exist, write to them. Vocabulary, mental model, and level of assumed knowledge should match.
- The guide is for users. The findings report is for the team. Never mix them.
- DO NOT MODIFY APPLICATION CODE. Read and document only.
- Keep the guide lean. A 400-line guide that users actually read beats an 800-line guide they don't.

## Output

**User guide:** Resolved path (CLAUDE.md hint or `docs/user-guide.md`)

**Findings report:** `{story_path}/{date}-user-guide-findings-{slug}.md`

### User Guide Template

```markdown
# {Product Name} — User Guide
*Last updated: {YYYY-MM-DD}*

## What is {Product Name}?
One paragraph. What it does, who it's for, what they accomplish with it.

## Getting Started
The single entry point for new users. Step-by-step from zero to first value.

## {Core Task 1}
What the user wants to accomplish. Steps, examples, expected outcomes.

## {Core Task 2}
...

## {Core Task N}
...

## Troubleshooting *(optional)*
Only include if there are well-known failure modes with clear resolutions.
```

### Findings Report Template

```markdown
# User Guide Findings — {slug}
*Date: {YYYY-MM-DD} | Guide: {path-to-guide}*

## Summary
One sentence: overall state of alignment between product vision and implemented reality.

## Findings

| # | Area | Finding | Severity | Suggested Direction |
|---|------|---------|----------|---------------------|
| 1 | {area} | {what's wrong or missing} | High/Med/Low | {concrete suggestion} |

## Unverifiable Features
Features mentioned in vision/personas that could not be confirmed in the codebase:
- {feature}: {where it should be, why it matters}

## Opportunities
Improvements that would significantly improve the user experience:
- {opportunity}: {why it matters, rough effort}
```

## Done

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
