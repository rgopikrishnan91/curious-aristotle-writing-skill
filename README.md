# Academic Writing Skills

Writing skills for formal, evidence-driven SE/ML research papers and technical chapters. Two versions: a full skill with progressive reference loading, and a compact, self-contained single-file version. Both include the complete twelve-failure prose repair protocol.

Built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/codex/), [Gemini](https://gemini.google.com/), and any agent that supports [agentskills.io](https://agentskills.io) SKILL.md format.

## What it covers

- **38 core rules** across sentences, diction, paragraphs, architecture, citations, and tone
- **12 prose failures** with detection patterns, fixes, and meaning-preservation safeguards
- **5 global repair rules**: no em dashes, claim-first paragraphs and sections, prose/table separation, locally grounded empirical claims, and strict terminology with repeated shorthand glosses
- **6-step repair procedure** with a complete hit list, repaired text, and verification reported separately
- Sentence craft from Strunk & White and Joseph Williams' *Style: Toward Clarity and Grace*
- Section architecture for empirical studies, audits, position papers, tool papers, and taxonomies
- Logical rigor: claim types, causal language auditing, scope checking, burden-of-proof calibration
- Context-sensitive wording diagnostics that preserve technical terms and avoid formulaic prose
- Adversarial self-review with six dimensions, applicability checks, and a stop rule
- Revision diagnostics for hidden actions, connected topics, clear referents, and preserved uncertainty

## Two versions

### `academic-writing/` (Full)

38 core rules in SKILL.md with 6 reference files. Load the prose repair protocol for every formal prose edit and before returning new drafts; load other references as needed.

| File | Purpose |
|---|---|
| [SKILL.md](academic-writing/SKILL.md) | Core rules and workflow routing |
| [references/prose-repair.md](academic-writing/references/prose-repair.md) | Five global rules, all twelve failures, six-step audit, separate deliverables |
| [references/pre-writing-checklists.md](academic-writing/references/pre-writing-checklists.md) | Backward reasoning for five paper types |
| [references/adversarial-review.md](academic-writing/references/adversarial-review.md) | Six-dimension self-review and claim-evidence mapping |
| [references/logic-audit.md](academic-writing/references/logic-audit.md) | Inference checks, evidence calibration, and valid reasoning patterns |
| [references/word-replacement-table.md](academic-writing/references/word-replacement-table.md) | Context-sensitive wording and technical-term safeguards |
| [references/revision-guide.md](academic-writing/references/revision-guide.md) | Williams-based prose diagnosis and techniques |

### `academic-writing-lite/` (Compact)

Same 38 core rules and the complete prose repair protocol in a single file. Includes inline wording diagnostics and a claim review protocol. No reference directory or full-version installation needed.

## Installation

To quickly install this skill, run:

```bash
npx skills@latest add rgopikrishnan91/curious-aristotle-writing-skill
```

If you prefer agent-specific instructions, check out below.

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
- "Repair this formal chapter without changing its meaning; report every hit separately from the final text"

Drafting, critique, substantive development, and delivery-only repair have different workflows. The skill does not impose a single chapter template on abstracts, rebuttals, or short paragraphs.

For delivery-only edits, the agent reads the full supplied text before editing, records every hit with its original location and ban number, applies safe rewrites, rereads in context, checks paragraph and section openings, and verifies the repaired text. Missing evidence, undefined referents, and meaning-changing repairs are flagged for the author. Necessary navigation references are reported explicitly rather than hidden behind a claim of zero self-references.

## Sources

Rules draw from:
- Strunk & White, *The Elements of Style*
- Joseph Williams, *Style: Toward Clarity and Grace*
- Prof. Peng Sida's research paper writing notes (structural patterns)
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (vocabulary candidates, retained only where meaning is preserved)
- Empirical SE reviewing and writing practice

## License

MIT
