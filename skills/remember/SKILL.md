---
name: remember
description: Bob's quick capture. Writes a thought, decision or insight straight to the knowledge inbox (knowledge/_INBOX/) without loading context or running a phase. Use when the user says "remember this", "note that" or wants to capture something mid-session for later filing.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Remember

Quick mid-session capture. Deliberately skips the `bob` hub: no start checklist, no finish checklist, no context loading. The first run bootstraps the vault (one-time cost).

## Process

1. Arguments given: use them as the content. None: ask "What should I remember?", one question only.
2. `knowledge/` missing: say "Setting up knowledge vault first...", run `python3 ../library/scripts/bootstrap.py` (the `library` skill's bootstrap, relative to this skill's folder) from the project root, then continue.
3. Slug: the first 4-5 significant words, kebab-case, without stop words (the, a, an, is, to, for, we, it, in, of, and, or, that, this).
4. Write `knowledge/_INBOX/{YYYY-MM-DD}-{slug}.md`:
   ```markdown
   ---
   title: <first line or best derived title>
   type: inbox
   timestamp: YYYY-MM-DDThh:mm:ssZ
   ---

   <content verbatim or lightly cleaned up>
   ```
5. Confirm: "Saved to `knowledge/_INBOX/<filename>.md`. Run `library process` to file it."

## Rules

- No conversation beyond the question in step 1 and the confirmation in step 5.
- Never modify existing notes, indexes or `knowledge/README.md`.
