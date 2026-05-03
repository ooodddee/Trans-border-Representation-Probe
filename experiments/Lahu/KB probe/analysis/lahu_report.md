# Community Report: Lahu
**TIODF · Paper 1 · Community 9**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 9 / 11       | 82%       |
| GPT-EN    | 9 / 11       | 82%       |
| DS-ZH     | 7 / 11       | 64%       |
| DS-EN     | 8 / 11       | 73%       |

GPT achieves 82% in both languages. DS-ZH (64%) and DS-EN (73%) differ by one probe. Despite similar pass rates across conditions, narrative scores diverge sharply along language lines — indicating that which probes are failed, not how many, is the primary driver of condition-level performance differences.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| B3 (G'ui Sha recognized as supreme creator deity across all Lahu communities?) | All four conditions | Pan-Lahu supreme creator divinity recognized across all nodes regardless of religious conversion |
| A2 (Lahu spoken as mutually intelligible language across trans-border communities?) | GPT-ZH, GPT-EN, DS-EN | Substantial mutual intelligibility across Yunnan, Myanmar, Thailand, and Laos |
| B1 (Yunnan and Thai Lahu use same self-designation "Lahu"?) | DS-ZH, DS-EN | Pan-community self-designation used across all nodes |
| A3 (Myanmar, Thailand, Laos have substantial indigenous Lahu communities?) | DS-ZH only | Long-term indigenous Lahu presence predating modern migration |
| C1 (Shared G'ui Sha belief is core cross-border cultural bond?) | DS-ZH only | G'ui Sha as primary trans-border identity anchor |

**B3 is a complete cross-model, cross-language knowledge failure**: all four conditions deny that G'ui Sha is recognized as the supreme creator deity across all Lahu communities — the community's most fundamental pan-Lahu cosmological concept. This is the third instance of a complete cross-condition failure on a foundational cultural node in the project, after Jingpo/Kachin D1 (Majoi Shingra) and De'ang D2 (syncretic religious system).

**A2 is a near-complete failure (three conditions)**: GPT-ZH, GPT-EN, and DS-EN all deny Lahu mutual intelligibility across borders; DS-ZH is the only passing condition. This structural inversion — the typically weakest ZH condition as the sole knowledge-accessible one — reflects a specific gap in EN-language and GPT training data on Lahu linguistic continuity, not a ZH-frame advantage.

**B1 cross-language DS failure**: both DS-ZH and DS-EN deny that Yunnan and Thai Lahu share the self-designation "Lahu" — a genuine knowledge deficit in DeepSeek on the community's own pan-community name.

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A2 | **No** | **No** | Yes | **No** |
| A3 | Yes | Yes | **No** | Yes |
| C1 | Yes | Yes | **No** | Yes |

A2 is structurally unusual: DS-ZH is the sole passing condition while all other three fail. A3 and C1 show standard DS-ZH-specific failures on geographic distribution and cosmological identity claims.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 9  | 2.67 | 2.00 | 2.22 | 2.56 | **9.44** |
| DS-EN     | 8  | 2.75 | 1.88 | 2.12 | 2.50 | 9.25  |
| GPT-ZH    | 9  | 2.33 | 1.78 | 1.89 | 2.11 | 8.11  |
| DS-ZH     | 7  | 1.71 | 1.29 | 1.43 | 1.57 | **6.00** |

**DS-ZH (6.0)** is the third-lowest condition average in the project, and the DS-EN vs. DS-ZH gap (**3.25 points**) is the largest within-model language divergence in the project. All four DS-ZH dimensions score below 2, with ID (1.29) the lowest for any condition outside De'ang DS-ZH. EN conditions outperform ZH conditions for both models, consistent with the De'ang pattern and confirming EN–ZH narrative inversion as a recurring feature of communities with strong ZH-frame domestication pressure.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A1     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| A3     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-EN     | 3  | 1  | 1  | 2  | **7** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| C2     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| D1     | DS-ZH     | 2  | 1  | 2  | 2  | **7** |
| D2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D2     | GPT-EN    | 2  | 1  | 2  | 2  | **7** |
| D2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D3     | GPT-ZH    | 2  | 1  | 2  | 2  | **7** |
| D3     | GPT-EN    | 2  | 1  | 2  | 2  | **7** |
| D3     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D3     | DS-EN     | 2  | 1  | 2  | 2  | **7** |

**D3 — cross-condition floor (all four conditions):** All four conditions score ≤ 7, making D3 a complete cross-condition structural floor. ID collapses to 1 across all four conditions regardless of model or language — identity fluidity is the specific failure node on cultural practice depth prompts, a consistent dimensional profile not driven by ZH-frame suppression since it affects EN conditions equally.

**D2 — three-condition floor:** GPT-ZH (4), GPT-EN (7), and DS-ZH (4) all KB-gap on the historical narrative prompt. TB collapses to 1 in both total=4 cases.

**A1 — cross-model ZH floor:** Both GPT-ZH and DS-ZH score 5 with ID, CC, NR at 1 — replicating the cross-model ZH introduction-prompt pattern from De'ang and Hani/Akha.

**A2 · DS-ZH (total = 4):** DS-ZH passes the A2 probe yet produces a full floor-level narrative with all four dimensions at 1 — framing failure against accessible knowledge, the clearest knowledge-framing decoupling case in this community.

**C1 · GPT-ZH and C2 · DS-ZH (total = 7, CC = 1):** Cross-model ZH CC-suppression on identity-category prompts, now confirmed across eight communities.

---

## 4. Summary

Lahu presents a severe ossification profile dominated by ZH-frame suppression, with the largest within-model language gap in the project (3.25 points) and the third-lowest DS-ZH condition average.

**B3 complete cross-condition knowledge failure (G'ui Sha):** All four conditions fail the probe on Lahu's pan-community cosmological concept — the third instance of a complete cross-model, cross-language knowledge failure on a foundational cultural node. Together with Jingpo D1 and De'ang D2, this establishes a cross-community pattern of cosmological and religious knowledge gaps that are immune to model origin and language condition, pointing to systematic underrepresentation of indigenous cosmological systems in LLM training data.

**A2 structural inversion:** Three of four conditions deny Lahu mutual intelligibility, with DS-ZH as the sole passing condition. DS-ZH still KB-gaps on A2 (total = 4), confirming framing failure even when knowledge is accessible. The inversion points to a specific EN and GPT training data gap rather than a ZH-frame effect.

**DS-ZH (6.0) and 3.25-point within-model gap:** The largest within-model language divergence in the project, driven by ZH-frame domestication suppressing all four narrative dimensions in DS-ZH. ID (1.29) and CC (1.43) are the lowest dimension averages for any condition with a Chinese *minzu* counterpart.

**D3 cross-condition ID collapse:** All four conditions show ID = 1 on the cultural practice depth prompt, indicating that identity fluidity in cultural practice contexts is a structural representational ceiling for Lahu independent of model or language — distinct from the ZH-frame failures above and not correctable through language-condition changes alone.
