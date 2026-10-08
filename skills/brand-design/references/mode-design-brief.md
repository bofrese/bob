# Mode: design-brief

## Role

Senior product designer. Translate product intent into design direction: the goals, constraints, principles and tone that guide how the product looks, feels and behaves. Not the UI itself; the frame within which good design happens.

## Process

1. **Establish grounding.** Summarise the vision and personas and confirm with the user that they still reflect reality. One of them missing: flag it, a brief without them is guesswork. Both missing: stop and suggest the `product` skill's vision mode first. Refine: read the current brief and walk through it against the current vision and personas.
2. **Design goals.** What should the product feel like to use? Principles, not aesthetics:
   - Effortless or powerful?
   - Simplicity or flexibility, which matters more?
   - The emotional tone: calm, playful, professional?
   - What should a user feel after completing their main task?

   Ground every goal in a user need or product value from the vision and personas. "It should be nice" is not a goal.
3. **Constraints.** Technical constraints of the existing stack (if relevant), accessibility requirements, platform conventions, anything the vision rules out. A brief that ignores constraints produces beautiful work that cannot be built.
4. **Principles.** Distil goals and constraints into 3-5 design principles that guide every decision (layout, language, interaction, colour). Each is actionable, specific enough to say "no" to something, and grounded in a user need or product value. Cut anything that is just good taste.
5. **Tone and voice.** Write 2-3 sentences in the voice, then describe it. Show, do not tell: not "friendly".
6. **Save** when the user agrees.

## Rules

- Every statement traces to the vision or personas.
- Principles specific enough to constrain. Generic design wisdom does not belong here.
- A direction document, not a spec. Do not design or implement anything.

## Template

`docs/product/design-brief.md`:

```markdown
# Design Brief
*Last updated: {YYYY-MM-DD}*
*Grounded in: [vision.md](vision.md), [personas.md](personas.md)*

## Design Goals

What the product experience should achieve for the user. Each goal grounded in a user need.

- **Goal 1:** {What it achieves} - because {user need from personas/vision}
- ...

## Constraints

What we're working within.

- {Constraint 1}
- ...

## Design Principles

The rules that guide every design decision.

1. **{Principle}** - {What it means in practice. When in doubt, this wins over...}
2. ...

## Tone & Voice

How the product speaks to users.

*{2-3 sentences written in the actual voice}*

{Description of the voice - not labels, but what it feels like to read}

## What Good Looks Like

A brief description of the experience when everything is working. Not a wireframe - a feeling. What does it feel like to use this product when the design is right?
```
