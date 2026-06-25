# Reconcile Procedure

Shared discovery-classify-confirm procedure. Called by process and ingest before creating or modifying any note.

**Maintenance note:** The discovery algorithm below mirrors `bob:knowledge/SKILL.md` — same traversal, same tools. If either is updated, update the other.

---

## Phase 1: Discovery

Goal: find vault notes that might overlap with the incoming content. Collect up to 5 candidates.

1. Extract tags and key terms from the incoming content
2. Check Obsidian running: `pgrep -x "Obsidian" > /dev/null 2>&1`
3. For each matching tag, run `obsidian search "query=tag:<tag>"` (vault online) or `grep -rl "<term>" knowledge/` (vault offline)
4. Read relevant subfolder `_index.md` files (decisions, concepts, research, patterns) — scan descriptions for overlap
5. Follow any index entry links that look related — read the note if the description matches
6. Collect candidates (max 5). If none found after full traversal: candidate list is empty (proceed to create-new)

---

## Phase 2: Classify

LLM reads candidates against incoming content and assigns one disposition per candidate pair:

| Disposition | When to use |
|-------------|-------------|
| **merge** | Same concept, significant overlap — fold incoming into the existing note |
| **enrich** | Existing note is relevant but thin/incomplete — add content or links from incoming |
| **split** | Existing note has grown beyond atomic (>500 words, multiple distinct ideas) — decompose it |
| **create-new** | No related note found, or existing notes cover different ground |

One incoming item may produce multiple dispositions (e.g. enrich note A and create-new note B).

---

## Phase 3: Batch Confirm

Group proposed changes by type before applying. Never apply without confirmation.

**Field renames, cross-link additions:**
Show as a batch: "Apply all N changes? [y/n/review each]"

**Merges and enrichments:**
Show side-by-side (existing note summary + proposed addition). Confirm individually or as a group:
"Apply merge: [title]? [y/n]"

**Splits:**
Always individual review — structural risk. Show the proposed decomposition (original note → N atomic notes with titles and target files). Confirm each piece separately.

**Create-new:**
Show the proposed note (title, type, tags, content outline). Confirm before writing.

---

## Output

After batch confirm, return to the calling mode (process or ingest) with:
- List of confirmed actions (what was applied)
- List of skipped/deferred items
- Any new tags proposed (caller adds to README Tags table)
