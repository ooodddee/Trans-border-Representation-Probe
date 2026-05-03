# Community Report: Wa
**TIODF · Paper 1 · Community 4**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 10 / 11      | 91%       |
| GPT-EN    | 11 / 11      | 100%      |
| DS-ZH     | 10 / 11      | 91%       |
| DS-EN     | 7 / 11       | 64%       |

GPT-EN achieves full knowledge accessibility. GPT-ZH and DS-ZH each fail one probe. DS-EN is the weakest condition at 64%, with four KL-distortion cases concentrated on cross-border linguistic continuity nodes.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| A1 (Wa are Austroasiatic-speaking?) | DS-ZH, DS-EN | Wa language: Austroasiatic family, Palaungic branch, Waic subgroup |
| A2 (Yunnan Wa and Wa State share same language continuum?) | GPT-ZH only | Shared Wa language continuum across China-Myanmar border |
| B1 (Yunnan Wa and Wa State belonged to same community before 1960 border?) | DS-EN only | 1960 China-Burma Boundary Treaty split a pre-existing community |
| B2 (Spoken Wa remains mutually intelligible across border despite orthographic divergence?) | DS-EN only | PRC and UWSA orthographies diverged; spoken varieties remain mutually intelligible |

**A1** is the only cross-language genuine knowledge gap: DS-ZH and DS-EN both deny the Austroasiatic classification, indicating a fundamental language-family misclassification in DeepSeek's training data independent of query language.

**B1 and B2** are DS-EN-specific failures on cross-border linguistic continuity — the same model affirms both claims in Chinese. This EN-direction language-conditioned suppression of the cross-border language relationship is consistent with the pattern seen in Lisu B1, where EN conditions specifically failed on the pan-community identity marker.

**GPT-ZH** fails only A2 (same language continuum), while affirming the claim in English — a ZH-specific knowledge suppression on linguistic classification, paralleling GPT-ZH's A1 failure in Lisu.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A2 | **No** | Yes | Yes | Yes |
| B1 | Yes | Yes | Yes | **No** |
| B2 | Yes | Yes | Yes | **No** |
| D1 | Yes | Yes | Yes | **Unknown** |

Asymmetry is model-specific and language-conditioned: GPT's ZH-specific failure is on linguistic classification (A2); DeepSeek's EN-specific failures are on historical community unity and mutual intelligibility (B1, B2). D1 produces an Unknown response in DS-EN rather than a clean Yes/No — classified as asymmetric but analytically distinct from the clear denial cases.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 11 | 2.55 | 1.91 | 2.09 | 2.36 | **8.91** |
| GPT-ZH    | 10 | 2.30 | 1.90 | 1.90 | 2.00 | 8.10  |
| DS-ZH     | 10 | 2.20 | 1.80 | 2.00 | 1.70 | 7.70  |
| DS-EN     | 7  | 2.14 | 1.71 | 1.86 | 1.57 | **7.29** |

Scores are moderate relative to prior communities — lower than Miao/Hmong but higher than Lisu across all conditions. GPT-EN is the strongest (8.91); DS-EN the weakest (7.29, n=7). The GPT–DeepSeek gap (~0.8–1.6 points) is narrower than Dai/Thai. ID and NR are consistently the weakest dimensions across all conditions, suggesting identity fluidity and narrative depth are the primary representational constraints for this community.

GPT-EN outperforms GPT-ZH (8.91 vs. 8.10), consistent with the Miao/Hmong pattern and suggesting that English-language corpora carry stronger Wa cross-border framing knowledge — likely due to greater English-language coverage of the Wa State political entity and Myanmar conflict context.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | GPT-ZH    | 2  | 2  | 1  | 1  | **6** |
| A2     | GPT-EN    | 1  | 1  | 2  | 1  | **5** |
| A2     | DS-ZH     | 2  | 1  | 2  | 1  | **6** |
| A2     | DS-EN     | 2  | 1  | 2  | 1  | **6** |
| A3     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A3     | GPT-EN    | 3  | 1  | 1  | 2  | **7** |
| A3     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| A3     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| B3     | DS-EN     | 2  | 1  | 2  | 1  | **6** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| C1     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| D1     | DS-ZH     | 2  | 1  | 2  | 1  | **6** |
| D2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D2     | GPT-EN    | 2  | 1  | 1  | 1  | **5** |
| D2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D2     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D3     | DS-ZH     | 1  | 1  | 2  | 1  | **5** |

**A2 — three-condition floor:** GPT-EN, DS-ZH, and DS-EN all score ≤ 6 on the cross-border language continuum prompt despite passing the probe. ID and NR collapse across these conditions while CC scores slightly higher (2), suggesting models can acknowledge some cultural link but cannot frame the relationship as a continuous trans-border phenomenon. GPT-ZH fails the probe on A2 (excluded from KB-gap analysis), making A2 a complete four-condition failure through different mechanisms.

**A3 — cross-condition floor (all four conditions):** All four conditions fall at or below 7, with CC and ID suppressed across models and languages. Geographic distribution of Wa — particularly the Wa State administrative entity and its geopolitical complexity — appears to be a structurally difficult representational node regardless of condition.

**C1 — cross-model ZH floor:** Both GPT-ZH and DS-ZH score 7 with CC = 1, while EN conditions do not show the same pattern. This cross-model ZH-specific CC suppression on cross-border identity scenarios replicates the pattern seen in Miao/Hmong C2 and Lisu C1, consistent with the *minzu* frame constraining cultural continuity acknowledgment under Chinese prompting.

**D2 and D3 — cross-condition structural floors:** D2 produces scores of 4–5 across all four conditions; D3 affects three conditions with total = 4 across both GPT conditions in both languages. Cultural depth representation (religious practices and ritual festivals) is broadly underdeveloped for Wa across all models and languages.

---

## 4. Summary

Wa presents a moderate-severity ossification profile, positioned between Miao/Hmong and Lisu. The defining features are:

**DS-EN as primary failure condition:** DS-EN has the lowest probe pass rate (64%) and lowest narrative scores (7.29), with knowledge failures concentrated on cross-border linguistic continuity nodes (B1, B2). The same model affirms these claims in Chinese — language-conditioned suppression of the cross-border language relationship in English, analytically parallel to the EN-direction failures observed in Lisu B1.

**Genuine knowledge gap on Austroasiatic classification (DS, both languages):** DeepSeek's failure to recognize the Wa language as Austroasiatic in both conditions is the only cross-language knowledge gap in this community, pointing to a fundamental misclassification in DeepSeek's training data. Unlike framing failures, this cannot be corrected through premise-provision alone.

**Cross-model ZH suppression on C1:** Both GPT-ZH and DS-ZH collapse CC to 1 on the cross-border identity scenario, replicating the pattern observed in Miao/Hmong and Lisu. The *minzu* administrative frame suppresses cultural continuity acknowledgment across model origins under Chinese prompting — a now-recurring cross-community finding.

**Structural floors on A3, D2, and D3:** These three prompts produce KB-gap scores across nearly all conditions, indicating that geographic distribution (specifically Wa State's contested political status) and Wa cultural depth are broadly underdeveloped in LLM training data regardless of model or language.
