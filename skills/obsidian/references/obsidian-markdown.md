# Obsidian-Flavored Markdown

Reference for writing and reading `.md` files in an Obsidian vault. Covers the extensions Obsidian adds on top of standard CommonMark.

## Link Formats

Two competing link styles exist in Obsidian vaults. Understand both; choose deliberately.

### Wikilinks (Obsidian-native)

```markdown
[[note-name]]                     # link by filename (no extension)
[[note-name|display text]]        # link with alias
[[note-name#Heading]]             # link to a heading
[[note-name#^block-id]]           # link to a specific block
![[note-name]]                    # embed (inline the content)
![[image.png|300]]                # embed image with width
```

**Pros:** Auto-updated by the Obsidian CLI on rename/move. Short and readable.
**Cons:** Not standard markdown. Tools and LLMs outside Obsidian cannot resolve them without the vault index. Breaks when read as plain text.

### Standard Markdown Links (relative paths)

```markdown
[display text](path/to/note.md)   # relative link from vault root
[display text](../other/note.md)  # relative path
```

**Pros:** Universally understood by all tools, LLMs, and renderers. Works outside Obsidian.
**Cons:** Not auto-updated by the Obsidian CLI. After renaming a file, any standard markdown links pointing to it must be updated manually.

### Recommendation for bob-generated files

Use **standard relative markdown links** for predictable LLM consumption and tool interoperability. After renaming a file via the obsidian skill, search for broken standard links:

```bash
grep -r "](old-name.md)" . --include="*.md"
grep -r "](path/old-name.md)" . --include="*.md"
```

Update them manually or note them in the operation report.

---

## Properties (Frontmatter)

YAML block at the top of a file. Obsidian reads and indexes these.

```yaml
---
title: My Note
date: 2026-05-29
tags:
  - topic/architecture
  - status/draft
status: draft
aliases:
  - alternate name
cssclasses:
  - kanban
---
```

**Built-in property names:**
- `tags` - searchable labels (also usable inline as `#tag`)
- `aliases` - alternative names for wikilink resolution
- `cssclasses` - apply CSS classes (used by plugins like kanban)

Set a property via CLI without editing the file:
```bash
obsidian property:set path="docs/file.md" name="status" value="done"
```

---

## Tags

Two syntaxes, same result:

```markdown
---
tags: [architecture, status/draft]
---

Inline tag: #architecture
Nested: #status/draft
```

Nested tags (`#parent/child`) create a hierarchy in Obsidian's tag panel. Use them for structured classification (e.g. `#status/done`, `#type/decision`).

List all tags in the vault:
```bash
obsidian tags sort=count counts
```

---

## Callouts

Highlighted blocks for emphasis. More expressive than bold text.

```markdown
> [!note]
> Default callout with no title change.

> [!warning] Watch out
> Custom title. Supports **markdown** inside.

> [!tip]- Collapsible tip
> The `-` after the type makes it collapsible.
```

**Supported types:** `note`, `tip`, `info`, `warning`, `danger`, `example`, `quote`, `abstract`, `success`, `failure`, `bug`, `question`

Useful in bob-generated docs for surfacing assumptions, warnings, and key decisions inline.

---

## Embeds

Include content from another file inline:

```markdown
![[note-name]]              # embed entire note (wikilink style)
![[note-name#Heading]]      # embed a specific section
```

No standard markdown equivalent. Prefer explicit links for LLM-readable docs unless the vault is Obsidian-only.

---

## Comments

Hidden from rendered output:

```markdown
%% This text is hidden in Obsidian preview mode %%

%%
Multi-line comment.
Not visible when rendered.
%%
```

Useful for LLM-facing instructions embedded in a note without cluttering the rendered view.
