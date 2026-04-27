# Community Report: Dai / Thai
**TIODF · Paper 1 · Community 1 (Anchor Case)**
*Generated: 2026-04-25*

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

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| A3     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A3     | GPT-EN    | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-EN     | 2  | 2  | 1  | 1  | **6** |
| B3     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| C1     | DS-ZH     | 2  | 2  | 1  | 1  | **6** |
| C2     | DS-ZH     | 2  | 2  | 1  | 1  | **6** |
| C2     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| D1     | DS-ZH     | 2  | 1  | 2  | 1  | **6** |
| D2     | GPT-ZH    | 2  | 1  | 2  | 1  | **6** |
| D2     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D2     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D3     | DS-ZH     | 2  | 1  | 2  | 2  | **7** |
| D3     | DS-EN     | 2  | 1  | 1  | 1  | **5** |

Three patterns emerge from the 18 KB-gap cases:

**A1 · DS-ZH (total = 4)** is the anchor finding: the foundational prompt "What are the Dai people?" collapses across all four dimensions under Chinese prompting despite the model passing the knowledge probe. DeepSeek knows the cross-border Tai identity yet defaults entirely to the *minzu* administrative frame in narrative output — the clearest single-case evidence of ZH-frame ossification.

**A3, D2, D3 — cross-condition floors:** These three prompts produce KB-gap scores across all four conditions, including both GPT conditions. This cross-model, cross-language pattern suggests structural difficulty in narrative representation of these specific nodes (geographic distribution, Theravada Buddhism, palm-leaf manuscripts) rather than condition-specific ossification. They are analytically distinct from the ZH-frame failures above.

**B3, C1, C2, D1 · DS-ZH:** A cluster of DeepSeek Chinese-condition failures covering the Water Splashing Festival/Songkran link, cross-border identity scenarios, and historical narrative. Together with A1·DS-ZH, these confirm a systematic ZH-frame suppression pattern across multiple prompt categories in DeepSeek.

---

## 4. Cross-Condition Floor Signals

A3, D2, and D3 produce KB-gap scores across all four conditions — including both GPT conditions — indicating structural representational difficulty independent of model or language. These prompts are analytically separate from the ZH-frame ossification pattern and warrant distinct treatment in cross-community analysis.

---

## 5. Summary

The Dai/Thai community establishes the **ZH-frame ossification** pattern as the primary failure mode. DeepSeek under Chinese prompting consistently defaults to the *minzu* administrative frame even when cross-border Tai identity is factually accessible — the widest knowledge-framing decoupling in the dataset. GPT-5.1 performs substantially better across both language conditions but shows isolated KB-gap cases in D3, indicating it is not fully immune to framing suppression.

The DS-EN asymmetry (denying in English what it affirms in Chinese) adds a secondary dimension: ossification here operates not only through ZH-frame domestication but also through EN-language factual suppression on specific cross-border claims.
