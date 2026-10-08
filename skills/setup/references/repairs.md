# Repairs and bootstrap (step 3)

Execute only items marked missing or partial. Skip items already present.

**projects/ missing:**

Try to derive a subproject name: check `package.json` `.name`, git remote URL, or current directory name. Offer the derived name as a default. Ask: "Subproject name? (default: {derived})"

Create `projects/{name}/stories/` and `projects/{name}/_kanban.md` using the Bootstrap procedure in the hub's `references/story-files.md` (project-level columns, `prefix`, `last-id: "000"`, `new-note-folder`, `new-line-trigger`).

**Story kanbans missing Obsidian frontmatter:**
For each story `_kanban.md` missing `kanban-plugin: board` frontmatter: prepend the frontmatter block (`kanban-plugin: board`, `title: [STORY-ID] Tasks`) and append the `%% kanban:settings %%` block with `new-note-folder` pointing to the story's `tasks/` folder and `new-line-trigger: shift-enter`. Existing column content is preserved.

**`_index.md` files missing tasks/notes link:**
For each story `_index.md` missing the `##### 📋 [Tasks](_kanban.md)` line: insert it after the opening description paragraph.

**`_index.md` files missing title frontmatter:**
For each story `_index.md` missing `title:`: add `title: "[STORY-ID] Story: [Story Name]"` to the frontmatter block, reading the story name from the `# [STORY-ID] - [Story Name]` heading.

**Story folders missing `_notes.md`, `_kanban.md`, `tasks/`, or `sessions/`:**
For each story missing any of these, create the missing pieces using the templates in the hub's `references/story-files.md` (Story Index, `_notes.md`, story-level kanban templates). Never overwrite files that already exist.

**Kanban files missing `new-line-trigger`:**
For each `_kanban.md` whose settings block lacks `new-line-trigger`, add `"new-line-trigger":"shift-enter"` to the existing settings JSON. Preserve all other settings keys.

**Session files at story root:**
For each dated file (`YYYY-MM-DD-*.md`) found directly in a story folder: move it into that story's `sessions/` subfolder (create if missing), then update every link to it - in the story's `_index.md` history table, `_kanban.md` cards, and cross-links between session files - to `sessions/[filename]`.

**knowledge/ missing:**

Run the `library` skill's bootstrap: `python3 ../library/scripts/bootstrap.py` (relative to this skill's folder) from the project root. It also covers the `personal/` and `.gitignore` items below.

**personal/ missing:**

Create `personal/daily/` and `personal/weekly/`.
Write `personal/scratchpad.md` if it doesn't exist:
```markdown
---
title: Scratchpad
---
# Scratchpad
```

**.gitignore entries missing:**

For each of `knowledge/_INBOX/` and `personal/` not already present in `.gitignore`: append to `.gitignore`.

**graphify corpus scope and provisioning (only when graphify is installed):**

Skip this entire item if `graphify` is not installed - the status report recommendation already covers that case, and there is nothing to consume a scope file yet. If the installed version is below `0.9.11`, print the upgrade recommendation (`uv tool upgrade graphifyy`) and skip the build/hook offers, but still write the scope file below.

1. **Write / refresh `.graphifyignore`** at the project root. This is bob-managed and idempotent: regenerate the block between the managed markers on every run so the scope tracks folders as they come and go; preserve anything the user added outside the markers. `.graphifyignore` uses gitignore semantics (merged with `.gitignore`, `!` negation, last-match-wins), so excluding the historical tiers leaves everything else (code + authoritative content) in the corpus. Add the `website/dist/` line **only when `website/src/` exists** (the b2 website signal) so the generated site does not duplicate its source; never add website lines otherwise (no bob-to-b2 coupling). Content:

   ```gitignore
   # >>> bob:graphify corpus scope (managed by /bob:setup - regenerated on each run) >>>
   # gitignore semantics: merged with .gitignore, ! negates, last-match-wins.
   # A .graphifyinclude allowlist can opt hidden paths back in if ever needed.
   #
   # Corpus tiers:
   #   Code                  - application/source files (kept)
   #   Authoritative content - docs/, knowledge/, website/src/ (kept)
   #   Historical (excluded) - projects/, ai/ (~74% of observed semantic cost, low authority)

   # Historical: excluded
   projects/
   ai/

   # Website: keep src/ as authoritative content, drop the generated build (b2 only)
   website/dist/
   # <<< bob:graphify corpus scope <<<
   ```

2. **Offer to build the graph** - only if `graphify-out/graph.json` does not yet exist. Surface the first-build cost for large corpora ("large repos can be expensive: hundreds of files / millions of words on the first pass"), and note the scope file above already trims the historical tiers. Offer to run `/graphify .` (initial build) and `graphify hook install` (post-commit auto-rebuild so the graph stays fresh). Never run either without confirmation.

3. **Idempotent re-run:** if the graph already exists, do not rebuild. If the hook is missing, offer `graphify hook install`. Always refresh the managed `.graphifyignore` block so the scope stays current as project folders change.

## bob 4 entry points

**AGENTS.md bob block missing or stale, or CLAUDE.md lacks the import:** run `python3 ../bob/scripts/primer.py --agents-md --apply`. It writes the primer between `<!-- bob:start -->` and `<!-- bob:end -->` in `AGENTS.md` (read by Codex and Copilot) and never touches text outside the markers. It adds `@AGENTS.md` to `CLAUDE.md`, or creates a `CLAUDE.md` holding only that import when none exists.

**bob 3.x names found:** run `python3 scripts/rename_scan.py --fix`. It replaces only names with a replacement (for example `/bob:product-coach` to `/bob:product`, `bob:context-protocol` to `bob:bob`). List the hits marked "fix by hand" in the summary. Mode names (personas, design-brief, ...) become their skill; mention the mode in the summary so the user can add it to the text.

## Learn and personal files

**`docs/process/learnings.md` missing:** Read the Bootstrap section of the `learn` skill's `references/persistence-map.md` (`../learn/references/persistence-map.md`, relative to this skill's folder) and create the file as specified there.

**`personal/interaction-profile.md` missing:** This is optional and personal (gitignored) - never auto-create silently. Offer once: "Want a personal interaction-profile file? It lets you set your preferred verbosity/experience-level defaults once instead of restating them per session." If yes, create `personal/` (if missing) and write a minimal starter:
```markdown
---
title: Interaction Profile
---
# Interaction Profile

<!-- Personal, gitignored. Notes on your preferred interaction style - verbosity, question pacing, experience level - read by the bob hub at session start. -->
```
Ensure `personal/` is already covered by the `.gitignore` entries step above.
