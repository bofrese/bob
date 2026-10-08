# Review report template

File: `{story_path}sessions/{date}-review-{slug}.md`.

## Formatting

- Two halves: a decision-first top the reader can act on alone (TL;DR, What's good, Action items, Recommendation), then a `---` divider, then Details for reference.
- Collapse any section with nothing to report to a single `None` line. Do not pad.
- Severity icons are fixed: findings use 🔴 / 🟡 / 🟢; table status cells use ✅ / ⚠️ / ❌ (or `n/a`). Never bare ✓ or ⚠.
- Obsidian-safe cross-references: name a section in bold ("see **Details** below"), never a `[text](#anchor)` link. Never wrap a plain label in `[brackets]`; use icon + bold (`🔴 **Bug**`).
- A Mermaid diagram belongs inside a finding only when it shows a real mechanism or blast radius.

## Template

```markdown
# Review: {Feature/Change}
**Date:** {YYYY-MM-DD} | **Verdict:** ✅ Approve | ⚠️ Approve with concerns | ❌ Needs work | 🛑 Significant issues
**Scope:** {what reviewed} | **Plan:** {path or N/A} | **Design:** {path or N/A}

## TL;DR
{2-4 sentences: the overall judgement, then the count of 🔴 must-fix / 🟡 your-call / 🟢 optional items. Close with: "You should be able to decide from this section alone; Details below is reference only."}

## What's good
- {thing - brief, supports the verdict. "Nothing notable" is valid.}

## Action items
{Each item plain-English and self-contained, with a "see {section} below" pointer when a Details block expands it. "No action items" is valid.}

### 🔴 Must fix
1. {action}

### 🟡 Your call
2. {a judgement the developer owns, not a defect - state the options}

### 🟢 Optional
3. {action}

## Recommendation
{Next steps: `document` (Update) Yes/No, `handover` then `reflect` Yes/No, each with one line why. Name any other next phase.}

---

## Details
_Reference only. The sections above hold everything needed to decide what to do._

### Findings
{"No findings" is valid in any category. Do not manufacture issues to fill sections. A mermaid diagram belongs here only when it shows a real mechanism or blast radius.}

#### Bugs
🔴/🟡/🟢 **{Title}** · `{file}:{line}`
{Issue and why it matters.} **Fix:** {action}

#### Design-Conformance Failures
🔴/🟡/🟢 **{Title}** · `{file}:{line}`
{How this deviates from the Design Record / plan.} **Fix:** {action}

#### Design Concerns
**{Title}** · `{file}:{line}`
{Code is correct and matches the design, but the design itself looks wrong given the implementation.} **Route to:** `design` (revise Design Record) | `reflect` (surface for developer)

### Plan Alignment
{Omit if no plan.}
| Aspect | Planned | Implemented | Status |
|--------|---------|-------------|--------|
| {aspect} | {planned} | {implemented} | ✅ / ⚠️ / ❌ |

### System Health
| Dimension | Assessment |
|-----------|------------|
| Architecture | |
| Maintainability | |
| Consistency | |
| Technical Debt | |

### Guideline Compliance
| Guideline | Status | Notes |
|-----------|--------|-------|
| {guideline} | ✅ / ⚠️ / ❌ / n/a | {notes} |

### Done Criteria
- ✅ / ⚠️ / ❌ {item} - {evidence}

### What Was Done
**Approach:** {How implemented - patterns and key design decisions.}
**Key points:**
- `{file}:{lines}` - {what the core logic does}
- {Non-obvious behavior, dependencies, gotchas}
```
