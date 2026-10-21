---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Generative AI and LLMs (NCP-GENL) - Practice Questions

15 questions for NCP-GENL prep, evenly weighted across LLM architecture, training and fine-tuning at scale, inference optimization, prompt engineering and RAG, and production deployment (20% each).

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

## Where to go deeper

- [NCP-GENL cert page](../nvidia/genai-llms-professional/README.md) - notes, practice plan, strategy
- [NCA-GENL practice questions](nvidia-genai-llms-associate.md) - the associate level below this
- [Inference servers](../../learn/concepts/inference-servers.md) - serving in plain English
- [Quantization and distillation](../../learn/concepts/quantization-and-distillation.md) - making models smaller
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
