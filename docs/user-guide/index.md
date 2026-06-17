# Bob User Guide
*Last updated: 2026-06-16*

Bob is a Claude Code plugin for structured, AI-assisted product development. From first idea through shipped, tested, documented code—with human judgment at every decision point.

This guide is organized around what you actually *do*, not what bob *has*. Pick your starting point based on where you are:

## I'm new to Bob
Start here: **[Getting Started](01-getting-started.md)** — Installation, your first session, what happens next.

## I'm planning a feature or thinking through a problem
Read: **[Engineering Workflows](02-engineering-workflows.md)** — The core pipeline: Brainstorm → Plan → Implement → Review.

## I'm designing a product or validating an idea
Read: **[Discovery Workflows](03-discovery-workflows.md)** — Vision, personas, business model, validation strategy.

## I'm trying to understand how to organize my project
Read: **[Project Management](04-project-management.md)** — How stories work, the kanban system, tracking progress across sessions.

## I'm trying to keep documentation in sync with my code
Read: **[Knowledge Management](05-knowledge-management.md)** — Guidelines, documentation, what to capture and when.

## I need to look something up quickly
Use: **[Commands Reference](06-commands-reference.md)** — Tables organized by layer, what each command does.

## Something isn't working or feels confusing
Read: **[Troubleshooting](07-troubleshooting.md)** — Known friction points and how to resolve them.

---

## The Two Fundamental Principles

Everything Bob does rests on two ideas:

**You decide, AI explores.** Every session is a conversation. The AI generates options, surfaces trade-offs, challenges your assumptions. You pick the direction. Nothing ships without your sign-off.

**Files are the memory.** Each command writes its output to a well-known file location. Close your laptop, come back tomorrow, hand off to a colleague — the context lives in the files, not the chat history. This is also what makes honest review possible: a plan written in one session is reviewed fresh in another, with no memory of the conversation that produced it.

---

## Quick Start

1. **Install Bob** (if you haven't):
   ```bash
   git clone https://github.com/bofrese/bob.git ~/.claude/plugins/bob
   ```

2. **Open Claude Code in your project directory** and pick your first command:
   - New product? Start with `/bob:product-coach` for comprehensive discovery.
   - Have an idea to build? Start with `/bob:brainstorm`.
   - Want to improve your workflow? Start with `/bob:pm` for a project status check.

3. **Read the output carefully.** It's your first draft, not gospel. Engage with it. Push back on assumptions. Edit the plans. When you're happy, move to the next phase.

4. **Come back to this guide** when you need context on how something works or when you hit friction.

---

## How to Use These Guides

- **Each guide is self-contained.** You can read them in any order based on what you need right now.
- **They describe what actually happens**, not what's supposed to happen. If you find gaps between the guide and reality, that's a finding worth noting.
- **They're task-oriented.** "How do I track progress on a feature?" beats "Here's what a kanban is."
- **They assume you have Claude Code open** and can run commands. References like `/bob:plan` are commands you can invoke.

---

## Feedback

If you find gaps, contradictions, or confusing sections, that's valuable. The guides surface what's unclear or missing in the system itself. Open an issue or reach out—this is a new system and user perspective helps sharpen both the implementation and the docs.
