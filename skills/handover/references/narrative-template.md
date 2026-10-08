# Narrative Template - Handover Artifact

**Filename:** `{date}-handover-{slug}.md`, written to `{story_path}/sessions/`.

## Reading-order policy

Order the walkthrough in conceptual, dependency or learning order, the order an experienced developer would want. Never file, diff or commit order. Each step only needs what came before it:
1. Start at the concept or interface that explains the change (often the new public surface, or the rule that changed).
2. Then what depends on it, in dependency order.
3. Then wiring and integration.
4. Tests next to the code they specify when a test is the clearest statement of the behavior; otherwise after the code.

## Presentation policy

Per place, choose what teaches best. Copy excerpts from the diff, never retype them. Label each excerpt with its path and line range in HEAD. Trim unchanged lines with `...`, never a changed line.

| Situation | Show |
|---|---|
| Changed behavior in existing code | Before and after blocks, or a `diff` block with enough surrounding lines to read it on its own |
| Small change inside a larger unit | The unit in context, changed lines marked (`diff` block with `+`/`-`) |
| New file or new abstraction | Public surface first (signatures, contracts, frontmatter), then the essential implementation; boilerplate as `...` |
| Prose or prompt files | The changed passage quoted; before and after when the meaning changed |
| Mechanical sweep | One sentence on what and why, file count, one sample hunk, file list in a `<details>` block |

Next to each excerpt: what to look for, why it was done this way, alternatives considered, learnings made there. Skip what the code already says.

## Navigation

- Number the walkthrough sections (`### 3. ...`) and sweeps (`### S1. ...`). The Contents list mirrors the numbers. In a project read in Obsidian, Contents entries link as `[[#3. Title]]`; otherwise a plain numbered list.
- Cross-reference by section number ("see 3"). Code paths in backticks; Markdown links only to docs.
- Long file lists go in `<details>` blocks.

## Coverage

End with the Coverage table: every changed file, and the section or sweep that covers it. Then pipe the scope's changed files into `gather.py --check {handover}` per repo. Every path it prints is missing: add it to a section or sweep and rerun until it prints nothing.

## Template

```markdown
# Handover: {Change}
**Date:** {YYYY-MM-DD} | **Story:** {STORY-ID} | **Scope:** {since last handover {date} / whole story / range} | **Repos:** {repo: N commits, M files, ...}
**Design:** [{name}]({path}) | **Implementation:** [{name}]({path}) | **Review:** [{name}]({path})
**Diff:** `git -C {repo} diff {baseline}..{head}` per repo

## TL;DR
{3-6 bullets: the problem, the main design idea, what changed, what to watch.}

## Contents
1. {Walkthrough section}
...
S1. {Sweep}

## Problem
{What was being solved, in 2-4 sentences.}

## Main design ideas
{The few ideas that shape the change. Where the built system departs from the Design Record, say so and why.}

## What changed and why
| Change | Why | Section |
|---|---|---|

## Walkthrough

### 1. {Concept or interface}
{What to look for and why it matters. Reasoning, alternatives, learnings.}

`{path}` ({lines})
```diff
{excerpt}
```

### 2. ...

## Sweeps

### S1. {Name} - {N} files
{What and why, in one or two sentences.}

`{sample path}`
```diff
{sample hunk}
```

<details><summary>{N} files</summary>

- `{path}`

</details>

## Review findings and resolution
| Finding | Resolution |
|---|---|

## Future impact
- New abstractions:
- Altered interfaces:
- Changed assumptions:
- New or changed patterns (with status):
- Where future work should follow the same approach:
- Provisional parts:
- Follow-ups:

## Architecture notes updated
- [{note}]({path}) - {what changed}
- Notes that still look stale after this change: {list, or "none"; route to `document`}

## Coverage
| File | Covered in |
|---|---|
```
