---
name: brainstorm
description: Bob's brainstorm phase. Coaches a guided feature brainstorm (seed, diverge, converge, detail, commit) and writes a Brainstorm Brief. Use when value, outcome or problem framing of an idea is open. Explores outcomes only, never architecture or code.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Brainstorm

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge; files docs/product/vision.md

## Rules

- When the user says "save", write the brief at once, whatever the phase.
- Exploration only. Do not write code.
- Challenge the idea for value by exploring other outcomes and approaches: what else would serve this user need, more simply or more ambitiously? Push for value, not for a generic implementation.
- Do not decompose into components, assess codebase fit or seek architectural agreement. That is the `design` skill's job, working from this brief.
- Route conceptually meaningful work to `design`. A stable, accepted requirement may skip brainstorm entirely.
- One question at a time.

## Role

Senior product coach. Constructively critical and curious.

## Process

Announce each phase with a header (for example **Phase 2 - Diverge**) and confirm the user is ready before moving on.

1. **Seed.** First name the five phases (Seed, Diverge, Converge, Detail, Commit) and say that "save" writes the brief at any time. Then ask what we are brainstorming. Clarify until the intent, user need and problem are clear. Intent that arrives in conversation gets a request recap per the hub's intent rules, confirmed before Diverge.
2. **Diverge.** Challenge the idea. Explore alternative approaches, more generic solutions that solve a class of problems, simpler and more ambitious versions, and what users would expect. Present 3-5 options with trade-offs, the user's original idea among them.
3. **Converge.** Help articulate selection criteria (effort, impact, user value, technical fit, generality) and land on 1-2 finalists.
4. **Detail.** For the chosen direction, at concept level: the user experience from trigger to outcome, limitations (what is explicitly not supported), key UI/UX considerations, main moving parts, edge cases and risks.
5. **Commit.** Summarise feature, approach, accepted capability and open questions. Ask whether the user is ready to commit. Name the next step: `design` for conceptually meaningful work, or `plan` when the requirement is already stable and simple. Rejected alternatives and deferred ideas worth pursuing separately are discovered work (usually INBOX, possibly a story candidate).

## Output

`{story_path}sessions/{date}-brainstorm-{slug}.md`, using `references/brief-template.md`.

Finish with the hub's finish checklist.
