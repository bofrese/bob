---
name: Prompt Engineering Principles
description: Invoke this skill when creating, reviewing, or improving bob commands. Provides principles for writing effective, token-efficient Claude commands.
version: 1.0.0
---

# Prompt Engineering Principles

Compact reference for writing effective Claude commands. Apply when creating or reviewing commands.

---

## Core Principles

**Be explicit** — "Write 5 bullets, each under 15 words" beats "be concise." Specify exact success criteria.

**Structure clearly** — Separate Context, Role, Process, Output. Don't mix in prose.

**Minimize tokens** — Every token costs money and latency. High-signal only. Cut filler, redundancy, verbose examples.

**Load just-in-time** — Don't dump context upfront. Load principles/guidelines when they apply.

**Allow uncertainty** — Give permission to say "I don't know" to reduce hallucinations.

**One question at a time** — Multi-part questions fragment attention.

**Perfect examples** — Claude 4.x pays close attention to details. Sloppy examples teach sloppy behavior.

**Standalone outputs** — Documents must be readable without conversation context. But standalone ≠ verbose. Include essentials only.

**Avoid over-constraining** — "You are a helpful architect" beats "You are a world-renowned expert who never makes mistakes."

**No aggressive language** — Claude 4.x is instruction-compliant. "CRITICAL: YOU MUST" causes over-triggering. Use normal language.

---

## Anti-Patterns

**Unstructured instructions** — Mixing context, constraints, and format in prose.

**Aggressive triggers** — "CRITICAL!" "MUST!" "NEVER!" cause over-triggering.

**Vague constraints** — "Be concise" vs "3-5 sentences, under 100 words."

**Poor examples** — Incomplete, inconsistent, or unrealistic.

**Context dumping** — Loading everything upfront instead of just-in-time.

**Multi-question barrages** — Asking 5 things at once instead of one at a time.

**Verbose outputs** — Generated files become future context. Keep them scannable and token-efficient.

---

## Command Structure Pattern

```markdown
## Context
{Date, project state, protocol loads}

## Role
{Who Claude is — architect, reviewer, coach}

## Process
{Step-by-step, numbered phases}

## Output
{Path, format, template}
```

---

## Output Template Philosophy

**Include:**
- Date and identifier
- Status/verdict
- Issues/decisions (bulleted, brief)
- Next actions (if applicable)

**Exclude:**
- Prose methodology explanations
- Percentage calculations
- Verbose rationales
- Repeated context
- Introductions/acknowledgments
