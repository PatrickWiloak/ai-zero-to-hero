---
last-updated: 2026-10-22
difficulty: intermediate
---

# Databricks Certified Generative AI Engineer Associate - Practice Questions

30 questions for this exam. Questions 1-15 were written against the older four-domain outline (RAG design and implementation, governance and evaluation, LLM fundamentals). Questions 16-30 follow the six sections of the exam guide live since 2026-03-18 (Design Applications, Data Preparation, Application Development, Assembling and Deploying Applications, Governance, Evaluation and Monitoring), weighted by the widely cited 14/14/30/22/8/12% split; the current guide itself publishes no weights.

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

### Question 16
**Scenario:** A legal team wants structured fields (party names, renewal dates, notice periods) pulled from 50,000 unstructured contracts into a table, with as little custom code as possible.

A. Knowledge Assistant, which answers questions over documents in a chat interface
B. A Vector Search index with no generation step
C. Agent Bricks Information Extraction
D. Multi-Agent Supervisor, which coordinates several existing agents

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Information Extraction is the Agent Bricks option for converting documents into structured fields. Knowledge Assistant is for question answering, not filling a table. A vector index retrieves chunks but extracts nothing. A supervisor coordinates agents that would still need to be built.
</details>

### Question 17
**Scenario:** The business asks for "AI on our support tickets" so a dashboard can show categories and urgency. What should the engineer define first?

A. The input (ticket text) and the output schema
B. The largest model available, since a bigger model will work out the requirement
C. A fine-tuning dataset of 100,000 labelled tickets
D. The GPU type for the serving endpoint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Translating the goal into concrete inputs and outputs comes before choosing models or infrastructure: it fixes the task (classification with a set schema) and makes evaluation possible. Model size, training data and hardware are decisions that depend on that definition.
</details>

### Question 18
**Scenario:** Source PDFs repeat page headers, footers, copyright notices and a two-page legal disclaimer. Retrieval keeps returning these chunks.

A. Increase the chunk overlap so the boilerplate is spread across more chunks
B. Switch to a larger generation model
C. Increase the number of chunks retrieved per query
D. Strip the boilerplate during parsing, before chunking

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Extraneous content that appears in every document competes with real content at retrieval time, so it should be filtered out during preparation. More overlap spreads it further. A larger model does not change what is retrieved. Retrieving more chunks just returns more boilerplate.
</details>

### Question 19
**Scenario:** Chunked text is written to a Delta table in Unity Catalog. Creating a Delta Sync vector index on it fails.

A. Vector Search only reads CSV files, so the table must be exported
B. Change Data Feed must be enabled on the source table
C. The table must be stored outside Unity Catalog
D. Delta Sync indexes require the embeddings to be computed by hand first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A Delta Sync index tracks changes in its source table through Change Data Feed, so the feature must be on. Vector Search reads Delta tables, and Unity Catalog governance is the expected setup. Delta Sync can compute embeddings for you (managed embeddings) or use ones you supply.
</details>

### Question 20
**Scenario:** Documents are chunked at 1,000 tokens, but the chosen embedding model accepts at most 512 tokens. Answers miss details that appear late in chunks.

A. Chunks are truncated by the embedding model's 512-token limit
B. The generation model's context window is too small to hold all of the retrieved chunks at once
C. The vector index needs more replicas
D. The retriever should return fewer chunks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Text beyond the embedding model's limit is cut off, so the second half of each chunk is never represented in its vector. Matching chunk size to the embedding context (or choosing a longer-context model) fixes it. The generator, replicas and result count do not affect what was embedded.
</details>

### Question 21
**Scenario:** A team picks an open model from a model hub for a commercial product that must handle Spanish and German.

A. Choose the model with the most downloads
B. Choose the newest model, since newer is always better
C. Check model cards for licence, languages and evaluation results
D. Choose any model, since all models published on a hub share the same open licence

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Model cards document licence, intended use, languages and benchmarks, which are exactly the constraints here. Popularity and recency do not guarantee a commercial licence or language support, and hub models carry many different licences.
</details>

### Question 22
**Scenario:** Experiments show three models all pass the team's quality threshold on the evaluation set. One is far cheaper and faster than the others.

A. Choose the model with the single highest score, whatever it costs
B. Choose the cheapest, fastest model that meets the quality threshold
C. Run all three in production and let users pick
D. Retrain all three before deciding

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Once the quality bar is met, latency and cost decide. The highest score may not matter if every model meets the bar. Running three in production triples cost and complexity. Retraining is unnecessary when all three already pass.
</details>

### Question 23
**Scenario:** A team has written an agent in Python. They want to log it with MLflow, trace each step, collect feedback from reviewers, and deploy it to a serving endpoint.

A. Copy the code into a notebook cell and share the notebook link with reviewers
B. Package it as a Docker image and run it on a single cluster node
C. Rewrite the agent as SQL so it can run in a warehouse
D. Mosaic AI Agent Framework with MLflow

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Agent Framework and MLflow cover authoring, tracing, logging, registration and deployment, and deploying an agent also creates a review app for feedback. A shared notebook and a single-node container skip tracing, governance and managed serving. Agents are not written in SQL.
</details>

### Question 24
**Scenario:** A multi-agent system needs to answer questions such as "What were our top five products by revenue last quarter?" from governed sales tables.

A. Add a Genie space as an agent in the system
B. Embed every row of the sales tables into a vector index and retrieve rows by similarity
C. Paste the full sales table into the prompt on each request
D. Fine-tune the model on last quarter's sales figures

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Genie spaces turn natural-language questions into queries over structured data, which is the right tool for aggregates like "top five by revenue". Vector similarity is poor at sums and rankings. Pasting whole tables does not scale. Fine-tuned numbers are stale the day after training.
</details>

### Question 25
**Scenario:** A chain logged with MLflow must be registered to Unity Catalog. Registration fails.

A. Unity Catalog only accepts models trained with Spark ML
B. Use the Unity Catalog registry URI, a three-level name and a signature
C. Models must be registered to a workspace folder first
D. Registration only works from the Databricks UI, not from code running in a notebook or job

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Registering to Unity Catalog needs the registry URI set to Unity Catalog, a catalog.schema.model name and a model signature (an input example lets MLflow infer one). Any MLflow flavour can be registered, there is no folder step, and registration from code is the normal path.
</details>

### Question 26
**Scenario:** Every night, five million product reviews in a Delta table must be classified by sentiment with an LLM. Analysts work in SQL.

A. A Python loop calling a chat endpoint one review at a time from a notebook
B. Fine-tune a model to output the sentiment and deploy it to a real-time endpoint
C. Use ai_query() in a SQL query to call the model over the table as a batch workload
D. Copy the reviews into a spreadsheet and use a browser extension

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** ai_query() applies a served model to rows directly in SQL, which is built for batch inference on tables. A one-at-a-time loop is slow and fragile. A real-time endpoint is designed for interactive traffic, and fine-tuning is not needed for sentiment. Spreadsheets do not scale to millions of rows.
</details>

### Question 27
**Scenario:** A Vector Search use case will hold close to a billion 768-dimension embeddings, is cost-sensitive, and can tolerate a little more query latency.

A. A standard endpoint, which is designed for the lowest latency at small scale
B. Ten separate small indexes, queried one after another and merged
C. No index, computing similarity against every vector at query time
D. A storage-optimized endpoint, which trades a little latency for scale and cost

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Storage-optimized endpoints hold roughly a billion vectors at 768 dimensions (about three times a standard endpoint's ~320 million), index 10-20 times faster and are priced for large vector counts, in exchange for about 250 ms of extra query latency. That matches the requirements. Standard endpoints suit lower latency at smaller scale. Splitting into sequential indexes adds latency and complexity. Brute force over a billion vectors is not practical.
</details>

### Question 28
**Scenario:** A team wants to add a scraped web dataset to a RAG application. The site's terms forbid commercial reuse.

A. Exclude the dataset or obtain a licence that permits the use, and record the source's terms
B. Use it anyway, since retrieval does not copy the data
C. Use it but remove the site's name from the documents
D. Use it only in production, not in testing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Legal and licensing requirements on data sources apply to RAG just as to training: the content is stored, indexed and shown to users. Removing attribution makes it worse. Restricting the use to production does not change the licence terms.
</details>

### Question 29
**Scenario:** An evaluation run uses several LLM judges. The team has no expected answers yet. Which judge cannot run without ground truth?

A. Safety
B. Relevance of the response to the query
C. Groundedness of the response in the retrieved context
D. Correctness, which compares the response to an expected answer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Correctness needs an expected response or expected facts to compare against. Safety, relevance and groundedness are judged from the request, response and retrieved context alone, so they run without labels.
</details>

### Question 30
**Scenario:** A RAG agent is live on a serving endpoint. The team needs to see real requests and responses, token usage and latency, and to spot quality problems over time.

A. Ask users to email screenshots of bad answers
B. Inference tables, usage tracking and monitoring with judges
C. Re-run the offline evaluation set once a year
D. Turn on debug printing in the agent code and read the cluster logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inference tables log requests and responses to Delta, usage tracking records tokens, and monitoring can score that traffic with LLM judges, which gives a continuous view of production. Screenshots, yearly offline runs and debug prints are incomplete and do not scale.
</details>

---

## Where to go deeper

- [GenAI Engineer Associate cert page](../databricks/genai-engineer-associate/README.md) - notes, practice plan, strategy
- [Databricks ML Associate practice questions](databricks-ml-associate.md) - the classical ML sibling
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in plain English
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - questions 8 and 10 in depth
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
