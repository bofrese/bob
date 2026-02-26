---
name: domain-knowledge
description: "Captures project-specific domain knowledge. Invoke when the user corrects a misunderstanding, clarifies what a term means in this project's context, or explains nuances an informed developer wouldn't assume. Do NOT invoke for general language/framework patterns, architecture decisions, or tooling — those belong in guidelines/subsystems."
user-invokable: true
---

## Process

1. **Read index**: `docs/domain/README.md` — scan to check if concept is already documented
2. **If exists**: load that file, check whether the current session adds new nuance
3. **If new**: extract from recent conversation — what was clarified, corrected, or explained
4. **Draft nugget** using the format below
5. **Verify**: present draft to user — "I picked up on [concept]. Here's my understanding: [draft]. Correct? Should I save this?"
6. **Save**: update existing file or create `docs/domain/<slug>.md`, then update the index

## Nugget Format

Keep under 10 lines. Brevity is correctness here.

```markdown
## [Concept Name]
#[category] #[tag]

[What it means in this project — 1–3 sentences. Not general knowledge; project-specific interpretation.]

- **Key**: [non-obvious fact or distinction]
- **Not**: [common misconception to avoid]
```

## Index Format (`docs/domain/README.md`)

```markdown
# Domain Knowledge Index

| File | Concepts Covered |
|------|-----------------|
| orders.md | order lifecycle, fulfillment states, cancellation rules |
```

## Rules

- One concept per invocation — don't batch
- Always verify before saving — domain knowledge is opinionated, not factual
- Project-specific meaning only — skip what any informed developer would know
- If uncertain whether something belongs here, ask: "Would I need to re-explain this next session?"
- Create `docs/domain/` and `docs/domain/README.md` if they don't exist
