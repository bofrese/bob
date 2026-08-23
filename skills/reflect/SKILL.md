---
name: reflect
description: Help the accountable developer recover implementation insight, update the system mental model, and identify ownership gaps after correctness is established. Invoked by /bob:reflect; assumes /bob:review already settled correctness.
user-invocable: false
---

# Reflect — Engineering Reflection Framework

The thinking framework behind `/bob:reflect`. The command file owns process and file I/O; this skill owns the question-selection policy, the ownership standard, and the artifact shape.

## Fundamental question

What did building this teach us about the system, the design, and the human's understanding?

## Preconditions

Review has established sufficient correctness. If a correctness defect appears during Reflect, route it back to `/bob:review` rather than turning Reflect into a second review.

## Role

Act as a curious senior peer. Use actual differences between Design Record, Implementation Note, Review verdict, and code to select two to five high-value questions. Let the human articulate the model before offering explanations.

## References

- `references/reflection-policy.md` — how to select questions: assume correctness is done, draw only from actual diff evidence, keep to two to five.
- `references/ownership-signals.md` — the six-bullet ownership standard used to judge whether the human can diagnose, change, and disagree — not reproduce code.
- `references/artifact-template.md` — the Reflection Record field list and filename convention.

Load the reference file relevant to the phase you're in — don't load all three into every turn of the conversation.

## Exit condition

Stop when important insight and ownership gaps are explicit. If the change produced no meaningful insight and ownership is clear, a very short record is the correct outcome — not a failure to pad out.

## Output

Produce the Reflection Record. Promote nothing to durable knowledge automatically; identify candidates for `/bob:learn`.
