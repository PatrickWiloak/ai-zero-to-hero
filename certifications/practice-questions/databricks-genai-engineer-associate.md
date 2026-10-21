---
last-updated: 2026-08-09
difficulty: intermediate
---

# Databricks Certified Generative AI Engineer Associate - Practice Questions

15 questions for this exam, weighted toward RAG application design (30%) and implementation (30%), then governance and evaluation (20%) and LLM fundamentals (20%).

> **Cert page:** [exams/databricks/genai-engineer-associate/](../databricks/genai-engineer-associate/README.md)

---

### Question 1
**Scenario:** A RAG application must answer questions from internal policy documents.

A. Train a model from scratch
B. Chunk and embed the documents into a Vector Search index, retrieve chunks at query time, and generate from them
C. Fine-tune a model on the documents so that the policy text is stored in its weights and answers are always current without reindexing
D. Put all of the documents into the prompt on every single request and let the model find the relevant policy text on its own

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAG separates knowledge from the model, so updating a policy means reindexing rather than retraining, and the retrieved chunk can be cited. Fine-tuning teaches behavior far better than it teaches facts, and full-document prompting hits context and cost limits quickly.
</details>

---

### Question 2
**Scenario:** A Delta table of documents must stay in sync with a vector index.

A. A Delta Sync Vector Search index, which updates as the source table changes
B. Manual upserts
C. Rebuild the index by hand each night from a full table export, accepting that it lags the data by a day
D. Export the table to CSV files and upload them to the index through the workspace UI each week

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Delta Sync indexes track the source table and update automatically, which removes the class of bugs where the index silently falls behind the data. Direct Vector Access indexes are the alternative when you manage embeddings and writes yourself.
</details>

---

### Question 3
**Scenario:** Chunk size must be chosen for a corpus of long technical manuals.

A. One chunk per document
B. Chunk size does not matter
C. Chunks sized to hold a complete idea with some overlap, ideally split on document structure such as sections rather than fixed character counts
D. One sentence per chunk

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Whole documents dilute the embedding so retrieval returns everything weakly; single sentences lose the context needed to answer. Structure-aware splitting with overlap keeps facts intact across boundaries, and it is the highest-leverage tuning knob in most RAG systems.
</details>

---

### Question 4
**Scenario:** Retrieval misses documents when the user's query uses different wording from the source.

A. Keyword search only, matching the exact words that appear in the source documents, with no synonym expansion
B. Increase temperature
C. Vector (semantic) search, optionally hybrid with keyword search for exact identifiers
D. A bigger model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Embeddings capture meaning rather than surface form, which is why a paraphrased query still retrieves. Hybrid search adds back the exact-match strength that dense retrieval lacks for error codes, part numbers, and rare proper nouns.
</details>

---

### Question 5
**Scenario:** A model endpoint must serve an external foundation model and a fine-tuned model behind one interface.

A. Manual routing
B. Mosaic AI Model Serving with external and custom model endpoints, optionally behind an AI Gateway
C. A load balancer in front of the two providers' separate APIs, which translates request formats and tracks usage
D. Two applications

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Serving fronts foundation model APIs, external providers, and your own registered models with one interface, and the gateway layer adds rate limiting, usage tracking, and credential management. That means switching providers does not mean rewriting the application.
</details>

---

### Question 6
**Scenario:** A chain of retrieval, prompt, and model must be tracked and versioned.

A. A notebook only, kept in the author's workspace folder, with the chain cells run by hand each time
B. A text file in a shared folder holding the prompt template and the name of the model version in use
C. Log the chain as an MLflow model, register it in Unity Catalog, and deploy that version
D. Copy the code to production by hand each time a change is ready, and rename the folder with the date

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Logging the whole chain rather than just the model makes the deployed artifact reproducible, including the prompt template and retrieval configuration. Registering in Unity Catalog gives it the same governance, lineage, and access control as data.
</details>

---

### Question 7
**Scenario:** The application must be evaluated for answer quality against ground truth.

A. User complaints collected through the support desk after release, reviewed once a month by the product owner
B. Latency only, measured as the median response time per request across a full week of real production traffic
C. Spot checks by the team on a handful of favorite questions before each release, recorded in a shared document
D. An evaluation set with metrics like correctness, groundedness and retrieval recall, run on each change

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Separating retrieval metrics from generation metrics matters because they fail for different reasons. Mosaic AI Agent Evaluation supports LLM-judge metrics alongside human review, and running it on every prompt or model change is what catches silent regressions.
</details>

---

### Question 8
**Scenario:** Retrieval must respect who is asking, so users only see permitted documents.

A. Rely on the model's training, which teaches it not to repeat documents the current user is not entitled to see
B. Post-process the answer by scanning it for document titles and removing any the user may not see
C. Filter at retrieval time by metadata reflecting the user's entitlements, enforced in code
D. Instruct the model in the system prompt to refuse any request for documents the user may not see

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Once content is in the context window it can appear in the output, so authorization must happen before retrieval returns. A prompt instruction is advisory and can be overridden by injected text in a retrieved document.
</details>

---

### Question 9
**Scenario:** Model responses must be traced for debugging and audit.

A. Print statements
B. No logging
C. Only errors
D. MLflow Tracing capturing spans for retrieval, prompt construction, and generation, plus inference tables logging requests and responses

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A wrong answer is usually a retrieval problem, and you cannot tell without seeing which chunks were retrieved. Tracing makes each step inspectable, and inference tables put production traffic into a Delta table you can query and build evaluation sets from.
</details>

---

### Question 10
**Scenario:** An agent must call tools to complete a task.

A. The model emits a tool call, your code runs it with a scoped credential and authorization check
B. The model executes tools itself, calling each API directly with the credentials supplied in its system prompt
C. Give the agent admin access
D. Skip authorization

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The execution step is where security lives, because the model is an untrusted planner that a retrieved document may have influenced. Unity Catalog functions as tools help here by carrying their own governance and grants.
</details>

---

### Question 11
**Scenario:** An embedding model is upgraded.

A. Increase the index size
B. Re-embed the entire index, because vectors from different models are not comparable
C. Re-embed new documents only, since existing vectors stay valid and only the new content needs the upgraded model
D. No further action is needed, because the new model can read the old vectors in the index without a problem

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mixing embedding spaces produces meaningless similarity scores, so a partial reindex is worse than no upgrade. Build the new index alongside the old one and cut over after validating, which is blue-green applied to retrieval.
</details>

---

### Question 12
**Scenario:** Unsafe or off-topic outputs must be constrained.

A. Prompt instructions alone
B. Layered guardrails: input and output classifiers, gateway topic limits, and measured violation and false refusal rates
C. Reduce the max tokens
D. Lower temperature, which makes the model deterministic and therefore stops it producing unsafe or off-topic text on any input

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve rather than a switch, so measuring false refusals matters as much as measuring violations: an over-blocking assistant is also a failed product. Prompt instructions are the weakest layer because injected content competes with them.
</details>

---

### Question 13
**Scenario:** Costs rise sharply as usage grows.

A. Measure tokens per request, use smaller models for simple steps, cache repeated prefixes, cap context
B. Increase the model size, since a larger model answers correctly more often, so fewer retries and fewer total tokens are needed per resolved task
C. Add more serving endpoints in several other regions so that each one carries a smaller share of the total traffic
D. Accept the rise as the normal price of growth, and revisit the bill again only when the quarter closes and finance asks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost is driven by tokens in and out, and retrieved context is often the largest and least examined contributor. Trimming top-k after measuring the effect on quality frequently reduces cost without any measurable loss.
</details>

---

### Question 14
**Scenario:** Which describes the difference between prompt engineering, RAG, and fine-tuning?

A. RAG replaces the model
B. They are interchangeable techniques that give the same results on every task, so the choice is purely a matter of team preference and cost
C. Fine-tuning is always best, because changing the weights gives the model permanent, up-to-date knowledge of your data and so removes any need for retrieval or prompts
D. Prompt engineering shapes behavior with instructions, RAG supplies knowledge at query time, and fine-tuning adjusts weights

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** They address different needs and cost increases in that order. Most production systems combine them: a tuned prompt, retrieval for facts, and optionally fine-tuning for format consistency the prompt could not reliably enforce.
</details>

---

### Question 15
**Scenario:** A model serving endpoint must scale down when idle.

A. A fixed provisioned endpoint
B. Scale-to-zero on the endpoint, accepting cold start latency on the first request after idle
C. Delete the endpoint each night and recreate it each morning
D. A larger instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scale-to-zero suits development and intermittent internal tools where a few seconds of cold start is acceptable. Interactive user-facing applications usually keep a warm minimum, so the choice follows the latency requirement rather than the cost target alone.
</details>

---

## Where to go deeper

- [GenAI Engineer Associate cert page](../databricks/genai-engineer-associate/README.md) - notes, practice plan, strategy
- [Databricks ML Associate practice questions](databricks-ml-associate.md) - the classical ML sibling
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in plain English
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - questions 8 and 10 in depth
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
