# Engineering Workflows
*Last updated: 2026-06-16*

The core pipeline: turn ideas into shipped, tested, documented code. This is where you'll spend most of your time.

## The Pipeline at a Glance

```
Brainstorm (idea) → Plan (how to build) → Implement (write code) → Review (quality check) → Done
```

But there's a critical step you might miss: **Review the plan before implementing.** A fresh set of eyes catches problems that the planning session missed.

```
Brainstorm → Plan → Review Plan → Implement → Review Code → Done
```

Each step is a separate session (usually separate days). Each session reads the previous output, produces a new output, and you make a go/no-go decision before moving forward.

## Phase 1: Brainstorm

**When:** You have an idea you want to think through properly.

**What you do:** Say `/bob:brainstorm` and describe the idea. The AI asks structured questions to help you explore it.

**The AI guides you through:**
1. **Diverge** — What are different ways to solve this? What alternatives exist?
2. **Converge** — Which approach is best given what matters (effort, impact, user value, technical fit)?
3. **Detail** — Flesh out the chosen approach. What's the user experience? What are the components?
4. **Validate** — Does this fit in the codebase cleanly? Any refactoring needed upfront?
5. **Commit** — Summarize what we're doing, open questions, and confirm you're ready to move forward.

**Output:** `{story_path}/{date}-brainstorm-{slug}.md`

A complete record of what you discussed, what you considered, what you decided, and why. This becomes input to planning.

**Time:** 30 minutes to 1.5 hours depending on complexity.

---

## Phase 2: Plan

**When:** After brainstorm, before any code is written.

**What you do:** Run `/bob:plan` and point it at your brainstorm report (or just the story context if bob detects it):

```
/bob:plan projects/myapp/stories/APP-001/2026-06-16-brainstorm-auth.md
```

The AI reads the brainstorm, examines the codebase, and walks you through implementation step by step.

**The plan includes:**
- **Approach** — How the change will be made. Where code will live. What patterns will be used.
- **Test strategy** — What needs to be tested *before* implementation. Using BDD (Given/When/Then) thinking.
- **Implementation steps** — Concrete numbered steps, one per code change or feature.
- **Questions & decisions** — Flags things the plan is unsure about. Your job is to answer or override.
- **Risks** — What could go wrong? What assumptions are we making?

**Output:** `{story_path}/{date}-plan-{slug}.md`

The plan is self-contained: someone who wasn't in the brainstorm conversation could pick this up and implement it.

**Critical:** Read the Questions & Decisions table. These are things the AI flagged as needing your judgment. Answer them. If you disagree with the approach, change it. The plan must be something *you* are genuinely happy with before moving forward.

**Time:** 30 minutes to 1 hour.

---

## Phase 3: Review the Plan (Don't Skip This)

**When:** Plan is written but before implementation starts.

**What you do:** Run `/bob:review-plan` and point it at your plan:

```
/bob:review-plan projects/myapp/stories/APP-001/2026-06-16-plan-auth.md
```

This command does something critical: it ignores the planning session. Fresh context. No memory of the conversation that produced the plan. It re-reads the codebase independently and checks:
- Does the plan's description of the current codebase match reality?
- Are there simpler approaches the plan missed?
- Are there security issues or edge cases not covered?
- Is the plan overengineered?

**Why this matters:** The longer a conversation goes, the less likely the AI pushes back. You expect a thinking partner. You get an enthusiastic yes-person. Session boundaries kill that. A plan reviewed fresh gets genuine critique, not polite agreement.

**Output:** `{story_path}/{date}-review-plan-{slug}.md`

If the review flags problems: update the plan and re-review it if needed. If the review approves it: move forward with confidence.

**Time:** 20-40 minutes depending on plan complexity.

---

## Phase 4: Implement

**When:** Plan is reviewed and approved.

**What you do:** Run `/bob:implement` and point it at your approved plan:

```
/bob:implement projects/myapp/stories/APP-001/2026-06-16-plan-auth.md
```

The AI reads the plan and executes it step by step. For each step:
1. Run the test suite first to establish a green baseline
2. Implement the step as described in the plan
3. Run tests after each change to verify it works
4. If it hits something the plan didn't anticipate: stop and ask you
5. If it spots a small improvement: make it and note it in the report

**Output:** Modified code + `{story_path}/{date}-implement-{slug}.md`

The implementation report documents what was built, any deviations from the plan, discoveries made along the way, and verification that tests pass.

**Your role:** Watch for surprises. The AI might ask you a question mid-implementation (unexpected complexity, decision needed). Answer it. Otherwise, trust the plan.

**Time:** Varies wildly (30 minutes for a small change, several hours for a complex feature). The AI does the heavy lifting.

---

## Phase 5: Code Review

**When:** Implementation is complete and tests pass.

**What you do:** Run `/bob:review`:

```
/bob:review
```

The AI auto-detects what changed (git diff), reads the plan to compare intent vs reality, reads your project guidelines, and walks you through findings one at a time.

**What it checks:**
- Does the code do what the plan said it would?
- Is the code clean? Are there refactoring opportunities?
- Do the tests verify behavior (not just implementation)?
- Does the code follow project guidelines?
- Is the codebase still healthy after this change?

**Output:** `{story_path}/{date}-review-{slug}.md`

A handoff document: anyone can read this and own the code confidently.

**Your role:** Fix things the review flags. If you disagree with a finding, say so (you're not obligated to fix everything). When the review is approved, you can merge.

**Time:** 20-60 minutes depending on change size and review depth.

---

## Phase 6: Document

**When:** Code is shipped (merged or in production).

**What you do:** Run `/bob:document`:

```
/bob:document
```

The AI looks at what changed and identifies what's not documented. It writes clear documentation for the *why* and *what*, not a line-by-line walkthrough.

**Output:** Updated or new files in `docs/`, with updates to `docs/README.md` (the navigation index).

**Your role:** Review what was written. Correct any misunderstandings. Approve or revise before committing.

**Time:** 20-40 minutes depending on scope.

---

## What If?

### "The plan has a problem that the review just caught"

Update the plan and re-run review. The review should approve the revised plan. Then proceed to implementation.

### "I disagree with something in the code review"

That's fine. Code review is a conversation. Discuss it with the AI. The review might be wrong. You might change your mind. Either way, you decide what ships.

### "Something went wrong during implementation"

The AI should catch it and ask you. If it doesn't, run `/bob:review` on the partial implementation. Fix what it flags. Then continue or resume from a known good state.

### "The plan was incomplete and I had to improvise"

That's okay. Document what you did in the implementation report and mention it. The review will check it. If it's good, great. If it needs adjustment, fix it.

---

## The Rhythm

Once you've done this a few times, it becomes a rhythm:

**Day 1 — Brainstorm**
Morning coffee, 1 session, 1 artifact, clear direction.

**Day 2 — Plan**
New session, fresh thinking, complete plan written.

**Day 3 — Review Plan**
Catch problems the planning session missed.

**Day 4 — Implement**
Follow the plan, write code, verify it works.

**Day 5 — Review**
Freshly reviewed code with guidelines applied.

**Day 6 — Document**
Capture what you built so the next person understands it.

Do it again next week with a different feature. By the tenth feature, you'll notice the quality is consistent, decisions are recorded, and context doesn't disappear between sessions.

---

## Guidelines and Patterns

As you build more features, you'll notice patterns. Good things to capture:

- Architectural patterns that work (dependency injection, service layer structure, etc.)
- Testing patterns that make sense for your stack
- UI patterns and conventions
- Naming conventions and terminology

When you notice a pattern that's stable and worth codifying, run `/bob:guidelines` to capture it. These guidelines load automatically in future brainstorms and reviews. They elevate code quality over time without you having to repeat yourself.

See [Knowledge Management](05-knowledge-management.md) for details.

---

## The Discipline

The reason this works is session boundaries. Each session is:
- Focused on one phase
- Starting fresh with no memory of previous conversations
- Producing a clear artifact
- Requiring human sign-off before moving forward

You avoid the trap of "we've been talking about this for 3 hours, I guess we should implement it." Each phase has its own decision point. Each decision is recorded. Each artifact is read again before the next phase.

This discipline is what maintains quality over time. It's also what makes it possible for someone else to pick up mid-project and understand everything that's happened.

---

## Next Steps

- Read [Project Management](04-project-management.md) to understand how to organize stories and tasks.
- Read [Commands Reference](06-commands-reference.md) for details on each command.
- Ready to start? Run `/bob:brainstorm` on your first feature.
