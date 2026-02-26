---
name: BDD — Behaviour-Driven Development
description: Invoke this skill when defining acceptance criteria, testing strategy, or evaluating whether something is done. Used by bob commands during implementation planning and before writing code.
version: 1.0.0
---

# BDD — Behaviour-Driven Development

A thinking framework. Apply when defining tests, acceptance criteria, or evaluating whether something is "done".

---

## The core discipline

**Write acceptance criteria before you write code.** If you can't state what success looks like in plain language, you don't understand the requirement yet. Go back.

## The shape of a criterion

Every acceptance criterion follows this structure:

- **Given** — the precondition. The state the system is in before the behaviour is triggered.
- **When** — the action. What the user (or system) does.
- **Then** — the observable outcome. What changes — and how you'd know it changed.

If "Then" can't be observed — by a user, a log, an API response, a database state — it's not a real criterion. It's an implementation detail.

## What we test: behaviour, not implementation

- Test what the system **does**, not how it **does it**.
- A good test survives a refactor of the internals. If your test breaks when you rename a private method, it's testing the wrong thing.
- Name tests after the behaviour. `user can reset password` not `PasswordService.callResetEndpoint`.

## Acceptance criteria live in the plan

Before `/bob:implement` starts, the plan must contain testable acceptance criteria for every piece of new behaviour. Written in Given/When/Then. Reviewed by `/bob:review-plan`. This is the contract.

## The golden check

Before shipping: does every acceptance criterion from the plan have a passing test or a verified manual check? If not, it's not done.
