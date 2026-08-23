# Escalation Policy

Four tiers. Pick the tier the evidence supports — never the plan step's Complexity or Conceptual-risk rating, and never "this is taking a while."

## Continue autonomously

Mechanical friction, not a signal. Local, reversible, conventional, semantics-preserving, and within boundaries the Design Record already approved. Fix it and keep moving; nothing to record.

## Continue and record

A minor deviation from the plan with no conceptual impact — the "why" is worth a line in the Implementation Note's Design Signals Raised section, but doesn't change what anyone needs to understand about the system. Note the evidence briefly and continue without stopping.

## Pause for human decision

Plausible conceptual impact, but the repository is still in a safe, working state. Stop before proceeding further on the affected area. Present all six evidence fields (`signal-taxonomy.md`) and the specific decision needed. Resume once the human decides; record the decision and its resolution in the Implementation Note.

## Stop and return to Design

One or more of: a contract change, a genuinely new core concept, a broken design assumption, an irreversible migration, or a substantial boundary change. Stop implementation entirely for the affected scope — do not keep coding around it, and do not resolve it here. The fix belongs in `/bob:design`, not in an ad hoc decision mid-implementation. Report what was completed, what's blocked, and why, then hand back to Design.

## Decision procedure

1. Does the observation change the conceptual model or an assumption the Design Record depends on? If no → mechanical friction, continue autonomously.
2. If yes, is the repository still in a safe state, and is the impact plausible rather than certain? → pause for human decision.
3. If the impact is a contract, core-concept, or boundary change, or the assumption is now disproven rather than merely questioned → stop and return to Design.
4. If the deviation is real but has no conceptual consequence → continue and record.

Do not raise a signal merely because implementation is difficult — difficulty is not risk. Do not hide a signal behind an adapter, helper, flag, or branch to avoid stopping.
