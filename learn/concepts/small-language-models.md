# Small Language Models

**In one line:** Know when a model of roughly 0.5 to 15 billion parameters is the better choice than a frontier model (cost, latency, privacy, offline use, narrow tasks), how small models are made good, which families to try first as of 2026-10, and how to test whether one is good enough for your job.
**Last reviewed:** 2026-10-21

---

> Assumes [LLM basics](llm-basics.md) and ideally [Quantization and distillation](quantization-and-distillation.md). For running one on your machine, see [Run a model locally](../day-one/run-a-model-locally.md).

## The short version

- "Small" is relative and has no official line. In practice a **small language model (SLM)** is one that runs on a single consumer GPU, a laptop or a phone: roughly 0.5B to 15B parameters, often quantised to 4 bits.
- Small models are not just weaker big models. Trained on carefully chosen data, distilled from larger models, and trained far longer than the compute-optimal point, a modern 4B model can beat the large models of two or three years ago on many benchmarks.
- Use one when you need **low cost at high volume, low latency, data that never leaves your hardware, offline use, or a narrow task you can fine-tune for**. Use a frontier model for open-ended reasoning, broad knowledge, long complex agent tasks, and anything where a wrong answer is expensive.
- Their weak spots are predictable: less world knowledge (more [hallucination](hallucinations.md) on facts), weaker multi-step reasoning, shorter effective context, and more brittleness to prompt wording.
- Families worth trying first as of 2026-10: **Qwen3** (0.6B to 14B), **Gemma** (Gemma 3 and 3n, and Gemma 4's small sizes), **Phi-4** and **Phi-4-mini**, **Llama 3.2** 1B and 3B, and **SmolLM3**. Check licences: they differ.

## Why small models got good

Three things changed the size-to-quality curve.

**Better data, not more of it.** The phi-1 paper (["Textbooks are all you need"](../../papers/language-models/135-phi-1-textbooks/summary.md)) showed a 1.3B model trained on filtered "textbook quality" and synthetic data could rival much larger models at Python coding. Data filtering work such as [FineWeb](../../papers/techniques/133-fineweb/summary.md) generalised the lesson: what you leave out matters as much as how much you put in.

**Overtraining on purpose.** [Chinchilla](../../papers/techniques/18-chinchilla/summary.md) worked out the cheapest way to reach a given quality at training time: about 20 tokens per parameter. But a model is trained once and served millions of times, so it pays to spend extra training compute to make a smaller model better, because every future query is cheaper. Hugging Face reports training the 3B SmolLM3 on 11.2 trillion tokens, thousands of tokens per parameter.

**Distillation.** A large "teacher" model generates training data or soft targets for a small "student". Many small models in current families are distilled from their bigger siblings, as are the distilled DeepSeek-R1 variants in the [DeepSeek-R1 summary](../../papers/language-models/26-deepseek-r1/summary.md). The original idea is in the [knowledge distillation summary](../../papers/techniques/134-knowledge-distillation/summary.md); [Quantization and distillation](quantization-and-distillation.md) explains the mechanics.

Add **quantisation** (storing weights in 4 or 8 bits instead of 16) and a 4B-parameter model needs only around 2 to 3 GB of memory, which fits on most laptops and recent phones.

## Families to know (as of 2026-10-21)

All from the publishers' model cards. Sizes are total parameters unless noted.

| Family | Small sizes | Context | Licence | Notes |
|---|---|---|---|---|
| **Qwen3** (Alibaba) | 0.6B, 1.7B, 4B, 8B, 14B dense; 30B-A3B MoE | 32K on 0.6B | Apache 2.0 | Switchable thinking and non-thinking modes; strong multilingual |
| **Gemma 3** (Google) | 270M, 1B, 4B, 12B | 32K (270M, 1B), 128K (4B+) | Gemma terms (check card) | Multimodal from 4B up |
| **Gemma 3n** (Google) | E2B, E4B ("effective" sizes) | 32K | Gemma terms (check card) | Built for phones and laptops; text, image and audio input |
| **Gemma 4** (Google) | E2B, E4B, 12B; 26B-A4B MoE | see card | Apache 2.0 | Newest generation (card updated 2026-07-30); the 26B MoE activates about 3.8B per token |
| **Phi-4** (Microsoft) | 14B | 16K | MIT | Reasoning and maths-heavy training data |
| **Phi-4-mini** (Microsoft) | 3.8B | 128K | MIT | Long context for its size |
| **Llama 3.2** (Meta) | 1B, 3B | 128K | Llama 3.2 Community License | Text-only small sizes; restrictions above a user threshold |
| **SmolLM3** (Hugging Face) | 3B | 64K (128K with YaRN) | Apache 2.0 | Fully open training recipe and data mix |
| **Apple on-device model** | about 3B | n/a | Apple platforms only | Exposed to app developers through the Foundation Models framework |

"Effective" parameters (E2B, E4B) and mixture-of-experts sizes like 30B-A3B mean the model does the compute of a small model per token while storing more weights. Memory is set by the total; speed by the active count. See the [mixture of experts summary](../../papers/architectures/37-mixture-of-experts/summary.md).

## When to choose small

| Situation | Why small wins |
|---|---|
| High-volume, narrow tasks (classify, extract, route, tag) | Cost per call is a fraction of a cent, often near zero self-hosted |
| Latency-critical (autocomplete, voice, UI hints) | Fewer parameters means faster tokens; can run next to the user |
| Data must not leave the device or your network | Runs locally; nothing sent to a provider |
| Offline or edge (field devices, aircraft, factories) | No network needed |
| You will fine-tune | Fine-tuning a 3B to 8B model with [LoRA](../../build/projects/fine-tune-with-lora.md) is cheap; a tuned small model often beats a prompted large one on its narrow task |
| A first-pass filter or router | Handle the easy 80% cheaply, escalate the rest |

And when not to: open-ended questions that need broad knowledge, multi-step planning, long agent runs, complex code across a large codebase, and high-stakes answers. A small model will give fluent, confident and wrong answers in exactly those places.

## A worked test: is a small model good enough?

Never decide from a leaderboard. Decide from your own task. A practical procedure:

1. Collect 50 to 200 real examples of the task with the correct answer (for extraction, the expected JSON; for classification, the label).
2. Run your current large model on them and score it. This is your bar.
3. Run two or three small models locally on the same prompts and score them the same way. With [Ollama](../day-one/run-a-model-locally.md), switching models is one string.
4. Look at the failures, not only the score. Are they random, or all one kind (dates, long inputs, a rare category)? Clustered failures can often be fixed with a better prompt, constrained output, or a few hundred fine-tuning examples.
5. Compare cost and latency at your real volume (see [AI cost basics](ai-cost-basics.md)).

A minimal harness using any OpenAI-compatible local server:

```python
import json
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")  # Ollama's local API

examples = [json.loads(line) for line in open("tickets.jsonl")]  # {"text": ..., "label": ...}
LABELS = ["billing", "bug", "feature_request", "account", "other"]

def classify(model, text):
    resp = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": f"Classify the support ticket. Reply with exactly one of: {', '.join(LABELS)}."},
            {"role": "user", "content": text},
        ],
    )
    return resp.choices[0].message.content.strip().lower()

for model in ["qwen3:4b", "gemma3:4b", "llama3.2:3b"]:
    correct = sum(classify(model, ex["text"]) == ex["label"] for ex in examples)
    print(f"{model}: {correct}/{len(examples)} correct")
```

Model tags follow Ollama's library naming at the time of writing; run `ollama list` to see what you have pulled. Use [structured outputs](structured-outputs.md) or constrained decoding if a model keeps adding extra words around its label, a common small-model habit.

## Making a small model work better

- **Narrow the task.** One job per call, short instructions, a fixed output format.
- **Give it the facts.** Small models know less, so [RAG](rag-explained.md) helps them even more than large ones.
- **Constrain the output.** JSON schemas and grammar-constrained decoding stop format drift.
- **Use few-shot examples** in the prompt; small models lean on them heavily.
- **Fine-tune** when prompting plateaus. A few hundred to a few thousand good examples go a long way at this size.
- **Turn thinking on selectively.** Hybrid models such as Qwen3 and SmolLM3 can reason step by step when asked, which helps on maths and logic at the cost of more tokens and latency.

## Common mistakes

- **Trusting general benchmarks.** A small model's MMLU score says little about your extraction task. Test on yours.
- **Expecting world knowledge.** Small models have less room to memorise facts; ground them.
- **Forgetting the licence.** "Open weights" ranges from Apache 2.0 to custom licences with use restrictions. Read it before shipping. See [Open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md).
- **Comparing a quantised small model to an unquantised large one** and blaming size for what quantisation did. Note the quantisation level in every comparison.
- **Over-long prompts.** A 128K context window on the model card does not mean quality holds at 128K; see the [RULER summary](../../papers/techniques/132-ruler/summary.md).

## Next steps

- [Run a model locally](../day-one/run-a-model-locally.md) and [Run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md)
- [Quantization and distillation](quantization-and-distillation.md)
- [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md)
- [Local LLM runners compared](../../tools/comparisons/local-llm-runners.md)
- [Open-source stack explainer](../../explainers/ecosystem/open-source-stack.md) and the [Qwen](../../explainers/model-families/qwen.md) and [Llama](../../explainers/model-families/llama.md) family explainers

## Sources

- Qwen team, "Qwen3: Think Deeper, Act Faster" (2025-04-29): https://qwenlm.github.io/blog/qwen3/ and model card https://huggingface.co/Qwen/Qwen3-0.6B
- Google, Gemma 3 model card: https://ai.google.dev/gemma/docs/core/model_card_3 ; Gemma 3n overview: https://ai.google.dev/gemma/docs/gemma-3n ; Gemma 4 model card: https://ai.google.dev/gemma/docs/core/model_card_4
- Microsoft, Phi-4 model card: https://huggingface.co/microsoft/phi-4 ; Phi-4-mini-instruct: https://huggingface.co/microsoft/Phi-4-mini-instruct
- Meta, Llama 3.2 1B model card: https://huggingface.co/meta-llama/Llama-3.2-1B
- Hugging Face, SmolLM3-3B model card (11.2T training tokens): https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- Apple Machine Learning Research, "Updates to Apple's On-Device and Server Foundation Language Models" (2025): https://machinelearning.apple.com/research/apple-foundation-models-2025-updates
- Gunasekar et al., "Textbooks Are All You Need" (2023): https://arxiv.org/abs/2306.11644
- Hinton, Vinyals and Dean, "Distilling the Knowledge in a Neural Network" (2015): https://arxiv.org/abs/1503.02531
- The harness above is untested against live models; tags and outputs vary by Ollama version.
