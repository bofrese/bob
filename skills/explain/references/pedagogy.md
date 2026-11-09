# Pedagogy for expert readers

Techniques for the outline. Each has a use, a misuse and its source. Pick per core idea; most pages need few of them.

## Principles

- **Coherence.** Exclude words, pictures and interactions that do not serve the learning goal. (Mayer, coherence principle)
- **Expertise reversal.** Guidance that helps novices burdens experts. Experts learn more from a problem to solve than from a worked walkthrough. Skip basics, give the problem. (Kalyuga; cognitive load theory)
- **Pretraining.** Name the key concepts and their characteristics before the complex part. (Mayer, pretraining principle)
- **Segmenting.** Small, reader-paced steps beat one long flow. A stepper beats autoplay. (Mayer, segmenting principle; Distill reports better comprehension for step layouts than scroll)
- **Signaling.** Cue what matters: highlight the key lines, one color per concept everywhere. (Mayer, signaling principle; Ciechanowski color-codes terms between text and diagrams)
- **Complementary, not redundant.** Text and visual say different things. A diagram that repeats the paragraph hurts. (Mayer, redundancy principle)
- **Start from the problem.** Show the force that made the design necessary before the design. (Nicky Case: show what made you care)

## Techniques

| Technique | Use when | Do not use when | Source |
|---|---|---|---|
| Predict, then reveal | A misconception is likely: ordering, edge case, failure path, "what happens if". Feedback right after the guess. | Everyone would guess right; it teaches nothing | Pretesting effect; Kim et al. "You Draw It"; Case "Place your bets" |
| Connected representations | One idea has several forms: code, state, timeline, diagram. Hover or step in one highlights the others. | The forms say the same thing | Distill, multiple representations |
| Real code, key lines highlighted | Always for repository topics: the reader must find it again in the editor | A general topic without a canonical implementation | Bob: the code is the territory |
| Stepper through a flow | Ordering matters: a request path, a sync, a migration | The flow has one step | Segmenting |
| Explorable parameter | An outcome depends on a value: a timeout, a threshold, a size | The relation is linear and obvious | Victor, Explorable Explanations |
| Lab or sandbox | Dynamics: state over time, interacting parts. Start simple, unlock more. | No dynamics; it becomes a toy | Case "Sandbox mode"; Distill |
| Break it | A design decision exists because of a force: switch it off and the reader watches the failure it prevents | No real alternative was ever possible | Case "Puzzle it out" |
| Details on demand | Precise detail some readers need: exact values, rare edge cases | The detail is a core idea; it belongs in the main text | Distill, details on demand |
| Static diagram | Structure without dynamics: boundaries, ownership, data shapes | Understanding depends on change over time | Distill: not everything needs to be interactive |

## Misconceptions are the material

Predictions and "Break it" work only on real misconceptions. Find them where intuition and code disagree:
- tests that assert surprising behaviour;
- guards, retries and ordering constraints with a "why" comment;
- bugs fixed in git history;
- rejected alternatives in Design Records.

A core idea without a misconception gets a representation, not a prediction.

## Costs

Interactivity costs authoring time, breaks when the code moves and is often unused (Distill; Amit Patel uses it on some pages only). Choose the cheapest technique that makes the idea clear.
