---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 6 min
---

# Microsoft Azure AI Apps and Agents Developer Associate (AI-103)

Microsoft's associate-level exam for engineers who build generative AI apps and agents on **Microsoft Foundry** with **Python**. Passing AI-103 earns **Microsoft Certified: Azure AI Apps and Agents Developer Associate**. It is the successor to AI-102 (Azure AI Engineer Associate), which retired on 2026-06-30. Where AI-102 was a tour of separate Cognitive Services, AI-103 is about one platform and one way of working: deploy models, build agents with tools and retrieval, keep them safe, measure them, and run them in production.

## Exam Details

- **Exam code:** AI-103, "Developing AI Apps and Agents on Azure" (skills measured as of 2026-04-16)
- **Passing score:** 700
- **Duration:** 120 minutes (stated on the certification page); the exam is proctored and may include interactive components
- **Question count:** not published; Microsoft says most exams have 40-60 questions
- **Cost:** based on the country or region where the exam is proctored (shown when you schedule)
- **Languages:** English, Chinese (Simplified), Chinese (Traditional), French, German, Japanese, Korean, Italian, Portuguese (Brazil), Spanish
- **Prerequisites:** none required. Microsoft expects experience developing apps in **Python** and familiarity with general AI, generative AI and Azure services
- **Renewal:** associate certifications expire after one year; renew free with an online assessment on Microsoft Learn

Full detail in the [fact sheet](fact-sheet.md).

## Skills measured

| Domain | Weight | Notes |
|---|---|---|
| Plan and manage an Azure AI solution | 25-30% | [01 Plan, secure and govern](notes/01-plan-and-manage-ai-solutions.md) |
| Implement generative AI and agentic solutions | 30-35% | [02 Generative AI apps and agents](notes/02-generative-ai-and-agents.md) |
| Implement computer vision solutions | 10-15% | [03 Image, video and visual understanding](notes/03-computer-vision.md) |
| Implement text analysis solutions | 10-15% | [04 Text analysis, translation and speech](notes/04-text-analysis-and-speech.md) |
| Implement information extraction solutions | 10-15% | [05 Retrieval, grounding and Content Understanding](notes/05-information-extraction.md) |

Domains 1 and 2 are 55-65% of the exam between them. Spend your time there.

## What changed from AI-102

| AI-102 (retired 2026-06-30) | AI-103 |
|---|---|
| Separate services: Azure AI Vision, Language, Speech, Document Intelligence, Cognitive Search, Bot Framework | One platform: Microsoft Foundry projects, Foundry Models, Foundry Agent Service and Foundry Tools |
| C# or Python | **Python** |
| Custom vision models (label, train, evaluate), LUIS-style intent models, QnA | Multimodal models for vision; prompting and Foundry Tools for text; Content Understanding for extraction |
| Generative AI was one domain among six | Generative AI and agents are the biggest domain, and planning (security, monitoring, responsible AI) is the second |
| Little on evaluation or observability | Evaluators, safety evaluations, tracing, token analytics, drift and grounding quality |
| No agents | Agents with tools, memory, retrieval, multi-agent orchestration and human approval |

If you studied for AI-102, keep Azure AI Search (indexes, skillsets, vector and hybrid search), responsible AI and the security basics (keys vs Entra ID, managed identity, private endpoints). Relearn everything else around Foundry.

## The habits that pass this exam

1. **Know the Foundry SDK shape.** `AIProjectClient(endpoint, DefaultAzureCredential())`, `project.get_openai_client()`, `responses.create(model=<deployment name>, input=...)`, `project.agents.create_version(... PromptAgentDefinition(model, instructions, tools))`, conversations for multi-turn state. Most code questions are about which line is wrong or missing.
2. **Match the scenario to the right building block.** Grounding on company documents is retrieval (Azure AI Search, Foundry IQ, file search); remembering a user across sessions is memory; calling your API is a function tool; extracting fields at volume with confidence scores is Content Understanding; translating text is Translator or a model.
3. **Prefer keyless, private and least privilege.** Managed identity and Entra ID over keys; private endpoints when the scenario says "no public internet"; scoped roles such as Foundry User rather than Owner.
4. **Separate the three safety layers.** Guardrails (content filters, Prompt Shields) act at runtime; evaluations measure quality and safety before and after release; tracing and monitoring show what happened in production.
5. **Read for the cost and residency clue.** "Lowest cost, large asynchronous job" is Batch; "predictable latency at high volume" is Provisioned; "data must stay in the EU" is Data Zone; "default" is Global Standard.

## Study sequence

1. Foundry fundamentals: projects, deployments, deployment types, the SDK (Domain 1 and the start of Domain 2)
2. Agents: tools, retrieval, memory, workflows, human approval (Domain 2)
3. Safety, evaluation and observability (Domains 1 and 2 together, since the exam mixes them)
4. Retrieval pipelines and Content Understanding (Domain 5)
5. Vision, image and video generation (Domain 3)
6. Text analysis, translation and speech (Domain 4)

Schedule in the [practice plan](practice-plan.md).

## Study resources

- **[📖 AI-103 certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/)** - scheduling, duration, languages
- **[📖 AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)** - the skills outline; study against this
- **[📖 AI-103T00: Develop AI apps and agents on Azure](https://learn.microsoft.com/en-us/training/courses/ai-103t00)** - four-day instructor-led course; its self-paced learning paths cover generative AI apps, agents, language solutions and visual data
- **[📖 Develop AI agents on Azure](https://learn.microsoft.com/en-us/training/paths/develop-ai-agents-azure/)** - free learning path (Foundry Agent Service and Microsoft Agent Framework)
- **[📖 Foundry SDK quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code)** - the code every other sample builds on
- Free practice assessment on Microsoft's AI Skills Navigator (linked from the certification page; sign-in required)
- [Practice questions](../../practice-questions/azure-ai-apps-agents-developer-ai-103.md) - original question bank in this repo
- [Flashcards](flashcards.csv) - import into Anki or any spaced-repetition app

## Related

- [Azure AI-102](../ai-102/README.md) - the retired predecessor, kept for reference
- [Azure AI-901](../ai-901/README.md) - the fundamentals exam; a good first step if Foundry is new to you
- [Azure generative AI study track](../genai/README.md) - self-directed platform study
- [AWS Generative AI Developer - Professional](../../aws/professional/genai-developer-aip-c01/README.md) and [Google Cloud Professional ML Engineer](../../gcp/machine-learning-engineer/README.md) - the nearest equivalents elsewhere
- Background on this site: [RAG explained](../../../learn/concepts/rag-explained.md), [Tool use and function calling](../../../learn/concepts/tool-use-and-function-calling.md), [Memory for agents](../../../learn/concepts/memory-for-agents.md), [Evals for LLMs](../../../learn/concepts/evals-for-llms.md), [Prompt injection defense](../../../safety/security/prompt-injection-defense.md)
