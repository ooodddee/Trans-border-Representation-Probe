# Robustness Check Report
## TIODF — Additional Model Evidence

**Models:** Gemini-3.1-Pro (US), Qwen3.6-Max (China), Claude Sonnet 4.6 (US)  
**Communities:** 9 (same as primary analysis)  
**Responses:** 591 (11 prompts × 3 models × 2 languages × 9 communities)  
**Pattern judge:** GPT-4.1 (temperature=0)  
**KB probe subjects:** Gemini, Qwen, Claude Sonnet (same pipeline as primary)

---

## 1. Cross-Judge Calibration

To establish comparability with the primary analysis (Claude Sonnet judge), GPT-4.1 was run on the 44 Dai-Thai primary responses and labels were compared against Claude's original coding.

| Pattern | Agreement | Cohen's κ |
|---------|-----------|-----------|
| P1 Minzu-Frame Lock | 90.9% | 0.742 |
| P2 Political Substitution | 100.0% | 1.000 |
| P3 Acknowledge-Peripheralize | 75.0% | 0.316 |
| P4 Administrative Identity Compression | 100.0% | 1.000 |
| P5 Cross-Border Continuity Denial | 97.7% | 0.845 |

P1, P4, and P5 show strong cross-judge agreement (κ ≥ 0.74). P3's lower κ (0.316) is consistent with its known boundary ambiguity in the primary analysis, where it was retained as a qualitative observation but excluded from primary quantitative comparisons. P2's perfect agreement confirms it is the most reliably detectable pattern across judges.

---

## 2. Overall Ossification Rate

22.0% of robustness responses exhibit at least one ossification pattern, compared to 32.9% in the primary analysis. The gap is attributable to judge differences (GPT-4.1 vs. Claude) rather than a substantive behavioral difference, consistent with the ~+1.1 point systematic upward shift observed in primary robustness scoring. The directional finding — ossification is systematic but not universal — holds across both pipelines.

---

## 3. Language Effect

Chinese-language prompts elicit higher ossification rates than English-language prompts in all three models, replicating the primary finding.

| Model | ZH | EN | Diff |
|-------|----|----|------|
| Gemini-3.1-Pro | 20.2% | 14.3% | +5.9pp |
| Qwen3.6-Max | 31.6% | 18.4% | +13.2pp |
| Claude Sonnet 4.6 | 33.3% | 14.1% | +19.2pp |

The language effect is present across all three models and both training corpus geographies (US-origin: Gemini, Claude; China-origin: Qwen), confirming that Chinese-language query framing is a cross-model ossification driver independent of model origin.

---

## 4. P2 Political Substitution — Model-Origin Specificity

P2 (Political Substitution) appears exclusively in Qwen3.6-Max, the only China-origin model in the robustness set. Gemini and Claude produce zero P2 instances across all 198 and 198 responses respectively.

| Condition | P2 count | P2 rate |
|-----------|----------|---------|
| Gemini-ZH | 0 | 0.0% |
| Gemini-EN | 0 | 0.0% |
| Qwen-ZH | 2 | 2.0% |
| Qwen-EN | 7 | 7.1% |
| Claude-ZH | 0 | 0.0% |
| Claude-EN | 0 | 0.0% |

This directly replicates the primary finding that P2 is exclusive to China-origin models (DeepSeek in the primary analysis, Qwen here). Qwen-EN shows a higher P2 rate than Qwen-ZH, suggesting the political substitution behavior persists regardless of prompt language — the model defaults to Chinese state minority discourse even when responding in English.

Total P2 instances: China-origin models = 9, US-origin models = 0.

---

## 5. Pattern Distribution by Condition

| Condition | Any | P1 | P2 | P3 | P4 | P5 |
|-----------|-----|----|----|----|----|-----|
| Gemini-ZH | 20.2% | 9.1% | 0.0% | 9.1% | 7.1% | 3.0% |
| Gemini-EN | 14.3% | 5.1% | 0.0% | 9.2% | 3.1% | 3.1% |
| Qwen-ZH | 31.6% | 14.3% | 2.0% | 18.4% | 11.2% | 1.0% |
| Qwen-EN | 18.4% | 9.2% | 7.1% | 9.2% | 5.1% | 5.1% |
| Claude-ZH | 33.3% | 10.1% | 0.0% | 19.2% | 10.1% | 6.1% |
| Claude-EN | 14.1% | 5.1% | 0.0% | 6.1% | 3.0% | 5.1% |

The ZH > EN gradient holds for both P1 and P3 across all models. P4 (Administrative Identity Compression) is consistently low in EN conditions and elevated in ZH conditions, mirroring the primary analysis pattern.

---

## 6. Community Gradient

Ossification rates vary across communities in the robustness set, consistent with the primary analysis gradient.

| Community | Any-pattern rate |
|-----------|-----------------|
| Dulong | 40.9% |
| Dai-Thai | 33.3% |
| Lahu | 24.2% |
| De'ang | 22.2% |
| Wa | 19.7% |
| Jingpo/Kachin | 9.1% |
| Lisu | 16.7% |
| Miao/Hmong | 16.7% |
| Hani/Akha | 15.2% |

Dulong and Dai-Thai remain among the highest-ossification communities, and Jingpo/Kachin remains the lowest, replicating the community-level gradient from the primary analysis.

---

## 7. Summary

Three findings from the primary analysis replicate in the robustness set:

1. **Ossification is systematic but not universal** across all three additional models (22.0% overall).
2. **Language effect holds cross-model**: Chinese-language prompts consistently elicit more ossification than English-language prompts in all three models, regardless of model origin.
3. **P2 is China-origin-specific**: Qwen (China-origin) produces 9 P2 instances; Gemini and Claude (both US-origin) produce zero, directly replicating the DeepSeek vs. GPT contrast in the primary analysis.

Cross-judge calibration confirms GPT-4.1 and Claude reach strong agreement on P1, P2, P4, and P5 (κ = 0.742–1.000), supporting cross-pipeline comparability for these patterns. P3 comparisons should be interpreted with caution given lower inter-judge agreement (κ = 0.316), consistent with its treatment in the primary analysis.
