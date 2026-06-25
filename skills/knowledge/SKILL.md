---
name: bob:knowledge
description: Load relevant knowledge from the project knowledge vault into context. Invoked silently by context-protocol at the start of every engineering command. Distinct from /bob:library command (vault management). Returns a Knowledge Context block. Skip silently if knowledge/ does not exist.
user-invocable: false
---

# Knowledge Retrieval Skill

Read-only retrieval skill for the project knowledge vault. Invoked silently by context-protocol at the start of every engineering command. Returns a Knowledge Context block with pre-loaded notes relevant to the current work.

**Note:** This skill is distinct from the `/bob:library` command. This skill loads knowledge into context; `/bob:library` manages the vault. **Sources folder:** `sources/` stores raw source materials, organised by topic when volume warrants it. This skill loads only atomic notes from `decisions/`, `patterns/`, `research/`, `concepts/`. Reference sources via the `resource:` field in atomic notes, not by direct retrieval from sources/.

## Protocol

### Step 1 - Check for vault
If `knowledge/README.md` does not exist: skip silently. Output nothing.

### Step 2 - Load root README
Read `knowledge/README.md` in full. It provides the folder inventory, the Tags table (all canonical tags — the single source of truth, no mirror exists elsewhere), and the MOC list. The Tags table is the cross-cutting discovery surface — use it to identify which tags match the current session topic.

### Step 3 - Identify relevant notes

Two complementary strategies — run both if Obsidian is running, fall back to keyword-only if not.

**Check whether Obsidian is running:** `pgrep -x "Obsidian" > /dev/null 2>&1` — exit 0 means running, non-zero means offline.

**Tag-based (primary when Obsidian is running):**
- Match current story/topic/command against the Tags table from README
- For each matching tag, run `obsidian search "query=tag:<tag>"` — returns all notes with that tag
- Prioritise: `decisions` > `concepts` > `research` within tag results

**Keyword-based:**
- If Obsidian is running: `obsidian search query="<key terms from current story/topic/command>"`
- If vault offline: load relevant `_index.md` files and scan descriptions

Combine results. Load at most 1-2 MOCs and 1-2 subfolder `_index.md` files, then at most 3 notes in full. Never exceed 5 notes total.

If no notes are clearly relevant: output only the root README summary. Do not load indexes or individual notes.

### Step 4 - Output Knowledge Context block

Always output the Tags table and MOC list — these are the session's discovery surfaces.

When notes were pre-loaded:
```
**Knowledge Context**

**Tags** (search with `obsidian search "query=tag:<name>"` on demand):
| Tag | Covers |
|-----|--------|
(copy Tags table from README)

**Available MOCs:**
- [MOC Title](knowledge/_MOC/slug.md) - one-line description
(list all MOCs from README, or "(none yet)" if empty)

**Pre-loaded for this session:**
- [Note Title](knowledge/decisions/file.md) - one-line summary
```

When vault exists but no notes matched:
```
**Knowledge Context**

**Tags** (search with `obsidian search "query=tag:<name>"` on demand):
(copy Tags table from README)

**Available MOCs:**
(list all MOCs)

**Pre-loaded:** none — topics in this session did not match vault content at startup
```

### Step 5 - Standing retrieval instruction

After the Knowledge Context block, append:

> Throughout this session: if a topic arises that might relate to vault content, search on demand using tags (`obsidian search "query=tag:<tag>"`) or keywords (`obsidian search query="<terms>"` or `grep -r "<terms>" knowledge/`). The Tags table above is your lookup surface — match the topic to a tag, then search by tag. Surface results only if relevant. Do not wait to be asked.

## Rules

- Read-only. Never writes to `knowledge/`
- Never load more than 5 notes in one invocation
- Skip files already loaded in this session (no duplicate loads)
- Always output the Tags table and MOC list — never omit them from the context block
- Tag-based search is preferred over keyword search when tags clearly match the topic
