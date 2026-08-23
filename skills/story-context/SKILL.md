---
name: story-context
description: Invoke this skill at the start of every engineering command (brainstorm, design, plan, review-plan, implement, review, investigate, ui-review), after loading context files. Resolves which story is active via a 4-tier chain, confirms with the user, and establishes the story folder path for artifact placement. Follow the protocol exactly — do not proceed until story context is confirmed.
version: 1.0.0
---

# Story Context

Resolves the active story for the current session. Every engineering command must invoke this skill and obtain a confirmed story path before writing any artifacts.

The skill invocation system provides an absolute base directory for this skill. Scripts are referenced as `$SKILL_BASE_DIR/scripts/<name>.sh`.

---

## Resolution Chain

Work through the tiers in order. Stop at the first tier that yields a result.

### Tier 1 — Path-derived (certain)

**Trigger:** A file argument was provided and its path contains `projects/[sub]/stories/[ID]/`.

```bash
bash "$SKILL_BASE_DIR/scripts/detect-story-from-path.sh" "<file-arg-path>"
```

If the script outputs `SUBPROJECT=` and `STORY_ID=`, the story is certain. Print the Story Context block and proceed — no confirmation needed.

---

### Tier 2 — Explicit mention (certain)

**Trigger:** No file arg, but the conversation or args contain a pattern matching `[A-Z]+-[0-9]+` (e.g. `BOB-001`).

Resolve the path: `projects/[subproject]/stories/[STORY-ID]/`. Run:

```bash
bash "$SKILL_BASE_DIR/scripts/detect-story-from-path.sh" "projects/[subproject]/stories/[STORY-ID]/_index.md"
```

If the directory exists, print the Story Context block and proceed — no confirmation needed.

---

### Tier 3 — Obsidian open tabs (probable)

**Trigger:** Tiers 1-2 yielded nothing. Try Obsidian.

```bash
bash "$SKILL_BASE_DIR/scripts/get-open-obsidian-files.sh" | bash "$SKILL_BASE_DIR/scripts/filter-story-paths.sh"
```

- **Zero results:** Fall through to tier 4.
- **One result:** Print the Story Context block and ask: "I see `[story-id]` open in Obsidian — is that the story we're working on?"
- **Multiple results:** List all candidates and ask the user to choose.

If the Obsidian CLI is unavailable (command fails), skip tiers 3 and 4 silently.

---

### Tier 4 — Obsidian recents (uncertain)

**Trigger:** Tier 3 yielded nothing. Try recents.

```bash
bash "$SKILL_BASE_DIR/scripts/get-recent-obsidian-files.sh" | bash "$SKILL_BASE_DIR/scripts/filter-story-paths.sh" | head -1
```

Take the most recent match. Print the Story Context block and ask: "The most recently opened story file I can see is `[story-id]` — is that what we're working on?"

---

### Fallback — Stop and ask

**Trigger:** All tiers exhausted with no result, or user declined all suggestions.

Present two options to the user:

1. **Provide a story:** "Which story are we working on? You can pass a file path or story ID (e.g. BOB-001)."
2. **Create a new story:** "If this is new work with no story yet, say 'new story' and I'll set one up."

If the user says "new story": invoke the `bob:project-tracking` skill and follow its story creation procedure. Then re-run this skill with the new story path.

If `projects/` does not exist at all: invoke the `bob:project-tracking` skill and follow its Bootstrap procedure. Then re-run this skill.

**Never proceed without a confirmed story path.**

---

## Story Context Output Block

Once a story is confirmed, print this block exactly — downstream commands parse it:

```
**Story Context**
- Path: `projects/[subproject]/stories/[STORY-ID]/`
- Story ID: `[STORY-ID]`
- Subproject: `[subproject]`
```

If a task ID was detected, add a fourth line:
```
- Task ID: `[TASK-ID]`
```

After printing the block, set `story_path = projects/[subproject]/stories/[STORY-ID]/` in your working memory. Session artifacts (brainstorm, plan, review, etc.) are written to `{story_path}sessions/` — see the command's own Output section for the exact filename pattern.

---

## Notes

- Tiers 3 and 4 require Obsidian to be running. If the CLI is unavailable, skip silently to fallback.
- Tiers 1 and 2 are certain — proceed without asking. Tiers 3 and 4 are inferred — always ask.
- Do not cache story context across separate command invocations. Each command invocation resolves fresh.
