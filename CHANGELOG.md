# Changelog

## 2026-09-24

### Added

- A complete formal prose-repair protocol in both skill versions: five global rules, twelve named prose failures with fixes, and a six-step audit.
- Separate hit-list, repaired-text, and verification outputs, with original locations, rule numbers, proposed rewrites, and author-review flags.
- Explicit checks for claim-first paragraphs and sections, local empirical evidence, table interpretation, terminology, repeated shorthand glosses, em dashes, and document self-references.
- This changelog and README guidance on version selection, workflows, installation, and updating an existing copy.
- Separate `dist/academic-writing.zip` and `dist/academic-writing-lite.zip` upload packages, each containing exactly one `SKILL.md` and the MIT license. The full package includes all six reference files.
- A reproducible packaging script with a `--check` option to detect missing or stale ZIPs.

### Fixed

- ZIP upload instructions now link to individual skill packages. GitHub's repository-wide archive contains two `SKILL.md` files and cannot be uploaded as a single skill.

### Changed

- Made active voice the default, with narrow exceptions that preserve meaning and avoid inventing actors.
- Rejected vague reframing such as "this is structural" and unsupported praise such as "robust." Retained established technical names and precisely defined claims supported by evidence.
- Required empirical findings to carry their evidence at each occurrence and limited document cross-references to genuine navigation.
- Separated delivery-only repair from drafting, critique, and substantive argument development. Missing evidence and meaning-changing repairs require author decisions.
- Replaced automatic synonym substitutions with context-sensitive wording checks. Preserved technical meaning, negation, agency, modality, uncertainty, and emphasis.
- Revised logic and evidence guidance: hedging does not remove the need for support, measured comparisons do not automatically establish mechanisms, and claim strength depends on the design and scope.
- Made review criteria depend on the contribution and study design, including replications, negative results, audits, taxonomies, and incremental improvements.
- Clarified that sentence rhythm, tense, nominalizations, examples, and sentence endings are techniques to apply when useful.
- Kept the complete repair protocol identical across the full and compact versions.
- Added a fallback for an unset `CODEX_HOME` in the README's manual copy commands.

### Removed

- The duplicate `academic-writing/references/anti-patterns.md` reference and overlapping compact checklist; useful guidance now lives in the core rules and repair protocol.
- Unsupported claims that uniform sentence or paragraph lengths identify AI authorship.
- Blanket restrictions on explaining incremental contributions as a baseline plus a change.
- The simplistic wording-to-evidence ladder and instructions to review indefinitely until no hypothetical rejection risk remains.

The skill revision is recorded in [c93b6a1](https://github.com/rgopikrishnan91/curious-aristotle-writing-skill/commit/c93b6a101fc479244e9c6da4c61de26bb90d8849). The changelog and expanded README follow in the documentation update.
