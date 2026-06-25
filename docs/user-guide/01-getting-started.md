# Getting Started with Bob
*Last updated: 2026-06-23*

This guide covers installation and your first session—from "what is this?" to "I just finished my first brainstorm."

## What is Bob?

Bob is a Claude Code plugin that structures AI-assisted development into phases:
- **Discovery:** Figure out what to build and why (optional, standalone)
- **Engineering:** Build it disciplined (brainstorm → plan → implement → review)
- **Knowledge:** Capture guidelines and documentation so every future session is better

Each phase is a separate session with a clear command. Each session writes its output to files. The next session reads those files. You decide at every step—the AI explores options and surfaces trade-offs.

## Installation

### Option 1: User-level (recommended)
Available in all your projects:

```bash
git clone https://github.com/bofrese/bob.git ~/.claude/plugins/bob
```

Update later:
```bash
cd ~/.claude/plugins/bob && git pull
```

### Option 2: Project-level
Only in the current project:

```bash
git clone https://github.com/bofrese/bob.git .claude/plugins/bob
```

## Your First Session

Here's what a typical first session looks like:

### 1. Open Claude Code in your project
```bash
cd /path/to/your/project
claude
```

### 2. Run `/bob:setup` on a new project
If this is a brand-new project (or you've just installed bob on an existing one), run:

```
/bob:setup
```

It audits what's present, shows you a summary, and with one confirmation creates everything missing:
- `projects/` folder with your first subproject and kanban board
- `knowledge/` vault for capturing learnings
- `personal/daily/` for daily notes (where pm can append status summaries)
- `.gitignore` entries to keep private folders local
- `docs/process/done-criteria.md`

Idempotent — safe to run on any project, new or existing. Skip this if you're returning to an established project.

### 3. Run `/bob:pm` to see where you are
The project mentor reads your kanban boards and tells you what's in flight, what's ready, and what to work on next.

### 4. Pick your starting point

**Brand new product?**
Run `/bob:product-coach`. It guides you through vision, validation, business model, and positioning.

**Have a feature idea?**
Run `/bob:brainstorm`. The AI asks structured questions to help you think it through. You leave with a clear direction documented.

**Not sure where to start?**
Just say "Hi Bob, where should I begin?" — Bob reads what exists and tells you exactly what to do first.

**Inherited a codebase with no docs?**
Run `/bob:document`. It scans what you have and captures it.

**Want better development workflows but not product stuff?**
Skip Discovery. Start with `/bob:brainstorm` for your next feature.

### 4. Engage with the output

Every command produces a report—a brainstorm, plan, review, or implementation report. **Read it carefully.** The AI has done the groundwork (read the codebase, thought through options, made assumptions). Now you engage with it.

- Does the plan make sense? Push back on parts that don't.
- Are there questions you want to explore deeper? Ask them.
- Should we do it differently? Say so. The AI can revise.

When you're ready, ask the AI to write the final report to a file.

### 5. You're done for this phase

Close Claude. Files are saved. You can come back tomorrow, or hand off to a colleague. Everything they need is in the files—no chat history required.

## File Locations

Bob creates files in four places. Understanding this prevents confusion:

| Folder | What lives here | Lifespan |
|--------|-----------------|----------|
| `docs/product/` | Vision, personas, design briefs, business model | Permanent — read and updated in place |
| `docs/guidelines/` | Best-practice guides for your tech stack | Permanent — reference and maintain |
| `projects/` | Stories, plans, brainstorms, implementation notes | Working memory — organized by story |
| `personal/` | Daily notes, weekly notes, scratchpad | Local only (gitignored) |

**Key insight:** `projects/` is where decisions live. `docs/` is what you ship and maintain. They work together — engineering commands read vision from `docs/`, write plans to `projects/`.

`personal/` and `knowledge/_INBOX/` are gitignored by default — they're for you, not the team.

## Your Second Session

New day, new idea. You open Claude again:

```bash
/bob:brainstorm
```

Bob asks which story you're working on (it tries to detect it from Obsidian tabs or recent files). You confirm or specify. Then you brainstorm, and it writes to `projects/[subproject]/stories/[ID]/`.

The next day:

```bash
/bob:plan projects/[subproject]/stories/[ID]/2026-06-16-brainstorm-notifications.md
```

Bob reads your brainstorm, examines the codebase, and walks you through a detailed plan.

This is the flow: each command reads the previous command's output. Files are the memory. Each session is focused and independent.

## What Not to Do

- **Don't try to brainstorm, plan, and implement in one session.** Session boundaries exist for a reason—they keep context clean and force you to make decisions explicit. One command, one session, one artifact.

- **Don't skip reading the output.** The AI made assumptions. Your job is to verify they're right before they become code.

- **Don't expect perfection on first draft.** Plans will need refinement. Code will need review. This is normal. The process surfaces and corrects problems—that's the whole point.

- **Don't work in chat history.** If you change files directly in code, run the appropriate command (`/bob:review`, `/bob:implement`) so the artifact matches reality.

## Key Commands for Getting Started

| Command | When to use | Output |
|---------|------------|--------|
| `/bob:pm` | "What should I do next?" — project status and recommendations | Status report (optional) |
| `/bob:brainstorm` | "I have an idea for a feature" | `{story_path}/{date}-brainstorm-{slug}.md` |
| `/bob:plan` | "Turn this brainstorm into a plan" | `{story_path}/{date}-plan-{slug}.md` |
| `/bob:implement` | "Execute this approved plan" | Modified code + implementation report |
| `/bob:review` | "Is this code ready to ship?" | Code review report |

See [Commands Reference](06-commands-reference.md) for the full list.

## Next Steps

- Read [Project Management](04-project-management.md) to understand how stories and tasks work.
- Read [Engineering Workflows](02-engineering-workflows.md) to see the full brainstorm → plan → implement → review cycle.
- Read [Knowledge Management](05-knowledge-management.md) when you've shipped your first feature and need to document it.

## Troubleshooting

**Bob asks for a story context and I don't have one yet**

If you're starting completely fresh, say "new story" and Bob will set one up. If you want to understand story structure first, read [Project Management](04-project-management.md).

**I closed Claude and can't remember what I was working on**

That's fine. Run `/bob:pm` to see recent activity and pick up where you left off.

**I want to work on just one small file without all the ceremony**

You can use Claude for that without Bob at all. Bob is best for features, refactors, and any work where planning matters. For a quick fix, just use Claude normally.
