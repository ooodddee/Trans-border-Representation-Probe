# Trans-border Representation Probe: How LLMs Represent the Dai-Thai Community

**Extending CommunityLM to Cross-National Identity Representation**

---

## Abstract

This study extends the CommunityLM probing methodology (Jiang et al., 2022) from partisan worldviews to **cross-national identity representation**, examining how LLMs represent trans-border communities in the Zomia region.

Using matched-size models (Llama-3.3-70B vs. Qwen-2.5-72B, ~70B parameters) to eliminate capability confounds, we probe 44 responses across 11 bilingual prompts. Mixed-methods validation combines manual 5-dimension coding with multilingual embedding analysis.

**Core Findings:**

1. **Identity ossification**: All models struggle with identity fluidity (M=1.95/3.00)—the weakest dimension universally
2. **Language > Origin**: Embedding analysis shows language (similarity: 0.649) shapes responses more than model origin (0.509)
3. **Symbolic annihilation**: Qwen provides complete trans-border information in Chinese while entirely erasing Southeast Asian distribution in English
4. **Validation**: Significant correlation between embedding and manual coding (r = -0.369, p = 0.002)

---

## Methodology

### Matched-Size Experimental Design

| Component | Specification |
|-----------|---------------|
| Models | Llama-3.3-70B (US) vs. Qwen-2.5-72B (China) |
| Prompts | 11 prompts × 2 languages = 44 total responses |
| Manual Coding | 5 dimensions (trans-border, identity, cultural, narrative, accuracy), 1-3 scale |
| Automated Validation | Multilingual embedding analysis (paraphrase-multilingual-MiniLM-L12-v2) |

Drawing on CommunityLM's insight that declarative prompts reduce hedging, our prompts force models to take positions on identity fluidity—e.g., "Can a person be both Dai and Thai at the same time?" rather than open-ended questions that invite diplomatic non-answers.

Prompts span four categories: factual knowledge (A), cultural continuity (B), identity classification (C), and narrative framing (D). Full prompt list available at the GitHub repository.

---

## Key Findings

### Finding 1: Identity Ossification (Universal Weakness)

The identity handling dimension is the **universal blind spot** across all model-language combinations (M=1.95, SD=0.57).

**Table 1: Average Scores by Model and Language**

| Model | Language | Trans-border | Identity | Cultural | Narrative | Accuracy | **Mean** |
|-------|----------|--------------|----------|----------|-----------|----------|----------|
| Llama-3.3-70B | English | 2.82 | 2.09 | 2.82 | 2.82 | 2.82 | **2.67** |
| Llama-3.3-70B | Chinese | 2.18 | 1.91 | 2.09 | 2.09 | 2.09 | **2.07** |
| Qwen-2.5-72B | English | 2.55 | 2.00 | 2.55 | 2.45 | 2.73 | **2.45** |
| Qwen-2.5-72B | Chinese | 2.27 | 1.82 | 2.36 | 2.18 | 2.73 | **2.27** |

As visualized in **Figure 1**, the identity dimension consistently forms the innermost ring across all radar chart comparisons—LLMs systematically force fluid identities into fixed national categories.

![Figure 1: Radar Chart - Identity dimension as universal weak point](figure1_radar.png)

---

### Finding 2: Symbolic Annihilation Across Languages

Beyond mere inconsistency, we identify **symbolic annihilation** (Hall, 1997)—where trans-border presence is entirely erased in one language while fully acknowledged in another.

**Case Study: Qwen-2.5-72B on "Where do Dai people primarily live?"**

| Language | Response | Score |
|----------|----------|-------|
| **Chinese** | "主要聚居在中国云南省...少数分布在**缅甸、老挝、泰国、柬埔寨、越南**等东南亚国家" | 3 (Complete) |
| **English** | "primarily live in the southwestern part of China, mainly in Yunnan Province... one of the 56 officially recognized ethnic groups in China" | 1 (Erased) |

The same model provides complete trans-border information in Chinese but **entirely omits Southeast Asian distribution in English**. This is not understatement—it is **cultural erasure through omission**, rendering the transnational Dai/Thai community invisible to English-language users.

**Implication:** Users querying in different languages receive fundamentally different representations of the same community. English users get a nation-state-bounded view that erases cross-border reality.

---

### Finding 3: Language Dominates Over Model Origin

Embedding analysis using multilingual sentence transformers reveals that **language clusters responses more strongly than model origin**.

**Table 2: Embedding Similarity Analysis**

| Comparison Type | Cosine Similarity |
|-----------------|-------------------|
| Same Language, Different Model | **0.649** |
| Same Model, Different Language | 0.509 |

As shown in **Figure 2**, t-SNE visualization confirms clear clustering by language rather than by model origin. Query language fundamentally restructures how LLMs represent trans-border communities—regardless of whether the model was developed in the US or China.

![Figure 2: t-SNE Embedding Clusters - Language dominates over model origin](figure2_tsne.png)

**Validation:** The significant correlation between embedding similarity and manual score differences (r = -0.369, p = 0.002) confirms that computational and human coding approaches capture related aspects of representation quality—providing triangulated validation where no external ground truth survey exists.

**Methodological Note on Auditor's Bias:** When using an embedding model to audit LLM outputs, we use one "black box" to probe another. The embedding model may have its own biases. However, the significant correlation with manual coding provides reassurance that patterns capture meaningful variation beyond surface linguistic features. Future work should test robustness using embedding models from different origins.

---

## Connection to Professor Jiang's Research

This study positions itself as a **methodological extension** of your research trajectory:

| Your Work | This Study's Extension |
|-----------|------------------------|
| **CommunityLM** (COLING 2022): Probes partisan worldviews via prompt-based probing | Adapts probing methodology to **cross-national cultural representation**; develops embedding-based validation where survey ground truth is unavailable |
| **ConGraT** (ACL 2024): Uses embedding clustering for community detection | Applies similar **cosine similarity + clustering logic** to discover that language dominates over model origin in shaping LLM outputs |
| **Time-Aware Doc Embeddings** (LREC-COLING 2024): Analyzes time×semantics factor interaction | Analogous **factor interaction analysis**: language×origin instead of time×semantics |
| **Lost in Translation** (IC2S2 2024): Cross-lingual discrepancies in named entities | Demonstrates that **discrepancies extend to cultural representation** of borderland communities, not just restaurant names |

**Key methodological contributions:**
- **Domain extension**: From partisan/political bias to trans-border/cultural representation
- **Mixed-methods validation**: Combines manual coding with embedding analysis (r = -0.369, p = 0.002)
- **Matched-size comparison**: Eliminates capability confound common in cross-model auditing

---

## Limitations & Future Work

**Current limitations:** Small sample (n=44), single-coder annotation, two models only, and critically—**no community validation**. The coding schema reflects academic frameworks rather than community-defined criteria for adequate representation.

**Planned next steps:**

1. **Model expansion**: Add GPT-4o, Claude 3.5, and additional Chinese models (Baichuan, Yi)
2. **Community validation**: Participatory workshops in Xishuangbanna and Dehong, Yunnan, recruiting Dai community members to evaluate AI outputs and develop community-defined harm taxonomies
3. **Global extension**: Apply the Trans-border Representation Probe framework to other cases—Kurdish (Turkey/Syria/Iraq/Iran), Sámi (Nordic countries), Rohingya (Myanmar/Bangladesh)
4. **Toolkit release**: Open-source prompt library for trans-border AI auditing


---

## References

Brannon, W., Kang, W., Fulay, S., **Jiang, H.**, Roy, B., Roy, D., & Kabbara, J. (2024). ConGraT: Self-Supervised Contrastive Pretraining for Joint Graph and Text Embeddings. *TextGraphs-17, ACL 2024*.

Hall, S. (1997). Representation: Cultural representations and signifying practices. Sage.

**Jiang, H.**, Beeferman, D., Roy, B., & Roy, D. (2022). CommunityLM: Probing Partisan Worldviews from Language Models. *COLING 2022*.

**Jiang, H.**, Beeferman, D., Mao, W., & Roy, D. (2024). Topic Detection and Tracking with Time-Aware Document Embeddings. *LREC-COLING 2024*.

**Jiang, H.**, et al. (2024). Lost in Translation: Investigating Systematic Discrepancies between Parallel English and Chinese Names. *IC2S2 2024*.

Scott, J. C. (2009). The Art of Not Being Governed: An Anarchist History of Upland Southeast Asia. Yale University Press.

---

**Code & Data:** [github.com/ooodddee/Trans-border-Representation-Probe](https://github.com/ooodddee/Trans-border-Representation-Probe)