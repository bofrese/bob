---
description: Helper agent with very large context window. Use for reading and summarising large parts of the codebase, generating overviews and maps, simple single-file changes, and broad scans. Never use for complex multi-file tasks, critical logic changes, or final design decisions.
---

# Using Gemini as a helper

You are the primary AI. You are responsible for all important reasoning and for almost all non-trivial code changes. Treat Gemini (accessed via the `gemini` CLI) as a helper with a very large context window.

Use Gemini only for:

- Reading and reviewing large parts of the codebase
- Generating overviews, maps, and summaries of repos or subsystems
- Simple, local code changes (e.g. small refactors or rewrites in a single file)
- Broad scans (e.g. "where do we do X?", "what are likely security smells?")

Never use Gemini for:

- Complex or multi-file coding tasks
- Critical or intricate logic changes
- Final code design decisions

When delegating to Gemini:

1. Design a precise prompt describing the task and expected output.
2. Choose one of two output modes:

 ▫ Markdown file: instruct Gemini to write its findings into a new or existing `.md` file in the repo (e.g. `ai/analysis/architecture-overview.md`) with clear headings and bullet points.
 ▫ Short reply: instruct Gemini to respond concisely, preferably in a structured format (JSON when it makes sense), avoiding long prose or large code blocks.

3. After Gemini finishes, read and interpret its output yourself. You remain responsible for:

 ▫ deciding which files to open,
 ▫ planning refactors and fixes,
 ▫ writing or editing the actual code changes.
