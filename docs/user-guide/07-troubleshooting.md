# Troubleshooting
*Last updated: 2026-06-16*

Known friction points and how to resolve them.

## Installation & Setup

### "I installed Bob but the commands don't show up"

**Check:** Did you restart Claude Code after installing?

Plugins need a restart to load. Close and reopen Claude, or in the terminal:

```bash
claude --reload-plugins
```

**Check:** Is the plugin in the right place?

User-level (all projects):
```bash
ls ~/.claude/plugins/bob
```

Project-level (current project):
```bash
ls .claude/plugins/bob
```

If one exists, that's the one being used. The project-level takes precedence.

**Check:** Is it a valid plugin?

Inside the bob folder, there should be a `.claude-plugin/` folder:
```bash
ls .claude/plugins/bob/.claude-plugin/plugin.json
```

If that file doesn't exist, the clone didn't work. Try cloning again.

---

## Story Context & Project Management

### "Bob asks me to pick a story but I haven't created one yet"

Say "new story". Bob will ask you to name it and set up the folder structure.

Or manually create `projects/[PROJECT]/stories/[ID]/` with `_index.md` and `_kanban.md` (templates in [Project Management](04-project-management.md)).

### "I can't remember which story I was working on"

Run `/bob:pm` — it shows recent activity and can tell you which stories are in progress.

Or check your Obsidian vault — Bob tries to detect open or recently-edited story files automatically.

### "The story folder got created but Bob can't find it"

**Check:** Is it in the right place?

Bob looks for stories at: `projects/[PROJECT]/stories/[STORY-ID]/`

If yours is somewhere else (e.g., `ai/stories/`), move it or create the expected structure.

**Check:** Does `_index.md` exist in the story folder?

If not, create it (template in [Project Management](04-project-management.md)).

### "I have multiple story candidates and Bob asks me to pick"

This is actually a good moment to be explicit. You're choosing what to work on. Pick one. If you want to work on multiple, do them sequentially (one session per story).

---

## Brainstorming

### "The brainstorm output doesn't feel complete"

Brainstorms are first drafts. They're conversations between you and the AI. If something feels incomplete:
1. Ask the AI follow-up questions in the same session.
2. Have it revise the section before writing the file.
3. Only save when you're satisfied.

The report should include enough that someone (including yourself in 3 months) can understand what you decided and why.

### "I'm not converging on a direction"

You're in the Diverge phase too long. Move to Converge:
- Name your selection criteria: effort, impact, user value, technical fit, simplicity
- Rank the options against those criteria
- Pick the top 1-2

Perfectionism is a failure mode. "Good enough that I can plan it" is the threshold.

### "I'm saving a brainstorm but realized we missed something"

That's fine. Save it. Then run another brainstorm on the same story for the missing aspect. Or save and immediately run `/bob:plan` — the planning phase often surfaces what the brainstorm missed.

---

## Planning

### "The plan is too detailed / not detailed enough"

**Too detailed:** Plans should be concept-level. If you're writing pseudocode or explaining every line, you're overcomplicating. Simplify to the approach and steps.

**Not detailed enough:** The Questions & Decisions table should flag uncertainties. If it doesn't, either the plan is over-confident or you missed something. When in doubt, ask in the plan review.

### "The Questions & Decisions table has things I don't agree with"

Edit it. The plan is yours. Change the AI's answers to match your judgment. Make sure the reasoning is clear.

When you ask Bob to write the final report, mention what you changed and why. This becomes part of the record.

### "The plan doesn't fit the codebase"

That's what the review-plan phase is for. Run `/bob:review-plan`. If it also flags a bad fit, the plan needs rework before implementation.

---

## Plan Review

### "The review contradicted something in the plan"

Great—that's the review working. Read the contradiction carefully. The review might be wrong, or the plan might need adjustment.

Update the plan to address the finding. Then re-run `/bob:review-plan` or at least carefully verify the fix before implementing.

### "The review approved it but I'm still worried"

Trust your instinct. If something feels off, ask the AI more questions before implementing. Better to catch problems now than after coding.

### "The review and plan disagree but I think they're both right"

They're probably right about different things. Synthesize: what's the resolution that satisfies both? Update the plan with the resolution.

---

## Implementation

### "Implementation hit a problem the plan didn't anticipate"

Bob stops and asks. Answer the question. It's information the plan was missing.

After the session, consider whether the plan should have caught this. If so, that's a learning for how to plan better next time. If the problem was genuinely unexpected, it's fine—the implementation report notes it.

### "I disagree with how the AI implemented something"

Stop the session. Revise the implementation yourself. Or ask the AI to do it differently. You're in control.

Make a note of what you changed and why in the implementation report.

### "Tests are failing"

The AI runs tests after each change. If tests fail:
1. The AI should catch it and ask what's wrong
2. If it doesn't, run the tests yourself and fix the failures
3. Re-implement that section or resume from the last green state

Tests are your safety net. Don't skip them.

---

## Code Review

### "The review found lots of issues"

That's valuable. Each issue is a thing that needs fixing, or a thing the review got wrong.

Go through them one at a time:
- **Agree?** Fix it.
- **Disagree?** Say why. You're not obligated to fix everything the review suggests.

When you're done, the codebase should be in a state you're happy to ship.

### "The review and the plan disagree"

The review is checking against current reality (code, guidelines). The plan was written before implementation. One or both might be right. Read carefully and decide what's correct.

If the code doesn't match the plan, either the code needs fixing or the plan needs revision. Fix whichever is wrong.

### "The review is very long"

Big changes get long reviews. If you want shorter feedback, break changes into smaller pieces.

---

## Documentation

### "Documentation feels out of date"

Run `/bob:document` in maintenance mode. It detects what's drifted and flags it.

Update the docs. Or if something's no longer relevant, remove it.

### "I'm not sure what to document"

After shipping, run `/bob:document` without specifying a topic. It scans the code and tells you what's missing.

Document high-level decisions, architecture, and features. Don't document implementation details that the code makes clear.

---

## Guidelines

### "I created a guideline but nobody follows it"

Reasons:
1. **It's not loaded.** Guidelines in `docs/guidelines/` are loaded by engineering commands automatically—but only if they're there *before* the session starts. Did you create it? Does the file exist?
2. **It's too vague.** "Be clean" doesn't help. "Use composition over inheritance, one component per file, lift shared state to parent" does.
3. **It contradicts the code.** If 80% of your code doesn't follow the guideline, the guideline is wrong. Update it.

### "The guideline is outdated"

Update it. Quarterly, run `/bob:guidelines` on a technology to check alignment with official standards.

### "I want to enforce guidelines with linting"

Great. Add the linting section to the guideline. The next code review will verify linting is set up.

---

## Project Organization

### "My projects/ folder is messy"

Archive old stories. Keep the kanban board current. Move completed stories to DONE. Keep the folder structure clean.

Messy project state makes it hard to find context. Spend 10 minutes every week cleaning it up.

### "I have too many stories in-progress"

Kanban is a visibility tool. If you have 10 stories in the In Progress column, you're not managing workflow—you're just tracking. Limit to 2-3 stories in progress. Finish them or move them to Blocked.

### "The kanban board doesn't match what I'm actually working on"

Update it. The board is your source of truth for project state. If it's wrong, it's a liability not a help.

---

## Memory and Context

### "Bob loaded the wrong vision or guideline"

The context-protocol skill loads documents from well-known paths. If the wrong file is being loaded:
- Check where the file actually is
- Check whether multiple versions exist (maybe one in `docs/product/` and one elsewhere)
- Delete duplicates or move files to standard locations

### "I want Bob to load a specific file"

If a file isn't being loaded automatically, mention it in the session:
> "Please read this file for context: [path]"

Or use the Skill tool directly to invoke context-protocol manually.

### "Previous sessions' context is bleeding into this session"

Each session should start fresh. If you notice Bob remembering things from a previous session that shouldn't carry over, that's a bug. Reset by:
1. Close Claude completely
2. Reopen
3. Run the command again

If it persists, it might be a Obsidian detection issue. Check the story-context skill documentation.

---

## General Friction

### "I feel like I'm doing too much ceremony"

You might be. Bob is opinionated about discipline. If phases feel heavyweight:
- Brainstorm and plan can be combined for tiny changes (small bug fix, copy edit)
- You can skip review-plan for very straightforward changes
- You can skip documentation for minor fixes

But for features, the ceremony has a purpose: each phase catches things the previous one missed. It's not wasted time.

### "I'm working on a small bug that doesn't need a story"

You can. Use Claude normally without Bob. Bob is best for:
- Features (anything worth planning)
- Refactors (anything that changes architecture)
- Investigations (bugs that need diagnosis)

Quick copy fixes or one-line fixes can skip Bob.

### "The commands are slow"

Commands can be slow if:
- The codebase is huge (AI reads a lot of files)
- The task is complex (AI explores multiple approaches)
- Context loading is slow (lots of discovery files)

This is normal. Patience. Or reduce context if you know a narrower scope.

---

## Reporting Issues

If you hit something that feels like a bug:

1. **What were you trying to do?** (run `/bob:brainstorm`, `/bob:implement`, etc.)
2. **What happened?** (output was wrong, command crashed, asked unexpected question, etc.)
3. **What did you expect?** (should have asked X, should have output Y, etc.)
4. **Reproduce:** Can you run the command again and see the same issue?

Open an issue on GitHub with these details.

---

## Next Steps

Still stuck? Run `/bob:pm` — the project mentor has holistic view of the system and can suggest next steps based on your specific situation.
