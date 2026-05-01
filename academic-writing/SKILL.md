---
name: academic-writing
description: "Improve academic paper writing for SE/ML research. Use when drafting, revising, editing, or reviewing any paper section: abstract, introduction, related work, method, experiments, discussion, conclusion, threats, limitations, or rebuttal. Also trigger when the user pastes prose and asks to tighten, clarify, polish, fix flow, or 'make this better.' Covers sentence craft, paragraph structure, section architecture, citation practice, logical rigor, and tone. Works across empirical studies, audits, position papers, tool papers, and taxonomy papers."
---

# Academic Paper Writing

## Workflow

1. **Pre-write** — answer backward reasoning questions for this paper type (`references/pre-writing-checklists.md`). Outline 3-7 bullets per section.
2. **Draft** — one paragraph at a time, first sentence carries the claim.
3. **Reverse outline** — extract first sentences; if they don't tell a coherent story, restructure.
4. **Review** — claim-evidence map, adversarial self-review (`references/adversarial-review.md`), logic audit (`references/logic-audit.md`).
5. **Revise** — anti-patterns (`references/anti-patterns.md`), word table (`references/word-replacement-table.md`), prose diagnosis (`references/revision-guide.md`).

Load only the reference file needed for the current step.

---

## A. Sentences

**1. Active voice.** "We evaluate," "Coverage measures." Passive only when (a) the actor is unknown, (b) irrelevant, or (c) it puts familiar information in the subject and new information at the end for better flow.

**2. Cut ruthlessly.** Omit needless words and empty hedges ("it is important to note that"). But preserve hedges that calibrate claim strength: "may," "suggests," and "indicates" carry epistemic weight in academic writing. Conciseness means fewer wasted words, not less substance; cut filler, never cut clarity.

**3. Positive form.** State what something *is*, not what it *isn't*, unless the negation is the point.

**4. End on the emphatic word.** The stress position is the end of the sentence. Introduce new technical terms there, preceded by context.

**5. Keep related words together.** Subject near verb, modifier near target. Don't interrupt subject-verb with long modifiers; move them to the start or end.

**6. Parallel construction** in all lists and compound structures.

**7. No run-on sentences.** Break them up. For controlled long sentences, see `references/revision-guide.md`.

**8. Hold a single tense** per passage unless the time reference actually changes.

**9. No em dashes.** Use commas, semicolons, colons, or restructure.

**10. Vary sentence rhythm.** Mix short sentences (3-8 words) with longer ones. Monotone length is the strongest structural signal of AI-generated text.

**11. Kill nominalizations.** Find actions hiding in nouns; turn them into verbs with character-subjects. "The implementation of the framework was performed" → "The team implemented the framework." Watch for empty verbs (*is, make, conduct, perform*) paired with noun-ified actions.

**12. Old before new.** Begin each sentence with familiar information; end with new or complex information. Choppy paragraphs usually start sentences with new concepts instead of connecting to what came before.

**13. Thread topics.** The subjects of consecutive sentences in a paragraph should form a connected sequence. If they scatter across unrelated referents, restructure.

## B. Diction

**14. Plain words; no LLM-sounding constructions.** "Use" not "utilize." "Is" not "serves as." Avoid dramatic reframing patterns: "This is not a technical problem; it is a structural one" or "It's not about X, it's about Y." State the point directly. See `references/word-replacement-table.md`.

**15. Define terminology on first use.** When introducing a term, concept, or abbreviation, define it clearly the first time it appears. Do not assume the reader shares your shorthand.

**16. Prevent terminology sprawl.** Pick one term for each concept and lock it in for the entire paper. Do not drift between near-synonyms across sections; readers will assume two terms mean two things. If they genuinely do mean different things, define the distinction explicitly on first use.

**17. Specific numbers over vague language.** "19%" not "a substantial share."

**18. No significance inflation.** Do not dress routine results in grand language. State what happened; let the reader judge.

## C. Paragraphs

**19. First sentence = the key claim (usually).** A reader skimming first sentences should reconstruct the argument. In motivation paragraphs building toward a gap, the claim may come last. Either way, one sentence carries the paragraph's point. Never open with connectors masquerading as claims.

**20. Bold strategically.** In results, bold the key finding. In limitations, bold the limitation. The bolded phrase need not be the first sentence; place it where it carries the most signal for a scanning reader.

**21. Results: numbers first, surprisal first.** Open with comparisons, x-out-of-y summaries, or trends. Surface the surprising finding, not the expected one. When presenting RQs, immediately follow each with a one-line answer preview.

**22. Vary paragraph length.** Uniform paragraph length reads as generated.

**23. Open with the domain, not the authors.** First sentence establishes the problem or technology. "We propose" belongs in the contributions paragraph.

## D. Section and Argument Architecture

**24. Motivation → approach → results** within each analysis, implicitly or explicitly.

**25. Motivate every methodological decision.** Trivial ones get a brief justification. Non-trivial ones need a citation or rationale.

**26. Visible logical structure.** Whether deductive, inductive, or eliminative, each step connects to the next.

**27. State each argument once, in the right place.** Cross-reference; never repeat across sections.

**28. No table-of-contents sentences in conference/short papers.** In journal papers (20+ pages), a brief organization paragraph at the end of the introduction is acceptable.

**29. No incremental-patch framing.** Never present a naive baseline then describe your delta. Frame the contribution as addressing a genuine gap.

**30. Ground gap claims in evidence.** Don't write "X remains underexplored" without support. Cite evidence when findable; otherwise state the observation directly.

**31. Use examples as a clarity device.** Be concise, but not at the cost of clarity. When an abstract concept or multi-step process resists compact explanation, walk the reader through a concrete example. For complex workflows, use a single non-trivial running example that reappears at each step, so the reader tracks the full transformation rather than rebuilding context from scratch. Toy examples that skip the hard parts teach nothing; pick one that exercises the real complexity.

## E. Citations and Evidence

**32. Every empirical claim needs grounding on first mention.**

**33. When citing, explain the connection.** Why does that finding support this choice? A bare citation is not a justification.

**34. Verify every citation.** Search, read, confirm the claim actually made. Flag uncertainty rather than fabricate. Never hallucinate a citation.

**35. Match claim strength to study design.** Flag causal verbs ("improves," "reduces," "enables") when the design is observational. Burden scale: "may" → low; "improves" → controlled evidence; "guarantees" → proof.

**36. Scope every major claim.** Specify population, dataset, or setting. "For public AI assets with discoverable GitHub links" not just "multi-source evidence improves generation."

## F. Tone and Voice

**37. Write with authority; be honest about limitations.** No defensive framing. Present limitations with bolded leads. Report what got worse alongside what improved. Digress only when it adds clear value.

**38. Do not over-polish.** Natural writing has rough edges: sentences starting with "But," deliberate fragments, repetition for emphasis. The goal is a confident human practitioner, not a compliance engine.
