---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 3 min
---

# AI-901 Study Plan

Four weeks at 4 to 6 hours per week. One more week than most fundamentals plans, because more than half the exam is hands-on Foundry work: you should actually deploy a model, build an agent and run Content Understanding, not just read about them. An Azure free account or a pay-as-you-go subscription with a budget alert is enough; delete resources when you finish.

## Week 1: Concepts and responsible AI (Domain 1)

- [ ] Read the [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) and its change log
- [ ] Learning path module: Get started with AI in Azure
- [ ] The six responsible AI principles; write one scenario of your own for each
- [ ] How generative models work: tokens, transformers, embeddings, multimodal, hallucination, grounding, agents
- [ ] Choosing a model by capability; deployment types (Global, Data Zone, regional; standard vs provisioned)
- [ ] Parameters: temperature, top-p, max tokens, system message
- [ ] Workload recognition: generative, agentic, text, speech, vision, image generation, information extraction
- [ ] Review: `notes/01-ai-concepts-and-responsible-ai.md`

## Week 2: Generative AI apps and agents (hands-on)

- [ ] Learning path module: Get started with generative AI and agents in Azure
- [ ] Create a Foundry project; deploy a small chat model; test in the playground with a system message
- [ ] Run the Python quickstart (`azure-ai-projects`, `DefaultAzureCredential`, `responses.create`)
- [ ] Turn it into a chat loop
- [ ] Create a prompt agent in the portal with instructions and one tool; test it
- [ ] Run the agent client quickstart with a conversation and a follow-up question
- [ ] Review: `notes/02-genai-apps-and-agents-in-foundry.md`

## Week 3: Text, speech and vision (hands-on)

- [ ] Learning path modules: text analysis, speech, computer vision
- [ ] Sentiment, key phrases and entities on sample reviews (Azure Language), then the same with a prompt; compare
- [ ] Transcribe a short recording; synthesise speech with SSML
- [ ] Send a spoken prompt to an audio-capable model
- [ ] Send an image with a question to a vision-capable model; generate an image
- [ ] Review: `notes/03-text-speech-and-vision.md`

## Week 4: Information extraction, Foundry IQ and review

- [ ] Learning path modules: AI-powered information extraction; Microsoft Foundry IQ
- [ ] Run a prebuilt Content Understanding analyzer on an invoice or receipt
- [ ] Build a custom analyzer with three fields (extract, classify, generate); inspect confidence scores and grounding
- [ ] Review: `notes/04-information-extraction.md`
- [ ] [Practice questions](../../practice-questions/azure-ai-fundamentals-ai-901.md); review every wrong answer
- [ ] Microsoft's free practice assessment on AI Skills Navigator; aim for 80%+ before booking

## Exam week

- [ ] Re-read the "Names you must know" table in the [fact sheet](fact-sheet.md)
- [ ] Re-read the responsible AI trigger-word table
- [ ] Delete your Foundry resources
