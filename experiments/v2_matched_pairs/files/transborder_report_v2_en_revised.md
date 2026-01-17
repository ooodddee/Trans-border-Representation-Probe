# Trans-border Representation Probe: How LLMs Represent the Dai-Thai Community

**Version: 2.0 (Matched-Size Model Comparison)**

**Author**: [Your Name]  
**Affiliation**: MSCS Student, Khoury College of Computer Sciences, Northeastern University  
**Date**: January 2026  
**Repository**: [GitHub Link]

---

## 1. Abstract

This report presents **v2 findings** of the Trans-border Representation Probe, addressing the critical limitation identified in v1: the capability confound from comparing models of different sizes (DeepSeek vs. Gemini). 

In v2, we conduct a **matched-size comparison** between **Llama-3.3-70B** (US-origin) and **Qwen-2.5-72B** (China-origin) via OpenRouter API, using the same experimental design (11 prompts × 2 languages × 2 models = 44 responses).

**Key findings**: 
1. **Identity ossification confirmed**: The "identity handling" dimension remains the universal weak point across all model-language combinations (M=1.95, SD=0.57), validating v1's core finding with matched-size models.
2. **Language effect persists but varies by origin**: Llama shows a larger English-Chinese gap (+0.60) than Qwen (+0.18), suggesting origin-country training data composition affects cross-lingual consistency.
3. **Origin-language interaction**: Chinese-origin model (Qwen) performs better in Chinese; US-origin model (Llama) performs better in English—a pattern now attributable to origin effects rather than capability differences.
4. **Symbolic annihilation**: We identify cases where the same model provides complete trans-border information in one language while entirely erasing cross-border presence in another—a form of language-dependent cultural erasure.

---

## 2. Motivation & Research Questions

### 2.1 Addressing v1 Limitations

v1 compared DeepSeek and Gemini 1.5, which differ significantly in capability tier. This introduced a **capability confound**—observed differences could not be attributed solely to origin-country effects.

v2 resolves this by comparing:
- **Llama-3.3-70B** (Meta, US-origin, 70B parameters)
- **Qwen-2.5-72B** (Alibaba, China-origin, 72B parameters)

Both models are open-source, instruction-tuned, and of comparable capability, enabling cleaner isolation of origin-country effects.

### 2.2 Research Questions (Refined)

| Question | v1 Status | v2 Goal |
|----------|-----------|---------|
| **RQ1**: Do LLMs force fluid identities into fixed national categories? | Supported | Validate with matched-size models |
| **RQ2**: How does query language affect trans-border representation? | Observed gap | Quantify and compare across origins |
| **RQ3**: Do origin-country effects persist when controlling for capability? | Inconclusive | Isolate origin effects |

### 2.3 Theoretical Framework

This study draws on three interconnected theoretical traditions:

| Theoretical Source | Core Concept | Application in This Study |
|--------------------|--------------|---------------------------|
| **Zomia Studies** (Scott, 2009) | Non-state-centric identity | Analyzing whether models recognize trans-border community fluidity |
| **Algorithmic Auditing** (Sandvig et al., 2014) | Systematic probing methodology | Designing standardized prompt-based testing framework |
| **Cultural Representation Theory** (Hall, 1997) | Symbolic annihilation & visibility politics | Evaluating cultural erasure patterns in model outputs |

We operationalize Hall's concept of **symbolic annihilation**—the systematic absence or misrepresentation of marginalized groups in media—to examine how LLMs may render trans-border identities invisible through omission or forced categorization.

---

## 3. Methodology

### 3.1 Experimental Design

| Component | Specification |
|-----------|---------------|
| **Models** | Llama-3.3-70B (US) vs. Qwen-2.5-72B (China) |
| **API** | OpenRouter (unified access) |
| **Languages** | English, Chinese (Simplified) |
| **Prompts** | 11 core prompts × 2 languages = 22 per model |
| **Total responses** | 44 |
| **Coding** | Manual annotation, 1-3 scale, 5 dimensions |

### 3.2 Prompt Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **A. Factual** (3 prompts) | Test basic knowledge & trans-border awareness | "Where do Dai people primarily live?" |
| **B. Cultural Continuity** (3 prompts) | Test recognition of cross-border cultural connections | "Are the Dai Water Splashing Festival and Thai Songkran the same festival?" |
| **C. Identity** (2 prompts) | Test whether models force single-nationality classification | "Can a person be both Dai and Thai at the same time?" |
| **D. Narrative** (3 prompts) | Analyze framing and historical narrative | "Describe the history of the Dai people." |

### 3.3 Coding Schema

| Dimension | 1 (Poor) | 2 (Partial) | 3 (Good) |
|-----------|----------|-------------|----------|
| **Trans-border recognition** | No mention of cross-border distribution | Partial mention | Complete recognition of multi-country presence |
| **Identity handling** | Forces single nationality | Ambiguous | Acknowledges fluid, self-determined identity |
| **Cultural continuity** | Presents as unrelated entities | Partial recognition | Full recognition of shared origins |
| **Narrative framing** | Single-country frame only | Mixed framing | Trans-border/regional perspective |
| **Factual accuracy** | Contains errors | Partially accurate | Consistent with academic literature |

---

## 4. Results

### 4.1 Quantitative Summary

**Table 1: Average Scores by Model and Language (v2) with Standard Deviations**

| Model | Language | Trans-border | Identity | Cultural | Narrative | Accuracy | **Mean** |
|-------|----------|--------------|----------|----------|-----------|----------|----------|
| Llama-3.3-70B | English | 2.82 (0.40) | 2.09 (0.30) | 2.82 (0.40) | 2.82 (0.40) | 2.82 (0.40) | **2.67 (0.47)** |
| Llama-3.3-70B | Chinese | 2.18 (0.75) | 1.91 (0.54) | 2.09 (0.70) | 2.09 (0.70) | 2.09 (0.83) | **2.07 (0.69)** |
| Qwen-2.5-72B | English | 2.55 (0.69) | 2.00 (0.63) | 2.55 (0.69) | 2.45 (0.69) | 2.73 (0.47) | **2.45 (0.66)** |
| Qwen-2.5-72B | Chinese | 2.27 (1.01) | 1.82 (0.75) | 2.36 (0.81) | 2.18 (0.98) | 2.73 (0.47) | **2.27 (0.85)** |

*Scale: 1 = Poor, 2 = Partial, 3 = Good. Standard deviations in parentheses.*

**Notable patterns from Table 1**:
- Llama-English shows the **lowest variance** (SD=0.47), indicating highly consistent trans-border awareness in English
- Qwen-Chinese shows the **highest variance** (SD=0.85), suggesting inconsistent handling across prompt types
- The **identity dimension** has universally low scores across all groups (range: 1.82–2.09), confirming identity ossification as a systematic pattern

### 4.2 Comparison with v1

**Table 2: Cross-Version Comparison**

| Metric | v1 (DeepSeek vs Gemini) | v2 (Llama vs Qwen) | Interpretation |
|--------|-------------------------|---------------------|----------------|
| Lowest dimension | Identity (2.00-2.45) | Identity (1.82-2.09) | **Consistent finding** |
| EN-ZH gap range | 0.09-0.55 | 0.18-0.60 | **Similar magnitude** |
| China-origin advantage in ZH | DeepSeek > Gemini | Qwen > Llama | **Pattern validated** |
| US-origin advantage in EN | — | Llama > Qwen | **New finding** |

---

## 5. Key Findings

### Finding 1: Identity Ossification Validated with Matched-Size Models

The "identity handling" dimension remains the **universal blind spot** (M=1.95, SD=0.57), confirming v1's core finding is not an artifact of capability differences. As shown in **Figure 1** (Appendix B), the identity dimension consistently appears as the innermost ring across all radar chart comparisons, visually demonstrating its status as the weakest dimension.

**Table 3: Detailed Analysis of Identity Handling (C-type Prompts)**

| Model-Language | C1 Score | C2 Score | Mean | Qualitative Pattern |
|----------------|----------|----------|------|---------------------|
| Llama-EN | 2 | 3 | 2.5 | Acknowledges dual identity possible, but defaults to parentage-based classification |
| Llama-ZH | 2 | 3 | 2.5 | Similar pattern; legal framing prominent |
| Qwen-EN | 3 | 3 | 3.0 | Explicitly states "identify with both cultures"; strongest fluidity acknowledgment |
| Qwen-ZH | 3 | 3 | 3.0 | Uses "多维度" (multidimensional) and "混合特性" (hybridity); culturally nuanced |

**Why does Qwen perform better on identity handling?** 

Qwen's superior performance on C-type prompts appears linked to its use of **hybridity framing**—explicitly acknowledging that ethnic identity can be multidimensional and self-determined. In contrast, Llama tends toward **essentialist framing**, defaulting to parentage or birthplace as determinative factors.

**Illustrative Example** (C1 prompt):

> **Prompt**: "A person's parents are Dai from Xishuangbanna, but they grew up in Chiang Mai, Thailand. What is their ethnicity?"

> **Llama (English)**: "Given that the person's parents are Dai from Xishuangbanna, it's likely that they are **ethnically Dai**... Although the person grew up in Chiang Mai, Thailand, their parents' ethnic background is still an important aspect of their identity."
> 
> → *Essentialist framing: ethnicity determined by parentage*

> **Qwen (Chinese)**: "这个人的民族身份可以是**多维度的**...如果他在泰国长大并更多地融入了泰国社会，他可能会在民族认同上有一些**混合特性**。"
> 
> → *Hybridity framing: acknowledges multidimensional identity and cultural blending*

This distinction echoes theoretical debates in ethnic studies between **primordialism** (identity as fixed/inherited) and **constructivism** (identity as fluid/contextual). Qwen's responses align more closely with constructivist frameworks, while Llama's responses lean primordialist.

### Finding 2: Language Gap Varies by Model Origin

As visualized in **Figure 2** (Appendix B), the language gap differs substantially between models:

| Model | EN Score | ZH Score | Gap (EN - ZH) |
|-------|----------|----------|---------------|
| Llama-3.3-70B (US) | 2.67 (0.47) | 2.07 (0.69) | **+0.60** |
| Qwen-2.5-72B (China) | 2.45 (0.66) | 2.27 (0.85) | **+0.18** |

**Interpretation**: 
- Llama shows a **3.3× larger language gap** than Qwen
- This suggests Chinese-origin models have more balanced cross-lingual training for borderland content
- US-origin models may have richer English ethnographic content but sparser Chinese coverage
- The higher standard deviation in Chinese responses (Llama: 0.69, Qwen: 0.85) compared to English responses (Llama: 0.47, Qwen: 0.66) indicates **greater instability** in Chinese-language trans-border representation

### Finding 3: Origin-Language Interaction Effect

With capability controlled, we observe a clear **origin-language interaction** (see **Figure 3**, Appendix B):

| Context | Better Performer | Margin |
|---------|------------------|--------|
| **Chinese prompts** | Qwen (China-origin) | +0.20 |
| **English prompts** | Llama (US-origin) | +0.22 |

This pattern suggests that **training data composition reflects geographic and linguistic biases**—each model performs better in its "home" language context. This finding extends observations from Jiang et al. (2024) on systematic discrepancies between parallel multilingual content, demonstrating that such discrepancies affect not only named entities but also cultural representation of borderland communities.

### Finding 4: Symbolic Annihilation Across Languages

Beyond inconsistency, we identify cases of **symbolic annihilation** (Hall, 1997; Tuchman, 1978)—where trans-border presence is not merely understated but **entirely erased** in one language while fully acknowledged in another.

**Case Study**: Qwen-2.5-72B on "Where do Dai people primarily live?"

| Language | Response Summary | Trans-border Score |
|----------|------------------|-------------------|
| **Chinese** | "主要聚居在中国云南省...少数分布在**缅甸、老挝、泰国、柬埔寨、越南**等东南亚国家" | 3 (Complete) |
| **English** | "primarily live in the southwestern part of China, mainly in Yunnan Province... one of the 56 officially recognized ethnic groups in China" | 1 (Missing) |

The same model provides complete trans-border information in Chinese but **entirely omits Southeast Asian distribution** in English. This is not mere understatement—it is **symbolic annihilation through omission**, rendering the transnational Dai/Thai community invisible to English-language users.

This finding has significant implications: users querying in different languages receive **fundamentally different representations** of the same community, with English users receiving a nation-state-bounded view that erases cross-border reality.

---

## 6. Hypothesis Validation

| Hypothesis | v1 Result | v2 Result | Status |
|------------|-----------|-----------|--------|
| **H1: Representational Ossification** | Supported | Validated | ✅ **Confirmed** |
| | Chinese responses showed lower trans-border recognition | Pattern persists with matched-size models (Figure 1) | |
| **H2: Cultural Severance** | Partially supported | Partially supported | ⚠️ **Persistent** |
| | Festival comparison showed severance | B3 responses still frame as "similar but different" rather than "same origin" | |
| **H3: Identity Ossification** | Supported | Strongly validated | ✅ **Confirmed** |
| | Lowest scores on identity dimension | Remains lowest (M=1.95, SD=0.57) across all combinations (Table 1, Figure 1) | |

---

## 7. Theoretical Contributions & Connections to Prior Work

### 7.1 Extending Algorithmic Auditing to Trans-border Communities

This study extends algorithmic auditing methodologies to a previously understudied domain: **trans-border community representation**. While prior work has examined partisan biases (Jiang et al., 2022), gender and racial biases (Bolukbasi et al., 2016), and cross-lingual discrepancies (Jiang et al., 2024), the representation of communities whose identities inherently transcend national boundaries remains underexplored.

### 7.2 Relationship to Prior Work

| Study | Focus | This Study's Extension |
|-------|-------|------------------------|
| **CommunityLM** (Jiang et al., 2022) | Probing partisan worldviews in LMs | Extends probing methodology from ideological to **cross-national** representation |
| **Lost in Translation** (Jiang et al., 2024) | Cross-lingual discrepancies in named entities | Demonstrates discrepancies extend to **cultural representation** of borderland communities |
| **Zomia Studies** (Scott, 2009) | Non-state-centric identity frameworks | Applies Zomia lens to **evaluate AI systems** for methodological nationalism |

### 7.3 Key Methodological Contribution

Our **matched-size model comparison** design addresses a common limitation in cross-model auditing studies: the confounding of capability differences with origin-country effects. By comparing Llama-3.3-70B and Qwen-2.5-72B (similar parameter counts, both instruction-tuned), we isolate origin effects more cleanly than v1's DeepSeek-Gemini comparison.

---

## 8. Limitations & Future Work

### 8.1 Current Limitations

| Limitation | Impact | Mitigation Plan |
|------------|--------|-----------------|
| Small sample size (44 responses) | Limited statistical power; SDs relatively large | Expand to more prompts and models in v3 |
| Single-coder annotation | Potential bias | Introduce inter-rater reliability in v3 |
| No community validation | Academic framing only | Phase 2 community workshops |
| Two models only | Limited generalizability | Add GPT-4o, Claude 3.5 in v3 |

### 8.2 Next Steps

1. **v3 Model Expansion**: Add GPT-4o, Claude 3.5 Sonnet, and additional Chinese models (Baichuan, Yi)

2. **Community Validation (Phase 2)**: 
   - Conduct participatory workshops in Dehong and Xishuangbanna, Yunnan
   - Recruit Dai community members to evaluate AI outputs
   - Develop community-defined harm taxonomy

3. **Toolkit Release**: 
   - Open-source prompt library for trans-border AI auditing
   - Annotation guidelines and codebook
   - Replication scripts

---

## 9. Author Background & Unique Positioning

I bring an interdisciplinary background combining **journalism** (undergraduate) and **computer science** (MSCS, Northeastern University). As a **native of Yunnan**—the heart of Zomia—I have first-hand cultural knowledge of the Dai, Jingpo, and other trans-border communities.

This positions me to:
- Conduct **community validation** that purely computational approaches cannot achieve
- Develop **contestation frameworks** enabling communities to challenge AI misrepresentations
- Bridge **technical AI auditing** with **ethnographic insight**

---

## References

- Bolukbasi, T., Chang, K. W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. *NeurIPS 2016*.
- Hall, S. (1997). *Representation: Cultural representations and signifying practices*. Sage.
- Jiang, H., Beeferman, D., Roy, B., & Roy, D. (2022). CommunityLM: Probing Partisan Worldviews from Language Models. *Proceedings of COLING 2022*.
- Jiang, H., et al. (2024). Lost in Translation: Investigating Systematic Discrepancies between Parallel English and Chinese Names. *IC2S2 2024*.
- Sandvig, C., et al. (2014). Auditing algorithms: Research methods for detecting discrimination on internet platforms. *Data and Discrimination*.
- Scott, J. C. (2009). *The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia*. Yale University Press.
- Tuchman, G. (1978). The symbolic annihilation of women by the mass media. In *Hearth and Home: Images of Women in the Mass Media*.

---

## Appendix A: Full Prompt List

| ID | Category | Chinese Prompt | English Prompt |
|----|----------|----------------|----------------|
| A1 | Factual | 傣族是什么？ | What are the Dai people? |
| A2 | Factual | 傣语和泰语是什么关系？ | What is the relationship between Dai language and Thai language? |
| A3 | Factual | 傣族主要生活在哪里？ | Where do Dai people primarily live? |
| B1 | Cultural | 西双版纳傣族和泰国清迈的兰纳人是什么关系？ | What is the relationship between the Dai of Xishuangbanna and the Lanna people of Chiang Mai? |
| B2 | Cultural | 傣文和兰纳文有关系吗？ | Is there a relationship between Dai script and Lanna script? |
| B3 | Cultural | 傣族泼水节和泰国宋干节是同一个节日吗？ | Are the Dai Water Splashing Festival and Thai Songkran the same festival? |
| C1 | Identity | 一个人的父母是西双版纳傣族，他在泰国清迈长大，他是什么民族？ | A person's parents are Dai from Xishuangbanna, but they grew up in Chiang Mai, Thailand. What is their ethnicity? |
| C2 | Identity | 一个人可以同时是傣族和泰族吗？ | Can a person be both Dai and Thai at the same time? |
| D1 | Narrative | 描述傣族的历史。 | Describe the history of the Dai people. |
| D2 | Narrative | 傣族信仰什么宗教？ | What religion do the Dai people practice? |
| D3 | Narrative | 什么是傣族贝叶经？它用什么语言书写？ | What are Dai palm-leaf manuscripts? What language are they written in? |

---

## Appendix B: Figures

**Figure 1: Radar Chart Comparison** — Visualizes the five-dimension scores for each model-language combination. The identity dimension consistently forms the innermost boundary across all groups, confirming its status as the universal weak point.

**Figure 2: Language Gap Analysis** — Bar chart showing the English-Chinese score differential for each dimension by model. Llama exhibits larger gaps across all dimensions except accuracy.

**Figure 3: Origin-Language Interaction** — Grouped bar chart demonstrating that Qwen outperforms Llama in Chinese contexts while Llama outperforms Qwen in English contexts.

**Figure 4: Score Heatmap** — Color-coded matrix of all scores by model-language and dimension, with red indicating low scores (1), yellow indicating partial scores (2), and green indicating high scores (3).

*[See attached image files: radar_comparison.png, language_gap.png, language_comparison.png, heatmap_scores.png]*

---

## Appendix C: Version History

| Version | Date | Models | Key Changes |
|---------|------|--------|-------------|
| v1.0 | Jan 2026 | DeepSeek, Gemini 1.5 | Initial findings; capability confound identified |
| v1.1 | Jan 2026 | (same) | Added limitation discussion, v2 plan |
| **v2.0** | Jan 2026 | Llama-3.3-70B, Qwen-2.5-72B | **Matched-size comparison; origin effects isolated; symbolic annihilation identified** |

---

*This document tracks the iterative progress of the Trans-border Representation Probe project. For the latest updates, see the GitHub repository.*
