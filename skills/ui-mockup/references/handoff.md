# Handoff

The handoff makes the mockups usable by a builder (a person or a later AI session) who never saw the conversation. Do it before the session ends and after each larger change, not once at the end.

## What a builder needs, in read order

1. The spec: behaviour, rules and the "picture, not a template" contract.
2. A screenshot of the artboard: layout, hierarchy, spacing. AI sessions read images directly; a picture is the right input for layout.
3. The mockup source: only for an exact value (a colour, a size, a text).

## Checklist

- [ ] `docs/design/{name}/screens/{Artboard}.png`: one screenshot per artboard, at the artboard's own size, made after the last change.
- [ ] `docs/design/{name}/README.md` from the template below, with the artboard-to-code map filled in from the real code (search for the current file of each screen; "new" when there is none).
- [ ] A pointer row in the repository instructions (the documentation table in `CLAUDE.md` or `AGENTS.md`) and in the docs index, if the project has one.
- [ ] A link from the spec header to the working copy.
- [ ] The local preview renders when opened plainly: the folder listing, a single file with no parameters, the gallery with no parameters. Checked by opening it that way, not only by the route you used to build it.
- [ ] Old design guidelines that the new design contradicts are named in the spec's open questions, so a builder does not follow both.

## README template

```markdown
# {Name} mockups

Repository copy of the mockups from story {ID}. Remote: {URL or "none"}.

The mockups show how the screens look. They do not say how they work. The rules, behaviour and decisions are in the [spec]({relative path to spec.md}).

## How to use this when you build

Read in this order:
1. The spec. Read "The mockup is a picture, not a template" first.
2. The screenshot in `screens/` for the screen.
3. The source file for the screen, only for an exact value.

Rules:
- Do not translate the mockup source literally. Use the platform's standard components and theme them.
- Do not copy colour or size values. Use the design tokens in {token file}.
- Use the real icons and fonts.
- Each screenshot shows one state. Other states are in the spec or in other artboards.

## Files
{Table: path, what it holds. Name the files that are local preview only and never published.}

## Artboards and the code they change
{Table: artboard, what it shows, current file or "new". Mark explorations that were not chosen.}

## Preview locally
{Numbered steps from the tool reference.}

## Keep this folder and the remote in step
{From the tool reference: download before editing, publish after, make the screenshots again.}
```
