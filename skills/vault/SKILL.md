# bob:vault

Vault management controller. Receives a mode from the invoking command (`/bob:library`) and loads only the relevant sub-file for that mode.

## Mode Routing

Check the mode passed by the invoking command:

| Mode | Action |
|------|--------|
| `process` | Read `skills/vault/process.md` and follow it |
| `ingest` | Read `skills/vault/ingest.md` and follow it |
| `organise` | Read `skills/vault/organise.md` and follow it |
| `bootstrap` | Read `skills/vault/bootstrap.md` and follow it |
| `status` | Run Status inline (see below) |

If no mode passed or unrecognised mode: run Status.

## Status (inline)

1. Count: inbox items (files in `knowledge/_INBOX/` excluding `_processed/`), files per typed subfolder, MOC count, source files, pending suggestions (non-empty lines in `_suggestions.md` after the heading), tag count from README Tags table
2. Show last modified date of `knowledge/README.md`
3. Present summary and ask what to do next
