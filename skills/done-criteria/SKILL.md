---
name: Done Criteria Protocol
description: Invoke this skill at the end of every output-producing bob command. Defines how commands interact with the done system, bootstraps the project done-criteria file, and tracks discovered issues. Follow the protocol exactly.
user-invocable: false
---

# Done Criteria — Protocol

This skill does two jobs: it defines **how commands interact with the done system**, and it contains the **bootstrap template** that seeds a fresh project.

---

## The Protocol — Six Behaviours

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

If none of the three categories apply: skip silently.

### 5. Track discovered issues (if applicable)

If your command discovered code issues, technical debt, or improvement opportunities:

**Step 1: Show brief summary** to user:
- List issues found with severity (🔴 Critical / 🟡 Important / 🟢 Nice to Have)
- Keep it concise (one line per issue)

**Step 2: Ask user**: "Should I add these to the story's issue tracker?"

**Step 3: If yes**, for each issue decide where it belongs:

- **Clearly within this story's scope** → add to `{story_path}/_kanban.md` Issues column as `- [ ] {description}`
- **General/cross-cutting concern** → add to `projects/{subproject}/_kanban.md` INBOX column
- **Looks like it could be its own story** → ask the user: "This feels like a separate concern that might deserve its own story rather than a task in this one. Should I add it to the `projects/{subproject}/_kanban.md` INBOX as a story candidate?" Add to project INBOX if yes.
- If subproject is unclear, derive from story context or ask

**Step 4: If no**: Skip tracking, just report in your output

**Commands this applies to**:
- `review`, `implement`, `plan`, `document`, `investigate`, `review-plan`
- Engineering tier commands that touch or read code

**Commands that skip this**:
- Discovery commands (`product-vision`, `personas`, `design-brief`)
- Commands focused on product/business artifacts, not code

### 6. Update story history

After producing any output artifact, add one row to `{story_path}/_index.md` history table:

```
| {date} | [{type}]({filename}) | {one-line summary} | {outcome} |
```

Where:
- `{type}` is the command type (Brainstorm, Plan, Plan Review, Implementation, Code Review, Investigation, UI Review)
- `{filename}` is the artifact filename relative to the story folder
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
