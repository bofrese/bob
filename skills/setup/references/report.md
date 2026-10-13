# Report and summary

## Status report (step 2)

Present a concise status table. No changes yet.

```
## Bob Setup - {date}

| Component              | Status          | Action needed               |
|------------------------|-----------------|------------------------------|
| projects/              | ✓ / ✗           | Create subproject            |
| knowledge/ vault       | ✓ / ✗           | Bootstrap                    |
| personal/ notes        | ✓ / ✗           | Create                       |
| .gitignore entries     | ✓ / ⚠ Partial / ✗ | Add missing entries       |
| docs/process/done-criteria.md | ✓ / ⚠ Upgrade / ✗ | Create / Patch        |
| docs/process/learnings.md | ✓ / ✗           | Create (Learn's cross-session staging log) |
| personal/interaction-profile.md | ✓ / ✗ (optional) | Offer to create      |
| Story kanbans          | ✓ / ⚠ N missing Obsidian frontmatter | Repair          |
| _index.md links        | ✓ / ⚠ N missing tasks/notes link     | Repair          |
| _index.md titles       | ✓ / ⚠ N missing title frontmatter    | Repair          |
| Story folder structure | ✓ / ⚠ N missing _notes.md/_kanban.md/tasks/sessions | Repair   |
| Kanban new-line-trigger | ✓ / ⚠ N missing                     | Repair          |
| Session files at story root | ✓ / ⚠ N found                   | Move to sessions/ |
| AGENTS.md bob block    | ✓ / ⚠ Stale / ✗ | Write block, add CLAUDE.md import |
| bob 3.x names          | ✓ / ⚠ N hits (M fixable) | Fix M; list the rest  |
| Orphan .md files       | N found         | Review manually              |
| Ponytail plugin (recommended) | ✓ installed / ✗ not installed | Recommend install |
| Obsidian vault (.obsidian/) | ✓ present / ✗ absent | Offer bootstrap from obsidian-for-bob |
| Obsidian Skills plugin (recommended) | ✓ installed / ✗ not installed | Recommend install |
| graphify (recommended) | ✓ installed vX.Y.Z / ⚠ below 0.9.11 / ✗ not installed | Recommend install/upgrade |
| graphify graph + hook | ✓ built + hook / ⚠ built, no hook / ✗ not built | Offer build + hook |
| .graphifyignore corpus scope | ✓ current / ⚠ stale / ✗ absent | Write/refresh scope |
| Mermaid CLI (recommended) | ✓ installed vX.Y.Z / ✗ not installed | Recommend install |
```

Recommendations only - never install anything automatically.

**If Ponytail is not installed:** a "lazy senior developer" reviewer that the `review` skill uses for an over-engineering pass. Install with `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` - more at https://ponytail.dev.

**If Obsidian Skills is not installed:** authoring skills for Obsidian-flavored markdown, Bases, and Canvas - bob is optimized for Obsidian and produces better-formatted notes when it is present. Install with `/plugin marketplace add kepano/obsidian-skills` then `/plugin install obsidian@obsidian-skills`. Note: bob's own `obsidian` skill remains authoritative for vault mutations (rename/move) - its approval-gated workflow takes precedence over the plugin's generic `obsidian-cli` skill.

**If graphify is not installed (or older than 0.9.11):** graphify builds a persistent code knowledge graph that the hub's code-graph loader queries so engineering phases orient from real structure instead of blind exploration. It is a separate third-party tool - recommend, never silent-install. Install with `uv tool install graphifyy` (the PyPI package is `graphifyy`, double-y, not a typo); upgrade a too-old copy with `uv tool upgrade graphifyy`. bob requires **>= 0.9.11**. Everything degrades gracefully when it is absent and bob works without it.

**If the Mermaid CLI is not installed:** bob writes Mermaid diagrams in designs, plans and architecture notes, and Mermaid fails silently in many renderers. With `mmdc` installed, commands validate a file before saving: `mmdc -q -i <file.md> -o <scratch>/out.md` renders every Mermaid block and exits non-zero on a syntax error. Install with `npm install -g @mermaid-js/mermaid-cli` (needs Node.js). Without it, diagrams are checked by eye only.

If everything is ✓: say "All bob infrastructure is present and up to date. Nothing to do." and stop.

Otherwise: list what will change and ask "Ready to apply?" - one confirmation covers everything.

## Summary (step 6)

One compact table:

| Item | Result |
|------|--------|
| projects/ | Created `projects/{name}/` / Already present |
| knowledge/ | Bootstrapped / Already present |
| personal/ | Created / Already present |
| .gitignore | Added N entries / Already complete |
| done-criteria | Created / Added N sections: {list} / Already up to date |
| learnings.md | Created / Already present |
| interaction-profile.md | Created / Declined / Already present |
| Story kanbans | Repaired N / Already correct |
| _index.md links | Repaired N / Already correct |
| _index.md titles | Repaired N / Already correct |
| Story folder structure | Repaired N / Already correct |
| Kanban new-line-trigger | Repaired N / Already correct |
| Session files at story root | Moved N / None found |
| AGENTS.md bob block | Written / Updated / Already current |
| bob 3.x names | Fixed M, N left to fix by hand: {file:line list} / None found |
| Orphan files | N found (see above) / None |
| Ponytail plugin | Installed / Recommended (not installed) |
| Obsidian vault | Bootstrapped / Declined / Already present |
| Obsidian Skills plugin | Installed / Recommended (not installed) |
| graphify | Installed vX.Y.Z / Recommended (install or upgrade to >= 0.9.11) |
| graphify graph + hook | Offered build/hook / Already built / N/A (not installed) |
| .graphifyignore corpus scope | Written / Refreshed / Unchanged / N/A (not installed) |
| Mermaid CLI | Installed vX.Y.Z / Recommended (not installed) |

List any manual steps remaining (e.g., Obsidian wikilinks setting).
