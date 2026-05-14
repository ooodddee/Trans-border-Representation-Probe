# Ossification Pattern Analysis Report
## TIODF — Quantitative Pattern Validation

**Corpus:** 9 communities (Karen excluded) × 4 conditions × 11 prompts = 395 responses  
**Models:** GPT-5.1 (US-origin) and DeepSeek-V3.2 (China-origin)  
**Conditions:** GPT-ZH, GPT-EN, DS-ZH, DS-EN  
**Patterns coded:** P1–P5 (LLM-as-judge, Claude Sonnet, temperature=0)

---

## 1. Overall Prevalence

32.9% of all responses (130/395) exhibit at least one ossification pattern. The remaining 67.1% are non-ossified, confirming that ossification is systematic but not total — both models are capable of producing non-ossified output, making the failure a default framing choice rather than an absolute incapacity.

---

## 2. Pattern Distribution by Condition

| Condition | Any pattern | P1 | P2 | P3 | P4 | P5 |
|-----------|------------|----|----|----|----|-----|
| GPT-ZH | 33.3% | 16.2% | 0.0% | 16.2% | 8.1% | 5.1% |
| GPT-EN | 10.2% | 4.1% | 0.0% | 4.1% | 1.0% | 3.1% |
| DS-ZH | 62.6% | 35.4% | 9.1% | 34.3% | 9.1% | 6.1% |
| DS-EN | 25.3% | 11.1% | 5.1% | 12.1% | 1.0% | 4.0% |

DS-ZH is the most ossified condition (62.6%), nearly double GPT-ZH (33.3%) and six times GPT-EN (10.2%). This gradient holds consistently across all nine communities.

---

## 3. Model-Origin Effects: DS vs. GPT

Chi-square tests were used for P1, P3, P4, and P5. Fisher's Exact Test was applied to P2, because GPT-5.1 produced zero instances, making the chi-square asymptotic approximation unreliable when one cell count is zero. Both tests assess whether the observed prevalence difference between DS and GPT could plausibly arise by chance.

Note on independence: responses to the same prompt across conditions share a common stimulus and are therefore not strictly independent observations. Chi-square and Fisher's Exact Test are applied here as approximate inferential tools; results should be interpreted as indicative rather than precise hypothesis tests.

### Tier 1 — DS-characteristic patterns (statistically significant)

| Pattern | DS% | GPT% | Test | p |
|---------|-----|------|------|---|
| P1 Minzu-Frame Lock | 23.2% | 10.2% | χ²=11.22 | 0.0008*** |
| P2 Political Substitution | 7.1% | 0.0% | Fisher's Exact | 0.0001*** |
| P3 Acknowledge-Peripheralize | 23.2% | 10.2% | χ²=11.22 | 0.0008*** |

**P2 is exclusively a DS pattern.** GPT-5.1 produces zero instances across all 395 responses. P2 appears in 14 cases spanning 8 of 9 communities (DS-ZH: 9 cases; DS-EN: 5 cases), confirming it is not community-specific but a cross-community behavioral signature of DeepSeek.

**P1 and P3 co-occur systematically in DS.** Their identical prevalence rates (23.2%) indicate they function as a coupled mechanism: when DS produces a minzu-frame narrative, it simultaneously peripheralizes cross-border content. In GPT, P1 and P3 are present at roughly half the rate and are less tightly coupled.

### Tier 2 — Shared patterns (no significant model-origin difference)

| Pattern | DS% | GPT% | Test | p |
|---------|-----|------|------|---|
| P4 Administrative Identity Compression | 5.1% | 4.6% | χ²=0.00 | 1.000 (ns) |
| P5 Cross-Border Continuity Denial | 5.1% | 4.1% | χ²=0.05 | 0.818 (ns) |

P4 and P5 are shared mechanisms, present at statistically indistinguishable rates in both models. Both models reduce identity questions to Chinese administrative categories at similar rates, and both produce cross-border denial at similar rates. This indicates these patterns reflect a broader structural tendency in language models processing Chinese-language identity questions, independent of training corpus geography.

---

## 4. Language Effects

Query language significantly modulates ossification rate within both models:

| Model | ZH ossification | EN ossification | χ² | p |
|-------|----------------|-----------------|-----|---|
| GPT-5.1 | 33.3% | 10.2% | 14.11 | 0.0002*** |
| DeepSeek-V3.2 | 62.6% | 25.3% | 26.57 | <0.0001*** |

Chinese-language queries elicit substantially higher ossification in both models. The language effect is larger in absolute terms for DS (37.3 percentage points vs. 23.1 for GPT), suggesting that Chinese-language training data reinforces ossification frames more strongly in DS than in GPT. Critically, however, both models show the same directional effect — ossification is a language-conditioned phenomenon across model origins.

---

## 5. Pattern Severity: Score Gaps

Mann-Whitney U tests (two-sided) comparing rubric scores for responses with versus without each pattern:

| Pattern | n (present) | Mean score (present) | Mean score (absent) | Diff | r | p |
|---------|-------------|---------------------|---------------------|------|---|---|
| P2 Political Substitution | 14 | 4.93 | 8.59 | −3.66 | 0.715 | <0.001*** |
| P1 Minzu-Frame Lock | 66 | 5.48 | 9.06 | −3.58 | 0.687 | <0.001*** |
| P3 Acknowledge-Peripheralize | 66 | 7.26 | 8.71 | −1.45 | 0.308 | <0.001*** |
| P4 Administrative Identity Compression | 19 | 7.21 | 8.53 | −1.32 | 0.272 | 0.043* |
| P5 Cross-Border Continuity Denial | 18 | 8.11 | 8.48 | −0.37 | 0.097 | 0.481 (ns) |

**P2 produces the largest score penalty** (−3.66, r=0.715), reflecting that political substitution completely displaces cultural content. P1 is nearly as severe (−3.58, r=0.687) because minzu-frame lock suppresses cross-border content at the structural level. P3 is moderate (−1.45, r=0.308) — cross-border content is present but marginalized, so the rubric awards partial credit for factual accuracy while penalizing framing failure.

**P5 does not produce a statistically significant score penalty** (p=0.481, r=0.097). Although the pattern is identifiable qualitatively — responses explicitly deny shared cross-border traditions — the responses still engage substantively with cultural content and achieve rubric scores comparable to non-ossified responses. P5 is therefore retained as a qualitative observation but is not treated as a primary quantitative finding.

---

## 6. Community Gradient

| Community | Overall | DS-ZH | GPT-EN |
|-----------|---------|-------|--------|
| Dulong | 48% | 64% | 27% |
| Dai-Thai | 41% | 64% | 18% |
| Hani/Akha | 41% | 55% | 36% |
| Lisu | 36% | 73% | 9% |
| Wa | 36% | 82% | 0% |
| Lahu | 32% | 82% | 0% |
| De'ang | 30% | 64% | 0% |
| Miao/Hmong | 18% | 45% | 0% |
| Jingpo/Kachin | 14% | 36% | 0% |

Two observations stand out:

**Lahu and Wa reach 82% ossification in DS-ZH**, the highest in the corpus. Both are communities where Chinese-side populations are relatively small and the larger population resides in Myanmar — making the minzu-frame lock particularly distorting.

**Hani/Akha has the highest GPT-EN rate (36%)**, which is anomalous. This reflects P4 (Administrative Identity Compression) appearing in GPT-EN C-category prompts for this community — suggesting that even in the most favorable condition, GPT defaults to administrative framing when handling Hani/Akha identity questions, possibly due to the complexity of the Hani-Akha naming relationship across national borders.

**Jingpo/Kachin has the lowest overall rate (14%)**, consistent with its relatively high rubric scores across conditions. This community's well-documented cross-border presence (Jingpo in China, Kachin in Myanmar) may be better represented in both models' training data, reducing the frequency of framing failures.

---

## 7. Embedding Group Structure

For embedding metric blindness analysis, responses are assigned to four groups based on pattern labels:

| Group | n | Mean rubric score |
|-------|---|-------------------|
| Non-ossified (no pattern) | 265 | 9.33 |
| P2/P3 Framing failure | 77 | 6.90 |
| P1 Pure lock | 24 | 4.38 |
| P4/P5 Other | 29 | 8.10 |

The score gap between non-ossified and P2/P3 framing failure is **2.43 points** (out of 12). This is the key comparison for embedding analysis: P2 and P3 responses contain cross-border vocabulary and cultural terms (and therefore will produce high KC-response embedding similarity), yet rubric scores are 2.43 points lower. If embedding similarity cannot distinguish non-ossified from P2/P3 responses, this constitutes direct evidence of metric blindness at the mechanism level.

---

## 8. Summary of Key Findings

**Finding 1 — Ossification is systematic but not universal.** 32.9% of responses show at least one pattern, confirming that ossification reflects a default framing choice rather than a knowledge absence.

**Finding 2 — P2 (Political Substitution) is exclusively a DeepSeek signature.** Zero instances appear in GPT across 395 responses; 14 instances appear in DS spanning 8 communities. This is the sharpest cross-model distinction in the corpus.

**Finding 3 — P1 and P3 are DS-characteristic but not DS-exclusive.** GPT produces these patterns at half the DS rate. Both models show minzu-frame ossification; DS shows it with greater frequency and severity.

**Finding 4 — P4 and P5 are model-origin-independent.** Administrative identity compression and cross-border continuity denial occur at statistically indistinguishable rates in both models, suggesting they reflect shared structural properties of language models rather than training corpus geography.

**Finding 5 — Language significantly modulates ossification in both models.** Chinese-language queries elicit substantially more ossification than English-language queries, but the directional effect holds across both model origins.

**Finding 6 — P5 does not produce a significant score penalty.** Despite being qualitatively identifiable, cross-border continuity denial does not significantly lower rubric scores (p=0.481), distinguishing it from the four other patterns in terms of measurable impact on ossification severity.
