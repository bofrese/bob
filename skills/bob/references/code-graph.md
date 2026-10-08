# Code graph

Uses a graph built by graphify. Read-only: never write `graphify-out/` and never rebuild during a phase.

## Is it usable?

Usable only if all hold, otherwise say nothing about the graph and use grep and file reads:
- `command -v graphify` succeeds and `graphify --version` is 0.9.11 or later.
- `graphify-out/graph.json` exists, has nodes, and its node count matches `graphify-out/GRAPH_REPORT.md`.
- graphify reports no material corruption, and no graphify call fails.

## Freshness

- `graphify hook status` shows the hook installed: committed code is current. If `git status --porcelain` shows code edits, note "graph excludes uncommitted edits".
- No hook: run graphify's `detect_incremental` through the graphify skill. If files changed, report "stale: N files changed, run `/graphify . --update`". Do not run it yourself.

Report one line: fresh, fresh without uncommitted edits, or stale.

## Queries

Ask the graph before grep for code-relationship questions:

| Question | Command |
|---|---|
| What depends on X, blast radius | `graphify affected "X"` |
| How does A reach B | `graphify path "A" "B"` |
| What is X, its neighbours | `graphify explain "X"` |
| Open-ended only | `graphify query "<question>"` |

- Always pass `--budget N` and scope with `--context` (repeatable). Exclude test nodes for architecture questions.
- Symbol questions: call the CLI. Fuzzy or natural-language questions: use the graphify skill.
- Never read or traverse `graph.json` yourself. Never use `graphify prs`.
- Graph results show references and paths. What they mean for the architecture is a human judgment, backed by reading the code.
