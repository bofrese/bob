# UI lenses 1-7: the screen and the body

Contents: 1. Visual Hierarchy is Not About Size, 2. Cognitive Load is the Real Enemy, 3. States Are the Real Design, 4. Typography as Functional Architecture, 5. Gestalt: Design with Perception, Not Against It, 6. Fitts's Law and the Body, 7. Microinteractions as Communication

## 1. Visual Hierarchy is Not About Size

Users don't read - they scan. The eye follows contrast, weight, spacing, and position in a predictable sequence. Good hierarchy creates a reading order that matches the user's priority sequence.

**What separates expert from average:**
- Think in *contrast ratios between elements*, not just individual element size
- Negative space is an active design element - it directs attention as powerfully as content
- Color, weight, and position are hierarchy signals; decorative icons and labels often aren't
- The reading order should be *designed*, not accidental

**Red flag:** Important actions buried in visual noise. Secondary content competing with primary content. Everything the same weight.

## 2. Cognitive Load is the Real Enemy

Every decision point, every unfamiliar pattern, every ambiguous label adds cognitive load. Users have a budget. Exceed it and they abandon, make errors, or distrust the interface.

**Hick's Law:** More choices = longer decision time. Reduce options at each decision step.
**Miller's Law:** Working memory holds ~7 items. Don't exceed it in a single view.
**Progressive disclosure:** Reveal complexity at the pace of user commitment - don't front-load.

**The expert's move:** Distinguish between *complexity* (inherent to the domain) and *complication* (your fault). Ruthlessly eliminate complication.

**Red flag:** More than 5–7 interactive elements competing for attention. Options without clear hierarchy. Labels that require interpretation.

## 3. States Are the Real Design

The happy path is easy. The quality of an interface is revealed in its edges: empty states, error states, loading states, partial data, offline, disabled.

**What experts obsess over:**
- Empty states are onboarding opportunities, not blank screens
- Error messages in user language, not system language
- Loading states as moments to build trust, not just wait
- Every interactive element has visible: default, hover/focus, active, disabled states

**Red flag:** Screens that only work with ideal data. Errors that say "Something went wrong." No indication of loading progress or duration.

## 4. Typography as Functional Architecture

Typography isn't style - it's structure. It establishes hierarchy, sets reading rhythm, and communicates tone without words.

**The fundamentals experts apply:**
- **Line length:** 45–75 characters for body text. Shorter = choppy. Longer = eye-tracking fatigue.
- **Leading (line-height):** Tight = tension, urgency. Loose = calm, spacious. Match to content mood.
- **Weight over size:** Changing weight communicates importance with less visual disruption than changing size.
- **Scale is a contract:** A type scale creates hierarchy expectations. Break it intentionally, never accidentally.

**Red flag:** Uniform weight throughout. Body text wider than 75 chars. Line-height below 1.4. Headings and body text indistinguishable at a glance.

## 5. Gestalt: Design with Perception, Not Against It

The brain organizes visual input into patterns automatically. Experts exploit this. Average designers fight it.

**The principles that matter in practice:**
- **Proximity:** Elements close together are perceived as related. Don't break this accidentally.
- **Similarity:** Visual consistency signals semantic consistency - same treatment = same behavior.
- **Common region:** A container (card, background fill) groups elements more powerfully than proximity alone.
- **Figure/ground:** Background activity competes with foreground tasks. Suppress it.
- **Closure:** Users complete incomplete shapes. You don't need to box everything in.

**Red flag:** Borders used to group things that proximity should handle. Background elements competing with foreground actions. Over-use of containers that create visual complexity without semantic value.

## 6. Fitts's Law and the Body

On touch interfaces, *where* something is placed matters as much as *what* it looks like. The finger is imprecise. The thumb has an arc. Reachability is a design constraint, not a detail.

**What experts internalize:**
- Touch targets: minimum 44×44pt, with adequate spacing between adjacent targets
- Primary actions belong in the thumb zone (bottom center on phone) - the most naturally reachable area
- Top corners are hardest to reach - reserve for infrequent or destructive actions
- The finger obscures what it taps - affordances must be understood before the tap, not during

**On pointer interfaces:** Apply the same logic to click target size and cursor travel distance.

**Red flag:** Primary actions in hard-to-reach positions. Targets too small or too close together. No visible tap affordance.

## 7. Microinteractions as Communication

Animations and transitions are the system's language. They communicate: *what just happened, what is happening, what will happen.* They are not decoration.

**What experts know:**
- Motion direction reinforces the spatial model - slide in = going deeper, slide down = dismissing
- Duration: <200ms = instant, 200–500ms = responsive, >500ms = slow
- Easing is meaning: ease-in = something leaving, ease-out = something arriving, spring = physicality
- Absence of feedback on user action creates uncertainty and erodes trust

**The four parts of a microinteraction:** Trigger → Rule → Feedback → Loop/Mode

**Red flag:** Animations with no semantic meaning. Transitions that contradict the spatial metaphor. User actions with no visible feedback. Identical animations for semantically different events.
