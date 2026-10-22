# OCI Generative AI Professional (1Z0-1127) - Practice Questions

30 questions for OCI Generative AI Professional prep. Three decisions recur: how to customize, on-demand versus dedicated cluster, and where retrieval quality comes from.

> **Cert page:** [exams/oracle/oci-generative-ai-professional/](../oracle/oci-generative-ai-professional/README.md)

---

### Question 1
**Scenario:** An insurer wants an assistant answering questions about policy documents. Documents change monthly, answers must cite the source clause, and there are no ML engineers.

A. Fine-tune a base model on the policy corpus each month so the clause wording is learned into its weights
B. Pre-train a domain model on the insurer's own documents from scratch
C. RAG over the policy documents, citing the retrieved clause
D. Put all documents in the prompt on every request and rely on the model to find the clause

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Monthly updates rule out fine-tuning, whose knowledge is frozen at training time. Citation requires knowing which source text produced the answer, which only retrieval provides. Putting all documents in the prompt exceeds the context window and costs enormously.
</details>

---

### Question 2
**Scenario:** A team has fine-tuned a model and wants to serve it to production with a latency commitment.

A. Either, depending on volume
B. A dedicated AI cluster, which is required to host a custom model and gives reserved capacity for latency
C. OCI Data Science model deployment, the managed service for serving fine-tuned models
D. On-demand inference

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On-demand serves base models only. Both fine-tuning and hosting a custom model require dedicated AI clusters, and dedicated capacity is also what makes a latency commitment possible. This is a hard constraint, not a preference.
</details>

---

### Question 3
**Scenario:** A RAG chatbot gives confidently wrong answers although the information is in the corpus. The team increased retrieved chunks from 3 to 20 and it got worse.

A. Raise the temperature so the model explores other phrasings and is less anchored to the wrong passages it retrieved
B. Log the retrieved chunks to check the right one is present, then cut the count and consider reranking
C. Increase the chunk count further, to 40, so that more of the corpus reaches the model and the right passage is certain to be included
D. Fine-tune the model on the corpus

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Diagnose before changing. If the correct chunk is retrieved but ignored, 20 chunks is likely the cause because models attend less to the middle of a long context. If it is not retrieved, the problem is chunking, the embedding model, or query phrasing. Raising temperature increases variety, not correctness.
</details>

---

### Question 4
**Scenario:** A pipeline extracts structured fields from contracts and produces slightly different values on repeated runs, breaking downstream reconciliation.

A. Set temperature to 0 and validate the output against a schema
B. Fine-tune the model on labelled contracts so that it always returns identical values for the same contract text
C. Increase max tokens so that the model has room to finish every extraction
D. Retry each extraction until two runs agree, then keep the shared value

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Temperature is the primary control over randomness, and 0 gives near-deterministic decoding. Schema validation is the safety net, since output is not guaranteed identical across model versions. Fine-tuning is an expensive answer to a decoding parameter problem.
</details>

---

### Question 5
**Scenario:** Inference costs tripled. Every request sends the full conversation history, 15 retrieved chunks, and a 2,000-token system prompt.

A. Reduce retrieved chunks, window or summarize memory, shorten the system prompt, cap max tokens
B. Reduce traffic
C. Cache whole responses
D. Move to a dedicated cluster, because a fixed hourly price always works out cheaper than per-token billing at any volume

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cost is driven by tokens in and out. The largest levers, in order, are retrieved context size, conversation history handling, and system prompt length. A dedicated cluster gives predictable cost, not necessarily lower cost. Response caching helps only for repeated identical questions.
</details>

---

### Question 6
**Scenario:** A multi-tenant assistant returns one organization's content to a user from another. What is the correct fix?

A. Filter by tenant in the vector query or use per-tenant namespaces, authorizing on user identity
B. Deploy a separate fine-tuned model per tenant, with documents baked into the weights
C. Post-filter results after generation
D. Instruct the model in the system prompt not to reveal other tenants' data

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** This is a retrieval authorization bug. A prompt is not an access control. Post-filtering is too late because the data has already entered the model's context. Separate models per tenant is enormously expensive and does not address the retrieval boundary.
</details>

---

### Question 7
**Scenario:** Which statement about fine-tuning versus RAG is correct?

A. They are alternatives that cannot be combined, since a tuned model cannot take retrieved context
B. RAG requires retraining when documents change
C. Fine-tuning is always more accurate
D. Fine-tuning changes how the model behaves; RAG changes what it knows on each request, so they can be combined

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** This is the decision rule the exam applies throughout. RAG updates instantly when source documents change, which is precisely why it beats fine-tuning for knowledge. The two can be combined: a fine-tuned model answering over retrieved context.
</details>

---

### Question 8
**Scenario:** Chunks are set to 50 tokens each. Answers cite the right documents but lack coherent explanation.

A. Change the similarity metric from cosine to dot product, since the right documents are found but ranked by the wrong measure
B. Lower the temperature
C. Increase chunk size, add overlap, and split on structural boundaries
D. Retrieve fewer chunks

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Chunks that are too small lack surrounding context, so retrieval finds the right words but the model cannot ground a coherent answer. Larger chunks with overlap, split on paragraphs or sections, resolve it. The similarity metric and temperature address different problems.
</details>

---

### Question 9
**Scenario:** Which LangChain component holds prior conversation turns and is a major cost driver?

A. Output parser that formats the model's reply into a structured object
B. Text splitter that cuts the source documents into chunks
C. Memory, the component that buffers earlier turns
D. Retriever

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Naive memory resends the whole conversation each turn, so token use grows sharply over a long session. Windowed memory keeps only recent turns and summary memory compresses older ones, both of which control the cost.
</details>

---

### Question 10
**Scenario:** What must be true for a query embedding to retrieve the right chunks?

A. The query must use exactly the same words as the document, since matching is done on shared vocabulary rather than meaning
B. The query must be embedded with the same model that indexed the chunks
C. The chunks must be sorted alphabetically by their source document title before upload
D. The vector store must use Euclidean distance rather than cosine similarity or dot product

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embeddings from different models occupy different vector spaces, so similarity between them is meaningless. Semantic search exists precisely so that queries need not share wording with documents, and the metric must match how the embedding model was trained.
</details>

---

### Question 11
**Scenario:** Which parameter should be adjusted to make output less repetitive over a long generation?

A. Top-k set to 1, so the model always picks its single most likely token and cannot loop over the same phrases
B. Max tokens
C. Temperature set to zero
D. Frequency penalty

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Frequency penalty reduces the likelihood of tokens in proportion to how often they have already appeared, which directly targets repetition. Presence penalty discourages tokens that have appeared at all. Top-k of 1 is greedy decoding, which usually increases repetition.
</details>

---

### Question 12
**Scenario:** A RAG system must be evaluated. What should be measured?

A. Answer quality only, scored end to end by reviewers, because retrieval problems always show up in the final answer
B. Retrieval quality and answer quality, measured separately
C. Token throughput
D. Model perplexity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They fail for different reasons and need different fixes. Retrieval is measured by whether the correct source appeared in the top K and how highly it ranked; answer quality by faithfulness, relevance, and correctness. Perplexity evaluates a model, not an application.
</details>

---

### Question 13
**Scenario:** Which parameter-efficient fine-tuning method does OCI Generative AI offer?

A. Distillation
B. Quantization
C. T-Few
D. Full fine-tuning only

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** T-Few updates a fraction of the weights, which makes fine-tuning far cheaper and faster than full fine-tuning and reduces the amount of training data required. Distillation and quantization are model compression techniques, not fine-tuning methods.
</details>

---

### Question 14
**Scenario:** What is the primary risk of retrieving from a corpus that outside parties can write to?

A. Slower retrieval, because every outside write forces a complete re-index that locks the vector store until it finishes
B. Higher embedding costs
C. Duplicate chunks
D. Indirect prompt injection: planted instructions reach the model via retrieved text

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Anything an outsider can write into the corpus can be retrieved into a future prompt, which makes the index a delivery vehicle for instructions. Controlling write access to the corpus and constraining what the application can do are the mitigations.
</details>

---

### Question 15
**Scenario:** Which is the correct order of the RAG indexing phase?

A. Chunk the documents, embed the chunks, store vectors with metadata
B. Store the documents, generate, then embed
C. Embed the query, search the vector store, retrieve the top chunks, and generate an answer from them
D. Fine-tune the model, deploy it to a dedicated cluster, and then evaluate it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Indexing runs once, or on document change: chunk, embed, store. The query phase is the other option listed: embed the query, search, retrieve, augment the prompt, generate. Keeping the two phases distinct is the basis for diagnosing where a RAG system fails.
</details>

---

### Question 16
**Scenario:** A developer sets top-p to 0.9 for a text generation call. What does this setting do?

A. It keeps only the 90 most likely tokens at each step and samples from those
B. It samples from the smallest set of tokens whose probabilities add up to at least 0.9
C. It makes the model 90% certain of each answer before it returns any output at all
D. It limits the response to 90% of the maximum output tokens set for the request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Top-p (nucleus) sampling keeps the most likely tokens until their cumulative probability reaches p, then samples within that set, so the candidate pool grows or shrinks with the model's confidence. A fixed count of candidates is top-k. Top-p is not a confidence guarantee and has nothing to do with output length.
</details>

---

### Question 17
**Scenario:** A model generates a product FAQ, but keeps writing extra unrelated questions after the last required answer. Each answer ends with a known marker line.

A. Raise the temperature so the model is more likely to choose an ending token sooner
B. Increase the frequency penalty so that the model stops repeating the question format
C. Lower top-k to one, so that the model can only pick the end-of-text token after each answer
D. Set a stop sequence on the marker so generation ends as soon as the model produces it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A stop sequence ends generation when the specified string appears, which cuts off unwanted continuation at a known boundary. Temperature and top-k change which tokens are chosen, not where generation ends, and a frequency penalty discourages repeated tokens without stopping output.
</details>

---

### Question 18
**Scenario:** A model often gets multi-step pricing calculations wrong when it is asked for only the final number.

A. Ask it to work through the steps before giving the final answer (chain-of-thought prompting)
B. Lower the maximum output tokens, so the model has to reach the answer in fewer steps
C. Fine-tune the model on final answers only, so that it memorizes the right numbers
D. Increase the presence penalty, so the model avoids reusing numbers it has already seen

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Chain-of-thought prompting asks the model to lay out intermediate steps, which improves accuracy on multi-step reasoning. Fewer output tokens remove room for those steps, memorizing answers does not teach the calculation, and a presence penalty would push the model away from numbers it needs to reuse.
</details>

---

### Question 19
**Scenario:** A team adds three labeled examples to a prompt and the model's classification accuracy improves. A manager asks whether the model has now been retrained.

A. Yes, the examples update the model's weights each time the prompt is sent to the service
B. Yes, but only for the duration of the dedicated AI cluster's current billing period
C. No; few-shot prompting works in context, and the weights do not change
D. No, because examples only affect the format of the output and never its accuracy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Few-shot (in-context) learning conditions the model on examples within the prompt; the weights are untouched, and the effect lasts only for that request. Changing weights requires fine-tuning. Examples can improve accuracy as well as format, as the scenario shows.
</details>

---

### Question 20
**Scenario:** A team designing a RAG system asks which kind of model produces the vectors for its document index and which writes the final answers.

A. A generation model produces both, using its final output tokens as the vectors
B. A fine-tuned model produces the vectors, and a base model writes the final answer
C. An image model produces the vectors, since vectors are a form of picture of the text
D. An embedding model produces the vectors, and a generation (chat) model writes answers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RAG uses two kinds of model: an embedding model turns text into vectors for semantic search, and a generation model reads the retrieved text and writes the answer. Generated tokens are not embeddings, fine-tuning is not what makes a model produce vectors, and image models are irrelevant here.
</details>

---

### Question 21
**Scenario:** A team wants to fine-tune a base model in OCI Generative AI on its support transcripts and then serve the result to an internal app.

A. Create a fine-tuning dedicated AI cluster for training, then host the custom model on a hosting cluster
B. Fine-tune it on demand with no cluster, then call the custom model through the on-demand endpoint
C. Upload the transcripts to Object Storage, since the service fine-tunes any model found there
D. Fine-tune it on a laptop and upload the weights to the on-demand endpoint for serving

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In OCI Generative AI, fine-tuning runs on a dedicated AI cluster, and a custom model can only be served from a dedicated hosting cluster through an endpoint. On-demand inference serves the pretrained base models, not custom ones, and the service does not train automatically from Object Storage or accept arbitrary uploaded weights.
</details>

---

### Question 22
**Scenario:** Only the platform team may create dedicated AI clusters and run fine-tuning, while application developers may call existing endpoints.

A. Put a note in the project wiki asking developers not to create any clusters themselves
B. Use separate IAM policies and compartments scoped to each group's Generative AI resources
C. Give all users administrator access and review the audit log for cluster creation each month
D. Share a single user account between both teams so that all activity comes from one identity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI IAM policies, scoped to compartments, control who can manage clusters and fine-tuning and who can only use endpoints, which enforces the split. A wiki note is not a control, administrator access with later review grants the permission first, and a shared account destroys accountability.
</details>

---

### Question 23
**Scenario:** A bank requires that calls from its applications to OCI Generative AI do not cross the public internet.

A. Use a longer API key so that traffic over the public internet is harder to intercept
B. Enable customer-managed encryption keys, which route traffic over private paths
C. Use a private endpoint so the service is reached from the bank's VCN over private paths
D. Restrict usage to business hours, when traffic is monitored more closely by the bank

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A private endpoint lets resources in a VCN reach the service without traversing the public internet. Encryption keys protect data at rest, not network routes, key length does not change the path traffic takes, and restricting hours is unrelated to network exposure.
</details>

---

### Question 24
**Scenario:** An HR team wants a question-answering assistant over its policy PDFs, with citations, live within weeks. It has no need to tune chunking or retrieval.

A. Fine-tune a model on the PDFs so that it can quote each policy from memory with citations
B. Build a custom pipeline in LangChain with its own chunking, embeddings and vector store
C. Paste all the PDFs into the system prompt of an on-demand chat model for every request
D. Use OCI Generative AI Agents over the documents, which manages ingestion and retrieval

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Agents service connects to a data source and handles ingestion, chunking, embedding and retrieval, returning grounded answers with citations, which fits a fast launch with no special retrieval needs. A custom pipeline is for when you need that control. Fine-tuning does not give reliable citations, and pasting every PDF into each request is costly and limited by the context window.
</details>

---

### Question 25
**Scenario:** A hospital's compliance officer asks whether prompts sent to OCI Generative AI will be used to train Oracle's base models.

A. Yes, every prompt is added to the training data used for the next base model release
B. No, customer data sent to the service is not used to train Oracle's base models
C. Only prompts sent through on-demand inference, since dedicated clusters are excluded
D. Only if the prompts contain medical terms, which are kept to improve the safety filters

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data submitted to OCI Generative AI is not used to train the base models, and dedicated AI clusters add infrastructure isolation on top. This does not depend on the inference mode or the content of the prompts.
</details>

---

### Question 26
**Scenario:** A RAG system splits manuals into fixed 400-token chunks. Answers often miss a step because the steps of one procedure are split across two chunks.

A. Add overlap between consecutive chunks, or split on section boundaries instead
B. Cut the chunk size to 50 tokens so that each step lands in a chunk of its own
C. Retrieve only one chunk per query so the model is not confused by partial steps
D. Use a higher temperature so the model fills in the missing steps by itself

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Overlap carries context across chunk boundaries, and structure-aware splitting keeps a procedure together, so a retrieved chunk contains the complete step. Tiny chunks lose more context, fewer chunks make the gap worse, and a higher temperature invents steps instead of retrieving them.
</details>

---

### Question 27
**Scenario:** A support assistant stores product document vectors in Oracle Autonomous Database. Results must be the most similar chunks, but only for products sold in the user's region.

A. Retrieve the top 100 chunks by similarity and ask the model to ignore other regions
B. Keep a separate vector database per region and synchronize it nightly from the main one
C. Use AI Vector Search to combine similarity with a region filter in one SQL query
D. Add the user's region to the prompt so the embedding model weights region chunks higher

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Because vectors sit beside relational data in Autonomous Database, AI Vector Search can combine vector similarity with ordinary predicates and joins in a single SQL statement. Asking the model to ignore content still sends it, separate stores add a second system to keep in sync, and the prompt does not affect how stored vectors are ranked.
</details>

---

### Question 28
**Scenario:** In a LangChain RAG application, which component takes the user's question and returns the relevant documents from the vector store?

A. The memory, which stores past turns and selects documents based on the conversation history
B. The prompt template, which formats variables and selects documents to include in the prompt
C. The output parser, which reads the model's answer and attaches the matching documents
D. The retriever, which runs the search against the vector store and returns the documents

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A retriever is LangChain's interface for fetching relevant documents for a query, usually backed by a vector store. Memory holds conversation history, prompt templates format inputs, and output parsers structure the model's response. None of them perform the search.
</details>

---

### Question 29
**Scenario:** Vector search returns the right documents somewhere in the top 20, but the three chunks sent to the model are often not the best ones.

A. Increase the number of chunks sent to the model from 3 to 20 so the right one is always included
B. Retrieve 20 candidates, rerank them with a reranking model, and send the top 3 to the model
C. Switch to a different embedding model for the queries while keeping the stored document vectors
D. Lower the temperature of the generation model so it focuses on the most relevant chunk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A reranker scores each query-chunk pair more precisely than vector similarity, so retrieving broadly and reranking puts the best chunks in the small set the model reads. Sending 20 chunks adds noise and cost, mixing embedding models makes vectors incomparable, and temperature does not choose chunks.
</details>

---

### Question 30
**Scenario:** Users of an internal assistant complain that they stare at a blank screen for 15 seconds while long answers are generated, even though answer quality is good.

A. Stream the response so tokens appear as they are generated
B. Move to a larger model, since larger models always generate text faster
C. Increase the maximum output tokens so that each answer finishes in a single pass
D. Cache every answer and return stored text instead of generating new responses

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Streaming returns tokens as they are produced, so users see the answer begin almost at once even though total generation time is unchanged. Larger models are usually slower, a higher token limit does not speed anything up, and caching only helps for identical repeated questions.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. The pass mark is 68%.
- **20-25 correct (65-84%):** Review the customization decision table and the diagnosis order for RAG failures.
- **Below 20:** Work the [scenarios](../oracle/oci-generative-ai-professional/scenarios.md) and build the [RAG pipeline project](../../build/projects/build-rag-pipeline.md) in this repo.
