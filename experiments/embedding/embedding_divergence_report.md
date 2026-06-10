# Bilingual Embedding Divergence Analysis
## TIODF — Supplementary Corroborating Evidence

---

## Method

For each (model, community, prompt) triple, we compute the cosine distance between the ZH and EN response embeddings as a **bilingual divergence score** — a measure of how semantically different the same model's Chinese and English responses are to the same question.

**Embedding model:** `paraphrase-multilingual-MiniLM-L12-v2` (multilingual-aligned space; ZH and EN vectors are directly comparable without translation)

**Length control:** Responses truncated to 500 characters before encoding. EN responses are 3–5× longer than ZH in character count; truncation reduces but does not fully eliminate this confound, as Chinese has higher information density per character.

**Corpus:** 9 communities × 2 models × 11 prompts = 198 divergence values (99 per model). Divergence values are averaged per community per model to produce 9 community-level scores for correlation analysis.

**Analysis:**
- Spearman correlation between community-level divergence and same-condition narrative scores, computed for all four (model × language-condition) pairings
- Heatmap of divergence by community × prompt category (A–D) for both models on a shared color scale

Both models (DeepSeek-V3.2, GPT-5.1) and both language conditions (ZH, EN) are treated symmetrically throughout.

---

## Results

### Spearman Correlations

| Pairing | r | p |
|---------|---|---|
| DS divergence vs DS-ZH score | −0.583 | 0.099 |
| DS divergence vs DS-EN score | **−0.717** | **0.030** |
| GPT divergence vs GPT-ZH score | −0.500 | 0.170 |
| GPT divergence vs GPT-EN score | **−0.750** | **0.020** |

All four r values are negative, indicating that communities with higher ZH/EN divergence consistently receive lower narrative scores — across both models and both language conditions. The EN-condition pairings reach statistical significance for both models (DS: p = 0.030; GPT: p = 0.020); ZH-condition pairings show the same direction but do not reach significance at n = 9.

**Why EN correlations are stronger:** ZH narrative scores are uniformly suppressed in ossification-heavy communities (ZH is the primary locus of ossification), leaving limited variance for correlation. EN scores vary more across communities — high in communities where EN framing is adequate, low where EN framing also fails — producing a cleaner relationship with divergence. High divergence signals that ZH and EN responses diverged substantially, which corresponds most directly to EN score variance: when the two language responses diverge, it is the EN score that captures the difference between communities where the model recovers under EN conditions and those where it does not.

### Heatmap Findings

**DS C-column (identity fluidity) for Lisu = 0.452** — the highest single cell in the dataset. DS produces opposing responses under ZH and EN conditions on identity-category prompts for Lisu (ZH: denies Lisu/Lisaw cross-border identity; EN: affirms it), directly reflected in maximal embedding divergence. GPT's Lisu C = 0.285, substantially lower, consistent with GPT showing less identity ossification on this community.

**A-column (knowledge baseline) is elevated for Wa and Dulong in both models** (DS: 0.400, 0.366; GPT: 0.396, 0.286). These are the two communities with the highest KB probe failure rates. High A-column divergence here reflects knowledge instability — both ZH and EN responses are inconsistent because the underlying training data is sparse — rather than framing divergence. This is mechanistically distinct from the Lisu C-column pattern.

**B-column (cross-border connectivity) is the lowest across all communities and both models.** Factual cross-border questions elicit the most consistent ZH/EN responses, confirming that the divergence measure is not noise: it is highest where framing or knowledge instability is greatest, and lowest where factual answers are stable.

---

## Interpretation

This analysis does not independently prove ossification. Its contribution is to show that **the same patterns identified through human coding are detectable at the embedding level through a fully independent method**: communities coded as more severely ossified also produce greater semantic distance between their ZH and EN responses. The consistency of the negative correlation direction across all four model × language-condition pairings, and the significance of the EN-condition results in both models independently, provides directional corroboration for the primary KB-gap and pattern-coding findings.

**Key limitation:** Divergence conflates framing differences with content differences and knowledge gaps. The Wa and Dulong A-column elevation illustrates this: high divergence there reflects data scarcity, not ossification. Community-level interpretation requires cross-referencing with KB probe results.
