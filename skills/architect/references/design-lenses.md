# Design Lenses

## Good design in BOB

Optimize for whole-system comprehensibility and conceptual integrity — not formal adherence to named principles.

Use SOLID, DRY, KISS, YAGNI, cohesion, coupling, information hiding, dependency direction, modularity, testability, DDD, and similar ideas as diagnostic lenses. Never treat them as independent objectives or scores.

Prefer software that is:

- predictable and unsurprising;
- navigable concept by concept;
- readable in a natural business-story order;
- explicit about domain meaning;
- cohesive without excessive fragmentation;
- separated so domain intent is not obscured by framework mechanics;
- simple across the whole system, not merely inside the changed feature.

Every design challenge should eventually answer:

- What concepts must a developer understand?
- Which concepts already exist?
- Did we add, remove, split, or merge a genuine concept?
- What complexity was removed?
- What complexity was introduced?
- What complexity was merely moved?
- Where will a developer start reading?
- What likely future change will stress the model?

## Generalization policy: semantic, not syntactic

Seek semantic generalization, not syntactic deduplication.

A proposed abstraction is **stronger** when:

- it represents something the domain or system genuinely has;
- its name improves the language used to explain the system;
- multiple callers vary along an intentional, understandable dimension;
- it reduces independent concepts or special-case workflows;
- future changes become easier to reason about.

**Challenge** abstraction when:

- similarity is only structural or syntactic;
- callers have different business meaning;
- the abstraction needs flags to preserve different semantics;
- extension points are speculative;
- navigation becomes harder;
- a generic name such as `shared`, `common`, `utils`, `manager`, or `factory` hides responsibility;
- duplication is better evidence-gathering than premature commitment.

Never use "DRY, always," "generic is always better," or "multiple cases prove a missing abstraction."
