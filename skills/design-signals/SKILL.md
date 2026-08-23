---
name: design-signals
description: Distinguish mechanical implementation friction from evidence that the approved conceptual design may not fit reality. Invoked internally by /bob:implement during Step 5 (Implement); not user-invocable.
user-invocable: false
---

# Design Signals — Implementation as Sensor

The thinking framework behind `/bob:implement`'s pause behavior. The command file owns process and file I/O; this skill owns the taxonomy, the escalation tiers, and the evidence discipline that decides when implementation should stop and talk to a human instead of typing through it.

## Fundamental question

Has implementation exposed evidence that changes the conceptual model or its important assumptions — or is this just coding friction?

## Mechanical friction (not a signal)

Resolve autonomously: local, conventional, reversible, semantics-preserving, and within the boundaries the Design Record already approved. Examples: imports, syntax, formatting, routine test fixtures, known API details, deterministic lint fixes. Never raise a signal for these, no matter how much typing they took.

## The 12 conceptual signals

See `references/signal-taxonomy.md` for the full list and evidence template. In outline:

1. New concept not in Design.
2. A special case undermines the model.
3. Boolean/configuration growth changes semantics.
4. Dependency direction or boundary must change.
5. Public, data, or semantic contract changes.
6. Ownership/responsibility becomes unclear.
7. Existing duplicate domain concept is discovered.
8. Naming repeatedly resists the agreed vocabulary.
9. Test setup or call sites reveal disproportionate complexity.
10. Planned abstraction does not fit actual data or behavior.
11. Implementation requires significant unplanned indirection.
12. Tests disprove a design assumption.

## Escalation policy

See `references/escalation-policy.md` for the full decision procedure. The four tiers:

- **Continue autonomously** — local, reversible, conventional, semantics unchanged. Not a signal.
- **Continue and record** — minor deviation with no conceptual impact. Note it in the Implementation Note; don't stop.
- **Pause for human decision** — plausible conceptual impact but the repository stays in a safe state. Stop, present evidence, wait for a decision.
- **Stop and return to Design** — contract change, new core concept, broken design assumption, irreversible migration, or substantial boundary change. Stop implementation entirely; the fix belongs in `/bob:design`, not here.

## Evidence requirement

Every signal at "pause" tier or above must report all six fields before anything is presented as a pause:

1. observation and source location;
2. approved Design assumption affected;
3. why it may matter;
4. plausible interpretations;
5. safe-continuation status;
6. human decision required.

A pause without all six fields is not a valid signal — go back and gather the missing evidence, or resolve it as mechanical friction instead.

## Rules

- Do not raise a signal merely because implementation is difficult. Difficulty is not risk.
- Do not hide a signal behind an adapter, helper, flag, or branch to keep moving — surface it instead.
- Avoid speculative warnings without evidence — no signal without an observation and a source location.
- Pausing is based on the escalation tier the evidence supports, never on a plan step's difficulty rating.
