---
last-updated: 2026-10-22
difficulty: intermediate
---

# Google Cloud Generative AI (Self-Directed Track) - Practice Questions

30 questions for the Google Cloud Generative AI study track, covering Gemini models on Agent Platform (formerly Vertex AI), grounding and RAG, agents, evaluation, and responsible AI.

This is a self-directed track rather than a Google exam, so these target working knowledge rather than a published objective list.

> **Cert page:** [exams/gcp/genai/](../gcp/genai/README.md)

---

### Question 1
**Scenario:** Which Google Cloud surface provides access to Gemini and other foundation models with enterprise controls?

A. Compute Engine, where you install and run open-weight models on your own GPU virtual machines
B. Agent Platform, including Model Garden and the Gemini API, with data residency, VPC Service Controls, and CMEK options
C. BigQuery only, since its SQL interface is the single entry point for every hosted model
D. Cloud Functions, which ship with Gemini bundled as a built-in library for every runtime

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Agent Platform is the managed platform with data residency options, VPC Service Controls support, customer-managed encryption keys, and a commitment that customer prompts are not used to train the foundation models. Those enterprise properties are usually why an organization chooses it over a consumer API.
</details>

---

### Question 2
**Scenario:** Answers must be grounded in the organization's own documents with citations.

A. Use a larger model, since extra parameters let it memorize the organization's documents and cite them accurately
B. Fine-tune the model on the documents so it learns their content and can quote the passage it relied on
C. Increase the temperature so the model explores more of the document text before settling on an answer
D. Grounding with Agent Search over your corpus, or a custom RAG pipeline with Vector Search

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Grounding retrieves passages and returns citations, so answers are checkable and update as the documents update. Fine-tuning bakes a snapshot into weights and cannot cite a source, which fails most enterprise requirements on its own.
</details>

---

### Question 3
**Scenario:** A model must return answers grounded in current public web information.

A. Grounding with Google Search, which attaches retrieved web results and links
B. A longer prompt that tells the model to use only information from the current year
C. A larger context window, which lets the model hold more recent web pages from its training data
D. Higher temperature, which makes the model more willing to mention events after its training cutoff

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Search grounding attaches retrieved web results to the request and returns supporting links, which covers the "what happened recently" gap that a model's training cutoff creates. It is a separate configuration from private-corpus grounding and the two can be combined.
</details>

---

### Question 4
**Scenario:** Which parameter should be adjusted to make responses more focused and less random?

A. `temperature` toward 0, optionally with a lower `topP`, tuning one at a time
B. `maxOutputTokens`, since capping response length forces the model to choose its words more carefully
C. `candidateCount`, since generating several candidates and returning the first removes the randomness
D. `stopSequences`, since ending generation at a marker keeps responses focused and removes variation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Temperature scales sampling randomness and topP truncates the candidate distribution. Tuning both hard at once makes behavior difficult to reason about, so pick one. `maxOutputTokens` bounds length and `stopSequences` ends generation at a marker.
</details>

---

### Question 5
**Scenario:** An application needs the model to call an internal API.

A. Function calling: declare the function schema, let the model emit a structured call, run it in your code, return the result
B. Fine-tune the model on recorded API responses so that it can call the API itself during generation
C. Paste the API docs in the prompt and let the model send the HTTP request directly from the Agent Platform endpoint
D. Ask the model to describe the API in plain language, then have it run those described steps against the production endpoint itself

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The model never calls anything itself; it emits a structured request that your code decides whether to execute. That gap is the security boundary: authorization must be checked there, against the calling user's rights, not left to the model.
</details>

---

### Question 6
**Scenario:** Gemini's multimodal capability is used to analyze a video.

A. Extract frames manually and have the model describe each one, then combine the descriptions by hand in a spreadsheet
B. Convert the video to a text transcript first, then send the transcript, since Gemini reads only text and cannot see frames
C. Pass the video directly in the request, since Gemini accepts video, image, audio, and text natively
D. It is not supported, because Gemini accepts only still images and text, not video or audio

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Native multimodality means the model reasons over the video with its temporal and audio context rather than over a lossy text summary you produced first. Frame-by-frame preprocessing throws away exactly the information that makes video analysis useful.
</details>

---

### Question 7
**Scenario:** Safety filters block legitimate content in a medical application.

A. Switch providers to a model with no safety filtering at all, which removes the blocking in a medical setting
B. Tune the configurable harm category thresholds to levels the use case justifies, and add domain checks
C. Rewrite prompts to avoid medical terms, using euphemisms so the classifiers stop flagging it
D. Disable all safety settings, since the application's users are clinicians

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety settings expose per-category thresholds so you can calibrate to context rather than choosing between all and nothing. Loosening them is a documented decision that should come with compensating controls, not a silent configuration change.
</details>

---

### Question 8
**Scenario:** Cost must be reduced for an application with a long, unchanging preamble on every request.

A. More output tokens, so the model can summarize the preamble instead of reading it each time
B. More replicas of the serving endpoint, which cache the preamble in memory across requests
C. A larger model, whose bigger context window means the preamble no longer counts toward the bill, however many times it is sent
D. Context caching for the repeated preamble, so it is processed once and then reused on every later request

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Context caching stores the processed prefix so repeated requests do not re-pay for it, which suits long system instructions, large documents, or a codebase reused across turns. Model routing to a smaller model for simple requests is the complementary lever.
</details>

---

### Question 9
**Scenario:** Output must conform to a JSON schema every time.

A. Controlled generation with a response schema, then validate the parsed result
B. Ask for JSON in the prompt and add an example, which guarantees the format on every response
C. Retry until it works, looping on the parser error and re-sending the same request unchanged
D. Parse with regular expressions that extract the braces, repairing missing fields afterwards

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Constraining decoding to a schema eliminates the class of errors where the model wraps JSON in prose or omits a field. Validation afterwards is still worth keeping, because schema-valid output can still be semantically wrong.
</details>

---

### Question 10
**Scenario:** An agent must complete multistep tasks using several tools.

A. A single prompt that lists every step, which the model works through in one response without tool calls
B. A fine-tuned model that has memorized the tool outputs, so no runtime calls or loop are required
C. Agent Builder on Agent Platform or an agent framework, with per-tool authorization in code and hard limits on loop iterations
D. Chain prompts manually forever, copying each output into the next prompt without any stop condition

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Agents need three things the model cannot provide: an execution loop with termination bounds, tools with narrowly scoped credentials, and authorization evaluated against the calling user. Without those, an agent's blast radius is whatever its service account can do.
</details>

---

### Question 11
**Scenario:** A RAG system returns irrelevant passages.

A. Increase temperature, so the model samples more broadly and finds the relevant passages
B. Improve chunking, add hybrid search and a reranker, and evaluate retrieval separately from generation
C. Shorten the answers, because long outputs dilute the retrieved passages with irrelevant text
D. Use a larger model, since extra reasoning capacity lets it fix a retrieval step that returned the wrong passages

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retrieval and generation fail for different reasons, so measure them separately: recall at k tells you whether the right passage was retrieved at all. If it was not, no change to the generation side can recover it.
</details>

---

### Question 12
**Scenario:** Model quality must be measured before and after a change.

A. Vendor benchmarks, since public leaderboard scores predict quality on any application's own data and domain
B. Manual review of a handful of outputs by the developer, run once after the change and never repeated afterwards
C. The Agent Platform evaluation service with task-appropriate metrics and a dataset of production traffic
D. Latency only, since a faster response always indicates that the model's answers are better

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Public benchmarks say little about your specific distribution. Computation-based metrics and model-based (autorater) evaluation both have a place, and the dataset that matters is one drawn from real requests, including the awkward ones.
</details>

---

### Question 13
**Scenario:** Generated images must be identifiable as AI-generated.

A. Metadata only, such as EXIF fields written at generation, which stay attached after screenshots
B. SynthID watermarking, which embeds an imperceptible, detectable marker in generated media
C. A filename convention, for example prefixing every file with ai-generated, enforced by the storage bucket
D. A caption asking users to be honest about how the image was made

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Watermarking survives common transformations that strip metadata, such as screenshots and re-encoding, which is exactly where filename and EXIF approaches fail. It supports provenance claims rather than relying on downstream honesty.
</details>

---

### Question 14
**Scenario:** Model customization is needed for a specific output style with a few hundred examples.

A. Supervised fine-tuning (including parameter-efficient tuning) on the labeled examples
B. Pretraining a new foundation model on the few hundred examples plus public text, which teaches style quickly
C. RAG over the examples, which changes the model's weights permanently
D. A longer prompt only, with all few hundred examples pasted in, which trains the model on them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Style, format, and task-specific behavior are what fine-tuning teaches well, and parameter-efficient methods make it feasible at that data scale. Reach for it after prompt engineering and few-shot examples stop improving results, not before.
</details>

---

### Question 15
**Scenario:** Which describes Google's responsible AI expectation for a launched feature?

A. A terms-of-service update that tells users the AI may be wrong, with responsibility for harm moved to the user
B. Accuracy testing alone, reported as one aggregate score across all users and signed off by the product owner before launch
C. Nothing specific, since responsible AI guidance applies only to research models, never to launched product features
D. Assess the use case for harms, test performance across affected groups, add safety controls, document limits, and keep a human path for appeals

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The pattern is consistent across major providers: identify harms in context, measure disaggregated performance, apply layered controls, be transparent about limits, and keep a human in the loop where the stakes justify it. Aggregate accuracy is the measure that hides the problems.
</details>

---

### Question 16
**Scenario:** An app must classify millions of short customer messages per day into five categories. Latency and cost matter more than deep reasoning.

A. The largest Pro model at its highest thinking level, so that no message is ever misclassified
B. An image generation model, since it can also read text when the messages are sent as images
C. A Flash-class Gemini model, tested on a labeled sample to confirm that accuracy holds
D. A custom model trained from scratch on the messages, since foundation models are too slow

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Flash-tier Gemini models are built for high-volume, low-latency tasks such as classification, and a labeled sample confirms quality before rollout. The largest model at maximum reasoning adds cost and latency the task does not need. An image model is the wrong modality, and training from scratch is far more work than this task justifies.
</details>

---

### Question 17
**Scenario:** A chatbot must keep the same persona, tone and refusal rules across every turn of a conversation, but users can sometimes talk it out of them.

A. Repeat the persona description in the first user message only, so the model sees it at the start
B. Put the persona and rules in the system instructions, which apply to the whole conversation
C. Raise the temperature so that the model's replies vary more and stay closer to the persona
D. Fine-tune the model on the persona before testing whether instructions alone are enough

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** System instructions are the place for persistent behavior such as role, tone and rules, and the model treats them as applying across the session rather than as one user's request. A rule in the first user turn is easier to override. Temperature adds randomness, and tuning is a heavy step to try before the standard prompt mechanism.
</details>

---

### Question 18
**Scenario:** A summarizer must always return a title line, three bullets and a one-line risk rating. Its output format varies from request to request.

A. Tune the model on 10,000 examples first, since prompts alone cannot control output format
B. Lower the output token limit so that the model has no room to add extra sections or lines
C. Ask for "a consistent format" at the end of the prompt and leave the rest of it unchanged
D. Include two or three examples of the exact output format in the prompt (few-shot prompting)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Few-shot examples show the model the exact structure to follow and are the first tool for consistency before any tuning. A vague request for consistency leaves the format undefined. A lower token limit cuts output rather than shaping it, and tuning is costly when examples usually solve this.
</details>

---

### Question 19
**Scenario:** An analyst needs answers to a few dozen questions about one 600-page technical manual, once. The team is about to build a full RAG pipeline with chunking and a vector database.

A. Build the RAG pipeline anyway, since every document over 100 pages needs chunking and retrieval
B. Summarize each chapter by hand first, then ask the model questions about the summaries instead
C. Use Gemini's long context window and pass the whole manual with the questions, with caching
D. Fine-tune a model on the manual so that it can answer questions about it without the text

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gemini's long context window can hold a manual of this size, which suits a one-off task without building retrieval infrastructure, and context caching cuts the cost of repeated questions. RAG pays off for large or changing collections queried over time. Hand summaries lose detail, and fine-tuning does not reliably teach facts.
</details>

---

### Question 20
**Scenario:** Each month a team must generate product descriptions for 2 million catalog rows stored in BigQuery. Nobody needs the results in real time.

A. Send 2 million online requests from a single script, one row at a time, over several days
B. Submit a batch inference job that reads from BigQuery and writes back, at a lower price
C. Ask the model to write all 2 million descriptions in a single request with one very long prompt
D. Buy provisioned throughput for a full year, since monthly jobs need reserved capacity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch inference processes large offline datasets from BigQuery or Cloud Storage asynchronously, at a discount to online prices and without per-request rate limit pressure. Online requests one by one are slow and costly, one request cannot produce 2 million outputs, and a year of reserved capacity for a monthly job wastes money.
</details>

---

### Question 21
**Scenario:** A semantic search system embeds documents and user queries with the same embedding model, but retrieval quality is weaker than expected.

A. Use a larger output token limit on the embedding model so each vector holds more information
B. Embed the queries with a chat model and the documents with an embedding model to mix strengths
C. Increase the temperature of the embedding model so the vectors cover more possible meanings
D. Set the task type, for example retrieval-document for documents and retrieval-query for queries

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Google's text embedding models accept a task type so that the embeddings are optimized for the use case, with separate document and query types for retrieval. Embeddings have no temperature or output token setting, and vectors from different models are not comparable.
</details>

---

### Question 22
**Scenario:** A bank's security team must make sure data used with Agent Platform cannot be copied to projects outside the bank's organization, even by a user with valid credentials.

A. Create a VPC Service Controls perimeter around the projects and the Agent Platform service
B. Turn on customer-managed encryption keys so that data cannot be moved to any other project
C. Give every user the Viewer role only, so that nobody can call the model APIs in the project
D. Put a note in the project description asking users to keep the bank's data in the project

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VPC Service Controls creates a service perimeter that blocks data from moving to resources outside it, which mitigates exfiltration even with valid credentials. CMEK controls encryption keys, not where data can be sent. Viewer-only access breaks the workload, and a note is not a control.
</details>

---

### Question 23
**Scenario:** A legal team asks whether the contracts it sends to Gemini models on Agent Platform will be used to train Google's foundation models.

A. Yes, every prompt sent to Agent Platform is added to the shared training data for future models
B. Only if the team uses Flash models, since Pro models are excluded from Google's model training
C. No, customer data on Agent Platform is not used to train Google's models without permission
D. Only prompts that trigger a safety filter, which are kept to retrain Google's safety classifiers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Google Cloud's terms for its generative AI services state that customer data is not used to train Google's foundation models without the customer's permission. This does not depend on model tier, and safety filtering does not route customer content into training.
</details>

---

### Question 24
**Scenario:** A production app on a pay-as-you-go Gemini endpoint gets intermittent `429 RESOURCE_EXHAUSTED` errors at peak times, and the business needs predictable capacity.

A. Raise the temperature so that each request finishes faster and frees capacity for others
B. Switch to a model with a longer context window, since it has a separate capacity pool
C. Send each request twice at the same time so that one of the two copies always succeeds
D. Buy provisioned throughput for the model and retry remaining errors with backoff

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Provisioned throughput reserves capacity for a model, which gives predictable throughput for production traffic, and exponential backoff handles the remaining transient errors. Temperature has nothing to do with capacity, duplicate requests increase the load that causes 429s, and context window size does not buy capacity.
</details>

---

### Question 25
**Scenario:** A team built a multi-tool agent in Python with the Agent Development Kit (ADK) and wants Google to host, scale and manage it in production.

A. Run the agent on a single Compute Engine VM with a cron job that restarts it every hour
B. Deploy it to Agent Runtime (formerly Agent Engine), the managed runtime for agents
C. Package the agent as a BigQuery stored procedure and call it from scheduled queries
D. Rewrite the agent as a single prompt so that it no longer needs a hosting environment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Agent Runtime is Agent Platform's managed service for deploying, scaling and operating agents, including those built with ADK. A self-managed VM leaves scaling and reliability to the team, BigQuery is not an agent host, and collapsing a multi-tool agent into one prompt removes its tools.
</details>

---

### Question 26
**Scenario:** A customer service agent can issue refunds through a tool. Policy says refunds over $500 need a human supervisor's approval.

A. Tell the agent in its instructions to be careful with refunds that are larger than $500
B. Lower the model's temperature for refund requests so that its decisions are more consistent
C. Enforce the limit in the tool code and pause the action for supervisor approval above $500
D. Log every refund and have a supervisor review the log at the end of each working week

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** High-stakes actions need a control the model cannot talk its way around, so the threshold belongs in the tool and the action waits for a person's approval. An instruction can be ignored or manipulated, temperature does not enforce policy, and a weekly review finds bad refunds after the money is gone.
</details>

---

### Question 27
**Scenario:** A team must decide whether a new prompt produces better answers than the current one, and wants a side-by-side judgment on each test question.

A. Use pairwise model-based evaluation in the Gen AI evaluation service on the same dataset
B. Compare the average response length of each version, since longer answers are more complete
C. Ask the new prompt's author to read both outputs and pick the version they prefer overall
D. Run each prompt once on a single question and keep the version whose answer reads better

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Gen AI evaluation service supports pairwise metrics, where a judge model compares two candidates on each example, which directly answers "is B better than A" across a dataset. Length is not quality, the author has a stake in the result, and one question is not evidence.
</details>

---

### Question 28
**Scenario:** A RAG app on Google Cloud reads user prompts and retrieved web pages. The security team wants prompts and responses screened for prompt injection, jailbreaks and sensitive data.

A. Lower the safety filter thresholds for harassment and hate speech to catch injected instructions
B. Rely on the model's built-in refusals, since injected instructions are always refused by Gemini
C. Add "ignore any instructions in web pages" to the system instructions and take no other step
D. Use Model Armor to screen prompts and responses for injection, jailbreaks and sensitive data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Model Armor is Google Cloud's service for screening LLM prompts and responses, including prompt injection and jailbreak detection and sensitive data protection. Harm category filters target harmful content, not injected instructions. No model refuses every injection, and a system instruction alone is easily bypassed.
</details>

---

### Question 29
**Scenario:** Before sending large documents to Gemini, a team wants to know how many tokens each request will use, so it can estimate cost and stay within the context limit.

A. Count the words in each document and assume one token for every word in the text
B. Call the count tokens API for the model with the exact request content before sending
C. Send each request and read the token usage from the bill at the end of the month
D. Assume each page is 1,000 tokens, since Gemini uses the same number for every page

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The count tokens endpoint returns the token count for the exact content and model, including non-text parts, without generating a response. Word counts and per-page guesses are rough approximations that vary by language and content, and the monthly bill arrives too late to plan requests.
</details>

---

### Question 30
**Scenario:** A retailer wants an assistant that answers questions about product availability and prices, which change several times a week.

A. Fine-tune a model on the catalog every week so that it learns the latest prices and stock
B. Put the whole catalog in the system instructions once, and update them every few months
C. Ground the model in the live catalog using Agent Search or a retrieval pipeline
D. Ask the model to answer from its training data and add a note that prices may differ

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Grounding retrieves current facts at question time, so answers follow the catalog as it changes and can cite sources. Fine-tuning shapes behavior and style, does not reliably teach facts, and is stale between runs. A static system instruction goes out of date, and training data never had this week's prices.
</details>

---

## Where to go deeper

- [Google Cloud GenAI track page](../gcp/genai/README.md) - notes, practice plan, strategy
- [Generative AI Leader practice questions](gcp-generative-ai-leader.md) - the business-level certification
- [Azure GenAI track practice questions](azure-generative-ai-track.md) - the Azure counterpart
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - the security side of question 10
- **[📖 Agent Platform generative AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)** - primary source
