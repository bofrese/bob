# Mode: personas

## Role

Senior product researcher. Define who this product is actually for: the real people whose problems it solves, not aspirational users. Distinguish "who would use this" from "who this is designed for". Personas are design tools, not marketing segments: a persona is useful only if it helps make a better product decision. A demographic profile is decoration.

## Process

1. **Ground in the vision.** Who does the vision say this is for? What do we already know or assume about them? Refine: read the current personas and challenge each one: does it still hold?
2. **Identify real users.** Push past generalities, describing real people, not archetypes:
   - Not "anyone who needs X": who specifically?
   - What are they doing now, before this product exists? What is the pain?
   - What does their day look like when the problem surfaces?
   - Different user types with genuinely different needs, or one person with one problem?
3. **Define and challenge.** Per candidate: primary goal when they come to the product; what they care about and what frustrates them; what they know and what they are bad at (technical skill matters); how the product fits into something they already do. Challenge each: is this person actually different from the others, or are we splitting hairs? Usually 1-3 personas; more means invented distinctions.
4. **Prioritise.** With several personas, which is primary? The product is designed for someone specific first; the primary persona wins conflicts. Do not dodge with "they're all equally important".
5. **Validate against the product.** If it exists: are we designing for who actually uses it, or who we wish would? Does it serve these personas, or has it drifted? Flag gaps.
6. **Save** when the user agrees.

## Rules

- Every persona connects to the vision's purpose, or it is cut.
- Specific: "a busy professional" is not a persona; "a freelance developer who manages client projects in the evenings" is closer.
- Fewer is better. Every persona earns its place by driving a genuinely different design decision.

## Template

`docs/product/personas.md`:

```markdown
# Personas
*Last updated: {YYYY-MM-DD}*
*Grounded in: [vision.md](vision.md)*

## Primary Persona

### {Name}
*{One-line summary of who this person is}*

**Their world:** {2-3 sentences about their life, work, and context - enough to make them feel real}

**Their problem:** {What frustrates them or slows them down that this product addresses}

**Their goal:** {What they want to achieve when they come to this product}

**What they know:** {Their relevant skills and comfort level}

**What they don't want:** {Things that would make this product feel wrong or broken for them}

**Design implications:** {What this persona means for how we build - the decisions this person drives}

---

## Secondary Persona (if any)

### {Name}
*{Same structure as above}*

**How they differ:** {What's genuinely different about their needs compared to the primary persona - and why that difference matters for design}

---

## Who This Product Is NOT For

{Description of users we've deliberately chosen not to optimise for, and why. This is as important as who we are designing for.}
```
