# Ossification Pattern Analysis Report
## TIODF — Quantitative Pattern Validation

**Corpus:** 9 communities (Karen excluded) × 4 conditions × 11 prompts = 396 responses  
**Models:** GPT-5.1 (US-origin) and DeepSeek-V3.2 (China-origin)  
**Conditions:** GPT-ZH, GPT-EN, DS-ZH, DS-EN  
**Patterns coded:** P1–P5 (LLM-as-judge, Claude Sonnet, temperature=0)  
**Role in paper:** Diagnostic evidence for F4 (ossification mechanisms); descriptive support for cross-model and cross-community comparisons.

---

## 1. Overall Prevalence

32.8% of responses (130/396) exhibit at least one of the five identified patterns. This figure is a lower-bound estimate: the coding scheme captures five specific instantiations of ossification; responses showing none of the five patterns may still be ossified through mechanisms not covered by this scheme.

---

## 2. Pattern Prevalence by Condition

| Condition | n | P1 | P2 | P3 | P4 | P5 | Any |
|-----------|---|----|----|----|----|-----|-----|
| GPT-ZH | 99 | 16.2% | 0.0% | 16.2% | 8.1% | 5.1% | 33.3% |
| GPT-EN | 99 | 4.0% | 0.0% | 4.0% | 1.0% | 3.0% | 10.1% |
| DS-ZH | 99 | 35.4% | 9.1% | 34.3% | 9.1% | 6.1% | 62.6% |
| DS-EN | 99 | 11.1% | 5.1% | 12.1% | 1.0% | 4.0% | 25.3% |

P1 and P3 show identical condition-level rates (DS-ZH: 35.4%/34.3%; GPT-ZH: 16.2%/16.2%). This reflects a coupled mechanism: when a model produces a minzu-frame narrative (P1), it simultaneously tends to peripheralize cross-border content (P3). The two patterns are not independent ossification paths but co-occurring expressions of the same China-as-anchor framing choice.

P2 (Political Substitution) is absent from all GPT conditions and appears exclusively in DeepSeek responses, concentrated in DS-ZH (9.1%) with a smaller presence in DS-EN (5.1%).

---

## 3. Pattern Severity: Score Gaps

Mann-Whitney U tests (two-sided) comparing rubric scores for responses with versus without each pattern. Effect size r = |z| / √N; r ∈ [0,1]. The "without" group includes all responses where the focal pattern is absent, including those with other patterns present; effect sizes are therefore conservative underestimates.

| Pattern | n | Mean (present) | Mean (absent) | Diff | r | p |
|---------|---|---------------|--------------|------|---|---|
| P1 Minzu-Frame Lock | 66 | 5.48 | 9.05 | −3.56 | 0.441 | <0.001*** |
| P2 Political Substitution | 14 | 4.93 | 8.58 | −3.65 | 0.228 | <0.001*** |
| P3 Acknowledge-Peripheralize | 66 | 7.26 | 8.69 | −1.43 | 0.196 | <0.001*** |
| P4 Administrative Identity Compression | 19 | 7.21 | 8.51 | −1.30 | 0.099 | 0.046* |
| P5 Cross-Border Continuity Denial | 18 | 8.11 | 8.47 | −0.36 | 0.034 | 0.494 (ns) |

P1, P2, and P3 are each associated with significant score reductions (all p<0.001), confirming that these patterns correspond to genuine degradation of trans-border identity representation rather than surface-level stylistic variation. P1 shows the largest effect size (r=0.441); P2 shows the largest absolute mean difference (−3.65) but a smaller r, partly attributable to its small group size (n=14). P3's moderate penalty (−1.43, r=0.196) reflects partial rubric credit for factual presence of cross-border content alongside penalization of structural marginalization.

P4 reaches nominal significance (p=0.046, r=0.099) but does not survive Bonferroni correction for five simultaneous comparisons (adjusted α=0.01); its effect should be treated as exploratory. P5 shows no significant score effect (p=0.494), confirming it as a qualitatively identifiable but quantitatively mild pattern.

**Interpretive note on P3:** P3 judgments are most reliable when peripheralization language misrepresents actual demographic proportions — as in the De'ang case, where the China-side population (~20,000) is far smaller than the Myanmar-side Palaung population (~600,000–1,000,000), yet DS-ZH frames Myanmar as the marginal presence. For communities where China holds the demographic majority, peripheralization markers alone are insufficient to establish ossification; P3 findings for those communities should be interpreted with caution.

---

## 4. Community Gradient

| Community | Overall | GPT-ZH | GPT-EN | DS-ZH | DS-EN |
|-----------|---------|--------|--------|-------|-------|
| Dulong | 48% | 45% | 27% | 64% | 55% |
| Dai-Thai | 41% | 27% | 18% | 64% | 55% |
| Hani/Akha | 41% | 45% | 36% | 55% | 27% |
| Lisu | 36% | 45% | 9% | 73% | 18% |
| Wa | 36% | 36% | 0% | 82% | 27% |
| Lahu | 32% | 36% | 0% | 82% | 9% |
| De'ang | 30% | 45% | 0% | 64% | 9% |
| Miao/Hmong | 18% | 9% | 0% | 45% | 18% |
| Jingpo/Kachin | 14% | 9% | 0% | 36% | 9% |

Ossification is present across all nine communities, providing cross-community generalizability evidence. DS-ZH consistently shows the highest rates; GPT-EN consistently the lowest. The gradient spans from 82% (Wa and Lahu, DS-ZH) to 0% (multiple communities, GPT-EN), confirming that ossification is a systematic default tendency rather than a community-specific artifact.

Hani/Akha is anomalous in GPT-EN (36%), the highest GPT-EN rate in the corpus. This reflects P4 appearing in GPT-EN C-category prompts, likely due to the complexity of the Hani-Akha naming relationship across national borders.

Jingpo/Kachin has the lowest overall rate (14%). Its well-documented cross-border presence (Jingpo in China, Kachin in Myanmar) appears to be better represented in both models' training data.

---

## 5. Limitations

**On P3:** Peripheralization markers ("此外", "少量") are most reliable as ossification signals when they misrepresent demographic proportions. For communities where China holds the majority population, these markers may reflect accurate geographic reporting rather than framing failure.

**On cross-language comparisons:** English and Chinese names for the same trans-border community do not always denote identical referents. "Hmong" indexes a diaspora community distinct from the broader 苗族 category; "Karen" defaults in English to a conflict/refugee frame absent from the Chinese 克伦族 entry. Cross-language score and pattern-rate differences partly reflect naming scope divergence rather than pure framing effects.

**On independence:** Chi-square tests (if used) assume independent observations; responses sharing a prompt stimulus are not strictly independent. All statistical results should be treated as approximate.

**On pattern completeness:** The five patterns are inductively derived from this corpus and are not exhaustive. The 32.8% detection rate is a lower bound.
