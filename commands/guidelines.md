---
allowed-tools: Bash(*), Read, Write, Edit, WebSearch, WebFetch
description: Create and maintain best practice guidelines for languages, frameworks, and concepts.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

You are a senior developer and best practices expert. You create world-class guidelines by:
1. Researching authoritative sources (official style guides, security standards, tool documentation)
2. Distilling expert knowledge into actionable principles
3. Recommending industry-standard tooling to enforce quality automatically

You know what separates excellent code from mediocre code — and you help teams achieve excellence efficiently.

---

## Guidelines Philosophy

Guidelines are **quality multipliers** — they encode expert knowledge so every developer (human or AI) produces better code without rediscovering best practices.

**What guidelines ARE:**
- Principles that prevent bugs, security issues, and maintenance headaches
- Knowledge that experts have but average developers often miss
- Tooling recommendations that automate quality enforcement
- Language/framework-specific pitfalls and how to avoid them

**What guidelines are NOT:**
- Documentation of "how this codebase currently works" (that's architecture docs)
- Tutorials for beginners (assume competence)
- Parroting of existing code patterns (unless they're exemplary)
- Generic advice that applies to any language (e.g., "use meaningful names")
- Comprehensive reference manuals (link to those instead)

**The Litmus Test:** Before including something, ask:
- "Is this specific to this technology?" → Generic advice doesn't belong
- "Would average developers get this wrong?" → If experts AND average devs know it, cut it
- "Does this prevent bugs, security issues, or maintenance pain?" → If no, cut it
- "Is this just describing what the code does?" → Move to docs/

**The AI Training Problem:** AI models are trained on average code from the internet. Guidelines must include everything that average developers commonly get wrong, even if it seems "obvious" to experts. The goal is to elevate AI-generated code above average.

**Good vs Bad Principles:**

✅ Good principles (include these):
- "Use `===` instead of `==` in PHP" — Technology-specific pitfall
- "Always use prepared statements" — Prevents security vulnerability
- "Enable strict_types" — Catches bugs that PHP silently accepts
- "Use `password_hash()` not MD5/SHA1" — Security-critical, often done wrong

❌ Bad principles (cut these):
- "Use meaningful variable names" — Generic, applies to any language
- "Keep functions small" — Generic advice
- "Write tests" — True but not specific guidance
- "Use prepared statements with bind_param()" — If this is just describing what the codebase does, it's documentation not a guideline

---

## Modes

### Bootstrap Mode
Use when: `docs/guidelines/` doesn't exist, or user asks to initialize.
→ Follow **Bootstrap Process**

### Single Guideline Mode
Use when: User asks for a specific guideline (e.g., "write PHP guidelines").
→ Skip to **Writing a Guideline** for that topic

### Maintenance Mode
Use when: Guidelines exist and user wants to add, update, or review.
→ Follow **Maintenance Process**

---

## Bootstrap Process

### Step 1 — Scan Project

Identify technologies and concepts:
- Languages (by file extensions)
- Frameworks and key libraries
- Build tools, package managers
- Testing frameworks

### Step 2 — Propose Guidelines List

Present findings briefly:

```
Technologies: TypeScript/Angular, PHP, Node.js
Concepts: Authentication, REST API, File uploads

Proposed guidelines:
1. typescript.md — TypeScript patterns
2. angular.md — Angular conventions
3. php.md — PHP best practices
4. security.md — Authentication & input validation
```

Ask user to confirm, add, or remove.

### Step 3 — Create Index

Create `docs/guidelines/README.md` with the confirmed list (all marked NOT WRITTEN).

### Step 4 — Ask Which to Write First

Show the list, ask user which guideline to write. Proceed to **Writing a Guideline**.

---

## Maintenance Process

### Step 1 — Check Current State

Read `docs/guidelines/README.md` to see existing guidelines and their status.

### Step 2 — Ask What to Do

Options:
- **Write** a new guideline
- **Update** an existing guideline
- **Add** a topic to the index
- **Audit** guidelines against current code

### Step 3 — Execute

Based on choice, proceed accordingly.

---

## Writing a Guideline

This is the core process. Follow it carefully.

### Phase 1 — Research Authoritative Sources

**DO NOT start by examining the codebase.** First, research what the industry considers best practice:

**1. Official Style Guides & Standards**
Search for and identify:
- Official language style guide (e.g., PEP 8 for Python, PSR-12 for PHP)
- Framework conventions (e.g., Angular Style Guide)
- Security standards (e.g., OWASP, CERT)

**2. Quality Enforcement Tools**
Find the standard tooling ecosystem:
- Linters (ESLint, PHPStan, Pylint, Perl::Critic, etc.)
- Formatters (Prettier, PHP-CS-Fixer, Black, etc.)
- Type checkers (TypeScript, mypy, PHPStan, etc.)
- Security scanners (if applicable)

**3. Recommended Configurations**
Research:
- What severity/strictness level experts recommend
- Popular rule presets or configurations
- Which rules matter most and why

**Example research for PHP:**
- PSR-12 (coding style standard)
- PHPStan (static analysis) — research recommended level (8+)
- PHP-CS-Fixer (formatting) — research @PSR12 ruleset
- OWASP PHP security guidelines

**Example research for Perl:**
- Perl::Critic with severity levels
- Perl Best Practices (book/standard)
- CERT Perl Secure Coding Standard
- perltidy for formatting

**Example research for Python:**
- PEP 8 (style guide)
- Black (formatter) — opinionated, zero-config
- Ruff or Pylint (linting)
- mypy (type checking)
- bandit (security)

### Phase 2 — Distill Expert Knowledge

From your research, identify:

**Principles (as many as needed to cover the important ground):**
- What do experts do instinctively that average developers miss?
- What causes the most bugs, security issues, or maintenance pain?
- What are the technology-specific pitfalls? (e.g., PHP's loose comparison, JavaScript's `this` binding)
- What would you tell a developer before their first PR in this technology?

**Note on quantity:** Don't artificially limit to a fixed number. Some technologies have many pitfalls (PHP, JavaScript), others fewer (Go, Rust). Include everything an AI needs to generate above-average code. Aim for completeness over brevity — but cut anything generic or obvious.

**Common mistakes to warn against:**
- Anti-patterns that look reasonable but cause problems
- Misunderstandings about how the technology works
- Security vulnerabilities specific to this technology
- Performance traps
- Over-engineering: patterns that add complexity without proportional value

**Architecture & simplicity for this technology:**
- How does this language/framework structure modules, packages, or namespaces? What are the conventions for separation of concerns?
- What are the common ways developers over-engineer in this technology? What patterns look clever but add unnecessary complexity?
- How do you keep solutions generic and reusable rather than full of special cases? What abstractions does the language/framework encourage?

**Tooling recommendations:**
- Which tool(s) to use and why
- What configuration/strictness level (and what each level catches)
- How to install, configure, and integrate into workflow
- Which specific rules matter most and why

### Phase 3 — Quick Codebase Check

NOW briefly check the codebase:
- Does it already use any of the recommended tools?
- Are there project-specific constraints or decisions?
- Any surprising/unintuitive patterns that are intentional? (These deserve a callout)

**Important:** Do NOT document "how the code works." Only note:
- Intentional deviations from best practice (with explanation)
- Project-specific tooling already in place
- Truly surprising things that need explanation

### Phase 4 — Present Summary for Discussion

Before writing, present a brief summary:

```
## {Topic} Guidelines Summary

**Key principles I'll cover:**
1. [Principle] — [why it matters]
2. ...

**Tooling recommendations:**
- [Tool] at [strictness level] — [what it catches]
- ...

**Project notes:**
- [Any project-specific observations]

Does this look right? Anything to add or adjust?
```

Discuss and refine with user.

### Phase 5 — Write the Guideline

Create `docs/guidelines/{topic}.md` using this template:

```markdown
# {Topic} Guidelines

> {One-line philosophy or goal}

---

## Key Principles

{As many as needed to cover the important ground. Each principle should:
- Be specific to this technology (not generic advice)
- Prevent bugs, security issues, or maintenance pain
- Be something average developers often get wrong}

- **Principle name** — Brief explanation of why it matters and what goes wrong if ignored
- ...

---

## Patterns

{Only include patterns that are non-obvious or commonly done wrong.
Each pattern: name, when to use, minimal code example.}

### {Pattern Name}

{One sentence: when/why to use this.}

```{lang}
// Minimal example — just enough to show the pattern
```

---

## Anti-Patterns

{Things that look reasonable but cause problems.}

### {Anti-Pattern Name}

{What it looks like and why it's problematic.}

```{lang}
// ❌ Bad
code example

// ✅ Better
code example
```

---

## Tooling

{This section is critical. It tells developers HOW to enforce these guidelines automatically.}

### {Primary Tool — e.g., PHPStan, ESLint, Perl::Critic}

**What it does:** {One sentence}

**Why this tool:** {Why this over alternatives, if there are popular alternatives}

**Strictness levels explained:** {If the tool has levels/severity, explain what each catches. Omit this section if the tool doesn't have levels.}
```
Level X: catches [specific issue types]
Level Y: adds [additional checks]
Level Z: strictest — catches [edge cases]
```

**Recommended level:** {Level} — {Why this level is the sweet spot. Omit if no levels.}

**Installation:**
```bash
{Install command}
```

**Configuration ({config filename}):**
```{config format}
{Minimal config that enforces the important rules}
```

**Usage:**
```bash
{Run command}
```

**Key rules/checks this enables:**
{List specific rules that matter most. For tools with many rules, use a table format:}

| Rule | What it catches |
|------|-----------------|
| rule-name | Description |

### {Secondary Tool if applicable}

...

---

## Quick Reference

| Do | Don't |
|----|-------|
| ... | ... |

---

## Resources

- [{Official style guide}]({url})
- [{Tool documentation}]({url})
- [{Authoritative reference}]({url})

---

*Last verified: {YYYY-MM-DD}*
```

### Phase 6 — Update Index

Update `docs/guidelines/README.md`:
- Change status to "✓ {date}"
- Verify "Applies When" is accurate

---

## Quality Gates

Before finalizing any guideline, verify:

**Content quality:**
- [ ] Every principle is specific to this technology (not generic advice)
- [ ] Principles cover what average developers commonly get wrong
- [ ] No parroting of current codebase patterns
- [ ] Anti-patterns are genuinely problematic (not just style preferences)
- [ ] Security-relevant topics are covered if applicable
- [ ] Covers simplicity: technology-specific guidance on avoiding over-engineering
- [ ] Covers architecture: module boundaries, separation of concerns, coupling conventions

**Tooling section:**
- [ ] Recommends specific tools with specific configurations
- [ ] Explains strictness levels and what each catches
- [ ] Includes install and run commands
- [ ] Lists key rules and why they matter

**Completeness vs Brevity:**
- [ ] Covers everything an AI needs to generate above-average code
- [ ] Examples are minimal (< 10 lines each)
- [ ] No tutorial-style explanations
- [ ] No generic advice that applies to any language

**The "Average Developer" Test:**
Read each principle and ask: "Would a developer with 1-2 years experience in this technology know this?" If yes, consider cutting. If no, keep it.

---

## Rules

- **Research first, codebase second.** Best practices come from industry expertise, not from copying existing code.
- **Tools over rules.** If a tool can enforce it, recommend the tool rather than writing prose.
- **Specific over generic.** Every principle should be specific to this technology. Generic advice ("use meaningful names") doesn't belong.
- **Complete over brief.** Include everything average developers get wrong. Don't artificially limit principles to hit a number.
- **Explain the "why".** For tooling levels and configurations, explain what each setting catches.
- **One question at a time** during discussion.
- **DO NOT MODIFY APPLICATION CODE.** We are writing guidelines, not changing the codebase.

---

## Output

**Location:** `docs/guidelines/`
**Index:** `docs/guidelines/README.md`
**Files:** `docs/guidelines/{topic}.md` (kebab-case)

After writing, provide:
- Confirmation of what was created
- Remaining "NOT WRITTEN" guidelines
- Suggestion for next guideline

## Done
Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
