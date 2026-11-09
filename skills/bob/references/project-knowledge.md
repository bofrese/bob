# Project knowledge

One loader for what the project already knows. Run it once the scope is clear. For each source: read the index first, then load only the files that match the scope (files, paths, concepts and terms the work touches). Never load a whole folder. Skip a missing source silently unless noted.

Never load `docs/explainers/`. Explainer pages are for humans, can be out of date and are never a source of truth.

## Domain: `docs/domain/`

Read `docs/domain/README.md`. Load the concept files for terms the work uses. Use the terms as defined there, in artifacts and in code names. A term that seems to conflict with the code is a question for the user.

## Architecture: `docs/architecture/`

Read `docs/architecture/README.md`. Load the concept notes the work touches and the pattern notes for the kinds of problem it solves. `established` patterns are the default approach. Departing from one, or adding a competing variant, is a design question for the human.

## Guidelines: `docs/guidelines/`

Read `docs/guidelines/README.md`. Load the guidelines whose "Applies When" matches: file extensions, paths, concepts, the current phase. Load `markdown.md` if it exists. Load `mermaid.md` if it exists and you will draw a diagram. If a loaded guideline needs a tool that is not installed, offer to install it before running code.

Folder missing: say once "No project guidelines found. The `guidelines` skill creates them."

## Product: `docs/product/`

Load the product files your phase skill lists. For scope questions without such a list, read `docs/product/README.md` or `docs/product/vision.md`.

## Knowledge vault: `knowledge/`

Read-only. The `library` skill manages the vault.
1. Read `knowledge/README.md`: folders, the Tags table (the only canonical tag list) and the MOC list.
2. Find notes. If this project is the active Obsidian vault (`obsidian vault info=path` equals the project root): `obsidian search "query=tag:<tag>"` for matching tags, and `obsidian search query="<terms>"`. Otherwise read the relevant `_index.md` files or `grep -r "<terms>" knowledge/`.
3. Prefer tag search when a tag clearly matches the topic. No note clearly relevant: load no index or note, report only the Tags table and MOC list. Otherwise load at most 1-2 MOCs, 1-2 `_index.md` files and 3 notes, 5 files at most. Load only notes that bear on what this phase decides. Prefer `decisions` over `concepts` over `research`. Notes from `decisions/`, `practices/`, `research/`, `concepts/` only; `sources/` is reached through a note's `resource:` field.
4. Status: prefer `validated` notes. Mark `proposed` notes as proposed. Skip `superseded` notes unless their chain matters. Say when `last_validated` looks old. Two validated notes that disagree: load both and report the conflict, leading with the more recent `last_validated` as the likelier one. Never drop either silently.
5. Report one short block: the Tags table, the MOC list, the notes loaded (with status), any conflicts.

For the rest of the session, when a topic may relate to the vault, search it by tag or keyword without being asked. Mention results only when relevant.
