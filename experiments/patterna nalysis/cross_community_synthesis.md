# Cross-Community Synthesis
**TIODF · Paper 1 · 9 Communities**
*Dai/Thai · Miao/Hmong · Hani/Akha · Lahu · Wa · Lisu · De'ang · Jingpo/Kachin · Dulong*

---

## 1. Condition-Level Score Summary

| Community     | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|---------------|--------|--------|-------|-------|
| Dai/Thai      | 9.45   | 9.00   | 6.82  | 7.56  |
| Miao/Hmong    | 10.27  | 10.55  | 9.22  | 8.89  |
| Hani/Akha     | 10.25  | 9.82   | 9.50  | 8.75  |
| Jingpo/Kachin | 9.20   | 9.80   | 8.00  | 9.00  |
| Wa            | 8.10   | 8.91   | 7.70  | 7.29  |
| Lisu          | 7.60   | 7.70   | 5.86  | 6.78  |
| De'ang        | 8.00   | 9.90   | 6.60  | 9.20  |
| Lahu          | 8.11   | 9.44   | 6.00  | 9.25  |
| Dulong        | 7.40   | 8.00   | 6.67  | 7.57  |

DS-ZH is the weakest condition in 7 of 9 communities. GPT-EN is the strongest or joint-strongest in 6 of 9. Hani/Akha is the exception where GPT-ZH leads (10.25) — a ZH gate artifact explained in Section 3.

---

## 2. Three Cross-Community Patterns

### Pattern 1 — *Minzu* Frame as Systematic CC/ID Suppressor (ZH-direction)

Cross-model ZH-specific CC collapse on identity-category prompts appears across 8 communities (all except Dulong where data scarcity extends the failure to DS-EN as well). The direct evidence for the *minzu* frame as causal mechanism: communities with a Chinese *minzu* counterpart consistently show lower ID and CC scores in ZH conditions than EN conditions. The mechanism is confirmed by the Jingpo and Dai/Thai cases where DS-ZH achieves high probe pass rates yet produces the lowest narrative scores — knowledge-framing decoupling in its clearest form.

### Pattern 2 — Complete Cross-Condition Knowledge Failure on Indigenous Cosmological Nodes

Three communities produce all-four-condition probe failures on foundational cultural-cosmological claims:

| Community     | Probe | Failed Node |
|---------------|-------|-------------|
| Jingpo/Kachin | D1    | Majoi Shingra ancestral homeland oral tradition |
| Lahu          | B3    | G'ui Sha as pan-community supreme creator deity |
| De'ang        | D2    | Shared Theravada-animist syncretic system across three countries |

Together with Dulong's A1 complete cross-condition KB-gap (introduction prompt floors all four conditions), these represent knowledge nodes absent from LLM training data regardless of model origin or query language — indigenous cosmological and origin-narrative knowledge that is systematically underrepresented in both Chinese and English corpora.

### Pattern 3 — EN-Direction Cross-Model Cultural Continuity Failure

Two communities show cross-model EN-specific failures where both GPT-EN and DS-EN deny a pan-community cultural marker while both ZH conditions affirm it:

| Community  | Probe | Failed Node |
|------------|-------|-------------|
| Lisu       | B1    | Pan-community self-designation ꓡꓲ-ꓢꓴ shared across all four countries |
| Miao/Hmong | A2    | EN-language framing collapse on cross-border historical continuity (consistent with refugee-frame compression) |

This is a distinct mechanism from ZH-frame ossification: EN-language corpora systematically underrepresent specific cross-border cultural markers relative to ZH corpora, producing a failure mode in the opposite language direction.

---

## 3. Ossification Severity Tiers

| Tier | Communities | Defining Features |
|------|-------------|-------------------|
| Moderate | Miao/Hmong, Jingpo/Kachin | High overall scores; ossification concentrated in specific knowledge nodes; GPT conditions near 9.5–10.5 |
| Moderate–High | Dai/Thai, Hani/Akha, Wa | Clear knowledge-framing decoupling; ZH-frame domestication confirmed; DS-ZH 6.8–9.5 |
| High | De'ang, Lahu | Largest within-model language gaps (2.6–3.25 pts); DS-ZH below 6.7; multiple ZH knowledge failures |
| Severe | Lisu, Dulong | Knowledge gap as primary driver alongside framing failure; DS-ZH pass rates at or below 27–64%; cross-condition floors on A-category prompts |

**Hani/Akha note:** GPT-ZH (10.25) leads all conditions due to the ZH knowledge gate effect — ZH probe failures exclude the most ossification-prone prompts, inflating the passing subset average. This is an artifact of the probe-exclusion design, not evidence of superior ZH framing.

---

## 4. Key Findings

**F1 — Ossification is cross-community and generalizable.** All 9 communities show measurable ossification across varying border configurations, *minzu* classification statuses, and geopolitical contexts.

**F2 — ZH-frame and EN-frame are two opposing mechanisms.** ZH-language prompts compress communities into *minzu* administrative categories, suppressing cross-border continuity; EN-language prompts either apply conflict/refugee frames (Miao/Hmong) or erase cross-border dimensions through data scarcity. Both directions produce the same structural outcome: severed trans-border identity.

**F3 — Knowledge accessibility does not guarantee narrative quality.** Dai/Thai DS-ZH achieves 100% probe pass rate yet scores 6.82/12 — the clearest evidence that ossification is a framing-level failure, not a knowledge-accessibility failure. This finding replicates across Lahu DS-ZH (A2: probe passed, total = 4) and De'ang DS-ZH.

**F4 — Indigenous cosmological knowledge is systematically absent.** Three complete cross-condition failures (Jingpo D1, Lahu B3, De'ang D2) and Dulong's A1 floor establish that indigenous origin narratives and cosmological systems are not representational failures of framing — they are knowledge gaps immune to language-condition or model-origin variation.

**F5 — Training data coverage is a hard ceiling.** Dulong's GPT-EN advantage disappears entirely (GPT-EN D2/D3 = 4/12), demonstrating that below a minimum corpus threshold, framing-level improvements cannot compensate for data absence. This sets a boundary on what ossification-mitigation interventions can achieve without changes to training data.
