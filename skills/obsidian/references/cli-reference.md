# Obsidian CLI Reference

Official CLI shipped with Obsidian 1.12.7+. Requires the Obsidian desktop app (auto-launches if not running on first command).

## Setup

| Platform | Path after registration |
|---|---|
| macOS | `/usr/local/bin/obsidian` (symlink, requires admin) |
| Linux | `~/.local/bin/obsidian` (ensure dir is in PATH) |
| Windows | Terminal redirector added automatically |

Enable: Settings → General → Command line interface → Register CLI

## Syntax Rules

- Parameters: `key=value` format; quote values containing spaces: `file="My Note"`
- Flags: bare words, no prefix: `open`, `overwrite`, `permanent`
- Vault targeting: `vault=<name>` or `vault=<id>` as first parameter
- File resolution:
  - `path=<path>` - exact path from vault root (e.g. `path="docs/Architecture.md"`). **Always use this** for deterministic behavior.
  - `file=<name>` - wikilink-style, matches by filename without extension. Avoid - ambiguous when multiple files share a name.

## File Commands

| Command | Required | Optional | Description |
|---|---|---|---|
| `obsidian rename` | `name=<name>` | `file=`, `path=` | Rename file; updates wikilinks |
| `obsidian move` | `to=<path>` | `file=`, `path=`, `name=` | Move to folder; updates wikilinks |
| `obsidian create` | `name=<name>` | `path=`, `content=`, `template=`, `open`, `overwrite` | Create new note |
| `obsidian read` | - | `file=`, `path=` (defaults to active) | Print note content |
| `obsidian append` | `content=<text>` | `file=`, `path=`, `inline`, `open` | Append to note |
| `obsidian prepend` | `content=<text>` | `file=`, `path=`, `inline` | Prepend to note |
| `obsidian delete` | - | `file=`, `path=`, `permanent` | Move to trash (or delete permanently) |
| `obsidian open` | - | `file=`, `path=`, `newtab` | Open note in Obsidian |
| `obsidian search` | `query=<text>` | `limit=<n>` | Search vault (uses Obsidian index) |

## Knowledge Graph Commands

| Command | Required | Optional | Description |
|---|---|---|---|
| `obsidian backlinks` | - | `file=`, `path=`, `counts`, `total`, `format=json\|tsv\|csv` | List all notes that link to this file |
| `obsidian links` | - | `file=`, `path=` | List outgoing links from a file |
| `obsidian orphans` | - | - | List files with no incoming links |
| `obsidian deadends` | - | - | List files with no outgoing links |
| `obsidian unresolved` | - | - | List unresolved (broken) links in vault |
| `obsidian tags` | - | `sort=count`, `counts` | List all tags; sort by frequency |

Examples:
```bash
obsidian backlinks path="docs/architecture.md"     # who links here?
obsidian search query="authentication" limit=10    # find related notes
obsidian tags sort=count counts                    # tag inventory
obsidian unresolved                                # find broken links
```

## Vault Info

| Command | Description |
|---|---|
| `obsidian vault` | Show active vault name, path, file count, size (TSV output) |
| `obsidian vaults` | List all known vaults |

Extract a single field directly:
```bash
obsidian vault info=path     # returns just the path, e.g. /Users/bfr/dev/ai/building-bob
obsidian vault info=name     # returns just the vault name
obsidian vault info=files    # returns just the file count
```

Validate active vault matches project root:
```bash
vault_path=$(obsidian vault info=path 2>/dev/null)
```

## Workspace & Context Commands

| Command | Description |
|---|---|
| `obsidian file` | Active file info: path (vault-relative), name, extension, size, timestamps (TSV) |
| `obsidian file file=<name>` | Same info for a named file - resolves vault-relative path |
| `obsidian workspace` | Workspace tree (main/left/right panes) |
| `obsidian tabs` | Flat list of all open tabs with type and filename (no paths) |
| `obsidian recents` | Recently opened files as vault-relative paths (excludes currently active file) |
| `obsidian outline` | Show headings for active (or specified) file |

### Get currently active file path

```bash
obsidian file | awk -F'\t' '/^path/{print $2}'
```

### Get all currently open markdown file paths (reliable)

`obsidian tabs` returns names without paths and cannot disambiguate multiple files sharing the same name. Use `eval` instead - it queries Obsidian's workspace API directly:

```bash
obsidian eval code="app.workspace.getLeavesOfType('markdown').map(l => l.view?.file?.path).filter(Boolean).join('\n')" | sed 's/^=> //'
```

Returns vault-relative paths for every open markdown tab, one per line. Correctly handles multiple files with the same name (e.g. several `_index.md` in different folders).

Combined with vault path for absolute paths:
```bash
vault=$(obsidian vault info=path)
obsidian eval code="app.workspace.getLeavesOfType('markdown').map(l => l.view?.file?.path).filter(Boolean).join('\n')" | sed 's/^=> //' | while read rel; do
  echo "$vault/$rel"
done
```

Note: `recents` / `recents ids` returns recently opened files in order (vault-relative paths) but is history-based, not workspace-based. Use `eval` for what is currently open.

## Metadata Commands

| Command | Required | Optional | Description |
|---|---|---|---|
| `obsidian property:set` | `name=<name>` `value=<value>` | `file=`, `path=` | Set a frontmatter property |

Example:
```bash
obsidian property:set path="projects/X/_index.md" name="status" value="in-progress"
```

## Content Formatting

- Newlines: use `\n` in `content=` values
- Tabs: use `\t`
- Example: `obsidian create name="Meeting Notes" content="# Meeting\n\n- Item 1\n- Item 2"`

## Global Flags

- `--copy`: copy command output to clipboard
- `obsidian` alone: enter TUI interactive mode (autocomplete, command history, reverse search)

## Link Update Behavior

`rename` and `move` update wikilinks **only if** "Automatically update internal links" is enabled:
Settings → Files & Links → Automatically update internal links

If this setting is off, the operation succeeds silently but all links to the file will be broken.

## Vault Default Behavior

The CLI defaults to the vault whose root matches the current working directory. If CWD is not a vault root, it falls back to the last active vault in Obsidian. For reliability in scripted contexts, always specify `vault=<name>` explicitly when operating outside a vault root.

## Known Issues

- **Homebrew macOS**: The Homebrew cask creates a symlink into the `.app` bundle that fails when called from outside the bundle context. Use the direct path `/Applications/Obsidian.app/Contents/MacOS/obsidian` or re-register the CLI via Settings.
- **First command delay**: If Obsidian is not running, the first CLI call auto-launches the app. Wait for startup before chaining additional commands.
- **Bulk operations are slow**: Each command is an IPC round-trip through the running app. Not suitable for batch-processing thousands of files.
