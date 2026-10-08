# Context loading

Load the minimum context the phase needs for its own judgment. Keep decisions and evidence from earlier phases; do not import their full reasoning.

## How a phase skill declares its loads

Each phase skill has one `Loads:` line near its top, for example:

```text
Loads: hub story, intent, project-knowledge, code-graph; files docs/product/vision.md
```

- `hub <name>`: read `references/<name>.md` in this skill's folder and follow it.
- `files <path>`: read the project file if it exists. Skip it silently if it does not.
- `story <type>`: read the newest `{story_path}sessions/{date}-{type}-{slug}.md`, for example `story brainstorm`, `story design`, `story plan`, `story review-plan`, `story implement`, `story handover`. `story review` skips `review-plan` files. Skip silently if there is none. A path the user gives wins.
- A phase skill may narrow a loader, for example "architecture notes linked from the Handover only". Its words win over the defaults here.
- Read each file once per conversation.

## Always

- Personal profile: if `personal/interaction-profile.md` exists, read it. It holds this developer's preferences (verbosity, question style). Skip silently if absent.
- Orientation: if `graphify-out/GRAPH_REPORT.md` exists, read only its `## Community Hubs (Navigation)` section. Otherwise explore the project structure briefly. Stay quiet about both.

## Defaults when no phase skill is active

The user describes engineering or product work without a bob skill:
- Engineering work: `project-knowledge` and `code-graph`.
- Product work: `docs/product/README.md` or `docs/product/vision.md`.
- Story only if the work will write a session artifact.
