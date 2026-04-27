# Community Report: Miao / Hmong
**TIODF · Paper 1 · Community 2**
*Generated: 2026-04-25*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 11 / 11      | 100%      |
| GPT-EN    | 11 / 11      | 100%      |
| DS-ZH     | 9 / 11       | 82%       |
| DS-EN     | 9 / 11       | 82%       |

GPT achieves full knowledge accessibility in both languages. DeepSeek fails two probes per language condition, but the failing probes differ by language.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Condition(s) | Answer | Knowledge Basis |
|-------|-------------|--------|-----------------|
| B1 (lusheng = qeej?) | DS-ZH, DS-EN | No (both) | Same reed-pipe instrument; different regional names |
| C1 (Hmong is subgroup of Miao?) | DS-ZH only | No | Hmong comprise ~1/3 of Miao population in China |
| C2 (Miao and Hmong share ethnic origin?) | DS-EN only | No | Community spans three nodes with historical continuity |

B1 is the only cross-language knowledge failure: DeepSeek denies the lusheng/qeej equivalence in both Chinese and English, indicating a genuine knowledge gap on this cultural marker. Notably, despite failing the probe, B1 narrative scores remain high across all conditions (11/12), confirming the knowledge gap does not propagate into narrative framing on this node.

**Asymmetric probes** (logically equivalent claims, opposite answers across languages in DeepSeek):

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| C1 | Yes | Yes | **No** | Yes |
| C2 | Yes | Yes | Yes | **No** |

C1 and C2 are two framings of the same underlying Miao/Hmong identity relationship. DeepSeek gives opposite answers depending on language direction, indicating that its Chinese-language and English-language representations of this identity boundary are non-integrated.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 11 | 2.82 | 2.45 | 2.45 | 2.82 | **10.55** |
| GPT-ZH    | 11 | 2.73 | 2.27 | 2.55 | 2.73 | 10.27 |
| DS-ZH     | 9  | 2.67 | 2.11 | 2.33 | 2.11 | 9.22  |
| DS-EN     | 9  | 2.44 | 2.11 | 2.11 | 2.22 | 8.89  |

Overall scores are substantially higher than Dai/Thai across all conditions. GPT-EN outperforms GPT-ZH (10.55 vs. 10.27) — a reversal of the ZH-advantage seen in Dai/Thai — suggesting that English-language corpora carry stronger cross-border Miao/Hmong cultural knowledge, likely driven by the Hmong diaspora's substantial English-language cultural production.

The GPT–DeepSeek gap is narrower here than in Dai/Thai (~1–1.7 points vs. ~2.6 points). Ossification is present but less severe and less systematic.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A2     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| C2     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| C2     | DS-ZH     | 2  | 2  | 1  | 1  | **6** |
| A3     | GPT-EN    | 2  | 2  | 1  | 2  | **7** |

**A2 · DS-EN (total = 4)** is the most extreme KB-gap in the dataset. All four narrative dimensions collapse to 1/3 under English prompting despite the model passing the knowledge probe. The same model under Chinese prompting scores 10/12 on the same prompt — a within-model, cross-language framing divergence of 6 points, confirming this is a language-conditioned framing failure on the cross-border historical continuity node rather than a knowledge deficit. This pattern is consistent with the **refugee-frame compression** mechanism identified during screening (EN-language models collapsing Hmong history toward post-1975 displacement, erasing pre-migration continuity), but direct confirmation requires inspection of the response text.

**C2 · GPT-ZH (total = 5) and DS-ZH (total = 6)** constitute a cross-model Chinese ossification signal. Both models — despite passing the knowledge probe — suppress ID, CC, and NR to floor level when asked whether the Chinese official *Miao* category and the Southeast Asian *Hmong* self-designation refer to the same ethnic-origin community. This cross-model convergence under Chinese prompting is absent in the English condition (GPT-EN: 11; DS-EN: probe-failed but narrative score = 11), pointing to the *minzu* administrative frame as an independent suppressor of trans-border identity recognition.

**A3 · GPT-EN (total = 7)** sits at threshold. CC collapses to 1 while other dimensions score 2 — a secondary signal consistent with EN-language cultural continuity suppression but not conclusive on its own.

---

## 4. Summary

The Miao/Hmong community produces two confirmed ossification patterns operating in opposite language directions.

**Pattern 1 — EN-language framing failure on cross-border continuity (DS-EN primary):** The A2·DS-EN collapse (total = 4; within-model cross-language gap of 6 points) confirms language-conditioned framing failure on the historical continuity node. The score pattern is consistent with the **refugee-frame compression** mechanism identified in screening, but the mechanism label is grounded in response-text analysis rather than scores alone. A3·GPT-EN (CC floor, total = 7) provides a secondary cross-model signal.

**Pattern 2 — Chinese-language identity ossification (cross-model):** C2 produces low scores under ZH prompting in both GPT-5.1 (5/12) and DeepSeek-V3.2 (6/12), while both models score 11/12 under EN prompting on the same prompt. The *minzu* administrative frame suppresses acknowledgment of the Miao/Hmong identity overlap specifically under Chinese-language conditions, independent of model origin.

The B1 KL-distortion cases (lusheng/qeej) represent a genuine knowledge gap in DeepSeek rather than a framing failure, and do not propagate into narrative scores — analytically separate from the two ossification patterns above.
