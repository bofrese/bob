# Writing artifacts

Applies to every file bob writes in the project and `docs/`. Not to publish-facing copy (posts, marketing) and not to bob's own skill files.

Text style: the `plain-writing` skill, technical register. If its rules are not in this session yet, load the skill. This file adds only the shape of bob artifacts.

Two readers: the next phase's agent (facts, decisions, paths, open questions) and a human reviewer (reads the TL;DR, scans headings, stops when satisfied).

## Shape

- TL;DR at the top: 3-6 bullets on what this is, what was decided, what is open. Rewrite it on every edit.
- One idea per paragraph. Concrete names, paths, numbers. Delete sentences that add no fact.
- Bullets for lists, tables for comparisons and anything with 3+ attributes.
- Evidence by reference: code paths in backticks (`src/auth/session.ts:42`), markdown links to docs.
- Verified claims only. A claim about behavior, or a bug, cites the line that makes the decision, read in the file itself, not inferred from which function calls which. A reason nobody recorded is written as "not recorded", never guessed.
- Diagrams only when they explain more than a list or table. If `mmdc` is installed, validate Mermaid before saving: `mmdc -q -i <file.md> -o <scratch>/out.md` (non-zero exit = syntax error). If it fails with "Could not find chrome-headless-shell", that is the setup, not your diagram: pass `-p <scratch>/pp.json` containing `{"executablePath": "<path to installed Chrome>"}`.
- End with the next step when there is one. No closing summary.

## Icons

Only where they carry meaning, never as decoration.

| Icon | Meaning |
|---|---|
| ✅ ❌ | ok or accepted; no or rejected |
| ⚠️ ❓ | risk; open question |
| 🔴 🟡 🟢 | critical, important, minor |
| ➕ ➖ 🔀 🆕 | added, removed, moved, new |

Before saving: is the TL;DR current, and does every section add a needed fact?
