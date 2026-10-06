# Concepts - Identification, Atomic Notes, Design Smells

Use when mapping what a system does, deciding what deserves an architecture note, or looking for design problems.

## Look for concepts, not structure

Classes, modules, packages, services and framework constructs are implementation structure. A concept is something the system does or enforces that an experienced developer would name when explaining the system to a peer.

Typical kinds: business concept, business rule, workflow, state transition, authorization or security boundary, validation, logging, persistence boundary, external integration, retry policy, event handling, configuration, scheduling, caching, cross-cutting policy.

**Test:** could this concept have a behavioral requirement that says how it is supposed to work? If yes, it is a concept. Sometimes that behavior can even be an executable requirement. If it only answers "which framework class is this", it is structure.

## Concept first, framework second

Explain a concept in its own terms first ("the authorization policy for these actions"). Point to the implementation (middleware, annotations) after that, for readers who need to go deeper.

## Navigation questions

The goal is orientation for humans and AI, not documentation for its own sake. For each meaningful concept, the architecture knowledge answers only the applicable questions:

- What is it, and why does it exist?
- What behavior does it provide?
- Where is it implemented?
- What does it depend on, and what depends on it?
- Where should I look if I need to change it?
- Which patterns does it take part in?
- Which tests or executable requirements verify it?

## Atomic note test

One note per concept. A note is atomic when:
- one noun phrase can link to it;
- every heading is about that concept;
- it answers only the applicable navigation questions above.

Knowledge local to one function, class or file stays in the code (a good name, a doc comment). Do not move local knowledge into notes.

## Design smells (signals, not bugs)

Raise a design question when a concept is:

- implemented in several unrelated places, or duplicated;
- represented inconsistently, or implemented differently in different areas without a clear reason;
- hard to name or hard to locate;
- poorly encapsulated, or spread across many files with no obvious boundary;
- mixed heavily with framework or infrastructure details;
- hidden behind incidental structure instead of an intentional abstraction.

Name the possible reading: architectural smell, refactoring candidate, missing abstraction, competing pattern, accidental complexity, design inconsistency. Never fix it silently. The human decides whether the situation is acceptable.
