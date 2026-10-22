---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA Certified Professional - Generative AI and LLMs (NCP-GENL) - Practice Questions

30 questions for NCP-GENL prep, evenly weighted across LLM architecture, training and fine-tuning at scale, inference optimization, prompt engineering and RAG, and production deployment (20% each).

> **Cert page:** [exams/nvidia/genai-llms-professional/](../nvidia/genai-llms-professional/README.md)

---

### Question 1
**Scenario:** Inference throughput is low because requests wait for the longest sequence in each batch to finish.

A. Reduce the context window so that each request is shorter, on the assumption that fewer tokens per sequence removes the wait for the longest one
B. Use a smaller GPU, because a lower-memory device forces smaller batches and therefore shorter waits per batch
C. Increase the batch size so that more requests are processed together, which amortizes the cost of each forward pass
D. Enable in-flight (continuous) batching so finished sequences are evicted and new ones join mid-batch

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Static batching wastes GPU cycles on padding and on slots held by finished sequences. Continuous batching, which TensorRT-LLM and vLLM implement, replaces completed sequences immediately and typically multiplies throughput several times over. Simply raising batch size makes the head-of-line problem worse.
</details>

---

### Question 2
**Scenario:** KV cache memory dominates GPU usage at long context lengths.

A. Paged attention style KV cache management, plus KV cache quantization or grouped-query attention
B. Disable the cache entirely so no key-value memory is held, accepting that every step recomputes attention over the whole sequence
C. Increase max_tokens so the server reserves a larger output budget up front and avoids reallocating cache blocks during generation
D. Add more layers so the work is spread thinner per layer, which lowers the per-layer share of KV cache memory

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** KV cache grows linearly with sequence length and batch size and typically becomes the binding memory constraint before weights do. Paged allocation removes fragmentation, GQA reduces the number of KV heads, and quantizing the cache to FP8 or INT8 cuts it further. Disabling the cache would force quadratic recomputation.
</details>

---

### Question 3
**Scenario:** A 70B parameter model does not fit on a single GPU.

A. Gradient accumulation, which simulates a larger batch by summing gradients over steps but still needs the full model on every device
B. A larger batch size
C. Tensor parallelism to shard each layer across GPUs, optionally with pipeline parallelism across nodes
D. Data parallelism, which replicates the full 70B model on each GPU and splits only the batches, so each device still needs all the weights

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Data parallelism replicates the whole model per device, so it does not help when the model itself does not fit. Tensor parallelism splits individual matrices across GPUs with high communication needs, which is why it stays within an NVLink domain, while pipeline parallelism splits layers and tolerates slower inter-node links.
</details>

---

### Question 4
**Scenario:** A fine-tuning run must minimize GPU memory while keeping most of the quality of full fine-tuning.

A. Prompt tuning only, which trains a few virtual token embeddings and always matches the quality of full fine-tuning on new tasks
B. Full fine-tuning at FP32
C. LoRA or QLoRA with a frozen base model
D. Training from scratch, which gives the model maximum freedom to learn the target behavior and so the best quality for the memory spent

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** LoRA trains a small number of adapter parameters, so optimizer state (the dominant memory cost in training) shrinks dramatically. QLoRA adds a quantized frozen base to cut it further. Prompt tuning is even lighter but has less capacity for genuinely new behavior.
</details>

---

### Question 5
**Scenario:** Which technique reduces the latency of generating tokens by proposing several tokens ahead and verifying them in one pass?

A. Speculative decoding with a smaller draft model
B. Top-k sampling, which restricts each step to the k most likely tokens to shape diversity but still generates one token per forward pass
C. Beam search, which keeps several candidate sequences alive to improve output quality but multiplies compute rather than cutting latency
D. Gradient checkpointing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A cheap draft model proposes tokens and the target model verifies them in a single forward pass, accepting the longest correct prefix. Output distribution is preserved, so this is a pure latency win when acceptance rates are good. Gradient checkpointing is a training memory technique.
</details>

---

### Question 6
**Scenario:** Multi-node training slows down disproportionately as node count rises.

A. The interconnect is the bottleneck: check NCCL collectives, topology, and whether InfiniBand with GPUDirect RDMA is being used
B. The GPUs are faulty, so some devices run slower and the whole job waits at every synchronization step as node count rises
C. The dataset is too small to keep many workers busy, so extra nodes sit idle
D. The learning rate is wrong for the larger global batch, so each node count needs retuning before throughput can scale cleanly again

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** All-reduce traffic grows with scale, so communication rather than compute becomes the limit. NCCL debug output, topology awareness, and GPUDirect RDMA over InfiniBand are the standard investigation. A learning rate problem would show up as poor convergence rather than poor scaling.
</details>

---

### Question 7
**Scenario:** A production serving stack needs multiple models, multiple frameworks, dynamic batching, and model versioning.

A. NeMo Curator, which cleans, deduplicates and filters training data at scale but does not serve models to clients
B. cuDF, the GPU DataFrame library that accelerates pandas-style data processing but is not an inference server with model versioning
C. NVIDIA Triton Inference Server, with dynamic batching, a versioned model repository and concurrent multi-framework backends
D. A single Flask app

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Triton serves TensorRT, PyTorch, ONNX, and Python backends concurrently with dynamic batching, concurrent model instances, model repositories with versions, and ensemble pipelines. NIM builds on this stack for packaged LLM deployment.
</details>

---

### Question 8
**Scenario:** FP8 quantization is applied and quality drops noticeably on a reasoning benchmark.

A. Increase temperature, which adds randomness to sampling and so recovers reasoning steps lost to the lower numeric precision
B. Check calibration data and per-layer sensitivity, and keep sensitive layers at higher precision (mixed precision)
C. Revert to FP32 everywhere, which restores quality but gives up the memory and throughput gains that were the reason for quantizing
D. Accept the loss, because a drop on a reasoning benchmark is an expected cost of lower precision and cannot be tuned back

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Quantization sensitivity is not uniform across layers, and calibration data that does not resemble production traffic produces poor scales. Selectively keeping outlier-heavy layers at higher precision usually recovers most of the loss while retaining most of the speedup.
</details>

---

### Question 9
**Scenario:** A RAG system must handle queries that mix an exact product code with a natural-language description.

A. Pure vector search, which embeds the whole query and matches semantically, so an exact code is found as reliably as the description
B. Increase the embedding dimension so the vectors encode more detail, which makes rare exact tokens easier to match
C. Keyword search only
D. Hybrid search combining sparse (BM25 or keyword) and dense retrieval, then rerank

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Dense embeddings are weak on rare exact tokens such as SKUs and error codes, which is precisely where sparse retrieval excels. Fusing both and applying a cross-encoder reranker gives the best of each. Raising dimensionality does not fix the exact-match weakness.
</details>

---

### Question 10
**Scenario:** Which describes the NeMo framework's role?

A. A vector database that stores embeddings and serves similarity search for retrieval pipelines
B. An end-to-end framework for building, customizing, and deploying generative models, including data curation, training, PEFT, alignment, and export
C. A container registry that stores and distributes the images used to package training and serving workloads on GPU clusters
D. A GPU monitoring tool that reports utilization, temperature and memory per device across a cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NeMo spans the model lifecycle: NeMo Curator for data, the training and customization stack for pretraining and PEFT, alignment methods, Guardrails for safety, and export paths into TensorRT-LLM and NIM for serving.
</details>

---

### Question 11
**Scenario:** Time to first token is acceptable but inter-token latency is poor under load.

A. The decode phase is memory-bandwidth bound; consider larger batches, better KV cache handling, quantization, or faster memory
B. The prefill phase is the bottleneck, because a long prompt processed in one pass delays every later token
C. Network latency between client and server under load, which would also delay the first token rather than only the gaps between later tokens
D. The tokenizer is slow, since converting text to token IDs on the CPU stalls each generated token

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prefill is compute bound and determines time to first token; decode is memory-bandwidth bound and determines inter-token latency because each step reads the full weight set. Knowing which phase a symptom belongs to points at completely different fixes, and chunked prefill exists to stop long prefills stalling decode.
</details>

---

### Question 12
**Scenario:** Several fine-tuned variants of one base model must be served cost-effectively.

A. Deploy each as a separate full model so every variant has its own isolated weights, accepting a full set of GPUs per variant
B. Retrain a single model on everything so one deployment covers all tasks, even though the variants can interfere with each other
C. Merge them all into one model by averaging their weights, which gives every variant's behavior at once with no per-request selection
D. Serve one base model with multiple LoRA adapters loaded and selected per request

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-LoRA serving keeps one copy of the base weights in memory and swaps small adapters per request, which is dramatically cheaper than one full deployment per variant. Merging adapters is appropriate when you want a single fixed behavior with no per-request switching.
</details>

---

### Question 13
**Scenario:** A model upgrade must be validated against the incumbent before rollout.

A. Ship and monitor, relying on production dashboards and user feedback to reveal regressions after the new model is live
B. Run the evaluation suite (task accuracy, groundedness, safety, latency, cost) on the incumbent and the candidate, then canary a small traffic share
C. Compare parameter counts, since a model with more parameters is expected to match or beat the incumbent on every task
D. Compare the benchmark scores published by the vendor, which show how the new model ranks on standard public tasks

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Public benchmarks say little about your task distribution. An internal eval suite plus a canary gives evidence on both quality and operational characteristics before full exposure, and it catches regressions in behavior the new model is otherwise better at.
</details>

---

### Question 14
**Scenario:** GPU utilization sits at 40% during inference despite queued requests.

A. Increase the model size so each request keeps the GPU busy for longer, which raises utilization on the same hardware
B. Profile with Nsight or Triton metrics to find the bottleneck: tokenization, host-device transfer, small batches, or CPU work
C. Reduce the context window so each request needs less KV cache memory and finishes sooner, which keeps the GPU busy with queued work
D. Add more GPUs so the queue drains in parallel across devices, which spreads the waiting requests over more capacity

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Low utilization with a queue means the GPU is starved, usually by CPU preprocessing, serialization, or a scheduling configuration that keeps batches small. Adding hardware to a pipeline bottleneck multiplies the idle capacity rather than fixing it.
</details>

---

### Question 15
**Scenario:** Guardrails must block a class of unsafe requests without harming legitimate use.

A. A blocklist of words that rejects any prompt containing a flagged term, which is simple to maintain and cheap to run
B. Layered controls: input classification, topical rails, output moderation, and tracking the violation rate alongside the false refusal rate
C. Lower temperature, which makes responses more deterministic and therefore less likely to contain unsafe content
D. Shorter responses, which limit how much unsafe text can appear in each reply

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve, not a switch, so both directions must be measured: blocking more raises false refusals, which is a genuine product failure. Word blocklists are trivially evaded and catch benign text, which is why they perform badly on both axes.
</details>

---

### Question 16
**Scenario:** A team serving a 70B model at long context finds that KV cache memory limits batch size. They are comparing architectures for their next model.

A. Use more query heads per layer, which shrinks the KV cache because queries are never cached
B. Use post-layer normalization, which removes the need to store keys and values during decoding
C. Use grouped-query attention, where groups of query heads share key and value heads
D. Use a larger vocabulary, which shortens sequences enough to remove the KV cache bottleneck

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The KV cache stores keys and values per head, so sharing a key-value head across a group of query heads divides the cache size by the group factor with little quality loss; multi-query attention is the extreme case with one KV head. Adding query heads does not shrink the cache. Normalization placement has no effect on caching, and a bigger vocabulary shortens sequences only modestly.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 17
**Scenario:** A model pretrained with rotary position embeddings (RoPE) at 8k context must handle 64k-token documents without full retraining.

A. Apply a RoPE scaling method such as position interpolation or YaRN, then fine-tune briefly on long sequences
B. Feed 64k-token inputs directly, since rotary embeddings extend to any length with no loss of quality
C. Replace RoPE with learned absolute position embeddings and continue pretraining from the start
D. Split each document into 8k windows and process them separately, which gives a 64k context

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context extension methods rescale rotary positions so long sequences map into the range the model saw during training, and a short fine-tune on long data recovers quality. Running far beyond the trained length without scaling usually degrades badly. Learned absolute embeddings cannot extrapolate either, and separate windows do not let tokens attend across the whole document.

**Key Concept:** [NeMo Framework overview](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)
</details>

---

### Question 18
**Scenario:** Profiling shows that standard attention spends most of its time reading and writing the full attention matrix to GPU high-bandwidth memory, not on math.

A. Switch attention to FP32, which reduces memory traffic by using fewer but wider memory reads
B. Approximate attention with a low-rank projection, which changes the results but is always faster
C. Increase the number of attention heads, which spreads the memory traffic across more SMs
D. Use FlashAttention, which tiles the work in on-chip memory and computes exact attention

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FlashAttention is IO-aware: it processes attention in tiles held in on-chip SRAM and never materializes the full attention matrix in HBM, cutting memory traffic while producing exact results. FP32 doubles the bytes moved. Low-rank approximations change outputs, and more heads do not reduce the matrix traffic.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 19
**Scenario:** A model is split across 8 pipeline stages, and profiling shows GPUs idle for long stretches at the start and end of each step.

A. Reduce the global batch size, which shortens each step and so removes the idle periods
B. Increase the number of pipeline stages to 16, which halves the idle time on every stage
C. Split each batch into many micro-batches, or use an interleaved schedule, to shrink the bubble
D. Switch to data parallelism only, since pipeline parallelism cannot be made efficient at all

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The idle time is the pipeline bubble while stages fill and drain. Its share falls as the number of micro-batches per step grows, and interleaved schedules that give each GPU several smaller stages reduce it further. A smaller batch means fewer micro-batches and a bigger bubble, more stages lengthen fill and drain, and data parallelism alone cannot fit a model that needs pipelining.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 20
**Scenario:** In data-parallel training, every GPU holds a full copy of the Adam optimizer states, which use more memory than the model weights.

A. Shard the optimizer states across data-parallel ranks with a distributed optimizer (ZeRO-style)
B. Switch from Adam to plain SGD on every model, since optimizer states are not needed at scale
C. Store the optimizer states on local NVMe and read them back only once per training epoch
D. Lower the learning rate, which reduces the size of the optimizer states held on each GPU

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A distributed optimizer partitions optimizer states, and optionally gradients and parameters, across data-parallel ranks so each GPU stores only its share, removing the redundant copies; Megatron Core and NeMo provide this. Abandoning Adam often hurts convergence for LLMs. Reading states from disk once per epoch is wrong because they are updated every step, and the learning rate does not change state size.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 21
**Scenario:** Training runs out of memory because of stored activations at long sequence lengths. The team can accept somewhat slower steps.

A. Turn off mixed precision, which stores activations more efficiently in FP32 format
B. Increase the micro-batch size, which lowers activation memory for each sequence
C. Remove the residual connections, which are what hold the activations in memory
D. Use activation checkpointing, which recomputes activations in the backward pass

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Activation checkpointing (recomputation) keeps only some activations during the forward pass and recomputes the rest during backward, trading extra compute for a large memory saving; selective recomputation targets the most memory-hungry parts. FP32 activations take more memory, bigger micro-batches add activations, and residual connections are essential to training deep networks.

**Key Concept:** [Megatron Core user guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/index.html)
</details>

---

### Question 22
**Scenario:** A multi-replica LLM service sees that many requests share long common prefixes, but a round-robin load balancer sends them to replicas that have not cached those prefixes.

A. Shorten the shared prefix in every request, which removes the need for any cache on the replicas
B. Send all traffic to one replica so that every prefix is cached in one place for all requests
C. Use KV-cache-aware routing, as in NVIDIA Dynamo, to send requests to workers that hold the prefix
D. Disable the KV cache on all replicas so that routing decisions no longer affect performance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A KV-aware router tracks which workers hold which cached blocks and sends each request where its prefix is already cached, while balancing load, so prefill work is reused instead of repeated. The shared prefix is often a needed system prompt or document. One replica cannot carry the load, and disabling the cache slows every request.

**Key Concept:** [NVIDIA Dynamo documentation](https://docs.nvidia.com/dynamo/latest/index.html)
</details>

---

### Question 23
**Scenario:** At small batch sizes, token generation is limited by reading the weights from GPU memory, and the team wants faster decoding with minimal quality loss.

A. Quantize activations only to INT8, which leaves weight reads unchanged but saves compute
B. Use 4-bit weight-only quantization such as AWQ, which cuts the bytes read for each token
C. Increase the batch size to 1,024, which makes decoding compute-bound for every request
D. Switch to FP32 weights, which the GPU reads more efficiently than reduced-precision formats

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** At small batch sizes decoding is memory-bandwidth-bound, so shrinking the weights to 4 bits cuts the data read per token and speeds up generation; activation-aware methods such as AWQ protect the most important weights to limit quality loss. Activation-only quantization leaves the bottleneck untouched. A huge batch changes the workload and its latency, and FP32 doubles the bytes moved.

**Key Concept:** [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/)
</details>

---

### Question 24
**Scenario:** Every request to a chat service starts with the same 6,000-token system prompt, and time to first token is high.

A. Enable prefix (KV cache) reuse, so the shared system prompt's prefill is computed once and reused
B. Move the system prompt to the end of each request so that the model reads it after the question
C. Increase the maximum number of output tokens, which reduces the time to the first output token
D. Lower the temperature, which shortens the prefill step for prompts longer than a few thousand tokens

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Time to first token is dominated by prefill, and with prefix caching the KV blocks for an identical prefix are computed once and reused across requests, so only the new part of each prompt needs prefill. Moving the prompt breaks the shared prefix. Output length and temperature do not affect prefill time.

**Key Concept:** [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/)
</details>

---

### Question 25
**Scenario:** Questions such as "Which supplier of our top-selling product had the most late shipments?" fail in a RAG system, because no single chunk contains the answer.

A. Increase the chunk size until one chunk holds the full answer to every multi-hop question
B. Lower the similarity threshold, so that the first search returns every chunk in the corpus
C. Fine-tune the embedding model, which teaches it to put the whole answer into a single vector
D. Decompose the question and retrieve iteratively, feeding each result into the next query

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-hop questions need intermediate answers (first find the top product, then its suppliers, then shipments), so decomposing the question and running retrieval in steps, often as an agentic loop, assembles evidence no single query finds. Huge chunks dilute relevance and still may not hold everything. Returning everything defeats retrieval, and a better embedding does not combine facts from separate documents.

**Key Concept:** [NVIDIA NeMo Retriever](https://docs.nvidia.com/nemo/retriever/index.html)
</details>

---

### Question 26
**Scenario:** Downstream code needs every response to be valid JSON matching a schema, and prompt instructions alone still produce malformed output now and then.

A. Lower the temperature to zero, which guarantees that every output is valid JSON for the schema
B. Retry each malformed response up to ten times, which makes valid JSON certain on every call
C. Use constrained (guided) decoding against the JSON schema, so that only valid tokens can be generated
D. Ask the model to double-check its JSON at the end of the answer before it finishes generating

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Guided decoding restricts which tokens can be sampled at each step to those that keep the output valid against a grammar or JSON schema, so the structure is guaranteed by construction; engines such as vLLM, SGLang and TensorRT-LLM support it. Low temperature reduces but does not remove malformed output. Retries add cost and latency without a guarantee, and self-checking is still free-form generation.

**Key Concept:** [NIM for LLMs API reference](https://docs.nvidia.com/nim/large-language-models/latest/reference/api-reference.html)
</details>

---

### Question 27
**Scenario:** A RAG prompt holds 40 retrieved chunks. The model answers well when the key chunk is first or last but often misses it in the middle.

A. Add more chunks so that the key fact appears several times somewhere in the middle of the context
B. Rerank and send fewer chunks, placing the most relevant at the start or end of the context
C. Raise the temperature so that the model's attention spreads more evenly across all of the chunks
D. Switch to a model with a larger vocabulary, which removes position effects in long contexts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models often use information at the beginning and end of a long context better than the middle (the "lost in the middle" effect), so fewer, reranked chunks with the most relevant placed prominently improve accuracy. More chunks make the problem worse. Temperature affects sampling, not where the model attends, and vocabulary size has nothing to do with position effects.

**Key Concept:** [NeMo Retriever reranking NIM](https://docs.nvidia.com/nim/nemo-retriever/reranking/latest/index.html)
</details>

---

### Question 28
**Scenario:** A team wants to score thousands of open-ended answers for helpfulness on every release. Human review of all of them is too slow.

A. Use an LLM-as-a-judge with a clear rubric, calibrated against a human-labeled sample, and track agreement
B. Use exact string match against one reference answer, which captures helpfulness for every open question
C. Measure perplexity on each answer, since a low perplexity proves that an answer is helpful to users
D. Count the words in each answer, since longer answers are reliably more helpful than shorter ones

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An LLM judge with an explicit rubric scales to thousands of answers, and checking its agreement with human labels on a sample shows whether its scores can be trusted, including known biases such as favoring longer answers. Exact match fails for open-ended text. Perplexity measures fluency, not helpfulness, and length is a known bias rather than a quality measure.

**Key Concept:** [NeMo Framework overview](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)
</details>

---

### Question 29
**Scenario:** Before launch, a team must size GPU capacity for an LLM service with targets for time to first token and inter-token latency at expected peak concurrency.

A. Use the GPU vendor's peak FLOPS figure and divide it by the model's parameter count
B. Send one request at a time and multiply its latency by the expected number of users
C. Assume that throughput grows linearly with concurrency until the GPU runs out of memory
D. Load test at rising concurrency, recording TTFT, inter-token latency and throughput

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** LLM serving performance depends on batching, KV cache pressure and sequence lengths, so the reliable approach is a benchmark that sweeps concurrency with realistic input and output lengths and finds where latency targets break. Peak FLOPS ignores memory-bound decoding. Single-request tests miss batching effects, and throughput flattens and latency climbs well before memory runs out.

**Key Concept:** [NIM for LLMs: model profiles and selection](https://docs.nvidia.com/nim/large-language-models/latest/deployment/model-profiles-and-selection.html)
</details>

---

### Question 30
**Scenario:** A shared LLM platform serves several internal teams, and one team's batch job sends huge prompts that slow everyone else down.

A. Give the batch team its own copy of the model weights, stored on the same set of GPUs as before
B. Limit every request to 100 tokens, which stops any single team from using too much capacity
C. Apply per-tenant token quotas and rate limits, and route batch work to its own pool
D. Lower the temperature for the batch team, which reduces the GPU time each of its requests uses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** LLM cost scales with tokens, not request count, so token-based quotas and rate limits per tenant contain a heavy user, and a separate pool or priority for batch work protects interactive latency. A second copy on the same GPUs still competes for them. A hard 100-token limit breaks legitimate use, and temperature does not change compute per token.

**Key Concept:** [NVIDIA Dynamo documentation](https://docs.nvidia.com/dynamo/latest/index.html)
</details>

---

## Where to go deeper

- [NCP-GENL cert page](../nvidia/genai-llms-professional/README.md) - notes, practice plan, strategy
- [NCA-GENL practice questions](nvidia-genai-llms-associate.md) - the associate level below this
- [Inference servers](../../learn/concepts/inference-servers.md) - serving in plain English
- [Quantization and distillation](../../learn/concepts/quantization-and-distillation.md) - making models smaller
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
