---
name: Done Criteria Protocol
description: Non-deferrable. Invoke before responding to any new request at the end of every output-producing bob command. Defines how commands interact with the done system, bootstraps the project done-criteria file, and tracks discovered issues. Follow the protocol exactly.
user-invocable: false
---

# Done Criteria — Protocol

This skill does two jobs: it defines **how commands interact with the done system**, and it contains the **bootstrap template** that seeds a fresh project.

---

## The Protocol — Seven Behaviours

### 1. Bootstrap if missing

At the start of your command, check whether `docs/process/done-criteria.md` exists.

If it does **not** exist:
- Create `docs/process/` if needed.
- Copy the **Bootstrap Template** (below) into `docs/process/done-criteria.md`.
- Replace `{date}` with today's date.
- Continue with your command as normal.

If it **does** exist: do nothing. It's already bootstrapped.

### 2. Check before finishing

Before you consider your output complete, read `docs/process/done-criteria.md` and check every item that applies to your command type. If anything isn't satisfied, flag it explicitly in your output rather than shipping incomplete work.

Which items apply:
- `implement` → Code changes section
- `plan` → Plans section
- `review`, `review-plan` → Reviews section
- `document` → Documentation section
- Product-tier commands (`product-vision`, `design-brief`, `personas`) → check that output is self-contained and readable without prior context

### 3. Register new artifact types

If your command introduces an artifact type that isn't already tracked in `docs/process/done-criteria.md`, add a new subsection under DONE with the appropriate criteria. This is how the list grows as a project adopts more commands.

**The golden rule:** criteria must be generic, not feature-specific. "Tests must pass" — yes. "The login tests must pass" — no. Feature-specific dependencies belong in the plan.

### 4. Flag decisions for persistence

Before finishing, explicitly list any of the following that emerged this session and aren't already in your output artifact:

1. **Terminology or naming conventions** established or clarified
2. **Architectural decisions** made that aren't captured in the plan
3. **Patterns discovered** that should become guidelines

For each item found: name it, explain why it matters, and recommend the specific command to persist it (`/bob:document` for decisions/terminology, `/bob:guidelines` for reusable patterns).

Also check for:

4. **Decisions and insights** not yet captured in `knowledge/` → write candidates to `knowledge/_INBOX/YYYY-MM-DD-<slug>.md` (frontmatter: `title:`, `type: inbox`, `timestamp: YYYY-MM-DDThh:mm:ssZ`; body: the decision or insight) and surface nudge: "N item(s) captured to `knowledge/_INBOX/` — run `/bob:library process` to file them." Skip if `knowledge/` does not exist. If `knowledge/_INBOX/` does not exist, run `mkdir -p knowledge/_INBOX/` before writing.

If none of the categories apply: skip silently.

### 5. Update daily note

If `personal/daily/` directory exists: append a session entry to `personal/daily/YYYY-MM-DD.md`, creating the file if it doesn't exist. If the directory does not exist: skip silently.

Append under `## Sessions`:
```
### /<command> (<STORY-ID>) HH:MM
1-2 sentence summary of what was done.
```
If no story context: use `### /<command> HH:MM` (omit story ID).

When creating a new daily file, use this template:
```markdown
---
title: YYYY-MM-DD
type: daily
date: YYYY-MM-DD
---

# YYYY-MM-DD

## Sessions

## Wrap-up

## Notes
```
No confirmation needed — personal content, gitignored entirely.

### 6. Track discovered issues (if applicable)

If your command discovered issues, technical debt, or improvement opportunities during this session:

**Step 1:** List discovered items with severity (🔴 Critical / 🟡 Important / 🟢 Nice to Have). Keep to one line per item.

**Step 2:** Invoke the `bob:work-routing` skill to compile routing destinations for each item.

**Step 3:** Ask the user once: "Should I file these N items to the kanban? (yes / no / specify which ones)"
- **yes** → file all items as routed
- **no** → skip tracking; items remain in the command output only
- **specify** → user can exclude or redirect individual items before filing

**Step 4:** After filing, confirm: "Filed to kanban: [summary — e.g., BOB-004 Issues +2, INBOX +1]." For 🔴 Critical items: name them explicitly in the summary.

Commands this applies to: `review`, `implement`, `plan`, `document`, `investigate`, `review-plan`, `brainstorm` — engineering tier commands that touch or read code.

**Skip if already routed:** If a mid-session PM step already ran during this session and routed all discovered items, skip Behaviour 6 to avoid prompting the user twice for the same items.

Commands that skip this: Discovery commands (`product-vision`, `personas`, `design-brief`).

### 7. Update story history

After producing any output artifact, add one row to `{story_path}/_index.md` history table:

```
| {date} | [{type}]({filename}) | {one-line summary} | {outcome} |
```

Where:
- `{type}` is the command type (Brainstorm, Plan, Plan Review, Implementation, Code Review, Investigation, UI Review)
- `{filename}` is `sessions/[artifact-filename]` — all session artifacts live in the story's `sessions/` subfolder, never at the story root
- `{one-line summary}` is what was done
- `{outcome}` is the result (e.g. Committed, Draft, Ready, Approve with changes, Completed, Root cause identified)

If `story_path` was not resolved (e.g. a Discovery command with no story context), skip this step silently.

---

## Bootstrap Template

Everything below the `---` is the template. Copy it verbatim into `docs/process/done-criteria.md` when bootstrapping. Replace `{date}` with today's date.

---

# Done Criteria

> This file is maintained by commands and humans alike.
> Commands add entries when they introduce new artifact types.
> Humans can add, remove, or edit entries at any time.

---

## READY — Before work starts

These must be true before `implement` (or any execution command) begins:

- [ ] A plan exists and has been reviewed (in story folder)
- [ ] Tests pass at baseline (green before any changes)
- [ ] Applicable guidelines have been read (`docs/guidelines/`)

---

## DONE — Before output is considered complete

Every command checks applicable items before finishing.

### Code changes (`implement`)
- [ ] All tests pass (existing and new)
- [ ] Linter/formatter clean on modified files
- [ ] No hardcoded secrets or debug code

### Documentation (`document`)
- [ ] `docs/README.md` index is up to date
- [ ] Related docs cross-referenced

### Plans (`plan`)
- [ ] Plan is self-contained (readable without prior context)
- [ ] Testing strategy defined
- [ ] Questions & Decisions table populated

### Reviews (`review`, `review-plan`)
- [ ] Findings categorised by severity
- [ ] Action items are actionable and prioritised

---

*Last updated: {date}*
*Maintained by: commands and humans*
