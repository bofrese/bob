---
name: obsidian
description: Bob's Obsidian vault operations - moves and renames .md files so links stay intact (Obsidian CLI, or a link-rewriting script without it), and searches the vault. Use before any mv or git mv of a markdown file, or when the user mentions Obsidian, wikilinks, internal links or vault search.
license: Apache-2.0
---

# Obsidian Vault Operations

Manages markdown file operations (rename, move) and vault search through the official Obsidian CLI. Direct filesystem moves (`mv`, `git mv`) on `.md` files are never used - they break internal links silently. Moves go through the Obsidian app when it runs this project as the active vault, otherwise through `scripts/md_move.py`, which moves the file and rewrites the relative markdown links to and from it.

## Prerequisites

### 1. Pick the mover

```bash
vault_path=$(obsidian vault info=path 2>/dev/null)
```

Compare `vault_path` to `$PWD`:

- **`vault_path` = `$PWD`**: use the `obsidian` commands under Operations.
- **Anything else** (CLI missing, Obsidian closed, another vault active): use the script fallback, without asking the user to open Obsidian. It covers markdown links, not `[[wikilinks]]`; if the project uses wikilinks, say so and offer to wait while the user opens the vault instead.
  ```bash
  python3 <skill-dir>/scripts/md_move.py "<from.md>" "<to-folder/ or to.md>" --dry-run   # plan: files whose links change
  python3 <skill-dir>/scripts/md_move.py "<from.md>" "<to-folder/ or to.md>"             # execute (git mv when tracked)
  ```

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

1. **Run prerequisite checks** - pick the mover, file path valid; stop if the file is missing
2. **Check backlinks** - show what currently links to the file: `obsidian backlinks path="folder/file.md"`, or the script's `--dry-run` output.
   Report the count and list to the user. Zero backlinks means a safe rename; many backlinks means more will be updated.
3. **Show the plan** - the exact command, the backlink count, what will change
4. **Wait for explicit approval** - never execute without the user confirming
5. **Execute** the command
6. **Verify** - confirm the file exists at its new path with `ls`

**Never skip the approval step.** A rename propagates across the whole vault and cannot be easily undone from the CLI.

## Link Update Requirement

Link updates only fire if **Settings → Files & Links → Automatically update internal links** is enabled in Obsidian.

Before the first operation in a project, warn the user to verify this setting is on. If it is off, the rename/move will succeed but all links pointing to the file will break silently.

Obsidian's auto-update rewrites both wikilinks (`[[note-name]]`) and standard markdown links (`[text](path/file.md)`).

## Search

Use vault search to find notes before reading them - faster than grep for large vaults.

```bash
obsidian search query="authentication flow" limit=10
```

- Returns matching note titles and excerpts
- Use to locate relevant notes before loading them into context
- Combine with `obsidian read path="..."` to load the content of specific results

## Hook Integration

A PreToolUse hook (`hooks/hooks.json`, script `scripts/md_move_guard.py`) intercepts any `mv` or `git mv` command on `.md` files and blocks it only when `.obsidian/` exists in the project and the `obsidian` CLI is on PATH, forcing the operation through this skill instead. It does not block `md_move.py`. This is automatic - no per-project configuration needed.

If the hook fires: acknowledge the block, pick the mover above, then proceed through the approval workflow before running the obsidian command.

## Additional Resources

- **`references/cli-reference.md`** - Full Obsidian CLI command reference with all parameters, workspace state (active file, open tabs, recents) and vault setup for users with no vault
- **`references/obsidian-markdown.md`** - Obsidian-flavored markdown conventions: link formats, properties, callouts, tags
