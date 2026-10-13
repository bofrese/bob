# Audit Mode

Check existing notes and `docs/` against the code. Runs on explicit request (refresh, sync, check docs).

## Steps

1. **Collect claims.** For each note in scope: files referenced, behavior described, dependencies, patterns and their status, `Verified by` links.
2. **Check claims against the code.** Use `git log --since` the note's `Last verified` date for the referenced files. Check that referenced files exist and still do what the note says. Look for new code in the same area that no note covers.
3. **Check patterns, naming and smells** with the `architect` skill, `references/patterns.md` and `references/concepts.md`: new variants of an established pattern, competing patterns not recorded, naming drift between notes and code, duplicated concepts, and design smells (scattered, duplicated or hard-to-locate concepts). Record a smell on a documented concept in its note (`## Inconsistencies`, ⚠️ marker) once confirmed, and raise it as a question; never fix the code.
4. **Classify** each finding: **stale** (changed or gone), **missing** (code or concept not covered), **drift** (pattern, naming, interface or organization), **accurate**.
5. **Walk through findings** one topic at a time. For each: is the change intentional (update the note) or is the code wrong (route as work, do not fix)?
6. **Check `docs/` placement.** List `docs/` files outside known homes (`architecture/`, `product/`, `guidelines/`, `domain/`, `process/`, `README.md`). For each, propose where it belongs: architecture note, guideline, product doc, knowledge vault, or delete. Confirm per file before moving anything. Before retiring a doc, run the fact check and link retargeting from Discover step 7. Move markdown through the `obsidian` skill so links stay intact, never with plain `mv` or `git mv`.
7. **Check the index.** Every note has a row, every "Read when" names a task someone would actually be doing, and "How it fits together" still matches the code.
8. **Write** the agreed updates and refresh `README.md` and `Last verified` dates.
