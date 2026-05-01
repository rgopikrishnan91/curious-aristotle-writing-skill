# Adversarial Self-Review

Read the paper as a skeptical reviewer. Answer each question with explicit evidence from the paper. Mark each: `pass` / `needs revision` / `needs new experiment`.

## Six Rejection Dimensions

### 1. Contribution
- What new knowledge does this paper give readers?
- Is the problem meaningful, not trivial?
- Is the technical idea non-obvious beyond well-explored practice?
- Is there at least one clear novelty type (new task, finding, method, insight)?

### 2. Writing Clarity
- Can a knowledgeable reader reproduce the method?
- Is every module/decision motivated?
- Is terminology consistent across sections?
- Does each paragraph carry one clear message?

### 3. Experimental Strength
- Are improvements over strong baselines meaningful, not just statistically tiny?
- Is absolute performance competitive for the target venue?
- Are gains consistent across settings/metrics?
- Are both strengths and failure cases reported?

### 4. Evaluation Completeness
- Ablations for all key design claims?
- Strong/recent baselines under fair settings?
- Standard metrics sufficient for this task?
- Challenging datasets/scenarios?

### 5. Method Design Soundness
- Is the setting realistic for practical use?
- Hidden technical defects or unreasonable assumptions?
- Robust without heavy per-case hyperparameter tuning?
- Do benefits outweigh added complexity?

### 6. Reproducibility
- Replication package available?
- Sufficient detail for independent replication?
- Data availability documented?

## Claim-Evidence Mapping

For every major claim (especially abstract and introduction), produce:

```
Claim: [the claim]
Evidence: [where in the paper it's supported]
Status: supported / needs evidence / needs weakening
```

## Workflow

1. Answer every question above with evidence from the paper.
2. Mark each item.
3. Revise claims, writing, experiments, or scope accordingly.
4. Repeat until no major rejection risk remains.
