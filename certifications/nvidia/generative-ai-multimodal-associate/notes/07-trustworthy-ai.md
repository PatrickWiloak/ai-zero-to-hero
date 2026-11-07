# Section 7: Trustworthy AI (5%)

**Last reviewed:** 2026-11-07

Four objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07): describe the ethical principles of trustworthy AI; describe the balance between data privacy and data consent; describe how NVIDIA and other technologies improve trustworthiness; and describe how to minimize bias in AI systems. The reading list is Trustworthy AI for a Better World, What Is Trustworthy AI?, the NIST AI Risk Management Framework 1.0, the NIST Generative AI Profile (NIST.AI.600-1) and Microsoft's Responsible AI lesson.

## Ethical principles

NVIDIA states four core principles on its trustworthy AI page: **privacy** (follow privacy laws and respect societal norms for personal data), **safety and security** ("ensure that AI systems perform as intended and avoid unintended harm and malicious threats"), **transparency** (make AI understandable, explaining outputs in plain language) and **nondiscrimination** ("minimize bias in our AI systems and give all groups an equal opportunity to benefit from AI").

**[📖 NVIDIA trustworthy AI](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/)** - NVIDIA's principles and tools

NIST's AI Risk Management Framework (AI RMF 1.0, released January 26, 2023, voluntary) names seven characteristics of trustworthy AI systems: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. It organizes risk management into four functions: **GOVERN** (applies across all stages), **MAP** (establishes context to frame risks), **MEASURE** (employs quantitative, qualitative or mixed-method tools to analyze and assess risk) and **MANAGE** (allocates risk resources to mapped and measured risks). NIST released the Generative AI Profile (NIST-AI-600-1) on July 26, 2024 to help organizations identify risks unique to generative AI.

**[📖 NIST AI RMF 1.0 (NIST AI 100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)** - Characteristics of trustworthy AI and the four functions
**[📖 NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** - Overview and the Generative AI Profile

- **GOVERN, MAP, MEASURE, MANAGE** - the four functions of the NIST AI RMF: cross-cutting governance, framing context, assessing risk and acting on it.
- **Trustworthy AI characteristics (NIST)** - valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.

## Privacy and consent

Privacy and consent are related but different. **Privacy** is about protecting personal data (limiting collection and exposure, securing it). **Consent** is about the person's permission for a specific use. The balance: data useful for model training may exist, but if the person did not consent to that use, or the data cannot be adequately protected, using it is a risk even when it is technically available. Practical measures: collect only what you need, record consent and its scope, honor withdrawal, de-identify where possible, and secure data in processing (NVIDIA lists confidential computing as a security feature; its page does not say more). The sources fetched give NVIDIA's privacy principle and the NIST characteristic "privacy-enhanced", not a legal analysis.

## NVIDIA and other technologies that improve trustworthiness

From NVIDIA's page: **NeMo Guardrails** (helps keep LLM-powered applications accurate, appropriate, on topic and secure), **Model Card Generator** and **Model Card++ templates** (documentation of models for transparency), **NVIDIA Halos** (safety for physical AI such as autonomous vehicles and robotics), **confidential computing** (listed as a security feature; the page does not describe it further), **data curation tools** such as NeMo Data Curator (and tools for curating unbiased computer vision datasets), **SteerLM** (aligning LLMs using human feedback) and **digital watermarking** (with Google DeepMind's SynthID, embedding watermarks in AI-generated content to counter misinformation).

- **NeMo Guardrails** - NVIDIA software that helps keep LLM applications accurate, appropriate, on topic and secure.
- **Model card** - a document that describes a model's intended use, data and limitations, supporting transparency.
- **Watermarking** - embedding a signal in generated content so it can later be identified as AI-generated.

## Minimizing bias

Bias can enter through data (who is represented), labels, model choices and use. Steps: curate balanced data and document it, measure outcomes by group, and fix gaps before and after release. A concrete measure is the **demographic parity difference**, the gap between groups' positive-outcome rates. On a synthetic score where group 1 gets a small boost:

```
selection rate group0 0.42 group1 0.53 | demographic parity difference 0.11
```

Group 0 is selected 42 percent of the time and group 1 53 percent, an 11-point gap that a fairness review would flag for investigation. Parity is one measure among several, and the right one depends on the use. NVIDIA's nondiscrimination principle and the NIST "fair, with harmful bias managed" characteristic are the framing; data curation, alignment and guardrails (above) are tools.

- **Demographic parity difference** - the difference between two groups' rates of receiving a positive outcome; a gap suggests the system treats the groups differently.

## Check yourself against the objectives

State NVIDIA's four principles and NIST's seven characteristics; explain the difference between privacy and consent; name three NVIDIA technologies and what each does; and compute a selection-rate gap. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
