---
name: academic-writing-lite
description: "Concise academic writing rules for SE/ML papers. Use when drafting, revising, or editing any paper section, abstract, rebuttal, or pasted prose the user wants tightened or clarified. Trigger on 'revise,' 'rewrite,' 'polish,' 'tighten,' 'clarify,' 'too wordy,' 'make this flow,' or 'fix this.'"
---

# Academic Writing — Compact Rules

## Sentences

1. **Active voice.** Passive only when (a) actor unknown, (b) irrelevant, or (c) it maintains old-to-new flow.
2. **Cut ruthlessly.** Drop empty hedges ("it is important to note that"). Preserve hedges that calibrate claim strength ("may," "suggests"). Conciseness means fewer wasted words, not less substance; cut filler, never cut clarity.
3. **Positive form.** "He forgot" not "He did not remember."
4. **End on the emphatic word.** New technical terms go at the end, preceded by context.
5. **Related words together.** Don't interrupt subject-verb with long modifiers.
6. **Parallel construction** in lists and compound structures.
7. **No run-ons.** Break up shapeless sentences.
8. **Single tense** per passage unless time reference changes.
9. **No em dashes.** Commas, semicolons, colons, or restructure.
10. **Vary rhythm.** Mix short and long sentences. Uniform length = AI tell.
11. **Kill nominalizations.** "The implementation was performed" → "We implemented." Find actions hiding in nouns; make the actor the subject.
12. **Old before new.** Begin sentences with familiar info; end with new/complex info.
13. **Thread topics.** Subjects of consecutive sentences should connect. If first words scatter, restructure.

## Diction

14. **Plain words; no LLM constructions.** "Use" not "utilize." "Is" not "serves as." Avoid dramatic reframing: "This is not a technical problem; it is a structural one." State the point directly.
15. **Define terminology on first use.** Don't assume the reader shares your shorthand.
16. **Prevent terminology sprawl.** Pick one term per concept; lock it in for the entire paper. Readers assume two terms mean two things. If they genuinely do, define the distinction explicitly.
17. **Specific numbers.** "19%" not "a substantial share."
18. **No significance inflation.** "A paradigm shift" for a 2% gain → just state the number.

## Paragraphs

19. **First sentence = key claim (usually).** For motivation paragraphs building to a gap, the claim can come last. Either way, one sentence carries the point.
20. **Bold strategically.** Bold the finding in results, the limitation in limitations. Not always the first sentence.
21. **Results: numbers first, surprisal first.** Lead with comparisons or x-out-of-y. Follow RQs with a one-line answer preview.
22. **Vary paragraph length.** Uniformity reads as generated.
23. **Open with the domain.** First sentence = problem, not "We propose."

## Architecture

24. **Motivation → approach → results** within each analysis.
25. **Motivate every method decision.** Non-trivial ones need citations or rationale.
26. **Visible logical structure.** Each step connects to the next.
27. **State once, cross-reference.** No repeated arguments across sections.
28. **No TOC sentences** in short/conference papers. OK in journals.
29. **No incremental-patch framing.** Don't present naive baseline then your delta.
30. **Ground gap claims.** Don't assert "underexplored" without evidence.
31. **Use examples as a clarity device.** When a concept or process resists compact explanation, walk the reader through a concrete example. For complex workflows, use a single non-trivial running example across steps so the reader tracks the full transformation.

## Evidence and Logic

32. **Every claim grounded on first mention.**
33. **Citations explain the connection.** "Strobl et al. find X" not just "[59]."
34. **Verify citations.** Search, read, confirm. Never hallucinate.
35. **Match claim to design.** Flag "improves" when design is observational. "May" → low burden; "improves" → controlled evidence; "guarantees" → proof.
36. **Scope every claim.** Specify population, dataset, setting.

## Tone

37. **Authority + honesty.** No defensive framing. Report what got worse alongside what improved.
38. **Don't over-polish.** Rough edges are human. Fragments, "But" openers, deliberate repetition — all fine.

---

## Quick Word Replacement Table

| Replace | With |
|---|---|
| leverage / utilize | use |
| delve / delve into | examine, explore |
| robust | strong, reliable |
| comprehensive | thorough, complete |
| seamless | smooth |
| cutting-edge | latest |
| pivotal | important, key |
| facilitate | enable, allow |
| multifaceted | (name the facets) |
| holistic | complete, full |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| novel (own work) | new |
| landscape (metaphor) | field, area |

## Anti-Patterns (Quick Check)

- Copula avoidance ("serves as" when you mean "is")
- Synonym cycling / terminology sprawl ("developers… engineers… practitioners…")
- Vague attribution ("Experts believe" — name them or drop it)
- Template openings ("In the rapidly evolving world of…")
- Dramatic reframing ("This is not X; it is Y" — just state Y)
- False concession ("While X is impressive, Y remains…" — both halves vague)
- Chatbot prose ("In this section, we will explore…")

## Claim Review (When Editing Results/Discussion)

For each major claim, ask:
1. **Type?** Descriptive, comparative, causal, generalization?
2. **Evidence fit?** Does the method support this inference type?
3. **Scope?** Population, dataset, conditions specified?
4. **Causal language earned?** "Improves" needs controlled evidence.
5. **Terminology defined?** Vague constructs operationalized?
6. **Alternatives?** Rival explanations considered?
7. **What would make this false?** Even if results are true?
