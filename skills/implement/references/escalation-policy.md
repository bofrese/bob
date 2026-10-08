# Escalation policy

Four tiers. Pick the tier the evidence supports, never the plan step's Complexity or Conceptual-risk rating, and never "this is taking a while".

## Continue autonomously

Mechanical friction, not a signal: local, conventional, reversible, semantics-preserving, and within the boundaries the Design Record approved. Examples: imports, syntax, formatting, routine test fixtures, known API details, deterministic lint fixes. Fix it and keep moving. Nothing to record, no matter how much typing it took.

## Continue and record

A minor deviation from the plan with no conceptual impact. The "why" is worth a line in the Implementation Note's Design Signals Raised section, but it does not change what anyone needs to understand about the system. Note the evidence briefly and continue.

## Pause for human decision

Plausible conceptual impact, but the repository is still in a safe, working state. Stop before going further on the affected area. Present all six evidence fields (`signal-taxonomy.md`) and the specific decision needed. Resume once the human decides; record the decision and its resolution in the Implementation Note.

## Stop and return to Design

One or more of: a contract change, a new core concept, a broken design assumption, an irreversible migration, or a substantial boundary change. Stop implementation for the affected scope. Do not code around it and do not resolve it here: the fix belongs in the `design` skill. Report what was completed, what is blocked, and why, then hand back to Design.

## Decision procedure

1. Does the observation change the conceptual model or an assumption the Design Record depends on? No: mechanical friction, continue autonomously.
2. Yes, the repository is still in a safe state, and the impact is plausible rather than certain: pause for human decision.
3. The impact is a contract, core-concept or boundary change, or the assumption is now disproven rather than questioned: stop and return to Design.
4. The deviation is real but has no conceptual consequence: continue and record.

Difficulty is not risk: do not raise a signal because implementation is hard. Do not hide a signal behind an adapter, helper, flag or branch to avoid stopping.
