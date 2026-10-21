# Azure AI Fundamentals (AI-901) Practice Questions

20 scenario-based questions weighted by exam domain, written against the AI-901 skills measured as of 2026-04-15. These are original questions for study, not real exam items.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Identify AI concepts and capabilities | 40-45% | 9 |
| Implement AI solutions by using Microsoft Foundry | 55-60% | 11 |

> **Cert page:** [exams/azure/ai-901/](../azure/ai-901/README.md)

---

## Domain 1: Identify AI Concepts and Capabilities (Questions 1-9)

### Question 1
**Scenario:** A bank's credit model approves applicants from one region less often than applicants from other regions with the same income and credit history. Which responsible AI principle is most directly at stake?

A. Transparency
B. Fairness
C. Inclusiveness
D. Reliability and safety

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Different outcomes for comparable people in different groups is a fairness problem. Inclusiveness is about whether everyone can access and use the system; transparency is about explaining it.
</details>

### Question 2
**Scenario:** A company's chatbot must tell users they are talking to an AI and explain that answers may contain mistakes. Which principle does this support?

A. Accountability
B. Privacy and security
C. Transparency
D. Fairness

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Disclosing that a system is AI and what its limits are helps people understand it: transparency. Accountability is about who is responsible for the system.
</details>

### Question 3
**Scenario:** A voice assistant works well for most users but fails for people with speech impairments. Which principle should the team address?

A. Inclusiveness
B. Transparency
C. Accountability
D. Privacy and security

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Designing so that people with disabilities can use the system is inclusiveness.
</details>

### Question 4
**Scenario:** An organisation creates a review board that must approve every AI system before release and names an owner who can shut a system down. Which principle is this?

A. Reliability and safety
B. Accountability
C. Transparency
D. Fairness

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Governance structures and named responsibility are accountability.
</details>

### Question 5
**Scenario:** A policy Q&A assistant gives slightly different wording and sometimes different facts to the same question. The team wants more consistent answers. Which change is most appropriate first?

A. Increase max tokens
B. Lower the temperature and ground answers in the policy text
C. Switch to an image-generation model
D. Increase top-p to 1.0

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lower temperature reduces randomness; grounding in the source text reduces invented facts. Max tokens only limits length.
</details>

### Question 6
**Scenario:** A retailer wants to know whether each of 2 million product reviews is positive, negative or neutral, and which product aspects customers complain about. Which workload and technique fit?

A. Computer vision; object detection
B. Text analysis; sentiment analysis with opinion mining
C. Speech; speech synthesis
D. Generative AI; image generation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sentiment classifies the overall feeling; opinion mining links sentiment to aspects such as "battery" or "delivery".
</details>

### Question 7
**Scenario:** A logistics firm wants a system that reads incoming emails, looks up the order in its system, books a redelivery and replies to the customer. Which workload best describes this?

A. Text analysis
B. Information extraction
C. Agentic AI
D. Speech recognition

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Planning and taking actions through tools across several steps is agentic AI. Extraction or text analysis alone would not book anything.
</details>

### Question 8
**Scenario:** A developer needs to build semantic search over thousands of internal documents so that "time off" finds pages about "annual leave". Which kind of model is needed for the search index?

A. An embedding model
B. An image-generation model
C. A text-to-speech model
D. A reasoning model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Embeddings represent meaning as vectors so that similar meanings are close together, which is what semantic search needs.
</details>

### Question 9
**Scenario:** A European company must keep the processing of prompts within the EU but does not want to be limited to a single region. Which deployment option fits best?

A. Global deployment
B. Data Zone deployment
C. Running the model on a laptop
D. Provisioned throughput in any region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data Zone deployments keep processing within a geography such as the EU while drawing on capacity across its regions. Global may process anywhere.
</details>

---

## Domain 2: Implement AI Solutions by Using Microsoft Foundry (Questions 10-20)

### Question 10
**Scenario:** You have created a Foundry project. What must you do before your application can send prompts to a model from the catalog?

A. Train the model on your data
B. Deploy the model and call it by its deployment name
C. Create an Azure Machine Learning workspace
D. Export the model weights to Blob Storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A deployment makes a catalog model callable from the project; code refers to the deployment name.
</details>

### Question 11
**Scenario:** You want every response from your support assistant to be under 100 words, friendly, and limited to your products. Where do you put these rules?

A. In each user prompt
B. In the system message (or the agent's instructions)
C. In the deployment name
D. In the max tokens setting only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The system message sets role, rules, scope and tone for the whole conversation. Max tokens only truncates length.
</details>

### Question 12
**Scenario:** A Python chat client contains `AIProjectClient(endpoint=..., credential=DefaultAzureCredential())` followed by `project.get_openai_client()` and `responses.create(model="support-chat", input=question)`. What is `"support-chat"`?

A. The name of the Foundry resource
B. The Azure region
C. The model deployment name
D. The agent's conversation ID

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The `model` parameter takes the deployment name chosen when the model was deployed.
</details>

### Question 13
**Scenario:** In the same client, why does the code use `DefaultAzureCredential()`?

A. It generates a new API key for each call
B. It authenticates with Microsoft Entra ID, using your sign-in locally or a managed identity in Azure
C. It disables authentication for testing
D. It encrypts the prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `DefaultAzureCredential` resolves an Entra ID identity from the environment, avoiding keys in code.
</details>

### Question 14
**Scenario:** You build a prompt agent and a client app. A user asks "What is the capital of France?" and then "And its population?". The agent answers the second question correctly. What made that possible?

A. The deployment type
B. A conversation that keeps the previous turns
C. A higher temperature
D. Content filters

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The conversation holds the history, so "its" can be resolved to France.
</details>

### Question 15
**Scenario:** A field engineer photographs a control panel showing a warning light and asks the app what to do. Which approach fits best?

A. Azure Speech text to speech
B. A vision-capable multimodal model with the image and question in the prompt
C. Azure Language key phrase extraction
D. An embedding model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Open-ended understanding of an image plus a question is what a multimodal model with visual input is for.
</details>

### Question 16
**Scenario:** A broadcaster needs live captions with very low latency for a news stream, and a custom vocabulary for presenter names. Which service fits best?

A. Azure Speech in Foundry Tools (real-time speech to text with phrase lists)
B. An image-generation model
C. Content Understanding on video, run after the broadcast
D. Azure Language summarization

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Real-time transcription with custom vocabulary is a specialised Azure Speech capability.
</details>

### Question 17
**Scenario:** You need a synthesised voice to pronounce a product name correctly and pause before the price. What do you use?

A. Temperature
B. SSML with Azure Speech text to speech
C. Opinion mining
D. Object detection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Speech Synthesis Markup Language controls pronunciation, pauses and emphasis.
</details>

### Question 18
**Scenario:** An insurer receives 30,000 claim PDFs a month and needs the policy number, claim amount and incident date from each, with low-confidence values sent to a human reviewer. Which solution fits best?

A. A chat playground session per file
B. Azure Content Understanding with an analyzer for the fields, using confidence scores for routing
C. Azure Speech batch transcription
D. An image-generation model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content Understanding extracts schema-defined fields at volume and returns confidence scores and grounding, which supports human review of uncertain values.
</details>

### Question 19
**Scenario:** A call centre wants, for each recorded call, the customer's reason for calling, the product mentioned and whether the issue was resolved. Which approach fits best?

A. Content Understanding on audio with extracted, classified and generated fields
B. Azure Vision OCR
C. Text to speech
D. Object detection on the audio waveform

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Content Understanding handles audio, combining transcription with fields you define, including generated values (reason) and classifications (resolved yes/no).
</details>

### Question 20
**Scenario:** A marketing team generates product images with a model in Foundry. Some prompts are refused. What is the most likely reason?

A. The deployment name is wrong
B. Content filters blocked prompts or outputs that violate policy
C. The temperature is too low
D. Image models only accept audio input

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content filters apply to prompts and generated images, supporting the reliability and safety principle. A wrong deployment name would fail every call, not some.
</details>
