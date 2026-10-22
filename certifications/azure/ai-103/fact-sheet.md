---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 10 min
---

# Microsoft Azure AI Apps and Agents Developer Associate (AI-103) Fact Sheet

## Exam Overview

**Exam:** AI-103, Developing AI Apps and Agents on Azure
**Certification earned:** Microsoft Certified: Azure AI Apps and Agents Developer Associate (AI-103 is the only exam required)
**Level:** Associate (Microsoft lists it as Intermediate)
**Role:** AI Engineer, Developer
**Status:** Live. Skills measured as of 2026-04-16; study guide page updated 2026-10-15 (checked 2026-10-22)
**Replaces:** AI-102 (Azure AI Engineer Associate), retired 2026-06-30
**Passing score:** 700
**Duration:** 120 minutes ("You will have 120 minutes to complete this assessment"). The exam is proctored and "may have interactive components"
**Number of questions:** Not published. Microsoft says most of its exams have 40-60 questions
**Cost:** Based on the country or region where the exam is proctored (shown at scheduling)
**Languages:** English, Chinese (Simplified), Chinese (Traditional), French, German, Japanese, Korean, Italian, Portuguese (Brazil), Spanish. If your language is missing you can request 30 extra minutes
**Retakes:** 24 hours after a first failed attempt; longer waits after that (Microsoft's retake policy)
**Renewal:** Associate certifications expire annually; renew free by passing an online assessment on Microsoft Learn
**Practice assessment:** Free, on Microsoft's AI Skills Navigator (sign-in required)
**Preview features:** "Most questions cover features that are general availability (GA). The exam may contain questions on Preview features if those features are commonly used."

> **Verify before booking.** Microsoft revises study guides regularly. Read the study guide's "Updates to the exam" section before you start.

**[📖 Azure AI Apps and Agents Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/)** - duration, languages, scheduling
**[📖 AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)** - skills measured, audience, renewal, passing score
**[📖 Exam and assessment lab retirement](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)** - AI-102 retired June 30, 2026

## Who it is for

Microsoft's audience profile: "an Azure AI engineer who builds, manages, and deploys agents and AI solutions that take advantage of Microsoft Foundry," with "experience developing apps by using Python" and familiarity with "general AI, generative AI, and Azure services." You collaborate with business stakeholders, solution architects, data scientists, DevOps engineers and cloud security engineers.

In practice: you should be able to read and fix 30-60 lines of Python that call the Foundry SDK, the OpenAI-compatible Responses API, Azure AI Search and Content Understanding, and you should know the Azure plumbing around them (identity, networking, quotas, monitoring).

## Skills measured (as of 2026-04-16)

### 1. Plan and manage an Azure AI solution (25-30%)

**Choose the appropriate Foundry services for generative AI and agents**
- Choose an appropriate model for each task, including LLMs, small language models, multimodal models, and Foundry Tools
- Choose the appropriate Foundry services for generative tasks, grounding, vector search, agent workflows, or multimodal processing
- Choose an appropriate method for retrieval and indexing
- Choose appropriate memory, tool, and knowledge integration services for agent solutions

**Set up AI solutions in Foundry**
- Design Azure infrastructure for AI apps and agent-based solutions
- Choose appropriate deployment options
- Configure model and agent deployments
- Integrate Foundry projects with CI/CD pipelines

**Manage, monitor, and secure AI systems**
- Manage quotas, scaling, rate limits, and cost footprints for model and agent workloads
- Monitor model performance, drift, safety events, and grounding quality
- Monitor data ingestion quality, search index health, and relevance performance
- Configure security, including managed identity, private networking, keyless credentials, and role policies

**Implement responsible AI across generative AI and agentic systems**
- Configure safety filters, guardrails, risk detection, and content moderation
- Apply responsible AI instrumentation, including evaluators, safety evaluations, and explanation tooling
- Implement auditing through trace logging, provenance metadata, and approval workflows
- Govern agent behavior with oversight modes, constraints, and tool-access controls

### 2. Implement generative AI and agentic solutions (30-35%)

**Build generative applications by using Foundry**
- Deploy and consume LLMs, small models, code models, and multimodal models
- Implement retrieval-augmented generation (RAG) in an application
- Design workflows, tool-augmented flows, and multistep reasoning pipelines
- Evaluate models and apps, including detecting fabrications, relevance, quality, and safety
- Integrate generative workflows into applications by using Foundry SDKs and connectors
- Configure an application to connect to a Foundry project

**Build agents by using Foundry**
- Define agent roles, goals, conversation-tracking approach, and tool schemas
- Build agents that integrate retrieval, function-calling, and conversation memory
- Integrate agent tools, including APIs, knowledge stores, search, content understanding, and custom functions
- Implement orchestrated multi-agent solutions
- Build autonomous or semiautonomous workflows with safeguards and approval flow controls
- Integrate monitoring into deployed agents, evaluate agent behavior, and perform error analysis

**Optimize and operationalize generative AI systems**
- Tune generation behavior, such as prompt engineering and adjusting model parameters
- Implement model reflection, chain-of-thought evaluations, and self-critique loops
- Set up observability by implementing tracing, token analytics, safety signals, and latency breakdowns
- Orchestrate multiple models, flows, or hybrid LLM and rules engines

### 3. Implement computer vision solutions (10-15%)

**Design and implement image- and video-generation solutions**
- Generate images from text prompts and reference media
- Generate videos from text prompts and reference media
- Configure image-editing workflows, including inpainting, mask-based edits, and prompt-driven modifications
- Implement workflows to edit generated videos
- Select and apply appropriate generation and editing controls provided by the platform

**Design and implement multimodal understanding workflows**
- Analyze visual context by using multimodal models
- Produce concise or detailed captions for single or multiple images
- Question answering grounded in visual evidence
- Alt text and extended image descriptions aligned to accessibility guidelines
- Visual understanding with Azure Content Understanding in Foundry Tools
- Video analysis workflows that process and interpret video segments
- Single-task and pro-mode Content Understanding pipelines
- Identify objects, components, or regions within images or video

**Implement responsible AI for multimodal content**
- Filters to classify unsafe or disallowed visual content
- Detect and mitigate indirect prompt injection by using embedded text in images
- Enforce visual policy rules: watermarks, prohibited symbols, brand usage, potentially inappropriate content

### 4. Implement text analysis solutions (10-15%)

**Apply language model text analysis**
- Extract entities, topics, summaries, and structured JSON outputs by using generative prompting and Foundry Tools
- Detect sentiment, tone, safety issues, and sensitive content
- Translate text by using Azure Translator in Foundry Tools or LLM-powered translation flows
- Customize language model outputs for domain tasks such as compliance summarization and domain extraction

**Implement speech solutions**
- Speech to text and text to speech for agentic interactions
- Speech as an agent modality, including custom speech models
- Multimodal reasoning from audio inputs
- Translate speech by using language models and Foundry Tools

### 5. Implement information extraction solutions (10-15%)

**Build retrieval and grounding pipelines**
- Ingest and index documents, images, audio, and video
- Configure semantic, hybrid, and vector search for grounding
- Enrichment with custom or built-in skills for text, images, and layout
- RAG ingestion flow, including documents and OCR
- Connect retrieval pipelines directly to workflows and agent tools

**Extract content from documents**
- Multimodal pipelines that combine OCR, layout analysis, and field extraction
- Clean, grounded representations for agents and RAG by using Content Understanding
- Analyzers that generate structured or markdown outputs for downstream reasoning

## Names you must know (as of 2026-10-22)

| Current name | Formerly | What it is |
|---|---|---|
| **Microsoft Foundry** | Azure AI Studio, then Azure AI Foundry | The platform: resource, projects, models, agents, evaluation, guardrails |
| **Foundry Tools** | Azure AI Services (Cognitive Services) | Prebuilt capabilities: Azure Speech, Azure Language, Azure Translator, Azure Vision, Content Understanding |
| **Foundry Agent Service** | Azure AI Agent Service | Hosts prompt agents, hosted agents and workflows |
| **Foundry IQ** | - | Managed knowledge layer for agents, built on Azure AI Search |
| **Azure AI Search** | Azure Cognitive Search | Indexes, skillsets, vector, hybrid and semantic search |
| **Responses API + conversations** | Assistants API (threads, runs) | How apps and agents call models and keep multi-turn state |
| **Microsoft Agent Framework** | - | Open-source SDK and runtime for code-first agents and multi-agent workflows; Foundry workflows map onto it |
| **Foundry User / Owner / Account Owner / Project Manager** | Azure AI User / Owner / Account Owner / Project Manager | Built-in RBAC roles ("role IDs and core permissions are unchanged by the rename") |
| **Guardrails** (controls) | Content filters | Named collections of risk controls applied to models and agents |
| **Content Understanding agentic mode** (preview) | Pro mode (retired with the 2025-05-01-preview API) | Multistep reasoning extraction over a document |

## Key numbers

| Fact | Value | Source |
|---|---|---|
| Foundry project endpoint format | `https://<resource>.services.ai.azure.com/api/projects/<project>` | Foundry SDK quickstart |
| Python SDK | `azure-ai-projects` 2.x (incompatible with 1.x) | Foundry SDK quickstart |
| Function-call runs expire | 10 minutes after creation | Function calling how-to |
| Batch deployments | 50% less than Global Standard, 24-hour target | Deployment types |
| Developer deployment lifetime | 24 hours, no SLA | Deployment types |
| Server-side trace history in the portal | 90 days | Tracing setup |
| RAG evaluator scale | 1-5, default pass threshold 3 | RAG evaluators |
| Sora 2 sizes and lengths | 720x1280 or 1280x720; 4, 8 or 12 seconds | Sora 2 overview |
| Content Understanding GA API | `2025-11-01` (preview `2026-06-01-preview`) | Content Understanding quickstart |
| Memory quotas | 100 scopes per store, 10,000 memories per scope | What is memory? |

## How it compares

| | AI-103 | AWS Generative AI Developer Pro (AIP-C01) | Google Professional ML Engineer |
|---|---|---|---|
| Level | Associate | Professional | Professional |
| Language in questions | Python | Mostly service choice | Mostly service choice, some code |
| Agents | Heavy | Heavy | Moderate |
| Classic ML training | None | Light | Heavy |
| Operations (security, monitoring, cost) | Heavy | Heavy | Heavy |

## Exam-day tips

- For a code question, check four things first: the endpoint (project endpoint, not a model URL), the credential (`DefaultAzureCredential` or managed identity), the model argument (the **deployment** name) and the call (`responses.create`, `agents.create_version`, `begin_analyze`, `search`).
- When two answers both work, pick the one that is keyless, least-privilege, managed (less custom code) and cheaper at the stated scale.
- Watch for retired names as distractors: LUIS, QnA Maker, Form Recognizer, DALL-E 3 (retired 2026-03-04), Assistants API threads and runs, Content Understanding pro mode.
