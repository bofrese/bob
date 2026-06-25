---
allowed-tools: Bash(*), Read, Write, Edit
description: Quick capture to the knowledge inbox. Writes immediately to knowledge/_INBOX/ without loading context or running phases.
---

## Context
No context loading. Quick mid-session capture — skips protocol overhead. First run bootstraps the vault (one-time cost); subsequent runs are low overhead.

## Process

1. If args provided: use them as content directly
2. If no args: ask "What should I remember?" — single question only
3. If `knowledge/` does not exist:
   - Inform the user: "Setting up knowledge vault first..."
   - Invoke the `bob:vault` skill for bootstrap mode and follow it.
   - Continue with capture
4. Create slug from content: first 4-5 significant words, kebab-case, skip stop words (the, a, an, is, to, for, we, it, in, of, and, or, that, this)
5. Write `knowledge/_INBOX/YYYY-MM-DD-<slug>.md`:
   ```markdown
   ---
   title: <first line or best derived title>
   type: inbox
   timestamp: YYYY-MM-DDThh:mm:ssZ
   ---

   <content verbatim or lightly cleaned up>
   ```
6. Confirm: "Saved to `knowledge/_INBOX/<filename>.md`. Run `/bob:library process` to file it."

## Rules
- No phases. No conversation beyond step 2 prompt and step 6 confirmation.
- Do not invoke context-protocol or done-criteria.
- Never modify existing notes, indexes, or README.
