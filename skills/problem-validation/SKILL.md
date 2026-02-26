---
name: Problem Validation Principles
description: Invoke this skill when validating problems before building solutions, working on problem discovery, or making early-stage product decisions. Used by bob:problem-space and bob:product-coach commands.
version: 1.0.0
---

# Problem Validation Principles

Compact reference for validating problems before building solutions. Apply when working on problem discovery, validation, or early-stage product decisions.

---

## Core Truth

**Problem-solution fit comes before product-market fit.** Most products fail because they solve the wrong problem or a problem that isn't painful enough — not because the solution is bad.

---

## The Framework

### 1. Problem Before Solution

**Separate problem space from solution space:**
- Problem space = the pain, cost, friction users experience
- Solution space = how you might fix it

Explore the problem thoroughly before proposing solutions. Resist the urge to solution-jump.

**Questions:**
- What is the user trying to accomplish?
- What's blocking them or slowing them down?
- What does it cost them (time, money, frustration)?
- What workarounds have they invented?

### 2. Jobs-to-be-Done (JTBD)

People "hire" products to do a job. Understand the job, not just the feature request.

**The job has three dimensions:**
- **Functional** — What task are they trying to complete?
- **Emotional** — How do they want to feel doing it?
- **Social** — How does this affect how others perceive them?

**Example:**
- Functional: "I need to track project tasks"
- Emotional: "I want to feel in control, not overwhelmed"
- Social: "I want to appear organized to my team"

### 3. Problem Severity

Not all problems are worth solving. Assess severity:

**Frequency × Intensity = Priority**
- **Frequency** — How often does this problem occur?
- **Intensity** — How painful is it when it happens?

**The threshold:**
- High frequency + high intensity = urgent problem (build for this)
- High frequency + low intensity = annoyance (maybe worth solving)
- Low frequency + high intensity = edge case (deprioritize)
- Low frequency + low intensity = not a real problem (ignore)

### 4. Current Alternatives

What are people doing TODAY?

**Three categories:**
1. **Existing solutions** — competitor products, tools
2. **Workarounds** — manual processes, spreadsheets, hacks
3. **Nothing** — they live with the pain

**Critical questions:**
- Why aren't existing solutions good enough?
- If they're using workarounds, why haven't they adopted a product?
- If they do nothing, is the problem real or hypothetical?

**Warning sign:** If people say "I wish something existed" but haven't tried alternatives, the problem may not be painful enough.

### 5. Validation Tests

How do you know the problem is real?

**Evidence hierarchy (strongest to weakest):**
1. **They're paying for an alternative** — problem is real, they value a solution
2. **They've built a workaround** — problem is real, existing solutions don't fit
3. **They complain about it unprompted** — problem is top-of-mind
4. **They agree it's a problem when asked** — problem exists, but maybe not urgent
5. **They say "that would be nice"** — problem is hypothetical

**Only 1-3 are strong signals.**

### 6. The Mom Test

Don't ask: "Would you use this?"
Ask: "Tell me about the last time you experienced [problem]."

**Good questions:**
- "Walk me through the last time you..."
- "What have you tried to solve this?"
- "What's the hardest part about..."
- "How much does this cost you (time/money)?"

**Bad questions:**
- "Would you use a product that..."
- "Do you think this is a good idea?"
- "How much would you pay for..."

### 7. When to Kill Ideas

Kill ideas fast when:
- **No one is paying for alternatives** — if the problem was real, someone would be monetizing it
- **Workarounds are "good enough"** — Excel works fine, your product won't displace it
- **Problem only exists in hypotheticals** — "People would want this" ≠ people actually want this
- **You can't find 10 people who've felt the pain in the last month** — problem isn't frequent or severe enough

**Better to kill a bad idea in a week than build it for six months.**

---

## Red Flags

**"Everyone needs this"** — If everyone is your customer, no one is.

**"There's no competition"** — Either the market doesn't exist or you haven't looked hard enough.

**"People will change their behavior"** — They won't. Design for existing behavior.

**"If we build it, they will come"** — No. Distribution is harder than product.

---

## Application Checklist

Before committing to build:

- [ ] Can you describe the problem without mentioning your solution?
- [ ] Have you talked to 10+ people who've experienced this problem in the last 30 days?
- [ ] Are people currently paying for an alternative or using a workaround?
- [ ] Can you articulate why existing solutions fail?
- [ ] Is the problem frequent AND intense (not just one or the other)?
- [ ] Would solving this problem measurably improve their life or work?

If you can't check all boxes, the problem needs more validation.

---

## Key Insight

**People don't buy products. They buy better versions of themselves.**

The product is just the mechanism. Understand what version of themselves they're trying to become, and you'll understand the real job to be done.
