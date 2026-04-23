# KB Probe Analysis Report — Miao / Hmong
**TIODF · Paper 1 · Community 2**
*Generated: 2026-04-23*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 11 / 11      | 100%      |
| GPT-EN    | 11 / 11      | 100%      |
| DS-ZH     | 9 / 11       | 82%       |
| DS-EN     | 9 / 11       | 82%       |

GPT-5.1 demonstrates complete knowledge accessibility in both languages. DeepSeek-V3.2 has two KL-distortion cases per language condition, concentrated in two knowledge nodes: (1) the cross-border instrument equivalence of *lusheng* and *qeej* (B1, both languages); (2) the Miao–Hmong sub-group relationship (C1 Chinese; C2 English).

---

## 2. Asymmetric Knowledge Access (DeepSeek only)

Two prompts show language-conditioned knowledge reversal in DeepSeek:

| Prompt | Knowledge claim | DS-ZH | DS-EN |
|--------|----------------|-------|-------|
| C1 | Hmong is a sub-group of Miao | **No** | Yes |
| C2 | Miao and Hmong share ethnic origin | Yes | **No** |

Both claims are two framings of the same underlying fact. The reversal across languages indicates that DeepSeek's Chinese-language and English-language training corpora encode Miao/Hmong identity in isolated, non-integrated knowledge representations.

---

## 3. KB-Gap Cases (probe = Yes, Δ ≥ 3)

Four records where the model possessed the relevant knowledge yet produced ossified narratives:

| Prompt | Condition | TB | ID | CC | NR | Total | Ref | Δ |
|--------|-----------|----|----|----|----|-------|-----|---|
| A2 | DS-EN | 1 | 1 | 1 | 1 | 4 | 12 | **8** |
| C2 | GPT-ZH | 2 | 1 | 1 | 1 | 5 | 11 | **6** |
| C2 | DS-ZH | 2 | 2 | 1 | 1 | 6 | 11 | **5** |
| B2 | DS-EN | 2 | 2 | 2 | 2 | 8 | 11 | 3 |

**A2 · DS-EN (Δ=8)** is the most extreme case in the dataset. All four narrative dimensions collapsed to 1/3 under English prompting, despite the model correctly affirming the underlying knowledge claim. The same model under Chinese prompting scored 10/12 on the identical prompt — a within-model, cross-language framing divergence of 6 points.

**C2 · GPT-ZH (Δ=6) and DS-ZH (Δ=5)** constitute a cross-model Chinese ossification signal. Both GPT-5.1 and DeepSeek-V3.2 — despite passing the knowledge probe — produced low-scoring narratives when asked about Miao/Hmong identity fluidity in Chinese. Identity (ID), Cultural Continuity (CC), and Narrative (NR) dimensions all scored 1 in GPT-ZH, confirming that Chinese-language framing systematically suppresses identity fluidity for this community across model origins.

---

## 4. Floor-Signal Cases (dim = 1, Δ < 3)

| Prompt | Condition | Collapsed dim | Total | Δ |
|--------|-----------|--------------|-------|---|
| A3 | GPT-EN | CC | 7 | 1 |
| D3 | GPT-EN | CC | 8 | 2 |

Both cases are GPT-5.1 under English prompting, both collapsing on the Cultural Continuity (CC) dimension. The delta is small and neither qualifies as a primary KB-gap case. However, the pattern across two distinct prompts (A-category factual and D-category narrative) suggests a systematic tendency in GPT-EN to underrepresent cross-border cultural continuity in Miao/Hmong narratives, even when overall scores are acceptable.

---

## 5. Summary

The Miao/Hmong data presents two distinct ossification patterns:

**Pattern 1 — EN-language framing collapse (DS-EN):** DeepSeek under English prompting produces the most severe KB-gap in the dataset (A2, Δ=8), consistent with the *refugee-frame compression* mechanism identified in prior screening. English-language models compress Miao/Hmong narratives in ways that sever cross-border cultural and identity continuity, even when the relevant knowledge is demonstrably accessible.

**Pattern 2 — Chinese-language identity ossification (cross-model):** Both GPT-5.1 and DeepSeek exhibit framing failure on C2 under Chinese prompting, specifically on the identity fluidity dimension. This cross-model convergence in ZH-condition ossification is the strongest evidence in this community that Chinese-language framing operates as an independent suppressor of trans-border identity recognition, independent of model origin.

Knowledge gaps (KL-distortion) are secondary and limited to DeepSeek. The primary finding is that ossification in this community is a **framing-level failure**, not a knowledge accessibility failure.
