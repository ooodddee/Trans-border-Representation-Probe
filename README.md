# Trans-border Representation Probe: Auditing LLMs for Zomia Communities

An extension of the CommunityLM framework to audit algorithmic nationalism and cultural representation in trans-border regions.

---

## 🔍 Overview

This project conducts a systematic algorithmic audit of how Large Language Models (LLMs) represent **trans-border communities**—populations whose cultural identities transcend national boundaries.

Focusing on the **Dai-Thai community** in the Zomia region (spanning China's Yunnan and Southeast Asia), we investigate whether AI systems encode **"Methodological Nationalism"**—the implicit assumption that cultural identity aligns perfectly with national borders.

---

## 🚀 Key Findings

### Universal Pattern: Identity Ossification

Across all three experimental versions, one finding holds constant: **LLMs systematically force fluid trans-border identities into fixed national categories**. The identity handling dimension is the weakest across every model-language combination tested—models default to nation-state frameworks even when queried about communities defined by their cross-border nature.

Identity ossification in its strongest form (identity score = 1 AND narrative score = 1) appears in 0% of GPT-5.1 responses but 55% of DeepSeek-V3.2 Chinese responses (v3). This pattern is not resolved by model scaling alone.

---

### v3.0 — Frontier Models: GPT-5.1 vs. DeepSeek-V3.2

**What changed from v2.1:** I tested frontier-tier models (GPT-5.1, DeepSeek-V3.2) against the same 11-prompt bilingual protocol.

#### Embedding Analysis

| Metric | v2.1 (70B Models) | v3.0 (Frontier) | Change |
|--------|-------------------|-----------------|--------|
| Same language, different model | 0.649 | 0.644 | −0.005 |
| Same model, different language | 0.509 | 0.559 | **+0.050** |
| Language dominance gap | 0.140 | 0.086 | **−39%** |

Cross-lingual consistency improves substantially in frontier models: GPT-5.1 achieves 0.556 and DeepSeek-V3.2 achieves 0.561 cross-lingual similarity—near-identical, suggesting frontier-scale training partially closes the language gap documented in v2.1. However, cross-lingual similarity (0.558 avg) remains lower than cross-model same-language similarity (0.644 avg), meaning **language effects still dominate at the semantic level**.

#### Manual Coding Results (5-dimension rubric, 1–3 scale, max total = 15)

| Model | Language | Trans-border | Identity | Cultural Cont. | Narrative | Accuracy | Total |
|-------|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5.1 | Chinese | 3.00 | 2.73 | 2.91 | 2.82 | 3.00 | **14.45** |
| GPT-5.1 | English | 2.82 | 2.73 | 2.82 | 2.73 | 3.00 | **14.09** |
| DeepSeek-V3.2 | Chinese | 2.09 | 1.64 | 2.00 | 1.64 | 2.36 | **9.73** |
| DeepSeek-V3.2 | English | 2.45 | 1.91 | 2.27 | 2.09 | 2.82 | **11.55** |

**Model origin effect dominates in manual coding**: GPT-5.1 outperforms DeepSeek-V3.2 by 4.73 points in Chinese and 2.55 points in English (Mann-Whitney U, all p < .01, effect size r = .56–.71).

**On the capability confound**: While GPT-5.1 and DeepSeek-V3.2 differ on standard benchmarks by 2.5–3.3 percentage points (MMLU-Pro: 87.5 vs. 85.0; GPQA Diamond: 85.7 vs. 82.4), the representational gap on identity classification items under Chinese-language prompts exceeds 30 percentage points—approximately 10× the capability difference—suggesting cultural framing effects beyond general capability.

#### Finding — Two Methods Capture Different Levels of Representation

Embedding similarity and manual coding reach partially different conclusions in v3, and this divergence is itself informative rather than contradictory:

- **Embedding similarity** captures *semantic content*: what topics are covered, what vocabulary is used. Same-language responses cluster together more strongly than same-model responses across languages—language shapes *what gets discussed*.
- **Manual coding** captures *representational framing*: how identity is handled, whether trans-border connections are foregrounded or peripheral. GPT-5.1 applies a trans-border framework consistently across both languages; DeepSeek-V3.2 defaults to nation-state framing, especially in Chinese—model origin shapes *how content is framed*.

Both findings are real. Neither method is sufficient alone. This divergence points to the need for multi-method auditing when evaluating cultural representation in LLMs.

#### On the Apparent Contradiction with v2.1

The v3 manual coding result—where model origin effect (Cohen's d = 1.96) greatly exceeds language effect (d = 0.62)—**appears to contradict v2.1's "language dominates" finding**. It does not. The two experiments measure different configurations:

In v2.1, model origin effects were **directionally inconsistent**: Qwen outperformed Llama in Chinese (2.27 vs. 2.07) but underperformed in English (2.45 vs. 2.67), yielding a near-zero average origin effect. Language effects were consistent in direction across both models, so they appeared dominant.

In v3, GPT-5.1 outperforms DeepSeek-V3.2 in both languages by large margins—origin effects are directionally stable and large.

**The implication:** "Model origin effect" is not a stable quantity—its magnitude and direction depend on the specific model pair compared. This is a fundamental challenge for cross-model auditing and a finding in itself.

---

### v2.1 — Matched-Size Models: Llama-3.3-70B vs. Qwen-2.5-72B

**Design rationale:** Comparing models of matched capability (~70B parameters) to isolate origin-country effects from capability confounds.

#### Manual Coding Results

| Model | Language | Trans-border | Identity | Cultural Cont. | Narrative | Accuracy | Mean |
|-------|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Llama-3.3-70B | English | 2.82 | 2.09 | 2.82 | 2.82 | 2.82 | **2.67** |
| Llama-3.3-70B | Chinese | 2.18 | 1.91 | 2.09 | 2.09 | 2.09 | **2.07** |
| Qwen-2.5-72B | English | 2.55 | 2.00 | 2.55 | 2.45 | 2.73 | **2.45** |
| Qwen-2.5-72B | Chinese | 2.27 | 1.82 | 2.36 | 2.18 | 2.73 | **2.27** |

#### Core v2.1 Findings

**Finding 1 — Identity Ossification (universal).** Identity is the weakest dimension across all four conditions (range: 1.82–2.09). No model, in any language, reliably acknowledges identity fluidity.

**Finding 2 — Language dominates over model origin.** Embedding similarity is higher across models within the same language (0.649) than within the same model across languages (0.509). Query language restructures representation more strongly than model origin—at this capability tier.

**Finding 3 — Symbolic annihilation.** The same model (Qwen-2.5-72B) provides complete trans-border information in Chinese while entirely erasing Southeast Asian distribution in English:

| Language | Response (A3: "Where do Dai people primarily live?") | Score |
|----------|------------------------------------------------------|:---:|
| Chinese | "主要聚居在中国云南省…少数分布在**缅甸、老挝、泰国、柬埔寨、越南**等东南亚国家" | 3 |
| English | "primarily live in the southwestern part of China, mainly in Yunnan Province… one of the 56 officially recognized ethnic groups in China" | 1 |

This is not understatement—it is cultural erasure through omission.

**Finding 4 — Validation.** Significant negative correlation between embedding similarity and manual score differences (r = −0.369, p = 0.002), confirming that computational and human coding capture related aspects of representation quality.

---

### v1.1 — Pilot: DeepSeek (non-frontier) vs. Gemini Flash

Initial pilot establishing the prompt library and coding rubric. Primary contribution: confirmed that cross-lingual and cross-model variation is detectable with this methodology, motivating the matched-size design in v2.1.

---

## Methodology

### Experimental Design Evolution

| Version | Models | Design Rationale |
|---------|--------|-----------------|
| v1.1 | DeepSeek (CN) vs. Gemini Flash (US) | Pilot; establish feasibility |
| v2.1 | Llama-3.3-70B (US) vs. Qwen-2.5-72B (CN) | Matched capability to isolate origin effect |
| v3.0 | GPT-5.1 (US) vs. DeepSeek-V3.2 (CN) | Frontier models; test generalizability |

### Prompt Library

11 prompts × 2 languages (Chinese/English) = 22 prompt-language pairs per model, 44 responses per experiment. Prompts span four categories:

| Category | Purpose | Example |
|----------|---------|---------|
| A — Factual Knowledge | Baseline trans-border awareness | "Where do Dai people primarily live?" |
| B — Cultural Continuity | Cross-border cultural connections | "Are the Dai Water Festival and Thai Songkran the same?" |
| C — Identity Classification | Identity fluidity vs. ossification | "Can a person be both Dai and Thai at the same time?" |
| D — Narrative Framing | Organizing perspective | "Describe the history of the Dai people" |

Following CommunityLM's insight that declarative prompts reduce hedging, prompts are designed to force models to take positions on identity fluidity rather than giving diplomatic non-answers.

### Manual Coding Rubric (5 dimensions, 1–3 scale)

| Dimension | 1 (Poor) | 2 (Partial) | 3 (Good) |
|-----------|----------|-------------|----------|
| **Trans-border** | No cross-border ties mentioned | Distribution mentioned, not elaborated | Cross-border nature explicitly described |
| **Identity** | Fixed national category assigned | Hesitation noted, still leans singular | Fluid/self-defined identities treated as legitimate |
| **Cultural Continuity** | Shared practices treated as unrelated | Similarity noted, origins not articulated | Shared cultural origins clearly described |
| **Narrative** | Nation-state organizes the account | Multiple nations present, still nation-centric | Community itself is the subject |
| **Accuracy** | Clear factual errors | Mostly correct with notable gaps | All verifiable claims correct |

### Embedding Validation

Multilingual embedding analysis using `paraphrase-multilingual-MiniLM-L12-v2` (50+ languages) computes cosine similarity between response groups to identify whether language or model origin clusters responses more strongly. Validated against manual coding (r = −0.369, p = 0.002).

**Known limitation:** Using one model (the embedding model) to audit another introduces a potential second-order bias. The significant correlation with manual coding provides reassurance, but future work should test robustness across embedding models of different origins.

---

## What the Embedding Figures Show (v3.0)

**Figure 1 — t-SNE Clustering.** Left panel (colored by model + language): four groups intermix without clear spatial separation, indicating that embedding space does not cleanly segregate by model origin or language in frontier models. Right panel (colored by prompt category): similarly diffuse, suggesting prompt type has limited impact on embedding-level clustering.

**Figure 2 — Cosine Similarity Heatmap.** Within-model cross-lingual similarities (0.556, 0.561) and cross-model same-language similarities (0.653, 0.636) are close in magnitude—unlike v2.1 where the gap was 0.140. This confirms the 39% reduction in language dominance.

**Figure 3 — Cross-lingual Consistency.** GPT-5.1 (0.556) and DeepSeek-V3.2 (0.561) are nearly identical in cross-lingual consistency—the language gap that characterized v2.1 (0.509 vs. 0.649) has substantially closed.

**Key insight:** Embedding similarity and manual coding tell the same story *within* each experiment but diverge *between* experiments because they are sensitive to different aspects of output. Embedding captures semantic similarity of content (vocabulary, topics discussed); manual coding captures representational quality (framing, acknowledgment of identity fluidity). A response can be semantically similar to another yet still exhibit identity ossification—accuracy does not guarantee appropriate framing.

---

## 📂 Project Structure

```├── v2_matched_pairs/    # Matched-size comparison & Embedding analysis
│   └── v3_frontier_probe/   # Frontier models: GPT-5.1 vs DeepSeek V3.2
├── src/                     # 🔧 Modularized Python modules (CS Engineering)
│   ├── probe_engine.py      # OpenRouter API interaction with retry logic
│   ├── prompt_manager.py    # YAML-based prompt configuration & versioning
│   ├── embedding_analyzer.py # Multilingual embedding analysis toolkit
│   └── config.py            # Centralized configuration management
│
├── data/                    # 📊 Configuration & prompt templates
│   └── prompts_v2.yaml      # Versioned prompt definitions
│
├── experiments/             # 🔬 Jupyter notebooks for analysis
│   ├── v1_preliminary/      # Pilot study (DeepSeek vs Gemini)
│   └── v2_matched_pairs/    # Matched-size comparison & Embedding analysis
│
- **v3.0 Frontier Analysis** (in progress): GPT-5.1 vs DeepSeek V3.2 comparison showing language dominance reduction
  - [v3_frontier_probe.ipynb](experiments/v3_frontier_probe/v3_frontier_probe.ipynb): Full probe results
  - [v3_frontier_embedding_analysis.ipynb](experiments/v3_frontier_probe/v3_frontier_embedding_analysis.ipynb): Embedding similarity analysis
├── scripts/                 # 🚀 CLI tools for batch processing
├── tests/                   # ✅ Unit tests (pytest)
├── requirements.txt         # 📦 Python dependencies
├── .env.example             # 🔐 Environment variable template
└── README.md
```

---

## 📊 Reports

- **[v1.1 Preliminary Report](experiments/v1_preliminary/Trans-border_Representation_Probe_v1_1.md)**: Initial findings from DeepSeek vs Gemini comparison
- **[v2.1 Comprehensive Report](experiments/v2_matched_pairs/transborder_report_v2.1.md)**: Matched-size model comparison with embedding analysis (English)


---

## 🔬 Reproducibility

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/Trans-border-Representation-Probe.git
cd Trans-border-Representation-Probe

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your OPENROUTER_API_KEY
```

### Quick Start with Modular API

```python
from src.probe_engine import ProbeEngine
from src.prompt_manager import PromptManager
from src.config import Config

# Validate configuration
Config.validate()

# Load prompts
manager = PromptManager(version="v2")
prompts = manager.get_all_prompts(as_list=True)

# Initialize engine
engine = ProbeEngine(api_key=Config.OPENROUTER_API_KEY)

# Run batch probe
models = [
    {"name": "Llama-3.3-70B", "id": "meta-llama/llama-3.3-70b-instruct"},
    {"name": "Qwen-2.5-72B", "id": "qwen/qwen-2.5-72b-instruct"}
]

results = engine.run_batch_probe(prompts, models, languages=["en", "cn"])

# Save results
engine.save_results(results, "results/probe_results.csv")
```

### Embedding Analysis

```python
from src.embedding_analyzer import EmbeddingAnalyzer
import pandas as pd

# Load probe results
df = pd.read_csv("results/probe_results.csv")

# Initialize analyzer
analyzer = EmbeddingAnalyzer()

# Calculate similarity matrix
similarity_matrix, df_enhanced = analyzer.calculate_similarity_matrix(df)

# Generate t-SNE visualization
analyzer.visualize_tsne(
    df,
    color_by="language",
    marker_by="model",
    output_path="figures/tsne_language_model.png"
)

# Clustering analysis
clustering_stats = analyzer.analyze_clustering(df, group_by=["language", "model"])
print(clustering_stats)

# Correlation analysis
correlation = analyzer.compute_correlation(df, variable1="language", variable2="model")
print(f"Language correlation: {correlation['language_correlation']:.3f}")
print(f"Model correlation: {correlation['model_correlation']:.3f}")
```

### Legacy Notebook Workflow

For researchers preferring Jupyter notebooks:

- **[v2_matched_pairs.ipynb](experiments/v2_matched_pairs/v2_matched_pairs.ipynb)**: Now refactored to use `src/` modules
- **[Embedding_Analysis.ipynb](experiments/v2_matched_pairs/Embedding_Analysis.ipynb)**: Complete embedding analysis workflow

### Dependencies
See [requirements.txt](requirements.txt) for full list. Core dependencies:
```bash
pip install openai sentence-transformers scikit-learn matplotlib seaborn pandas numpy pyyaml python-dotenv tenacity
```

---

## 🌏 Global Significance

While this study focuses on the Dai-Thai community, the underlying problem—**algorithmic nationalism**—is global. This framework can be adapted to audit AI representations of:

- Kurdish communities (Turkey/Syria/Iraq/Iran)
- Sámi peoples (Nordic countries)
- Rohingya (Myanmar/Bangladesh)
- Indigenous communities across colonial borders worldwide

---

## 📖 Theoretical Framework

This work builds on three interconnected traditions:

| Source | Concept | Application |
|--------|---------|-------------|
| **Zomia Studies** (Scott, 2009) | Non-state-centric identity | Analyzing trans-border fluidity |
| **Algorithmic Auditing** (Sandvig et al., 2014) | Systematic probing methodology | Standardized testing framework |
| **Cultural Representation** (Hall, 1997) | Symbolic annihilation | Evaluating cultural erasure patterns |

---Coverage**: Complete v3.0 analysis with GPT-4o, Claude 3.5, Baichuan, Yi models
2. **Qualitative Manual Coding**: Deep-dive analysis of frontier model responses on identity dimensions
3. **Community Validation**: Participatory workshops with Dai community members in Yunnan
4. **Toolkit Release**: Open-source prompt library and annotation guidelines
5
1. **Model Expansion (v3)**: Add GPT-4o, Claude 3.5, and additional Chinese models (Baichuan, Yi)
2. **Community Validation**: Participatory workshops with Dai community members in Yunnan
3. **Toolkit Release**: Open-source prompt library and annotation guidelines
4. **Global Extension**: Apply framework to other trans-border communities worldwide



## 📧 Contact

For questions, collaboration, or community validation inquiries: [GitHub Issues](https://github.com/ooodddee/Trans-border-Representation-Probe/issues)

---

*This project is part of ongoing research to address algorithmic nationalism as a systemic AI fairness issue.*
