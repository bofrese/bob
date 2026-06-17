---
allowed-tools: Bash(*), Read, Write, Edit
description: Quick capture to the knowledge inbox. Writes immediately to knowledge/_INBOX/ without loading context or running phases.
---

## Context
No context loading. Fast path — skip all protocol overhead. Bootstrap only if vault is absent (one-time cost).

## Process

1. If args provided: use them as content directly
2. If no args: ask "What should I remember?" — single question only
3. If `knowledge/` does not exist:
   - Inform the user: "Setting up knowledge vault first..."
   - Locate `library.md` in the same `commands/` folder as this file (the plugin install path is not guaranteed to be `bob/`). Read it and run its Bootstrap section (steps 1-7).
   - Continue with capture
4. Create slug from content: first 4-5 significant words, kebab-case, skip stop words (the, a, an, is, to, for, we, it, in, of, and, or, that, this)
5. Write `knowledge/_INBOX/YYYY-MM-DD-<slug>.md`:
   ```markdown
   ---
   title: <first line or best derived title>
   type: inbox
   created: YYYY-MM-DD
   ---

   <content verbatim or lightly cleaned up>
   ```
6. Confirm: "Saved to `knowledge/_INBOX/<filename>.md`. Run `/bob:library process` to file it."

## Rules
- No phases. No conversation beyond step 2 prompt and step 6 confirmation.
- Do not invoke context-protocol or done-criteria.
- Never modify existing notes, indexes, or README.
