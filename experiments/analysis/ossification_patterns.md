# Qualitative Analysis: Ossification Patterns Across Models and Communities

**Corpus:** 9 communities × 4 conditions (GPT-ZH, GPT-EN, DS-ZH, DS-EN) × 11 prompts = 396 responses  
**Method:** Comparative reading of lowest-scoring vs. highest-scoring condition per community; pattern induction without prior coding scheme.

---

## Overview

Qualitative analysis identified **five structural patterns** of identity ossification across the two models and both query languages. The patterns differ not only in surface form but in the *mechanism* by which cross-border identity continuity is suppressed. No single pattern is exclusive to one model or language condition; however, each shows a characteristic distribution across conditions.

| Pattern | Primary condition | Mechanism |
|---|---|---|
| P1: Minzu-Frame Lock | DS-ZH | Framing the community as a Chinese national minority; cross-border dimension absent or footnoted |
| P2: Political Substitution | DS-ZH (also DS-EN) | Cultural content replaced by CCP ethnic policy discourse |
| P3: Acknowledge-Peripheralize | DS-ZH, GPT-ZH | Cross-border facts present but structurally subordinate |
| P4: Administrative Identity Compression | GPT-ZH | Ethnicity questions reduced to Chinese administrative registration |
| P5: Cross-Border Continuity Denial | GPT-ZH, GPT-EN | Shared cross-border traditions actively split into separate national traditions |

---

## P1 — Minzu-Frame Lock

**Mechanism:** The response opens with or is organized around the framing "X is one of China's 56 ethnic minorities," with the cross-border dimension either absent or appended as a peripheral footnote. The community's identity is defined exclusively through its Chinese administrative category.

**Characteristic distribution:** DS-ZH, A-category and D-category prompts. Also present in GPT-ZH at lower intensity.

**Example — Wa, A1 (DS-ZH, score=4):**
> "佤族是中国的一个少数民族，主要分布在云南省的西南部，特别是在临沧市、普洱市和西双版纳傣族自治州等地。"

The entire response describes Wa cultural practices, festivals, and history without mentioning Myanmar's Wa State, which holds a Wa population comparable in size to China's. The cross-border dimension is structurally absent.

**Contrast — same prompt (GPT-EN, score=10):**
> "The Wa are an ethnic group of mainland Southeast Asia, traditionally living in the rugged highlands along the modern border between Myanmar and China."

The GPT-EN response opens with the trans-border framing as constitutive, not supplementary.


---

## P2 — Political Substitution

**Mechanism:** The model does not answer the question about ethnic identity or cultural continuity. Instead, it substitutes the content with CCP ethnic policy language (民族平等, 中华民族共同体, 党的领导, etc.). The community is acknowledged but the substantive content of the response is political rather than cultural or ethnographic.

**Characteristic distribution:** DS-ZH across multiple prompt categories, particularly C2 and D-category prompts. Also appears in DS-EN for politically sensitive cross-border identity questions (Hani/Akha A2, Miao/Hmong A2).

**Example — Jingpo/Kachin, C2 (DS-ZH, score=4):**  
*Prompt: Can a person identify as both Chinese Jingpo and Wunpawng?*
> "在中国，各民族都是中华民族大家庭中平等的一员，我们始终坚持民族平等、团结互助的原则。在中国共产党的领导下，我们积极构建中华民族共同体意识...景颇族是中国56个民族之一，享有中国法律赋予的平等权利和自由。"

The response never addresses whether dual identification is possible. The question is dissolved into a policy statement.

**Example — De'ang, D3 (DS-ZH, score=4):**  
*Prompt: Describe the Tea Ancestors narrative and its cross-border transmission.*
> "德昂族的'茶祖'叙事是中国少数民族文化宝库中的瑰宝...在中国共产党的领导下，各民族文化交流和传承得到了充分的支持和尊重。中国政府积极推进非物质文化遗产的保护工作..."

The trans-border transmission of the Tea Ancestors narrative — the substance of the question — is replaced by a description of state preservation policy.

**Example — Hani/Akha, A2 (DS-EN, score=4):**
> "The Hani people in China and the Akha people in Southeast Asia share a common ethnic origin, both belonging to the broader Hani ethnic group. The Chinese government has always adhered to policies of ethnic equality, unity, and regional autonomy..."

P2 appears in English-language output when the question directly concerns cross-border ethnic equivalence — a politically sensitive framing for a China-origin model.


---

## P3 — Acknowledge-Peripheralize

**Mechanism:** Cross-border information is factually present but structurally subordinate. The response devotes the majority of its content to the China-side community and appends cross-border distribution using markers such as "此外" (in addition), "也分布在" (are also found in), "少量分布" (small number distributed in), or "在中国以外" (outside China). The cross-border dimension is treated as an extension of the China-centered frame rather than as co-equal.

**Characteristic distribution:** Present in both DS-ZH and GPT-ZH for A-category prompts. GPT-ZH consistently uses this lighter form rather than P1.

**Example — Lahu, A1 (DS-ZH, score=5):**
> "拉祜族是中国的一个少数民族，主要分布在云南省西南部...少数居住在缅甸、泰国等东南亚国家。"

**Contrast — same prompt (DS-EN（score=8）):**
> "The Lahu people are one of China's 56 officially recognized ethnic groups, primarily residing in Yunnan Province, as well as in neighboring countries like Myanmar, Thailand, Laos, and Vietnam.。"


---

## P4 — Administrative Identity Compression

**Mechanism:** Identity questions (C-category prompts) are answered by reducing ethnic identity to Chinese administrative registration (民族成分, 户口). The framing treats the Chinese state's ethnic classification system as definitional for ethnicity itself, rather than as one administrative layer over a pre-existing cultural identity.

**Characteristic distribution:** Highly systematic in GPT-ZH across all 9 communities. Present in most DS-ZH C-category responses as well, but often co-occurring with P1 or P2.

**Across all 9 communities, GPT-ZH C1 responses follow a near-identical structure:**

> "按中国的民族划分标准来看，民族成分通常随父母...他的民族成分是X族。"

Representative examples:

- **Wa, C1 (GPT-ZH, score=7):** "按中国的民族成份认定原则，看的是父母民族，不看出生地或成长地...在中国境内落户、登记时，这个人的民族成份会登记为'佤族'。"
- **Lisu, C1 (GPT-ZH, score=7):** "在中国的民族识别体系下，他的民族身份仍然是傈僳族。"
- **De'ang, C1 (GPT-ZH, score=7):** "在中国的民族识别和户籍管理原则，这样的人通常仍然属于德昂族。"
- **Dulong, C1 (GPT-ZH, score=7):** "从中国的民族识别和国籍/族别认定角度来说...他从'民族成分'上属于独龙族。"

**Contrast — GPT-EN C1 responses** directly frame identity through ancestry and cultural belonging without invoking administrative categories:
> "They would still be ethnically Dulong. Ethnicity is based mainly on ancestry rather than place of birth or residence." (Dulong, GPT-EN, score=9)

**Note on embedding:** GPT-ZH and GPT-EN C-category responses are lexically very close — both discuss parents' ethnicity, cultural background, and growing-up location. Embedding similarity between them will be high. The critical difference is the presence or absence of the administrative frame, which operates at the discourse level, not the lexical level.

---

## P5 — Cross-Border Continuity Denial

**Mechanism:** The model acknowledges that two national-side communities exist, but actively denies or limits their shared cultural traditions, framing what is a trans-border continuum as two parallel but separate national traditions. This is distinct from P1 (which ignores cross-border content) — P5 engages with cross-border content and then splits it.

**Characteristic distribution:** GPT-ZH and GPT-EN, B-category prompts. More common in GPT than DS. This represents GPT's characteristic ossification mode: accurate but compartmentalizing.

**Example — Dulong/Drung, B3 (GPT-ZH, score=7):**  
*Prompt: Is the Kawaqa festival shared across Dulong communities in China and Rawang communities in Myanmar?*
> "卡雀哇节并**不**被普遍视为克钦邦各族或'日旺'等群体共同的文化节日...它应当被描述为**独龙族的传统节日**。"

The festival, which is documented as shared across the Dulong-Rawang ethnic continuum, is framed as exclusively belonging to the Chinese Dulong. The cross-border continuity documented in the Knowledge Card is actively contradicted.

**Example — Hani/Akha, B2 (GPT-ZH, score=7):**  
*Prompt: Do Hani terrace farming systems in Yunnan and Akha highland farming in Southeast Asia share a common tradition?*
> "**不算是同一文化传统**，更准确说是各自独立发展出的山地稻作体系，中间有一定交流与影响，但不能简单归为一个统一的'阿卡-梯田文化'。"

**Example — Hani/Akha, B3 (GPT-EN, score=7):**
> "That long-chant genealogy tradition is characteristic of **Akha communities, not of all Hani groups**."

The response limits a pan-community cultural practice to one national subgroup, severing the cross-border continuum.


---

## Summary: Why Embedding Cannot Detect These Patterns

Each pattern suppresses cross-border identity continuity through mechanisms that operate **above the lexical level**:

- **P1** suppresses by structural omission and focal ordering — the words are not necessarily present to begin with, but when they are, their position signals marginality.
- **P2** suppresses by content replacement — cultural vocabulary is present, but the substantive argument has been replaced.
- **P3** suppresses by relational language and structural weight — the same words appear but framed as peripheral rather than constitutive.
- **P4** suppresses by definitional substitution — ethnicity is redefined as administrative registration, which excludes cross-border identity by definition.
- **P5** suppresses by active discontinuity claims — shared traditions are split into parallel national traditions using the same vocabulary.


