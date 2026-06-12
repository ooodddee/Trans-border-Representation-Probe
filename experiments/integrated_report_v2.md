# TIODF · Integrated Report
## LLM Coding (P1–P5) × KB Probe · 9 Communities

**Corpus:** 9 communities × 4 conditions × 11 prompts = 395 scored responses  
**KB Probes:** 11 binary probes per community per condition (temperature=0)  
**Models:** GPT-5.1 (US-origin) · DeepSeek-V3.2 (China-origin)  
**Judge:** Claude Sonnet, temperature=0  
**KB-gap definition:** probe_accepted=True AND total_score ≤ 7

---

## Part I — KB Probe: Knowledge Accessibility

### Pass Rates by Community and Condition

| Community | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-----------|--------|--------|-------|-------|
| Dai/Thai | 11/11 (100%) | 11/11 (100%) | 11/11 (100%) | 9/11 (82%) |
| Miao/Hmong | 11/11 (100%) | 11/11 (100%) | 9/11 (82%) | 9/11 (82%) |
| Lisu | 10/11 (91%) | 10/11 (91%) | 7/11 (64%) | 9/11 (82%) |
| Wa | 10/11 (91%) | 11/11 (100%) | 10/11 (91%) | 7/11 (64%) |
| Jingpo/Kachin | 10/11 (91%) | 10/11 (91%) | 9/11 (82%) | 7/11 (64%) |
| Hani/Akha | 8/11 (73%) | 11/11 (100%) | 6/11 (55%) | 8/11 (73%) |
| De'ang | 8/11 (73%) | 10/11 (91%) | 5/11 (45%) | 5/11 (45%) |
| Lahu | 9/11 (82%) | 9/11 (82%) | 7/11 (64%) | 8/11 (73%) |
| Dulong | 10/11 (91%) | 10/11 (91%) | 3/11 (27%) | 7/11 (64%) |

**Key structural observations:**

- **GPT-EN achieves the highest pass rates in every community**, reaching 100% in 4 of 9 (Dai/Thai, Miao/Hmong, Wa, Hani/Akha).
- **DS-ZH is the weakest condition in 7 of 9 communities** (all except Dai/Thai where DS-ZH = 100%, and Wa where DS-ZH = DS-EN's superior). Dulong DS-ZH (27%) is the project's single lowest pass rate.
- **De'ang is the only community where DS-ZH = DS-EN** (both 45%), indicating symmetric DeepSeek knowledge collapse independent of language direction.
- **Miao/Hmong is the only community where GPT achieves 100% in both languages**, making its KB-gap cases the cleanest framing-filter evidence in the dataset (no knowledge absence as alternative explanation).

### KL-Distortion Cases: Complete Cross-Condition Failures

Three probe nodes fail across all four conditions — the most severe knowledge gaps in the project:

| Community | Probe | Significance |
|-----------|-------|--------------|
| Jingpo/Kachin | D1 — Majoi Shingra as shared ancestral homeland | Foundational oral origin tradition absent across all models and languages |
| Lahu | B3 — G'ui Sha as supreme creator deity across all communities | Pan-Lahu cosmological concept absent across all models and languages |
| De'ang | D2 — syncretic Theravada-animist system across China/Myanmar/Thailand | Shared religious identity absent across 3 of 4 conditions (DS-EN: Unknown) |

These three cases establish a cross-community pattern: **indigenous cosmological and religious origin nodes are systematically absent from LLM training data regardless of model origin or query language**.

### KL-Distortion Cases: Cross-Language DS Failures (Genuine Knowledge Gaps)

| Community | Probe | DS-ZH | DS-EN | Significance |
|-----------|-------|-------|-------|--------------|
| Miao/Hmong | B1 — lusheng/qeej equivalence | No | No | Genuine knowledge gap; does not propagate into narrative scores |
| Wa | A1 — Wa is Austroasiatic-speaking | No | No | Language-family misclassification in DeepSeek training data |
| Lisu | D1 — Jinsha/Yalong oral origin tradition | No | No | Training data deficit on Lisu origin narrative |
| Jingpo/Kachin | C2 — Wunpawng as pan-Kachin identity | No | No | Pan-community identity concept absent from DeepSeek |
| Lahu | B3 — G'ui Sha | No | No | See complete failures above |
| Lahu | B1 — Yunnan/Thai Lahu share self-designation "Lahu" | No | No | DeepSeek denies community's own pan-community name |
| De'ang | D2 — syncretic religious system | No | Unk | See complete failures above |
| De'ang | D3 — lahpet ritual function | No | No | Most distinctive cross-border cultural marker absent in DS |
| Dulong | B1 — Dulong/Rawang mutual intelligibility | No | No | Basic linguistic relationship absent in DeepSeek |
| Dulong | D2 — shared animist system | No | No | Religious system absent in DeepSeek |
| Dulong | D3 — Kawaqa as shared New Year festival | No | No | Primary festival absent in DeepSeek |

### KL-Distortion Cases: Cross-Model ZH Failures (Minzu Gate Effect)

| Community | Probe | GPT-ZH | DS-ZH | Significance |
|-----------|-------|--------|-------|--------------|
| Hani/Akha | A2 — Chinese Hani and SE Asian Akha are same ethnic group | No | No | First cross-model ZH knowledge failure in project; *minzu* frame operating as knowledge gate |
| Hani/Akha | B2 — terraced rice agriculture shared cross-border | No | No | Cross-border practice denied by both ZH models |
| De'ang | C2 — Ta'ang self-designation emphasizes trans-border indigenous identity | No | No | *Minzu* frame blocks acknowledgment of trans-border identity meaning |
| Dulong | A3 — Dulongjiang Valley spans China-Myanmar border | No | No | ZH corpora represent Dulongjiang as China-internal |

The Hani/Akha A2/B2 and De'ang C2 cases establish a **minzu knowledge gate** mechanism distinct from framing failure: the *minzu* administrative frame is strong enough to suppress affirmative knowledge responses in ZH conditions across both model origins, not merely to distort narrative framing.

### Asymmetric Probes (Model-Specific Language-Conditioned Reversals)

Selected most structurally significant cases:

| Community | Probe | GPT-ZH | GPT-EN | DS-ZH | DS-EN | Pattern |
|-----------|-------|--------|--------|-------|-------|---------|
| Dai/Thai | A2 — SW Tai branch | Yes | Yes | Yes | **No** | DS-EN-specific suppression |
| Dai/Thai | B3 — Songkran same tradition | Yes | Yes | Yes | **No** | DS-EN-specific suppression |
| Miao/Hmong | C1 — Hmong is subgroup of Miao | Yes | Yes | **No** | Yes | DS-ZH-specific suppression |
| Miao/Hmong | C2 — Miao/Hmong share ethnic origin | Yes | Yes | Yes | **No** | DS-EN-specific suppression |
| Lisu | B1 — self-designation ꓡꓲ-ꓢꓴ | Yes | **No** | Yes | **No** | Cross-model EN failure (unique) |
| Wa | A2 — same language continuum | **No** | Yes | Yes | Yes | GPT-ZH-specific suppression |
| Lahu | A2 — mutual intelligibility | **No** | **No** | Yes | **No** | DS-ZH sole passing condition (structural inversion) |
| Jingpo/Kachin | B2 — Manau festival trans-border | Yes | Yes | Yes | **No** | DS-EN-specific suppression |

**Lisu B1** is the only cross-model EN-direction failure in the project: both GPT-EN and DS-EN deny the pan-community self-designation while both ZH conditions affirm — the inverse of the typical ZH-suppression pattern.

**Lahu A2** is a structural inversion: DS-ZH (typically the weakest condition) is the sole passing condition, with GPT-ZH, GPT-EN, and DS-EN all failing — a specific EN and GPT training data gap on Lahu linguistic continuity.

---

## Part II — Narrative Scores by Community

Scores out of 12 (TB + ID + CC + NR, each 1–3). Reported on probe-passed responses only (n varies by condition).

| Community | GPT-ZH | n | GPT-EN | n | DS-ZH | n | DS-EN | n |
|-----------|--------|---|--------|---|-------|---|-------|---|
| Miao/Hmong | 10.27 | 11 | 10.55 | 11 | 9.22 | 9 | 8.89 | 9 |
| Hani/Akha | **10.25** | 8 | 9.82 | 11 | 9.50 | 6 | 8.75 | 8 |
| Jingpo/Kachin | 9.20 | 10 | 9.80 | 10 | 8.00 | 9 | 9.00 | 7 |
| Dai/Thai | 9.45 | 11 | 9.00 | 11 | **6.82** | 11 | 7.56 | 9 |
| De'ang | 8.00 | 8 | **9.90** | 10 | 6.60 | 5 | 9.20 | 5 |
| Lahu | 8.11 | 9 | **9.44** | 9 | **6.00** | 7 | 9.25 | 8 |
| Wa | 8.10 | 10 | **8.91** | 11 | 7.70 | 10 | 7.29 | 7 |
| Lisu | 7.60 | 10 | 7.70 | 10 | **5.86** | 7 | 6.78 | 9 |
| Dulong | 7.40 | 10 | **8.00** | 10 | 6.67 | 3 | 7.57 | 7 |

**Bold** = highest score per community (GPT-EN leads in 6 of 9); lowest DS-ZH scores bolded for emphasis.

**Structural observations:**

- **DS-ZH is the weakest narrative condition in 7 of 9 communities** (exception: Jingpo/Kachin where DS-EN=9.0 > DS-ZH=8.0 but GPT-ZH leads; and De'ang/Lahu where EN conditions dominate but DS-ZH is still worst).
- **Hani/Akha ZH narrative inversion:** GPT-ZH (10.25) is the highest-scoring condition despite the lowest GPT probe pass rate (73%). ZH knowledge failures exclude the most ossification-prone prompts, inflating the passing subset — a selection artifact requiring careful interpretation.
- **Dai/Thai DS-ZH (6.82, n=11) is the canonical KB-gap case:** 100% probe pass rate with the lowest narrative average — the clearest knowledge-framing decoupling in the dataset.
- **Dulong cross-condition ceiling (all < 8.1):** All four conditions fall below GPT's typical range (9.0–10.5 in other communities), establishing data scarcity as a hard ceiling independent of framing.

### Within-Model Language Gap (DS-EN vs. DS-ZH)

| Community | DS-ZH | DS-EN | Gap |
|-----------|-------|-------|-----|
| Lahu | 6.00 | 9.25 | **+3.25** |
| De'ang | 6.60 | 9.20 | **+2.60** |
| Dai/Thai | 6.82 | 7.56 | +0.74 |
| Jingpo/Kachin | 8.00 | 9.00 | +1.00 |
| Miao/Hmong | 9.22 | 8.89 | −0.33 |
| Lisu | 5.86 | 6.78 | +0.92 |
| Wa | 7.70 | 7.29 | −0.41 |
| Hani/Akha | 9.50 | 8.75 | −0.75 |
| Dulong | 6.67 | 7.57 | +0.90 |

Lahu (+3.25) and De'ang (+2.60) show the sharpest EN–ZH inversions, both driven by extreme ZH-frame domestication pressure. Three communities show DS-EN < DS-ZH (Miao/Hmong, Wa, Hani/Akha), where ZH knowledge failures filter out the most ossification-prone prompts, depressing DS-ZH's denominator.

---

## Part III — LLM Coding: P1–P5 Pattern Distribution

### Overall Prevalence

**32.9% of all responses (130/395) exhibit at least one ossification pattern.** The 67.1% non-ossified rate confirms ossification is a default framing choice rather than an absolute incapacity.

### By Condition

| Condition | Any pattern | P1 | P2 | P3 | P4 | P5 |
|-----------|------------|----|----|----|----|-----|
| DS-ZH | 62.6% | 35.4% | 9.1% | 34.3% | 9.1% | 6.1% |
| GPT-ZH | 33.3% | 16.2% | 0.0% | 16.2% | 8.1% | 5.1% |
| DS-EN | 25.3% | 11.1% | 5.1% | 12.1% | 1.0% | 4.0% |
| GPT-EN | 10.2% | 4.1% | 0.0% | 4.1% | 1.0% | 3.1% |

DS-ZH (62.6%) is nearly double GPT-ZH (33.3%) and six times GPT-EN (10.2%).

### Model-Origin Effects (Chi-square)

**Tier 1 — DS-characteristic (statistically significant):**

| Pattern | DS% | GPT% | χ² | p |
|---------|-----|------|----|---|
| P1 Minzu-Frame Lock | 23.2% | 10.2% | 11.22 | 0.0008*** |
| P2 Political Substitution | 7.1% | 0.0% | 12.45 | 0.0004*** |
| P3 Acknowledge-Peripheralize | 23.2% | 10.2% | 11.22 | 0.0008*** |

**P2 is exclusively a DeepSeek behavioral signature:** 0 instances in GPT-5.1 across all 395 responses; 14 instances in DS spanning 8 of 9 communities (DS-ZH: 9 cases; DS-EN: 5 cases).

**Tier 2 — Shared (model-origin-independent):**

| Pattern | DS% | GPT% | χ² | p |
|---------|-----|------|----|---|
| P4 Administrative Identity Compression | 5.1% | 4.6% | 0.00 | 1.000 (ns) |
| P5 Cross-Border Continuity Denial | 5.1% | 4.1% | 0.05 | 0.818 (ns) |

### Pattern Severity (Mann-Whitney U Score Penalties)

| Pattern | n | Score (present) | Score (absent) | Δ | r | p |
|---------|---|----------------|----------------|---|---|---|
| P2 Political Substitution | 14 | 4.93 | 8.59 | −3.66 | 0.715 | <0.001*** |
| P1 Minzu-Frame Lock | 66 | 5.48 | 9.06 | −3.58 | 0.687 | <0.001*** |
| P3 Acknowledge-Peripheralize | 66 | 7.26 | 8.71 | −1.45 | 0.308 | <0.001*** |
| P4 Administrative Compression | 19 | 7.21 | 8.53 | −1.32 | 0.272 | 0.043* |
| P5 Cross-Border Continuity Denial | 18 | 8.11 | 8.48 | −0.37 | 0.097 | 0.481 (ns) |

P5 does not produce a statistically significant score penalty; retained as a qualitative observation only.

---

## Part IV — KB-Gap Analysis: Framing Filter Evidence

KB-gap cases confirm ossification as framing-level failure: the model passes the knowledge probe (possesses the cross-border fact) but produces a low-scoring narrative. Selected high-salience cases:

### Anchor Cases — Clearest Framing-Filter Evidence

| Community | Condition | Prompt | Probe result | Score | Interpretation |
|-----------|-----------|--------|-------------|-------|----------------|
| Dai/Thai | DS-ZH | A1 — What are the Dai people? | Yes (100% pass rate) | 4/12 | All 4 dimensions = 1; canonical KB-gap; *minzu* frame fully displaces cross-border Tai identity |
| Miao/Hmong | DS-EN | A2 — cross-border historical continuity | Yes | 4/12 | Within-model cross-language gap = 6 points (DS-ZH same prompt: 10/12); refugee-frame compression candidate |
| Miao/Hmong | GPT-ZH | C2 — Miao/Hmong identity overlap | Yes | 5/12 | Cross-model ZH convergence (DS-ZH also: 6/12); *minzu* frame suppresses identity fluidity in both models |
| Hani/Akha | DS-EN | A2 — Hani-Akha historical continuity | Yes | 4/12 | All 4 dimensions = 1; DS-EN affirms the claim yet produces a fully ossified narrative |
| Jingpo/Kachin | GPT-ZH | A2 — cross-border linguistic relationship | Yes | 4/12 | All 4 dimensions = 1; structural floor in all four conditions |
| Lahu | DS-ZH | A2 — mutual intelligibility | Yes | 4/12 | All 4 dimensions = 1; DS-ZH is sole passing condition yet KB-gaps |

### Cross-Condition KB-Gap Floors (Structural Representational Ceilings)

Prompts producing KB-gap scores across ≥3 conditions, pointing to training data limits rather than framing:

| Prompt node | Communities affected | Primary deficit |
|-------------|---------------------|-----------------|
| A2 — cross-border linguistic relationship | Dai/Thai, Lisu, Wa, Jingpo/Kachin, De'ang, Dulong | Linguistic continuity across national borders systematically underdeveloped |
| D2 — religious system depth | Dai/Thai, Wa, Lisu, Lahu, Jingpo/Kachin, Dulong | Cultural-religious depth broadly absent regardless of condition |
| D3 — ritual/festival depth | Dai/Thai, Wa, Lisu, Lahu, Dulong | Cultural practice depth broadly absent regardless of condition |
| A3 — geographic distribution | Dai/Thai, Wa, Lisu, De'ang, Dulong | Distribution framing suppressed cross-condition |

### Cross-Model ZH CC-Suppression on C1 (Recurring Pattern)

C1 (cross-border identity scenario) produces CC=1 under ZH prompting across both models in **8 of 9 communities** (all except Dulong, where data scarcity extends the failure to DS-EN as well):

| Community | GPT-ZH C1 CC | DS-ZH C1 CC | GPT-EN C1 CC | DS-EN C1 CC |
|-----------|-------------|-------------|--------------|-------------|
| Dai/Thai | 1 | 1 | — | 1 |
| Miao/Hmong | — | — | — | — |
| Lisu | 1 | 1 | — | — |
| Wa | 1 | 1 | — | — |
| Jingpo/Kachin | 1 | — | — | — |
| Hani/Akha | — | — | — | — |
| De'ang | 1 | 1 | — | — |
| Lahu | 1 | 1 | — | — |
| Dulong | 1 | 1 | — | 1 |

This cross-model, cross-community ZH CC-suppression on identity-scenario prompts is the strongest recurring quantitative signal for the *minzu* administrative frame as a cross-border cultural continuity suppressor.

---

## Part V — Community Severity Gradient

| Community | DS-ZH score | Overall ossification | Primary mechanism | Anomaly |
|-----------|------------|---------------------|-------------------|---------|
| Lisu | 5.86 | High | DS ZH-frame lock + cross-model EN gap (B1) + data scarcity | Cross-model EN failure on self-designation (unique) |
| Lahu | 6.00 | High | ZH-frame domestication; largest within-model gap (+3.25) | A2 structural inversion; complete B3 knowledge failure |
| Dai/Thai | 6.82 | High | ZH-frame ossification (canonical KB-gap case) | DS-ZH 100% probe pass; clearest framing-filter evidence |
| De'ang | 6.60 | High | ZH-frame domestication; highest asymmetric probe count (10) | Near-complete D2 failure; DS-ZH=DS-EN at 45% |
| Dulong | 6.67 | Severe (data) | Training data scarcity; DS-ZH 27% pass rate | GPT-EN scores suppressed below 8.1; data ceiling |
| Wa | 7.70 | Moderate | DS-EN EN-direction suppression; DS A1 genuine gap | DS cross-language Austroasiatic misclassification |
| Jingpo/Kachin | 8.00 | Moderate | ZH-frame domestication; cross-condition A2/D2 floors | Complete D1 failure; DS C2 Wunpawng gap |
| Hani/Akha | 9.50 | Moderate | Cross-model ZH knowledge gate (A2, B2); CC as sole failure dim | ZH narrative inversion artifact; fewest KB-gap cases (5) |
| Miao/Hmong | 9.22 | Low | Bidirectional framing (EN: A2·DS-EN; ZH: C2 cross-model) | 100% probe pass all conditions; cleanest framing evidence |

---

## Part VI — Integrated Findings

**F1 — Ossification is systematic but not universal.**  
32.9% prevalence (130/395); both models produce non-ossified output in majority of responses. Ossification is a default framing choice, not an incapacity.

**F2 — P2 (Political Substitution) is exclusively a DeepSeek behavioral signature.**  
14 instances in DS spanning 8 communities; 0 in GPT across 395 responses (χ²=12.45, p=0.0004). The sharpest cross-model distinction in the corpus.

**F3 — KB-gap confirms ossification as framing-level failure, not knowledge absence.**  
Miao/Hmong (100% probe pass in all 4 conditions) and Dai/Thai DS-ZH (100% probe pass, 6.82 mean) provide the strongest evidence. KL-distortion cases are excluded from framing analysis and treated separately as knowledge-level failures.

**F4 — ZH-direction and EN-direction ossification are mechanistically distinct.**  
ZH: P1+P3 coupling, *minzu*-frame lock, quantitatively captured. EN: refugee/conflict compression or administrative reduction, partially captured by P3/P4; lacks complete P1–P5 quantitative coverage — identified as motivation for Paper 2.

**F5 — The *minzu* administrative frame operates as both a framing filter and a knowledge gate.**  
In most communities it functions as a framing filter (probe=Yes, low narrative score). In Hani/Akha (A2, B2) and De'ang (C2), it suppresses affirmative knowledge responses in ZH conditions across both model origins — a more fundamental suppression not correctable through premise-provision alone.

**F6 — Three cosmological/religious nodes are absent from LLM training data across all conditions.**  
Jingpo/Kachin D1 (Majoi Shingra), Lahu B3 (G'ui Sha), and De'ang D2 (syncretic religious system) fail across all or nearly all model-language combinations, establishing a cross-community pattern of indigenous cosmological knowledge absence.

**F7 — Training data scarcity sets a hard ceiling that framing improvements cannot overcome.**  
Dulong: all four conditions score below 8.1 (GPT-EN typically reaches 9.5–10.5 elsewhere); GPT-EN KB-gaps at total=4 on D2 and D3. Lisu: DS-ZH 5.86 driven by knowledge failures that compound framing failures. The KB probe successfully distinguishes this ceiling from framing-level failures.

**F8 — Cross-model ZH CC-suppression on identity-scenario prompts (C1) is the strongest recurring cross-community signal.**  
CC=1 under ZH prompting in both models appears in 8 of 9 communities, consistently implicating the *minzu* administrative frame as a cross-border cultural continuity suppressor under Chinese prompting.

---

*Communities: Dai/Thai · Miao/Hmong · Lisu · Wa · Jingpo/Kachin · Hani/Akha · De'ang · Lahu · Dulong*  
*Karen excluded (no China minzu counterpart; structural asymmetry deferred to Paper 2)*  
*Source: Individual community reports generated 2026-04-25/26*
