# Ingest Mode

Ingest an external source (URL or local file) into the vault. Extracts atomic concepts, runs reconcile on each, proposes note updates or creates new notes.

## Step 1: Fetch and Extract

**URL source:**
```bash
# Fetch content
curl -sL "<url>" -o /tmp/ingest-source.html 2>/dev/null || true
```
If curl fails or returns non-markdown: use the WebFetch tool to read the URL content directly.

**Local file:**
Read the file directly.

## Step 2: Identify Atomic Concepts

Read the fetched content and extract key atomic concepts worth persisting in the vault. Each concept should be:
- A single distinct idea (not a topic summary or full article)
- Self-contained — makes sense without the source
- Worth linking to or referencing in future notes

Propose a list of candidate concepts (title + one-line description). Show the list and get confirmation before proceeding.

## Step 3: Run Reconcile on Each Concept

For each confirmed concept:
1. Read `skills/vault/reconcile.md` and run the full reconcile procedure
2. Reconcile determines: merge, enrich, split, or create-new
3. Execute confirmed actions (same as process mode)

## Step 4: Save Raw Source

Save the original source material to `sources/`:
- URL: save as `sources/{topic}/{YYYY-MM-DD}-{short-slug}.md` (or `.html` if not markdown). Create a topic subfolder if 3+ sources already cover the same topic; otherwise file flat.
- Local file: move to `sources/` using `obsidian move` (vault active) or `mv` (vault offline).

Add `resource: sources/{path}` to the frontmatter of all atomic notes created from this source.

## Step 5: Log and Report

Call `log_append.py`:
```bash
python3 bob/skills/vault/scripts/log_append.py ingest "Source: <url-or-filename>. Extracted N concepts. Merged X, enriched Y, created Z new."
```

Report: source ingested, concepts extracted, actions taken.

## Rules

- Always confirm the concept list before running reconcile — user may remove irrelevant items
- Run reconcile before creating any note — no exceptions
- Save raw source to `sources/` — do not delete it
- For all vault moves: use `obsidian move` if vault active, fall back to `mv`
