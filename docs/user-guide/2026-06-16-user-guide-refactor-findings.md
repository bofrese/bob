# User Guide Refactor — Findings Report
*Date: 2026-06-16 | Previous: `bob/docs/user-guide.md` (675 lines) | New: `bob/docs/user-guide/` folder (2,052 lines across 8 files)*

## Summary

Refactored the monolithic user guide into 7 task-focused guides organized by user goal. Maintains same scope and depth while improving discoverability and reducing cognitive load. Particularly strengthened Project Management and Knowledge Management sections (new material not in previous version).

---

## What Changed

### Organization
- **Before:** One 675-line file covering philosophy → commands → systems
- **After:** 7 focused guides (~250-400 lines each) + index, organized by user task

### New Structure
1. **Index** — Entry point, navigation to all guides
2. **Getting Started** — Installation, first session
3. **Engineering Workflows** — Brainstorm → Plan → Implement → Review cycle (with review-plan critical step)
4. **Discovery Workflows** — Product strategy commands (optional but thorough)
5. **Project Management** — How stories, tasks, and kanban boards work (greatly expanded)
6. **Knowledge Management** — Guidelines, documentation, how they stay in sync (greatly expanded)
7. **Commands Reference** — Quick lookup, all 30 commands organized by layer
8. **Troubleshooting** — Known friction points and solutions

### Content Improvements

**Project Management** (new/expanded):
- Added concrete folder structure with relative paths
- Detailed story lifecycle: creation, folder layout, status tracking
- Explained kanban columns at both project and story level
- Added task file templates
- Added guidance on discovering and tracking issues
- Added section on multi-project structure
- Added tips for keeping story folders clean

**Knowledge Management** (new/expanded):
- Separated Guidelines from Documentation (was conflated)
- Explained why both exist and when each is used
- Added "Knowledge Loop" section showing how knowledge accumulates
- Added section on maintaining guidelines (quarterly refresh, evolution)
- Added Knowledge Inbox pattern (for Obsidian users wanting to capture insights)
- Explained drift detection and maintenance mode

**Engineering Workflows** (improved):
- Moved "Review the Plan" to be prominent — it's critical and often skipped
- Added "What If?" section for common mid-workflow problems
- Explained the rhythm (Day 1 brainstorm, Day 2 plan, etc.)
- Connected to guidelines explicitly

**Getting Started** (new, concise):
- Shortened from monolithic "Philosophy" section
- Focused on "what now?" instead of "why this exists"
- Clear file location mental model upfront

---

## Findings: Gaps & Ambiguities Surfaced

### Project Management System — Implementation Clarity Issues

| # | Issue | Severity | Finding |
|---|-------|----------|---------|
| 1 | **Story context detection is fragile** — Bob tries Obsidian tabs, recent files, then falls back to asking. But which method actually works reliably? Users will hit the fallback and might not understand the hierarchy. | Medium | Document the resolution chain more clearly in Getting Started. Add troubleshooting for "which method was tried?" |
| 2 | **INBOX vs ToDo distinction unclear** — Both are "uncommitted" in some sense. When do you move from INBOX to ToDo? What's the decision point? Current docs say "candidates vs committed" but don't explain the workflow. | Medium | Add a "Moving cards" section with decision framework. "INBOX = ideas I haven't validated. ToDo = I decided to do this." |
| 3 | **`_index.md` history table maintenance** — Docs say Bob updates it automatically. But for manually-created artifacts (notes, edge-case documents), what's the format? When should users update it themselves? | Low | Add explicit guidance on manual history entry format. When Bob's involved, format is clear. When it's not, currently ambiguous. |

### Knowledge Management System — Structure & Maintenance Gaps

| # | Issue | Severity | Finding |
|---|-------|----------|---------|
| 4 | **Guidelines loading timing** — Docs say guidelines "load automatically in future sessions." But are they loaded at session *start*? After scope is clear? For every brainstorm or only specific commands? Actual timing unclear from `/bob/skills/context-protocol/SKILL.md`. | Medium | Clarify in Knowledge Management guide: "Guidelines load after scope is clear (you've picked your story/area)." Or check if this is actually implemented correctly. |
| 5 | **Guidelines vs Documentation boundary is still soft** — Guide tries to clarify (Guidelines = how we do X, Docs = what we built). But in practice: is a "React Component Pattern" guide or doc? Is "API Response Format" guide or doc? Users will create duplicates or misplace things. | Medium | Add decision framework with examples in Knowledge Management: use a 2x2 (project-specific vs generic, practice vs artifact) to help users place things. |
| 6 | **`docs/guidelines/` doesn't have its own index** — Unlike `docs/product/` and main `docs/README.md`, there's no `docs/guidelines/README.md` to navigate what's been created. Users creating guideline #3 don't know what guidelines #1-2 were. | Medium | Recommend creating `docs/guidelines/README.md` as the index. Either `/bob:guidelines` should create it, or users should maintain it manually. |
| 7 | **Knowledge Inbox pattern is optional but powerful — not discovered** — Guide mentions it but buries it at the end. It's actually a great way to capture insights without context-switching. Should be higher in Knowledge Management. | Low | Promote Knowledge Inbox to a main section in Knowledge Management guide. It's useful enough to highlight. |
MY NOTES: 
6) I can se that another project it have included both guidelines and other docs in the docs/README.md - not a separate docs/guidelines/README.md . Which might work well - but I can see the reason to split it. The intent is that guidelines are for code and architecture guidelines - how to use language features libraries etc. - i.e. guidelines you need to know when building new things.  The other docs/ are documentation of what have been build. Of course when building new things you also need to be aware of what have been build - so a coding agent would typically need to read both.


### Done-Criteria System — Visibility & Adoption

| # | Issue | Severity | Finding |
|---|-------|----------|---------|
| 8 | **Done-criteria file is created but often ignored** — Guide doesn't explain why it matters or what it's for. It's mentioned in passing. Users see `docs/process/done-criteria.md` exist, don't understand what it's tracking, don't engage with it. | Medium | Add "Done Criteria" section to Project Management (or Knowledge Management). Explain what it tracks, why it matters, how to read it. Link to the actual file's content. |
| 9 | **Discovered issues tracking could be clearer** — Done-criteria protocol has complex logic about where issues go (story issues, project inbox, separate story candidate). Guide doesn't explain when to use which. | Medium | Add decision tree in Troubleshooting: "When I find a bug, where does it go?" |

### Story Context Resolution — Edge Cases

| # | Issue | Severity | Finding |
|---|-------|----------|---------|
| 10 | **Path-derived detection (Tier 1) — might be too strict** — If user runs `/bob:plan projects/app/stories/APP-001/2026-06-16-brainstorm.md`, the path *includes* the story ID, so it should work. But what if they pass just the story folder path? What if they pass a plan file that isn't in a story folder? | Low | Test Tier 1 detection. If there are edge cases, document them in Troubleshooting. |

---

## Unverifiable Features

Features mentioned in the system that I couldn't fully verify in code/docs:

- **Obsidian story detection (Tier 3-4 of story-context)** — Skill file exists and defines the protocol, but I couldn't verify whether the detection scripts actually work and reliably detect story folders. Assuming they work as documented.
- **Guidelines auto-loading in brainstorm** — Documented that `/bob:brainstorm` loads relevant guidelines, but didn't trace exactly when/how this happens. Assuming it works as context-protocol defines.
- **Daily note tracking** — Done-criteria mentions `personal/daily/YYYY-MM-DD.md` for personal tracking. This is very specific and Optional. Seems like an advanced pattern that may not be widely used.

---

## Opportunities for Improvement

### High Priority
- **Add `docs/guidelines/README.md` index.** Guidelines need a navigation layer like product docs have. Without it, users don't know what already exists.
- **Clarify INBOX vs ToDo decision workflow.** This is where projects actually get managed, but the distinction is vague.
- **Make done-criteria visible and explained.** It's powerful but currently invisible to users. Promote it.

### Medium Priority
- **Create a "Migration Guide"** for users switching from the old monolithic guide to the new structure. "The Project Management section is entirely new. The Engineering Workflows section changed significantly. Philosophy moved to Troubleshooting."
- **Expand Project Management "Tips" section** with real scenarios: "I have 3 concurrent features. How do I organize stories?" "Should I create sub-stories?" "When do I archive a story?"
- **Clarify guidelines loading timing.** Document exactly when guidelines are loaded relative to when a user picks their scope/story.

### Low Priority
- **Strengthen Troubleshooting with video references** (if any exist). "This is a common pattern—see the demo here."
- **Add a "Decision Log" template** to Project Management. Mentions decisions are captured, but doesn't provide a standard format for story-level decisions.

---

## Recommendations

### What to Do With the Old Guide

**Option 1 (Recommended): Archive it**
- Move `bob/docs/user-guide.md` to `bob/docs/user-guide/archive/user-guide-monolithic-original.md`
- Update `bob/README.md` to point to the new `docs/user-guide/index.md`
- Add a note in the archived file: "This is the original monolithic guide. It's been refactored into focused guides. Start here: [link to index]"

**Option 2: Keep both during transition**
- Keep old file as-is for 1-2 weeks so users with bookmarks/links don't break
- Add a banner at the top: "This guide has been refactored. Start here: [link to new index]"

I recommend Option 1. The new guides are comprehensive and better organized.

### Next Steps

1. **Address high-priority findings** (Guidelines index, INBOX/ToDo clarity, done-criteria visibility)
2. **Test Obsidian story detection** — verify Tier 1-4 actually work as documented
3. **Create guidelines index** — either add to `/bob:guidelines` command or document as manual task
4. **Add done-criteria visibility** — consider promoting it in Project Management or making it required reading

---

## Process Notes

During refactoring, I was writing from the user's perspective and discovered gaps by trying to explain concepts. These findings emerged naturally—not from testing the code, but from testing the *explanations* against user needs.

**Strong areas:** Engineering workflow is solid and clear. Discovery commands are well-designed.

**Weak areas:** Project management and knowledge management are new-ish and have operational ambiguities that'll surface as users adopt them. Worth observing and iterating.

**Worth validating:** Obsidian integration. If it's critical for story detection and it's fragile, users will hit friction quickly.
