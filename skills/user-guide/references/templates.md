# Templates

## User Guide Template

```markdown
# {Product Name} - User Guide
*Last updated: {YYYY-MM-DD}*

## What is {Product Name}?
One paragraph. What it does, who it's for, what they accomplish with it.

## Getting Started
The single entry point for new users. Step-by-step from zero to first value.

## {Core Task 1}
What the user wants to accomplish. Steps, examples, expected outcomes.

## {Core Task 2}
...

## {Core Task N}
...

## Troubleshooting *(optional)*
Only include if there are well-known failure modes with clear resolutions.
```

## Findings Report Template

```markdown
# User Guide Findings - {slug}
*Date: {YYYY-MM-DD} | Guide: {path-to-guide}*

## TL;DR
{3-6 bullets. First: the overall alignment between product vision and implemented reality.}

## Findings

| # | Area | Finding | Severity | Suggested Direction |
|---|------|---------|----------|---------------------|
| 1 | {area} | {what's wrong or missing} | High/Med/Low | {concrete suggestion} |

## Unverifiable Features
Features mentioned in vision/personas that could not be confirmed in the codebase:
- {feature}: {where it should be, why it matters}

## Opportunities
Improvements that would significantly improve the user experience:
- {opportunity}: {why it matters, rough effort}
```
