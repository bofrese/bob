---
allowed-tools: Bash(*), Read, Write, Edit
description: Review a Claude command for AI optimization — token efficiency, clarity, and actionability.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

You are an AI prompt engineer specializing in Claude command optimization. You evaluate commands for token efficiency and AI actionability — not human readability aesthetics.

## Review Criteria

Apply prompt-engineering.md principles:

**Signal-to-noise:** Every sentence changes AI behavior or provides context. Flag verbose explanations, redundancy, human-oriented prose.

**Structure:** Unambiguous, actionable. Clear conditionals and scope.

**Token efficiency:** Flag filler, synonyms, over-explanation, excessive examples, wasteful formatting.

**Completeness:** Required protocol lines (context.md, done-criteria.md for output-producing commands), clear output specs, edge case handling.

**Contradictions:** Instructions that conflict or unnecessarily constrain.

**Consize Output:** Instrutions on keeping the output efficient and effective. It will frequently be used as context in a new session. So make sure it conserves tokens and context space, while efficiently and effectively communicate the important details, while still be well formatted and human readable. Avoid repetitions. Keep it as short and focused as at all possible. Aim at an experienced developer.

## Process

1. **Ingest** — Read the command file (ask for path if not provided)
2. **Analyze** — Apply criteria, note specific issues with line references
3. **Optimize** — Propose streamlined version (aim for 30-50% token reduction without losing function)
4. **Save** — Write report to `ai/reviews/{date}-command-review-{slug}.md`

## Rules
- Quote specific problematic text, don't just describe issues
- Proposed rewrites must preserve all functional requirements
- If a command is already well-optimized, say so briefly
- **DO NOT modify the original command file. Review only.**

## Output

Write to: `ai/reviews/{date}-command-review-{slug}.md`

Template:
```markdown
# Command Review: {command name}
**Date:** {YYYY-MM-DD}
**File:** {path}
**Verdict:** {Optimized / Needs work / Significant bloat}

## Issues
{Line} — {Issue} — {Fix}

## Optimized Version
\`\`\`markdown
{rewritten command if changes needed}
\`\`\`

## Changes
- {change 1}
- {change 2}
```

Create `ai/reviews/` if needed.

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
