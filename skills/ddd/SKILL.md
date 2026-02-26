---
name: DDD — Domain-Driven Design
description: Invoke this skill when decomposing a problem, naming things, or deciding where code belongs. Used by bob commands during feature ideation and architectural planning.
version: 1.0.0
---

# DDD — Domain-Driven Design

A thinking framework. Apply when decomposing a problem, naming things, or deciding where code belongs.

---

## The core discipline

**Let the domain drive the design.** The structure of the code should mirror the structure of the problem, not the structure of the database or the UI.

## Bounded contexts

A bounded context is a part of the system where a specific model applies — and where terms have precise, agreed meanings. Outside that context, the same word might mean something different.

- Identify the boundaries before you name things.
- Within a boundary: one model, one vocabulary, one source of truth.
- Across boundaries: translate explicitly. Don't let one context's internals leak into another.

## Ubiquitous language

Within a bounded context, everyone — developers, product people, the code — uses the **same words** for the same things.

- Name your code the way the domain names the concept. Not the way the database column is named.
- If a concept doesn't have a domain name, find one before you code it. Forcing domain language on the code is one of the highest-value acts in a codebase.

## Model reflects the domain, not the database

- The domain model is the source of truth. The database is a persistence detail.
- If your model class looks like a table schema — flat rows with foreign key fields — you haven't modelled the domain. You've modelled the storage.
- Ask: "Does this structure make sense if I explain it to someone who understands the problem but not the tech?"

## The golden check

Before committing: does the code read like a conversation about the problem? If someone unfamiliar with the internals can follow the domain logic by reading the names alone, the design is working.
