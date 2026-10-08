# Domain capture

Capture project-specific meaning when the user corrects a misunderstanding, clarifies what a term means here, or explains a nuance an informed developer would not assume. Test: would I need this explained again next session?

Not here: general language or framework knowledge, architecture decisions (`design` or `reflect`), tooling and technology pitfalls (`guidelines`).

## Steps

One concept at a time.
1. Read `docs/domain/README.md`. If the concept has a file, load it and check what is new.
2. Classify:
   - Project fact ("this field means X here"): draft a nugget.
   - Claim about how or why the system is structured: route to `design` or `reflect` instead.
   - Uncertain inference: draft it as a candidate and say so.
3. Ask: "I picked up on {concept}. My understanding: {draft}. Correct? Should I save it?"
4. On yes: update the file or create `docs/domain/{slug}.md`, then update the index. Create `docs/domain/` and its README if missing.

## Nugget (under 10 lines)

```markdown
## {Concept}
#{category} #{tag}

{What it means in this project, 1-3 sentences.}

- **Key**: {non-obvious fact or distinction}
- **Not**: {common misconception}
- Source: {story or session, if known}
```

## Index (`docs/domain/README.md`)

```markdown
# Domain Knowledge Index

| File | Concepts Covered |
|------|-----------------|
| orders.md | order lifecycle, fulfillment states, cancellation rules |
```
