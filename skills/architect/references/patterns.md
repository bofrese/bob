# Patterns - Recognition, Status, Drift

Use when discovering how a codebase solves recurring problems, checking a change against existing patterns, or looking for drift.

## What a pattern is here

A recurring, context-sensitive way this codebase resolves a class of problem (Coplien's sense), not a Gang of Four label. The question: "When this kind of problem occurs here, how do we normally solve it, and why?"

Typical candidates: introducing a new business capability, validation, attaching authorization, expressing persistence boundaries, wrapping external integrations, representing and propagating errors, separating domain decisions from infrastructure, structuring async work, introducing configuration, exposing a module's public interface, applying cross-cutting concerns, emitting and consuming events, representing state transitions, organizing tests around a concept.

Give a pattern a short, local name. Do not force it into a textbook label.

## Status

| Status | Evidence | Who sets it |
|---|---|---|
| `established` | The same problem is solved the same way across the system | Human only. AI proposes, never promotes |
| `emerging` | Several places converge on one approach, not yet explicit | AI may record it; surface it to the human |
| `competing` | Similar problems solved differently in different places | AI records both variants in one note, ending with an open design question |

Never choose a winner between competing variants. Differences can be intentional (different context), historical, accidental or debt. The human decides.

An AI finding a pattern does not make it a universal rule.

## Checking a change against patterns

- Does the change follow the `established` pattern for its kind of problem?
- Does it introduce a second way (a new competing variant)? That is a design concern, not a bug.
- Does it strengthen an `emerging` pattern enough to propose promotion?

## Drift signals

Drift appears across many locally reasonable changes. Look for:

- **Pattern drift:** a new way to solve a problem that already has a pattern.
- **Architecture drift:** a concept note no longer matches the code (moved, split, merged, no longer exists).
- **Naming drift:** the same concept under different names, or one name for different concepts.
- **Interface drift:** a public surface that grows leaks of framework or implementation detail.
- **Source-organization drift:** new files that break the established layout or reading order.
- **Duplicated concepts:** two notes, modules or rules that describe the same thing.

Report drift with evidence (paths, notes). Do not fix it silently.
