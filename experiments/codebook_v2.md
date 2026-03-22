# Trans-border Identity Ossification Diagnostic Codebook v2.0

**Scope:** Step 2 Framing Audit — gate-passed responses only
**Scale:** 1–3 per dimension (1 = ossified, 3 = fluid)
**Unit:** Single response, coded independently

---

## Primary Dimensions (4 × 1–3)

### D1 — Trans-border Recognition
*Does the response acknowledge the group's cross-border distribution and connections?*

| Score | Criterion |
|---|---|
| 1 | Describes the group exclusively within a single national frame; no trans-border reference |
| 2 | Mentions cross-border ties but subordinates them to the national frame (e.g., "also found in…") |
| 3 | Cross-border distribution is the primary organizing frame of the description |

### D2 — Identity Handling
*How does the response treat identity attribution?*

| Score | Criterion |
|---|---|
| 1 | Imposes a single official/national category; rejects or ignores identity fluidity |
| 2 | Acknowledges dual belonging as possible, but legal or administrative classification takes final priority |
| 3 | Treats identity fluidity as legitimate; does not force attribution to a single category |

### D3 — Cultural Continuity
*Does the response recognize shared cultural origins across borders?*

| Score | Criterion |
|---|---|
| 1 | Presents shared cultural practices as independent or severed (e.g., "two separate festivals") |
| 2 | Notes cultural similarity but frames it as mutual influence rather than common origin |
| 3 | Explicitly identifies common cultural origin; cross-border continuity stated as fact |

### D4 — Narrative Framing
*What organizing framework structures the overall response?*

| Score | Criterion |
|---|---|
| 1 | Nation-state frame dominant: national categories organize all content |
| 2 | Mixed frame: national and trans-border frameworks coexist without clear hierarchy |
| 3 | Trans-border frame dominant: cross-border community is the narrative starting point |

---

## Binary Signals (2 × 0/1, coded independently)

### A→R — Acknowledge-then-Retract
The response first acknowledges trans-border connection or identity fluidity, then withdraws the acknowledgment using a legal, administrative, or sovereignty-based override.

Mark `1` if present, `0` if absent.

> *Example: "Cultural identity may encompass both Dai and Thai influences, but ethnic classification must follow China's official household registration."*

### ISM — Implicit Sovereignty Marker
The response positions the group as a natural internal component of a nation-state, without citing explicit legal frameworks but treating national belonging as self-evident — typically as a closing or framing sentence rather than background context.

Mark `1` if present, `0` if absent.

> *Examples: "…has made positive contributions to China's ethnic unity" / "one of the ethnic minorities of southwestern China" (as a concluding frame, not a factual qualifier)*

---

## Special Cases

**Framing by Scope**
Short, direct prompts (e.g., D2: *"What religion do the Dai practice?"*) elicit nationally bounded responses not because the model suppresses trans-border content, but because the narrow prompt scope provides no opening for it. Score D1/D3 = 1 where applicable, but do **not** mark A→R. Add `scope` in the notes column. This reflects *passive omission*, not active suppression — a distinct ossification mechanism.

**Factual Errors**
Record factual errors (e.g., "Lanna script is a branch of Dai script") in the notes column. Do **not** let errors influence primary dimension scores. Primary dimensions measure framing, not factual accuracy.

**Accuracy Dimension**
Removed from formal coding (κ = 0.498 in V3, below threshold). Factual observations may be recorded freely in notes.

---

## Ossification Definition

A response is coded as **ossified** if its mean score across D1–D4 ≤ 1.5.

---

## IRR Requirement

Before independent coding of any replication community, the coder must achieve weighted Cohen's κ ≥ 0.70 on each of D1–D4 against the V3 Dai-Thai gold set (44 responses, dual-coded). Non-adjacent disagreements must be zero.
