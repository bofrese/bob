# Reflection Policy - Question Selection

Reflect is not a second review and not an oral exam. It runs on a tight evidence-driven budget.

## Assume correctness is done

`/bob:review` already decided whether the code is correct. Never re-open bugs, design-conformance failures, or findings it already settled. If new evidence of a correctness defect surfaces during Reflect, name it and route it back to `/bob:review` - do not fix or adjudicate it here.

## Select 2-5 high-value questions from actual diff evidence

Do not ask generic retrospective questions ("what did you learn?", "how do you feel about the code?"). Ground every question in something the session actually produced:

- a part of the Handover's reading order or future impact the human cannot yet explain in their own words;
- a Design Signal that fired during Implement, and how it resolved;
- a deviation Review flagged between plan/design and what shipped;
- a code path the Handover's reading order marks as carrying the design;
- a place where the Design Record and the final code disagree, even if Review accepted the disagreement;
- a surprising or non-obvious decision made mid-implementation with no human present;
- a design smell, drift, unnecessary complexity or a missed simplification visible in the change (`bob:architect` `references/concepts.md`, `references/patterns.md`).

If the diff gives fewer than two genuine candidates, ask fewer questions - do not manufacture more to hit a quota. A count of zero is valid when the change was small and mechanical.

## The human has the map; probe the territory

The human has read the Handover. Do not re-explain it. Ask about what lies beyond it: why a choice holds, what would break it, how the next change would land. Pose the question and wait. Do not immediately supply the explanation. Only step in to explore together when the answer is vague, contradicted by the code, or the human says they don't know.

## Keep it short

Two to five questions is the ceiling, not a target. A session that confirms ownership in one exchange is a success, not an incomplete reflection.
