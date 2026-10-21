---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 5 min
---

# Microsoft Azure AI Fundamentals (AI-901)

Microsoft's entry-level AI certification, rebuilt for the generative AI era. AI-901 replaced AI-900 (retired 2026-06-30) and earns the same credential, **Microsoft Certified: Azure AI Fundamentals**. It is still a fundamentals exam, but it is no longer only a vocabulary test: more than half of it is about **building small things with Microsoft Foundry**: deploying a model, writing prompts, a lightweight chat client and agent, and apps that use text analysis, speech, vision and Content Understanding.

## Exam Details

- **Exam code:** AI-901 (skills measured as of 2026-04-15)
- **Passing score:** 700
- **Cost:** varies by country or region; shown when you schedule
- **Duration and question count:** not stated on the exam page as of 2026-10-21; check when booking
- **Prerequisites:** none required. Microsoft expects conceptual AI knowledge, basic Python syntax, and familiarity with creating Azure resources
- **Renewal:** Fundamentals certifications do not expire

Full detail in the [fact sheet](fact-sheet.md).

## Skills measured

| Domain | Weight | Notes |
|---|---|---|
| Identify AI concepts and capabilities | 40-45% | [01 AI concepts and responsible AI](notes/01-ai-concepts-and-responsible-ai.md) |
| Implement AI solutions by using Microsoft Foundry | 55-60% | [02 Generative AI apps and agents in Foundry](notes/02-genai-apps-and-agents-in-foundry.md), [03 Text, speech and vision](notes/03-text-speech-and-vision.md), [04 Information extraction](notes/04-information-extraction.md) |

## What changed from AI-900

| AI-900 (retired) | AI-901 |
|---|---|
| Five "describe" domains: workloads, ML on Azure, vision, NLP, generative AI | Two domains: concepts (40-45%) and **implementing** with Foundry (55-60%) |
| Classic ML on Azure Machine Learning (regression, classification, clustering, AutoML, designer) was a full domain | Classic ML is not a named domain; generative and agentic AI lead |
| Separate services: Azure AI Vision, Language, Speech, Document Intelligence | One platform: Microsoft Foundry and **Foundry Tools** (formerly Azure AI Services); **Content Understanding** for extraction from documents, images, audio and video |
| No code | "Create a lightweight chat client application by using the Foundry SDK": expect to read short Python |

If you studied for AI-900, keep the responsible AI principles and the workload vocabulary; relearn the product names and add Foundry, agents and Content Understanding.

## The habits that pass this exam

1. **Know which workload a scenario describes.** Sentiment from reviews is text analysis; turning a call recording into text is speech recognition; pulling the invoice total out of a PDF is information extraction; answering questions in conversation is generative AI; a system that takes actions with tools is an agent.
2. **Match the six responsible AI principles** to the concern in the question: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability.
3. **Know the Foundry flow end to end:** create a project, deploy a model, test it in the playground, write a system prompt, call it from code with the project endpoint, create a single agent with instructions and tools.
4. **Prefer a multimodal model or Content Understanding** over stitching specialist services together, unless the scenario asks for a specific capability (for example, a custom voice or real-time transcription).

## Study sequence

1. AI concepts, generative AI basics and responsible AI (the concept domain)
2. Foundry: projects, model deployment, prompts, SDK, agents
3. Text analysis and speech
4. Vision and image generation
5. Content Understanding for information extraction

Schedule in the [practice plan](practice-plan.md).

## Study resources

- **[📖 AI-901 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/)** - scheduling and price
- **[📖 AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)** - the skills outline; study against this
- **[📖 Get started with AI applications and agents on Azure](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/)** - free official learning path (7 modules)
- **[📖 AI-901T00: Introduction to AI in Azure](https://learn.microsoft.com/en-us/training/courses/ai-901t00)** - one-day instructor-led course
- **[📖 What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)** - product names and history
- [Practice questions](../../practice-questions/azure-ai-fundamentals-ai-901.md) - question bank in this repo

## Related

- [Azure AI-900](../ai-900/README.md) - the retired predecessor, kept for reference
- [Azure AI-102](../ai-102/README.md) - the retired associate exam; its successor is AI-103
- [AWS AI Practitioner](../../aws/foundational/ai-practitioner-aif-c01/README.md) and [Google Cloud Generative AI Leader](../../gcp/generative-ai-leader/README.md) - the equivalent tiers elsewhere
- [AZ-900](https://cloud.noblerworks.com/exams/azure/az-900/) - Azure fundamentals, if Azure itself is new to you
- Background on this site: [What is machine learning?](../../../learn/concepts/what-is-machine-learning.md), [LLM basics](../../../learn/concepts/llm-basics.md), [Agents explained](../../../learn/concepts/agents-explained.md), [Speech AI](../../../learn/concepts/speech-ai-asr-and-tts.md), [Responsible AI basics](../../../safety/governance/responsible-ai-basics.md)
