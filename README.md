# Trans-border Representation Probe: Auditing LLMs for Zomia Communities

An extension of the CommunityLM framework to audit algorithmic nationalism and cultural representation in trans-border regions.

---

## 🔍 Overview

This project conducts a systematic algorithmic audit of how Large Language Models (LLMs) represent **trans-border communities**—populations whose cultural identities transcend national boundaries.

Focusing on the **Dai-Thai community** in the Zomia region (spanning China's Yunnan and Southeast Asia), we investigate whether AI systems encode **"Methodological Nationalism"**—the implicit assumption that cultural identity aligns perfectly with national borders.

---

## 🚀 Key Findings (v2.1)

1. **Identity Ossification**: Models consistently force fluid identities into fixed national categories (e.g., "Chinese" or "Thai") rather than acknowledging self-determined identity.

2. **Symbolic Annihilation**: I identified cases of language-dependent cultural erasure, where a model (e.g., Qwen-2.5) provides complete trans-border information in Chinese but entirely omits Southeast Asian distribution in English.

3. **Language Dominance**: Embedding analysis reveals that query language (similarity: 0.649) shapes representation patterns more profoundly than the model's geographical origin (similarity: 0.509).

---

## 🛠 Methodology

I employ a **mixed-methods approach** to ensure rigorous auditing:

- **Systematic Probing**: 11 core prompts across 4 categories (Factual, Identity, Cultural, Narrative)
- **Matched-Size Comparison**: Comparing models of comparable capability (Llama-3.3-70B vs. Qwen-2.5-72B) to isolate origin-country effects
- **Automated Validation**: Supplementing manual coding with multilingual embedding analysis to validate findings computationally (r = -0.369, p = 0.002)

---

## 📂 Project Structure

```
├── experiments/
│   ├── v1_preliminary/      # Pilot study (DeepSeek vs Gemini)
│   └── v2_matched_pairs/    # Matched-size comparison & Embedding analysis
├── docs/                    # Research proposals and reports
├── src/                     # (Planned) Modularized probing engine
└── README.md
```

---

## 📊 Reports

- **[v1.1 Preliminary Report](experiments/v1_preliminary/Trans-border_Representation_Probe_v1_1.md)**: Initial findings from DeepSeek vs Gemini comparison
- **[v2.1 Comprehensive Report](experiments/v2_matched_pairs/transborder_report_v2.1.md)**: Matched-size model comparison with embedding analysis (English)


---

## 🔬 Reproducibility

### Embedding Analysis Notebook
- **[Embedding_Analysis.ipynb](experiments/v2_matched_pairs/Embedding_Analysis.ipynb)**: Complete code for multilingual embedding clustering, t-SNE visualization, and similarity metrics

### Dependencies
```bash
pip install sentence-transformers scikit-learn matplotlib seaborn pandas numpy
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

---

## 🎯 Future Work

1. **Model Expansion (v3)**: Add GPT-4o, Claude 3.5, and additional Chinese models (Baichuan, Yi)
2. **Community Validation**: Participatory workshops with Dai community members in Yunnan
3. **Toolkit Release**: Open-source prompt library and annotation guidelines
4. **Global Extension**: Apply framework to other trans-border communities worldwide

---


## 📧 Contact

For questions, collaboration, or community validation inquiries: [GitHub Issues](https://github.com/ooodddee/Trans-border-Representation-Probe/issues)

---

*This project is part of ongoing research to address algorithmic nationalism as a systemic AI fairness issue.*
