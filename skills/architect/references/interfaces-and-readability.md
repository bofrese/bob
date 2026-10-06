# Interfaces and Readability

Use when shaping a new capability's interface, or judging how a new or significantly changed source file reads. Readability is a recommendation and a design concern, never an enforced rule.

## Deep modules

Start from "what is the ideal interface to this capability?", not "which classes do we create?". The interface is a user interface whose user is another developer.

A good interface:
- exposes what the caller needs and hides implementation complexity;
- has clear semantics and a small conceptual surface;
- makes misuse difficult;
- does not leak framework mechanics.

**Smell:** a shallow module, where the interface is almost as complex as the implementation (pass-through methods, configuration the caller must understand, many small classes each doing one step).

## Public surface first

Follow the idiom of the language for what "public" means (exports, `pub`, header file, public class members). Within that idiom, a source file reads in this order:

1. What the file or module provides.
2. How to use it: public types, functions, entry points, contracts.
3. Implementation details, visibly separated from the public part.

A developer who only needs to use the module can stop reading after the public part.

## Comments explain the abstraction

Comments at the public surface state intent, guarantees, assumptions, lifecycle, important edge cases and semantic constraints. They do not narrate syntax.

## Reading-order smells

- Public interface buried among helper functions.
- Private implementation mixed with exported behavior.
- File-local details before the main abstraction.
- No clear line between API and implementation.
- Order that follows accident (order of writing) instead of how a reader should read.

## Questions for a new module

- What should another developer see first?
- What is the public surface, and what sits below the abstraction boundary?
- Can someone use it without reading the internals?
- In which order should a reader open the new files?
