# Community Report: Jingpo / Kachin
**TIODF · Paper 1 · Community 6**
*Generated: 2026-04-25*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 10 / 11      | 91%       |
| GPT-EN    | 10 / 11      | 91%       |
| DS-ZH     | 9 / 11       | 82%       |
| DS-EN     | 7 / 11       | 64%       |

GPT achieves 91% in both languages. DS-EN has the lowest pass rate (64%), but produces a higher narrative average (9.0) than DS-ZH (8.0, 82% pass rate) — indicating that DS-EN's knowledge failures are concentrated on specific nodes that, when excluded, leave a higher-scoring response subset.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| D1 (Majoi Shingra is shared ancestral homeland in Kachin oral tradition?) | All four conditions | Foundational oral origin tradition shared across all Kachin subgroups |
| C2 (Wunpawng is pan-Kachin umbrella identity including Chinese Jingpo?) | DS-ZH, DS-EN | Wunpawng (万邦): most widely used internal collective term for pan-Kachin identity |
| B2 (Manau festival is shared trans-border cultural ritual?) | DS-EN only | Observed across Myanmar, Yunnan, and global Kachin diaspora |
| D3 (Christianity is dominant religion among Kachin/Singpho across Myanmar and India?) | DS-EN only | Christianity became dominant through late 19th-century missionary work in Myanmar and India |

**D1 is the most severe knowledge gap in the project**: all four conditions deny that Majoi Shingra is the shared ancestral homeland in Kachin oral tradition — a complete cross-model, cross-language knowledge failure on the community's foundational origin narrative. This is distinct from framing failure; the knowledge node is absent across all conditions.

**C2 (Wunpawng)** fails in both DS conditions (ZH and EN), indicating a genuine cross-language knowledge gap in DeepSeek on the pan-Kachin collective identity concept — a term that directly encodes the cross-border unity of the Jingpo/Kachin community.

**B2 and D3** are DS-EN-specific failures, consistent with the EN-direction suppression pattern seen in prior communities (Wa B1/B2, Lisu B1, Karen B2).

**Asymmetric probes:**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| B2 | Yes | Yes | Yes | **No** |
| D3 | Yes | Yes | Yes | **No** |

Both asymmetric cases are DS-EN-specific — consistent with DeepSeek's EN-condition suppression of cross-border cultural continuity claims. C2 and D1 are not listed as asymmetric because their failures span multiple conditions rather than reversing by language direction.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 10 | 2.60 | 2.40 | 2.20 | 2.60 | **9.80** |
| GPT-ZH    | 10 | 2.50 | 2.30 | 2.00 | 2.40 | 9.20  |
| DS-EN     | 7  | 2.57 | 2.14 | 2.00 | 2.29 | 9.00  |
| DS-ZH     | 9  | 2.22 | 2.00 | 1.89 | 1.89 | **8.00** |

Scores are the second highest in the project after Karen, with all conditions above 8. The GPT–DeepSeek gap is moderate (~0.2–1.8 points). DS-ZH (8.0) is the weakest narrative condition despite having a higher probe pass rate than DS-EN — confirming knowledge-framing decoupling in the ZH condition. CC is the weakest dimension across all conditions, suggesting cultural continuity framing is the primary representational constraint regardless of model or language.

**DS-EN (9.0) outperforms DS-ZH (8.0)** despite DS-EN having fewer probe-passed responses (n=7 vs. n=9). Jingpo is a recognized Chinese *minzu*, so ZH-frame domestication is the likely driver of DS-ZH's relative underperformance — the *minzu* administrative frame suppresses cross-border Kachin framing in Chinese-language narratives.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| A2     | GPT-EN    | 1  | 1  | 2  | 1  | **5** |
| A2     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A2     | DS-EN     | 2  | 1  | 2  | 1  | **6** |
| B2     | DS-ZH     | 2  | 1  | 2  | 1  | **6** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| D2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| D2     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| D2     | DS-ZH     | 1  | 1  | 1  | 1  | **4** |
| D2     | DS-EN     | 2  | 1  | 1  | 1  | **5** |

**A2 — cross-condition floor (all four conditions):** All four conditions score ≤ 6 on the cross-border linguistic relationship prompt despite passing the probe, with ID and NR consistently collapsing. Models can acknowledge the Jingpo/Kachin connection at the knowledge level but fail to frame it as a continuous cross-border linguistic community in narrative output.

**D2 — cross-condition floor (all four conditions):** All four conditions score 4–5 on historical origins and colonial border narrative. TB collapses to 1 in three of four conditions. This is the second cross-condition floor in this community and, together with A2, indicates that both cross-border linguistic framing and historical narrative depth are structural weak points across all models and languages.

**C1 · GPT-ZH (total = 7, CC = 1):** Cross-border identity scenario collapses on CC under Chinese prompting despite GPT-ZH achieving 91% probe pass rate. This replicates the cross-model ZH CC-suppression pattern on C-category prompts seen in Miao/Hmong, Lisu, and Wa — now appearing across six communities.

**B2 · DS-ZH (total = 6):** Manau festival framing suppressed under Chinese prompting despite DS-ZH passing the probe. DS-EN fails the probe on B2 (excluded from KB-gap), making B2 a complete DeepSeek failure across both conditions through different mechanisms — probe failure in EN, framing failure in ZH.

---

## 4. Summary

Jingpo/Kachin produces the second-highest overall scores in the project alongside Karen, with a moderate ossification profile. The defining features are:

**D1 complete cross-model knowledge gap (Majoi Shingra):** All four conditions fail the foundational oral origin tradition probe — the most comprehensive knowledge failure in the project, exceeding even Lisu's B1 cross-model EN failure. The Majoi Shingra origin narrative is absent from LLM training data across both models and both languages. This is a genuine knowledge deficit, not a framing failure.

**C2 cross-language DS knowledge gap (Wunpawng):** DeepSeek's failure to recognize Wunpawng as the pan-Kachin collective identity in both Chinese and English indicates that the concept bridging Chinese Jingpo and Myanmar Kachin identity is absent from DeepSeek's training data — a particularly consequential gap given that Wunpawng is the primary internal term for cross-border community unity.

**DS-ZH as weakest narrative condition:** DS-ZH (8.0) underperforms DS-EN (9.0) despite higher probe pass rates, consistent with *minzu* frame domestication suppressing cross-border Kachin framing in Chinese-language narratives — the same mechanism observed in Dai/Thai and Miao/Hmong.

**Cross-condition structural floors on A2 and D2:** Both prompts fail across all four conditions, indicating that cross-border linguistic framing and historical narrative depth are broadly underdeveloped for Jingpo/Kachin regardless of model or language.

**C1 ZH CC-suppression:** GPT-ZH's CC collapse on the cross-border identity scenario extends the cross-model ZH cultural continuity suppression pattern now observed across six communities, consistently implicating the *minzu* administrative frame as a cross-border framing constraint under Chinese prompting.
