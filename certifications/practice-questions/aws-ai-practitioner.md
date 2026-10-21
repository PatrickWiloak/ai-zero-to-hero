# AWS Certified AI Practitioner (AIF-C01) - Practice Questions

15 scenario-based questions for AIF-C01 prep.

> **Cert page:** [exams/aws/foundational/ai-practitioner-aif-c01/](../aws/foundational/ai-practitioner-aif-c01/README.md)

---

### Question 1
**Scenario:** A company wants to add a chatbot trained on their internal product docs. They want to avoid model fine-tuning. What pattern?

A. Retrieval Augmented Generation (RAG): retrieve relevant docs at query time and inject them into the prompt
B. Continual pre-training on the internal docs, which updates the model weights with a new training run
C. Quantization, which compresses the model weights to lower precision so it runs on smaller hardware
D. Train a custom LLM from scratch on the internal docs plus a large public text corpus

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RAG retrieves company-specific context at query time without modifying the model. Cheaper, faster, no training data labeling, easier to update (just update the doc store). Fine-tuning is for stylistic adaptation, not knowledge updates.
</details>

---

### Question 2
**Scenario:** What is "hallucination" in the context of LLMs?

A. The model crashes or times out partway through generating a response and returns an error code
B. The model refuses to answer because a safety filter has blocked the prompt or the completion
C. The model generates plausible-sounding but factually wrong content
D. A specific technique that adds random noise to the training data so the model generalizes better

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hallucination = confident but factually incorrect output. Mitigated via grounding (RAG with citations), guardrails, output validation, and clear "I don't know" instructions in the system prompt.
</details>

---

### Question 3
**Scenario:** Which Amazon service hosts foundation models from multiple providers (Anthropic, Meta, Cohere, Stability) behind a unified API?

A. AWS Lambda, which runs event-driven code without servers but does not host foundation models
B. Amazon Bedrock, a managed API for foundation models from multiple providers
C. Amazon Rekognition, which analyzes images and video
D. Amazon SageMaker, a platform for building and training models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bedrock is the managed foundation-model API. Models include Claude (Anthropic), Llama (Meta), Mistral, Cohere, Stability, plus Amazon's own Titan family. Pay per token. Bedrock Knowledge Bases adds RAG; Bedrock Agents adds tool-use.
</details>

---

### Question 4
**Scenario:** A bank wants to use AI for credit decisions. What responsible-AI consideration is paramount?

A. Bias and fairness across protected demographics, plus explainability for regulatory compliance
B. Speed of inference, because lending decisions must return to the applicant within a few milliseconds
C. Model size, because a larger model is required to meet credit fairness rules
D. Cost, because the cheapest model that meets accuracy targets satisfies the regulators' requirements

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** High-stakes decisions (lending, hiring, medical) require fairness audits across protected demographics + interpretability for regulations like ECOA, FCRA, GDPR Article 22. Tools: SageMaker Clarify, Bedrock Guardrails, formal model cards.
</details>

---

### Question 5
**Scenario:** Which AWS service is best for analyzing sentiment in customer reviews at scale (no model training needed)?

A. Amazon Polly, which turns written text into lifelike speech
B. Amazon Rekognition, which analyzes images and video for objects, faces, and unsafe content
C. Amazon Textract, which extracts printed text and forms from scanned documents
D. Amazon Comprehend (pre-trained NLP, including sentiment analysis)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Comprehend is pre-built NLP: sentiment, entity recognition, key phrases, language detection, PII redaction. No training needed. Bedrock could also be prompted for sentiment, but Comprehend is simpler and cheaper for the standard use case, while Textract only extracts text from scans.
</details>

---

### Question 6
**Scenario:** Prompt engineering best practices include:

A. Clear instructions, examples (few-shot), a stated output format, and a role
B. No instructions; let the model figure out the task from the data alone, which keeps the prompt short
C. Long, complex prompts always, because adding more text and constraints improves every response
D. Random examples picked from anywhere in the data, since varied examples teach the model the most

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Effective prompts are clear, structured, with examples for non-trivial tasks (few-shot), and specify the desired output format (JSON, list, etc.). Roles ("You are a helpful tax advisor") set context.
</details>

---

### Question 7
**Scenario:** What's an "embedding"?

A. A numeric vector representing the semantic meaning of text, images, or audio (similar items have similar vectors)
B. A storage format that packs documents into compressed blocks so they load faster from object storage and are cheaper to keep
C. A binary file produced after training that contains the model weights, the tokenizer rules, and the inference settings
D. A type of model that generates images from text prompts by removing noise step by step

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Embeddings convert content into high-dimensional vectors where semantic similarity = vector closeness. Used in: similarity search, clustering, RAG retrieval, recommendation. Amazon Titan Embeddings, Cohere Embed are common providers.
</details>

---

### Question 8
**Scenario:** Which AWS service provides a serverless vector database for embeddings?

A. Amazon RDS, a managed relational database that stores rows and tables for transactional workloads
B. Amazon Athena, a serverless SQL query service that reads data directly from files in S3
C. Amazon OpenSearch Serverless (vector search) or Amazon Bedrock Knowledge Bases
D. Amazon DynamoDB, a serverless key-value store that is queried by partition key and sort key

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OpenSearch Serverless supports a vector engine for k-NN searches. Bedrock Knowledge Bases provides a managed RAG stack on top (embedding + vector store + retrieval). Aurora pgvector and Amazon MemoryDB also support vectors.
</details>

---

### Question 9
**Scenario:** A team wants to fine-tune a Bedrock foundation model on company-specific data. What's the prerequisite?

A. Bedrock doesn't support fine-tuning, so the only way to adapt a model is to build one in SageMaker
B. Custom hardware, since fine-tuning needs dedicated GPUs that the team must buy and register with AWS
C. Written permission from the model provider for each fine-tuning job
D. A high-quality labeled dataset, plus an understanding of the cost trade-off against RAG

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bedrock supports fine-tuning for some models (e.g., Titan, Llama via custom models). Requires a labeled dataset. Often RAG is faster/cheaper for knowledge updates; fine-tuning is for stylistic / task-specific behavior. Customers should compare both.
</details>

---

### Question 10
**Scenario:** What's "model bias"?

A. A type of error metric that measures the average difference between predicted and actual values
B. The model is broken because its weights were corrupted during training and it returns random output
C. The model is too slow, because its latency rises when the input comes from some user groups
D. The model produces systematically different outputs for different demographic groups because of imbalanced or mislabeled training data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bias = systematic, group-correlated error. Sources: imbalanced training data, label noise, proxy features. Mitigation: diverse training data, fairness metrics, post-hoc bias correction, regular audits.
</details>

---

### Question 11
**Scenario:** Bedrock Guardrails do what?

A. Reduce cost by routing every request to the cheapest model and capping output tokens
B. Filter prompts and responses for unsafe content (hate, violence, PII), enforce topic restrictions, and check grounding
C. Speed up inference by running a smaller copy of the model on dedicated hardware near the application, cutting round trips and cost
D. Cache responses so that repeated prompts are answered from stored output without calling the model, which lowers cost and latency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Guardrails are configurable safety policies. Block harmful categories, deny topics, redact PII, enforce allowed input/output formats. Apply at the Bedrock API level.
</details>

---

### Question 12
**Scenario:** Which is true about generative AI cost?

A. Subscription only, with a flat monthly fee per account regardless of how many requests are sent
B. Pay per user, with each named user licensed separately
C. Always free, because foundation models are open
D. Pay-per-token, with input and output tokens billed separately, often at different rates

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bedrock and most LLM APIs bill per token. Input tokens (your prompt) and output tokens (the response) often have different rates. Larger models cost more per token. Optimization: shorter prompts, prompt caching, smaller models when sufficient.
</details>

---

### Question 13
**Scenario:** A "context window" is:

A. The screen the user sees while chatting, where the conversation history and the model's replies are displayed
B. The maximum number of tokens (input + output combined) a model can process in one call
C. The number of users who can send requests at the same time
D. The time to respond, from prompt sent to last token

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Context window = max tokens per inference. Constrains how much input + output you can fit. Bigger windows enable longer documents, more conversation history, larger code files. Cost scales with tokens, not just window size.
</details>

---

### Question 14
**Scenario:** AWS Q is positioned as:

A. A search engine that indexes AWS documentation, blogs, forums, and release notes and returns ranked links to the user
B. An AI-powered assistant for AWS users (helps build apps, answer questions, draft code) - separate from Bedrock
C. A foundation model from Amazon that developers call through the Bedrock API
D. A storage service for vector data that scales to billions of embeddings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Amazon Q is a SaaS AI assistant: Q Developer (in IDE/CLI), Q Business (enterprise chat over your data), Q in QuickSight (analytics chat). Built on Bedrock under the hood but presented as an opinionated end-user product.
</details>

---

### Question 15
**Scenario:** Most cost-effective way to test if a use case benefits from GenAI:

A. Use a pre-trained foundation model via Bedrock + RAG, evaluate on a test set, then decide whether to invest in fine-tuning
B. Build a custom model from scratch, so the team can measure the full upper bound of what GenAI can do
C. Hire an AI consultancy to run a six-month pilot and produce a report on likely business benefits
D. Skip evaluation and launch to all users, then use their feedback to decide whether to keep the feature

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Standard "build vs buy vs adapt" pattern - start with the cheapest option (managed FM + RAG), evaluate on a representative test set, only invest in custom training when you have evidence the simpler approach falls short.
</details>

---

### Question 16
**Scenario:** A team wants to give Claude / Llama on Bedrock access to internal company docs without fine-tuning.

A. Re-train the model from scratch on the company docs combined with the original pre-training corpus
B. Embed docs in the prompt, pasting the full text of every document into each request
C. Bedrock Knowledge Bases, a managed RAG service with ingestion and retrieval
D. SageMaker custom training, running a fine-tuning job on the company docs and hosting the result

<details><summary>Answer</summary>

**Correct: C**

**Why:** Bedrock Knowledge Bases handles ingestion, chunking, embedding, vector storage (OpenSearch / Aurora pgvector / Pinecone), and retrieval-augmented prompting. Fully managed. B doesn't scale beyond a few KB.
</details>

---

### Question 17
**Scenario:** Risk that a model trained on biased data perpetuates that bias in predictions:

A. Drift, where the live input data changes over time and the model's accuracy slowly declines
B. Hallucination, where a generative model states plausible content that is not true
C. Bias / fairness issue, where outputs favor or disadvantage certain groups
D. Overfitting, where the model memorizes the training data and performs poorly on new data

<details><summary>Answer</summary>

**Correct: C**

**Why:** Bias in training data leads to biased predictions. Detect with fairness metrics (demographic parity, equalized odds); mitigate by rebalancing training data, using bias-mitigation algorithms, or applying SageMaker Clarify.
</details>

---

### Question 18
**Scenario:** SageMaker feature for monitoring model quality drift over time:

A. SageMaker Ground Truth, which manages human labeling workflows to build training datasets
B. SageMaker Studio, the web-based IDE for building, training, and deploying models
C. SageMaker Model Monitor, which checks deployed models for drift
D. SageMaker Pipelines, which orchestrates ML workflow steps such as processing, training, and registering

<details><summary>Answer</summary>

**Correct: C**

**Why:** Model Monitor detects: data quality drift (input distribution), model quality drift (predictions vs labels), bias drift, feature attribution drift. Pipelines orchestrates training; Studio is the IDE; Ground Truth is for labeling.
</details>

---

### Question 19
**Scenario:** Choosing between training a custom model and using a foundation model:

A. Avoid foundation models, because they send company data to other customers
B. Always train custom for accuracy, since a model trained only on your own data beats any general model
C. Always use foundation models, since training a smaller custom model never lowers the cost per request
D. Use a foundation model for general tasks; train custom for narrow, high-volume tasks where the cost math justifies it

<details><summary>Answer</summary>

**Correct: D**

**Why:** Foundation models (Claude, Llama, Titan) handle general tasks out-of-the-box. Custom training pays off only for narrow, high-volume tasks where a smaller fine-tuned model is dramatically cheaper.
</details>

---

### Question 20
**Scenario:** Hallucinations in LLM output. Mitigation:

A. Always trust LLM output, because modern foundation models are trained to reject statements they cannot verify
B. Disable the LLM for any task that involves facts, and route those requests to a human reviewer
C. RAG with citations, temperature near 0, clear system prompts, and validation of output against authoritative sources
D. Train a second LLM to verify the first one's answers, accepting whatever the two models agree on as correct

<details><summary>Answer</summary>

**Correct: C**

**Why:** Layered defense: ground the model with retrieved context (RAG), cite sources, lower temperature for factual responses, validate critical output (e.g., extracted numbers) against ground truth.
</details>

---

### Question 21
**Scenario:** A team wants to reduce inference latency on Bedrock without sacrificing quality much.

A. Use a larger model, whose extra parameters let it finish the response in fewer steps
B. Use a smaller, faster model variant (Haiku vs Sonnet vs Opus), which trades a little quality for speed and cost
C. Disable streaming, so that the full response is returned at once rather than in small chunks
D. Add more hops in the pipeline, such as an extra summarizing call before the main request

<details><summary>Answer</summary>

**Correct: B**

**Why:** Model size trades quality for speed and cost. Claude Haiku is faster and cheaper than Sonnet, which is faster and cheaper than Opus. Pick the smallest model that meets your quality bar.
</details>

---

### Question 22
**Scenario:** Token cost optimization for an app making many similar calls with a long stable system prompt:

A. Increase max_tokens, which raises the allowed response length and so lowers the price of each token
B. Send the same prompt every time, in full, and rely on the model to ignore the repeated text
C. Use a more expensive model, since better answers reduce retries
D. Bedrock prompt caching, which caches the stable prefix across calls at a reduced rate

<details><summary>Answer</summary>

**Correct: D**

**Why:** Prompt caching dramatically reduces cost for stable-prefix prompts: cached input tokens cost ~10x less than uncached. Available on Bedrock Anthropic models, OpenAI, and others.
</details>

---

### Question 23
**Scenario:** Which service is BEST for transcribing audio recordings to text at scale?

A. Amazon Transcribe, a speech-to-text service
B. Amazon Polly, which converts written text into natural-sounding speech
C. Amazon Comprehend, which finds entities, sentiment, and topics in text
D. Amazon Translate, which translates text between languages

<details><summary>Answer</summary>

**Correct: A**

**Why:** Transcribe = speech-to-text. Polly = text-to-speech. Translate = language translation. Comprehend = NLP (entities, sentiment, topics). Memorize the four "talk to AI" managed services.
</details>

---

### Question 24
**Scenario:** Bedrock with strict data residency in regulated industry (finance, healthcare):

A. Bedrock model invocation in your VPC via PrivateLink, no customer data used to train models, regional endpoints
B. Default Bedrock settings on us-east-1 only, since public endpoints already enforce every residency rule
C. Cross-region replication of prompts and outputs, which copies data to other regions for availability
D. Outbound internet from Bedrock to the model provider's own servers, which process the prompts on their infrastructure

<details><summary>Answer</summary>

**Correct: A**

**Why:** Bedrock honors regional residency, supports VPC PrivateLink for private network access, and (per terms) doesn't use customer prompts/completions to train models. This is what makes Bedrock acceptable for regulated workloads where direct OpenAI / Anthropic calls aren't.
</details>

---

### Question 25
**Scenario:** Best evaluation approach for a generative AI feature:

A. Manual review of every output by a subject expert before it is shown to the user, for each and every request
B. Build an eval set of representative inputs with expected outputs or a rubric; run it regularly and alert on regression
C. Skip evaluation, because a foundation model that scores well on public benchmarks will perform well on any task you give it
D. Trust user feedback collected from thumbs-up and thumbs-down buttons after release

<details><summary>Answer</summary>

**Correct: B**

**Why:** Eval sets are the regression test for AI. Without them, you can't know if a prompt change, model change, or data change made things better or worse. AWS offers SageMaker Clarify; many teams use LangSmith / Langfuse / Helicone / Phoenix / Braintrust.
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read responsible AI + Bedrock sections.
- **<17:** AWS Skill Builder AI Practitioner course + re-attempt.

AIF-C01 is foundational - tests **awareness** of AI/ML concepts and AWS AI services, not deep technical implementation. 65 questions, 90 minutes, 700/1000 to pass.
