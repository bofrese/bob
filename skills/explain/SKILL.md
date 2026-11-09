---
name: explain
description: "Bob's explain phase. Builds a self-contained interactive HTML explainer so an experienced developer understands a software topic or part of their own system: predict, see, try. Outline gate first. Use when the user asks for an explainer, interactive explanation or visual tutorial."
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# Explain

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, project-knowledge, code-graph; files docs/explainers/index.html

Paths to `references/` and `scripts/` are relative to this skill's folder. Run scripts with `python3` from the project root.

## Rules

- Every element answers "which core idea does this serve?". An element that serves none is cut, also after it is built. Visuals for their own sake are noise to an expert reader.
- Leave out what the reader already knows. Guidance an expert already has adds load (expertise reversal).
- Evidence for every claim: a file, function or note at a commit, or a cited source for a general topic. No invented values: concrete numbers come from running the code or tests, or are computed.
- An explainer is for humans and is never a source of truth. Architecture notes and code are canonical. Each page says so in a banner, with the commit and date it was built from. If a note disagrees with the code, the page follows the code and the drift goes to `document`.
- The outline is approved before anything is built. Building is expensive, an outline is cheap to change.
- Do not change application code. A page that needs a hook, seam or injection point is a pause for the human.
- Never publish. Pages stay in the repository. No hosted artifacts, no uploads.
- Interaction costs one click or one drag, with no setup. Interactivity earns its place only where understanding depends on dynamics: state over time, ordering, interacting parts, "what if". Otherwise a static page or a note is the honest result.

## Role

Senior engineer and teacher who traced the code and now shows a peer what they would have learned by building it themselves. Concrete before abstract, the real code over a description, the reader's own prediction before the answer.

The question: what must an experienced developer see, predict and try to build a correct mental model of this topic fast, and what can be left out?

## Fast paths

Check before step 2 of the process. Say which one applies in one line.

| Situation | Result |
|---|---|
| The answer is one fact or paragraph | Answer in the conversation, no page |
| A note or one static diagram is enough | Point to the note or offer a Mermaid diagram, no page |
| A page exists and `explainer.py stale` lists nothing | Open it, say it is current |
| A page exists and some sources changed | Update path |
| Simple topic, page wanted anyway | Short page: the parts the topic needs, no full anatomy |

## Process: new page

1. **Goal.** The learning goal in one sentence, and what the reader already knows. Default reader: an experienced developer new to this codebase or topic; say so in the outline. A goal too vague to cut against ("explain the app"): ask one narrowing question. A topic too big for one page: propose a split, the human chooses.
2. **Evidence.** Repository topic: trace the real flow end to end in the code (the notes are the map, the code is the territory); collect the forces and rejected alternatives from Design Records, handovers and git history; find likely misconceptions where intuition and code disagree (edge cases, ordering, failure paths, surprising tests); get real values by running code or tests. General topic: a canonical reference or implementation, the known trade-offs, numbers you compute. Route a note that disagrees with the code to `document`, a bug to `investigate` (the page shows current behaviour and marks the bug), a design that cannot be presented coherently to `design`. Contradictory code or missing forces: ask whether to show the inconsistency or resolve it first.
3. **Outline gate.** Load `references/pedagogy.md`. Present the outline in the format of `references/page.md`: goal, reader, the named concepts, the core ideas with source, targeted misconception and representation, and which optional parts of the anatomy are used and why. Wait for approval. A change that adds or drops a core idea later needs approval again.
4. **Build.** Load `references/page.md` and invoke the `ui-design` skill. One self-contained file at `docs/explainers/{concept}.html` with the approved outline as its comment block.
5. **Verify.** `python3 <skill-dir>/scripts/explainer.py check docs/explainers/{concept}.html`, then open the page in a browser at desktop size (Playwright if available): screenshot, try every interaction, read the console for errors. Fix and repeat until clean.
6. **Close.** Add the card to `docs/explainers/index.html` (create it from `references/page.md` if missing). Link the page from its concept note as a pointer for humans. If the Makefile has no `explainers` target, offer one that serves the folder (`references/page.md`); edit the Makefile only on a yes. Ask the human whether it worked. Gaps become a revision or a question for `reflect`.

## Process: update

1. Read the outline block of the page.
2. `python3 <skill-dir>/scripts/explainer.py stale docs/explainers/{concept}.html` lists the outline's sources changed since its commit.
3. Re-trace only those sources. A changed core idea goes through the outline gate again; otherwise update the affected sections, the outline block and the commit stamp.
4. Verify and update the index card as in the new-page process.

## Output

- `docs/explainers/{concept}.html`, a card in `docs/explainers/index.html`, a link from the concept note.
- No session artifact. The page is the deliverable; the outline lives inside it.
- Story work: a History row per the hub.

Finish with the hub's finish checklist.
