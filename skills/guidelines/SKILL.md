---
name: guidelines
description: Bob's guideline writer. Creates and maintains short best-practice guidelines in docs/guidelines/ for the project's languages, frameworks and concepts, researched from authoritative sources. Use when the user wants coding guidelines, technology pitfalls or linter setup written down.
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit, WebSearch, WebFetch
---

# Guidelines

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: files docs/guidelines/README.md

## Rules

- Guidelines are loaded as AI context in every engineering session: at most 60 lines per file.
- Research first, codebase second.
- Tools over rules: if a tool enforces it, list the tool instead of writing a principle.
- Specific over generic: every principle names the technology.
- Do not modify application code.

## Role

Senior developer. Research authoritative sources and distil expert knowledge into principles that prevent bugs, security issues and maintenance pain.

## What a guideline holds

Include technology-specific pitfalls, security issues, non-obvious behaviour, tooling commands. Exclude generic advice ("use meaningful names"), tutorial content, code examples, resource lists. Project patterns (how this codebase solves a recurring problem) go to `docs/architecture/patterns/` through the `document` skill.

Litmus test per principle: specific to this technology? Would a developer with 1-2 years of experience miss it? Does it prevent bugs, security issues or maintenance pain? Good: "Use === not == in PHP". Bad: "Use meaningful variable names".

## Modes

- **Bootstrap**, `docs/guidelines/` missing: scan for languages (by extension), frameworks and key concepts. Propose a list with one-line descriptions and confirm it. Create `docs/guidelines/README.md` with the confirmed list, all marked NOT WRITTEN. Ask which to write first.
- **Single**, the user names a guideline: go to Writing a guideline.
- **Maintenance**, guidelines exist: read the README and ask what to do (write, update, add, audit).

## Writing a guideline

1. **Research**, authoritative sources first, not the codebase: the official style guide or security standard (OWASP, PEP 8, PSR-12, Angular Style Guide), the standard linter, formatter or type checker (ESLint, PHPStan, Black, mypy), the recommended strictness level and key rule configuration.
2. **Distil**: what experts do instinctively that average developers miss; technology-specific pitfalls (PHP loose comparison, JS `this` binding); security vulnerabilities specific to this technology; over-engineering traps; what makes AI-generated code mediocre in it.
3. **Codebase check**, brief: tools already in use, intentional deviations worth noting.
4. **Confirm before writing**: present the key principles and the tooling recommendation, one question at a time. Wait for confirmation.
5. **Write** per `references/guideline-template.md` (relative to this skill's folder).
6. **Update the index**: in `docs/guidelines/README.md` set the status to `✓ {date}`. Make the "Applies When" trigger precise and machine-matchable (`ext: .ts`, `cmd: plan, review-plan`, `path: docs/`).

## When a guideline is used

A later session that loads a guideline offers to install a recommended tool that is missing, then runs it at the relevant points (implement: after each step; review: during scope analysis).

## Output

`docs/guidelines/{topic}.md` and the updated `docs/guidelines/README.md`. Then confirm what was created, list the guidelines still NOT WRITTEN, and suggest the next one.

Finish with the hub's finish checklist.
