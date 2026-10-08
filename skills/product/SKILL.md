---
name: product
description: Bob's product coach. Guides product discovery and keeps docs/product/ current - vision, personas, problem space, validation plan, business model, pricing, positioning and go-to-market. Use for product or business strategy work, or to find gaps in the product docs.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Product

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub project-knowledge; files docs/product/README.md, docs/product/vision.md. Then the product docs the chosen mode reads (Modes table), by the same `files` rule.

Product work has no story: its documents live in `docs/product/` and are updated in place, not dated session artifacts.

## Rules

These hold in every mode.

- One question at a time. Challenge assumptions and vague answers; ask for evidence, not opinions.
- Be direct. Marketing language is useless here. Clarity matters more than comfort: say so when an idea should be killed or a statement is weak.
- Do not implement, design or propose solutions. These are product documents.
- Never invent facts or numbers. Unknowns (market size, CAC) are assumptions to validate.
- Ground every mode in the product docs that exist. Vision missing: flag it, since the other documents are guesswork without it, and suggest vision mode first.
- Load a `principles-*.md` reference when its step starts, never all upfront.
- Documents are drafts until the user agrees. Do not save early.
- Adapt depth to the project type: a personal tool needs less than a business.
- Create and Refine: the document is missing, build it from scratch; it exists, read it first and walk through it section by section: what still holds, what shifted, what is missing.
- Save to the mode's document, creating `docs/product/` if needed, with today's date from the hub. If `docs/product/README.md` exists, update that document's status and date in it (format: `references/mode-coach.md`).

## Modes

| Mode | Use when | Reference | Maintains (`docs/product/`) | Also reads |
|---|---|---|---|---|
| coach (default) | Discovery from the start, "what am I missing", reviewing or maintaining the product docs, or no other mode fits | `references/mode-coach.md` | `README.md`, plus any document below | all existing product docs |
| vision | What the product is, who it is for, why it matters | `references/mode-vision.md` | `vision.md` | |
| personas | Who the users are, target users, user types | `references/mode-personas.md` | `personas.md` | `problem-space.md` |
| problem-space | Is the problem real and painful enough, jobs-to-be-done, kill or proceed | `references/mode-problem-space.md` | `problem-space.md` | |
| validation | Assumptions, risks, experiments, MVP scope | `references/mode-validation.md` | `validation-plan.md` | `problem-space.md`, `business-plan.md`, `positioning.md` |
| business-plan | Business model, monetisation, revenue model, pricing, unit economics | `references/mode-business-plan.md` | `business-plan.md` | `positioning.md`, `personas.md` |
| positioning | Market position, competitors, differentiation, messaging, go-to-market channels | `references/mode-positioning.md` | `positioning.md` | `problem-space.md`, `business-plan.md`, `personas.md` |

## Choosing a mode

1. Match the user's words to "Use when". Pricing and revenue go to business-plan. Go-to-market goes to positioning, or to business-plan when the question is how the business model acquires customers.
2. Design direction, look and feel, visual identity: the `brand-design` skill. LinkedIn: the `linkedin` skill.
3. Anything else, several areas, or unclear: coach. Coach may move into a mode during the session; then read that mode's reference and follow it.
4. Name the chosen mode in one line, then read its reference and follow its process.

## Principles

| Reference | Used by |
|---|---|
| `references/principles-problem-validation.md` | problem-space, vision (framing), coach |
| `references/principles-assumption-testing.md` | validation |
| `references/principles-business-model.md` | business-plan |
| `references/principles-go-to-market.md` | business-plan, positioning |
| `references/principles-positioning-strategy.md` | positioning |

Finish with the hub's finish checklist.
