# Guideline template

Target 40-60 lines. No code examples. No resources section. Save as `docs/guidelines/{topic}.md` (kebab-case).

````markdown
# {Topic} Guidelines

> {One-line goal}

## Principles

- **{Name}** - {why it matters; what breaks if ignored; technology-specific}
- ...

## Tooling

### {Tool name}

**Install:** `{install command}`
**Run:** `{run command}`
**Config ({filename}):**
```{format}
{minimal config - only settings that matter most}
```
**Key rules:** {2-4 most important rules and what they catch}

*Last verified: {YYYY-MM-DD}*
````

Several tools: one `### {Tool}` subsection per tool.
