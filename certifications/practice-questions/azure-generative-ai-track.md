---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Generative AI (Self-Directed Track) - Practice Questions

15 questions for the Azure Generative AI study track, weighted toward Azure OpenAI fundamentals (25-30%), prompt engineering (20-25%), and AI Foundry deployment (20-25%), with responsible AI and production integration.

This is a self-directed track rather than a Microsoft exam, so these questions target working knowledge rather than a published objective list.

> **Cert page:** [exams/azure/genai/](../azure/genai/README.md)

---

### Question 1
**Scenario:** A deployment must guarantee throughput for a latency-sensitive production application.

A. Batch deployment, which processes requests asynchronously at a lower price within a 24-hour target
B. Provisioned throughput units (PTU), which reserve capacity
C. Standard (pay-as-you-go) deployment, which scales on demand but shares capacity and can return 429 errors
D. A larger model, which improves answer quality but does not reserve any capacity for the deployment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PTU reserves capacity so throughput and latency are predictable rather than shared. Standard deployments are cheaper and elastic but subject to variable latency and 429 responses under load. Batch is the opposite trade: much cheaper, with results delivered asynchronously.
</details>

---

### Question 2
**Scenario:** An application must answer questions from a company's internal documents.

A. Retrieval-augmented generation: index the documents and pass relevant chunks as context
B. Put every document in the system prompt, so the model can read the company's whole content on each request
C. Train a model from scratch on the company's documents, which gives full control over what it knows
D. Fine-tune the model on the documents so that it memorizes the facts and needs no retrieval step

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RAG is the default for factual grounding because content updates without retraining, sources can be cited, and access control can be enforced at retrieval time. Fine-tuning teaches style and format far better than it teaches facts. Stuffing everything into the prompt hits context limits and costs.
</details>

---

### Question 3
**Scenario:** Retrieval quality is poor: relevant passages exist but are not returned.

A. Lower the top-k, so fewer passages are returned and the most relevant ones are easier to find in the list
B. Increase the model's temperature, which makes the model explore more of the index and surface other passages
C. Improve chunking and use hybrid search (keyword plus vector) with semantic reranking
D. Use a larger model, which can find passages in the index given capacity

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Retrieval failures are retrieval problems, not generation problems. Chunk boundaries that split a fact across two chunks, pure vector search missing exact identifiers, and no reranking are the three usual causes. Changing the model cannot recover context it was never given.
</details>

---

### Question 4
**Scenario:** Which parameter makes output more deterministic?

A. Lowering temperature toward 0, which makes sampling close to greedy decoding
B. Raising top_p to 1, which lets the sampler consider every token in the vocabulary at each step
C. Increasing max_tokens, which gives the model more room to settle
D. Raising temperature, which sharpens the probability distribution so the most likely token wins more often

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Temperature scales the randomness of token sampling, so near zero is close to greedy decoding. Note that even at temperature 0 output is not strictly guaranteed identical across runs. Adjust temperature or top_p, not both at once, or the interaction becomes hard to reason about.
</details>

---

### Question 5
**Scenario:** An app must return JSON that always matches a defined schema.

A. Lower temperature only, since near-zero sampling makes the model emit the same schema every time
B. Use structured outputs or JSON mode with a schema, and validate the result
C. Ask nicely in the prompt, naming the required keys
D. Parse with a regular expression, extracting the fields from whatever text the model returns

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Constrained decoding against a schema removes the class of failures where the model emits prose around the JSON or drops a field. Validation after the fact is still worth keeping, because a schema-valid response can still be semantically wrong.
</details>

---

### Question 6
**Scenario:** Content filtering must be adjusted for a medical application where clinical terms trigger false positives.

A. Switch cloud providers, since another vendor's default filters will not flag clinical terms
B. Disable all filtering for the deployment on your own, so that no clinical term is blocked in a prompt or a completion, whatever the category
C. Configure severity thresholds per category, and apply for modified filters where the use case justifies it
D. Rewrite the prompts to avoid clinical terms, replacing them with lay words

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure OpenAI content filters have per-category severity thresholds for hate, sexual, violence, and self-harm, applied to both prompt and completion. Legitimate use cases can request modified configurations through Microsoft's approval process. Avoiding clinical vocabulary would break the application's purpose.
</details>

---

### Question 7
**Scenario:** A retrieval system must not return documents the asking user cannot see.

A. Rely on the model to decline when a document looks confidential
B. Add a system prompt instruction that tells the model never to reveal documents the user cannot access under any circumstance
C. Lower top-k so that fewer documents are returned
D. Filter results by the user's identity and group membership at query time, using security trimming on the index

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Authorization must be enforced in the retrieval layer, in code, before content reaches the context window. A system prompt instruction is a suggestion an injected instruction can compete with, and the model has no reliable way to know who is asking.
</details>

---

### Question 8
**Scenario:** Costs are dominated by a long, unchanging system prompt repeated on every request.

A. Use a smaller model only, accepting lower answer quality
B. Move the system prompt into the user message of each request, which changes where the tokens sit but not how many are billed
C. Batch the requests, which lowers the price but delays every response
D. Use prompt caching so the repeated prefix is billed and processed at a reduced rate

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Caching a stable prefix is the direct fix and requires the shared content to be at the start of the prompt, which is a real design constraint worth planning for. Batch processing helps for offline workloads but not for interactive latency.
</details>

---

### Question 9
**Scenario:** Which technique gives the model examples of the desired input and output format inside the prompt?

A. Chain of thought, which asks the model to write out its reasoning steps before the final answer
B. Fine-tuning, which trains the model's weights on example pairs outside the prompt
C. Few-shot prompting, which includes example inputs and outputs in the prompt
D. Zero-shot prompting, which gives the instruction alone with no examples in the prompt

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Few-shot means including exemplars in the prompt, which is the cheapest way to pin down format and edge-case handling. Chain of thought asks the model to reason step by step, which is about the process rather than the format. Fine-tuning moves examples into the weights.
</details>

---

### Question 10
**Scenario:** An agent has a tool that can delete records. What is the minimum responsible design?

A. Narrow credential scope, an authorization check against the calling user in code, confirmation for destructive actions, and logging of every call
B. Add a warning in the system prompt telling the model never to delete a record unless the user has clearly asked
C. Trust the model's judgment, since a capable model will not call a delete tool unless the task requires it
D. Use a smaller model, which is less likely to follow injected instructions that ask it to delete records

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The tool boundary is the last non-model control that can refuse, so it must carry the authorization check rather than delegating it to the prompt. Treat the model as an untrusted caller: assume an injected instruction will eventually reach it and design so that the worst outcome is bounded.
</details>

---

### Question 11
**Scenario:** A model deployment must be evaluated before and after a version upgrade.

A. Manual spot checks of a few favorite prompts by the developer, repeated after the upgrade goes live in production
B. An evaluation set with defined metrics (groundedness, relevance, fluency, task accuracy) run against the old and new versions
C. User complaints collected through the support queue, reviewed weekly after the new version is released to everyone
D. Latency measurement only, since a model with the same response time must behave the same as it did before the upgrade

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model upgrade is a behavior change, and without a regression suite you find out from users. Azure AI Foundry evaluation supports both AI-assisted and code-based metrics, and safety evaluations belong in the same suite as quality ones.
</details>

---

### Question 12
**Scenario:** Which Azure service provides the managed development surface for building, evaluating, and deploying generative AI applications?

A. Azure Machine Learning only, which trains and deploys classical models but is not the generative AI hub
B. Azure Data Factory, which orchestrates data movement and transformation pipelines between data stores
C. Azure AI Foundry, with model catalog, prompt flow, evaluation, and deployment
D. Azure Functions, which runs event-triggered code without servers and is not a development surface for models

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AI Foundry is the generative AI development hub, including the model catalog across Azure OpenAI and open models, prompt flow for orchestration, evaluations, content safety, and tracing. Azure Machine Learning remains the broader ML platform underneath.
</details>

---

### Question 13
**Scenario:** An embedding model is swapped for a newer one in a live RAG system.

A. Increase the index size, so the stored vectors from the old model have more room to match new queries
B. Only new documents need re-embedding, because older vectors remain valid
C. Nothing else is needed, since vectors from any embedding model share one common similarity space and compare directly
D. The entire index must be re-embedded, because vectors from different models are not comparable

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Embedding spaces are model-specific, so mixing vectors from two models produces meaningless similarity scores. Plan the reindex, and keep the old index serving until the new one is validated, which is the usual blue-green pattern applied to retrieval.
</details>

---

### Question 14
**Scenario:** Which Microsoft framework should guide the responsible AI review of a new generative feature?

A. ISO 27001 alone, since an information security management certification covers the harms of a generative feature
B. The Microsoft Responsible AI Standard and its principles: fairness, reliability, privacy, inclusiveness, transparency, and accountability
C. The Azure Well-Architected Framework alone, since its pillars of reliability and security cover the harms of AI features
D. The Cloud Adoption Framework alone, since its govern methodology already includes impact assessments for each use case

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Responsible AI Standard names the six principles and requires an impact assessment for the use case. The Well-Architected and Cloud Adoption frameworks are complementary but cover architecture and adoption rather than AI-specific harms, and ISO 27001 is information security management.
</details>

---

### Question 15
**Scenario:** Production monitoring must catch quality degradation over time.

A. Log prompts, completions, latency, token usage, and evaluation scores on sampled traffic, with alerts on score drift
B. Wait for support tickets and escalations to show that answers have worsened
C. Monitor CPU only, because compute saturation is the first sign of any regression
D. Re-run the launch evaluation once a year, comparing the scores with the numbers from the original release and the previous review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Generative systems degrade silently as inputs, content, and model versions shift, and infrastructure metrics show nothing. Sampled online evaluation with the same metrics used pre-launch is what turns a quality regression into an alert instead of a complaint.
</details>

---

## Where to go deeper

- [Azure GenAI track page](../azure/genai/README.md) - notes, practice plan, strategy
- [AI-103 practice questions](azure-ai-apps-agents-developer-ai-103.md) - the certification nearest this track (AI-102, retired: [questions](azure-ai-engineer-ai-102.md))
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - the security side of question 10
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in plain English
- **[📖 Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** - primary source
