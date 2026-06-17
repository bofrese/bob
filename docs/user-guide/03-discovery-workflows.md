# Discovery Workflows
*Last updated: 2026-06-16*

Optional but powerful: figure out what to build and why before you build it. You can use Discovery standalone (pure product strategy), or alongside Engineering (grounded in a real vision).

## When to Use Discovery

**Use Discovery if:**
- You're building a new product from scratch
- The market or customers are changing and your strategy needs revisiting
- You're unsure whether a problem is worth solving
- You want to validate business assumptions before committing resources to development
- You want to understand personas deeply before designing

**Skip Discovery if:**
- You already have a clear vision and know what to build
- You're just fixing bugs or building one-off features
- Discovery was done already and nothing has changed

## The Discovery Pipeline

```
Product Vision → Personas → Design Brief
     ↓
Problem Space → Business Model → Positioning → Validation Plan
```

Not strictly linear—you can loop back. And not all necessary—pick what matters.

**Quick path (most projects):** Vision → Personas → Business Model

**Deep path (new product launch):** Vision → Personas → Design Brief → Problem Space → Business Model → Positioning → Validation Plan

---

## Phase 1: Product Vision

**What:** Establish what you're building, who it's for, why it matters.

**When:** At the start of a new project, or when direction needs revisiting.

**Run:** `/bob:product-vision`

The AI asks:
- What problem are you solving?
- Who has this problem?
- What does success look like?
- Why now? Why you?

**Output:** `docs/product/vision.md`

This is the single source of truth. Everything downstream (personas, plans, brainstorms) references this.

**Output structure:**
- Problem statement
- Market opportunity
- Target persona (rough)
- Solution approach (high level)
- Success metrics
- Why now, why you

**Time:** 45 minutes to 2 hours.

---

## Phase 2: Personas

**What:** Detailed characters representing your users. Not demographics on a slide—real people with goals, behaviors, frustrations.

**When:** After vision is clear. Before design or detailed planning.

**Run:** `/bob:personas`

The AI grounded in your vision, creates 2-4 detailed personas. Each includes:
- Name, role, context
- Goals (what are they trying to accomplish?)
- Behaviors (how do they currently solve this?)
- Frustrations (what's broken about current solutions?)
- How your product helps

**Output:** `docs/product/personas.md`

**Why this matters:** Personas are a shared language. Instead of "users want X", you say "Maya, our busy PM, needs X because she has to juggle 5 projects." This specificity prevents feature bloat and keeps design decisions grounded.

**Time:** 30-60 minutes.

---

## Phase 3: Design Brief

**What:** The visual and interactive direction. How should this product feel and look?

**When:** After vision and personas. Before UI design or high-fidelity mockups.

**Run:** `/bob:design-brief`

The AI creates a design brief grounded in who your personas are and what they need:
- Visual style (modern, minimal, playful, etc.)
- Interaction patterns (wizard vs freeform, modal vs in-place editing, etc.)
- Brand tone (voice, personality)
- Key UI principles

**Output:** `docs/product/design-brief.md`

**Why this matters:** A design brief prevents "let me just decide as I go." It's a north star for UI decisions, keeping visual coherence across the product.

**Time:** 20-45 minutes.

---

## Phase 4: Problem Space

**What:** Validate that the problem is real and worth solving before you invest in solutions.

**When:** After vision. Before major development commitment.

**Run:** `/bob:problem-space`

The AI challenges your assumptions:
- Is this actually a problem people face?
- How painful is it? Painful enough to pay for a solution?
- Why hasn't it been solved already?
- Are you solving for real users or imagined ones?

You explore evidence (user research, competitor analysis, market signals).

**Output:** `docs/product/problem-space.md`

**Why this matters:** It's easy to build solutions looking for problems. This phase forces you to validate the assumption before sink-costs drive you forward.

**Time:** 30-60 minutes depending on research depth.

---

## Phase 5: Business Model

**What:** How do you create and capture value? Pricing, revenue model, unit economics.

**When:** After vision and personas. When strategy is solidifying.

**Run:** `/bob:business-plan`

The AI explores:
- How does the customer get value from this?
- How do you capture value (subscription, one-time, freemium, etc.)?
- What are unit economics? How much does it cost to serve one customer?
- What's your pricing strategy?

**Output:** `docs/product/business-plan.md`

**Why this matters:** You can build the perfect product and still fail if the business model doesn't work. Thinking this through early prevents surprises.

**Time:** 45 minutes to 1.5 hours.

---

## Phase 6: Positioning

**What:** How you win in the market. Competitive strategy, differentiation, go-to-market.

**When:** After business model. When you're ready to think about launch or market fit.

**Run:** `/bob:positioning`

The AI explores:
- Who are your competitors?
- How are you different?
- Who do you win against?
- How do you reach customers?
- What's your launch strategy?

**Output:** `docs/product/positioning.md`

**Why this matters:** The best product doesn't win if no one knows about it or understands why it's better. Positioning forces clarity on this.

**Time:** 1-2 hours.

---

## Phase 7: Validation Plan

**What:** A test plan for your biggest assumptions. What are you betting on? How will you test those bets?

**When:** After strategy is defined. Before development or major resource commitment.

**Run:** `/bob:validation-plan`

The AI identifies your riskiest assumptions (market size, customer willingness to pay, technical feasibility, etc.) and designs small experiments to test them:
- Fake landing page signup to validate demand
- Concierge MVP to validate workflow
- Price sensitivity interviews
- Competitive testing

**Output:** `docs/product/validation-plan.md`

**Why this matters:** You can't eliminate risk, but you can reduce it by testing assumptions cheaply before development. This prevents building features no one wants.

**Time:** 30-75 minutes depending on complexity.

---

## Discovery Feeding Engineering

Once Discovery is done, it feeds into Engineering automatically:

- `/bob:brainstorm` reads your vision to ground the conversation
- `/bob:plan` checks against personas and design principles
- `/bob:review` verifies UI changes fit the design brief
- Everything is grounded in validated business assumptions

You don't have to re-introduce your strategy every session. It's in the files. Commands read it automatically.

---

## Product Coach: The Shortcut

If you don't know which commands to run or want guidance through the whole discovery process, start with:

```
/bob:product-coach
```

It's a conversational guide that helps you figure out what you need, guides you through each phase, and maintains the navigation file (`docs/product/README.md`) so you always know what exists and what's missing.

---

## Solo Discovery or Paired with Engineering?

**Solo discovery:** You're validating an idea before building. Run discovery, document findings, iterate on strategy. Great for founders, product managers, anyone thinking through strategy.

**Paired with engineering:** You have a vision and are building features. Start with discovery to establish the foundation (vision, personas, business model). Then switch to engineering commands for brainstorm → plan → implement cycles. Each feature is grounded in the strategy. Strategy can be revisited if market changes.

---

## What If You Change Your Mind?

Revise the artifacts. Run `/bob:product-vision` to update vision. Run `/bob:personas` to refine personas. Engineering commands pick up the changes automatically.

The "change your mind" part is the point: these are working documents, not holy scripture. They're statements of what you believe today. When you learn something new, update them and keep moving.

---

## Next Steps

- If you have a vision already, read [Engineering Workflows](02-engineering-workflows.md) to move to building.
- If you need product strategy guidance, run `/bob:product-coach`.
- If you're solo on discovery without engineering yet, that's fine—discovery stands alone.
