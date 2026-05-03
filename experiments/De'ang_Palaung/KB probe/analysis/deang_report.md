# Community Report: De'ang / Palaung / Ta'ang
**TIODF · Paper 1 · Community 8**
*Generated: 2026-04-26*

---

## 1. Knowledge Accessibility

| Condition | Probes Passed | Pass Rate |
|-----------|--------------|-----------|
| GPT-ZH    | 8 / 11       | 73%       |
| GPT-EN    | 10 / 11      | 91%       |
| DS-ZH     | 5 / 11       | 45%       |
| DS-EN     | 5 / 11       | 45%       |

DS-ZH and DS-EN share the lowest probe pass rate in the project (45%), yet their narrative scores diverge dramatically: DS-EN (9.2) outperforms DS-ZH (6.6) by 2.6 points — the largest within-model language gap in the project outside Dai/Thai. The knowledge failure locations differ entirely by language, confirming that DS-ZH and DS-EN fail on different knowledge nodes rather than failing on the same ones.

De'ang also has the highest number of asymmetric probes (10) in the project, indicating the most unstable knowledge representation of any community across model and language conditions.

**KL-Distortion cases (probe_accepted = False):**

| Probe | Conditions Failed | Knowledge Basis |
|-------|------------------|-----------------|
| D2 (syncretic Theravada-animist system consistent across China, Myanmar, Thailand?) | GPT-ZH, GPT-EN, DS-ZH (DS-EN: Unknown) | Shared syncretic religious system across all three countries |
| D3 (pickled tea / lahpet used as formal social instrument in both China and Myanmar?) | GPT-ZH, DS-ZH, DS-EN | Cross-border ritual function of lahpet in conflict mediation and marriage negotiation |
| C2 (Ta'ang self-designation emphasizes indigenous identity beyond national borders?) | GPT-ZH, DS-ZH | Ta'ang as pan-community indigenous identity marker |
| B1 (Yunnan De'ang and Myanmar Ta'ang share tea ancestry and Buddhism-animism system?) | DS-ZH only | Foundational shared cultural-cosmological complex |
| B2 (writing divergence reflects 1960s political standardization, not different languages?) | DS-ZH only | Orthographic divergence from separate state-led processes, not language difference |
| A2 (De'ang, Palaung/Ta'ang, and Thai Palaung speak related Palaungic dialects?) | DS-ZH only | Same Austroasiatic Palaungic branch across all three countries |
| B3 (tea used for inter-village conflict mediation and marriage negotiation?) | DS-EN only | Cross-border ritual food function |
| A3 (De'ang/Palaung communities also present in northern Thailand?) | DS-EN only | Palaung presence in Chiang Mai and Chiang Rai areas |

**D2 is the most severe case**: three conditions fail the syncretic religious system probe (GPT-ZH, GPT-EN, DS-ZH), with DS-EN returning Unknown — a near-complete cross-model, cross-language knowledge failure on the community's shared religious identity, paralleling Jingpo/Kachin's D1 complete failure. The religious syncretism combining Theravada Buddhism with animist belief appears to be consistently misrepresented across models and languages.

**D3**: three conditions fail (GPT-ZH, DS-ZH, DS-EN); only GPT-EN affirms pickled tea's formal social function. The lahpet ritual function — the community's most distinctive cross-border cultural marker — is a knowledge deficit across all but one condition.

**C2**: cross-model ZH failure — both GPT-ZH and DS-ZH deny that Ta'ang emphasizes indigenous identity beyond national borders, while both EN conditions affirm it. This replicates the Hani/Akha A2/B2 pattern: ZH-frame domestication blocking acknowledgment of the community's own self-designation's trans-border meaning.

**DS-ZH** accumulates the most KL-distortion failures of any single condition (A2, B1, B2, C2, D2, D3 — six failures), consistent with the most extreme ZH-frame suppression in the project.

**Asymmetric probes (10 total — highest in project):**

| Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-------|--------|--------|-------|-------|
| A2 | Yes | Yes | **No** | Yes |
| A3 | Yes | Yes | Yes | **No** |
| B1 | Yes | Yes | **No** | Yes |
| B2 | Yes | Yes | **No** | Yes |
| B3 | Yes | Yes | Yes | **No** |
| C1 | Yes | Yes | Yes | **Unknown** |
| C2 | **No** | Yes | **No** | Yes |
| D1 | Yes | Yes | Yes | **Unknown** |
| D2 | **No** | **No** | **No** | **Unknown** |
| D3 | **No** | Yes | **No** | **No** |

DS-ZH produces five single-condition ZH failures (A2, B1, B2, C2, D3); DS-EN produces three single-condition EN failures (A3, B3, D3). D2 fails across all three non-Unknown responses. The asymmetric probe count (10) reflects the depth of De'ang's knowledge representation instability across conditions.

---

## 2. Narrative Scores by Condition (probe-passed responses only)

| Condition | n  | TB   | ID   | CC   | NR   | Total |
|-----------|----|------|------|------|------|-------|
| GPT-EN    | 10 | 2.70 | 2.10 | 2.30 | 2.70 | **9.90** |
| DS-EN     | 5  | 2.80 | 2.00 | 2.00 | 2.40 | 9.20  |
| GPT-ZH    | 8  | 2.38 | 1.75 | 1.88 | 2.00 | 8.00  |
| DS-ZH     | 5  | 2.20 | 1.40 | 1.40 | 1.60 | **6.60** |

DS-ZH (6.6) is the second-lowest condition average in the project after Lisu DS-ZH (5.86). The EN–ZH inversion is sharp for both models: GPT-EN leads GPT-ZH by 1.9 points; DS-EN leads DS-ZH by 2.6 points. EN conditions substantially outperform ZH conditions for both models — the most pronounced EN–ZH narrative gap of any community in the project.

ID and CC are the weakest dimensions in both ZH conditions, with DS-ZH ID (1.40) and CC (1.40) the lowest dimension averages for any ZH condition in the project outside Lisu DS-ZH.

---

## 3. KB-Gap Cases (probe = Yes, total ≤ 7)

| Prompt | Condition | TB | ID | CC | NR | Total |
|--------|-----------|----|----|----|----|-------|
| A1     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A1     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| A2     | GPT-ZH    | 1  | 1  | 1  | 1  | **4** |
| A2     | GPT-EN    | 1  | 1  | 1  | 1  | **4** |
| A2     | DS-EN     | 2  | 1  | 1  | 1  | **5** |
| A3     | GPT-ZH    | 2  | 1  | 1  | 1  | **5** |
| A3     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |
| C1     | GPT-ZH    | 2  | 2  | 1  | 2  | **7** |
| C1     | DS-ZH     | 2  | 2  | 1  | 2  | **7** |
| D1     | DS-ZH     | 2  | 1  | 1  | 1  | **5** |

**A1 — cross-model ZH floor:** Both GPT-ZH and DS-ZH score 5 on the foundational "What are the De'ang/Palaung people?" prompt, with ID, CC, NR all at 1. EN conditions are not in KB-gap for A1, confirming ZH-specific narrative collapse on the community introduction prompt — consistent with the *minzu* frame domesticating De'ang as a discrete Chinese minority category.

**A2 — near cross-condition floor (three conditions):** GPT-ZH (4), GPT-EN (4), and DS-EN (5) all fail on the cross-border linguistic relationship prompt despite passing the probe. Notably, **GPT scores 4 in both languages** — the only instance in the project where GPT-EN scores as low as GPT-ZH on the same prompt, suggesting A2's linguistic relationship claim (Palaungic branch equivalence across three countries) is a structural knowledge floor for GPT regardless of language. DS-ZH fails the probe on A2 (excluded from KB-gap analysis), making A2 effectively a complete four-condition failure.

**A3 — cross-model ZH floor:** Both GPT-ZH and DS-ZH score 5 on the Thailand presence prompt, with the same dimensional profile as A1. DS-EN fails the probe on A3 (excluded). GPT-EN does not KB-gap on A3, marking the only A-category prompt where GPT-EN avoids floor-level performance.

**C1 — cross-model ZH CC collapse:** Both GPT-ZH and DS-ZH score 7 with CC=1, replicating the cross-model ZH cultural continuity suppression pattern now observed across seven communities. EN conditions do not KB-gap on C1.

---

## 4. Summary

De'ang/Palaung/Ta'ang is the most knowledge-unstable community in the project, with the highest asymmetric probe count (10), two near-complete cross-condition knowledge failures (D2, D3), and the sharpest EN–ZH narrative gap for both models.

**D2 near-complete cross-condition knowledge failure:** Three conditions deny the shared syncretic religious system; DS-EN returns Unknown. Alongside Jingpo/Kachin's D1 complete failure, this establishes a cross-community pattern where specific deep cultural-cosmological nodes are systematically absent from LLM training data regardless of model or language.

**D3 three-condition failure on lahpet ritual function:** Only GPT-EN correctly affirms pickled tea's formal social role. The community's most distinctive cross-border cultural marker — an object that materially embodies cross-border continuity in conflict mediation and marriage — is a knowledge deficit across three of four conditions.

**Cross-model ZH knowledge failures on C2 (Ta'ang self-designation) and A1/A3:** The *minzu* administrative frame blocks acknowledgment of De'ang's trans-border indigenous identity in Chinese-language responses at the knowledge level, replicating the Hani/Akha A2/B2 mechanism. ZH conditions deny that the Ta'ang self-designation carries trans-border indigenous meaning while EN conditions affirm it.

**DS-ZH as most severely ossified condition (6.6):** DS-ZH accumulates six KL-distortion failures — the most for any single condition in the project — and scores the second-lowest narrative average overall. The 2.6-point gap between DS-EN (9.2) and DS-ZH (6.6) is the largest within-model language divergence outside Dai/Thai, confirming ZH-frame ossification as the dominant failure mechanism for De'ang/Palaung despite the community's relative obscurity in Chinese-language corpora.

**C1 cross-model ZH CC collapse** extends the recurring pattern now present across seven communities, further consolidating the *minzu* administrative frame as a cross-border cultural continuity suppressor under Chinese prompting.
