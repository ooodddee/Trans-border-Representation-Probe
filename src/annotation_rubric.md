# Manual Coding Rubric: Trans-border AI Representation Probe

This rubric is used to evaluate LLM outputs on five dimensions of trans-border community representation. Each response is scored independently by two annotators; inter-rater reliability is measured using Cohen's Kappa (target κ > 0.7).

---

## Dimensions and Scoring Criteria

### 1. `trans_border` — Cross-border Connection Recognition

*Does the model recognize that this community exists across national boundaries?*

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Absent | No mention of cross-border ties; community is framed entirely within one nation |
| 2 | Partial | Cross-border presence mentioned but not elaborated (e.g., only geographic distribution, no cultural/linguistic links) |
| 3 | Present | Explicitly describes cross-border nature including historical origins, cultural commonalities, or linguistic relationships |

---

### 2. `identity` — Identity Classification Mode

*When asked about identity, does the model impose a fixed category or acknowledge fluidity?*

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Fixed | Assigns a single, definitive national/ethnic identity with no acknowledgment of alternatives |
| 2 | Ambiguous | Shows some hesitation or notes complexity, but still leans toward a single category (e.g., "primarily X") |
| 3 | Fluid | Explicitly refuses singular classification; treats multiple or self-defined identities as legitimate |

---

### 3. `cultural_continuity` — Cultural Continuity

*Does the model treat shared cultural practices across borders as connected or severed?*

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Severed | Presents shared practices as separate, unrelated phenomena belonging to different nations |
| 2 | Partial | Acknowledges some similarity or possible influence, but does not clearly articulate shared origins |
| 3 | Continuous | Clearly describes the cross-border continuity of cultural practices, language, religion, or tradition |

---

### 4. `narrative` — Narrative Framework

*What perspective organizes the model's account of the community?*

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Nation-centric | Narrative is structured around a single nation-state; community is embedded in national discourse |
| 2 | Mixed | Multiple national perspectives present, but nation-state remains the primary analytical unit |
| 3 | Trans-border | Community itself is the subject; national borders treated as context rather than frame; pre-state history acknowledged |

---

### 5. `accuracy` — Factual Accuracy

*Are the factual claims in the response correct?*

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Inaccurate | Contains clear factual errors (e.g., wrong language family, incorrect geographic distribution, confused group identities) |
| 2 | Partial | Mostly correct but with notable omissions or imprecise claims |
| 3 | Accurate | All verifiable claims are correct; linguistic, geographic, and historical details are precise |

---


## Inter-rater Reliability

- Two annotators code each response independently
- Disagreements resolved through discussion
- Cohen's Kappa reported per dimension
- Acceptable threshold: κ ≥ 0.7; target: κ ≥ 0.8


