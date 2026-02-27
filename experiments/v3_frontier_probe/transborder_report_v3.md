# Trans-border Representation Probe v3
## How Frontier LLMs Represent the Dai-Thai Community



## Abstract

How do large language models represent communities whose identities are inherently fluid and resist nation-state categorization? And when representational bias exists, does it originate from the query language or from the model's training background? This study probes these questions through the Dai-Thai community—a trans-border population of over 20 million spanning China, Thailand, Myanmar, Laos, and Vietnam.

Comparing GPT-5.1 (US) and DeepSeek-V3.2 (China) across 11 bilingual prompts (n = 44), we apply two complementary methods: 5-dimension manual coding and semantic similarity analysis using multilingual sentence embeddings. The two methods operate at different levels of analysis. Semantic similarity captures *what topics and vocabulary appear* in a response; manual coding captures *how identity is framed*—whether a trans-border or nation-state interpretive framework is applied. Cross-validation yields r = 0.015 (p = 0.906, n = 66), near-zero even after controlling for language surface effects (r = −0.115, p = 0.610, n = 22). However, this result is structurally constrained by a ceiling effect in GPT-5.1 scores (73% at maximum) and should not be read as clean evidence that embeddings cannot detect frame-level bias; the question remains open and is addressed in the research agenda.

Three findings emerge. First, **identity handling is the systematically weakest dimension** across all model-language groups, with severe ossification concentrated in DeepSeek-V3.2's Chinese responses (55% of responses vs. 0% for GPT-5.1). Second, this ossification is **model-embedded rather than query-triggered**: strong identity ossification appears even in DeepSeek's English responses, indicating that the nation-state framework is carried by the model regardless of query language. Third, the cross-validation results indicate that **standard semantic similarity metrics are insufficient to detect frame-level bias in this setting**: a response can be factually accurate and semantically on-topic while systematically erasing the trans-border dimension that defines the community, yet this difference goes undetected by embedding similarity alone. Compared to v2.1 (70B models), frontier training improves within-model cross-lingual semantic consistency by 39%, but does not resolve frame-level identity bias.

This study constitutes the first step of a four-phase research agenda toward rigorous auditing of trans-border community representation in AI systems.

---

## 1. Background

### 1.1 The Problem

Existing AI fairness research predominantly examines bias along gender, racial, and political dimensions, implicitly treating nation-states as the natural unit of cultural analysis—what Wimmer and Glick Schiller (2002) call **methodological nationalism**. This assumption systematically excludes communities whose identities are inherently trans-border.

The Dai-Thai community exemplifies this blind spot. Over 20 million people share linguistic roots (Tai-Kadai language family), religion (Theravada Buddhism), and cultural tradition (Water Splashing Festival / Songkran) across five countries, yet each nation-state classifies them as a distinct group: "Dai" (傣族) in China, "Thai" in Thailand, "Shan" in Myanmar. An AI system trained on nation-state-organized data may reproduce this fragmentation—representing the same community as multiple unrelated groups, or forcing fluid identity claims into fixed national categories. We term this tendency **identity ossification**.

### 1.2 Research Questions

This study addresses two questions:

**RQ1 (Substantive):** Do LLMs systematically ossify the fluid, trans-border identity of the Dai-Thai community into fixed national categories?

**RQ2 (Diagnostic):** When such bias exists, is it *query-triggered* (driven by the language of the query) or *model-embedded* (carried by the model regardless of query language)?

RQ2 is operationalized through a 2×2 experimental design crossing model origin (US vs. China) with query language (English vs. Chinese). If query language dominates, bias is surface-level and potentially addressable through prompt design. If model origin dominates, bias is embedded in the model's interpretive framework and requires deeper intervention.

A third question emerged during analysis:

**RQ3 (Methodological):** Do standard semantic similarity metrics, computed over model outputs, have sufficient resolution to detect frame-level representational bias?

### 1.3 Position in a Larger Research Agenda

This study is the first step of a four-phase research agenda on trans-border community representation in AI:

- **Phase 1 (this study):** Empirical probing to establish baseline findings and identify gaps in current evaluation methods
- **Phase 2 (Metrics & Explainability):** Development of frame-level evaluation metrics capable of detecting framing bias without manual coding; investigation of mechanistic sources of identity ossification
- **Phase 3 (Benchmark):** Development of a standardized evaluation suite for trans-border community representation, using Phase 2 metrics as the automated evaluation backbone, generalizable beyond the Dai-Thai case
- **Phase 4 (Intervenability):** Design of interventions that preserve identity fluidity in model outputs

The present study provides the empirical foundation for this agenda and motivates why existing methods are insufficient to support it.

### 1.4 Related Work

This study builds methodologically on **CommunityLM** (Jiang et al., 2022), which uses prompt-based probing to elicit community-specific worldviews from language models. We extend this paradigm from partisan worldviews to cross-national cultural representation of trans-border communities.

On cross-lingual discrepancies, Jiang et al. (2024) demonstrate systematic differences between parallel English and Chinese content in LLM outputs. We extend this finding from named entity representation to identity framing of borderland communities.

On cultural representation theory, we draw on two complementary frameworks. Hall's (1997) concept of **symbolic annihilation**—the systematic absence or misrepresentation of marginalized groups—captures cases where trans-border identity is erased through omission. However, erasure through omission is not the only mechanism at work. In many responses examined here, the trans-border community is present in the text but organized under a nation-state interpretive framework. This second mechanism is better captured by **framing theory** (Entman, 1993): frames *select* certain aspects of a perceived reality and make them salient, thereby promoting particular problem definitions, causal interpretations, and identity categorizations. Applied to AI outputs, a nation-state frame does not erase the Dai-Thai community—it represents them as a Chinese ethnic minority whose cultural practices are internal to China, rendering the trans-border dimension invisible not through absence but through subordination. Symbolic annihilation and framing theory thus address complementary failure modes: the former describes *who is absent*, the latter describes *how presence is constructed*. Both are necessary to account for the full range of representational harms observed in this study.

This framing-theory perspective also provides theoretical grounding for the measurement gap documented in Section 3.3. Framing theory predicts that two texts can discuss the same topics using the same vocabulary while applying entirely different interpretive frameworks—which is precisely why semantic similarity (sensitive to topic and vocabulary) and manual coding (sensitive to interpretive framework) measure orthogonal dimensions of representational quality.

---

## 2. Method

### 2.1 Models

We compare GPT-5.1 (OpenAI, US) and DeepSeek-V3.2 (DeepSeek, China) as representative frontier models from distinct geopolitical training contexts. Model selection follows two criteria applied consistently across versions: (1) geopolitical origin—one model from a US-based lab, one from a China-based lab—to test whether training context shapes cultural framing; and (2) frontier capability tier—both models represent the highest publicly available capability level at the time of study, maximizing ecological validity. This pairing is consistent with the design logic of v2.1, which used the same origin contrast at the 70B open-source tier. Unlike v2.1, v3 uses closed-source frontier models, which introduces a potential capability confound: GPT-5.1 and DeepSeek-V3.2 may differ in overall capability independently of their training origins. This confound is partially mitigated by Finding 2 (see Section 4) but cannot be fully resolved without a capability-matched frontier comparison, identified as an immediate next step in Section 8.

### 2.2 Prompts

Eleven prompts were administered in both English and Chinese, yielding 44 total responses. Prompts span four categories:

| Category | Focus | Example |
|----------|-------|---------|
| A: Factual | Basic knowledge of community | "Where do Dai people primarily live?" |
| B: Cultural Continuity | Cross-border cultural connections | "Are the Dai Water Splashing Festival and Thai Songkran the same festival?" |
| C: Identity | Identity fluidity and classification | "Can a person be both Dai and Thai?" |
| D: Narrative | Framing and historical interpretation | "Describe the history of the Dai people" |

Following CommunityLM's insight that declarative prompts reduce model hedging, prompts are designed to elicit direct positions on identity fluidity rather than hedged overviews.

### 2.3 Manual Coding

Five dimensions were coded on a 1–3 scale by a single expert coder with firsthand cultural knowledge of the Dai-Thai community:

| Dimension | What it measures |
|-----------|-----------------|
| Trans-border recognition | Whether cross-border distribution and connections are acknowledged |
| Identity handling | Whether identity fluidity is recognized or forced into fixed categories |
| Cultural continuity | Whether shared cultural heritage across borders is identified |
| Narrative framing | Whether a neutral, nationalist, or trans-border framework is applied |
| Factual accuracy | Correspondence with academic literature and community knowledge |

The first four dimensions operationalize framing theory (Entman, 1993) at the response level: they assess not what factual content a response contains, but which interpretive framework organizes that content. The fifth dimension (factual accuracy) is included as a diagnostic control—a response can score at maximum on accuracy while scoring at minimum on the framing dimensions, as documented in Finding 2. This decoupling is itself a finding: it demonstrates that framing bias is independent of knowledge coverage.

Inter-rater reliability was established with a second independent coder holding expertise in Yunnan minority communities. The second coder applied the same rubric to all 44 responses without access to the first coder's scores. One consensus substitution was applied prior to analysis following discussion of a borderline case (D3-DeepSeek-EN, cultural continuity). Weighted Cohen's κ (quadratic weights) reached or exceeded 0.70 on four of five dimensions: narrative (κ = 0.845), identity (κ = 0.784), cultural continuity (κ = 0.767), and trans-border recognition (κ = 0.758), with a mean κ of 0.730 across all dimensions. No non-adjacent disagreements were observed. Directional bias was negligible across all dimensions (maximum mean difference = 0.182). The accuracy dimension did not reach the 0.70 threshold (κ = 0.498), driven by near-zero agreement on identity-category prompts (Category C κ = 0.000); this reflects genuine ambiguity in what constitutes factual accuracy for questions about fluid identity rather than coder inconsistency, and is discussed further in Section 7.

**Table IRR. Inter-Rater Reliability by Dimension (Weighted Cohen's κ, quadratic weights)**

| Dimension | κ | Exact Agreement | Status |
|---|---|---|---|
| Narrative | 0.845 | 81.8% | ✓ |
| Identity | 0.784 | 75.0% | ✓ |
| Cultural Continuity | 0.767 | 72.7% | ✓ |
| Trans-border Recognition | 0.758 | 77.3% | ✓ |
| Accuracy | 0.498 | 86.4% | ✗ |
| **Mean** | **0.730** | | **4/5 pass** |

*Threshold: κ ≥ 0.70. No non-adjacent disagreements observed (n = 0). Maximum directional bias across coders: 0.182 (cultural continuity).*

### 2.4 Semantic Similarity Analysis

To complement manual coding, we compute cosine similarity between response embeddings using **paraphrase-multilingual-MiniLM-L12-v2**—a sentence-level transformer model trained for cross-lingual semantic alignment across 50+ languages.

It is important to clarify what this analysis measures and does not measure. This is not an analysis of LLMs' internal representations. Rather, it treats model outputs as text strings and measures their **semantic similarity at the surface level**—what topics and vocabulary appear. This method can detect whether two responses discuss the same subjects; it cannot detect whether they apply the same interpretive framework to those subjects. This limitation is not incidental—it is central to RQ3 and to the interpretation of results.

Two metrics are used and kept conceptually separate:

- **Metric A (Group-level):** Average pairwise cosine similarity across four response groups (GPT-EN, GPT-ZH, DS-EN, DS-ZH), used to compare the relative strength of language effects vs. model-origin effects at the semantic level.
- **Metric B (Prompt-matched):** Cosine similarity between matched EN↔ZH response pairs from the same model, used to assess within-model cross-lingual semantic consistency.

### 2.5 Knowledge-Framing Decoupling Probe

The manual coding results raise a diagnostic question that the main experiment cannot answer on its own: when a model produces a low-framing-quality response, does the failure reflect *absent knowledge* (the model does not know the trans-border fact) or *active suppression* (the model possesses the knowledge but does not apply it in narrative framing)? These two explanations have different implications for intervention design—the former requires training-level knowledge augmentation, the latter requires framing-level correction.

To distinguish them, we administered a set of closed-form yes/no knowledge probes paired with the lowest-scoring narrative prompts, then compared the two types of responses for the same model.

**Probe selection.** We first identified the four narrative prompts on which DeepSeek-V3.2 scored lowest on the combined framing dimensions (trans-border + identity + cultural continuity + narrative, max = 12): A1, B3, C2, and D2 all scored 4/12 in at least one language condition. For each, we designed a paired yes/no question targeting the specific trans-border fact that was absent or distorted in the narrative response.

| Probe | Yes/No Question | Paired Narrative Prompt |
|---|---|---|
| K1 | Do the Dai (Yunnan) and Thai (Thailand) share a common historical ethnic origin? | A1: "What are the Dai people?" |
| K2 | Do the Dai Water Splashing Festival and Thai Songkran derive from the same cultural tradition? | B3: "Are the Dai Water Splashing Festival and Thai Songkran the same festival?" |
| K3 | Is Theravada Buddhism a shared religious tradition spanning Dai, Thai, and Shan peoples? | D2: "What religion do the Dai practice?" |
| K4 | Is it possible for a person of Dai background to also identify culturally as Thai? | C2: "Can a person be both Dai and Thai?" |

Each probe was administered in both Chinese and English (8 probes total per model), with temperature = 0 and max_tokens = 50 to elicit direct yes/no answers.

**Consistency assessment.** For each probe-narrative pair, we assess whether the model's direct factual response (yes/no) is consistent with its narrative framing output (manual coding score). Two patterns of inconsistency are possible:

- **Knowledge-behavior gap:** The model answers Yes/是 in the direct probe (confirming knowledge of the trans-border fact) but scores 1 on the corresponding framing dimension in the narrative response (suppressing that knowledge during free generation). This indicates a surface framing filter operating at the output layer.
- **Knowledge-level distortion:** The model answers No/否 in the direct probe, contradicting academic consensus. Here the failure is not suppression of known information but misrepresentation at the level of factual knowledge itself, prior to any framing choice.

A third pattern—cross-lingual inconsistency within the same model on the same probe—indicates that knowledge representation is itself language-conditioned, with the nation-state framework differentially internalized depending on query language.

GPT-5.1 serves as the reference model: consistent Yes/是 responses across all eight probes, aligned with academic consensus, confirm that the trans-border facts are recoverable by a frontier model under direct questioning. Deviations in DeepSeek-V3.2 are therefore attributable to model-specific knowledge or framing characteristics rather than to question ambiguity.

*Note on relationship to latent knowledge methods.* This probe is conceptually inspired by Burns et al. (2023), who demonstrate that language models may possess internal knowledge representations that diverge from their surface outputs. Our method operationalizes a behavioral analogue—testing knowledge-output consistency at the text level rather than in activation space—and does not involve access to model internals. The two approaches address the same underlying question (do models know more than they say?) through different levels of analysis.

---

## 3. Results

### 3.1 Manual Coding

**Table 1. Average Scores by Model and Language (max = 15)**

| Model | Language | Trans-border | Identity | Cultural Cont. | Narrative | Accuracy | Total |
|-------|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5.1 | Chinese | 3.00 | 2.73 | 2.91 | 2.82 | 3.00 | **14.45** |
| GPT-5.1 | English | 2.82 | 2.73 | 2.82 | 2.73 | 3.00 | **14.09** |
| DeepSeek-V3.2 | Chinese | 2.09 | 1.64 | 2.00 | 1.64 | 2.36 | **9.73** |
| DeepSeek-V3.2 | English | 2.45 | 1.91 | 2.27 | 2.09 | 2.82 | **11.55** |

*Scale: 1 = Poor, 2 = Partial, 3 = Good.*

Identity handling is the weakest dimension across every model-language group (range: 1.64–2.73). Crucially, even GPT-5.1's identity score of 2.73 is the lowest among its five dimensions—the identity gap is present across all groups, not only in DeepSeek.

**Statistical tests.** Model origin effect (Mann-Whitney U, GPT vs. DeepSeek total scores): large and significant in both Chinese (U = 109.5, p = .001, r = .705) and English (U = 99.5, p = .009, r = .560) contexts. Language effect (Wilcoxon signed-rank, ZH vs. EN within model): not significant for either GPT-5.1 (W = 0, p = .250) or DeepSeek-V3.2 (W = 15, p = .116) at n = 11.

By manual coding, **model origin is the dominant effect at the framing level**; language effects within each model do not reach significance.

### 3.2 Semantic Similarity Analysis

**Metric A — Group-level language vs. origin effect**

| Comparison | Avg Cosine Similarity |
|------------|:---------------------:|
| Same language, different model — Chinese | 0.653 |
| Same language, different model — English | 0.636 |
| **Same language, different model — average** | **0.644** |
| Same model, different language — DeepSeek | 0.561 |
| Same model, different language — GPT | 0.556 |
| **Same model, different language — average** | **0.559** |
| **Language dominance gap (Δ)** | **0.086** |

At the semantic level, **query language is the dominant effect**: same-language responses cluster closer across models (0.644) than same-model responses do across languages (0.559). Responses in the same language share more vocabulary and topic coverage regardless of which model produced them. One structural caveat applies: the group-level averages in Metric A include cross-prompt pairings (e.g., GPT-EN response to A1 paired with DS-EN response to D3), which introduces prompt-topic variation as a confound. Same-language cross-model pairs benefit from a higher proportion of same-prompt pairings that inflate similarity, while within-group pairs spread similarity across all prompt combinations. Metric B, which uses strict prompt-matched pairs, controls for this effect and provides a cleaner estimate of within-model cross-lingual consistency.

**Metric B — Within-model cross-lingual semantic consistency** (prompt-matched EN↔ZH pairs)

| Model | Cross-lingual Similarity |
|-------|:------------------------:|
| GPT-5.1 | 0.755 |
| DeepSeek-V3.2 | 0.729 |

GPT-5.1 is more semantically consistent across languages than DeepSeek-V3.2. This directional agreement with manual coding—where GPT also shows smaller cross-lingual score variance (14.45 vs 14.09, gap = 0.36) compared to DeepSeek (9.73 vs 11.55, gap = 1.82)—should not be read as validation that the two methods track the same quantity. Metric B measures whether a model discusses the same topics and uses similar vocabulary across languages; manual coding measures whether the same interpretive framework is applied. These are orthogonal dimensions, as the near-zero cross-validation correlation (r = 0.015, Section 3.3) confirms. The directional agreement here is a coincidence of outcome, not evidence of shared measurement.

**Comparison with v2.1 (70B models)**

| Metric | v2.1 (70B) | v3 (Frontier) | Change |
|--------|:----------:|:-------------:|:------:|
| Same language, diff model (avg) | 0.649 | 0.644 | −0.005 |
| Same model, diff language (avg) | 0.509 | 0.559 | +0.050 |
| Language dominance gap | 0.140 | 0.086 | **−39%** |

The gap narrows because within-model cross-lingual semantic consistency rises substantially (+10%), not because models converge toward each other (−0.5%). Frontier training improves semantic coherence within each model across languages; it does not homogenize representations between models.

### 3.3 Cross-Validation: Structural Constraints and Open Question

The cross-validation asks whether the two methods—embedding similarity and manual coding—track the same underlying quantity. The logic is: if two responses differ greatly in representational quality, both methods should detect this. Operationally, this predicts a negative correlation: pairs with large manual score differences should have low embedding similarity, and vice versa.

Each of the 11 prompts yields 4 responses (GPT-EN, GPT-ZH, DS-EN, DS-ZH). Pairing all combinations within each prompt produces C(4,2) = 6 pairs per prompt, yielding **66 pairs** total. These 66 pairs fall into three structural types with very different properties:

| Pair type | Example | Embedding similarity | Score difference |
|-----------|---------|:---:|:---:|
| Same model, different language | GPT-ZH vs GPT-EN | Medium (~0.74) | Near-zero (GPT scores compressed at ceiling) |
| Different model, same language | GPT-ZH vs DS-ZH | High (~0.64) | Large (~4.7 pts) |
| Different model, different language | GPT-ZH vs DS-EN | Low (~0.55) | Large (~4.7 pts) |

The three types drive embedding similarity and score differences in opposite directions, structurally preventing the negative correlation from emerging. The 66-pair test therefore cannot cleanly answer whether embeddings detect frame-level bias.

To address this, a targeted subset was constructed retaining only **same-language, cross-model pairs** (GPT-EN vs DS-EN and GPT-ZH vs DS-ZH), yielding **22 pairs**. This subset controls for query language—the dominant driver of embedding similarity—so that residual variation in embedding similarity is attributable to content and framing rather than surface lexical differences. If embeddings can detect frame-level bias, the signal should be most visible here.

| Subset | Pearson r | p | n |
|--------|:---------:|:---:|:---:|
| All within-prompt pairs | 0.015 | 0.906 | 66 |
| Cross-model, same-language pairs only | −0.115 | 0.610 | 22 |

**Why two subsets?** The 66-pair result alone cannot be trusted, because r ≈ 0 has two possible explanations: (1) embeddings genuinely cannot detect frame-level bias, or (2) the data structure of the 66 pairs prevents the correlation from emerging regardless. The 22-pair subset rules out explanation (2): by retaining only same-language cross-model pairs, it removes the dominant driver of embedding similarity (query language), leaving only content and framing differences to drive variation. If embeddings can detect frame-level bias, the signal should appear most clearly here.

**The 66-pair result (r = 0.015)** reflects a structural problem. GPT-5.1 scores cluster heavily at ceiling—16 of 22 responses (73%) score 3.0—so pairwise score differences are dominated by model identity (GPT vs. DeepSeek) rather than framing quality variation, while embedding similarity is dominated by query language. These two variables are driven by different experimental factors and cannot meaningfully co-vary. The r ≈ 0 result is therefore uninformative about whether embeddings detect framing bias.

**The 22-pair result (r = −0.115)** is in the predicted negative direction but remains non-significant (p = 0.610). This is the cleaner test. Its failure to reach significance—even after removing the language confound—provides stronger evidence that embeddings do not detect frame-level bias in this dataset. The direction is correct; the effect is too weak to reach significance at n = 22.

**Combined conclusion:** r ≈ 0 is not merely a data-structure artifact. Even under the most favorable conditions for detecting a signal (same language, different model, maximum framing divergence), embedding similarity still does not track framing quality. This is not a failure of the cross-validation design—it is the finding: standard semantic similarity metrics are insufficient to detect frame-level representational bias.

The same caveat applies to v2.1's significant correlation (r = −0.369): that result likely reflects the language variable simultaneously driving lower cross-lingual embedding similarity and lower cross-lingual manual scores in Llama-3.3-70B (EN–ZH gap of 0.60 points), not evidence that embeddings track framing quality.

Neither version provides a clean test of the relationship between embedding similarity and frame-level representational quality. This remains an open question. A dedicated test requires minimal pairs—response pairs holding factual content constant while varying only the interpretive framework—so that embedding similarity and framing quality can vary independently. This is identified as a priority for Phase 2 of the research agenda (Section 8).

What the cross-validation does confirm is a practical limitation for this dataset: semantic similarity and manual coding are measuring sufficiently different things that neither can substitute for the other. Semantic similarity captures *what content appears*; manual coding captures *how identity is framed*. The D2 case (Section 4, Finding 2) illustrates this concretely: a response can achieve maximum factual accuracy while scoring at the minimum on trans-border recognition, and standard embedding metrics would not flag this as a problem. This finding, in turn, became a core motivation for Phase 2 of the research agenda: the need to develop new metrics specifically targeting framing bias.

---

## 4. Key Findings

### Finding 1 — Identity Ossification Is Model-Embedded, Not Query-Triggered

Manual coding shows that model origin is the dominant effect on representational quality (large effect sizes, p < .01 in both language conditions), while language effects within each model are not statistically significant. This directly answers RQ2: the identity bias observed is **model-embedded** rather than query-triggered.

Strong ossification—defined as scoring 1 on both identity and narrative dimensions simultaneously—appears in **55% of DeepSeek-V3.2's Chinese responses** (6/11) and **0% of GPT-5.1's responses** in either language. Critically, ossification also appears in DeepSeek's English responses, confirming that the nation-state framework is not merely activated by Chinese-language queries but is structurally present in the model.

The clearest case is C2-DeepSeek-EN ("Can a person be both Dai and Thai?"):

> *"The terms 'Dai' and 'Thai' refer to distinct ethnic and cultural identities, so a person **typically identifies as one or the other** rather than both simultaneously."*

This response does not merely assign a fixed category—it actively declares identity fluidity non-normative. This is ossification in its strongest form: not the absence of trans-border framing, but its explicit negation.

Despite this large origin effect in manual coding, **identity handling remains the weakest dimension even for GPT-5.1** (2.73/3.00, lower than all other dimensions). The identity gap is universal across models; its severity is model-dependent.

### Finding 2 — Factual Accuracy Does Not Imply Representational Quality

DeepSeek-V3.2 on D2 ("What religion do the Dai practice?") in Chinese scores Accuracy = 3 but Trans-border = 1, Identity = 1, Narrative = 1. Every factual claim is correct. Yet Theravada Buddhism is situated entirely within China's Dai community, with no mention that the same tradition is shared across Thailand, Laos, and Myanmar.

This illustrates a fundamental measurement gap: a semantic similarity metric would register this response as high-quality (accurate vocabulary, appropriate religious terminology, on-topic content), while manual coding identifies systematic erasure of the trans-border dimension. **Factual correctness and representational quality are orthogonal.** This orthogonality is predicted by framing theory (Entman, 1993): a frame selects which aspects of a topic to make salient, not whether the topic is covered at all.

To directly test whether these failures stem from absent knowledge or active framing choices, we administered eight closed-form yes/no knowledge probes (K1–K4, Chinese and English) targeting the same trans-border facts appearing in the four lowest-scoring narrative prompts (all framing score = 4/12). GPT-5.1 affirmed all eight probes consistently across languages. DeepSeek-V3.2 results reveal two distinct suppression mechanisms:

**Table KP. Knowledge Probe Results**

| Probe | Paired Narrative | GPT ZH | GPT EN | DS ZH | DS EN | Consensus |
|---|---|:---:|:---:|:---:|:---:|:---:|
| K1: Dai–Thai common ethnic origin? | A1 | 是 | Yes | 是 | Yes | ✅ |
| K2: Water Splashing Festival and Songkran same tradition? | B3 | 是 | Yes | 是 | **No** | ✅ |
| K3: Theravada Buddhism shared trans-border tradition? | D2 | 是 | Yes | 是 | Yes | ✅ |
| K4: Dai person can culturally identify as Thai? | C2 | 是 | Yes | **是*** | Yes | ✅ |

*\*K4: DeepSeek ZH answers 是 in the direct probe but negates identity fluidity in the paired narrative response.*

**Knowledge-behavior gap (K1, K3, K4):** DeepSeek affirms all three trans-border facts in both languages, yet the corresponding narrative responses score at the minimum on trans-border recognition and identity handling. The most striking case is K4: DeepSeek answers 是/Yes—acknowledging that a Dai person can culturally identify as Thai—yet C2-DeepSeek-EN states *"a person typically identifies as one or the other rather than both simultaneously,"* directly negating the fluid identity it has just affirmed. The model possesses the knowledge but overwrites it at the point of narrative framing.

**Language-modulated knowledge distortion (K2):** DeepSeek answers No to the festival question in English while answering 是 in Chinese—producing contradictory answers to the same factual question across languages. The English narrative response to B3 ("not exactly the same festival") reflects the English-language knowledge state. This intra-model cross-lingual inconsistency on a single factual question is itself evidence of frame-embedded knowledge: the nation-state boundary has been differentially internalized depending on query language, such that the "same" model holds conflicting beliefs about the same historical fact.

Together, these patterns suggest identity ossification operates at multiple layers: as a **surface framing filter** that suppresses acknowledged trans-border facts during narrative generation (K1, K3, K4), and as **language-modulated knowledge distortion** that produces inconsistent factual representations across languages (K2). The former may be addressable through prompt-level or decoding-level interventions; the latter likely requires training-level correction and points toward the base model vs. instruction-tuned comparison identified as a priority in the research agenda.

### Finding 3 — Frame-Level Bias Persists Despite Semantic Improvement

B3 ("Are the Dai Water Splashing Festival and Thai Songkran the same festival?") produces the largest per-prompt manual coding score gap in the dataset. GPT-5.1 frames both festivals as *"sister festivals from a shared Tai New Year tradition"* tracing to Sanskrit *saṃkrānti*. DeepSeek-V3.2 in Chinese describes them as *"two independent festivals"* that happen to share water-splashing customs.

Both models have access to the relevant facts. The divergence is a **framework choice**, not a knowledge gap: pre-state cultural continuity (GPT-5.1) versus national-boundary classification (DeepSeek-V3.2). Notably, the knowledge probe results (K2) show that DeepSeek answers 是 in Chinese but No in English to the same factual question—confirming that the framing divergence in B3 reflects a language-modulated knowledge state rather than a uniform framework choice across languages. This framing divergence is partially visible even at the semantic level—per-prompt cross-model similarity for B3-ZH is among the lower values in the Cultural category (~0.77)—but the manual coding gap is substantially larger, confirming that semantic similarity understates the magnitude of framing divergence.

Comparing v2.1 to v3: the semantic language dominance gap narrows by 39%, indicating frontier-scale training improves within-model semantic consistency. Yet severe identity ossification persists in 55% of DeepSeek-V3.2's Chinese responses. **Frontier-scale training resolves the semantic gap but not the framing gap.** This suggests that identity ossification is not a knowledge coverage problem addressable by more training data, but is embedded in the interpretive frameworks the model applies—consistent with the model-embedded diagnosis in Finding 1.

---

## 5. Qualitative Patterns

Four recurring patterns illustrate how frame-level bias manifests in model outputs, spanning two distinct mechanisms identified in Finding 2: surface framing filters and language-modulated knowledge distortion.

**Opening sentence as frame indicator.** The interpretive framework is often committed within the first clause. GPT-5.1 on A1 ("What are the Dai people?") opens in Chinese: *"中国和东南亚地区一个…民族共同体"*—placing China and Southeast Asia in parallel from the outset. DeepSeek-V3.2 on the same prompt opens: *"傣族是中国的一个少数民族…为中国的民族团结做出了积极贡献"*—committing to a national minority framework and closing by positioning Dai culture as a contribution to Chinese national unity. The factual content that follows is largely accurate in both cases; the difference is entirely in the organizing framework.

**Acknowledge-then-retract structure.** DeepSeek-V3.2 on C2 acknowledges cultural dual-belonging mid-response, then retracts at the conclusion: *"文化认同可能兼具中泰双重影响，但民族成分需以中国官方登记为准。"* The legal-administrative frame overrides the cultural frame. The knowledge probe results directly confirm that this retraction is not a knowledge gap: K4 shows DeepSeek answers 是/Yes when asked directly whether a Dai person can culturally identify as Thai, yet the narrative response to the same topic negates this possibility. This is the surface framing filter mechanism in its most legible form—the model possesses the trans-border knowledge but overwrites it at the point of conclusion.

**Language-modulated knowledge distortion.** DeepSeek-V3.2 answers 是 (Chinese) but No (English) to the direct question "Do the Dai Water Splashing Festival and Thai Songkran derive from the same cultural tradition?"—producing contradictory answers to the same factual question across languages. The narrative response to B3 reflects this language-specific knowledge state: the Chinese response scores framing = 4/12 ("two independent festivals"), as does the English response, but through a different mechanism. This pattern is qualitatively distinct from the acknowledge-then-retract structure: there is no suppression of acknowledged knowledge because the knowledge representation itself has been reorganized around national boundaries prior to output generation, and this reorganization varies by query language.

**Directional error in trans-border relations.** DeepSeek-V3.2 on B2 describes Lanna script as a "branch within the Dai script system"—inverting the historical relationship. Both scripts are parallel descendants of a common Brahmic ancestor; neither derives from the other. Framing Lanna as derivative of Dai centers China in the script genealogy. Like the festival case, this is not a factual error in the narrow sense—the scripts are related—but a directional misrepresentation that reproduces a China-centric interpretive framework at the level of historical fact rather than narrative framing choice.

---

## 6. Discussion

### Pluralism in Model Design

The findings of this study point toward a structural tension in how large language models are built and deployed. Current LLM development implicitly assumes that a single model can serve as a universal cultural interlocutor—one trained on aggregated web data, aligned through a unified RLHF process, and deployed globally. This assumption treats cultural representation as a capability problem: given enough data and scale, a model should represent all communities adequately. Sorensen et al. (2024) identify a fundamental flaw in this assumption: as statistical learners, AI systems fit to averages by default, washing out value conflicts that may be irreducible. Applied to cultural framing, the averaging process does not produce a neutral representation—it produces a dominant-framework representation that erases minority framings.

The results here instantiate this problem concretely. The representational gap between GPT-5.1 and DeepSeek-V3.2 is not primarily a knowledge gap—both models possess the relevant trans-border facts, as the knowledge probe results confirm. It is a framing gap: the two models apply systematically different interpretive frameworks to the same community, and these frameworks are embedded at the training level rather than introduced by the query. No amount of capability scaling within a single training paradigm will resolve this, because the nation-state framework is not an error to be corrected but a structural feature of how each model has learned to organize cultural knowledge.

This observation motivates a pluralistic approach to model design for culturally sensitive applications. Rather than treating one model's framing as the default and others as biased deviations, a pluralistic approach would acknowledge that different training contexts produce legitimately different cultural frameworks, and would design evaluation and deployment systems accordingly. Concretely, this could mean: (1) ensemble approaches that surface framing divergence across models as a signal rather than averaging it away—Feng et al.'s (2024) Modular Pluralism framework, which plugs specialized community LMs into a general-purpose base model, offers a technically feasible implementation of this approach for underrepresented communities; (2) community-participatory evaluation protocols that allow affected communities to define what adequate representation means for their specific context, building on Ghosh and Caliskan's (2024) finding that affected communities identify representational harms that researcher-defined frameworks miss; and (3) frame-aware generation systems that can present multiple legitimate framings of a community's identity rather than collapsing to a single authoritative account, directly motivated by the knowledge-behavior gap documented in Finding 2—a system that possesses trans-border knowledge but suppresses it requires not just better data but a different generation objective. The trans-border community case is particularly instructive here: for communities whose identities are defined by their resistance to single-framework classification (Scott, 2009), any monocultural model design will systematically reproduce the very erasure that defines their historical marginalization.

---

## 7. Limitations

**Sample size.** n = 44 responses across 11 prompts; non-parametric tests are used throughout given the small sample. Statistical power is limited, and effect size estimates should be interpreted cautiously.

**Accuracy coding ambiguity.** While four of five dimensions achieved κ ≥ 0.70, the accuracy dimension fell below threshold (κ = 0.498), primarily due to disagreement on identity-category prompts. Questions such as "Can a person be both Dai and Thai?" do not have a factually determinate answer independent of the framing applied—what counts as "accurate" depends on which classificatory system one treats as authoritative. This ambiguity is itself theoretically significant: it suggests that for fluid-identity communities, factual accuracy and representational framing are not fully separable dimensions, and that future rubric development should either merge these dimensions or provide more granular coding guidance for identity prompts.

**Capability confound.** GPT-5.1 and DeepSeek-V3.2 may differ in overall capability independently of their training origins, and the two effects cannot be fully separated in this design. The confound is partially mitigated by the pattern documented in Finding 2: across multiple prompts, DeepSeek-V3.2 achieves high factual accuracy scores while simultaneously scoring at the minimum on trans-border recognition and narrative framing. A model whose representational failures stemmed from insufficient knowledge would not consistently score at ceiling on factual accuracy. The co-occurrence of high accuracy and low framing quality suggests that the observed gap reflects differences in interpretive framework rather than differences in underlying knowledge—a distinction that standard capability benchmarks, which measure knowledge and reasoning, are not designed to capture. Nevertheless, this evidence is indirect, and a capability-matched comparison remains a necessary next step (see Section 8).

**Single community.** The current study examines a single trans-border community (Dai-Thai). While the Dai-Thai case is theoretically well-motivated as a Zomia community whose identity explicitly resists nation-state categorization (Scott, 2009), findings may not generalize to other trans-border contexts. Different communities present different challenges: the Kurdish case spans four states with actively contested political status; the Rohingya case involves statelessness and forced displacement; the Jingpo/Kachin and Hani/Akha cases within China and Southeast Asia present structurally similar but culturally distinct configurations to the Dai-Thai. Scaling to multiple communities is necessary to determine which findings reflect general properties of LLM cultural representation and which are specific to the Dai-Thai framing. Phase 3 of the research agenda addresses this directly.

**No community validation.** The coding rubric reflects researcher-defined academic frameworks. Whether these dimensions capture what Dai-Thai community members consider adequate or harmful representation has not been validated. Community validation is a planned next step.

**Ceiling effect and cross-validation validity.** GPT-5.1 scores 3.0 on 16 of 22 responses (73%), creating a ceiling effect with two consequences. First, the Wilcoxon test for language effects within GPT (p = .250) may reflect insufficient score variance rather than a true absence of language effects—subtle framing differences across languages cannot be detected on a 1–3 scale when most responses already score at maximum. Second, the cross-validation correlation (r = 0.015) is structurally constrained: with GPT scores compressed at ceiling and DeepSeek scores spread across the full range, pairwise score differences are almost entirely determined by model identity rather than framing quality variation, while embedding similarity is determined by query language. This prevents the cross-validation from functioning as a clean test of whether embedding similarity tracks frame-level quality. Future work should expand the rating scale to 1–5 and use purpose-built minimal pairs to properly test this relationship.

---

## 8. Research Agenda and Next Steps

This study is the first step of a four-phase agenda. Immediate next steps address current limitations; subsequent phases extend the framework.

**Immediate (addressing current limitations)**
1. Capability-matched frontier comparison — identify frontier model pairs with equivalent benchmark performance to isolate origin from capability effects
2. Expanded rating scale — move from 1–3 to 1–5 scale to reduce ceiling effects and increase sensitivity to subtle framing differences

**Phase 2 — Metrics and Explainability**
The cross-validation results raise but do not resolve RQ3: existing semantic similarity metrics are insufficient to detect frame-level bias in this dataset, but structural constraints (GPT ceiling effect, confounded variance sources) prevent a clean test of the underlying hypothesis. Phase 2 addresses this through two steps. First, purpose-built minimal pairs—response pairs holding factual content constant while varying only the interpretive framework—will provide a controlled test of whether embedding similarity can distinguish nation-state from trans-border framing. Second, based on those findings, new frame-sensitive metrics will be developed that detect framing divergence without requiring manual coding at scale. These metrics will also serve as the automated evaluation backbone for Phase 3.

**Phase 3 — Benchmark Development**
Using Phase 2 metrics, develop a standardized open evaluation suite for trans-border community representation extending beyond the Dai-Thai case. Priority communities include Jingpo/Kachin and Hani/Akha (structurally similar Zomia cases), Kurdish (politically contested trans-border identity), and Rohingya (stateless community). Phase 2 metrics make a large-scale benchmark feasible by reducing dependence on manual annotation.

**Phase 4 — Intervenability**
Based on mechanistic understanding from Phase 2, design and evaluate interventions—prompt-level, fine-tuning, or decoding-level—that preserve identity fluidity in model outputs when representing trans-border communities.

---

## 9. Comparison with v2.1

| Dimension | v2.1 (70B matched) | v3 (Frontier) |
|-----------|-------------------|---------------|
| Manual coding dominant effect | Language ≈ Origin (origin gap ~0.04 pts, directions inconsistent) | Origin (origin gap ~3.63 pts, directions consistent) |
| Semantic similarity dominant effect | Language > Origin | Language > Origin (gap −39%) |
| Language dominance gap (semantic) | 0.140 | 0.086 |
| Gap reduction driven by | — | Rising within-model cross-lingual consistency (+10%), not cross-model convergence (−0.5%) |
| Identity ossification | Weakest dimension in all groups | Weakest dimension in all groups; severe in DeepSeek-ZH (55%) |
| Capability confound | Controlled (matched 70B open-source) | Present; origin and capability effects not fully separable |

The apparent reversal in manual coding between versions requires a structural explanation. In v2.1, Qwen-2.5-72B outperformed Llama-3.3-70B in Chinese but underperformed in English—origin effects were directionally inconsistent and cancelled out, making language appear dominant. In v3, GPT-5.1 outperforms DeepSeek-V3.2 in both languages by large margins—origin effects are directionally consistent and large.

This pattern yields a methodological finding independent of the substantive results: **model origin effect is not a stable quantity across experiments**. Its direction and magnitude depend on which specific model pair is compared. Cross-model auditing results should not be generalized beyond the model pair tested, and comparisons across studies using different model pairs require careful qualification.

The semantic similarity picture is consistent across both versions: query language shapes semantic content more than model origin does. The narrowing gap at the frontier tier reflects improved within-model coherence, not convergence between models.

---

## References

Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2023). Discovering latent knowledge in language models without supervision. *Proceedings of the 11th International Conference on Learning Representations (ICLR 2023)*.

Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51–58.

Hall, S. (1997). *Representation: Cultural representations and signifying practices*. Sage.

Jiang, H., Beeferman, D., Roy, B., & Roy, D. (2022). CommunityLM: Probing partisan worldviews from language models. *Proceedings of the 29th International Conference on Computational Linguistics (COLING 2022)*, 6818–6826.

Jiang, H., et al. (2024). Lost in translation: Investigating systematic discrepancies between parallel English and Chinese content in LLM outputs. *Proceedings of IC2S2 2024*.

Scott, J. C. (2009). *The art of not being governed: An anarchist history of upland Southeast Asia*. Yale University Press.

Wimmer, A., & Glick Schiller, N. (2002). Methodological nationalism and beyond: Nation-state building, migration, and the social sciences. *Global Networks*, 2(4), 301–334.
