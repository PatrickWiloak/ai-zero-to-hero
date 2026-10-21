---
last-updated: 2026-08-09
difficulty: intermediate
---

# Google Cloud Generative AI (Self-Directed Track) - Practice Questions

15 questions for the Google Cloud Generative AI study track, covering Gemini models on Agent Platform (formerly Vertex AI), grounding and RAG, agents, evaluation, and responsible AI.

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

## Where to go deeper

- [Google Cloud GenAI track page](../gcp/genai/README.md) - notes, practice plan, strategy
- [Generative AI Leader practice questions](gcp-generative-ai-leader.md) - the business-level certification
- [Azure GenAI track practice questions](azure-generative-ai-track.md) - the Azure counterpart
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - the security side of question 10
- **[📖 Agent Platform generative AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)** - primary source
