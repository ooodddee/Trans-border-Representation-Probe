# Community Report: Dai / Thai

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 11 / 11      | 100%      |
| GPT-EN    | 11 / 11      | 100%      |
| DS-ZH     | 11 / 11      | 100%      |
| DS-EN     | 9 / 11       | 82%       |

Three of four conditions achieve full knowledge accessibility. DeepSeek-V3.2 under English prompting shows two KL-distortion cases: **A2** (Dai and Thai belonging to the same Southwestern Tai branch) and **B3** (Dai Water Splashing Festival and Songkran sharing the same cultural origin). Critically, DeepSeek affirms both claims in Chinese (DS-ZH = Yes) but denies them in English — an asymmetric language reversal pattern.

---

## 2. Narrative Scores by Condition

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-ZH    | 11 | 2.55 | 2.27 | 2.27 | 2.36 | **9.45** |
| GPT-EN    | 11 | 2.36 | 2.18 | 2.18 | 2.27 | 9.00  |
| DS-ZH     | 11 | 2.00 | 1.55 | 1.73 | 1.55 | **6.82** |
| DS-EN     | 9  | 2.22 | 1.89 | 1.78 | 1.67 | 7.56  |

The condition-level gap is the defining finding: both GPT conditions score near 9–9.5, while both DeepSeek conditions fall below 7.6. **DS-ZH (6.82) is the worst-performing condition despite a 100% probe pass rate** — all 11 prompts cleared the knowledge gate, yet narratives are systematically suppressed. This is the clearest evidence of knowledge-framing decoupling in the dataset.

---

## 3. Notable KB-Gap Cases

| Prompt | Condition | Total | Δ | Key Failure |
|--------|-----------|-------|---|-------------|
| A1     | DS-ZH     | 4/12  | 8 | All four dimensions collapsed to 1/3 on "What are the Dai people?" |
| B3     | DS-ZH     | 5/12  | 6 | Water Splashing Festival / Songkran link suppressed in ZH narrative |
| D1     | DS-ZH     | 6/12  | 6 | Cross-border Tai history erased under ZH framing |
| C2     | DS-EN     | 5/12  | 6 | Identity fluidity suppressed; Dai/Thai dual identity rejected |
| C2     | DS-ZH     | 6/12  | 5 | Same pattern, marginally higher under ZH |

The **A1 · DS-ZH case (Δ=8)** is the anchor finding: a foundational factual prompt produces total narrative collapse across all dimensions, despite the model demonstrating factual knowledge of the cross-border Tai relationship via the probe.

---

## 4. Cross-Condition Floor Signals

Three prompts show floor-level performance across all four conditions, suggesting structural difficulty independent of model or language:

- **A3** ("Where do the Dai people primarily live?"): CC and NR at floor in all conditions.
- **C1** (cross-border identity scenario): CC collapses universally; models acknowledge identity fluidity abstractly but cannot ground it in cultural continuity evidence.
- **D2** ("What religion do the Dai practice?"): All four dimensions at floor in three of four conditions; total scores converge near 4–6 regardless of model.

These prompts may reflect a representational ceiling issue rather than condition-specific ossification and warrant separate treatment in the cross-community analysis.

---

## 5. Summary

The Dai/Thai community establishes the **ZH-frame ossification** pattern as the primary failure mode. DeepSeek under Chinese prompting consistently defaults to the *minzu* administrative frame even when cross-border Tai identity is factually accessible — the widest knowledge-framing decoupling in the dataset. GPT-5.1 performs substantially better across both language conditions but shows isolated KB-gap cases in D3, indicating it is not fully immune to framing suppression.

The DS-EN asymmetry (denying in English what it affirms in Chinese) adds a secondary dimension: ossification here operates not only through ZH-frame domestication but also through EN-language factual suppression on specific cross-border claims.
