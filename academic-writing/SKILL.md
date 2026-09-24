---
name: academic-writing
description: "Improve formal, evidence-driven academic writing for SE/ML research, including technical chapters and papers. Use when drafting, revising, editing, or reviewing any paper section: abstract, introduction, related work, method, experiments, discussion, conclusion, threats, limitations, or rebuttal. Also trigger when the user pastes prose and asks to tighten, clarify, polish, fix flow, or 'make this better.' Covers sentence craft, paragraph structure, section architecture, citation practice, logical rigor, tone, and a twelve-failure prose repair audit that preserves meaning. Works across empirical studies, audits, position papers, tool papers, and taxonomy papers."
---

# Academic Paper Writing

## Workflow

Choose the operation before editing. For revision, polishing, tightening, or delivery-only repair of supplied formal prose, first read `references/prose-repair.md` in full and follow its complete procedure: read without editing, list every hit, apply safe rewrites, smooth seams, verify first sentences, and run final checks. Return the hit list separately from the final text. Preserve the argument, evidence, claims, numbers, citations, uncertainty, and emphasis exactly; flag meaning-changing repairs for the author.

Use the broader workflow below for drafting or explicitly requested substantive development. During delivery-only repair, use its diagnostics to identify issues, but do not add experiments, reframe claims, supply new arguments, or alter emphasis. Record substantive suggestions separately.

1. **Pre-write:** Answer backward reasoning questions for this paper type (`references/pre-writing-checklists.md`). Outline the claims and evidence needed for each section.
2. **Draft:** Write one paragraph at a time; its first sentence states its core claim. Open each section with its core claim.
3. **Reverse outline:** Extract first sentences. Check that they reconstruct the full argument.
4. **Review:** Build a claim-evidence map; use adversarial self-review (`references/adversarial-review.md`) and the logic audit (`references/logic-audit.md`).
5. **Revise:** Run the complete twelve-failure audit (`references/prose-repair.md`). Use the wording diagnostics (`references/word-replacement-table.md`) and prose diagnosis (`references/revision-guide.md`) as needed.

For critique-only requests, report issues and recommendations without rewriting the supplied text. Match the output to the task; do not force a chapter structure onto an abstract, rebuttal, or short paragraph.

Load references needed for the current step. The prose repair protocol is required for every formal prose edit; its five global rules, twelve numbered bans, and six-step audit are not optional quick checks. For new drafting, also load the protocol and apply its global rules and twelve bans before returning the text.

---

## A. Sentences

**1. Prefer active voice.** Make active voice the default. Put the known actor before a direct verb: "We evaluated the patches" or "The evaluator rejects invalid patches." Use passive voice only when the actor is unknown or irrelevant, or when active voice would distort the intended focus. Never invent an actor; do not use a generic preference for flow to leave avoidable passive constructions unchanged.

**2. Cut ruthlessly.** Omit needless words and empty hedges ("it is important to note that"). But preserve hedges that calibrate claim strength: "may," "suggests," and "indicates" carry epistemic weight in academic writing. Conciseness means fewer wasted words, not less substance; cut filler, never cut clarity.

**3. Use positive form when it preserves the claim.** Prefer a direct affirmative statement where equivalent, but preserve meaningful negation. "No evidence of benefit" is not equivalent to "evidence of no benefit."

**4. Use sentence endings for new information.** Put new or complex information near the end when it improves comprehension. Treat this as a flow heuristic, not a requirement to intensify every sentence or delay necessary definitions.

**5. Keep related words together.** Subject near verb, modifier near target. Don't interrupt subject-verb with long modifiers; move them to the start or end.

**6. Parallel construction** in all lists and compound structures.

**7. No run-on sentences.** Break them up. For controlled long sentences, see `references/revision-guide.md`.

**8. Use tense deliberately.** Use past tense for completed procedures and observations, present tense for definitions and current interpretations, and future tense for planned work. Change tense when the meaning requires it; do not force a whole passage into one tense.

**9. No em dashes anywhere.** Use colons, commas, semicolons, parentheses, or restructure.

**10. Vary sentence rhythm.** Mix short and longer sentences where the argument supports it. Do not manufacture slogans or fragments for variety. Allow short parallel sentences when the symmetry itself carries information.

**11. Unpack nominalizations that hide actions.** Prefer "the team implemented the method" to "implementation was performed by the team." Preserve established technical nouns, named constructs, and useful references to earlier actions. Do not add an actor or alter agency merely to use a verb.

**12. Connect familiar information to new information.** Usually begin with an established topic and then develop it. Keep the claim-first rule and necessary definitions; do not force every sentence into the same information order.

**13. Thread topics.** The subjects of consecutive sentences in a paragraph should form a connected sequence. If they scatter across unrelated referents, restructure.

## B. Diction

**14. Use concrete wording; reject abstract reframing.** Do not write "this is structural," "this is a structural problem," or "this is not a technical problem; it is a structural one" as a substitute for explanation. Name the component, dependency, constraint, or failure, and state what happens. Keep a precise technical use of "structural" only when its referent is explicit and necessary. Reject unsupported "robust," "comprehensive," "seamless," and similar praise; state the measured property or flag missing evidence. Preserve established technical names such as "robust regression." Cut staged pivots, vague concessions, and stock openings without changing the claim. Do not infer AI authorship from surface style.

**15. Define and gloss terminology.** Define every specialized term at first use. Every ID or shorthand outside its definition must carry a 2-6 word gloss at each occurrence. Resolve definitions from the source; flag missing ones rather than inventing them.

**16. Prevent terminology sprawl.** Pick one term for each concept and lock it in for the entire paper. Do not drift between near-synonyms across sections; readers will assume two terms mean two things. If they refer to different concepts, define the distinction explicitly on first use.

**17. Use warranted numerical precision.** Report the relevant number, denominator, units, and conditions when supported. Do not invent a number, add decimal precision, or recompute a result during delivery-only repair. Flag quantitative evidence that the strict repair protocol requires but the source does not supply.

**18. No significance inflation or bare importance assertions.** Delete self-ranking praise and state the supported consequence. Retain a superlative only when it is a checkable, supported factual claim. Do not replace "crucial" with "important"; state the fact that establishes the consequence.

## C. Paragraphs

**19. First sentence = the core claim of every paragraph.** A reader skimming only first sentences must recover the full argument. This includes motivation paragraphs; do not defer their claim to the end. Never open with connectors masquerading as claims. Flag cases where reordering would change meaning or emphasis.

**20. Preserve emphasis during repair.** Do not add bolding or intensify a finding while editing delivery. When drafting, use bold strategically for findings and limitations if the target format permits it.

**21. Results: lead with the finding.** Use a comparison, x-out-of-y summary, or trend with its number and citation. When drafting research questions, follow each with a one-line answer preview. During repair, preserve the original selection and emphasis of findings.

**22. Let paragraph length follow the argument.** Vary length when the content warrants it; keep one core claim per paragraph.

**23. Open with the substantive claim.** For introductions, establish the phenomenon, problem, or contribution. In other sections, lead with the claim that serves that section. Avoid generic scene-setting and document narration; do not force every section to reopen the domain problem.

## D. Section and Argument Architecture

**24. Open every section with its core claim.** The first paragraph must state that claim, starting with it. Then connect motivation, approach, and results within each analysis.

**25. Justify consequential methodological decisions.** Explain decisions that affect interpretation, validity, reproducibility, or comparison. Do not pad prose with justifications for every routine implementation detail. During repair, flag missing rationale rather than inventing it.

**26. Visible logical structure.** Whether deductive, inductive, or eliminative, each step connects to the next.

**27. Avoid duplicated arguments, not local evidence.** Give each argument a clear home, but restate every empirical finding with its number and citation wherever it is used. Never replace evidence with "as noted above," a section pointer, an experiment nickname, or "the 83 percent."

**28. Remove document self-reference.** Make the phenomenon, not the chapter, section, or table, the subject. Keep a cross-reference only when navigation is genuinely the point; list retained navigation references during verification. Paper length is not an exemption.

**29. Describe the actual contribution at its supported scale.** A baseline-plus-change explanation is valid when it makes the mechanism or comparison clear. Do not dismiss incremental work or manufacture a larger gap. Preserve contributions from replications, negative results, datasets, audits, and measured improvements.

**30. Ground gap claims in evidence.** Do not write "X remains underexplored" without support. During repair, flag missing support for the author instead of inventing evidence, reframing the claim, or silently weakening it.

**31. Use examples when they resolve a concrete ambiguity.** Choose the simplest example that preserves the relevant difficulty. Use a running example when it helps readers track a process. During delivery-only repair, clarify existing examples without adding facts, comparisons, or new illustrations.

## E. Citations and Evidence

**32. Ground every empirical claim at every occurrence.** State the finding with its number and citation locally, preserving the scope and conditions needed to interpret it. Flag missing evidence. Prose interprets and tables enumerate: do not repeat table contents as a prose inventory; include only numbers needed to support the interpretation.

**33. Make the evidence-to-claim connection explicit.** State the relevant finding and why it supports the inference. Use author names only when attribution or comparison needs them; do not turn related work into a sequence of names. A citation alone does not establish the reasoning.

**34. Verify every citation.** Read the cited source and confirm the claim actually made; search when needed for verification. Flag uncertainty or inaccessible sources. During repair, recover existing citations from supplied material, but flag any need for new evidence or citation changes rather than silently adding them. Never fabricate a citation.

**35. Match the inference to the evidence.** Distinguish a measured comparison from a causal explanation. Evaluate the design, confounding, identification assumptions, and scope instead of banning individual verbs. Hedging with "may" does not remove the need for evidence. Flag unsupported causal or universal claims during repair; do not silently recalibrate them.

**36. Keep scope local to the claim.** Preserve the population, dataset, setting, inclusion criteria, and uncertainty that bound the inference. If necessary scope is absent, flag it rather than guessing.

## F. Tone and Voice

**37. State epistemic status plainly.** Preserve limitations and mixed results without defensive framing or certifications such as "honestly," "frankly," or "we are transparent about." When drafting, report what got worse alongside what improved; during repair, flag missing evidence rather than adding it.

**38. Keep a natural, serious register.** Use direct, connected prose. Do not add internet vocabulary, snark, slogans, stock witticisms, abstract binaries, stacked metaphors, or extra emphasis to make the prose sound human.
