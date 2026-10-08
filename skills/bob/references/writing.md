# Writing artifacts

Applies to every file bob writes in the project and `docs/`. Not to publish-facing copy (posts, marketing) and not to bob's own skill files.

Two readers: the next phase's agent (facts, decisions, paths, open questions) and a human reviewer (reads the TL;DR, scans headings, stops when satisfied).

## Shape

- TL;DR at the top: 3-6 bullets on what this is, what was decided, what is open. Rewrite it on every edit.
- One idea per paragraph. Concrete names, paths, numbers. Delete sentences that add no fact.
- Headings in sentence case, bullets for lists, tables for comparisons and anything with 3+ attributes.
- Evidence by reference: code paths in backticks (`src/auth/session.ts:42`), markdown links to docs.
- Diagrams only when they explain more than a list or table. If `mmdc` is installed, validate Mermaid before saving: `mmdc -q -i <file.md> -o <scratch>/out.md` (non-zero exit = syntax error).
- End with the next step when there is one. No closing summary.

## Icons

Only where they carry meaning, never as decoration.

| Icon | Meaning |
|---|---|
| ✅ ❌ | ok or accepted; no or rejected |
| ⚠️ ❓ | risk; open question |
| 🔴 🟡 🟢 | critical, important, minor |
| ➕ ➖ 🔀 🆕 | added, removed, moved, new |

## Plain international English

Most readers are engineers who are not native English speakers.
- Active sentences of 12-20 words, subject-verb-object. No nested clauses.
- No idioms ("low-hanging fruit", "move the needle"). Say the plain thing.
- Exact technical terms, simple prose around them. Do not explain basics to peers.

## Do not write

- AI vocabulary: delve, tapestry, pivotal, testament, robust, holistic, seamless, leverage, foster, underscore, showcase, intricate, meticulous, paradigm shift, game-changer, landscape, valuable insights.
- "serves as", "stands as", "boasts", "features": write "is" or "has".
- Tag-ons such as ", ensuring X" at the end of a sentence. Give the consequence its own sentence.
- "Not only X, but also Y", "It's not X, it's Y", stacked triads, puffery, "experts agree".
- Openers and wrap-ups: "In today's world", "In conclusion", "I hope this helps".
- The em dash (U+2014). Use "-", a comma or a full stop. Straight quotes.
- Bold on every bullet, a rule between every section, skipped heading levels.

Before saving: is the TL;DR current, can a reader in Tokyo or Berlin read each sentence once, does every section add a needed fact?
