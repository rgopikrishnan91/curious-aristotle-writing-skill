# Academic Writing Skills

Formal, evidence-driven writing for software engineering and machine learning papers, technical chapters, abstracts, and rebuttals. Both versions prefer active voice, concrete explanations, concise prose, and claims supported by evidence.

Use with [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/codex/), [Gemini](https://gemini.google.com/), or another agent that supports the [Agent Skills format](https://agentskills.io).

See the [changelog](CHANGELOG.md) for the September 2026 prose-repair update and writing-guidance audit.

## Writing preferences

- **Prefer active voice.** Name the known actor and use a direct verb. Keep passive voice only when needed; never invent an actor.
- **Explain concretely.** Replace vague labels such as "this is structural" with the actual component, constraint, failure, or consequence.
- **Avoid unsupported praise.** Replace general claims such as "robust" with the supported property or result. Preserve exact technical names such as "robust regression."
- **Use no em dashes.** Restructure or use commas, colons, semicolons, or parentheses.
- **Lead with the claim.** Every paragraph starts with its core claim, and every section opens with its core claim.
- **Let prose interpret and tables enumerate.** Include the numbers needed for an interpretation without retelling a table.
- **Ground empirical findings locally.** Restate the finding with its number and citation wherever used. Flag missing evidence rather than inventing it.
- **Keep terminology consistent.** Define specialized terms at first use and add a 2-6 word gloss to every ID or shorthand used outside its definition.

During delivery-only repair, preserve meaning, argument, evidence, numbers, citations, scope, uncertainty, and emphasis. Flag changes that require an author decision. Do not force a chapter template onto a short paragraph or rebuttal.

## Choose a version

| Version | Contents | Best fit |
|---|---|---|
| [Full: academic-writing](academic-writing/SKILL.md) | 38 core rules, the complete repair protocol, and six references loaded when needed | Paper development, detailed review, and long documents |
| [Compact: academic-writing-lite](academic-writing-lite/SKILL.md) | The same 38 core rules and complete repair protocol, plus concise wording and claim checks in one file | A self-contained installation with fewer supporting diagnostics |

The compact version includes all twelve prose failures, all five global rules, and the full six-step repair procedure. It does not depend on the full version or a reference directory.

### Full-version resources

| File | Purpose |
|---|---|
| [prose-repair.md](academic-writing/references/prose-repair.md) | Five global rules, twelve failures and fixes, six-step audit, separate deliverables |
| [pre-writing-checklists.md](academic-writing/references/pre-writing-checklists.md) | Questions for five types of research contribution |
| [adversarial-review.md](academic-writing/references/adversarial-review.md) | Six review dimensions with applicability checks and a stop rule |
| [logic-audit.md](academic-writing/references/logic-audit.md) | Inference, evidence, scope, uncertainty, and reasoning checks |
| [word-replacement-table.md](academic-writing/references/word-replacement-table.md) | Context-sensitive wording diagnostics that preserve technical meaning |
| [revision-guide.md](academic-writing/references/revision-guide.md) | Active voice, hidden actions, information flow, and paragraph repair |

## Workflows and output

| Request | Expected behavior |
|---|---|
| Draft new prose | Develop the claims and evidence, use claim-first paragraphs, and check the global rules and twelve failures |
| Polish or repair existing prose | Read the full supplied text before editing; return a hit list, complete repaired text, and verification separately |
| Critique only | Report issues and recommendations without rewriting |
| Develop the argument | Make substantive changes when requested and distinguish them from delivery-only repairs |

For repair, the agent records each hit with its original location, ban number or global rule, proposed rewrite, and status. It then applies safe edits, rereads them in context, checks the first-sentence skim, and verifies evidence, terminology, punctuation, and self-references. It reports unresolved author decisions, unverified checks, and any retained navigation references.

Example requests:

- "Use academic-writing to repair this introduction without changing its claims."
- "Use academic-writing-lite to tighten this paragraph; return only the revised text."
- "Review this discussion for unsupported causal claims. Do not rewrite it."

An explicit output request can shorten the report; it does not skip the repair audit.

## Installation

Use the installer:

```bash
npx skills@latest add rgopikrishnan91/curious-aristotle-writing-skill
```

For a manual installation, first clone the repository and enter its directory:

```bash
git clone https://github.com/rgopikrishnan91/curious-aristotle-writing-skill.git
cd curious-aristotle-writing-skill
```

The commands below install the full version. Substitute `academic-writing-lite` for `academic-writing` to install the compact version.

### Claude Code

Install globally:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R academic-writing "$HOME/.claude/skills/"
```

For a project installation, copy the selected skill folder into that project's `.claude/skills/` directory.

### Codex

Use `CODEX_HOME` when set, with `$HOME/.codex` as the fallback:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R academic-writing "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Gemini

```bash
mkdir -p "$HOME/.gemini/skills"
cp -R academic-writing "$HOME/.gemini/skills/"
```

## Updating an existing installation

For a manual installation, run the following inside your repository clone:

```bash
git pull --ff-only
```

Then replace the installed skill folder with the corresponding updated folder from the clone, preserving any local customizations you need. Pulling the repository alone does not update a separately copied installation. The full version no longer uses `references/anti-patterns.md`; replacing the folder also removes that obsolete file.

## Sources

The guidance draws from:

- Strunk & White, *The Elements of Style*
- Joseph Williams, *Style: Toward Clarity and Grace*
- Prof. Peng Sida's research paper writing notes
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing), with vocabulary suggestions limited to changes that preserve meaning
- Empirical software engineering reviewing and writing practice

## License

[MIT](LICENSE)
