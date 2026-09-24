# Logic Audit

Use this audit to assess whether evidence supports the inference actually made. During delivery-only repair, record substantive problems for the author; do not weaken, strengthen, or extend a claim. Apply changes to the argument only when the user requests substantive revision.

## Identify the Inference

| Claim type | Check |
|---|---|
| Descriptive | Does the measurement establish the stated property under the stated conditions? |
| Comparative | Are the comparator, metric, inputs, and conditions fair and explicit? |
| Causal | Does the design identify the claimed effect, and are its assumptions defensible? |
| Generalization | Does sampling or another argument support extension beyond observed cases? |
| Explanatory | Is the proposed mechanism supported, and are plausible alternatives considered? |
| Normative | Are the values, tradeoffs, and factual premises explicit? |
| Theoretical | Are definitions and premises clear, and does the conclusion follow? |

Distinguish "A scored higher than B in the evaluated setting" from "the proposed mechanism caused the gain." A comparative measurement does not by itself establish a mechanism. Evaluate causal identification and its assumptions; observational evidence is not automatically incapable of supporting a causal inference.

## Calibrate Wording Without Using a Fixed Ladder

| Wording | Required check |
|---|---|
| may help | Is there support for this possibility, or is it clearly identified as an untested hypothesis? |
| suggests | What inference is suggested, with what uncertainty and plausible alternatives? |
| improves | Is this a measured comparison or a causal claim, and does the evidence support that reading? |
| solves | Which stated task and success criterion are satisfied, under which conditions? |
| guarantees | Is there a proof or enforceable condition covering the stated scope? |
| is necessary | Have alternatives been excluded within the stated scope? |
| is sufficient | Does the condition establish the outcome within the stated scope? |

Do not equate cautious wording with low evidential burden. Adding "may" cannot repair an unsupported inference. Preserve distinctions between possibility, ability, recommendation, necessity, probability, and universality. During repair, flag a mismatch instead of silently changing modality.

## Checks

1. **Warrant:** Identify the reasoning connecting evidence to conclusion. Make hidden assumptions explicit when supplied; flag missing ones.
2. **Scope and unit:** Check population, dataset, conditions, quantifiers, and unit of analysis. Repository observations alone do not establish individual developer behavior.
3. **Constructs and proxies:** Define measured concepts and distinguish a metric from the broader property it represents. Do not treat test passage alone as complete coding ability.
4. **Causal identification:** Examine confounding, assignment, temporal order, and identification assumptions. Do not infer a mechanism solely from correlation or a higher score.
5. **Comparison and ablation:** Check comparable inputs, budgets, implementation quality, and evaluation criteria. Ask whether an ablation isolates the factor claimed.
6. **Numbers and uncertainty:** Check denominators, inclusion criteria, units, effect magnitude, and appropriate uncertainty. Repeated runs matter for stochastic outcomes; do not demand them automatically for deterministic counts or proofs.
7. **Aggregation:** Check whether averages hide subgroup differences and whether component-level evidence supports a system-level conclusion.
8. **Alternatives:** Assess plausible rival explanations relevant to the conclusion. Do not add speculative mechanisms just to fill a checklist.
9. **Necessity and sufficiency:** Distinguish "needed for the outcome" from "enough to establish the outcome." State the conditions that limit either claim.
10. **Counterexamples:** Ask whether the reported results could be true while the conclusion is false. Flag the missing premise or overreach.
11. **Reporting and selection:** Check whether the selected results, comparisons, failures, and limitations support the stated scope. Flag cherry-picking without inventing omitted results.
12. **Applicability:** Apply checks appropriate to the claim and study design. A taxonomy, replication, qualitative study, audit, or proof need not satisfy a new-method benchmark template.

## Reasoning Patterns

Use these patterns to diagnose reasoning, not to manufacture new premises during prose repair.

- **Modus tollens:** If P implies Q, and Q is false, then P is false. Both the implication and the observation need support.
- **Counterexample to sufficiency:** A case where P holds but Q does not refutes the claim that P alone guarantees Q. An undesirable outcome is not itself a logical contradiction.
- **Contrapositive:** If P implies Q, then absence of Q implies absence of P. Do not confuse this with claiming that Q implies P.
- **Case analysis:** Show that each case in an exhaustive set supports the conclusion. Check that the cases are actually exhaustive and use the same outcome criterion.

## Claim Review Output

For each substantive issue, state the original claim, inference type, supporting evidence, logical risk, and missing condition or evidence. Suggest a calibrated alternative only as an author decision when meaning would change. Do not insert a stronger or weaker claim into a delivery-only edit.
