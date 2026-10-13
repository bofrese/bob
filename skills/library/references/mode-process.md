# Process Mode

Processes `knowledge/_INBOX/` items into atomic notes, using reconcile to prevent duplicates.

## Pre-flight: Inbox Assessment

1. List all files in `knowledge/_INBOX/` (excluding `_processed/`). If empty: "Inbox is empty." Stop.
2. Count files and estimate total tokens (use file size as proxy: ~250 words/KB ≈ ~330 tokens/KB)
3. Decide processing mode:
   - Total estimated tokens **< 20K**: process all inline, sequentially (go to Processing Loop below)
   - Total estimated tokens **≥ 20K**: bundle into batches of ~5K tokens each, go to Batch Processing below

## Processing Loop (inline)

For each file, in order:

1. Read the file
2. Identify distinct atomic concepts it contains - one inbox file may yield multiple notes
3. For each candidate note: read `references/reconcile.md` and run the reconcile procedure
4. After reconcile returns confirmed actions, execute each:
   - **create-new**: write note using the Note Format below; append entry to subfolder `_index.md`; check existing MOCs and add entry if applicable; check `_suggestions.md` for related MOC candidates
   - **merge**: fold incoming content into the existing note (read it, append or rewrite section, confirm before writing)
   - **enrich**: add content or links to existing note, confirm before writing
   - **split**: decompose existing note per reconcile's proposal, confirm each piece
5. Assess the original inbox file:
   - Authoritative source (article, research paper, major spec): move to `sources/` (move per the Rules in `SKILL.md`). Name it: `{YYYY-MM-DD}-{short-slug}.{ext}`. Choose a topic subfolder if 3+ source files already cover the same topic; otherwise file flat. Never use typed folder names (decisions/, practices/, research/) in sources/. Add `resource: sources/{path}` to atomic notes derived from it.
   - Ephemeral capture (rough notes, quick thought): move to `_INBOX/_processed/` (move per the Rules in `SKILL.md`).
6. Append any new patterns noticed to `_suggestions.md` (MOC candidates, tag inconsistencies, schema gaps)

## Batch Processing (≥ 20K tokens)

1. Bundle inbox files into batches of ~5K tokens each
2. Process batches **sequentially** - items on the same subject must see prior decisions
3. If the agent can delegate to subagents, give each batch to one; otherwise process the batches inline in sequence. Each batch gets:
   - Its bundle of inbox files
   - A vault state summary (folder counts, recent index entries)
   - A **summary of prior batch results** (type + title + disposition only - not full proposal text, to prevent context growth)
4. Collect all confirmed actions from each batch before starting the next

## Post-processing

1. Update `knowledge/README.md` Tags table if new tags were added during this run
2. Call `log_append.py` to record the run:
   ```bash
   python3 <skill-dir>/scripts/log_append.py process "Inbox: N items. Merged X, enriched Y, created Z new. W deferred."
   ```
3. Report: files processed, notes created/merged/enriched, moved to sources, moved to `_processed/`

## Note Format

```markdown
---
title: <title>
type: <decision|concept|research|practice>
tags: [tag1, tag2]
timestamp: YYYY-MM-DDThh:mm:ssZ
story: <STORY-ID>  # if captured in story context
evidence:          # required for decision/pattern; optional for concept/research
  - path or experiment reference
status: proposed | validated | superseded
last_validated: YYYY-MM-DD
supersedes: optional-note-link
---

# <title>

[Content - atomic, self-contained, 5-15 lines]

**Why it matters:** [one sentence]
```

`decision` and `practice` notes require `evidence` and `status`. A claim with no `evidence` entries is an inference, not an observation - set `status: proposed`, never `validated`, until it has one. `last_validated` should be set to the processing date on creation and bumped whenever the claim is re-confirmed. Full field definitions: "Evidence and Validation Frontmatter" in `knowledge/_schema.md` (`assets/_schema.md`).

## Conflict surfacing

Before creating a new `decision` or `practice` note, check whether an existing note in the same subfolder makes a conflicting claim (reconcile's job already covers exact/near-duplicate detection - this is about a *contradicting*, not duplicate, claim). If a conflict is found:

- Do not silently pick a side or overwrite the existing note.
- Surface both claims to the user: the existing note's claim + `status`/`last_validated`, and the incoming claim + its evidence.
- Ask which one is current. If the incoming claim wins, set the old note's `status: superseded` and add `supersedes` on the new note pointing back to it - do not delete the old note.
- If genuinely uncertain which is current, leave both as `status: proposed` and note the open conflict in `_suggestions.md` for a human to resolve later - this is the one case where an unresolved conflict is an acceptable outcome for this run.

Retrieval (the hub's `project-knowledge.md`) prefers `validated` notes over `proposed`/`superseded` ones and when two `validated` notes still disagree, reports both, leading with the more recent `last_validated`. It never drops either silently.

## Rules

- Run reconcile before creating any new note - no exceptions
- Tags: read the Tags table in `knowledge/README.md` first. If no existing tag fits, propose a new tag with a description, get confirmation, add to README Tags table before using
- Never delete files - move to `_INBOX/_processed/` or `sources/` only
- For all moves: follow the move rule in `SKILL.md`.
- Never add a note to any index without user confirmation
- Filenames: kebab-case, no date prefix for processed notes; `YYYY-MM-DD-slug.md` for inbox only
- Never mark a `decision`/`practice` note `status: validated` without at least one `evidence` entry
- The `learn` skill may recommend consolidation, supersession, or deletion of stale notes, but must never perform destructive vault cleanup without confirmation - process mode always asks before merging, enriching, splitting, or changing `status` on an existing note
