# Azure AI Engineer Associate (AI-102) - Practice Questions

25 scenario-based questions for AI-102 prep.

> **Cert page:** [exams/azure/ai-102/](../azure/ai-102/README.md)

---

### Question 1
**Scenario:** A company wants to use GPT-4 via Azure OpenAI Service. What's the correct way to deploy?

A. Public endpoint with an API key only, shared by all developers and kept in the application's settings file for simplicity
B. Use OpenAI's public API directly with a company credit card, since the models are identical
C. Provision an Azure OpenAI resource, deploy the model in AI Studio, and call it from an Azure app or private endpoint
D. Self-host the model on a GPU VM in the subscription, because Microsoft lets customers download the GPT-4 weights for that purpose

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure OpenAI is a managed service with enterprise features: customer-controlled networking, RBAC, content filtering, regional residency. Provision the resource, deploy the model in your subscription, and use Managed Identity or Entra ID for auth.
</details>

---

### Question 2
**Scenario:** A team needs to translate documents into 30 languages with formatting preserved. Which service?

A. Azure Translator (Document Translation feature)
B. Azure Form Recognizer, which extracts text and tables from the documents and returns them as JSON
C. Custom Translator, which trains a model on parallel documents and is required for every translation job
D. Azure Speech, which converts spoken audio to text and can read the translated text aloud afterwards

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Translator's Document Translation translates entire documents (Word, PDF, PowerPoint) preserving format. Custom Translator builds custom translation models on parallel corpora; not needed for standard translation.
</details>

---

### Question 3
**Scenario:** Which Azure service extracts structured data (key-value pairs, tables) from invoices and receipts?

A. Azure Computer Vision OCR, which returns the key-value pairs and tables
B. Azure AI Document Intelligence (formerly Form Recognizer), with prebuilt models for invoices, receipts, and IDs
C. Azure Cognitive Search, which indexes the invoices and extracts fields with a built-in invoice model
D. Azure OpenAI, which can read the scanned image and return a fixed table of fields in the same format every time it is asked

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Document Intelligence has prebuilt models for invoices, receipts, IDs, business cards, contracts. Custom models train on your forms. OCR is just text; Document Intelligence understands structure.
</details>

---

### Question 4
**Scenario:** A chatbot must use company-specific knowledge. Which architecture?

A. A custom NLU model only, trained with intents and entities for each question that employees might ask, with new ones added by hand
B. Bot Framework alone, which stores the company knowledge in the bot's state
C. Train GPT-4 from scratch on the company documents
D. RAG: Azure AI Search with a vector index plus Azure OpenAI for generation (the "use your data" feature)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RAG with Azure AI Search is the canonical pattern. AI Studio's "use your data" feature provides a low-code path to ingest documents, embed, index, and ground LLM responses. Bot Framework provides the chat UI.
</details>

---

### Question 5
**Scenario:** Real-time speech-to-text with speaker diarization (who said what)?

A. Azure Cognitive Search, which indexes transcripts and can label the speakers later
B. Azure OpenAI Whisper, which transcribes uploaded audio files one request at a time
C. Azure Speech Service - real-time speech-to-text with speaker diarization, using the Speech SDK conversation transcriber
D. Azure Video Indexer, which only works on uploaded video files

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Speech Service includes speech-to-text with diarization, custom acoustic models, and pronunciation assessment. Video Indexer adds video-specific features but speech is at the Speech Service level.
</details>

---

### Question 6
**Scenario:** Computer Vision custom image classification on 5000 product images?

A. Train from scratch in Azure ML with a custom convolutional network, after requesting GPU quota for the job
B. Azure Custom Vision (custom image classification + object detection)
C. Built-in Computer Vision API with no training
D. Document Intelligence prebuilt models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom Vision is purpose-built for custom image classification and object detection. Upload labeled images, train, deploy via REST or container. Built-in Computer Vision is generic; Azure ML is overkill for standard image-classification.
</details>

---

### Question 7
**Scenario:** Azure Cognitive Search vs Azure AI Search?

A. Cognitive Search is the older service that is being retired in favor of a separate AI Search product
B. They're the same service, rebranded
C. AI Search has fewer features, because vector search was removed when the service was renamed
D. Different services, with separate pricing and APIs, so an index cannot move between them

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Same service, renamed to Azure AI Search to align with the broader Azure AI portfolio. Capabilities: full-text search, vector search, semantic ranking, AI enrichment via skillsets.
</details>

---

### Question 8
**Scenario:** Content moderation for user-generated text (hate speech, harassment, sexual content)?

A. Azure AI Content Safety (hate, sexual, self-harm, violence, with severity levels)
B. Azure OpenAI alone, with a system prompt that asks the model to refuse harmful input of any kind
C. Azure Form Recognizer, which scans user text and flags any phrase that matches its trained categories
D. Azure Translator, which detects the language of each message and removes words that are not appropriate

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure AI Content Safety provides modern moderation across 4 categories with multi-level severity (Safe / Low / Medium / High). Content Moderator is the legacy product still operational but Content Safety is the recommended path.
</details>

---

### Question 9
**Scenario:** Which Azure service generates speech from text in 50+ languages with voice customization?

A. Azure Translator, which converts the text into 50 languages and reads each translation aloud in a neural voice
B. Azure Speech Service - text-to-speech with neural voices and Custom Neural Voice
C. Azure AI Studio, which synthesizes speech directly from text through its portal without any other service
D. Azure OpenAI, which generates spoken audio from text using GPT models in 50 languages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Speech Service text-to-speech: prebuilt neural voices in 100+ languages, plus Custom Neural Voice for brand-specific voices (requires application + speaker recordings).
</details>

---

### Question 10
**Scenario:** Securing an Azure OpenAI deployment - key controls?

A. Public access only, restricted by a firewall rule that allows the company's office IP address range
B. An API key in code, rotated yearly in the config file
C. Private endpoint + Entra ID auth + Managed Identity + content filtering + abuse monitoring
D. No security needed, because Microsoft secures the service and the customer has no shared responsibility at all

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Layered security: network isolation via private endpoints, identity-based auth (RBAC + Managed Identity, not just API keys), content filtering tuned to your use case, abuse monitoring on logs. API keys in code are a recipe for credential leaks.
</details>

---

### Question 11
**Scenario:** A team needs to fine-tune a GPT model on customer support tickets. What's required?

A. Model support for fine-tuning, a curated JSONL training file, enough examples, and tuned hyperparameters
B. Just upload the raw tickets as PDF files to the resource, which fine-tunes the model automatically overnight with no extra setup
C. Train from scratch, which Azure OpenAI supports by letting customers upload their own model weights and architecture
D. Fine-tuning isn't supported in Azure OpenAI

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure OpenAI supports fine-tuning for select models. Requires JSONL training file (prompt-completion pairs or chat format), validation set, and capacity for fine-tuned hosting. Often RAG is faster/cheaper for knowledge updates; fine-tune for stylistic / instruction-following adaptation.
</details>

---

### Question 12
**Scenario:** Which feature controls LLM output to follow a specific JSON schema?

A. Function calling / structured output / response_format
B. Random sampling, with the top-p value set low enough that the output always matches the schema
C. Temperature = 0, which makes the output deterministic and therefore always valid for the schema
D. System prompts only, because the model cannot be constrained by anything outside the prompt text

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Modern OpenAI models support structured output: `response_format={"type": "json_schema", ...}` enforces a JSON schema. Function calling has the model produce arguments matching a function signature. Both are reliable for parseable output.
</details>

---

### Question 13
**Scenario:** Azure AI Studio's primary value?

A. A unified workspace to build, test, evaluate, and deploy generative AI apps, including prompt flow and evaluation
B. Cheaper than other clouds, because every model call made in the portal is billed at a flat discounted rate
C. Replaces Azure ML completely, so custom model training and deployment move into the new portal
D. Only for data scientists, because the portal can be used only through Python notebooks and SDK code

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AI Studio is the GenAI workbench: prompt flow for orchestration, evaluations, fine-tuning, model catalog, content filtering config, deployment. Azure ML is for traditional ML (training/deployment of custom models). They complement each other.
</details>

---

### Question 14
**Scenario:** Detecting prompt injection on user input?

A. Azure AI Content Safety Prompt Shield
B. Cannot be detected
C. Hardcoded blocklists of known attack phrases, maintained by the application team in code
D. Azure Active Directory, which authenticates each caller and rejects users who send malicious prompts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prompt Shield (part of Content Safety) detects prompt injection attempts in user input or in retrieved documents (indirect injection). Use as part of layered defense - sanitize, then filter via Prompt Shield, then evaluate response.
</details>

---

### Question 15
**Scenario:** A team wants to evaluate LLM response quality across 100 prompts on 3 model deployments. What feature?

A. Azure AI Studio Evaluation (groundedness, relevance, similarity, fluency, with built-in or LLM-as-judge evaluators)
B. Azure Test Plans, which runs scripted test cases against the app and records pass or fail results
C. Application Insights, which records latency and failures per request and also scores the answer quality
D. Manual review only, because the quality of a language model answer cannot be measured automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AI Studio Evaluation runs prompts across multiple deployments and scores outputs on relevance, groundedness (RAG-specific), fluency, similarity to ground truth, plus custom metrics. Tracks results over time for regression detection.
</details>

---

### Question 16
**Scenario:** A team uses Azure AI Search with vector index for a RAG bot. Retrieval relevance is poor on multi-sentence questions. Which change usually helps most?

A. Increase the embedding model temperature so that the vectors capture more varied meanings of the question
B. Switch from cosine similarity to dot product
C. Reduce chunk size to 50 tokens
D. Enable hybrid retrieval (BM25 keyword + vector) and add a semantic ranker

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hybrid (keyword + vector) + semantic ranking consistently outperforms vector-only on multi-sentence queries because the ranker re-orders the top-N candidates using a cross-encoder. AI Search exposes both as a single query option. Embedding similarity metric and temperature have far smaller effects.
</details>

---

### Question 17
**Scenario:** Your application sends 8K-token prompts to GPT-4o thousands of times a day, often with the same long system prompt. Cost is high. What helps most?

A. Add more context to every request
B. Disable streaming, because streamed responses are billed at a higher per-token rate than complete ones
C. Switch to GPT-3.5, which has the same quality as GPT-4o and accepts 8K-token prompts at a lower price per token
D. Enable prompt caching on the static system prompt prefix so cached tokens are discounted

**Correct: D**

**Why:** Azure OpenAI supports prompt caching for repeated prompt prefixes (and a "global standard" deployment uses it). Cached tokens are charged at a fraction of normal input rate. Splitting the static system prompt up front and the variable user content at the end maximizes hit rate.

---

### Question 18
**Scenario:** A developer wants to enrich documents in AI Search with custom logic during indexing (e.g., call an internal classifier). Which feature?

A. Power Automate, which can call the internal classifier from a cloud flow whenever a new file lands
B. Indexer schedule, which runs the indexer at fixed intervals and lets you add a classifier call to each run
C. Built-in OCR, which reads the text in images and scanned pages but runs no external code
D. Custom skill - exposed as a Web API skill in the AI Search skillset

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AI Search skillsets chain enrichment steps. Custom skills are HTTPS endpoints (Azure Function is common) that follow the skill input/output contract, letting you plug in classification, redaction, or domain-specific extractors during indexing.
</details>

---

### Question 19
**Scenario:** Bot Framework: which choice connects a published bot to Microsoft Teams without rewriting code?

A. A webhook proxy that forwards Teams messages to the bot and returns its replies to the chat
B. Azure Logic Apps, which relay every message between Teams and the bot through a connector workflow
C. Build a separate Teams app that wraps the bot logic in a new project and publish it again
D. Add a Microsoft Teams channel in Azure Bot resource configuration

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure Bot resources support multiple "channels" (Teams, Web Chat, Direct Line, SMS, etc.) via configuration. The bot logic runs once; channels handle protocol translation. Each channel has its own configuration page in the portal.
</details>

---

### Question 20
**Scenario:** Document Intelligence: which model type is best for extracting fields from a custom contract layout that varies slightly across vendors?

A. Layout API only, which returns raw structure
B. Read API only
C. Custom neural model trained on labeled samples (5+ per layout)
D. Prebuilt invoice model, which handles any document that contains vendor names, dates, and totals

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Custom neural models handle layout variation (vs custom template models which are stricter on positioning). Train on 5+ labeled samples per variant and the model generalizes across similar but non-identical layouts. Layout API gives you raw structure but no field labels.
</details>

---

### Question 21
**Scenario:** A team needs to generate captions for product images at scale, in multiple languages. Which combination is most direct?

A. Document Intelligence + Speech
B. Azure OpenAI vision input + multilingual prompt
C. Custom Vision trained on labeled images
D. Computer Vision describe + Translator, which describes the image in English and then translates it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GPT-4o (and similar) accept image input plus a multilingual prompt and produce captions in any target language in one call. Computer Vision describe + Translator works but adds latency and a translation step. Custom Vision classifies, doesn't caption.
</details>

---

### Question 22
**Scenario:** Responsible AI: a chatbot occasionally outputs ungrounded answers ("hallucinations") despite having retrieval-based context. Which mitigations stack best?

A. Add more training data to the base model so that it memorizes the facts in the company documents, then retrain it every quarter
B. Layered: better retrieval, an abstain instruction in the system prompt, offline groundedness evaluation, and runtime Groundedness Detection
C. Lower temperature only, setting it to 0 so the model always picks the most likely token and never invents text
D. Switch models to the newest and largest one available, since larger models do not produce hallucinations

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hallucinations are a multi-cause problem - retrieval, prompting, and evaluation all contribute. Stacked defenses: improve retrieval quality, instruct the model to abstain, evaluate offline with Groundedness metric, detect at runtime with Content Safety. Single levers (temperature, model swap) rarely solve it alone.
</details>

---

### Question 23
**Scenario:** Speech Service: how do you build a voicebot that can be interrupted mid-sentence by the user?

A. Cancel after each turn, so that the user must wait until the bot finishes before starting to speak again
B. Use the REST API only, sending each utterance as a request and playing the reply when it is returned
C. Speech SDK with continuous recognition, stopping synthesized playback when user speech is detected (barge-in)
D. Polling the service every second for new audio and stopping playback when a transcript is found

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Barge-in / interruption requires continuous recognition (not single-shot) plus the ability to stop the TTS playback when speech is detected. Speech SDK exposes both. REST API is request/response, not appropriate for full-duplex conversation.
</details>

---

### Question 24
**Scenario:** A team builds a multi-agent app in Azure AI Studio's prompt flow. Which design ensures observability and reproducibility across runs?

A. Print to console from each node
B. Disable telemetry, so that no prompt or response data leaves the workspace and results stay private
C. Manual notes in a shared document about each run, listing the settings that the team remembers using for it
D. Enable tracing to Application Insights, save flow versions, and parameterize model deployments

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prompt flow tracing emits per-node spans to App Insights (latency, tokens, errors). Versioned flows + parameterized model deployments make A/B comparison and rollback trivial. This is the GenAI equivalent of structured logging + feature flags.
</details>

---

### Question 25
**Scenario:** Pricing: which decision lever has the largest direct impact on monthly Azure OpenAI spend for a bursty workload?

A. Number of API keys, since each additional key adds a monthly fee to the Azure OpenAI resource
B. Resource group name, which determines the billing tier of every resource placed in the group
C. Choosing between PTU for steady high volume and pay-as-you-go for bursty load, matching the commitment to utilization
D. Region name alone, since every Region bills its own flat monthly fee for the resource

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** PTU buys reserved throughput at a flat hourly rate - cheaper if utilization is high, expensive if idle. Pay-as-you-go is per-token, no commitment - fits bursty / unpredictable load. Wrong choice can swing costs 5-10x. Azure OpenAI does not bill a flat monthly fee per Region (D), per API key (A), or per resource group name (B).
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read prompt engineering + responsible AI sections.
- **<17:** Hands-on with Azure AI Studio + re-read fact-sheet.

AI-102: ~50 questions, 100 minutes, 700/1000 to pass. Strong focus on Azure AI services portfolio and modern GenAI patterns (RAG, prompt flow, evaluation).
