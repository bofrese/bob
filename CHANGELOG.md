# Changelog

## 4.0.0

Skills only. Every bob phase is one Agent Skills spec-compliant skill. The listing drops from 58 entries to 29.

### Added
- `bob` hub skill with the start and finish checklists every phase shares. Replaces the eight protocol skills and `pm`.
- SessionStart primer hook (`hooks/hooks.json`, `skills/bob/scripts/primer.py`): in a bob project, every session starts with the pointer to the hub.
- `setup` writes a marked bob block into `AGENTS.md` (read by Codex and Copilot) and makes `CLAUDE.md` import it.
- `setup` upgrade scan (`rename_scan.py`): finds 3.x names in `CLAUDE.md`, `AGENTS.md`, `docs/process/*.md` and `docs/guidelines/`, reports the replacement, offers to fix.
- `scripts/check.py`: structural validator and generator of the README skill table.
- Selftests for the vault scripts, `story.py`, `gather.py` and others.

### Changed
- Text style moved to the separate `plain-writing` plugin, now a dependency. `skills/bob/references/writing.md` keeps only the artifact shape (TL;DR, icons, evidence).
- `commands/` removed. Slash commands are now the skills themselves (`/bob:plan` still works).
- Merged skills: product modes in `product`, design modes in `brand-design`, `library` (vault plus library).
- Story resolution asks no confirmation when the story is named or already active.
- `learn` and `review-skill` write reports into the current project (story `sessions/` or `docs/process/`), not into the plugin directory.

### Rename map

| Old | New |
|---|---|
| product-coach, product-vision, personas, problem-space, validation-plan, business-plan, positioning | `product` (mode) |
| design-brief, art-director | `brand-design` (mode) |
| new-command, review-command | `new-skill`, `review-skill` |
| improve-command | `learn` (scoped mode) |
| pm | `bob` |
| create-prompt | removed |

The deleted protocol skills map to the hub (`context-protocol`, `story-context`, `done-criteria`, `work-routing`, `project-tracking`, `domain-knowledge`, `writing`, `knowledge`, `code-graph`), `library` (`vault`), `implement` (`design-signals`), `product` (the business principles) and `new-skill` (`prompt-engineering`).

### Removed
- The `gemini` agent, the `create-prompt` command, all of `commands/`.
- `ai/reviews/` (moved out of the plugin).
- `settings.local.json`, `settings.json` (the guard moved to `hooks/hooks.json`).

### Upgrading from 3.x
Run `/bob:setup` in each project. Project file layout (`docs/`, `projects/`, `knowledge/`) is unchanged.

### Fixed (from 3.1.1)
- The markdown-move guard blocked `mv` in every project. It now blocks only when the project has `.obsidian/` and the `obsidian` CLI is on PATH, and matches `mv` / `git mv` only as a command word.
- The obsidian skill no longer forbids plain `mv` where Obsidian is absent.
- Review reports no longer ship inside the plugin.
