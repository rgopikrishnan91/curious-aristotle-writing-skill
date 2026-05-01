# Logic Audit

Load this when reviewing claims, during adversarial review, or when editing results/discussion sections.

## Core Principle

A paper is a chain of arguments, not a collection of claims. Every important claim needs: **Evidence + Warrant + Scope + Qualification.**

## Claim Type Classification

Classify before editing. Each type has a different evidence bar.

| Type | Example | What it needs |
|---|---|---|
| Descriptive | "Tool X extracts 25 fields." | Clear measurement |
| Comparative | "X outperforms Y." | Fair baseline comparison |
| Causal | "X improves Y." | Controlled design or causal argument |
| Generalization | "Developers struggle with X." | Representative sample |
| Explanatory | "This happens because of X." | Rival explanations considered |
| Normative | "Researchers should do X." | Values, harms, tradeoffs |
| Theoretical | "This reframes post-training as maintenance." | Conceptual consistency, explanatory power |

## Burden-of-Proof Scale

| Wording | Burden |
|---|---|
| may help | low |
| suggests | moderate |
| improves | controlled evidence |
| solves | very high |
| guarantees | proof or formal condition |
| is necessary | strong exclusion of alternatives |
| is sufficient | strong positive demonstration |

Downshift "prove," "solve," "ensure," "guarantee," "always," "clearly" unless earned.

## Modality Table

| Word | Force |
|---|---|
| may | possible |
| can | possible under some conditions |
| should | normative recommendation |
| must | necessity |
| likely | probabilistic |
| always | universal |
| cannot | impossibility |

## 20 Checks

### Applicable to all paper types

1. **Warrant** — What hidden reasoning connects evidence to conclusion? Is it explicit?
2. **Scope** — Does the claim specify population, dataset, setting? Don't turn local evidence into universal claims.
3. **Causal language** — Flag: improves, reduces, enables, drives, leads to, mitigates, causes. Is the design causal?
4. **Quantifiers** — all, most, many, often, rarely, always, never. Does the study design support them?
5. **Construct validity** — Vague constructs (quality, trustworthiness, robustness, safety) must be defined and operationalized before measuring.
6. **Proxy validity** — A metric is not the thing itself. Pass@1 ≠ coding ability.
7. **Necessary vs sufficient** — Does the paper confuse "needed for X" with "enough for X"?
8. **Definitions and equivocation** — Key terms defined consistently? Flag meaning drift.
9. **Unit of analysis** — Conclusion stays at the same level as evidence. Don't infer developer behavior from repository data.
10. **Counterexamples** — Could all results be true while the conclusion is still false? If yes, narrow.
11. **Alternative explanations** — Never explain a result with only the preferred explanation. Consider and address rivals.
12. **Mechanism** — For strong papers, connect results to *why*: X improves Y *because* it changes intermediate factor M.
13. **Falsifiability** — State what would count against the claim. Good for intros and evaluation design.

### Primarily for empirical/tool papers

14. **Baseline fairness** — Same inputs? Comparable prompts? Reasonable hyperparameters? Failures from design limits or bad setup?
15. **Ablation logic** — Does the ablation isolate one mechanism at a time?
16. **Denominator rule** — Every percentage needs a denominator and inclusion criteria. "91% of what? Over how many cases?"
17. **Variance** — Confidence interval, standard deviation, run-to-run stability? One run is an anecdote.
18. **Direction vs magnitude** — Not enough to say an effect exists. How large? Does it matter practically?
19. **Cherry-picking** — What got worse? What stayed flat? Were all planned metrics reported?
20. **Aggregation risks** — Do averages hide subgroup weaknesses? System-level claims from component-level evidence without integration evidence?

## Formal Logic Patterns for Academic Arguments

**Modus tollens** (powerful for critique):
If a benchmark adequately tests edit preservation, then it should detect unrelated modifications. It does not detect them. Therefore, it does not adequately test edit preservation.

**Reductio** (powerful for theoretical framing):
If pass rate alone were sufficient for deployment readiness, then a model could be considered reliable even when it edits unrelated code. That conclusion is unacceptable. Therefore, pass rate alone is insufficient.

**Dilemma** (shows conclusion holds across cases):
Whether the missing field is absent from the source or present but not extracted, the generated output is still incomplete.

**Contrapositive** (defines evaluation criteria):
If a tool is fully evidence-grounded, every field should be traceable. Therefore, if fields lack traces, the output is not fully evidence-grounded.

## Output Format for Claim Review

```
Main issue: [one sentence]
Claim type: [descriptive / comparative / causal / etc.]
Logical risk: [what could make it invalid or overbroad]
Suggested rewrite: [calibrated version]
Optional stronger claim: [what extra evidence would justify it]
```
