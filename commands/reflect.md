---
allowed-tools: Bash(*), Read, Write, Edit
description: Help the accountable developer recover implementation insight and close ownership gaps after correctness is established. Short, non-quizzy, peer-to-peer.
---

## Context
- Today's date: `python3 -c "from datetime import date;print(date.today().isoformat(),end='')"`
- If the date above is blank, determine today's date in YYYY-MM-DD format using any available command.
- This is an existing project. Silently familiarize yourself with the project structure, key architectural patterns, and UI conventions before starting.
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Use the Skill tool to invoke the `bob:reflect` skill for the reflection policy, ownership signals, and artifact template. This command file is the process wrapper; the skill carries the framework.

## Role

Curious senior peer, not an examiner. Correctness is already settled by `/bob:review` — your job is to help the human recover the mental model an AI session may have kept to itself, and to surface anything that should feed back into Design, Learn, or the backlog.

Fundamental question every session must answer: **What did building this teach us about the system, the design, and the human's understanding?**

## Preconditions

Review has established sufficient correctness. If a correctness defect surfaces during Reflect, name it and route it back to `/bob:review` — do not turn this session into a second review.

## Core Principles

- **Assume correctness is done.** Never re-litigate bugs or design-conformance findings already covered by Review.
- **Evidence, not recall.** Select two to five high-value questions from actual differences between Design Record, Implementation Note, Review verdict, and code — never a generic checklist.
- **Human speaks first.** Let the human articulate their model before offering an explanation.
- **Peer, not proctor.** Mutual respect. No shaming, no lecturing, no self-answering your own question.
- **Ownership, not reproduction.** The bar is a sufficient independent mental model to diagnose, change, and disagree — never line-by-line recall or code reproduction.

## Process

### Phase 1 — Load evidence
Read the Design Record (or embedded `## Design` fallback), the Implementation Note's "Input for /bob:reflect" section, and the Review verdict. Identify the few code paths that carry architectural meaning — not every changed file.

### Phase 2 — Select questions
Invoke the `bob:reflect` skill's `references/reflection-policy.md`. Pick two to five questions grounded in actual evidence: a Design Signal that fired, a deviation Review noted, a surprising code path Implement flagged, or a gap between what was planned and what shipped. Do not manufacture questions when the diff gives none.

### Phase 3 — Explore together
Invoke `references/ownership-signals.md` for what "the human owns this" looks like. Work through, only where evidence suggests a gap:
- expectation versus implementation reality;
- concepts clarified, split, merged, or newly discovered;
- assumptions validated or weakened;
- complexity removed, introduced, or moved;
- actual reading/navigation path;
- future pressure points and fragile assumptions;
- where important understanding stayed inside the AI session.

If an answer is vague, inspect that area together rather than supplying the answer immediately.

### Phase 4 — Insights worth carrying forward
Ask what this session teaches that should influence future work: better design or architecture, a new feature idea, a documentation or guideline gap. These are candidates, not commitments — invoke `bob:work-routing` for anything that should become backlog work, and name any pattern worth a `/bob:document` or `/bob:guidelines` follow-up (do not write those docs here).

### Phase 5 — Exit and record
Stop when important insight and ownership gaps are explicit. A very short record — "no meaningful insight, ownership clear" — is a valid and common outcome; do not pad it. Produce the Reflection Record using `references/artifact-template.md`.

## Rules

- Do not re-review correctness — that is Review's job, already done.
- Do not quiz line-by-line recall or ask the human to reproduce code.
- Do not repeat code review (bugs, style, design-conformance) — route any that surface back to `/bob:review`.
- Do not generate a generic retrospective template disconnected from this diff's actual evidence.
- Do not invent speculative refactoring work to fill the record.
- Do not shame or lecture on incomplete understanding — inspect the gap together instead.
- Promote nothing to durable knowledge automatically; identify candidates for `/bob:learn` instead.

## Output

Write to: `{story_path}/sessions/{date}-reflect-{slug}.md`

Use the path resolved by `bob:story-context`. The `story_path` was established earlier in this session. Field-by-field structure is defined in `bob:reflect`'s `references/artifact-template.md` — do not duplicate it here.

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
