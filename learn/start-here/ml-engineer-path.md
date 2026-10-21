# The ML Engineer Path

**In one line:** A route for people who want to work below the API - training, fine-tuning, evaluating and serving models themselves - covering the maths you actually need, classical ML, deep learning, fine-tuning, and inference infrastructure, in roughly four to six months part time.
**Last reviewed:** 2026-10-21

---

## The short version

- An **ML engineer** trains, adapts, evaluates and serves models. Where an [AI engineer](ai-engineer-path.md) treats the model as a service, you treat it as an artifact you own: its data, its weights, its hardware and its latency.
- You need more foundations than the AI engineer path: Python and NumPy fluency, linear algebra and probability at an applied level, one deep learning framework (PyTorch is the default), and a working knowledge of GPUs.
- Learn in this order: **classical ML** (to learn evaluation and overfitting cheaply), **deep learning** (to learn training), **transformers** (to understand what everyone ships), **fine-tuning** (the most common modern task), **serving** (where the cost lives).
- Most ML engineering work in 2026 is not pretraining a frontier model. It is fine-tuning open-weight models, building data pipelines, running evaluations, and making inference fast and cheap.
- The data is usually the hard part. Expect to spend more time on datasets than on architectures.

## Who this is for

You can program comfortably in Python. You may be a software engineer, a data scientist, a data engineer, or a student. You want to understand and control models, not just call them. If you would rather build applications on hosted models, the [AI engineer path](ai-engineer-path.md) is faster and the job market for it is broader; you can come back here later.

## Stage 1: The maths, applied (weeks 1 to 4)

You need less maths than people fear and more than zero. The goal is to read a training loop or a paper's method section and know what each line is doing.

- **Linear algebra:** vectors, matrices, matrix multiplication, dot products, and what a shape like `(batch, sequence, hidden)` means. A neural network layer is a matrix multiply plus a simple function; once that is natural, most architectures are readable.
- **Calculus:** what a derivative and a gradient are, and the chain rule. You will not compute gradients by hand (frameworks do that), but you need to know what "the gradient of the loss with respect to the weights" means.
- **Probability and statistics:** distributions, expectation, variance, conditional probability, and the logic of a train/validation/test split. A language model outputs a probability distribution over tokens; [sampling and decoding](../../explainers/concepts/sampling-and-decoding.md) is applied probability.

Learn these with code, not just pen and paper: implement a dot product, a softmax and a gradient-descent step in NumPy. [Python for AI](../day-one/python-for-ai.md) and [Notebooks and Colab](../day-one/notebooks-and-colab.md) cover the tools.

**Checkpoint:** you can implement linear regression trained by gradient descent in about 30 lines of NumPy, and explain why the loss goes down.

## Stage 2: Classical machine learning (weeks 5 to 7)

Start with [What is machine learning?](../concepts/what-is-machine-learning.md) for the framing, then [Classic ML: supervised vs unsupervised](../concepts/classic-ml-supervised-vs-unsupervised.md) and [Training, validation and overfitting](../concepts/training-validation-and-overfitting.md), which give you runnable scikit-learn baselines and the metrics (precision, recall, F1, ROC-AUC) you will use for the rest of your career. [Recommender systems basics](../concepts/recommender-systems-basics.md) shows those pieces in the system most companies actually run. Then work with scikit-learn on tabular data: linear and logistic regression, decision trees, gradient-boosted trees, k-means. Gradient-boosted trees are still the strongest choice for many tabular business problems, and they train in seconds.

The real lessons of this stage are not the algorithms. They are **overfitting**, **data leakage**, **choosing a metric**, and **honest evaluation**. These lessons carry straight into deep learning and LLM work, and they are far cheaper to learn on a dataset that fits in memory.

**Checkpoint:** you have trained a model on a public tabular dataset, beaten a simple baseline on a held-out test set, and can explain one way you could have fooled yourself with leakage.

## Stage 3: Deep learning (weeks 8 to 12)

Read [Neural networks in plain English](../concepts/neural-networks-plain-english.md), then learn PyTorch: tensors, autograd, `nn.Module`, a training loop, a data loader. Train a small image classifier and a small text model yourself.

This is where the research summaries start paying off. Read them alongside the code:

- [Adam](../../papers/techniques/142-adam/summary.md), the optimiser you will use by default, and [Muon](../../papers/techniques/144-muon/summary.md), a newer alternative.
- [ResNet](../../papers/architectures/73-resnet/summary.md), the residual connection that made deep networks trainable.
- [Mixed precision training](../../papers/techniques/143-mixed-precision-training/summary.md), why modern training runs in 16-bit or lower.
- [Software 2.0](../../papers/essays/110-software-2/summary.md) and [The Bitter Lesson](../../papers/essays/111-bitter-lesson/summary.md) for the philosophy.

**Checkpoint:** you can write a PyTorch training loop from scratch, train a model on a GPU, and diagnose an overfitting run from its loss curves.

## Stage 4: Transformers and language models (weeks 13 to 16)

Read [Transformer architecture](../concepts/transformer-architecture.md) and the [Attention Is All You Need summary](../../papers/architectures/01-attention-is-all-you-need/summary.md), then build one. Andrej Karpathy's "Let's build GPT" video walks through writing a small GPT from scratch in a few hundred lines, and it is the best single exercise on this path.

Then learn what changed after 2017: [tokenization](../../explainers/concepts/tokenization.md), [RoPE positional embeddings](../../papers/techniques/54-rope-rotary-position-embedding/summary.md), [grouped-query attention](../../papers/architectures/75-grouped-query-attention/summary.md), [FlashAttention](../../papers/techniques/16-flash-attention/summary.md), [mixture of experts](../../papers/architectures/37-mixture-of-experts/summary.md), the [KV cache](../../explainers/concepts/kv-cache.md), and [scaling laws](../../papers/techniques/12-scaling-laws/summary.md) with [Chinchilla](../../papers/techniques/18-chinchilla/summary.md). The [LLaMA](../../papers/language-models/15-llama/summary.md) and [DeepSeek-V3](../../papers/language-models/27-deepseek-v3/summary.md) summaries show how these pieces combine in real models.

**Checkpoint:** you have trained a small character- or token-level GPT, and can explain what each block in a modern open model's config file controls.

## Stage 5: Post-training and fine-tuning (weeks 17 to 20)

This is the most common ML engineering task today. Read [How LLMs are trained](../concepts/how-llms-are-trained.md) for the whole pipeline you are slotting into, then [Fine-tuning vs RAG](../concepts/fine-tuning-vs-rag.md), so you know when not to fine-tune. Then:

- **Parameter-efficient fine-tuning:** [LoRA](../../papers/techniques/10-lora/summary.md) and [QLoRA](../../papers/techniques/22-qlora/summary.md). These let you fine-tune a large model on one GPU.
- **Preference tuning:** [InstructGPT/RLHF](../../papers/language-models/05-instructgpt-rlhf/summary.md), [DPO](../../papers/language-models/19-dpo/summary.md), [KTO](../../papers/techniques/103-kto/summary.md).
- **Reinforcement learning for reasoning:** [PPO](../../papers/techniques/63-ppo/summary.md), [GRPO](../../papers/techniques/38-grpo/summary.md), [RLVR](../../papers/techniques/39-rlvr/summary.md), [DeepSeek-R1](../../papers/language-models/26-deepseek-r1/summary.md), and the [reasoning models explainer](../../explainers/concepts/reasoning-models.md).
- **Data:** [Self-Instruct](../../papers/techniques/79-self-instruct/summary.md), [phi-1 "Textbooks Are All You Need"](../../papers/language-models/135-phi-1-textbooks/summary.md), [FineWeb](../../papers/techniques/133-fineweb/summary.md), and the [Tulu 3](../../papers/language-models/148-tulu-3/summary.md) open post-training recipe, which documents a full pipeline end to end.
- **Smaller and cheaper:** [Small language models](../concepts/small-language-models.md), [Quantization and distillation](../concepts/quantization-and-distillation.md), [GPTQ and AWQ](../../papers/techniques/86-gptq-awq-quantization/summary.md), [knowledge distillation](../../papers/techniques/134-knowledge-distillation/summary.md).

**Project:** [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md). Fine-tune a small open-weight model on a narrow task, and compare it against the base model with a prompt, using an eval set you wrote before training. Be prepared for the prompt to win; finding that out is a valid result.

## Stage 6: Serving and infrastructure (weeks 21 to 24)

Models cost most when they run, not when they train. Read [GPUs for AI](../concepts/gpus-for-ai.md), [Inference servers](../concepts/inference-servers.md), the [PagedAttention/vLLM summary](../../papers/techniques/52-pagedattention-vllm/summary.md), [speculative decoding](../../papers/techniques/45-speculative-decoding/summary.md), and the [inference economics](../../explainers/compute/inference-economics.md) and [AI hardware landscape](../../explainers/compute/ai-hardware-landscape.md) explainers. For training at scale, [ZeRO and Megatron-LM](../../papers/techniques/76-zero-megatron/summary.md) and [cost of training](../../explainers/compute/cost-of-training.md).

**Projects:** [Run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md) with an inference server, measure throughput and latency at different batch sizes, then [Deploy an ML model](../../build/projects/deploy-ml-model.md) behind an API. [The LLM serving decision](../../tools/decisions/llm-serving.md) and the [AI/ML pipeline pattern](../../build/patterns/ai-ml-pipeline.md) frame the production choices, and [cloud AI/ML services](../../tools/comparisons/cloud-ai-ml-services.md) compares the managed options.

## Hardware and budget

You do not need to buy a GPU. Free notebook tiers ([Notebooks and Colab](../day-one/notebooks-and-colab.md)) cover Stages 1 to 3, though free GPU access is limited and not guaranteed. For Stages 4 to 6, renting a cloud GPU by the hour is usually cheaper than buying one until you are using it most days. A consumer GPU with 16 to 24 GB of memory is enough to fine-tune small models with QLoRA and to serve 7B-to-30B-class models quantised.

## Common mistakes

- **Skipping classical ML.** It is where you learn evaluation discipline cheaply. People who skip it make leakage mistakes on expensive GPU runs.
- **Starting from pretraining.** Almost no one pretrains a large model. Learn to adapt and serve existing ones first.
- **Fine-tuning to add knowledge.** Fine-tuning is good at teaching a format, a style or a narrow skill. It is a poor way to teach facts; use retrieval for that.
- **No baseline.** Always compare against the base model with a good prompt. If you cannot beat it, the fine-tune is not worth maintaining.
- **Ignoring data quality.** Most fine-tuning failures are data failures: duplicates, label noise, train/test overlap, or training examples that do not look like production inputs.

## Next steps

- [ML engineer interview](../../careers/interviews/ml-engineer-interview.md)
- [AI careers map](../../careers/roles/ai-careers-map.md)
- [Researcher path](researcher-path.md) if you want to go further toward the frontier
- The paper-first "ML student/researcher" route in [docs/ROADMAP.md](../../docs/ROADMAP.md)
- NVIDIA certification study guides on this site: [NVIDIA tracks](../../certifications/nvidia/README.md)

## Sources

- PyTorch tutorials: https://docs.pytorch.org/tutorials/
- scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Andrej Karpathy, "Let's build GPT: from scratch, in code, spelled out" (video): https://www.youtube.com/watch?v=kCc8FmEb1nY
- Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models" (2021): https://arxiv.org/abs/2106.09685
- Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs" (2023): https://arxiv.org/abs/2305.14314
- Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (2023): https://arxiv.org/abs/2309.06180
- Google Colab FAQ (free tier limits are not guaranteed): https://research.google.com/colaboratory/faq.html
