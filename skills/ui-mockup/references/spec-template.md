# Spec template

The spec is `{story_path}spec.md`. It is loaded by later sessions (mockup, design, plan, implement), so keep it scannable: one item per bullet, short subsections, a status on every decision. Update it in place; it is not a dated session artifact.

Status markers, after the item: `(Decided)`, `(Proposed)`, `(Open)`. Add who and when for Decided items that reverse an earlier one: `(Decided, {user} {date})`.

```markdown
---
title: {Story title} - UI spec
updated: {date}
---
# {Story title} - UI spec

This file holds what the mockups do not show: behaviour, rules, data, edge cases and the reasons. The mockups show how it looks; this file says how it works and why.

- Tool: {Claude Design canvas | local HTML | Figma exports}
- Remote: {canvas or file URL, or "none"}
- Working copy: [docs/design/{name}](../../../../docs/design/{name}/README.md)
- Requests log: [input/{date}-mockup-requests.md](input/{date}-mockup-requests.md)

## 0. Functionality to build or change before the views
{Grouped by area: data model, shared logic, data formats, removals, not before version 1. Each item links to the section with the details.}

## 1. Principles
{Project principles for this UI. Start from the design brief; change them as the mockups show what works.}

### The mockup is a picture, not a template (Decided)
- Build with the platform's standard components, themed: {list the ones that apply, for example navigation bar, list, toggle, picker, date picker, menu, search, alert, sheet}.
- Use the real icons, fonts and logo. The mockup's stand-ins are never copied.
- Use the design tokens (section "Design system"). No colour or size values copied from the mockup source.
- Custom drawing only for: {the parts no standard component covers}.

## 2.. {One section per screen, flow or topic}
{Per item: behaviour, states, rules, edge cases, the reason. Name the artboards that show it.}

## {n}. Design system
{Tokens the mockups use (colour with light and dark values, type, spacing, radius, components, motion), mapped onto the code's token layer. Tokens to remove. Order of work.}

## {n}. Open questions
{One per bullet, with who decides.}

## {n}. Future ideas
{Ideas out of scope for this story, to be split into stories later.}
```

## Requests log

`{story_path}input/{date}-mockup-requests.md`: the user's own messages, verbatim, one section per message: `## {n}. {short topic} ({date})`, then the message text. Write it by hand. Do not copy session transcripts into the repository with scripts.
