---
name: UI Design Principles
description: Invoke this skill when designing, reviewing, or critiquing any user interface. Used by bob:ui-review, bob:art-director, and bob:design-brief commands.
version: 1.0.0
---

# UI Design Principles

A thinking framework for expert UI/UX evaluation. Apply when designing, reviewing, or critiquing any user interface — across platforms, at any stage from concept to code.

---

## The fundamental question

**Does this interface reduce friction between a user and their goal?** Every principle below serves this question. When in doubt, return to it.

---

## 1. Visual Hierarchy is Not About Size

Users don't read — they scan. The eye follows contrast, weight, spacing, and position in a predictable sequence. Good hierarchy creates a reading order that matches the user's priority sequence.

**What separates expert from average:**
- Think in *contrast ratios between elements*, not just individual element size
- Negative space is an active design element — it directs attention as powerfully as content
- Color, weight, and position are hierarchy signals; decorative icons and labels often aren't
- The reading order should be *designed*, not accidental

**Red flag:** Important actions buried in visual noise. Secondary content competing with primary content. Everything the same weight.

---

## 2. Cognitive Load is the Real Enemy

Every decision point, every unfamiliar pattern, every ambiguous label adds cognitive load. Users have a budget. Exceed it and they abandon, make errors, or distrust the interface.

**Hick's Law:** More choices = longer decision time. Reduce options at each decision step.
**Miller's Law:** Working memory holds ~7 items. Don't exceed it in a single view.
**Progressive disclosure:** Reveal complexity at the pace of user commitment — don't front-load.

**The expert's move:** Distinguish between *complexity* (inherent to the domain) and *complication* (your fault). Ruthlessly eliminate complication.

**Red flag:** More than 5–7 interactive elements competing for attention. Options without clear hierarchy. Labels that require interpretation.

---

## 3. States Are the Real Design

The happy path is easy. The quality of an interface is revealed in its edges: empty states, error states, loading states, partial data, offline, disabled.

**What experts obsess over:**
- Empty states are onboarding opportunities, not blank screens
- Error messages in user language, not system language
- Loading states as moments to build trust, not just wait
- Every interactive element has visible: default, hover/focus, active, disabled states

**Red flag:** Screens that only work with ideal data. Errors that say "Something went wrong." No indication of loading progress or duration.

---

## 4. Typography as Functional Architecture

Typography isn't style — it's structure. It establishes hierarchy, sets reading rhythm, and communicates tone without words.

**The fundamentals experts apply:**
- **Line length:** 45–75 characters for body text. Shorter = choppy. Longer = eye-tracking fatigue.
- **Leading (line-height):** Tight = tension, urgency. Loose = calm, spacious. Match to content mood.
- **Weight over size:** Changing weight communicates importance with less visual disruption than changing size.
- **Scale is a contract:** A type scale creates hierarchy expectations. Break it intentionally, never accidentally.

**Red flag:** Uniform weight throughout. Body text wider than 75 chars. Line-height below 1.4. Headings and body text indistinguishable at a glance.

---

## 5. Gestalt: Design with Perception, Not Against It

The brain organizes visual input into patterns automatically. Experts exploit this. Average designers fight it.

**The principles that matter in practice:**
- **Proximity:** Elements close together are perceived as related. Don't break this accidentally.
- **Similarity:** Visual consistency signals semantic consistency — same treatment = same behavior.
- **Common region:** A container (card, background fill) groups elements more powerfully than proximity alone.
- **Figure/ground:** Background activity competes with foreground tasks. Suppress it.
- **Closure:** Users complete incomplete shapes. You don't need to box everything in.

**Red flag:** Borders used to group things that proximity should handle. Background elements competing with foreground actions. Over-use of containers that create visual complexity without semantic value.

---

## 6. Fitts's Law and the Body

On touch interfaces, *where* something is placed matters as much as *what* it looks like. The finger is imprecise. The thumb has an arc. Reachability is a design constraint, not a detail.

**What experts internalize:**
- Touch targets: minimum 44×44pt, with adequate spacing between adjacent targets
- Primary actions belong in the thumb zone (bottom center on phone) — the most naturally reachable area
- Top corners are hardest to reach — reserve for infrequent or destructive actions
- The finger obscures what it taps — affordances must be understood before the tap, not during

**On pointer interfaces:** Apply the same logic to click target size and cursor travel distance.

**Red flag:** Primary actions in hard-to-reach positions. Targets too small or too close together. No visible tap affordance.

---

## 7. Microinteractions as Communication

Animations and transitions are the system's language. They communicate: *what just happened, what is happening, what will happen.* They are not decoration.

**What experts know:**
- Motion direction reinforces the spatial model — slide in = going deeper, slide down = dismissing
- Duration: <200ms = instant, 200–500ms = responsive, >500ms = slow
- Easing is meaning: ease-in = something leaving, ease-out = something arriving, spring = physicality
- Absence of feedback on user action creates uncertainty and erodes trust

**The four parts of a microinteraction:** Trigger → Rule → Feedback → Loop/Mode

**Red flag:** Animations with no semantic meaning. Transitions that contradict the spatial metaphor. User actions with no visible feedback. Identical animations for semantically different events.

---

## 8. Signal-to-Noise Ratio

Every element on screen competes for attention. Noise is anything that doesn't serve the user's current task.

**The ruthless audit:**
- Decorative dividers with no semantic meaning → remove
- Icons alongside text labels that say the same thing → choose one
- Color used without meaning → default to neutral
- Helper text explaining things that are obvious → remove
- Repeated information → consolidate

**The test:** "What would be lost if this element disappeared?" If the answer is "nothing" or "it would be clearer" — remove it.

**Red flag:** Visual busyness. Labels explaining other labels. Empty space that feels like a mistake rather than intent. Color everywhere.

---

## 9. Consistency as Cognitive Savings

Consistency isn't about making things look the same. It's about **reducing the number of patterns users must learn.** Every novel pattern has a learning cost. Minimize the pattern surface area.

**What this means in practice:**
- Same interaction should produce same result, everywhere
- Same visual treatment should mean same semantic meaning
- Terminology consistent throughout — don't call it "entries" here and "records" there
- A design system isn't a style guide — it's a cognitive budget. Spend it carefully.

**Red flag:** Two similar button styles with no semantic distinction. The same action labeled differently in different contexts. Interaction patterns that vary without reason.

---

## 10. Emotional Design: Three Levels

Don Norman's framework. Most designers nail level 1. World-class designers operate at all three.

- **Visceral (level 1):** Does it look and feel beautiful? First impression. Gut reaction.
- **Behavioral (level 2):** Is it efficient, effortless, and forgiving? The experience of using it.
- **Reflective (level 3):** Does it create meaning? Does the user feel capable, trusted, understood?

**For reflective design, ask:** What does the user think about themselves after using this? What does the product say about who they are or what they value?

**Red flag:** Beautiful UI that is inefficient to use (level 1 without 2). Efficient UI with no character (1+2 without 3). Reflective aspirations undermined by behavioral friction.

---

## 11. Platform Fluency vs. Platform Deference

Every platform has a language — conventions users are fluent in. Deviating forces relearning. The question isn't "should I follow the guidelines?" but "do I understand what it costs not to?"

**The expert's position:**
- Know the platform guidelines well enough to *choose* when to follow them
- Following conventions = lower learning curve, more trust, faster development
- Diverging = differentiation, but at the cost of user surprise and re-learning
- The best products extend the platform language, not replace it

**Never deviate for aesthetic reasons alone.** Deviate when the user experience is meaningfully better.

**Red flag:** Custom behaviors that fight native conventions. Non-standard navigation patterns with no clear benefit. Native controls reskinned to look custom but behave inconsistently.

---

## 12. Design for Context, Not Ideal Conditions

UIs are used in the real world: one hand, bad lighting, distracted, stressed, rushed, tired. The demo is not the use case.

**Questions experts ask:**
- What is the user's cognitive and emotional state at the moment they need this most?
- Can it be used with one hand? In bright sunlight? Half-asleep?
- Does the most critical path work in the worst plausible conditions?

**The stress test:** Describe the worst plausible moment a user opens this screen. Design for that moment first, not the demo moment.

**Red flag:** Critical actions requiring sustained attention or precise input. Important information in low contrast. Multi-step flows that assume the user is sitting comfortably with full attention.

---

## 13. Brand Voice Lives in the Interface

Colors, spacing, motion, copy — these express the brand without words. The emotional tone of the UI *is* the brand experience.

**What experts articulate:**
- Dense, efficient layout = powerful, respects your time
- Generous whitespace = calm, premium, unhurried
- Rounded shapes + soft colors = friendly, accessible
- Sharp geometry + high contrast = bold, confident, precise
- Fast, snappy motion = responsive, efficient
- Smooth, gradual motion = refined, thoughtful

**The alignment question:** Does the UI's emotional tone match what the product promises? If the brand says "calm and trustworthy" but the interface feels demanding and busy — there's a gap.

**Red flag:** Visual tone inconsistent with product positioning. In-app experience that feels completely different from the marketing. Personality-free interfaces for products that claim strong personality.

---

## The Expert's Final Check

Before calling any UI done:

1. **Hierarchy:** Can a new user identify the primary action in under 3 seconds without instructions?
2. **Cognitive load:** Can a user complete the core task while mildly distracted?
3. **States:** Does every screen have a design for empty, error, and loading?
4. **Consistency:** Does every interaction pattern appear elsewhere and behave the same way?
5. **Signal/noise:** If you greyscaled this screen and removed all labels, would the layout still communicate structure?
