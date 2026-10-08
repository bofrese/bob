# Prompt engineering principles

Principles for writing effective, token-efficient skills. Apply when creating, reviewing or improving one. Structure and frontmatter rules: `authoring-rules.md`.

## Core principles

- **Be explicit.** "Write 5 bullets, each under 15 words" beats "be concise". Specify exact success criteria.
- **Structure clearly.** Separate rules, role, process and output. Do not mix them in prose.
- **Minimize tokens.** Every token costs money and latency. High-signal only. Cut filler, redundancy, verbose examples.
- **Load just-in-time.** Do not dump context upfront. Load principles and guidelines when they apply.
- **Allow uncertainty.** Permission to say "I don't know" reduces hallucinations.
- **One question at a time.** Multi-part questions fragment attention.
- **Perfect examples.** Models pay close attention to details. Sloppy examples teach sloppy behaviour.
- **Standalone outputs.** Documents must be readable without the conversation. Standalone is not verbose: essentials only.
- **Avoid over-constraining.** "You are a helpful architect" beats "You are a world-renowned expert who never makes mistakes."
- **No aggressive language.** Current models follow instructions. "CRITICAL: YOU MUST" causes over-triggering. Use normal language.
- **Descriptions trigger the skill.** The description is all the model sees before loading: what the skill does and when to use it, with the user's likely words first.

## Human-owned-workflow design rubric

When creating or reviewing a skill, check that it defines each of these. Token efficiency must not remove any of them, since they preserve human ownership:

- the single fundamental question the skill answers;
- explicit human and AI roles;
- evidence requirements for any claim;
- an interaction policy appropriate to experience level (do not infer lack of thought from brevity);
- the autonomy boundary (what AI may decide, what it must surface);
- stop and escalation conditions;
- the exit condition, including a valid short or no-op outcome;
- the artifact contract (what, if anything, must survive the session);
- progressive-disclosure triggers (when to load deeper reference material);
- proportional and skip behaviour (the fast path stays available);
- positive, negative and no-op test scenarios;
- instruction-conflict and prompt-growth review: does an addition contradict or duplicate the hub or another skill?

## Anti-patterns

- **Unstructured instructions:** context, constraints and format mixed in prose.
- **Aggressive triggers:** "CRITICAL!", "MUST!", "NEVER!" cause over-triggering.
- **Vague constraints:** "be concise" instead of "3-5 sentences, under 100 words".
- **Poor examples:** incomplete, inconsistent or unrealistic.
- **Context dumping:** loading everything upfront instead of just-in-time.
- **Multi-question barrages:** asking 5 things at once instead of one at a time.
- **Typography:** never the em dash (U+2014) in skill files. Use "-", a comma or a full stop.
- **Verbose outputs:** generated files become future context. Their style is owned by the hub's `references/writing.md`; a skill's Output section points there instead of restating style rules.

## Output templates

Every artifact template follows the hub's `references/writing.md`: it starts with a `## TL;DR` section and uses only its icon vocabulary. When a template and `writing.md` disagree, `writing.md` wins and the template is fixed.

Include: date and identifier, status or verdict, issues and decisions (bulleted, brief), next actions if any.

Exclude: prose methodology explanations, percentage calculations, verbose rationales, repeated context, introductions and acknowledgements.
