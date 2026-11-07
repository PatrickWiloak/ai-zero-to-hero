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

A. Inclusiveness, because the model should be usable by people of different abilities and backgrounds
B. Transparency, because applicants should be told how the model reaches its decisions
C. Fairness, because comparable applicants should receive comparable outcomes in every region
D. Reliability and safety, because the model should perform consistently under expected conditions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Different outcomes for comparable people in different groups is a fairness problem. Inclusiveness is about whether everyone can access and use the system; transparency is about explaining it.
</details>

### Question 2
**Scenario:** A company's chatbot must tell users they are talking to an AI and explain that answers may contain mistakes. Which principle does this support?

A. Transparency: users are told they are dealing with an AI system and what its limits are
B. Accountability: a named owner is responsible for the chatbot's behaviour and can act on complaints
C. Privacy and security: user conversations are protected and handled under data protection rules
D. Fairness: the chatbot treats users from different groups equitably in its answers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Disclosing that a system is AI and what its limits are helps people understand it: transparency. Accountability is about who is responsible for the system.
</details>

### Question 3
**Scenario:** A voice assistant works well for most users but fails for people with speech impairments. Which principle should the team address?

A. Transparency: users are told how the voice assistant recognises and interprets what they say
B. Accountability: named people are responsible for failures and can fix them when they occur
C. Privacy and security: recordings of the user's voice are protected from unauthorised access
D. Inclusiveness: the system should work for people with a range of abilities

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Designing so that people with disabilities can use the system is inclusiveness.
</details>

### Question 4
**Scenario:** An organisation creates a review board that must approve every AI system before release and names an owner who can shut a system down. Which principle is this?

A. Reliability and safety: the system performs as intended, including under unexpected conditions
B. Accountability: people answer for the system, through governance and the authority to stop it
C. Transparency: stakeholders can understand how and why the system behaves as it does
D. Fairness: the system treats comparable groups of people equitably in its outcomes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Governance structures and named responsibility are accountability.
</details>

### Question 5
**Scenario:** A policy Q&A assistant gives slightly different wording and sometimes different facts to the same question. The team wants more consistent answers. Which change is most appropriate first?

A. Lower the temperature and ground answers in retrieved policy passages
B. Raise top-p to 1.0 so the model samples from the full range of likely words
C. Increase max tokens so every answer has room to be complete and detailed
D. Add more examples of friendly phrasing to the system message so the style is stable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lower temperature reduces randomness; grounding in the source text reduces invented facts. Max tokens only limits length.
</details>

### Question 6
**Scenario:** A retailer wants to know whether each of 2 million product reviews is positive, negative or neutral, and which product aspects customers complain about. Which workload and technique fit?

A. Computer vision: image classification on the product photos attached to the reviews
B. Speech: speech-to-text transcription of the recorded customer support calls
C. Generative AI: image generation to illustrate the most common complaints
D. Text analysis: sentiment analysis with opinion mining on the review text

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Sentiment classifies the overall feeling; opinion mining links sentiment to aspects such as "battery" or "delivery".
</details>

### Question 7
**Scenario:** A logistics firm wants a system that reads incoming emails, looks up the order in its system, books a redelivery and replies to the customer. Which workload best describes this?

A. Text analysis: classifying the sentiment and key phrases of each incoming email
B. Agentic AI: a system that plans the steps and calls tools to complete the task
C. Information extraction: pulling order numbers and dates out of each email into fields
D. Speech recognition: transcribing customer voicemails into text for the support team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Planning and taking actions through tools across several steps is agentic AI. Extraction or text analysis alone would not book anything.
</details>

### Question 8
**Scenario:** A developer needs to build semantic search over thousands of internal documents so that "time off" finds pages about "annual leave". Which kind of model is needed for the search index?

A. A text-to-speech model, which reads each document aloud in a natural voice
B. An image-generation model, which creates a thumbnail picture for each document
C. An embedding model, which converts text into vectors that capture meaning
D. A reasoning model, which plans multi-step answers to complex questions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Embeddings represent meaning as vectors so that similar meanings are close together, which is what semantic search needs.
</details>

### Question 9
**Scenario:** A European company must keep the processing of prompts within the EU but does not want to be limited to a single region. Which deployment option fits best?

A. Data Zone deployment, which processes requests within the EU using capacity across several EU regions
B. Global deployment, which routes requests to any Azure region that has spare capacity
C. A single-region Standard deployment, which keeps processing in one region and has no pooled capacity
D. Provisioned throughput in any region, which reserves capacity but does not restrict where processing happens

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data Zone deployments keep processing within a geography such as the EU while drawing on capacity across its regions. Global may process anywhere.
</details>

---

## Domain 2: Implement AI Solutions by Using Microsoft Foundry (Questions 10-20)

### Question 10
**Scenario:** You have created a Foundry project. What must you do before your application can send prompts to a model from the catalog?

A. Fine-tune the model on your own data so that it accepts requests from the project
B. Create an Azure Machine Learning workspace and register the model in it
C. Export the model weights to Blob Storage and load them in your application
D. Deploy the model in the project and call it by its deployment name

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A deployment makes a catalog model callable from the project; code refers to the deployment name.
</details>

### Question 11
**Scenario:** You want every response from your support assistant to be under 100 words, friendly, and limited to your products. Where do you put these rules?

A. In each user prompt, repeated at the start of every question the user types
B. In the deployment name, so the model reads the rules whenever it is called
C. In the system message or the agent's instructions, for the conversation
D. In the max tokens setting, which caps each response and so also sets the tone

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The system message sets role, rules, scope and tone for the whole conversation. Max tokens only truncates length.
</details>

### Question 12
**Scenario:** A Python chat client contains `AIProjectClient(endpoint=..., credential=DefaultAzureCredential())` followed by `project.get_openai_client()` and `responses.create(model="support-chat", input=question)`. What is `"support-chat"`?

A. The name of the Foundry resource that hosts the project and appears in its endpoint URL
B. The model deployment name, chosen when the model was deployed in the project
C. The Azure region where the model deployment is running
D. The ID of the conversation that stores the earlier turns of the chat

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The `model` parameter takes the deployment name chosen when the model was deployed.
</details>

### Question 13
**Scenario:** In the same client, why does the code use `DefaultAzureCredential()`?

A. It authenticates with Microsoft Entra ID, using your sign-in or a managed identity
B. It generates a short-lived API key for the project and renews it automatically on every call
C. It encrypts the prompt before it is sent to the model deployment endpoint
D. It turns off authentication on the project endpoint while you test locally

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `DefaultAzureCredential` resolves an Entra ID identity from the environment, avoiding keys in code.
</details>

### Question 14
**Scenario:** You build a prompt agent and a client app. A user asks "What is the capital of France?" and then "And its population?". The agent answers the second question correctly. What made that possible?

A. The deployment type, because Global deployments remember earlier requests
B. A higher temperature, which lets the model recall more of what was said
C. Content filters, which carry the previous question into the next prompt
D. A conversation that keeps the previous turns, so "its" can be resolved

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The conversation holds the history, so "its" can be resolved to France.
</details>

### Question 15
**Scenario:** A field engineer photographs a control panel showing a warning light and asks the app what to do. Which approach fits best?

A. Azure Speech text to speech, reading the photo's caption aloud to the engineer
B. Azure Language key phrase extraction, run on the engineer's typed question
C. A vision-capable multimodal model, with the image and question in one prompt
D. An embedding model that turns the photo into a vector for storage

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Open-ended understanding of an image plus a question is what a multimodal model with visual input is for.
</details>

### Question 16
**Scenario:** A broadcaster needs live captions with very low latency for a news stream, and a custom vocabulary for presenter names. Which service fits best?

A. Content Understanding on the video, run after the broadcast has ended and the file is saved
B. Azure Speech in Foundry Tools, using real-time speech to text with a phrase list
C. Azure Language summarization, run on the transcript of the finished programme
D. An image-generation model that draws caption text over the video frames

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Real-time transcription with custom vocabulary is a specialised Azure Speech capability.
</details>

### Question 17
**Scenario:** You need a synthesised voice to pronounce a product name correctly and pause before the price. What do you use?

A. A higher temperature on a chat model, so that it varies how it pronounces words
B. Opinion mining on the product description, to find where the price appears
C. Object detection on a recording, to locate the product name in the audio
D. SSML sent to Azure Speech text to speech, with a phoneme and a break element

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Speech Synthesis Markup Language controls pronunciation, pauses and emphasis.
</details>

### Question 18
**Scenario:** An insurer receives 30,000 claim PDFs a month and needs the policy number, claim amount and incident date from each, with low-confidence values sent to a human reviewer. Which solution fits best?

A. Azure Content Understanding with an analyzer for the fields, routing by confidence score
B. A chat playground session per file, copying each answer into a spreadsheet by hand to review
C. Azure Speech batch transcription, followed by a keyword search of the transcripts
D. An image-generation model that redraws each PDF with the fields highlighted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Content Understanding extracts schema-defined fields at volume and returns confidence scores and grounding, which supports human review of uncertain values.
</details>

### Question 19
**Scenario:** A call centre wants, for each recorded call, the customer's reason for calling, the product mentioned and whether the issue was resolved. Which approach fits best?

A. Azure Vision OCR, run on the audio file to read the spoken words
B. Text to speech, to read a written summary of each call back to the agent
C. Content Understanding on audio, with extracted, classified and generated fields
D. Object detection on the audio waveform, to find the product that was mentioned

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Content Understanding handles audio, combining transcription with fields you define, including generated values (reason) and classifications (resolved yes/no).
</details>

### Question 20
**Scenario:** A marketing team generates product images with a model in Foundry. Some prompts are refused. What is the most likely reason?

A. The deployment name is wrong, so the service rejects the request
B. Content filters blocked prompts or outputs that violate the configured policy
C. The temperature is too low, so the model cannot produce the requested image
D. Image models accept only audio input, so text prompts are refused

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content filters apply to prompts and generated images, supporting the reliability and safety principle. A wrong deployment name would fail every call, not some.
</details>
