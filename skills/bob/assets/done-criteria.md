# Done Criteria

> This file is maintained by bob and by humans.
> bob adds entries when a phase introduces new artifact types.
> Humans can add, remove, or edit entries at any time.

---

## READY - Before work starts

These must be true before `implement` (or any execution phase) begins:

- [ ] A plan exists and has been reviewed (in story folder)
- [ ] Tests pass at baseline (green before any changes)
- [ ] Applicable guidelines have been read (`docs/guidelines/`)

---

## DONE - Before output is considered complete

Every phase checks applicable items before finishing.

### Code changes (`implement`, `dev`)
- [ ] All tests pass (existing and new)
- [ ] Linter/formatter clean on modified files
- [ ] No hardcoded secrets or debug code

### Documentation (`document`)
- [ ] `docs/architecture/README.md` index lists every concept and pattern note
- [ ] Each touched note is atomic (one concept) and has a current `Last verified` date
- [ ] Pattern status `established` was set by the human, never by the AI

### Handover (`handover`)
- [ ] Change set confirmed by the human (scope per repo, staged files)
- [ ] Every changed file is narrated or listed in a sweep (`gather.py --check` prints nothing)
- [ ] Reading order is conceptual, not file or diff order; changed code is shown, not paraphrased

### Plans (`plan`)
- [ ] Plan is self-contained (readable without prior context)
- [ ] Testing strategy defined
- [ ] Questions & Decisions table populated

### Reviews (`review`, `review-plan`, `ui-review`)
- [ ] Findings categorised by severity
- [ ] Action items are actionable and prioritised

### Investigation and ideas (`investigate`, `brainstorm`)
- [ ] Findings or options are written to the story, not left in chat
- [ ] Root cause or chosen direction is stated with its evidence
- [ ] Open questions are listed

### Design (`design`)
- [ ] Material concepts and human-owned decisions are explicit
- [ ] Repository claims have evidence
- [ ] Complexity removed, introduced, or moved is addressed
- [ ] Blocking uncertainty is resolved or clearly marked

### Reflection (`reflect`)
- [ ] Critical mental model and code paths were examined proportionally
- [ ] Ownership gaps, if any, are explicit

### Harness learning (`learn`)
- [ ] Proposed lessons cite evidence
- [ ] Persistence destination and downside are explicit
- [ ] Weak or one-off lessons may be rejected

---

*Last updated: {date}*
*Maintained by: bob and humans*
