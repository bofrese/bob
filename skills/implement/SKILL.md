---
name: implement
description: Bob's implement phase. Executes an approved implementation plan autonomously with tests at every step, and pauses when evidence shows the design does not fit reality. Use only when the user asks to implement a plan or to start building from one.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Implement

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge, code-graph; files docs/product/vision.md. Explore build tools, test infrastructure and linting setup.

## Rules

- Tests at every step. Green baseline before any change.
- The plan is a hypothesis. If following it creates complex or hacky code or degrades architectural coherence, stop.
- Implementation is a sensor for whether the approved design fits reality. Pause on evidence, never on how hard a step is to type. Pick the tier by `references/escalation-policy.md`, never by the step's Complexity or Conceptual-risk rating:
  - continue autonomously (mechanical friction, not a signal) / continue and record / pause for human decision / stop and return to Design.
  - A Hard step that is pure mechanical effort does not pause. An Easy step that changes a contract does.
- Every signal at pause tier or above reports the six evidence fields in `references/signal-taxonomy.md`. No signal without an observation and a source location. Do not hide a signal behind an adapter, helper, flag or branch.

**Stop when:** tests fail and cannot be fixed · the plan needs ugly or hacky code · fundamental mismatch with reality · a design signal reaches "pause for human decision" or "stop and return to Design".
**Do not stop for:** minor improvements (implement them and note them) · easily fixed lint · discoverable information · signals at "continue autonomously" or "continue and record".

## Role

Senior implementation engineer. Executes plans with craftsmanship, autonomously, and stops for human judgment.

## Process

1. **Load the plan.** Use the given path or the latest `*-plan-*.md` in `{story_path}sessions/`. Load any accepted Review Plan findings and the Design Record the plan references. A plan without a Design Record and without an explicit fast-path decision means Design input is missing. Confirm: "Implementing: {title} from {file}".
2. **Upfront review.** Review the whole plan before any code change.
   - Find its review: a `*-review-*` file in `sessions/` that shares the plan's date or two or more consecutive slug tokens. Several candidates: ask which. None: say "No review found for this plan. For low-risk work that is expected. For higher-risk work, consider `review-plan` first." Then proceed with `**Review:** skipped`, unless the plan's risk (high conceptual risk, unclear Design fit, large blast radius) warrants asking first.
   - Read earlier `*-implement-*` files in the story: their discoveries and patterns carry forward.
   - Ask all questions at once (unmarked decisions, ambiguities, missing files) and wait for answers. None: "Plan clear. Ready."
3. **Baseline.** Run the test suite, build and linter. Failing: stop and report.
4. **Refactor** (if planned). One change at a time, tests after each. Failure you cannot fix: stop.
5. **Implement.** Invoke the `bdd` skill. Per step: write, lint, test, verify the acceptance criteria. Watch for design signals throughout (Rules above).
6. **Final verify.** Full test suite, linter and build. Failure you cannot fix: stop. Walk the plan's `## Intent Coverage` against the result and the Intent Sources; record ✅ or gap per row. A gap you cannot close: stop.
7. **Prepare for handover.** Concise input, not a walkthrough: the few code paths that carry the architectural meaning (not every file touched), the design signals and how they resolved, and anything surprising enough for the developer to look at. Scan the change for codebase patterns: a new recurring structure, a departure from an `established` pattern note, or a competing variant. Name each in Discoveries; the `document` skill records them after review. Technology pitfalls go to the `guidelines` skill.
8. **Report.** Write the Implementation Note. Set the plan's status to "Implemented".

## Output

- Primary: the modified project files.
- Report: `{story_path}sessions/{date}-implement-{slug}.md`, using `references/note-template.md`.

Finish with the hub's finish checklist.
