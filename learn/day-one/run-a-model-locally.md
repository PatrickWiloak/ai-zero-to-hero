# Run a Model Locally

**In one line:** Download an open-weight language model and run it on your own laptop or desktop with Ollama, chat with it, call it from Python through an OpenAI-compatible API, and know which model sizes your hardware can handle.
**Last reviewed:** 2026-10-21

---

## The short version

- **Open-weight** models (from families such as Gemma, Qwen, Llama, Mistral and DeepSeek) can be downloaded and run on your own machine: free per use, private, and working offline.
- **Ollama** is the easiest way to start: one install, then `ollama run <model>`. LM Studio is a friendly desktop alternative; llama.cpp is the engine underneath much of this ecosystem.
- What you can run is set mostly by **memory**: your GPU's VRAM, or unified memory on Apple Silicon. A quantised model needs roughly half a gigabyte per billion parameters, plus room for the context.
- On a typical modern laptop, models in the 2B to 12B range run comfortably. 27B to 35B models want 24 GB or more. The largest open models need server hardware.
- Local models are good for learning, privacy-sensitive drafts, offline work, high-volume simple tasks and tinkering. For the hardest reasoning and coding tasks, hosted frontier models are still clearly stronger.
- Ollama exposes an **OpenAI-compatible API** on your machine, so code written for hosted models can point at a local one by changing two lines.

## Why run a model yourself

Hosted APIs are easier and, for the hardest tasks, better. Running locally earns its place for other reasons:

- **Privacy.** The text never leaves your machine. That matters for personal notes, medical or legal drafts, and anything your employer would not want sent to a third party.
- **Cost.** No per-token bill. A batch job that would cost real money on an API costs only electricity.
- **Offline.** Works on a plane.
- **Understanding.** You see directly how model size, quantisation and context length trade off against speed and quality. That intuition is hard to get any other way.
- **Control.** No model you depend on gets retired out from under you. You can fine-tune it, inspect it, and pin the exact version.

[Open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md) covers the bigger picture, and the [open-source stack explainer](../../explainers/ecosystem/open-source-stack.md) maps the tools.

## Step 1: Install Ollama

As of 2026-10, the official install methods are:

```bash
# Linux (and macOS, alternatively)
curl -fsSL https://ollama.com/install.sh | sh
```

```powershell
# Windows PowerShell
irm https://ollama.com/install.ps1 | iex
```

On macOS you can also download the app from [ollama.com/download](https://ollama.com/download). Piping a script from the internet into a shell runs it with your permissions; if that makes you uneasy (it is a reasonable instinct), download the script, read it, then run it.

Check it worked:

```bash
ollama --version
```

## Step 2: Run a model

```bash
ollama run gemma4:e4b
```

The first time, this downloads the model (several gigabytes, so expect a wait), then drops you into a chat prompt. Type a question. Type `/bye` to leave.

As of 2026-10, two good starting families in the Ollama library are:

| Model tag | Download size | Context | Notes |
|---|---|---|---|
| `gemma4:e2b` | about 4.6 to 7.5 GB | 128K | Google's small on-device variant; runs on most laptops |
| `gemma4:e4b` | about 6.6 to 9.5 GB | 128K | A good default on a 16 GB machine |
| `gemma4:12b` | about 8 GB | 256K | Noticeably stronger, still laptop-friendly |
| `gemma4:26b`, `gemma4:31b` | about 16 to 20 GB | 256K | Wants 24 GB or more of GPU or unified memory |
| `qwen3.5:4b` | about 3.3 to 4 GB | 256K | Alibaba's Qwen; text and image input |
| `qwen3.5:9b` | about 6.6 to 7.6 GB | 256K | Strong mid-size option |
| `qwen3.5:27b` | about 17 to 20 GB | 256K | Wants 24 GB or more |

Download sizes come from the Ollama library pages; the ranges reflect different quantisation variants. Useful commands:

```bash
ollama list            # models you have downloaded
ollama ps              # models currently loaded in memory
ollama pull qwen3.5:9b # download without starting a chat
ollama rm gemma4:31b   # delete a model to free disk space
```

Check each model's licence on its page before using it in a product. Many small open models are under permissive licences such as Apache 2.0, but not all, and some families have custom licences with conditions. The [Qwen](../../explainers/model-families/qwen.md), [Gemini and Gemma](../../explainers/model-families/gemini.md) and [Llama](../../explainers/model-families/llama.md) explainers cover the licence details for their families.

## Step 3: Which size can my machine run?

The model's weights must fit in fast memory, with room left over for the context (the [KV cache](../../explainers/concepts/kv-cache.md) grows with conversation length). A useful back-of-envelope calculation:

```
memory for weights  ~=  parameters x bytes per parameter

16-bit (unquantised):  2 bytes per parameter  -> 8B model ~= 16 GB
8-bit quantised:       1 byte                 -> 8B model ~=  8 GB
4-bit quantised:       0.5 bytes              -> 8B model ~=  4 GB

Add 10-30% for the runtime and a modest context window.
```

Most models in the Ollama library are distributed **quantised** to around 4 bits by default, which is why a model with billions of parameters downloads as a few gigabytes. Quantisation trades a little quality for a large saving in memory and speed; [Quantization and distillation](../concepts/quantization-and-distillation.md) and the [GPTQ and AWQ summary](../../papers/techniques/86-gptq-awq-quantization/summary.md) explain how.

Rough guide:

| Your hardware | Comfortable model sizes |
|---|---|
| 8 GB RAM laptop, no GPU | 1B to 4B; expect slow-ish replies |
| 16 GB RAM, or Apple Silicon with 16 GB | Up to about 12B |
| GPU with 12 to 16 GB VRAM | Up to about 14B at good speed |
| GPU with 24 GB, or Apple Silicon with 32 GB or more | 27B to 35B |
| Multiple GPUs or 64 GB or more unified memory | 70B-class and larger |

If a model does not fit in GPU memory, Ollama splits it between GPU and system RAM. It still runs, but much more slowly. If replies crawl, try the next size down. [GPUs for AI](../concepts/gpus-for-ai.md) explains why memory bandwidth, not just size, decides speed.

## Step 4: Call it from code

Ollama runs a local server on port 11434 with an API that copies OpenAI's. That means the OpenAI SDK works against it unchanged except for two settings:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",   # required by the SDK but ignored by Ollama
)

response = client.chat.completions.create(
    model="gemma4:e4b",
    messages=[
        {"role": "system", "content": "You answer in one short paragraph."},
        {"role": "user", "content": "What is the difference between RAM and VRAM?"},
    ],
)
print(response.choices[0].message.content)
```

This uses the Chat Completions format, which almost every local and hosted server supports. Make sure Ollama is running (the desktop app, or `ollama serve` in a terminal) and the model is pulled first.

The payoff: you can develop and test against a free local model, then switch `base_url` and `model` to a hosted provider when you need more capability, with the rest of your code unchanged. It also makes local models a cheap way to run large batches of simple tasks such as classification or tagging.

## Other tools worth knowing

- **LM Studio** ([lmstudio.ai](https://lmstudio.ai/)): a desktop app with a model browser and chat window. It can also run an OpenAI-compatible server, by default at `http://localhost:1234/v1`.
- **llama.cpp** ([github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)): the C/C++ inference engine that popularised running models on ordinary hardware, and the source of the GGUF model file format. Use it directly when you want maximum control.
- **vLLM and other inference servers:** for serving models to many users on a GPU server rather than one person on a laptop. See [Inference servers](../concepts/inference-servers.md), [Run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md), and the [PagedAttention/vLLM summary](../../papers/techniques/52-pagedattention-vllm/summary.md).

The [local LLM runners comparison](../../tools/comparisons/local-llm-runners.md) compares them side by side.

## What to expect from quality

Be honest with yourself about the gap. A small local model is excellent at summarising, rewriting, classifying, extracting fields and answering questions about text you give it. It is noticeably weaker than frontier hosted models at multi-step reasoning, hard coding tasks, long agent loops, and facts from memory, and it [hallucinates](../concepts/hallucinations.md) more. A good exercise: write ten prompts from your real work, run them on a local model and a hosted one, and judge where the difference matters for you.

## Common mistakes

- **Downloading the biggest model first.** It will not fit, will run from system RAM, and will feel broken. Start small and size up.
- **Forgetting the context costs memory.** A model that loads fine can slow down or fail with a very long prompt.
- **Comparing local models to frontier models on the hardest tasks only.** Test on what you actually need.
- **Ignoring licences.** "Open weights" does not always mean "use for anything". Read the model card.
- **Leaving the server open to the network.** By default Ollama listens on localhost. If you change that to share it, put authentication in front of it.

## Next steps

- [Your first LLM API call](first-llm-api-call.md): the hosted equivalent
- [Quantization and distillation](../concepts/quantization-and-distillation.md)
- [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md): adapt a local model to your task
- [ML engineer path](../start-here/ml-engineer-path.md)

## Sources

- Ollama, Linux download and install commands (read 2026-10-21): https://ollama.com/download/linux
- Ollama library, Gemma 4 tags and sizes (read 2026-10-21): https://ollama.com/library/gemma4
- Ollama library, Qwen3.5 tags and sizes (read 2026-10-21): https://ollama.com/library/qwen3.5
- Ollama, OpenAI compatibility (base URL `http://localhost:11434/v1/`, port 11434): https://docs.ollama.com/api/openai-compatibility
- LM Studio, OpenAI compatibility endpoints (`http://localhost:1234/v1`): https://lmstudio.ai/docs/developer/openai-compat
- llama.cpp repository: https://github.com/ggml-org/llama.cpp
