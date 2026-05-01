# Academic Writing Skills

Writing skills for SE/ML research papers. Two versions: a full skill with progressive reference loading, and a lightweight single-file version.

Built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/codex/), [Gemini](https://gemini.google.com/), and any agent that supports [agentskills.io](https://agentskills.io) SKILL.md format.

## What it covers

- **38 rules** across sentences, diction, paragraphs, architecture, citations, and tone
- Sentence craft from Strunk & White and Joseph Williams' *Style: Toward Clarity and Grace*
- Section architecture for empirical studies, audits, position papers, tool papers, and taxonomies
- Logical rigor: claim types, causal language auditing, scope checking, burden-of-proof calibration
- AI-writing pattern avoidance: word replacement table, 11 named anti-patterns, terminology sprawl prevention
- Adversarial self-review with 6 rejection dimensions
- Revision diagnostics: nominalization hunting, old-to-new flow, topic threading, stress positions

## Two versions

### `academic-writing/` (Full)

38 rules in SKILL.md with 6 reference files loaded on demand:

| File | Purpose | Lines |
|---|---|---|
| `SKILL.md` | Core rules and workflow | 104 |
| `references/pre-writing-checklists.md` | Backward reasoning for 5 paper types | 39 |
| `references/adversarial-review.md` | 6-dimension self-review, claim-evidence mapping | 57 |
| `references/logic-audit.md` | 20 logic checks, burden-of-proof table, formal patterns | 99 |
| `references/anti-patterns.md` | 11 named writing traps | 25 |
| `references/word-replacement-table.md` | 22-entry AI-tell table + concision patterns | 53 |
| `references/revision-guide.md` | Williams-based prose diagnosis and techniques | 84 |

### `academic-writing-lite/` (Compact)

Same 38 rules in a single file. Includes an inline word table, anti-pattern checklist, and claim review protocol. No reference directory needed.

## Installation

### Claude Code

**Full version (global):**
```bash
mkdir -p "$HOME/.claude/skills"
cp -R academic-writing "$HOME/.claude/skills/"
```

**Full version (project-level):**
```bash
mkdir -p .claude/skills
cp -R academic-writing .claude/skills/
```

**Lite version:**
```bash
mkdir -p "$HOME/.claude/skills"
cp -R academic-writing-lite "$HOME/.claude/skills/"
```

### Codex

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R academic-writing "$CODEX_HOME/skills/"
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R academic-writing "$HOME/.gemini/skills/"
```

## Usage

Ask your agent to use the skill explicitly, or it will trigger automatically on writing-related requests:

- "Revise this introduction"
- "Make this paragraph flow better"
- "Review my abstract for logical issues"
- "Tighten this results section"
- "Edit this draft using the academic-writing skill"

## Sources

Rules draw from:
- Strunk & White, *The Elements of Style*
- Joseph Williams, *Style: Toward Clarity and Grace*
- Prof. Peng Sida's research paper writing notes (structural patterns)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (AI-tell vocabulary tiers)
- Empirical SE reviewing and writing practice

## License

MIT
