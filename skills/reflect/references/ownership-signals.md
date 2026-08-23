# Ownership Standard

Ownership does not require reproducing generated code or explaining every line. It requires a sufficient independent mental model to diagnose, change, and disagree.

For significant work, the accountable developer should be able to:

- explain domain intent and the conceptual model;
- identify critical code paths and boundaries;
- explain major trade-offs and fragile assumptions;
- predict likely failure modes;
- know where to begin debugging;
- describe how a plausible future change would affect the design;
- challenge an AI proposal that violates the model.

## Using this during Reflect

Check for these signals only where the evidence-driven questions (see `reflection-policy.md`) surfaced a candidate gap — this is not a checklist to march through line by line.

If an answer is vague on one of these dimensions, inspect that area together: look at the code, the Design Record, or the Implementation Note until the gap is either closed or explicitly named as an open ownership gap in the Reflection Record. Do not shame, lecture, or immediately answer your own question.

Ownership gaps are a valid, reportable outcome — the point of Reflect is to make them explicit, not to guarantee they never exist.
