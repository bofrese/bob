# Bob User Guide
*Last updated: 2026-06-23*

Bob is a set of Agent Skills (a Claude Code plugin) for structured, AI-assisted product development. From first idea through shipped, tested, documented code - with human judgment at every decision point.

This guide is organized around what you actually *do*, not what bob *has*. Pick your starting point based on where you are:

## I'm new to Bob
Start here: **[Getting Started](01-getting-started.md)** - Installation, your first session, what happens next.

## I'm planning a feature or thinking through a problem
Read: **[Engineering Workflows](02-engineering-workflows.md)** - The core pipeline: Brainstorm → Design → Plan → [Review Plan] → Implement → Review → Document → Handover → Reflect → Learn (proportional - small work stays on the `/bob:dev` fast path).

## I'm designing a product or validating an idea
Read: **[Discovery Workflows](03-discovery-workflows.md)** - Vision, personas, business model, validation strategy.

## I'm trying to understand how to organize my project
Read: **[Project Management](04-project-management.md)** - How stories work, the kanban system, tracking progress across sessions.

## I'm trying to keep documentation in sync with my code
Read: **[Knowledge Management](05-knowledge-management.md)** - Architecture notes, guidelines, the knowledge vault, and what goes where.

## I need to look something up quickly
Use: **[Skills Reference](06-skills-reference.md)** - Tables organized by layer, what each skill does.

## Something isn't working or feels confusing
Read: **[Troubleshooting](07-troubleshooting.md)** - Known friction points and how to resolve them.

---

## The Two Fundamental Principles

Everything Bob does rests on two ideas:

**You decide, AI explores.** Every session is a conversation. The AI generates options, surfaces trade-offs, challenges your assumptions. You pick the direction. Nothing ships without your sign-off.

**Just describe your work.** In a project that uses bob, a session primer and the `bob` hub skill make sure the right phase starts - you do not have to remember the skill names.

**Files are the memory.** Each skill writes its output to a well-known file location. Close your laptop, come back tomorrow, hand off to a colleague - the context lives in the files, not the chat history. This is also what makes honest review possible: a plan written in one session is reviewed fresh in another, with no memory of the conversation that produced it.

---

## Quick Start

1. **Install Bob** (if you haven't):
   ```
   /plugin marketplace add bofrese/claude-plugins
   /plugin install bob@bofrese-plugins
   ```

2. **Bootstrap your project** (new projects only):
   ```
   /bob:setup
   ```
   Creates the folder structure, knowledge vault, and project infrastructure in one go.

3. **Open Claude Code in your project directory** and pick your first skill:
   - New product? Start with `/bob:product` for comprehensive discovery.
   - Have an idea to build? Start with `/bob:brainstorm`.
   - Want a project overview? Start with `/bob:bob` for a status check and recommendations.

4. **Read the output carefully.** It's your first draft, not gospel. Engage with it. Push back on assumptions. Edit the plans. When you're happy, move to the next phase.

5. **Come back to this guide** when you need context on how something works or when you hit friction.

---

## How to Use These Guides

- **Each guide is self-contained.** You can read them in any order based on what you need right now.
- **They describe what actually happens**, not what's supposed to happen. If you find gaps between the guide and reality, that's a finding worth noting.
- **They're task-oriented.** "How do I track progress on a feature?" beats "Here's what a kanban is."
- **They assume you have Claude Code open** and can run skills. References like `/bob:plan` are skills you can invoke.

---

## Feedback

If you find gaps, contradictions, or confusing sections, that's valuable. The guides surface what's unclear or missing in the system itself. Open an issue or reach out - this is a new system and user perspective helps sharpen both the implementation and the docs.
