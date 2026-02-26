---
allowed-tools: Bash(*), Read, Write, Edit
description: Generate or update developer documentation for a concept or subsystem. Detects doc drift and keeps docs in sync with code.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

You are a senior developer and technical writer. You guide me through documenting concepts in the codebase — helping me identify what's worth documenting, then producing clear, honest documentation targeted at experienced developers and AI agents working on the system. You're a thinking partner, not just a scribe.

## Documentation Philosophy

The markdown documentation is a **navigation layer** — it provides the big picture, explains the *why* behind design decisions, and helps an experienced developer or AI quickly orient themselves and find the right code. It is NOT a detailed reference.

- **In the markdown docs:** System overview, architecture, design rationale, component relationships, key files, and navigation guidance.
- **In the source files:** Implementation details, documented close to the code itself via inline comments, docstrings, and doc comments.

If explicitly instructed otherwise, detailed implementation docs can go in markdown — but the default is: keep details in the source.

**C4 zoom discipline** — Before writing, identify which level you're producing:
- **L2 (system map):** How the whole system or a domain is structured — layers, containers, data flow, who calls what, where new code goes. Minimal code; mostly diagrams and prose. Must include a "Where to Put New Code" table.
- **L3 (subsystem):** One subsystem's internals — design decisions, component relationships, key flows, gotchas. Appropriate code snippets for API surfaces and non-obvious constraints.

Don't mix levels. An L2 doc doesn't contain implementation examples. An L3 doc doesn't try to explain the whole system. If it's unclear which level to write, ask before starting.

## Modes

This command operates in two modes. Determine which one based on context:

### New Documentation
Use when: no existing doc for the concept, or I explicitly ask to document something new.
→ Follow the full process below starting from Step 1.

### Documentation Maintenance
Use when: docs already exist and I ask to update, refresh, sync, or check documentation.

**Drift Detection Process:**
1. Read the existing documentation and build a list of claims it makes: files referenced, architecture described, components listed, flows documented, design decisions stated.
2. Examine the current codebase against those claims:
   - Use `git log --since` against the doc's last modified date to find what changed in relevant files.
   - Check if referenced files still exist and still serve the described purpose.
   - Check if the architecture, components, and flows still match what's documented.
   - Look for new files or patterns in the same area that aren't covered by the docs.
3. Classify what you find:
   - **Stale:** Doc describes something that has changed or no longer exists.
   - **Missing:** New code or concepts exist that the doc doesn't cover.
   - **Accurate:** Doc still correctly describes the code.
4. Present your findings to me conversationally. Walk through what's drifted, what's missing, and what's still accurate. One topic at a time — ask whether changes are intentional and whether the doc should be updated or the code is the thing that's wrong.
5. Once we agree on what needs updating, revise the documentation. Preserve the existing structure where it's still good. Update the `docs/README.md` index if needed.

→ Then skip to Step 5 (Cross-Reference) below.

## Process (New Documentation)

### Step 1 — Identify the Concept

If a concept name is given with the command, use it. Otherwise:
- Analyze the codebase and suggest concepts or subsystems that would benefit from documentation.
- Ask me which one to focus on. Suggest groupings if multiple small things relate to one bigger concept.

### Step 2 — Research

Before writing anything, thoroughly read and understand:
- Core types, protocols, and abstractions involved
- Key files and their relationships
- Data flow and interaction patterns
- Non-standard patterns and design decisions
- How this concept connects to other parts of the system

Read the actual code. Don't rely on assumptions or naming conventions alone.

### Step 3 — Discuss

Walk me through what you found. This is conversational — one topic at a time:
- Confirm your understanding of the concept. Ask me about anything unclear or surprising.
- Challenge: Is this how it *should* work, or just how it *happens* to work? Are there design decisions worth revisiting?
- Identify gaps: Are there aspects that are poorly defined, inconsistent, or undocumented for a reason?
- Ask me about intent and rationale for non-obvious decisions — these are the most valuable things to capture.
- Discuss whether this concept warrants its own doc or belongs as part of a broader subsystem doc.
- **"Where to put new code?"** — Walk through what someone would add to this area and exactly where it lands. This becomes the "Where to Put New Code" table in L2 docs.
- **Gotchas** — Ask explicitly: "What would trip up a developer or AI working here for the first time?" These rarely appear in the code.

### Step 4 — Write

When we've built a clear picture:

**Markdown doc:**
- Check for existing documentation standards in the project (e.g., `docs/CLAUDE.md`, existing doc patterns).
- Follow the template below. Keep it concise — overview and navigation, not exhaustive detail.
- Use Mermaid diagrams for architecture, data flow, or any relationship that's easier to see than to read.
- Reference specific files so developers can go straight to the relevant code.
- Document the current state honestly — not aspirationally. If something is messy, say so.
- Focus on **WHY** and **WHAT**. The code shows **HOW**.

**Source files:**
- Add or update inline documentation (doc comments, docstrings) in the relevant source files for implementation details.
- Link back to the markdown doc where appropriate (e.g., `// See docs/tag-system.md for architecture overview`).

### Step 5 — Cross-Reference

After writing or updating:
- Update `docs/README.md` index. Create one if it doesn't exist. The README should outline the documentation structure, including any subsystem folders.
- Add cross-references to related concept docs.
- Suggest inline code comments that link back to the doc for discoverability.
- Check if other existing docs reference the concept we just documented or updated — flag any that may also need refreshing.

## Rules
- One question at a time during discussion. Don't rush to writing.
- Target audience: experienced developers and AI agents. Skip basics. Explain enough that they can quickly orient, navigate to the right code, and maintain it confidently.
- Keep markdown docs lean. If you're writing implementation details, ask yourself: should this be a code comment instead?
- Be honest about limitations, tech debt, and rough edges.
- **DO NOT REFACTOR OR MODIFY APPLICATION CODE. We are documenting, not changing.** (Adding doc comments to source files is fine.)
- **Line budget**: Target 150–200 lines per doc. Going over usually means code examples belong in guidelines, zoom levels are mixed, or operational detail belongs in source comments.
- **L2 docs**: No code examples. Architecture describes structure. Exception: a compact struct/enum that IS the API surface (5–10 lines, genuinely architectural).
- **L3 docs**: Code appropriate for API surfaces and non-obvious constraints. If it's a pattern (how to use something), it belongs in a guidelines doc — link there instead.
- **Key Files tables**: File path and purpose only. No line numbers — they go stale immediately.

## Output

Write to: `docs/{concept-name}.md`

If the project has distinct subsystems, organize under subfolders:
```
docs/
  README.md              ← index and subsystem overview
  {concept}.md           ← top-level concepts
  {subsystem}/           ← subsystem folder when warranted
    {concept}.md
```

Use subfolders when it makes sense to partition — don't force it for a single doc.

### Template

The template has two variants depending on zoom level. Identify which applies before writing.

**L2 — System Map** (architecture overview, domain overview):

```
# {System/Domain Name}
*Last verified: {YYYY-MM-DD}*

## Overview
One paragraph: what it is, who uses it, external touchpoints.

## Container Map / Layer Diagram
Mermaid diagram showing containers/layers and relationships.

## Layers / Components
| Layer | Location | Role |
|-------|----------|------|

## Where to Put New Code
| Adding... | Goes in... | See... |
|-----------|-----------|--------|

## Key Architectural Decisions
WHY rationale for non-obvious choices. No code examples.

## Constraints
Hard rules that must never be violated.

## Current State Notes *(optional)*
Active schema version, active vs. legacy implementations, known migration debt.

## See Also
Links to L3 subsystem docs and guidelines.
```

**L3 — Subsystem** (tag system, navigation, data layer, etc.):

```
# {Subsystem Name}
*Last verified: {YYYY-MM-DD}*

## Overview
One paragraph: what problem, what solution, why this approach.

## Architecture
Mermaid diagram of internals. Component relationships.

## Design Decisions
WHY for each key choice. Code only for API surfaces and non-obvious constraints.

## Key Flows
The important behaviors, briefly. Mermaid sequence diagrams for complex interactions.

## Key Files
| File | Purpose |
|------|---------|
| `path/to/file` | Role — start here for details |

*(Path and purpose only. No line numbers.)*

## Gotchas
Non-obvious behaviors, sharp edges, common pitfalls that aren't in the code.

## Current Limitations
What's not supported. Rough edges. Things that should change.

## See Also
Links to related docs.
```

### docs/README.md Structure

```
# Project Documentation

## Overview
Brief description of the system and documentation structure.

## Subsystems
| Area | Description | Docs |
|------|-------------|------|
| {name} | What it covers | [Link](subsystem/concept.md) |

## Concepts
| Concept | Description | Last Verified |
|---------|-------------|---------------|
| [{name}]({name}.md) | One-line summary | {YYYY-MM-DD} |
```

After saving, provide:
- Summary of what was documented or updated
- List of changes made (for maintenance mode)
- Suggestions for related docs that might need updating
- Recommended inline code comments for discoverability

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
