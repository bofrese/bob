---
name: Assumption Testing Principles
description: Invoke this skill when identifying, ranking, and testing assumptions before building. Used by bob:validation-plan and bob:product-coach commands for validation planning and MVP definition.
version: 1.0.0
---

# Assumption Testing Principles

Compact reference for identifying, ranking, and testing assumptions before building. Apply when working on validation planning, MVP definition, or early-stage product validation.

---

## Core Truth

**Every product idea is a stack of assumptions.** Most fail because a core assumption was wrong, not execution. Find riskiest assumptions and test them before writing code.

---

## Assumption Types

**Desirability:** Do customers want this? Will they pay? Is problem painful enough?

**Feasibility:** Can we build it? Scale it? Support it? Distribute it?

**Test desirability first.** No point building something feasible that no one wants.

---

## The Assumption Stack

Build explicit list: "Our product succeeds IF..."

```
├─ People have problem X (desirability)
├─ Current solutions fail to solve X (desirability)
├─ Our approach solves X better (desirability)
├─ People will pay $Y (desirability)
├─ We can build in Z months (feasibility)
├─ CAC < $W (feasibility)
└─ Can scale to N users (feasibility)
```

---

## Risk Ranking

**Impact × Uncertainty = Risk**

### Impact Scale
- **Critical:** Product fails completely if wrong
- **High:** Major pivot required
- **Medium:** Delays or scope reduction
- **Low:** Minor adjustment

### Uncertainty Scale
- **High:** Pure guess, no evidence
- **Medium:** Some signals, inconclusive
- **Low:** Strong evidence, confident

### Priority Matrix

| Uncertainty | Critical | High | Medium | Low |
|-------------|----------|------|--------|-----|
| **High** | **TEST FIRST** | Test early | Test when convenient | Assume |
| **Medium** | Test early | Test soon | Monitor | Assume |
| **Low** | Validate once | Monitor | Assume | Assume |

Focus: high uncertainty + high impact.

---

## Validation Experiments

Structure per assumption:
1. **Hypothesis:** "We believe [assumption]"
2. **Test:** "To verify, we will [experiment]"
3. **Success:** "We're right if [specific result]"
4. **Timeline:** "[X days/weeks]"

### Validation Hierarchy (Cheapest → Most Expensive)

| Method | Cost | Time | Validates |
|--------|------|------|-----------|
| Customer conversations | Free | 1-2wk | Problem severity, alternatives |
| Landing page test | $500-2k | 1-2wk | Value prop, demand |
| Prototype/mockup | 1-2wk design | 2-3wk | UX, features |
| Concierge MVP | High time, low dev | Ongoing | Willingness to pay, value |
| Wizard of Oz MVP | Mod dev + high time | 2-4wk + ongoing | Full experience, WTP |
| Working MVP | Highest | 4-12wk | Everything |

**Start at #1. Only move down when cheaper tests validate.**

---

## Build-Measure-Learn

**Build (Minimum):** Smallest thing to test the assumption.

**Measure (Specific):** Not "see if people like it." Instead: "20% trial → paid in 30d."

**Learn (Honest):**
- **Validated:** Evidence supports, proceed
- **Invalidated:** Evidence contradicts, pivot/kill
- **Inconclusive:** Need more data or different test

Weak signals ≠ validation. "They liked it" ≠ "they paid for it."

---

## MVP Scope Definition

MVP = Minimum to validate riskiest assumptions.

### The Formula
1. List all assumptions
2. Rank by risk (uncertainty × impact)
3. Identify top 3 riskiest
4. Define minimum product to test those 3
5. **That's your MVP**

### What to Cut

**Include:** Features to test core assumptions, minimum core value, enough quality for actual use

**Cut:** Features that don't test assumptions, nice-to-haves, optimizations, polish, scale beyond testing needs

**Test:** "If we remove this, can we still validate our riskiest assumption?"
- Yes → Cut it
- No → Keep it

---

## Success Criteria

Define "validated" BEFORE running experiment.

### Good Criteria

✅ Specific: "10 customers pre-pay for beta"
✅ Achievable: "5 trial signups in 2 weeks"
✅ Meaningful: "20% convert to paid" (revenue validates WTP)

❌ Vague: "People seem interested"
❌ Unrealistic: "1000 users in 2 weeks" (without distribution)
❌ Weak signal: "100 email signups" (low commitment)

### Commitment Ladder

1. Said they like it (weakest)
2. Gave email (low)
3. Signed up for trial (medium)
4. Used repeatedly (high)
5. Paid for it (strong)
6. Referred others (PMF signal)

Optimize for climbing ladder, not stopping at bottom.

---

## Red Flags

**"We'll figure it out as we build"** → No. Test assumptions before building.

**"If we build it, they will come"** → Distribution assumption = deadliest assumption.

**"Everyone loved the idea"** → Did they pay? If not, not validation.

**"We need to launch to really know"** → Launch = most expensive test. Run cheaper first.

**"MVP needs 50 features"** → Not MVP. Full product. Cut scope.

---

## Validation Checklist

- [ ] Listed all critical assumptions?
- [ ] Ranked by uncertainty × impact?
- [ ] Identified top 3 riskiest?
- [ ] Designed experiments to test them?
- [ ] Defined specific success criteria?
- [ ] Run cheapest tests first?
- [ ] Measuring commitment, not interest?

---

## Key Insight

**Goal isn't proving you're right. It's finding truth as cheaply as possible.**

Being wrong quickly > being wrong slowly. Test fast, kill bad ideas faster.
