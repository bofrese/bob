---
allowed-tools: Bash(*), Read, Write, Edit, WebSearch, WebFetch
description: Create and maintain best practice guidelines for languages, frameworks, and concepts.
---

## Context
- Use the Skill tool to invoke the `bob:context-protocol` skill and follow the protocol.

## Role

Senior developer. Create guidelines by researching authoritative sources and distilling expert knowledge into principles that prevent bugs, security issues, and maintenance pain.

---

## What Guidelines Are

**These files are loaded as AI context tokens in every engineering session. Max 60 lines per file.**

Include: technology-specific pitfalls, security issues, non-obvious behaviors, tooling commands.
Exclude: generic advice ("use meaningful names"), tutorial content, code examples, resources lists.

**Litmus test per principle:**
- Specific to this technology? (not generic advice)
- Would a 1-2 year developer miss this? (not obvious)
- Prevents bugs, security issues, or maintenance pain?

**Good:** `"Use === not == in PHP"` — technology-specific pitfall.
**Bad:** `"Use meaningful variable names"` — generic, cut it.

---

## Modes

**Bootstrap** — `docs/guidelines/` doesn't exist → follow Bootstrap Process.
**Single** — User requests a specific guideline → skip to Writing a Guideline.
**Maintenance** — Guidelines exist → read README.md, ask what to do (write / update / add / audit).

---

## Bootstrap Process

1. Scan: identify languages (by extension), frameworks, key concepts.
2. Propose list with one-line descriptions. Confirm with user.
3. Create `docs/guidelines/README.md` with confirmed list (all marked NOT WRITTEN).
4. Ask which to write first.

---

## Writing a Guideline

### Phase 1 — Research (authoritative sources first, codebase second)

Research in order:
1. Official style guide / security standard (OWASP, PEP 8, PSR-12, Angular Style Guide, etc.)
2. Standard linter/formatter/type-checker (ESLint, PHPStan, Black, mypy, etc.)
3. Recommended strictness level and key rule configuration

Do not start with the codebase.

### Phase 2 — Distill

Identify:
- What do experts do instinctively that average developers miss?
- Technology-specific pitfalls (PHP loose comparison, JS `this` binding, etc.)
- Security vulnerabilities specific to this tech
- Over-engineering traps specific to this tech
- What makes AI-generated code mediocre in this technology?

### Phase 3 — Codebase check (brief)

- Tools already in use?
- Any intentional deviations from best practice worth noting?

### Phase 4 — Confirm before writing

Present: key principles + tooling recommendation. One question at a time. Wait for confirmation.

### Phase 5 — Write

**Target: 40-60 lines.** No code examples. No resources section.

```markdown
# {Topic} Guidelines

> {One-line goal}

## Principles

- **{Name}** — {why it matters; what breaks if ignored; technology-specific}
- ...

## Tooling

### {Tool name}

**Install:** `{install command}`
**Run:** `{run command}`
**Config ({filename}):**
```{format}
{minimal config — only settings that matter most}
```
**Key rules:** {2-4 most important rules and what they catch}

*Last verified: {YYYY-MM-DD}*
```

**If multiple tools:** add a `### {Tool}` subsection per tool.

### Phase 6 — Update index

Update `docs/guidelines/README.md`: status → `✓ {date}`. Verify "Applies When" trigger is precise and machine-matchable (e.g., `ext: .ts` or `cmd: plan, review-plan` or `path: docs/`).

---

## Tooling Behavior

When the guideline is later loaded during an engineering session:
- If a recommended tool is not installed, offer to install it before proceeding.
- Once installed, run it at relevant points (implement: after each step; review: as part of scope analysis).

---

## Rules

- Research first, codebase second.
- Tools over rules — if a tool enforces it, list the tool rather than writing a principle.
- Specific over generic — every principle must name the technology.
- **Max 60 lines** — these are AI context tokens, not developer tutorials.
- Do not modify application code.

---

## Output

`docs/guidelines/{topic}.md` (kebab-case) + updated `docs/guidelines/README.md`

After writing: confirm what was created, list remaining NOT WRITTEN guidelines, suggest next.

## Done — Non-Deferrable
**Invoke `bob:done-criteria` before responding to any new request.** If the user asks to move on or start another command, run done-criteria first, then proceed.

Use the Skill tool to invoke the `bob:done-criteria` skill and follow the protocol.
