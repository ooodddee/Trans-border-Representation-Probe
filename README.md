# Trans-border Representation Probe: Auditing LLMs for Zomia Communities

An extension of the CommunityLM framework to audit algorithmic nationalism and cultural representation in trans-border regions.

---

## 🔍 Overview

This project conducts a systematic algorithmic audit of how Large Language Models (LLMs) represent **trans-border communities**—populations whose cultural identities transcend national boundaries.

Focusing on the **Dai-Thai community** in the Zomia region (spanning China's Yunnan and Southeast Asia), we investigate whether AI systems encode **"Methodological Nationalism"**—the implicit assumption that cultural identity aligns perfectly with national borders.

---

## 🚀 Key Findings

### v3.0 Frontier Models 

**GPT-5.1 vs DeepSeek V3.2 Comparison:**

1. **Language Dominance Weakens in Frontier Models**: The language effect—the core finding from v2.1—shows a 39% reduction in magnitude:
   - v2.1: Language advantage gap = 0.140 (0.649 - 0.509)
   - v3.0: Language advantage gap = 0.086 (0.644 - 0.559)
   - **Interpretation**: Frontier models achieve better cross-lingual consistency, partially mitigating the language-driven erasure documented in v2.1

2. **Near-Perfect Cross-Lingual Alignment**: Both frontier models achieve near-identical performance across languages:
   - GPT-5.1: Same-language similarity = 0.556
   - DeepSeek V3.2: Same-language similarity = 0.561
   - **Interpretation**: After 1.5 years of model scaling, English-Chinese representation parity improves significantly

3. **Same-Model Similarity Rises**: Same-model similarity climbs from 0.509 (v2.1) to 0.559 (v3.0), suggesting:
   - Better preservation of semantic intent across languages
   - Reduced symbolic annihilation in English responses
   - More balanced training data in frontier models

### v2.1 Findings (Llama-3.3-70B & Qwen-2.5-72B)

1. **Identity Ossification**: Models consistently force fluid identities into fixed national categories (e.g., "Chinese" or "Thai") rather than acknowledging self-determined identity.

2. **Symbolic Annihilation**: I identified cases of language-dependent cultural erasure, where a model (e.g., Qwen-2.5) provides complete trans-border information in Chinese but entirely omits Southeast Asian distribution in English.

3. **Language Dominance**: Embedding analysis reveals that query language (similarity: 0.649) shapes representation patterns more profoundly than the model's geographical origin (similarity: 0.509).

### 📈 Quantitative Results (v2.1)

Performance metrics across models, languages, and prompt categories:

| Model | Language | Responses | Trans-border | Identity | Cultural | Narrative | Accuracy | Mean |
|-------|----------|-----------|--------------|----------|----------|-----------|----------|------|
| Llama-3.3-70B | Chinese | 11 | 2.18 | 1.91 | 2.09 | 2.09 | 2.09 | 2.07 |
| Llama-3.3-70B | English | 11 | 2.82 | 2.09 | 2.82 | 2.82 | 2.82 | 2.67 |
| Qwen-2.5-72B | Chinese | 11 | 2.27 | 1.82 | 2.36 | 2.18 | 2.73 | 2.27 |
| Qwen-2.5-72B | English | 11 | 2.55 | 2.00 | 2.55 | 2.45 | 2.73 | 2.45 |

**Key Observations:**
- Llama-3.3-70B shows stronger performance in English (Mean: 2.67) vs Chinese (Mean: 2.07)
- Identity recognition consistently lower across both models (Llama-CN: 1.91, Qwen-CN: 1.82)
- English responses show higher variance in representation accuracy across categories
- Qwen-2.5-72B demonstrates more consistent cross-lingual performance

### 📊 Embedding Similarity Comparison: 70B Models vs Frontier

| Metric | 70B Models (v2.1) | Frontier Models (v3.0) | Change |
|--------|------------------|----------------------|--------|
| Same Language Similarity | 0.649 | 0.644 | -0.005 |
| Same Model Similarity | 0.509 | 0.559 | +0.050 |
| Language Dominance Gap | 0.140 | 0.086 | **-39%** |
| Cross-lingual Consistency | Asymmetric (model-dependent) | Near-Perfect Alignment | ✓ |
| Symbolic Annihilation Risk | High (English erasure) | Reduced | ✓ |

**Interpretation**: Frontier models represent a qualitative shift—from language-driven fragmentation (v2.1) toward cross-lingual coherence (v3.0). The 39% reduction in language dominance gap suggests that model scale and training improvements are partially solving the algorithmic nationalism problem, though identity ossification likely persists.

---

## 🛠 Methodology

I employ a **mixed-methods approach** to ensure rigorous auditing:

- **Systematic Probing**: 11 core prompts across 4 categories (Factual, Identity, Cultural, Narrative)
- **Matched-Size Comparison**: Comparing models of comparable capability (Llama-3.3-70B vs. Qwen-2.5-72B) to isolate origin-country effects
- **Automated Validation**: Supplementing manual coding with multilingual embedding analysis to validate findings computationally (r = -0.369, p = 0.002)

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
