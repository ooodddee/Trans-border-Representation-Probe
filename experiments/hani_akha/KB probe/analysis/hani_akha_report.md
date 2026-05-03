# Community Report: Hani / Akha
**TIODF · Paper 1 · Community 7**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 8 / 11       | 73%       |
| GPT-EN    | 11 / 11      | 100%      |
| DS-ZH     | 6 / 11       | 55%       |
| DS-EN     | 8 / 11       | 73%       |

GPT-EN achieves full knowledge accessibility. ZH conditions have substantially lower pass rates (73% and 55%), with multiple cross-model ZH-specific failures — a pattern not seen in this form in prior communities.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| A2 (Chinese Hani and SE Asian Akha are two nodes of same ethnic group?) | GPT-ZH, DS-ZH | Same people, different national names; historical continuity across China-SE Asia border |
| B2 (Yuanyang-style terraced rice agriculture present across all countries?) | GPT-ZH, DS-ZH | ~1,300 years of terraced farming present in Yunnan, Myanmar, Laos, Thailand, and Vietnam |
| B3 (Men expected to recite 50+ generations of patrilineal genealogy?) | DS-ZH, DS-EN | Cross-border patrilineal genealogy recitation practice across all Hani/Akha nodes |
| D2 (Akhazang is a living system still practised in SE Asian Akha communities?) | DS-ZH, DS-EN | Akhazang is a living normative order in contemporary SE Asian Akha communities |
| A3 (Akha communities in SE Asia established before 19th century?) | GPT-ZH only | Long-standing indigenous highland communities predating modern borders |
| D3 (SE Asian Akha communities predate modern China-Myanmar/China-Laos borders?) | DS-ZH only | SE Asian Akha presence historically established before modern borders |

**A2 and B2** produce cross-model ZH-specific failures: both GPT-ZH and DS-ZH deny that Chinese Hani and SE Asian Akha are historically continuous, and that terraced rice agriculture is a shared cross-border practice — while both EN conditions affirm these claims. This is the first instance in the project of cross-model knowledge failure concentrated in the ZH direction. The *minzu* administrative frame, by categorizing 哈尼族 as a discrete Chinese national minority, appears to block acknowledgment of the Hani-Akha identity connection at the knowledge level in Chinese-language models — a more fundamental suppression than framing failure.

**B3 and D2** are cross-language DS failures: DeepSeek denies both the patrilineal genealogy recitation practice and Akhazang's contemporary vitality in SE Asian communities in both Chinese and English — genuine knowledge deficits on the community's core normative system.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A2 | **No** | Yes | **No** | Yes |
| A3 | **No** | Yes | Yes | Yes |
| B2 | **No** | Yes | **No** | Yes |
| B1 | Yes | Yes | Yes | **Unknown** |
| D3 | Yes | Yes | **No** | Yes |

A2 and B2 show a clean cross-model ZH-direction reversal — the only such pattern in the project where ZH conditions fail and EN conditions pass across both models simultaneously.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-ZH    | 8  | 2.62 | 2.75 | 2.38 | 2.50 | **10.25** |
| GPT-EN    | 11 | 2.55 | 2.45 | 2.27 | 2.55 | 9.82  |
| DS-ZH     | 6  | 2.50 | 2.17 | 2.33 | 2.50 | 9.50  |
| DS-EN     | 8  | 2.50 | 2.00 | 1.75 | 2.50 | **8.75** |

The narrative score ordering is the inverse of the knowledge accessibility ordering: **GPT-ZH (10.25) is the highest-scoring condition despite having the lowest GPT pass rate (73%)**, and both ZH conditions outperform their EN counterparts. This inversion is the most structurally distinctive finding in Hani/Akha.

The explanation is the ZH knowledge gate effect: GPT-ZH's 8 probe-passed responses represent a filtered subset of prompts where Chinese-language models did acknowledge the Hani-Akha cross-border connection — and when that acknowledgment occurs, the rich Chinese ethnographic literature on 哈尼族 produces high-quality narratives. The ZH knowledge failures on A2, B2, and A3 exclude precisely the prompts most likely to produce ossified narratives, inflating the average of the passing subset.

**CC is the weakest dimension across all conditions** — the primary representational constraint for this community regardless of model or language. This contrasts with communities like Dai/Thai (where ID is the primary bottleneck) and confirms the community-specific nature of ossification failure modes.

**DS-EN (8.75)** is the weakest condition, with CC collapsing to 1.75 — the lowest CC condition average in the project outside of Lisu and Dai/Thai.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A2     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| B2     | DS-EN     | 2  | 2  | 1  | 2  | **7** |
| B3     | GPT-EN    | 2  | 2  | 1  | 2  | **7** |
| C2     | GPT-EN    | 2  | 2  | 1  | 2  | **7** |
| D2     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |

Hani/Akha has the fewest KB-gap cases in the project (5 cases), consistent with the high overall narrative scores. However, **CC = 1 in all five cases** — a uniform dimensional profile not seen in any other community. Cultural continuity is the exclusive collapsing dimension across every KB-gap case regardless of model, language, or prompt category.

**A2 · DS-EN (total = 4):** All four dimensions collapse on the foundational cross-border identity claim despite DS-EN passing the probe (DS-EN affirms Hani-Akha historical continuity in English but produces a fully ossified narrative). This is the clearest framing-level failure in this community — knowledge accessible, narrative collapsed.

**B3, C2, D2 · GPT-EN and GPT-ZH (total = 7 each):** All three show an identical dimensional profile (TB=2, ID=2, CC=1, NR=2). CC is the sole collapsing dimension across prompts spanning cultural continuity (B3), identity (C2), and cultural practice (D2). This consistency suggests that GPT systematically struggles to represent cross-border cultural continuity as an ongoing living practice rather than as historical fact.

---

## 4. Summary

Hani/Akha produces a structurally distinctive profile characterized by the inversion of the typical knowledge-narrative relationship and a unique cross-model ZH knowledge failure pattern.

**Cross-model ZH knowledge failure on A2 and B2:** Both models in Chinese deny the Hani-Akha identity connection and the cross-border terraced rice tradition — the first instance in the project of cross-model knowledge failure in the ZH direction. The *minzu* administrative frame appears to operate not only as a framing filter but as a knowledge gate: the categorical separation of 哈尼族 from SE Asian Akha is strong enough to suppress affirmative knowledge responses in both Chinese-language models, not merely to distort their narrative framing.

**ZH narrative inversion:** GPT-ZH (10.25) is the highest-scoring condition despite the lowest GPT probe pass rate. ZH knowledge failures exclude the most ossification-prone prompts from the narrative scoring pool, producing a filtered high-scoring subset. This inversion is an artifact of the probe-exclusion design and should be interpreted carefully — it does not indicate that ZH framing is superior, but that ZH knowledge failures concentrate on a specific cluster of cross-border identity nodes.

**CC as the exclusive failure dimension:** All five KB-gap cases collapse on CC alone, with TB, ID, and NR scoring 2. Cultural continuity — the ability to represent Hani/Akha practices as living, cross-border, and ongoing rather than historical or China-bounded — is the community's primary representational constraint across all models and languages.

**DS cross-language gaps on B3 and D2:** DeepSeek's failure to recognize patrilineal genealogy recitation and Akhazang's contemporary vitality in both languages points to genuine training data deficits on the community's normative system, analytically separate from the ZH-direction framing failures above.
