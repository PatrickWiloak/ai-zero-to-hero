---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 12 min
---

# 01 AI Concepts and Responsible AI

Domain 1 of AI-901: **Identify AI concepts and capabilities (40-45%)**. Three skill groups: responsible AI principles, model components and configuration, and recognising AI workloads.

## Responsible AI: the six principles

Microsoft's six principles appear in nearly every Microsoft AI exam. Questions describe a concern and ask which principle it maps to. Learn the trigger words.

| Principle | The question it answers | Trigger words in a scenario | Example |
|---|---|---|---|
| **Fairness** | Does it treat all groups equitably? | bias, discriminate, one group approved less often | A loan model approves fewer applicants from one postcode with the same finances |
| **Reliability and safety** | Does it work as intended, including in unusual conditions, without causing harm? | edge cases, testing, failure, harmful output, rare conditions | A medical triage bot must be tested on rare symptoms before launch; content filters block harmful output |
| **Privacy and security** | Is personal data protected and the system secure? | personal data, consent, data retention, encryption, leaks | Customer recordings used for training only with consent; prompts not retained |
| **Inclusiveness** | Does it work for everyone, including people with disabilities? | accessibility, disabilities, languages, accents | A voice app must handle speech impairments and many accents; captions for deaf users |
| **Transparency** | Do people understand what it is and how it decides? | explain, disclose, understand why, users know it is AI | Telling users they are talking to an AI; explaining which factors drove a decision |
| **Accountability** | Who is responsible for it? | governance, oversight, human review, who answers for it | A named owner, an approval board, a human who can override the system |

Commonly confused pairs:

- **Transparency vs accountability.** Transparency is about *understanding* (explanations, disclosure). Accountability is about *responsibility* (people and processes that answer for the system).
- **Fairness vs inclusiveness.** Fairness is about *outcomes* not differing unjustly between groups. Inclusiveness is about *access*: designing so everyone can use it.
- **Reliability and safety vs privacy and security.** Harmful or wrong outputs are reliability and safety; data exposure and attacks are privacy and security.

In Foundry, these principles show up as concrete features: **content filters** (Azure AI Content Safety) on model deployments, **evaluations** for quality and safety, **transparency notes** published for each service, and access controls on projects. See [Responsible AI basics](../../../../safety/governance/responsible-ai-basics.md) on this site.

## How generative AI models work

You need the concepts, not the maths:

- A **large language model** is trained to predict the next **token** (a word or part of a word) from the text before it. Trained on enormous amounts of text, it learns language, facts and patterns of reasoning. See [LLM basics](../../../../learn/concepts/llm-basics.md) and [How LLMs are trained](../../../../learn/concepts/how-llms-are-trained.md).
- Most current models are **transformers**, which use **attention** to weigh every token against every other token in the context.
- **Embeddings** are lists of numbers representing meaning; similar meanings have nearby vectors. They power semantic search and retrieval.
- **Multimodal** models accept (and sometimes produce) images, audio and video as well as text.
- Models are **non-deterministic** and can **hallucinate**: produce fluent, confident, false statements. **Grounding** (supplying trusted data in the prompt, as in retrieval-augmented generation) reduces this.
- An **agent** is a model that can call **tools** (functions, search, code) in a loop to complete a task, rather than only answering.

## Choosing a model by capability

Questions describe a need and ask for an appropriate kind of model. Think in capabilities, not brand names:

| Need | Appropriate model type |
|---|---|
| Chat, summarisation, drafting, Q&A | A general-purpose language model (a chat completion model) |
| Hard multi-step reasoning, maths, code | A reasoning model (spends more tokens "thinking"; slower and costlier) |
| Understand an image, chart or screenshot in a prompt | A multimodal (vision-capable) model |
| Answer a spoken question or respond in speech | A multimodal model with audio input/output, or Azure Speech plus a language model |
| Create an image from a description | An image-generation model |
| Semantic search, clustering, retrieval | An embedding model |
| High volume, low latency, low cost, simple task | A small or "mini" model |

The [model catalog in Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure) lets you filter by capability, compare benchmarks and see deployment options. See [Which model for which job](../../../../tools/decisions/which-model-for-which-job.md) and [Small language models](../../../../learn/concepts/small-language-models.md).

## Deployment options and configuration parameters

**Deployment** makes a model callable from your project with an endpoint. Things to know:

- **Deployment types** affect where data is processed and how you pay: **Global** deployments route to Microsoft's capacity worldwide; **Data Zone** deployments keep processing within a geography (for example the EU or US); regional deployments stay in one region. Standard (pay per token) versus provisioned throughput (reserved capacity, predictable latency) is the other axis.
- You call a deployment by its **deployment name**, which you choose and which can differ from the model name.

**Configuration parameters** you should be able to explain:

| Parameter | What it does | Turn it up when | Turn it down when |
|---|---|---|---|
| **Temperature** | Randomness of word choice | You want variety (brainstorming, creative text) | You want consistent, factual answers |
| **Top-p** | Restricts choice to the most probable tokens adding up to p | Similar to temperature; usually change one or the other | |
| **Max tokens** (max output tokens) | Caps the length of the response | Long answers are needed | You want short answers or to cap cost |
| **Stop sequences** | Text that ends generation | | |
| **System message / instructions** | Sets role, rules, tone and format for the whole conversation | Always set one | |

Some reasoning models do not accept temperature and use a **reasoning effort** setting instead.

## Identifying AI workloads

The skill is reading a scenario and naming the workload. Clues:

| Workload | What it does | Scenario clues |
|---|---|---|
| **Generative AI** | Creates new text, code, images or audio | draft, summarise, chat, write, generate, create an image |
| **Agentic AI** | Plans and takes actions with tools across steps | book, update the system, multi-step, take action, call an API |
| **Text analysis** | Extracts meaning from existing text | sentiment, key phrases, entities, language detection, PII |
| **Speech** | Converts between speech and text | transcribe, captions, read aloud, voice, spoken |
| **Computer vision** | Understands images and video | detect objects, describe an image, read text in images (OCR), tag |
| **Image generation** | Creates new images | create artwork, product mock-ups from a description |
| **Information extraction** | Pulls structured fields out of documents, images, audio or video | invoice total, form fields, receipt, contract dates, call summary fields |

### Text analysis techniques

- **Keyword (key phrase) extraction:** the main talking points ("battery life", "delivery time").
- **Entity detection (named entity recognition):** people, places, organisations, dates, quantities; **entity linking** connects them to a knowledge base entry.
- **Sentiment analysis:** positive, negative, neutral or mixed, at document or sentence level, often with confidence scores; **opinion mining** ties sentiment to aspects ("the screen is great, the battery is poor").
- **Summarization:** extractive (picks key sentences) or abstractive (writes new sentences).
- Also: language detection, PII detection and redaction.

### Speech

- **Speech recognition (speech to text):** real-time or batch transcription, with features such as diarisation (who spoke) and custom vocabulary.
- **Speech synthesis (text to speech):** neural voices, **SSML** to control pronunciation, pauses and emphasis, and custom voices (with consent requirements).
- **Speech translation:** recognise and translate in one step.

See [Speech AI: ASR and TTS](../../../../learn/concepts/speech-ai-asr-and-tts.md).

### Computer vision and image generation

- **Image analysis:** captions, tags, object detection (with bounding boxes), people detection, **OCR** (reading printed and handwritten text).
- **Image classification vs object detection:** classification labels the whole image; detection finds and locates each object.
- **Face** capabilities are restricted under Microsoft's responsible AI policy (limited access for identification).
- **Image generation** creates images from text prompts; content filters apply to prompts and outputs.

### Information extraction

Taking unstructured content and producing structured fields: from documents and forms (invoices, receipts, IDs), images, audio (call transcripts plus fields such as reason for call) and video (scene descriptions, key moments). In Foundry this is **Azure Content Understanding**; see [note 04](04-information-extraction.md).

## Check yourself

1. A hiring model rejects more applicants over 50 with equivalent qualifications. Which principle? *(Fairness.)*
2. Users must be told they are chatting with an AI. Which principle? *(Transparency.)*
3. You want consistent, repeatable answers for a policy Q&A bot. Which parameter do you lower? *(Temperature.)*
4. "Extract the total, vendor and due date from 10,000 PDF invoices." Which workload? *(Information extraction.)*
5. "Tell me whether each product review is positive or negative." Which workload and technique? *(Text analysis; sentiment analysis.)*
