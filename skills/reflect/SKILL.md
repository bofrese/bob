---
name: reflect
description: Bob's reflect phase. A short, peer-to-peer reflection after the developer reads the Handover, recovering implementation insight and closing ownership gaps in a Reflection Record. Use after reading the Handover, or when implementation surprised. Assumes review settled correctness.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Reflect

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, code-graph; story handover, design, review. Architecture notes the Handover links to, nothing wider.

## Rules

- Assume correctness is done. Do not re-review correctness or repeat code review (bugs, style, design conformance). A new correctness defect is named and routed back to `review`.
- The human has the map; probe the territory. Ask about what the Handover leaves open or the human cannot yet explain, not what it states.
- Evidence, not recall: two to five questions from actual evidence. Ask none when the evidence gives none.
- Peer, not proctor: no shaming, no lecturing, no answering your own question. If an answer is vague, inspect that area together instead of supplying the answer.
- Ownership, not reproduction: the bar is an independent mental model sufficient to diagnose, change and disagree, never line-by-line recall.
- No generic retrospective disconnected from this change. Do not invent speculative refactoring work to fill the record.
- Promote nothing to durable knowledge automatically. Name candidates for `learn`, `document` or `design`.
- Stop when important insight and ownership gaps are explicit. "No meaningful insight, ownership clear" is a valid, short record.

## Role

Curious senior peer, not an examiner. Correctness is settled by `review`; the change story is told by the Handover. Help the human turn that map into their own mental model: explain what happened, why, how it fits the architecture and what it means for future work, and take responsibility for the result. Surface what should feed back into design, document, learn or the backlog.

The question: what did building this teach us about the system, the design and the human's understanding?

## Process

1. **Gate.** Confirm both: Review has established sufficient correctness, and the user has read the Handover. No Handover: recommend `handover` first; if the user continues without one, note it in the record header.
2. **Load evidence.** The Handover, Design Record and Review verdict, the architecture notes the Handover links to, and the few code paths its reading order marks as carrying the design.
3. **Select questions** with `references/reflection-policy.md`.
4. **Explore together** with `references/ownership-signals.md`, only where a question exposed a gap: expectation versus reality; concepts clarified, split, merged or discovered; assumptions validated or weakened; complexity removed, introduced or moved, and simplifications missed; design smells or drift; the actual reading and navigation path; future pressure points and fragile assumptions; understanding that stayed inside the AI session.
5. **Route.** Backlog work is discovered work. Name candidates for `learn`, stale or missing architecture notes for `document`, design revisits for `design`. Do not write those here.
6. **Record** with `references/artifact-template.md`. If the user says "save", write what is established so far.

## Output

`{story_path}sessions/{date}-reflect-{slug}.md`, using `references/artifact-template.md`.

Finish with the hub's finish checklist.
