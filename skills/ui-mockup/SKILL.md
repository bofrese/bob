---
name: ui-mockup
description: "Bob's UI mockup phase. Designs app screens, web pages or flows as visual mockups (Claude Design canvas, local HTML, Figma exports) with a living spec beside them, then hands them to builders with screenshots and a code map. Use when a UI must be designed visually before it is built."
license: Apache-2.0
allowed-tools: Bash(*), Read, Write, Edit
---

# UI mockup

Invoke the `bob` hub skill (`bob:bob`) and run its start checklist.
Loads: hub story, intent, project-knowledge; files docs/product/design-brief.md

Fundamental question: what should this UI look like, and what must a builder know that the picture does not show?

## Rules

- The working copy lives in the repository from the first mockup, in `docs/design/{name}/`. Never only in temporary storage, never only in a remote tool. Temporary folders are cleared without warning.
- The mockup shows the look. The spec (`{story_path}spec.md`) holds behaviour, rules, data, edge cases and reasons. Every decision goes into the spec in the same turn, marked Decided, Proposed or Open. This includes ideas raised only in chat and ideas out of scope (section "Future ideas").
- The user's own messages go verbatim into `{story_path}input/{date}-mockup-requests.md`, one numbered section per message, written by hand.
- This skill holds no design principles. Load the `ui-design` skill for every design judgment. Project principles start from the design brief and live in the spec, where they may change as the mockups show what works. A deliberate break with a `ui-design` lens is recorded in the spec with its reason.
- The mockup is a picture, not a template. Write this into the spec at the start: the build uses the platform's standard components, real icons and fonts, and the code's design tokens. The mockup's hand-drawn controls and stand-in icons are never copied.
- Before you edit, check the remote tool for a newer version (the user may have edited there). Download it into the working copy first.
- Show, then ask. Present a mockup change and one question about it. The user owns every look-and-feel decision; Proposed stays Proposed until they say otherwise.
- Websites built with the b2 plugin: use `b2:design`, which owns site mockups and theme generation.

## Role

Product designer and design partner. Make the mockups, keep the spec honest, push back on choices that hurt the user's goal (with the `ui-design` lens that says why), and make sure the result survives the session and reaches the people who build it.

## Process

### 1. Set up (once per story)

1. Read the story's `spec.md` if it exists: a returning session continues from it. Read the design brief and the vision. Missing brief: offer the `brand-design` skill first, but follow the user's choice.
2. Choose the tool. If the spec header already names one, use it. Otherwise check whether a Claude Design artifact type is available (Artifact tool, `action: quickstart`, `intent: design`) and ask once:
   - **Claude Design canvas** (default when available): `references/tool-claude-design.md`.
   - **Local HTML files**: `references/tool-local-html.md`.
   - **Figma**: only with a Figma connector in the session. Without one, the user designs in Figma and exports frames into `screens/`; this skill keeps the spec and the handoff.
3. Create the spec from `references/spec-template.md`, with the tool, the remote link and the working copy path in its header. Register it in the story History (Type: UI Mockup).
4. Create the working copy folder and its README from the template in `references/handoff.md`.

### 2. Mockup loop

1. Sync from the remote tool if it has a newer version.
2. Make the change, one artboard per screen and per state that matters: empty, error, loading, larger text, dark, other languages. Explorations go in a separate, labelled row and say so in their title.
3. Judge it with the `ui-design` lenses that apply. Fix what fails before you show it.
4. Publish or preview per the tool reference, and look at the result yourself (screenshot) before you show it.
5. Update the spec and the input log in the same turn.

### 3. Spec sections that grow with the work

Keep these current, not only at the end (template in `references/spec-template.md`):
- **Functionality before the views**: model, logic, data format and removal work that the mockups need. Visual sessions find this work; it is often the larger part.
- **Design system**: the tokens the mockups use, mapped onto the code's token layer.
- **Open questions** and **Future ideas**.

### 4. Handoff (before the session ends, and after each larger change)

Follow `references/handoff.md`: a screenshot per artboard, the README with read order and an artboard-to-code map, a pointer in the repository instructions, a local preview that renders when opened plainly. Check the preview the way a person would open it: no parameters, from the folder listing.

### 5. Exit

- Principles marked Decided that hold beyond this story: propose them for the design brief (`brand-design` owns it), with the user's confirmation.
- A lesson about good UI that holds for any product: stage it for `learn`, never in agent memory.
- A spec that holds more than one releasable piece of work: propose the split into stories (functionality, design system, views per area) and route it per the hub tracking rules.
- Risky model or data changes in the functionality section: name `design` (Design Record) as the next phase.

## Output

- `docs/design/{name}/`: the working copy, `screens/`, `README.md`.
- `{story_path}spec.md`: the living spec. `{story_path}input/{date}-mockup-requests.md`: the user's words.
- A pointer row in the repository instructions (for example the documentation table in `CLAUDE.md`).

Finish with the hub's finish checklist.
