# Community Report: Lisu
**TIODF · Paper 1 · Community 3**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 10 / 11      | 91%       |
| GPT-EN    | 10 / 11      | 91%       |
| DS-ZH     | 7 / 11       | 64%       |
| DS-EN     | 9 / 11       | 82%       |

GPT achieves 91% in both languages. DS-ZH is the weakest condition at 64%, with multiple ZH-specific knowledge failures. DS-EN fails two probes.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| A1 (Lisu spans China, Myanmar, Thailand, India?) | GPT-ZH only | Archetypal Zomia four-country distribution |
| B1 (Lisu/Lisaw share self-designation ꓡꓲ-ꓢꓴ?) | GPT-EN, DS-EN | Pan-community self-designation used across all four countries |
| B2 (Fraser script used in Myanmar and Thailand?) | DS-ZH only | Fraser script used across trans-border Lisu communities |
| B3 (Kuoshi Festival celebrated across all four countries?) | DS-ZH only | Most important pan-Lisu annual celebration |
| C2 (傈僳族 and Lisaw are same community under different national names?) | DS-ZH only | Pan-community naming across four countries |
| D1 (Oral traditions cite Jinsha/Yalong basins as homeland?) | DS-ZH, DS-EN | Foundational origin narrative |

**B1** is the only cross-model knowledge failure, but it is EN-specific: both GPT-EN and DS-EN deny the shared self-designation ꓡꓲ-ꓢꓴ between Yunnan Lisu and Thai Lisaw, while both ZH conditions affirm it. This cross-model EN-direction failure on the pan-community identity marker — the inverse of the ZH-suppression pattern — is the most structurally distinctive finding in this community.

**DS-ZH** accumulates four ZH-specific knowledge failures (A1 excluded; B2, B3, C2 — all cross-border cultural continuity nodes) plus the cross-language D1 failure, consistent with broad ZH-frame suppression of trans-border knowledge.

**D1** is a cross-language knowledge gap in DeepSeek (both DS-ZH and DS-EN deny the Jinsha/Yalong oral tradition), indicating a genuine training data deficit on the Lisu origin narrative rather than a language-conditioned framing effect.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A1 | **No** | Yes | Yes | Yes |
| B1 | Yes | **No** | Yes | **No** |
| B2 | Yes | Yes | **No** | Yes |
| B3 | Yes | Yes | **No** | Yes |
| C2 | Yes | Yes | **No** | Yes |

Two distinct asymmetry patterns: GPT-ZH alone fails A1 (four-country distribution); both EN conditions fail B1 (self-designation equivalence); DS-ZH alone fails B2, B3, C2 (cultural continuity nodes). The B1 cross-model EN failure is structurally distinct from anything observed in prior communities.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 10 | 2.20 | 1.70 | 1.70 | 2.10 | **7.70** |
| GPT-ZH    | 10 | 2.20 | 1.80 | 1.80 | 1.80 | 7.60  |
| DS-EN     | 9  | 2.11 | 1.56 | 1.56 | 1.56 | 6.78  |
| DS-ZH     | 7  | 1.71 | 1.43 | 1.29 | 1.43 | **5.86** |

All four conditions fall below 8 — the same pattern seen in the first Lisu dataset. DS-ZH (5.86, n=7) remains the lowest condition in the project. GPT conditions converge near 7.6–7.7 with no meaningful ZH/EN advantage, suggesting neither language corpus carries substantially stronger Lisu framing knowledge.

ID and CC are consistently the weakest dimensions across all conditions, indicating that identity fluidity and cultural continuity are the primary representational constraints for this community regardless of model or language.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| A2     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| A2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| A2     | DS-EN     | 2  | 1  | 2  | 1  | **6** |
| A3     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-EN     | 3  | 1  | 1  | 2  | **7** |
| B3     | DS-EN     | 2  | 1  | 2  | 1  | **6** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| C1     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| C2     | GPT-EN    | 2  | 2  | 1  | 2  | **7** |
| C2     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| D2     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| D2     | GPT-EN    | 2  | 1  | 1  | 1  | **5** |
| D2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D3     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D3     | DS-EN     | 1  | 1  | 1  | 1  | **4** |

**A2 — cross-condition floor (three of four conditions at total = 4):** GPT-ZH, GPT-EN, and DS-ZH all collapse across all four dimensions despite passing the probe. DS-EN scores 6, also below threshold. This is the broadest single-prompt KB-gap in the dataset — complete cross-model framing failure on a linguistic relationship prompt, independent of language condition.

**C1 — cross-model ZH floor:** Both GPT-ZH and DS-ZH score 7 with CC = 1, while EN conditions do not show the same pattern. This replicates the cross-model ZH-specific CC suppression seen in Miao/Hmong C2 and Wa C1, consistent with *minzu* frame constraining cultural continuity acknowledgment under Chinese prompting.

**C2 · DS-EN (total = 4):** All four dimensions collapse despite DS-EN passing the probe. The same prompt fails the probe in DS-ZH (excluded from KB-gap analysis), making C2 a complete DeepSeek failure across both conditions through different mechanisms — probe failure in ZH, framing failure in EN.

**D2 and D3 — cross-condition structural floors:** D2 produces KB-gap scores in three conditions; D3 affects all four conditions with total = 4 across both models in both languages. Cultural depth representation (religious syncretism, ritual festivals) is broadly underdeveloped for Lisu regardless of model or language.

---

## 4. Summary

Lisu is the strongest ossification signal in the project, characterized by the combination of low probe pass rates, the lowest narrative scores across all conditions, and a qualitatively new knowledge failure pattern.

**Cross-model EN failure on B1 (self-designation):** Both GPT-EN and DS-EN deny that Yunnan Lisu and Thai Lisaw share the pan-community self-designation ꓡꓲ-ꓢꓴ, while both ZH conditions affirm it. This is the first instance in the project of a cross-model, EN-direction knowledge failure — distinct from the ZH-suppression patterns seen in prior communities and not reducible to the *minzu* frame mechanism.

**DS-ZH systematic ZH-frame suppression:** DS-ZH accumulates the most KL-distortion cases of any single condition in the project (B2, B3, C2, plus D1 cross-language), covering Fraser script distribution, Kuoshi Festival, naming equivalence, and oral traditions. Combined with the lowest narrative average (5.86), DS-ZH is the most ossification-prone condition for Lisu.

**A2 and D3 as cross-condition structural floors:** These two prompts produce KB-gap scores across all four conditions, including both GPT conditions. Alongside D2 (three conditions), they indicate that certain representational nodes — cross-border linguistic relationships and ritual-cultural depth — are broadly underdeveloped in LLM training data for this community, not attributable to a specific framing mechanism.

**DS knowledge gap on D1 (both languages):** DeepSeek's denial of the Jinsha/Yalong oral tradition origin narrative in both Chinese and English points to a genuine training data deficit, analytically separate from framing failures and not correctable through premise-provision.
