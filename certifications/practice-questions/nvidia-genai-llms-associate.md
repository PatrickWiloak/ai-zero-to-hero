---
last-updated: 2026-10-22
difficulty: intermediate
---

# NVIDIA Certified Associate - Generative AI and LLMs (NCA-GENL) - Practice Questions

30 questions for NCA-GENL prep, weighted toward LLM fundamentals (25%), prompt engineering (20%), and RAG and vector databases (20%).

> **Cert page:** [exams/nvidia/genai-llms-associate/](../nvidia/genai-llms-associate/README.md)

---

### Question 1
**Scenario:** What does the self-attention mechanism in a transformer compute?

A. The order of words in a sentence, using fixed sine and cosine position signals added to each embedding
B. The model's loss, by comparing each predicted token distribution with the ground truth at the end of every step
C. A weighted relationship between every token and every other token in the sequence, scored by learned query-key similarity
D. The tokenizer vocabulary, by counting how often each subword appears across the training corpus and ranking them

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attention lets each position attend to all others, weighting them by learned query-key similarity, which is what captures long-range dependencies. Order comes from positional encoding, not attention itself, because attention alone is permutation-invariant.
</details>

---

### Question 2
**Scenario:** A model has a 128k token context window. What does that limit?

A. The combined tokens of the input plus the generated output for a single request
B. The number of parameters in the model, which sets its memory footprint and is fixed once training finishes
C. The training data size, meaning the number of documents the model saw before its weights were frozen
D. The vocabulary size of the tokenizer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The context window is the working memory for one request and covers prompt and completion together, which is why a long prompt reduces the room left for output. It is unrelated to parameter count, which is model capacity, and to the training corpus.
</details>

---

### Question 3
**Scenario:** Which customization approach best teaches a model a specific output style and format with a few hundred examples?

A. RAG, which retrieves reference documents from a vector store and adds them to the prompt at inference time
B. Pretraining from scratch on a new corpus of several trillion tokens, which would reset every learned weight
C. Parameter-efficient fine-tuning such as LoRA
D. Raising temperature, which makes sampling more random but does not teach the model any new behavior

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** LoRA trains small low-rank adapter matrices while freezing the base weights, so it needs far less data, memory, and time than full fine-tuning, and adapters can be swapped per task. RAG injects knowledge rather than behavior, and pretraining needs orders of magnitude more data.
</details>

---

### Question 4
**Scenario:** A chatbot invents a policy that does not exist in the company handbook.

A. The context window is too large, so the model fills the unused space
B. The temperature is too low, which makes the model overconfident and forces it to make up missing facts
C. The model is broken, so its weights are corrupted and it must be retrained from the last good checkpoint
D. Hallucination: ground answers with retrieval, require citations, and measure groundedness

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Language models generate plausible continuations and have no built-in notion of truth, so ungrounded factual questions are the highest-risk case. Retrieval plus a requirement to cite the retrieved passage is the standard mitigation, and a groundedness metric turns it into something you can measure.
</details>

---

### Question 5
**Scenario:** In a RAG pipeline, what does the embedding model do?

A. Ranks the final output by scoring each candidate answer against a set of human-written reference responses
B. Converts text into vectors so that semantically similar passages sit close together in vector space and can be found by nearest-neighbor search
C. Generates the answer by reading the retrieved passages and writing a natural-language reply to the user
D. Stores the documents and their metadata so they can be filtered and returned when a query arrives

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embeddings turn meaning into geometry, which is what makes nearest-neighbor search return relevant passages for a paraphrased query. The vector database stores and indexes those vectors, and the generative model writes the answer from what retrieval returned.
</details>

---

### Question 6
**Scenario:** Which index type in a vector database trades a small amount of recall for much faster search?

A. Hash index, which maps each vector to a bucket by exact value and so only finds identical vectors
B. Exact k-nearest-neighbor (flat), which compares the query to every stored vector and so is exact but not faster
C. B-tree, which keeps sorted keys for range scans and gives logarithmic lookups on high-dimensional embeddings
D. Approximate nearest neighbor such as HNSW or IVF

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** ANN indexes such as HNSW build a navigable graph that finds close-enough neighbors in sublinear time. Flat search is exact but scales linearly with corpus size. B-trees and hash indexes serve exact-match and range queries, not similarity in high-dimensional space.
</details>

---

### Question 7
**Scenario:** Prompt output quality improves noticeably when the model is asked to "think step by step."

A. Few-shot prompting, which supplies worked input and output examples inside the prompt
B. Chain-of-thought prompting, which elicits intermediate reasoning steps
C. Quantization, which lowers weight precision to save memory
D. Retrieval augmentation, which fetches relevant documents and adds them to the prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chain of thought elicits intermediate reasoning, which helps most on multi-step arithmetic and logic. Few-shot provides examples, which is a different lever aimed mainly at format and edge cases. The two combine well.
</details>

---

### Question 8
**Scenario:** Which NVIDIA offering packages an optimized model as a container with a standard inference API?

A. NVIDIA DCGM, which exports GPU health and utilization metrics from the data center for monitoring
B. RAPIDS, a suite of GPU-accelerated libraries for data science
C. NVIDIA NIM microservices, containers bundling an optimized model with a standard API
D. Nsight Systems, a profiler that traces CPU and GPU activity

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NIM microservices bundle the model, the optimized runtime (typically TensorRT-LLM), and an OpenAI-compatible API into a deployable container. DCGM is GPU monitoring, RAPIDS is GPU data science, and Nsight is a profiler.
</details>

---

### Question 9
**Scenario:** A model must run on a smaller GPU with acceptable quality loss.

A. Quantize the weights to a lower precision such as INT8 or FP8, trading a small accuracy loss for much less memory
B. Add more layers, which deepens the network and increases its representational capacity per token
C. Increase the batch size, which processes more requests per step and raises peak memory use
D. Increase the context window, which lets the model read longer prompts at the cost of more GPU memory

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Quantization reduces the bits per weight, cutting memory footprint and often increasing throughput, at some accuracy cost that varies by method and model. Post-training quantization is the quick path; quantization-aware training recovers more quality when the drop matters.
</details>

---

### Question 10
**Scenario:** What is tokenization?

A. Removing stop words and punctuation from the text so that only the meaningful terms reach the model
B. Splitting text into subword units the model processes, each mapped to an integer ID
C. Encrypting the prompt before it is sent so that the hosting provider cannot read the request
D. Assigning API keys to each client so that the service can meter the requests that user makes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models operate on token IDs, not characters or words. Subword tokenization means an unusual word may cost several tokens, and non-English text often costs more tokens per character, which has direct pricing and context-budget consequences.
</details>

---

### Question 11
**Scenario:** Which NVIDIA framework provides programmable guardrails for conversational AI applications?

A. cuDF, a GPU dataframe library that speeds up pandas-style data preparation
B. Triton Inference Server, which serves models from many frameworks at scale with batching
C. Omniverse, a platform for 3D simulation and digital twins built on OpenUSD
D. NeMo Guardrails, a toolkit for adding programmable rails to LLM apps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NeMo Guardrails defines topical, safety, and security rails in a configuration language, sitting between the user and the model. Triton serves models, cuDF is GPU dataframes, and Omniverse is the simulation and 3D platform.
</details>

---

### Question 12
**Scenario:** A responsible AI review flags that the training data may under-represent a demographic group.

A. Ignore it if overall accuracy is high, since a strong aggregate score shows the model is fair to every group
B. Add a disclaimer to the product page only and ship the model unchanged
C. Evaluate performance per subgroup, document the limitation, and mitigate before deployment
D. Increase model size, because a larger network always learns every group well

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Aggregate accuracy hides subgroup failure, so disaggregated evaluation is the control. Documentation (model cards) and mitigation are both expected, and a disclaimer alone shifts the burden to users without reducing the harm.
</details>

---

### Question 13
**Scenario:** Which describes RLHF?

A. Reinforcement learning from human feedback, using a reward model trained on human preferences
B. A vector index that organizes embeddings into a graph so that approximate nearest-neighbor queries run quickly
C. A quantization scheme that stores each weight in fewer bits
D. Retrieval from a large corpus of documents, which supplies grounding passages

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RLHF is the alignment stage that shapes helpfulness and harmlessness after pretraining and supervised fine-tuning. Direct preference optimization is a more recent alternative that skips the separate reward model.
</details>

---

### Question 14
**Scenario:** Two chunking strategies are compared for a RAG system over legal contracts.

A. Always use one sentence per chunk, because the smallest unit gives the most precise embeddings for every contract clause
B. Boundaries matter: too small loses context, too large dilutes relevance, and overlap avoids splitting a fact
C. Always use one chunk per document, so each passage carries the whole contract
D. Chunk size is irrelevant, because the embedding model normalizes any length of text

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chunking is the single highest-leverage knob in most RAG systems. Structure-aware splitting on sections or clauses usually beats fixed character counts for documents with real structure, and a modest overlap protects against boundary loss.
</details>

---

### Question 15
**Scenario:** How should an LLM feature be evaluated before release?

A. A held-out evaluation set with task metrics plus safety tests, run automatically on every model or prompt change
B. Latency benchmarks only, since response time is the one property that cannot be checked after the release
C. Manual review of a handful of prompts chosen by the developer who wrote the feature, done once on their own laptop before the release
D. User feedback after launch, collected through thumbs-up buttons and support tickets once real traffic arrives at scale

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Evals are the regression suite for a nondeterministic system, and they only earn their keep if they run on every change: prompt edits and model upgrades both change behavior. Post-launch feedback is a lagging signal that arrives after users are affected.
</details>

---

### Question 16
**Scenario:** A team needs a model to classify support tickets and tag product names in them. It does not need to generate any free text.

A. A decoder-only model, because only GPT-style models can label tokens within a sequence
B. An encoder-only model such as BERT, which reads the whole input in both directions
C. A diffusion model, because classification works by denoising the input into a label
D. An encoder-decoder model, because every classification task needs a separate decoder

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Encoder-only models attend to the full input bidirectionally, which makes them a strong, efficient fit for understanding tasks such as classification and named entity recognition. Decoder-only models can do these tasks but are built for generation and usually cost more. Diffusion models generate images and other media, and an encoder-decoder adds a generator the task does not need.

**Key Concept:** [NeMo Framework overview](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)
</details>

---

### Question 17
**Scenario:** During training, a decoder-only model applies a mask inside its self-attention layers.

A. The mask hides padding tokens only, so that each batch can hold sequences of different lengths
B. The mask hides a random 15% of tokens, which the model must then predict from the surrounding context
C. The mask removes attention heads at random during training, which acts as a form of regularization
D. The causal mask stops each position from attending to later tokens, so that it predicts the next token

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A causal mask lets each position attend only to itself and earlier positions, so training on next-token prediction cannot peek at the answer, and the same model generates text left to right. Padding masks exist too but are not what makes a decoder causal. Masking 15% of tokens is BERT's masked language modeling, and dropping heads describes a dropout-style technique.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 18
**Scenario:** A lab has a fixed compute budget for pretraining and must choose between a larger model on fewer tokens and a smaller model on more tokens.

A. Always choose the largest model that fits in memory, since parameter count alone decides quality
B. Spend the budget on extra epochs over a small dataset, since repeating data is as good as new data
C. Follow compute-optimal scaling results, which favor scaling parameters and training tokens together
D. Choose the smallest model, since smaller models always reach a lower loss for the same compute

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Compute-optimal scaling research (the Chinchilla results) showed many large models were undertrained, and that for a fixed budget, parameters and training tokens should grow together. Parameter count alone does not decide quality. Repeating a small dataset gives diminishing returns, and the smallest model is not always best either.

**Key Concept:** [NeMo Framework overview](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)
</details>

---

### Question 19
**Scenario:** A model has a large total parameter count, but each token is processed by only a few of its feed-forward sub-networks, chosen by a learned router.

A. A mixture-of-experts model, which activates a subset of experts for each token
B. A distilled model, which copies the outputs of a larger teacher at each layer
C. A quantized model, which stores each weight in four bits to save GPU memory
D. A pruned model, which has had most of its weights permanently set to zero

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In a mixture-of-experts (MoE) layer, a router sends each token to a few experts, so compute per token tracks the active parameters while total capacity is much larger. All experts still need to be held in memory. Distillation, quantization and pruning are compression techniques with no per-token routing.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 20
**Scenario:** An application extracts invoice fields into JSON, and the same input must give the same output on every call as far as possible.

A. Use a high temperature with top-p near 1.0, which keeps the model focused on the likeliest tokens
B. Use a temperature of zero or close to it, so the model picks the most likely token at each step
C. Raise the maximum output length, which makes the model's answer the same on every call
D. Add more few-shot examples, since examples remove all randomness from the model's sampling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Temperature scales how sharply the model's choices favor the most likely token; near zero, decoding is close to greedy and outputs become highly repeatable, which suits extraction. High temperature with wide top-p increases variety. Output length limits only truncate, and examples improve format but do not control sampling randomness.

**Key Concept:** [NIM for LLMs API reference](https://docs.nvidia.com/nim/large-language-models/latest/reference/api-reference.html)
</details>

---

### Question 21
**Scenario:** A model keeps returning product summaries in inconsistent layouts, even though the instructions describe the desired format in detail.

A. Raise the temperature so that the model explores more layouts and finds the right one by itself
B. Fine-tune a new base model from scratch on product summaries before trying any other change
C. Remove the instructions and let the model choose a layout, since detailed instructions confuse it
D. Add two or three examples of input and correctly formatted output to the prompt (few-shot)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Few-shot examples show the model the exact output pattern, which is often more reliable than describing a format in words, and it costs only prompt tokens. Higher temperature increases variation. Training from scratch is far out of proportion to a formatting problem, and removing instructions makes consistency worse.

**Key Concept:** [NIM for LLMs API reference](https://docs.nvidia.com/nim/large-language-models/latest/reference/api-reference.html)
</details>

---

### Question 22
**Scenario:** A RAG assistant summarizes web pages. One page contains hidden text telling the model to reveal its system prompt, and the model obeys.

A. Direct prompt injection, so the fix is to block users from typing the word "instructions"
B. A hallucination, so the fix is to lower the temperature for every request that uses web pages
C. Indirect prompt injection: treat retrieved text as data and add input and output guardrails
D. Model drift, so the fix is to fine-tune the model again on a newer set of web pages

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Instructions hidden in content the system retrieves, rather than typed by the user, are indirect prompt injection. Mitigations include clearly delimiting retrieved content as untrusted data, limiting what the model can do, and rails such as NeMo Guardrails on inputs and outputs. Keyword blocking misses it because the user typed nothing malicious, it is not a hallucination, and retraining does not address untrusted input.

**Key Concept:** [NeMo Guardrails library overview](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)
</details>

---

### Question 23
**Scenario:** A RAG system's vector search returns 50 candidate chunks, and the best one is often ranked twentieth. Only the top 5 fit in the prompt.

A. Add a reranking model that scores each query and chunk pair together and reorders the candidates
B. Increase the embedding dimension of the index so that vector search ranks the chunks correctly
C. Put all 50 chunks in the prompt and let the model find the right one inside the long context
D. Reduce the chunk size to one sentence, so that more chunks fit in the prompt at the same time

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Retrieval with embeddings is fast but approximate; a reranker (a cross-encoder) reads the query and each candidate together and orders them by relevance, so the best chunks reach the top 5. NeMo Retriever offers reranking NIMs for this. A bigger embedding dimension needs re-embedding and does not guarantee better order. Stuffing 50 chunks raises cost and dilutes attention, and tiny chunks lose context.

**Key Concept:** [NeMo Retriever reranking NIM](https://docs.nvidia.com/nim/nemo-retriever/reranking/latest/index.html)
</details>

---

### Question 24
**Scenario:** A vector database is configured to use cosine similarity between query and document embeddings.

A. It counts how many words the query and the document have in common
B. It measures the angle between two vectors, ignoring their length
C. It measures the straight-line distance between the two vectors' tips
D. It compares the two texts character by character after tokenization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cosine similarity is the cosine of the angle between two vectors, so it compares direction, which encodes meaning, and ignores magnitude. For normalized vectors it ranks the same as dot product. Word overlap is a lexical measure such as BM25, straight-line distance is Euclidean, and character comparison is not semantic at all.

**Key Concept:** [NeMo Retriever embedding NIM](https://docs.nvidia.com/nim/nemo-retriever/embedding/latest/index.html)
</details>

---

### Question 25
**Scenario:** Users say a RAG chatbot gives wrong answers. The team must find out whether retrieval or generation is at fault.

A. Measure only the final answer accuracy, since retrieval quality cannot be measured on its own
B. Replace the language model with a larger one, since wrong answers are always a generation problem
C. Ask users to rate each answer, since automatic metrics cannot assess any part of a RAG pipeline
D. Evaluate the stages separately: retrieval recall for the right chunks, then answer faithfulness

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** RAG failures come from two places: the right content was never retrieved, or it was retrieved and the model misused it. Measuring retrieval (for example, recall at k against labeled relevant chunks) separately from generation (faithfulness and answer relevance) shows which to fix. End-to-end accuracy alone hides the cause, a larger model cannot use content that was never retrieved, and user ratings are slow and coarse.

**Key Concept:** [NVIDIA NeMo Retriever](https://docs.nvidia.com/nemo/retriever/index.html)
</details>

---

### Question 26
**Scenario:** A developer must fine-tune a 70B model on a single GPU with limited memory and still get quality close to full fine-tuning.

A. QLoRA, which keeps the frozen base model in 4-bit precision and trains small LoRA adapters
B. Full fine-tuning in FP32, which updates every weight and gives the highest possible quality
C. Prompt engineering only, since a model of this size cannot be fine-tuned on a single GPU
D. Training a new 70B model from scratch, which needs less memory than fine-tuning an old one

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** QLoRA quantizes the frozen base weights to 4-bit and trains low-rank adapters in higher precision, cutting memory enough to fine-tune very large models on one GPU with quality close to full fine-tuning. Full FP32 fine-tuning needs many times the model's size in memory for gradients and optimizer states. Single-GPU fine-tuning is feasible this way, and pretraining from scratch costs far more.

**Key Concept:** [NeMo AutoModel documentation](https://docs.nvidia.com/nemo/automodel/latest)
</details>

---

### Question 27
**Scenario:** After full fine-tuning on legal documents, a model drafts contracts well but has become noticeably worse at general reasoning and everyday questions.

A. Overfitting to the validation set, fixed by removing the validation set from the run
B. Catastrophic forgetting, reduced by PEFT methods or by mixing general data into training
C. Hallucination, fixed by grounding every answer in retrieved legal documents
D. Underfitting, fixed by training the same data for many more epochs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Updating all weights on a narrow domain can overwrite general abilities, which is catastrophic forgetting. Parameter-efficient methods such as LoRA keep the base weights frozen, and mixing general data into the fine-tuning set preserves broad skills. Removing validation data hides problems, RAG addresses facts rather than lost skills, and more epochs on legal text worsens the forgetting.

**Key Concept:** [NeMo AutoModel documentation](https://docs.nvidia.com/nemo/automodel/latest)
</details>

---

### Question 28
**Scenario:** During text generation, an inference engine stores the attention keys and values of previous tokens instead of recomputing them for each new token.

A. The model's weights, which are reloaded from the cache at the start of each generation step
B. The tokenizer's vocabulary, which is cached to speed up converting text into token IDs
C. The KV cache, which saves recomputation but grows with sequence length and batch size
D. The prompt cache in the browser, which stores previous answers to return them faster

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The KV cache keeps the key and value tensors for tokens already processed, so each new token needs attention computed only for itself. It trades memory for speed, and because it grows with context length and batch size it is often the main memory limit in serving. Weights and the vocabulary are not what this cache stores, and a browser cache is unrelated.

**Key Concept:** [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/)
</details>

---

### Question 29
**Scenario:** A team wants the highest LLM inference throughput on NVIDIA GPUs using optimized kernels, in-flight batching and FP8 or INT4 quantization.

A. RAPIDS cuDF, which accelerates DataFrame operations on GPUs
B. NeMo Curator, which filters and deduplicates training datasets
C. DCGM, which monitors GPU health and performance metrics
D. TensorRT-LLM, an open-source library for optimized LLM inference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** TensorRT-LLM provides optimized attention kernels, paged KV cache, in-flight batching, quantization and multi-GPU parallelism for LLM inference on NVIDIA GPUs, and serving stacks such as Triton and Dynamo can run it as a backend. cuDF is for DataFrames, NeMo Curator prepares data, and DCGM monitors GPUs.

**Key Concept:** [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/)
</details>

---

### Question 30
**Scenario:** A customer-service LLM application logs every prompt and response for quality review, and some prompts contain customers' card numbers and addresses.

A. Detect and redact personal data before logging, and limit who can read the logs and for how long
B. Stop logging altogether, since any record of prompts is unlawful for a customer service tool
C. Keep the logs as they are, since data typed into a chatbot is not considered personal data
D. Encrypt the logs once a year, which is enough to make storing raw card numbers acceptable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Responsible handling means minimizing personal data: detect and redact PII before it is stored, restrict access, and set retention limits, which keeps quality review possible. Logging is lawful when it is controlled. Chat input can certainly be personal data, and occasional encryption does not make storing raw card numbers acceptable.

**Key Concept:** [NeMo Guardrails library overview](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)
</details>

---

## Where to go deeper

- [NCA-GENL cert page](../nvidia/genai-llms-associate/README.md) - notes, practice plan, strategy
- [NCP-GENL practice questions](nvidia-genai-llms-professional.md) - the professional level above this
- [LLM basics](../../learn/concepts/llm-basics.md) - plain-English foundation
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in depth
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
