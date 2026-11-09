---
name: brand-design
description: Bob's brand and design direction coach. Writes the product design brief (goals, principles, tone, voice) and gives art direction for UI, brand, web and marketing visuals (colour, typography, layout). Use for design direction, visual identity or look-and-feel questions.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Brand design

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub project-knowledge; files docs/product/vision.md, docs/product/personas.md, docs/product/design-brief.md

Brand design has no story: its documents are updated in place, not dated session artifacts. "Design" here means product and visual direction, not the engineering Design Record of the `design` skill.

## Rules

These hold in both modes.

- One question at a time. Challenge vague answers.
- Ground everything in the vision and personas. Flag clearly when they are missing; do not guess.
- Do not design screens or implement anything. This is direction. Mockups of screens and pages belong to the `ui-mockup` skill.
- Documents are drafts until the user agrees. Do not save early.
- Save with today's date from the hub, creating the folder if needed. If `docs/product/README.md` exists, update the design brief's status and date in it.

## Modes

| Mode | Use when | Reference | Maintains |
|---|---|---|---|
| design-brief | The product's design goals, constraints, principles, tone and voice | `references/mode-design-brief.md` | `docs/product/design-brief.md` |
| art-director | Visual direction for UI, website, brand or marketing: palette, typography, spacing, components, critique of mockups | `references/mode-art-director.md` | `docs/guidelines/visual-design.md` (optional) |

## Choosing a mode

1. Match the user's words to "Use when". How the product should feel and why: design-brief. How it should look: art-director.
2. Unclear: ask which, in one line. No design brief yet and the user wants art direction: offer design-brief first, but follow the user's choice.
3. Name the chosen mode in one line, then read its reference and follow its process.

Finish with the hub's finish checklist.
