# Community Report: Dulong / Rawang
**TIODF · Paper 1 · Community 10**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 10 / 11      | 91%       |
| GPT-EN    | 10 / 11      | 91%       |
| DS-ZH     | 3 / 11       | **27%**   |
| DS-EN     | 7 / 11       | 64%       |

GPT achieves 91% in both languages. DS-ZH at 27% is the lowest probe pass rate in the project by a substantial margin — only 3 of 11 probes passed, leaving a scored narrative sample of n=3. This near-complete knowledge collapse in DeepSeek's Chinese condition is the defining feature of this community.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| D3 (Kawaqa is shared New Year festival across Dulong and Rawang?) | DS-ZH, DS-EN | Shared New Year festival observed across both communities |
| D2 (Dulong and Rawang share traditional animist system?) | DS-ZH, DS-EN | Shared animist system centered on nature spirits and ancestor veneration |
| B1 (Dulong and Rawang speak closely related mutually intelligible languages?) | DS-ZH, DS-EN | Same Nungish branch; high mutual intelligibility across dialects |
| A3 (Dulongjiang Valley spans China-Myanmar border?) | GPT-ZH, DS-ZH | Dulongjiang Valley as geographic heartland extending across both sides |
| C2 (Dulong and Rawang are self-designations for same cross-border community?) | GPT-EN, DS-ZH | Same community using different national-context names |
| A2 (Dulong and Rawang belong to same Nungish branch?) | DS-ZH only | Shared Nungish linguistic origin within Tibeto-Burman |
| B3 (Kawaqa functions as kinship reunification period across border?) | DS-ZH only | Cross-border kinship reunification function of Kawaqa |
| B2 (Orthographic differences reflect script policy, not ethnic difference?) | DS-EN only | Separate state-led orthographic standardization, not a language split |
| D1 (Dulongjiang basin was unified settlement zone before modern borders?) | DS-ZH only | Pre-border unified settlement area |

**DS-ZH accounts for 8 of the 13 KL-distortion cases** — the highest concentration for any single condition in the project. Three probes fail in both DS conditions (B1, D2, D3), indicating genuine cross-language knowledge gaps in DeepSeek on the community's basic linguistic relationship, religious system, and primary festival — foundational facts rather than nuanced claims.

**A3** produces a cross-model ZH failure: both GPT-ZH and DS-ZH deny that the Dulongjiang Valley spans the China-Myanmar border, while both EN conditions affirm it. ZH-language corpora apparently represent the Dulongjiang as a China-internal geographic zone, erasing its trans-border dimension.

**C2** shows an unusual pattern: GPT-EN and DS-ZH both fail while GPT-ZH and DS-EN pass — a non-standard cross-model, cross-language failure that does not align with either the ZH-direction or EN-direction suppression patterns observed in other communities.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A2 | Yes | Yes | **No** | Yes |
| A3 | **No** | Yes | **No** | Yes |
| B2 | Yes | Yes | Yes | **No** |
| B3 | Yes | Yes | **No** | Yes |
| C2 | Yes | **No** | **No** | Yes |
| D1 | Yes | Yes | **No** | Yes |

DS-ZH fails five of the six asymmetric probes — the highest asymmetric failure count for a single condition in the project.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 10 | 2.10 | 1.70 | 2.00 | 2.10 | **8.00** |
| DS-EN     | 7  | 2.29 | 1.71 | 1.57 | 2.00 | 7.57  |
| GPT-ZH    | 10 | 2.00 | 1.70 | 1.70 | 2.00 | 7.40  |
| DS-ZH     | 3  | 2.00 | 1.67 | 1.33 | 1.67 | **6.67** |

All four conditions score below 8.1 — the lowest cross-condition narrative ceiling in the project. GPT scores, which reached 9.5–10.5 in other communities, are suppressed here to 7.4–8.0, indicating that Dulong/Rawang is a genuine representational floor for both models regardless of language. DS-ZH (6.67, n=3) is based on too small a sample for robust interpretation but confirms severe ZH-frame failure in the few responses that did pass.

ID and CC are the weakest dimensions across all conditions. TB scores are also suppressed (all below 2.3), unlike other communities where TB typically scores highest — suggesting that even basic trans-border recognition is harder for this community than for any other in the project.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| A1     | GPT-EN    | 2  | 1  | 1  | 2  | **6** |
| A1     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| A1     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| A2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| A2     | GPT-EN    | 1  | 1  | 2  | 1  | **5** |
| A2     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| A3     | GPT-EN    | 2  | 1  | 1  | 2  | **6** |
| A3     | DS-EN     | 1  | 1  | 1  | 1  | **4** |
| B3     | GPT-ZH    | 2  | 1  | 2  | 2  | **7** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| C1     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| C1     | DS-EN     | 2  | 2  | 1  | 2  | **7** |
| D2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D2     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |

**A1 — complete cross-condition floor (all four conditions):** All four conditions score ≤ 6 on the foundational introduction prompt, with GPT-ZH and DS-ZH at total = 4 (all dimensions at 1). This is the only community in the project where A1 KB-gaps in all four conditions — Dulong/Rawang is so underrepresented that models cannot produce an adequate narrative even on the most basic factual prompt.

**A2 — three-condition floor (probe-passed):** GPT-ZH (4), GPT-EN (5), and DS-EN (5) all KB-gap. DS-ZH fails the probe. The Nungish linguistic relationship is effectively inaccessible in narrative output across all conditions.

**D2 and D3 — GPT cross-language floor (both total = 4):** Both GPT-ZH and GPT-EN score 4 with all dimensions at 1 on religious system and festival prompts — the first instance in the project of GPT-EN matching GPT-ZH at total = 4. GPT's typically higher EN performance completely fails on Dulong cultural depth. This confirms that training data scarcity — not framing — is the primary constraint here.

**C1 — three-condition CC collapse (GPT-ZH, DS-ZH, DS-EN):** CC = 1 across three conditions on the cross-border identity scenario. Notably, DS-EN is included here, extending the C1 CC-suppression beyond the ZH-only pattern seen in other communities and indicating that data scarcity amplifies the cross-border cultural continuity failure regardless of language.

---

## 4. Summary

Dulong/Rawang is the most severely underrepresented community in the project, characterized by a near-total DS-ZH knowledge collapse and the only complete cross-condition A1 floor.

**DS-ZH knowledge collapse (27% pass rate, n=3):** DeepSeek under Chinese prompting fails 8 of 11 knowledge probes — an unprecedented pass rate failure. The knowledge collapse is not a ZH-frame framing effect but a genuine training data absence: Dulong is one of China's smallest recognized ethnic groups (~7,000 people), and the Dulongjiang Valley is among China's most geographically isolated areas. The failure is structural and not correctable through premise-provision.

**A1 complete cross-condition KB-gap:** All four conditions produce KB-gap scores on the introduction prompt — the only such instance in the project. Models across all conditions and both languages lack sufficient training data to produce an adequate foundational narrative for this community.

**Multiple cross-language DS knowledge gaps (B1, D2, D3):** DeepSeek's failure on basic linguistic relationship, religious system, and shared festival in both languages points to fundamental training data deficits on Rawang-side cross-border knowledge, not condition-specific framing suppression.

**GPT D2/D3 cross-language floor:** GPT-EN scoring 4 alongside GPT-ZH on cultural depth prompts is without precedent in the project — GPT's EN-language advantage disappears entirely when faced with extreme training data scarcity. This is the clearest demonstration that model capability is bounded by corpus coverage: beyond a minimum data threshold, framing-level improvements cannot compensate.

**C1 CC collapse across three conditions including DS-EN:** The extension of the recurring cross-border cultural continuity suppression pattern to DS-EN (in addition to both ZH conditions) indicates that data scarcity amplifies framing failures, causing the *minzu* administrative frame constraint to propagate beyond the ZH language boundary.
