---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 8 min
---

# Microsoft Azure AI Fundamentals (AI-901) Fact Sheet

## Exam Overview

**Exam:** AI-901, Microsoft Azure AI Fundamentals
**Certification earned:** Microsoft Certified: Azure AI Fundamentals (AI-901 is the only exam required)
**Level:** Fundamentals
**Status:** Live. English version updated 2026-04-15; skills measured as of 2026-04-15
**Replaces:** AI-900, retired 2026-06-30
**Passing score:** 700
**Cost:** Based on the country or region where the exam is proctored (shown at scheduling)
**Duration / number of questions:** Not stated on Microsoft's exam page as of 2026-10-21; Microsoft's exam sandbox and the confirmation at booking show the current figures
**Languages:** 13
**Renewal:** None needed; Microsoft states that Fundamentals certifications do not expire
**Practice assessment:** Free, on Microsoft's AI Skills Navigator

> **Verify before booking.** Microsoft revises study guides regularly. Read the "skills measured" change log on the study guide page before you start.

**[📖 Exam AI-901](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/)**
**[📖 Azure AI Fundamentals certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/)**
**[📖 AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)**
**[📖 AI-900 retirement notice](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-900/)** - "retired on June 30, 2026, and has been replaced by AI-901"

## Who it is for

Microsoft describes the candidate as someone at the start of a career building AI solutions, with conceptual knowledge of AI in Azure, knowledge of **Python syntax and programming techniques**, and familiarity with Azure resources. That last part is the real change from AI-900, which was pitched equally at non-technical candidates. You do not need to be a developer, but you should be comfortable reading a 20-line Python script and knowing what an endpoint, a key and a deployment are.

## Skills measured (as of 2026-04-15)

### 1. Identify AI concepts and capabilities (40-45%)

**Describe principles of responsible AI**
- Considerations for fairness
- Considerations for reliability and safety
- Considerations for privacy and security
- Considerations for inclusiveness
- Considerations for transparency
- Considerations for accountability

**Identify AI model components and configurations**
- Describe how generative AI models work
- Identify an appropriate AI model, based on capabilities
- Identify appropriate model deployment options and configuration parameters

**Identify AI workloads**
- Scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction
- Common text analysis techniques: keyword extraction, entity detection, sentiment analysis, summarization
- Features and capabilities of speech recognition and speech synthesis
- Features and capabilities of computer vision and image-generation models
- Techniques to extract information from text, images, audio and videos

### 2. Implement AI solutions by using Microsoft Foundry (55-60%)

**Implement generative AI apps and agents by using Foundry**
- Create effective system and user prompts for generative AI models
- Deploy a model and interact with it in the Foundry portal
- Create a lightweight chat client application by using the Foundry SDK
- Create and test a single-agent solution in the Foundry portal
- Create a lightweight client application for an agent

**Implement AI solutions for text and speech by using Foundry**
- Build a lightweight application that includes text analysis
- Respond to spoken prompts by using a deployed multimodal model
- Build a lightweight application by using Azure Speech in Foundry Tools

**Implement AI solutions with computer vision and image-generation capabilities by using Foundry**
- Interpret visual input in prompts by using a deployed multimodal model
- Create new visual outputs by using generative models
- Build a lightweight application that includes vision capabilities

**Implement AI solutions for information extraction by using Foundry**
- Extract information from documents and forms by using Azure Content Understanding in Foundry Tools
- Extract information from images by using Content Understanding
- Extract information from audio and video by using Content Understanding
- Build a lightweight application with information extraction capabilities by using Content Understanding

## Names you must know (as of 2026-10-21)

| Current name | Formerly | What it is |
|---|---|---|
| **Microsoft Foundry** | Azure AI Studio, then Azure AI Foundry | The platform: projects, model catalog, deployments, playgrounds, agents, evaluation |
| **Foundry Tools** | Azure AI Services (Cognitive Services) | The prebuilt capabilities: Azure Speech, Azure Language, Azure Vision, Content Understanding and others |
| **Azure OpenAI in Foundry** | Azure OpenAI Service | OpenAI models sold directly by Azure |
| **Foundry Agent Service** | Azure AI Agent Service | Building and running agents |
| **Azure Content Understanding** | (new; overlaps Document Intelligence) | Extracts structured fields from documents, images, audio and video |
| **Foundry IQ** | - | Managed knowledge layer, built on Azure AI Search |
| **Responses API** | Assistants API | The API agents and chat clients use |

Source: [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) ("Evolution of Foundry" table).

## Official training

- **Learning path:** [Get started with AI applications and agents on Azure](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/), 7 modules: Get started with AI in Azure; generative AI and agents; text analysis; speech; computer vision; AI-powered information extraction; Microsoft Foundry IQ
- **Instructor-led:** [AI-901T00-A, Introduction to AI in Azure](https://learn.microsoft.com/en-us/training/courses/ai-901t00), one day, beginner

## How it compares

| | AI-901 | AWS AI Practitioner (AIF-C01) | Google Generative AI Leader |
|---|---|---|---|
| Hands-on content | Yes: Foundry portal and short Python | No | No |
| Classic ML | Light | Moderate | Light |
| Generative AI and agents | Heavy | Heavy | Heavy |
| Business strategy | Light | Moderate | Heavy |

## Exam-day tips

- Read the last sentence of each question first: is it asking for a **workload**, a **principle**, a **service** or a **step**?
- For "which service" questions, the current answer is usually a Foundry capability; distractors use retired names (LUIS, QnA Maker, Form Recognizer) or the wrong workload.
- For code questions, find the endpoint, the credential, the deployment or model name, and the call. Those four lines are what gets tested.
