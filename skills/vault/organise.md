# Organise Mode

Vault health and maintenance. Incremental by default: scopes to notes changed since last run. Full vault scan on first run or when log.md is missing.

## Step 0: Determine Scope

1. Read `knowledge/log.md` if it exists. Find the most recent `## [timestamp] organise` entry. Extract the timestamp.
2. If timestamp found:
   ```bash
   python3 bob/skills/vault/scripts/git_scope.py "<last-organise-timestamp>" knowledge
   ```
   If the list is empty: "No notes changed since last run." Stop.
3. If no timestamp (first run or log.md missing): process all notes.
4. Report scope: "N notes changed since last run." or "First run — processing all notes."

## Phase 1: Lint

Run lint on scoped files:
```bash
python3 bob/skills/vault/scripts/lint.py knowledge
```

Filter output to scoped files only. For each issue found:
- **Missing required field** — surface as a warning, propose adding the field
- **Old field name** (`source:` or `created:`) — batch with other field renames for batch confirm below
- **Broken link** — surface as a warning, do not auto-fix

Group all field renames into a batch: "Rename N old field names across M notes? [y/n/review each]"

## Phase 2: Vault Integrity Audit

Always run on scoped files:

a. **Inbox stubs in typed folders** — find `.md` files in `decisions/`, `concepts/`, `research/`, `patterns/` with `type: inbox` in frontmatter. Move each to `_INBOX/_processed/` using `obsidian move` (vault active) or `mv` (vault offline).

b. **Orphaned notes** — compare scoped files on disk against entries in `_index.md`. Files present on disk but absent from the index are orphaned. Present proposed index entries and add after confirmation.

c. **README consistency** — verify the Folders table lists all typed subfolders. Verify `_schema.md` tag governance rule points to README (no mirrored tag list). Rebuild README if Folders table is incomplete.

d. **Dead resource: references** — scan scoped notes for `resource:` frontmatter values. For each, verify the referenced path exists. Report dead references (do not auto-fix — ask user).

Present audit findings. If all clean, say so and continue.

## Phase 3: Active Maintenance

1. Read `knowledge/_suggestions.md` as the agenda. If empty: note "No pending suggestions."
2. For each agenda item: load relevant vault context and decide action
3. For each structural change (new MOC, tag rename, type fix, schema update): show proposed change and wait for confirmation before executing

4. **Active librarian maintenance** (propose each action, confirm before executing):
   a. **Cross-linking** — for scoped notes, scan for related notes sharing tags or overlapping keywords. Propose adding relative markdown links where they would aid discovery. Show candidate pairs before adding.
   b. **Tag consistency** — run `grep -rh "^tags:" knowledge/decisions/ knowledge/concepts/ knowledge/research/ knowledge/patterns/ 2>/dev/null` to collect all used tags. Read the Tags table from `knowledge/README.md`. For each tag found in notes but absent from the README table: either propose adding it with a description (if it names a genuinely new domain) or propose renaming it to the closest canonical tag (if it overlaps an existing one). Use `obsidian search "query=tag:<old-tag>"` (vault active) or `grep -rl "<old-tag>" knowledge/` to find all affected notes. After any additions or renames, update `knowledge/README.md` Tags table only.
   c. **Sources hierarchy** — if `sources/` contains 3+ ungrouped files clearly sharing a topic, propose creating a topic subfolder and moving them via `obsidian move`.
   d. **MOC candidates** — if 4+ notes share tags or topic keywords not yet covered by an existing MOC, append to `_suggestions.md`: `MOC candidate: <topic> (N notes)`.

5. If Tags table, Folders table, or MOC list changed: rebuild root `knowledge/README.md`
6. Clear resolved items from `_suggestions.md`; keep unresolved with a note

## Step 4: Log and Report

Call `log_append.py`:
```bash
python3 bob/skills/vault/scripts/log_append.py organise "Changed since last run: N notes. Updated X field names, added Y cross-links."
```

Report changes made.

## Rules

- Scope to changed files only (git_scope.py); fall back to all notes if log.md missing
- For all moves: use `obsidian move` if vault active, fall back to `mv` (warn user: backlinks will not be updated)
- Never auto-fix dead references — surface them and ask
- Propose every structural change before executing
