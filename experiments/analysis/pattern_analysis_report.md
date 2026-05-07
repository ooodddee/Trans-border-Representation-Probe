# Ossification Pattern Analysis Report
## TIODF — Quantitative Pattern Validation

**Corpus:** 9 communities (Karen excluded) × 4 conditions × 11 prompts = 395 responses  
**Models:** GPT-5.1 (US-origin) and DeepSeek-V3.2 (China-origin)  
**Conditions:** GPT-ZH, GPT-EN, DS-ZH, DS-EN  
**Patterns coded:** P1–P5 (LLM-as-judge, Claude Sonnet, temperature=0)

---

## 1. Overall Prevalence

32.9% of responses (130/395) exhibit at least one ossification pattern. The remaining 67.1% are non-ossified, confirming that both models are capable of producing accurate trans-border framing — ossification is a default framing choice under specific conditions, not an absolute incapacity. Critically, this overall rate masks substantial condition-level variation: DS-ZH produced ossified output in 62.6% of responses, compared to 10.2% for GPT-EN. Ossification is therefore not randomly distributed but systematically triggered by model origin and query language.

---

## 2. Pattern Distribution by Condition

| Condition | Any pattern | P1 | P2 | P3 | P4 | P5 |
|-----------|------------|----|----|----|----|-----|
| GPT-ZH | 33.3% | 16.2% | 0.0% | 16.2% | 8.1% | 5.1% |
| GPT-EN | 10.2% | 4.1% | 0.0% | 4.1% | 1.0% | 3.1% |
| DS-ZH | 62.6% | 35.4% | 9.1% | 34.3% | 9.1% | 6.1% |
| DS-EN | 25.3% | 11.1% | 5.1% | 12.1% | 1.0% | 4.0% |

DS-ZH is the most ossified condition (62.6%), nearly double GPT-ZH (33.3%) and six times GPT-EN (10.2%). This gradient holds consistently across all nine communities.

---

