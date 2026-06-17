# Knowledge Management
*Last updated: 2026-06-17*

The system that makes every future session better: capture what you learn, codify how you work, so both you and the AI start each session informed.

---

## Three Types of Knowledge

**Guidelines** live in `docs/guidelines/`. They answer: "How do we do [technology] in this project?" TypeScript patterns, testing approach, React conventions, security practices. Written once, applied automatically in every session.

**Documentation** lives in `docs/`. It answers: "What did we build and why?" Architecture, APIs, design decisions — the *why* behind the code.

**Knowledge vault** lives in `knowledge/`. It answers: "What have we learned?" Research, architectural decisions, reusable patterns, concept definitions. Structured, searchable, and loaded automatically into engineering sessions when relevant.

---

## Guidelines: How We Do It Here

A guideline is a set of validated practices for a technology in your project. When one exists, engineering commands (`/bob:brainstorm`, `/bob:plan`, `/bob:implement`, `/bob:review`) load relevant guidelines automatically before starting.

### Creating and updating guidelines

Run `/bob:guidelines` to create or refresh guidelines for a technology. The AI scans your project, identifies patterns, and produces a guide covering principles, patterns, anti-patterns, and tooling.

**Output:** `docs/guidelines/{topic}.md`

**When to update:** after discovering a recurring pattern, during quarterly review, or when a code review reveals the guideline is wrong or outdated.

---

## Documentation: What We Built and Why

After shipping a feature, run `/bob:document`. The AI looks at what changed and identifies what needs documenting: architecture updates, new features, changed APIs, unexplained concepts.

**Output:** new or updated files in `docs/`, with updates to the index.

### Structure

```
docs/
├── README.md              # Navigation index
├── product/               # Vision, personas, design briefs
├── guidelines/            # Technology-specific practices
├── process/               # How work happens
├── architecture/          # System design
├── api/                   # API reference
└── features/              # Feature documentation
```

Keep `docs/README.md` as a table of contents. Every document should be linked from the index.

---

## Knowledge Vault: What We've Learned

The `knowledge/` vault stores research, decisions, patterns, and concepts as atomic notes. Unlike documentation (which explains the system), the vault captures *learned knowledge* — insights that inform future work.

Engineering commands automatically retrieve relevant vault notes at session start, so what you've captured surfaces when it matters.

### Quick capture: `/bob:remember`

The fastest way to capture something mid-session without breaking flow:

```
/bob:remember We should avoid X because of Y — discovered in story AUTH-002
```

With no arguments, it asks "What should I remember?" — one question, done. The note lands in `knowledge/_INBOX/` for later processing.

### Managing the vault: `/bob:library`

`/bob:library` is the full vault management command. Run it with no arguments to see vault status.

**Modes:**

| Command | What it does |
|---------|-------------|
| `/bob:library` | Show vault status: inbox count, note counts, pending suggestions |
| `/bob:library process` | Work through inbox items — propose type, tags, filename for each; file on approval |
| `/bob:library retrieve <query>` | Search the vault for notes matching a query |
| `/bob:library organise` | Vault health check: orphaned notes, tag consistency, MOC candidates |
| `/bob:library weekly` | Weekly retrospective digest from daily notes |

### Note types

The vault uses four typed subfolders:

| Type | Folder | Use for |
|------|--------|---------|
| `decision` | `decisions/` | Architectural, design, or process decisions with rationale |
| `concept` | `concepts/` | Terms, technologies, or domain concepts worth defining |
| `research` | `research/` | External findings, benchmarks, tool evaluations |
| `pattern` | `patterns/` | Reusable solutions and anti-patterns |

### The inbox flow

Capture goes to `_INBOX/` (via `/bob:remember` or manually), then gets processed into typed notes via `/bob:library process`. Processing is interactive: the AI proposes type, tags, and filename; you confirm before anything is written.

Raw source materials (articles, papers, specs) go to `sources/` — not as notes, but as originals you might reference.

### Automatic retrieval

You don't need to search the vault yourself. At the start of every engineering session, `bob:brainstorm`, `bob:plan`, `bob:implement`, `bob:review`, and similar commands automatically search the vault for notes relevant to the current story and load up to 5 matches. What you filed last week appears silently in context this week.

### Vault setup

If `knowledge/` doesn't exist, `/bob:library` or `/bob:remember` bootstraps it automatically the first time you run either command.

---

## The Workflow

**Capture as you go:** Hit a useful insight, run `/bob:remember`. No friction.

**Process in batches:** Every few sessions, run `/bob:library process` to file inbox items into typed notes with proper tags.

**Maintain quarterly:** Run `/bob:library organise` to check tag consistency, find orphaned notes, and propose Maps of Content for clusters of related notes.

**Let retrieval work:** Engineering sessions pick up relevant notes automatically. You don't need to remember what you captured — the vault does.

---

## Guidelines vs. Documentation vs. Knowledge Vault

| | Guidelines | Documentation | Knowledge Vault |
|---|-----------|---------------|-----------------|
| **Answers** | How we do [tech] here | What we built and why | What we've learned |
| **Lives in** | `docs/guidelines/` | `docs/` | `knowledge/` |
| **Created by** | `/bob:guidelines` | `/bob:document` | `/bob:remember`, `/bob:library` |
| **Loaded in sessions** | Automatically, by scope | Referenced manually | Automatically, by relevance |
| **Updates** | Quarterly or on drift | After every major change | Continuously |

---

## Tips

**Capture cheap, curate later.** Use `/bob:remember` freely. Process with `/bob:library process` when you have 10 minutes — not in the moment.

**Guidelines are earned.** Don't create one for something you've done once. Wait until you've repeated a pattern 3-4 times and know what actually works.

**Keep the doc index fresh.** `docs/README.md` is the navigation surface. A doc that isn't in the index won't be found.

**Link generously.** Guidelines should reference implementations. Vault notes should link to related stories and decisions. Easy navigation compounds over time.

---

## Next Steps

- After shipping your first feature, run `/bob:document` to capture what you built.
- After discovering a pattern worth keeping, run `/bob:remember` to capture it.
- After building a few features with a repeating pattern, run `/bob:guidelines` to codify it.
- Read [Engineering Workflows](02-engineering-workflows.md) to see how guidelines and vault notes load into sessions.
