# Update Mode

Bring the notes in line with what a story actually built. Runs after Review, before Handover.

## Inputs

- The story's Design Record (intent), Implementation Note and Review (what was built, deviations, signals).
- The code changed by the story (`git log --grep {STORY-ID}`, or the diff the human names).
- `docs/architecture/README.md` and the notes it points to for the touched concepts.

## Steps

1. **List affected notes.** For each concept the change touched: unchanged, needs update, or new concept. Describe the implemented system, not the Design Record. Where they differ, the code wins and the difference is worth a line in the handover.
2. **Check patterns** with `bob:architect` `references/patterns.md`:
   - Did the change follow the `established` pattern for its problem?
   - Did it introduce a new or competing variant? Record it in the pattern note (`competing`, open question) and tell the human.
   - Did it strengthen an `emerging` pattern? Propose promotion; the human decides.
3. **Check drift** in the touched area (architecture, naming, interface, source-organization drift, duplicated concepts). Report with evidence. Do not fix code.
4. **Propose the change list** (note, change, reason) and get confirmation.
5. **Write** the notes and update `README.md`. Set `Last verified` on each touched note.

Keep it story-scoped. Drift outside the touched area goes to work routing, not into this update.
