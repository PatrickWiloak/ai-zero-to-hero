---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 4 min
---

# AI-103 Study Plan

Six weeks at 6 to 8 hours per week, weighted the way the exam is: two weeks on agents and generative apps, one on planning, security and responsible AI, then one each for retrieval and extraction, vision, and text and speech, with review folded in. This is a Python developer exam, so most of the time goes into running code, not reading. An Azure subscription with a budget alert is enough; use small deployments, delete resources at the end of each week, and avoid provisioned throughput (it bills by the hour).

## Week 1: Foundry foundations and planning (Domain 1, part 1)

- [ ] Read the [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) and its "Updates to the exam" section
- [ ] Create a Foundry resource and project; note the project endpoint format
- [ ] Deploy a small chat model as Global Standard; read the deployment types page and write one scenario for each type
- [ ] Run the Foundry SDK quickstart (`azure-ai-projects` 2.x, `DefaultAzureCredential`, `responses.create`)
- [ ] Assign yourself the narrowest role that still works; try the call with no role to see the error
- [ ] Review: `notes/01-plan-and-manage-ai-solutions.md` (sections up to "Managing, monitoring and securing")

## Week 2: Agents (Domain 2, part 1)

- [ ] Create a prompt agent with `create_version`; chat with it in a conversation; remove the conversation ID and see the follow-up fail
- [ ] Add a function tool; handle `function_call` and return `function_call_output`; make it fail on purpose by not returning the output
- [ ] Create an Azure AI Search index (portal "Import data" wizard is fine), connect it to the project, attach the Azure AI Search tool, read the citations
- [ ] Try the memory search tool (preview) or read the memory concepts page; write down memory vs conversation vs knowledge in your own words
- [ ] Build a two-agent sequential workflow (Foundry portal workflow or Agent Framework `SequentialBuilder`); add a tool that requires approval
- [ ] Review: `notes/02-generative-ai-and-agents.md` (up to "Optimising and operationalising")

## Week 3: Safety, evaluation and observability (Domains 1 and 2)

- [ ] Create a guardrail: content harms at Medium, user prompt attack and document attack detection; assign it to your agent; test a jailbreak and an indirect injection in a document
- [ ] Learn the blocking levels table (Low blocks only high severity; High blocks everything from low up)
- [ ] Build a 20-row test dataset; run groundedness, relevance and response completeness evaluators; read the reasons
- [ ] Connect Application Insights; view server-side traces; add client-side tracing with `AIProjectInstrumentor` and a custom span
- [ ] Write a self-critique loop and a small-model-first cascade
- [ ] Review: rest of `notes/01-...` and `notes/02-...`

## Week 4: Retrieval and extraction (Domain 5)

- [ ] Build an index with a vector field (HNSW profile), a vectorizer and a semantic configuration
- [ ] Run keyword, vector, hybrid and semantic hybrid queries on the same question; compare the top 5
- [ ] Set up an indexer with a skillset: OCR or the Content Understanding skill, Text Split, AzureOpenAIEmbedding; add index projections
- [ ] Run `prebuilt-invoice` with `begin_analyze`; create a custom analyzer with extract, classify and generate fields; inspect confidence and grounding
- [ ] Read the agentic mode page (successor to pro mode)
- [ ] Review: `notes/05-information-extraction.md`

## Week 5: Vision, image and video (Domain 3)

- [ ] Send images to a vision-capable model: short caption, detailed description, alt text plus extended description, grounded visual Q&A
- [ ] Generate an image with a GPT-image model; edit it with a mask; try `input_fidelity`
- [ ] Generate a short Sora 2 video (asynchronous job), then remix it (or read the samples if the model is unavailable in your region)
- [ ] Test an image containing injected instructions; apply document-attack detection to its extracted text
- [ ] Review: `notes/03-computer-vision.md`

## Week 6: Text, speech and final review (Domain 4)

- [ ] Azure Language: PII redaction, sentiment with opinion mining; then the same with a model and a JSON Schema; compare
- [ ] Translator: translate into several languages in one call; compare with an LLM translation of marketing copy
- [ ] Speech: recognise from a file, synthesise with SSML, try speech translation; read the Voice Live overview
- [ ] Review: `notes/04-text-analysis-and-speech.md`
- [ ] [Practice questions](../../practice-questions/azure-ai-apps-agents-developer-ai-103.md); review every wrong answer against the notes
- [ ] Microsoft's free practice assessment on AI Skills Navigator; aim for 80%+ before booking

## Exam week

- [ ] Re-read the "Names you must know" and "Key numbers" tables in the [fact sheet](fact-sheet.md)
- [ ] Flashcards: [flashcards.csv](flashcards.csv)
- [ ] Try the exam sandbox to see the interactive question types
- [ ] Delete your Foundry, Search and Speech resources
