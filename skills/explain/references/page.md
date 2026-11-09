# Explainer page

Conventions for `docs/explainers/{concept}.html`, its outline block, the index card and verification.

## Outline block

The approved outline, as the first thing inside `<head>`. It is shown at the gate in the same shape, and the update path reads it back. `explainer.py` parses `commit:`, `date:` and the `source:` lines.

```html
<!-- explainer
goal: Understand why a reminder sometimes does not fire after a meal.
reader: Experienced iOS developer, new to this codebase.
commit: 0060a25
date: 2026-10-27
concepts: plan, sync, mirror, tombstone
core ideas:
1. plan is a pure function of entries, settings and now.
   source: Glysimi/Model/ReminderManager.swift
   misconception: a save schedules its own reminder.
   representation: predict, then a timeline of plan versus pending.
2. ...
parts: banner, problem, concepts, core ideas, break it, reading order
why parts: break it shows what the sync chain prevents.
-->
```

One `source:` line per file a core idea rests on, repository-relative. General topics cite URLs in `source:`; `stale` ignores them.

## Anatomy

A menu. Parts marked always are required; every other part is justified in `why parts:`.

| Part | When |
|---|---|
| Banner: "Explainer for humans. Not a source of truth. Built from commit X on date Y. Canonical: (note link)" | always |
| The problem in one screen: the force behind the design | always |
| Named concepts, each with one color used in text, diagrams and code | always; the concepts the reader needs, no fixed number |
| One section per core idea: predict where a misconception exists, reveal with a representation, the real code with the key lines highlighted | always |
| Lab or sandbox | the topic has dynamics |
| Break it: switch off one decision, watch the failure | the topic has design forces |
| Reading order in the code, links to the notes | repository topics |

## Build rules

- One file, inline CSS, JavaScript and SVG. No CDN, no external fonts, no network: it opens offline and does not break when a library changes.
- Desktop layout, light theme. Mobile and dark mode are not required.
- Copy code from the source at the stamped commit; do not paraphrase it. Highlight the lines that carry the idea.
- Logic the page simulates is a hand-written copy and can drift: name the source function next to it.
- Text follows the plain-writing rules. Short. The visual carries what words would over-explain.
- No spaces in file names. Name the page after the concept.

## Index card

`docs/explainers/index.html` lists the pages. One card per page:

```html
<a class="card" href="reminders.html">
  <h3>How reminders work</h3>
  <p>After this page you can predict which reminders are pending after any diary change, and why.</p>
  <div class="meta">Built from commit 0060a25 · 2026-10-27 · not a source of truth</div>
</a>
```

A missing index: create a minimal page with a title, one line saying the explainers are for humans and never canonical, and the cards.

## Makefile target

Offered when missing, added only on a yes:

```make
explainers: ## Serve docs/explainers on http://localhost:8000
	python3 -m http.server -d docs/explainers 8000
```

## Verify

1. `explainer.py check` passes.
2. Desktop browser: screenshot, read it as the reader would.
3. Try every interaction once. Console free of errors.
4. Walk the outline: every core idea is on the page, nothing on the page serves no core idea.
