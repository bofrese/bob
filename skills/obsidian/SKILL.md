---
name: obsidian
description: This skill should be used when the user asks to rename or move a markdown file, when Claude is about to execute mv or git mv on any .md file, when searching for notes or content in an Obsidian vault, when the user mentions "obsidian", "wikilinks", "internal links", "vault", or "search vault", or when file operations on .md files need to preserve link integrity.
version: 0.2.0
---

# Obsidian Vault Operations

Manages markdown file operations (rename, move) and vault search through the official Obsidian CLI. Direct filesystem moves (`mv`, `git mv`) on `.md` files are never used - they break internal links silently. All operations route through the Obsidian app's internal API.

## Prerequisites

Verify both conditions before any operation. Stop immediately if either fails.

### 1. Correct Vault is Active

```bash
vault_path=$(obsidian vault info=path 2>/dev/null)
```

Compare `vault_path` to `$PWD`:

- **Empty result**: CLI is not in PATH. **Stop:**
  > "The `obsidian` CLI is not available. Enable it in Obsidian: Settings → General → Command line interface → Register CLI. Requires Obsidian 1.12.7+."

- **`vault_path` ≠ `$PWD`**: Wrong vault is active. **Stop:**
  > "Active Obsidian vault is `<vault_path>` but current project is `<PWD>`. Open this project folder as a vault in Obsidian first."

- **`vault_path` = `$PWD`**: Correct vault confirmed. Continue.

This single check validates that the CLI is available, Obsidian is reachable, and the active vault matches the project root. Do not fall back to plain `mv` on failure.

### 2. File Path is Valid

Before running any operation, confirm the source file exists at the given path:

```bash
ls "<vault-relative-path>"
```

If the file doesn't exist: stop and report the correct path before proceeding.

## Operations

Always use `path=` with the vault-relative path (relative to project root). Never use `file=` - wikilink-style resolution is ambiguous when multiple files share a name.

### Rename (same folder, new name)

```bash
obsidian rename path="folder/old-name.md" name="new-name"
```

- `path=` is the current file path relative to vault/project root, including `.md`
- `name=` is the new filename **without** `.md` extension

### Move (change folder)

```bash
obsidian move path="folder/file.md" to="new-folder"
```

- `to=` is the destination folder path relative to vault root (no filename, no extension)

### Rename and move in one step

```bash
obsidian move path="old-folder/old-name.md" name="new-name" to="new-folder"
```

## Workflow

Every file operation follows this exact sequence:

1. **Run prerequisite checks** - vault detection, CLI check, file path valid; stop if any fails
2. **Check backlinks** - show what currently links to the file:
   ```bash
   obsidian backlinks path="folder/file.md"
   ```
   Report the count and list to the user. Zero backlinks means a safe rename; many backlinks means more will be updated.
3. **Show the plan** - the exact `obsidian` command, the backlink count, what will change
4. **Wait for explicit approval** - never execute without the user confirming
5. **Execute** the command
6. **Verify** - confirm the file exists at its new path with `ls`

**Never skip the approval step.** A rename propagates across the whole vault and cannot be easily undone from the CLI.

## Link Update Requirement

Link updates only fire if **Settings → Files & Links → Automatically update internal links** is enabled in Obsidian.

Before the first operation in a project, warn the user to verify this setting is on. If it is off, the rename/move will succeed but all wikilinks pointing to the file will break silently.

Note: Obsidian's auto-update applies to **wikilinks only** (`[[note-name]]`). Standard markdown links (`[text](path/file.md)`) are not updated by the CLI. If the vault mixes link styles, check for broken standard links manually after rename.

## Search

Use vault search to find notes before reading them - faster than grep for large vaults.

```bash
obsidian search query="authentication flow" limit=10
```

- Returns matching note titles and excerpts
- Uses Obsidian's index (faster than filesystem grep)
- Use to locate relevant notes before loading them into context
- Combine with `obsidian read path="..."` to load the content of specific results

## Workspace State

Commands for reading what is currently open or recently visited in Obsidian. Used by the `bob:story-context` skill to detect the active story without user input.

### Active file path

```bash
obsidian file | awk -F'\t' '/^path/{print $2}'
```

Returns the vault-relative path of the currently active file.

### All open markdown tab paths

```bash
obsidian eval code="app.workspace.getLeavesOfType('markdown').map(l => l.view?.file?.path).filter(Boolean).join('\n')" | sed 's/^=> //'
```

Returns one vault-relative path per line for every open markdown tab. Use this in preference to `obsidian tabs`, which returns filenames only and cannot disambiguate files that share a name (e.g. multiple `_index.md` files).

### Recently opened files

```bash
obsidian recents
```

Returns recently opened files as vault-relative paths, most recent first. History-based — reflects past visits, not current open tabs.

## Setup Instructions (for users with no vault)

1. Open Obsidian
2. Click "Open folder as vault" and select the project root
3. This creates `.obsidian/` at the project root
4. Enable CLI: Settings → General → Command line interface → Register CLI
5. Enable link updates: Settings → Files & Links → Automatically update internal links

## Hook Integration

A PreToolUse hook in the bob plugin's `settings.json` intercepts any `mv` or `git mv` command on `.md` files and blocks it, forcing the operation through this skill instead. This is automatic - no per-project configuration needed.

If the hook fires: acknowledge the block, invoke the vault/CLI checks above, then proceed through the approval workflow before running the obsidian command.

## Additional Resources

- **`references/cli-reference.md`** - Full Obsidian CLI command reference with all parameters
- **`references/obsidian-markdown.md`** - Obsidian-flavored markdown conventions: link formats, properties, callouts, tags
