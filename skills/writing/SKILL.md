---
name: writing
description: How bob writes every artifact it produces in the project folder and docs/ (plans, designs, reviews, notes, story files, architecture notes, product docs). TL;DR first, short, scannable, plain international English, no AI tells. Loaded by context-protocol for all commands. Does not apply to bob's own prompt files or to publish-facing copy.
user-invocable: false
---

# Writing - How Bob Writes Artifacts

## Scope

- ✅ Applies to: every file bob writes in the project folder and `docs/`: story artifacts, plans, design records, reviews, notes, architecture notes, guidelines, product docs.
- ❌ Does not apply to: LinkedIn posts, marketing and other publish-facing copy (they need a personal voice), and bob's own command and skill files (`bob:prompt-engineering` owns those).

## Two Readers

Every artifact has two readers. Write for both:
- **The next command's AI context:** facts, decisions, paths, open questions. Nothing it has to re-derive.
- **A human reviewer:** reads the TL;DR, scans headings, stops when satisfied.

## Shape

- **TL;DR at the top.** 3-6 bullets: what this is, what was decided, what is open. Rewrite it on every edit, so it never describes an older version.
- **Short and specific.** One idea per paragraph. Concrete names, paths, numbers. Delete sentences that add no fact.
- **Scannable.** Headings in sentence case, bullets for lists, tables for comparisons and anything with 3+ attributes. No walls of text.
- **Evidence by reference.** Code paths in backticks (`src/auth/session.ts:42`). Markdown links to docs only.
- **Next step at the end** when the artifact leads somewhere. No summary that repeats the body.

## Icon Vocabulary

Use only these, and only where they carry meaning (status, severity, change type). Never as decoration or bullet markers.

| Icon | Meaning |
|---|---|
| ✅ | ok, done, accepted |
| ⚠️ | risk, caution |
| ❌ | no, rejected, removed |
| ❓ | open question |
| 🔴 🟡 🟢 | severity: critical, important, minor |
| ➕ ➖ 🔀 | added, removed, moved |
| 🆕 | new |

## Plain International English

Most readers are engineers who are not native English speakers.
- Short active sentences, 12-20 words, subject-verb-object. Avoid nested clauses.
- No idioms or regional metaphors ("low-hanging fruit", "move the needle", "boil the ocean"). Say the plain thing ("easy tasks", "show results", "do too much").
- Exact technical terms, simple prose around them. Do not explain basics to experienced peers.

## Banned AI Tells

- **Vocabulary:** delve, tapestry, pivotal, testament, robust, holistic, seamless, leverage, foster, underscore, showcase, intricate, meticulous, paradigm shift, game-changer, landscape, valuable insights. Use plain verbs and nouns.
- **Verb bloat:** "serves as", "stands as", "functions as", "boasts", "features". Write "is" or "has".
- **Participle tag-ons:** ", ensuring X", ", highlighting Y" at the end of a sentence. Make the consequence its own sentence.
- **False contrasts:** "Not only X, but also Y", "It's not X, it's Y". State the fact.
- **Stacked triads:** "fast, reliable, and scalable". Use one or two properties, with a number if you have one.
- **Puffery and weasel words:** "a pivotal moment", "experts agree", "many believe". State the event or the source.
- **Throat-clearing and wrap-ups:** "In today's world...", "In conclusion...", "I hope this helps".
- **Typography:** never use the em dash (U+2014). Use "-", a comma, or a full stop. Straight quotes, not curly quotes.
- **Markup tells:** no bold on every bullet lead, no thematic breaks between every section, no skipped heading levels.

## Final Check

Before saving: Is the TL;DR current? Could a developer in Tokyo or Berlin read each sentence once without a dictionary? Does every section add a fact the reader needs?
