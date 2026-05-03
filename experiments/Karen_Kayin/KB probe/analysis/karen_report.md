# Community Report: Karen / Kayin
**TIODF · Paper 1 · Community 5**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 11 / 11      | 100%      |
| GPT-EN    | 10 / 11      | 91%       |
| DS-ZH     | 8 / 11       | 73%       |
| DS-EN     | 8 / 11       | 73%       |

GPT-ZH achieves full knowledge accessibility — the only condition to do so in this community. DeepSeek conditions both sit at 73%, with failures distributed across different knowledge nodes by language.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| A3 (Karen are largest hill tribe group in Thailand?) | DS-ZH, DS-EN | Thai Karen (Karieng) are the largest officially recognized hill tribe group in Thailand |
| B1 (Pgaz K'Nyau self-designation used across Myanmar and Thailand?) | DS-ZH only | Pan-S'gaw self-designation used in highland communities across both countries |
| B2 (La Ku Kee wrist-tying ceremony is pan-Karen cultural marker?) | GPT-EN, DS-EN | Most important pan-Karen cultural marker observed across Myanmar, Thailand, and diaspora |
| D1 (La Ku Kee practiced in Karen diaspora communities in US and Australia?) | DS-ZH only | La Ku Kee extends to global Karen diaspora including US and Australia |
| D2 (Karen cross-border distribution originates from 19th-century British-Siam border?) | DS-EN only | Colonial boundary split a pre-existing Karen community |

**A3** is the only cross-language knowledge gap in DeepSeek: both DS-ZH and DS-EN deny that Karen are the largest hill tribe group in Thailand, indicating a genuine data deficit on Karen's demographic position in Thailand independent of query language.

**B2** is a cross-model EN-specific failure: both GPT-EN and DS-EN deny that La Ku Kee is a pan-Karen cultural marker, while both ZH conditions affirm it. This is structurally identical to the cross-model EN failure observed on Lisu B1 — models performing worse in English on a pan-community cultural continuity claim than in Chinese.

**DS-ZH** accumulates ZH-specific failures on B1 and D1 (both related to the La Ku Kee / pan-community identity axis), consistent with ZH-frame suppression of cross-border cultural continuity. However, the mechanism here is data scarcity rather than *minzu* domestication, since Karen has no counterpart in China's 56-minzu system.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| B1 | Yes | Yes | **No** | Yes |
| B2 | Yes | **No** | Yes | **No** |
| D1 | Yes | Yes | **No** | Yes |
| D2 | Yes | Yes | Yes | **No** |

B2 is the only probe where both EN conditions fail while both ZH conditions pass — a clean cross-model EN-direction reversal on the community's most important cultural continuity marker.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-ZH    | 11 | 2.45 | 2.64 | 2.45 | 2.45 | **10.00** |
| GPT-EN    | 10 | 2.30 | 2.80 | 2.40 | 2.30 | 9.80  |
| DS-EN     | 8  | 2.38 | 2.25 | 2.25 | 1.88 | 8.75  |
| DS-ZH     | 8  | 2.38 | 1.88 | 1.88 | 1.88 | **8.00** |

Overall scores are among the highest in the project, comparable to Miao/Hmong. The GPT–DeepSeek gap (~1.0–2.0 points) is moderate. Two findings are structurally distinctive:

**ID is the strongest dimension across all conditions** — GPT-EN scores 2.80, the highest single-dimension average in the project. Karen's absence from China's 56-minzu system means models cannot impose a single-nation identity frame, and fluid identity handling is correspondingly less suppressed. This directly contrasts with communities like Dai/Thai and Miao/Hmong where ID collapses under ZH prompting due to *minzu* categorization pressure.

**DS-ZH (8.00) underperforms DS-EN (8.75)** — a ZH-worse pattern. Unlike other communities where ZH-language data scarcity explains this, Karen's ZH underperformance cannot be attributed to *minzu* frame domestication (no such frame exists). It instead reflects genuine scarcity of Chinese-language coverage of Karen as a cross-border community, since the community falls outside China's domestic ethnic classification system entirely.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | GPT-EN    | 2  | 2  | 1  | 2  | **7** |
| A1     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A1     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| A2     | DS-ZH     | 2  | 1  | 2  | 1  | **6** |
| B1     | GPT-ZH    | 1  | 3  | 2  | 1  | **7** |
| B1     | DS-EN     | 2  | 2  | 2  | 1  | **7** |
| C1     | DS-ZH     | 1  | 1  | 2  | 1  | **5** |
| C1     | DS-EN     | 2  | 2  | 2  | 1  | **7** |

Karen has the fewest KB-gap cases in the project (8 cases), consistent with the higher overall narrative scores.

**A1 — three-condition floor:** GPT-EN, DS-ZH, and DS-EN all score ≤ 7 on the foundational "What are the Karen people?" prompt. CC collapses to 1 across all three conditions, while TB and ID score higher. Models can acknowledge the existence of Karen as an ethnic group but fail to frame them as a culturally continuous cross-border community. GPT-ZH passes with a full score on this prompt — the only condition to do so — consistent with Chinese-language corpora carrying specific knowledge of 克伦族 from the Myanmar border context.

**B1 · GPT-ZH (total = 7, TB = 1, ID = 3):** An unusual dimensional profile — TB collapses to 1 (cross-border recognition failure) while ID scores the maximum 3 (full identity fluidity recognition). This reflects GPT-ZH's ability to handle Karen identity complexity while simultaneously failing to frame the S'gaw self-designation Pgaz K'Nyau as a trans-border marker. NR also collapses to 1.

**C1 · DS-ZH (total = 5) and DS-EN (total = 7):** Both DeepSeek conditions produce KB-gap scores on the cross-border identity scenario, with NR collapsing to 1 in both. DS-ZH is more severe (5 vs. 7), suggesting that Chinese prompting produces stronger narrative frame suppression on identity scenarios even in a community without a *minzu* domestication mechanism.

---

## 4. Summary

Karen is the highest-scoring community in the project alongside Miao/Hmong, but produces a structurally distinctive ossification profile driven by the community's complete absence from China's 56-minzu system.

**Absence of *minzu* frame produces elevated ID scores:** The most notable finding is that ID is the strongest dimension across all conditions (GPT-EN: 2.80), in direct contrast to every other community where ID is consistently suppressed under ZH prompting. Without a domestic Chinese ethnic category to anchor to, models default to more fluid identity representations. This confirms the *minzu* frame as the primary suppressor of identity fluidity in ZH-condition responses — its absence produces measurably better identity handling.

**Cross-model EN failure on B2 (La Ku Kee):** Both GPT-EN and DS-EN deny that the wrist-tying ceremony is a pan-Karen cultural marker, while both ZH conditions affirm it. This is the second instance of cross-model EN-direction failure on a pan-community cultural continuity marker (after Lisu B1), suggesting a recurring pattern where EN-language corpora underrepresent specific cross-border cultural practices relative to ZH corpora.

**DS-ZH underperformance without *minzu* mechanism:** DS-ZH (8.00) falls below DS-EN (8.75) through data scarcity rather than frame domestication. Chinese-language coverage of Karen as a cross-border community is limited because Karen falls entirely outside China's domestic ethnic classification system — a different route to ZH-language underperformance than observed in Dai/Thai or Miao/Hmong.

**A3 cross-language knowledge gap (DS):** DeepSeek's failure to recognize Karen as Thailand's largest hill tribe group in both languages is an isolated genuine knowledge deficit, not a framing failure, and is analytically separate from the ossification patterns above.
