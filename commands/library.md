---
allowed-tools: Bash(*), Read, Write, Edit
description: “Manage the project knowledge vault. Modes: process (inbox to notes), ingest (external source to notes), retrieve (search), organise (vault health), status (no args). Bootstraps knowledge/ if it doesn't exist.”
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Mode Detection

Determine mode from args:
- `process` → Vault process mode
- `ingest [url-or-file]` → Vault ingest mode
- `retrieve [query]` → Retrieve mode (inline)
- `organise` → Vault organise mode
- No args (or unrecognised args) → Status mode

If `knowledge/` does not exist: invoke the `bob:vault` skill for bootstrap mode, then enter the requested mode (or Status if no args given).

## Vault Modes

For `process`, `organise`, and `status` modes: invoke the `bob:vault` skill and pass the current mode. Follow the skill's output.

## Retrieve Mode

1. Read `knowledge/README.md`
2. If Obsidian vault is active for this project (`obsidian vault info=path 2>/dev/null` returns a path matching `$PWD`): `obsidian search query="<user terms>"` — returns excerpts, token-efficient
3. Otherwise: `grep -rl "<user terms>" knowledge/` to find files, then read relevant excerpts
4. Present matching excerpts with file paths
5. Ask if any should be opened in full

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
