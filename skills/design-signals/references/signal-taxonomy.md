# Signal Taxonomy

Twelve signals implementation can raise. Each is evidence that the approved conceptual design may not fit reality — not a measure of coding effort. When one fires, fill in the evidence template below before deciding an escalation tier (see `escalation-policy.md`).

| # | Signal | What it looks like in practice |
|---|--------|---------------------------------|
| 1 | New concept not in Design | A name, entity, or responsibility is needed that the Design Record never mentioned. |
| 2 | Special case undermines the model | An "if this one case, then..." branch that the approved model doesn't account for. |
| 3 | Boolean/configuration growth changes semantics | A new flag or config option doesn't just toggle behavior — it changes what the thing means. |
| 4 | Dependency direction or boundary must change | Module A needs to know about B, or vice versa, in a direction the Design Record ruled out. |
| 5 | Public, data, or semantic contract changes | An API shape, persisted schema, or event/message meaning must change from what was approved. |
| 6 | Ownership/responsibility becomes unclear | Two components could plausibly own a piece of behavior and the Design Record didn't say which. |
| 7 | Existing duplicate domain concept is discovered | The codebase already has something that does what the new concept is meant to do. |
| 8 | Naming repeatedly resists the agreed vocabulary | The agreed term keeps needing qualifiers or doesn't fit what's actually being built. |
| 9 | Test setup or call sites reveal disproportionate complexity | Wiring a test (or a caller) needs far more scaffolding than the design implied — a sign the abstraction doesn't match usage. |
| 10 | Planned abstraction does not fit actual data or behavior | The interface or type designed on paper doesn't hold once real inputs/outputs are in hand. |
| 11 | Implementation requires significant unplanned indirection | An extra layer, adapter, or intermediate step is needed that the Design Record didn't call for. |
| 12 | Tests disprove a design assumption | A test written from the Design Record fails not from a bug but because the assumption itself was wrong. |

## Evidence template

For any signal at "pause" tier or above, report all six fields — a signal without all six isn't ready to present:

1. **Observation and source location** — what was seen, and exactly where (file:line, test name, command output).
2. **Affected Design assumption** — the specific claim in the Design Record (or embedded `## Design` section) this bears on.
3. **Why it matters** — the concrete consequence if the assumption is wrong.
4. **Plausible interpretations** — at least two readings of what this could mean, not a single conclusion presented as fact.
5. **Safe-continuation status** — can implementation keep going elsewhere while this is decided, or does it block the current step.
6. **Required human decision** — the specific choice needed to unblock, framed as a question, not a recommendation dressed as a fact.

No signal without an observation and a source location. Do not manufacture a signal to appear thorough — a clean implementation with no signals is a valid, and common, outcome.
