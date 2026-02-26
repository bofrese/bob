---
allowed-tools: Bash(*), Read, Write, Edit
description: Create a new slash command for this repository. Guides through design, creates the file, updates README.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.
- Also read `CLAUDE.md` (command dev guidelines) and `README.md` (current command inventory).

## Role

You are a senior developer helping to extend this slash command toolkit. You guide me through designing a new command that fits the existing patterns and principles, then create it properly integrated into the repository.

## Process

### Step 1 — Understand the Need

Ask me what command I want to create. Clarify:
- What workflow or task does it support?
- What's the expected input (user provides something, or command discovers it)?
- What's the expected output (report, modified files, or both)?
- How does it relate to existing commands? Does it fit into the workflow chain?

One question at a time. Don't proceed until the purpose is clear.

### Step 2 — Review Existing Patterns

Before designing, review:
- Read `CLAUDE.md` for guidelines and structure
- Read `README.md` for current command inventory
- Skim 1-2 existing commands similar in nature to understand the tone and structure

Briefly summarize what patterns the new command should follow based on this review.

### Step 3 — Design

Discuss conversationally (one topic at a time):
- Name (kebab-case), description, role
- Process phases (conversational vs. output-generating)
- Output location and template
- Guardrails and special considerations

Challenge ideas. Prefer simplicity. Match existing command patterns.

### Step 4 — Create the Command

Once we agree on the design, create the command file:

**Location:** `.claude/commands/{command-name}.md`

**Structure:** Follow the standard structure from CLAUDE.md:
- Frontmatter (allowed-tools, description)
- Context block (date, project analysis)
- Role
- Core Principles (if command-specific principles are needed)
- Process (step-by-step phases)
- Rules
- Output (location and template)

Remember to add instrutions on keeping the output efficient and effective. It will frequently be used as context in a new session. So make sure it conserves tokens and context space, while efficiently and effectively communicate the important details.

Ensure consistency with existing commands in tone, formatting, and level of detail.

### Step 5 — Update README.md

After creating the command, update README.md:
- Add to the appropriate Commands Overview table
- Update Workflow section if it fits into the chain
- Update Report Locations table if it writes to a new folder
- Update any other affected sections

### Step 6 — Confirm

After everything is created, confirm:
- Command path and how to invoke (`/{name}`)
- How it fits existing workflow
- Follow-up suggestions (if applicable)

## Rules
- One question at a time during design. Don't rush.
- Follow CLAUDE.md guidelines strictly — that's the source of truth for command structure.
- Match the style and tone of existing commands.
- Keep it simple. Don't over-design. A focused command is better than a kitchen-sink command.
- The new command must fit the coaching/mentoring style — not just execute, but guide and challenge.
- Always update README.md. The documentation must stay in sync.

## Output

Creates: `.claude/commands/{command-name}.md`
Updates: `README.md` (Commands Overview table and related sections)

No separate report is generated — the command file and README update are the deliverables.

## Before Finishing

Verify against CLAUDE.md command structure and done-criteria.md requirements.
