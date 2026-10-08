# Intent

Current intent = the original sources + an ordered list of explicit changes. No artifact rewrites intent as a new summary.

## Sources

`{story_path}_index.md` `## Intent Sources` links every original: `input/*` documents, files the user supplied, and request recaps.

When intent arrives in conversation, write a recap to `{story_path}input/{date}-request.md`. It is complete, not condensed: every requirement, idea, constraint and open question raised. Show it to the user, save it after they confirm, and add it to Intent Sources.

## Changes

A phase that refines intent (brainstorm, design, plan) adds an `## Intent Changes` table to its artifact:

| Source ref | Change | New content | Why | Decided by |
|---|---|---|---|---|
| {source file + section, or earlier change row} | dropped / changed / added / deferred | {new intent} | {reason} | {person} |

## Rules

- A source item that no change row touches still applies.
- The latest explicit change wins over earlier changes, which win over the original. Order = the `_index.md` History table.
- Summaries are navigation only. Quote and link a source when it matters.

## Loading

design, plan, review-plan, implement, review and handover read every Intent Source in full, plus the `## Intent Changes` section of every earlier artifact in History, before their own process starts.

## Coverage

The plan has an `## Intent Coverage` table: each current intent item (source section or change row) -> what must be present -> plan step or target.
- review-plan checks that every source section and change row has a row, or a change marking it out of scope.
- implement verifies the table as its final step.
- review uses it as its conformance checklist.
