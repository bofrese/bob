# Placement - Domain Language and Where Code Belongs

Use when decomposing a problem, naming things, or deciding where code belongs. DDD is a lens here, not a mandate for tactical patterns.

## Let the domain drive the design

The structure of the code mirrors the structure of the problem, not the structure of the database or the UI.

## Bounded contexts

A bounded context is a part of the system where one model applies and terms have precise, agreed meanings. Outside it, the same word can mean something else.

- Identify the boundaries before you name things.
- Within a boundary: one model, one vocabulary, one source of truth.
- Across boundaries: translate explicitly. Do not let one context's internals leak into another.

## Ubiquitous language

Within a bounded context, developers, product people and the code use the same words for the same things.

- Name code the way the domain names the concept, not the way the database column is named.
- If a concept has no domain name, find one before you code it.

## Model reflects the domain, not the database

- The domain model is the source of truth. The database is a persistence detail.
- A model class that looks like a table schema (flat rows, foreign key fields) models storage, not the domain.
- Ask: does this structure make sense to someone who understands the problem but not the tech?

## The golden check

Does the code read like a conversation about the problem? If someone unfamiliar with the internals can follow the domain logic from the names alone, the design works.

## Pre-abstraction checklist

Before recommending a new entity, value object, service, aggregate, bounded context or other abstraction, answer all five:

1. Which domain distinction does it represent?
2. What repository or requirement evidence supports it?
3. Which concept or special case does it remove?
4. What does it cost in navigation and reading path?
5. Why can existing concepts not express the capability?

Allow duplication while the shared concept is not understood yet. Reject an abstraction that rests only on similar code shape (see `design-lenses.md`, semantic generalization).
