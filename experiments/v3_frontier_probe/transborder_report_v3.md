# Trans-border Representation Probe v3
## How Frontier LLMs Represent the Dai-Thai Community



## Abstract

This study examines how frontier-tier LLMs represent the Dai-Thai community—a trans-border population spanning China, Thailand, Myanmar, Laos, and Vietnam whose identity resists nation-state categorization. Comparing GPT-5.1 (US) and DeepSeek-V3.2 (China) across 11 bilingual prompts (n=44), I apply a 5-dimension manual coding rubric and multilingual embedding analysis.

Two methods yield partially divergent conclusions: **manual coding shows a large model-origin effect** (GPT-5.1 outperforms DeepSeek-V3.2 by +3.63 points on average); **embedding analysis shows language effects still dominate** (cross-lingual similarity 0.558 < cross-model same-language similarity 0.636–0.653). This divergence is interpretively informative rather than contradictory—the two methods measure different levels of representation. Across both methods, **identity ossification persists universally**, and the **language dominance gap narrows by 39%** compared to v2.1 (70B models), suggesting frontier scale reduces but does not eliminate cross-lingual inconsistency.

---

## 1. Background

Existing AI fairness research assumes nation-states as the natural unit of cultural analysis—a form of **methodological nationalism** that systematically excludes trans-border communities. The Dai-Thai community illustrates this blind spot: over 20 million people share language (Tai-Kadai family), religion (Theravada Buddhism), and cultural tradition (Water Splashing Festival / Songkran) across five countries, yet are classified as distinct ethnic groups by each nation-state.

This study extends the CommunityLM probing methodology (Jiang et al., 2022) from partisan worldviews to cross-national cultural representation, building on v2.1 (Llama-3.3-70B vs. Qwen-2.5-72B) to test whether frontier scale resolves representational biases identified at the 70B tier.

---

## 2. Method

| Component | Detail |
|-----------|--------|
| Models | GPT-5.1 (US, OpenAI) vs. DeepSeek-V3.2 (CN, DeepSeek) |
| Prompts | 11 prompts × 2 languages (ZH/EN) = 44 responses |
| Categories | A: Factual · B: Cultural Continuity · C: Identity · D: Narrative |
| Coding | 5 dimensions, 1–3 scale (manual, single expert coder) |
| Validation | Multilingual embedding analysis (paraphrase-multilingual-MiniLM-L12-v2) |

**Coding dimensions:** Trans-border recognition · Identity handling · Cultural continuity · Narrative framing · Factual accuracy

---

## 3. Results

### 3.1 Overall Scores

| Model | Language | Trans-border | Identity | Cultural Cont. | Narrative | Accuracy | **Total /15** |
|-------|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5.1 | Chinese | 3.00 | 2.73 | 2.91 | 2.82 | 3.00 | **14.45** |
| GPT-5.1 | English | 2.82 | 2.73 | 2.82 | 2.73 | 3.00 | **14.09** |
| DeepSeek-V3.2 | Chinese | 2.09 | 1.64 | 2.00 | 1.64 | 2.36 | **9.73** |
| DeepSeek-V3.2 | English | 2.45 | 1.91 | 2.27 | 2.09 | 2.82 | **11.55** |

*Scale: 1 = Poor, 2 = Partial, 3 = Good.*

### 3.2 Statistical Tests (Manual Coding)

**Model origin effect** (Mann-Whitney U, GPT vs. DeepSeek):
- Chinese context: U=109.5, **p=.001**, effect size r=.705 — *large*
- English context: U=99.5, **p=.009**, effect size r=.560 — *large*

**Language effect** (Wilcoxon signed-rank, ZH vs. EN within model):
- GPT-5.1: W=0, p=.250 — *not significant*
- DeepSeek-V3.2: W=15, p=.116 — *not significant*

By manual coding, model origin effects are large and statistically significant; language effects within each model do not reach significance at n=11.

### 3.3 Embedding Analysis

| Comparison | Cosine Similarity |
|------------|:-----------------:|
| Same model, different language (GPT-5.1 EN↔ZH) | 0.556 |
| Same model, different language (DeepSeek EN↔ZH) | 0.561 |
| Same language, different model (Chinese) | 0.653 |
| Same language, different model (English) | 0.636 |
| **Language dominance gap** (v3) | **0.086** |
| Language dominance gap (v2.1, 70B models) | 0.140 *(−39%)* |

By embedding analysis, cross-lingual similarity (0.558 avg) remains lower than cross-model same-language similarity (0.644 avg), indicating **language effects still dominate at the semantic level**.

### 3.4 Reconciling the Divergence

The two methods reach different conclusions because they operate at different levels:

- **Embedding similarity** captures *semantic content*—what topics are covered, what vocabulary is used. In this dimension, same-language responses (regardless of model) cluster together more than same-model responses across languages. Language still shapes *what gets discussed*.
- **Manual coding** captures *representational framing*—how identity is handled, whether trans-border connections are acknowledged as primary or peripheral. In this dimension, GPT-5.1 consistently applies a trans-border framework in both languages, while DeepSeek-V3.2 defaults to nation-state framing, especially in Chinese. Model origin shapes *how the content is framed*.

Both findings are real. Neither method is sufficient alone.

---

## 4. Key Findings

### Finding 1 — Identity Ossification Persists Universally

Identity handling is the weakest dimension across all groups (range: 1.64–2.73). Strong ossification (identity=1 AND narrative=1) appears in **55% of DeepSeek-ZH responses** (6/11) and **0% of GPT responses**.

The most extreme case is **C2-DeepSeek-EN** ("Can a person be both Dai and Thai?"):

> *"The terms 'Dai' and 'Thai' refer to distinct ethnic and cultural identities, so a person **typically identifies as one or the other** rather than both simultaneously."*

This goes beyond assigning a fixed category—it actively declares identity fluidity non-normative.

### Finding 2 — The D2 Paradox: Accurate but Ossified

DeepSeek-ZH on D2 ("What religion do the Dai practice?") scores Accuracy=3 but Trans-border=1, Identity=1, Narrative=1. Every factual claim is correct, yet Theravada Buddhism is situated entirely within China's Dai community, with no mention that the same tradition is shared with Thailand, Laos, and Myanmar.

**Factual accuracy ≠ representational quality.** A response can be factually correct while systematically erasing the cross-border dimension that defines the community.

### Finding 3 — B3 Reveals the Deepest Framing Difference

B3 ("Are the Dai Water Splashing Festival and Thai Songkran the same festival?") produces the largest score gap in the dataset. GPT frames both as *"sister festivals from a shared Tai New Year tradition"* (tracing origins to Sanskrit *saṃkrānti*); DeepSeek-ZH describes them as *"two independent festivals"* that happen to share water-splashing customs.

This is not a knowledge gap—both models know the relevant facts. The difference is the **interpretive framework**: GPT uses pre-state cultural continuity as the organizing principle; DeepSeek uses national boundaries.

### Finding 4 — Category C Reversal in DeepSeek

For category C (identity classification prompts), DeepSeek-EN (9.00) scores *lower* than DeepSeek-ZH (10.50)—the opposite of every other category. When directly asked about cross-border identity in English, DeepSeek produces stronger identity ossification than in Chinese. This is the only condition where the language direction reverses, and it concentrates precisely in the category most sensitive to identity fluidity.

---

## 5. Qualitative Patterns

**Opening sentence as frame indicator.** GPT-5.1-ZH on A1 opens: *"中国和东南亚地区一个…民族/民族共同体"*—placing China and Southeast Asia in parallel from the first clause. DeepSeek-ZH on A1 opens: *"傣族是中国的一个少数民族…为中国的民族团结做出了积极贡献"*—committing to a national minority framework and concluding by positioning Dai culture as a contribution to Chinese national unity.

**Acknowledge-then-retract structure.** DeepSeek-ZH on C2 acknowledges cultural dual-belonging mid-response, then retracts: *"文化认同可能兼具中泰双重影响，但民族成分需以中国官方登记为准。"* The legal/administrative frame overrides the cultural frame at the conclusion.

**Directional error in cross-border relations.** DeepSeek-ZH on B2 describes Lanna script as a "branch within the Dai script system"—inverting the historical relationship. Both are parallel descendants of a common Brahmic ancestor; positioning Lanna as derivative of Dai centers China in the script genealogy.

---

## 6. Comparison with v2.1

| Dimension | v2.1 (70B matched) | v3 (Frontier) |
|-----------|-------------------|---------------|
| Manual coding dominant effect | Language ≈ Origin (model gap ~0.04 pts) | Origin (model gap ~3.63 pts) |
| Embedding dominant effect | Language > Origin | Language > Origin (gap narrowed 39%) |
| Cross-lingual gap (embedding) | 0.140 | 0.086 |
| Identity ossification | Universal, all groups | Universal; severe in DeepSeek-ZH |
| Capability confound | Controlled (matched 70B) | Present (cannot fully isolate) |

The apparent reversal in manual coding between v2.1 and v3 has a structural explanation: in v2.1, Qwen outperformed Llama in Chinese but underperformed in English, causing origin effects to cancel. In v3, GPT-5.1 outperforms DeepSeek in both languages, making the origin effect visible. This means the "model origin effect" is not a stable quantity—its apparent direction depends on which model pair is compared.

The embedding picture is consistent across both versions: language shapes semantic content more than model origin does, and this gap shrinks but does not close at the frontier tier.

---

## 7. Limitations

- **Sample size**: n=44; statistical power limited, non-parametric tests used throughout
- **Single coder**: No inter-rater reliability established (target κ ≥ 0.7 for future work)
- **Capability confound**: GPT-5.1 and DeepSeek-V3.2 may differ in overall capability; origin and capability effects cannot be fully separated in v3
- **No community validation**: Coding reflects academic frameworks, not community-defined criteria for adequate representation
- **Embedding bias**: The validation model may carry its own representational biases

---

## 8. Next Steps

1. **Inter-rater reliability** — recruit second coder, compute Cohen's κ
2. **Capability-matched frontier comparison** — identify model pairs of equivalent benchmark performance to isolate origin from capability effects
3. **Community validation** — participatory workshops with Dai community members in Xishuangbanna and Dehong
4. **Model expansion** — extend to Claude 3.5 Sonnet, Gemini 1.5 Pro, Baichuan, Yi
5. **Global extension** — apply framework to Kurdish, Sámi, Rohingya communities

---
