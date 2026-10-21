# Local LLM Runners Compared

**In one line:** To run open-weight models on your own machine, use Ollama for the easiest command-line start, LM Studio for a point-and-click app, llama.cpp for maximum control on modest hardware, and vLLM when you are serving many users from a GPU server.
**Last reviewed:** 2026-10-21

---

## The short version

- Running a model locally means **no per-token bill, no data leaving your machine, and it works offline**. The price is that local models are smaller and weaker than frontier APIs, and you need enough memory.
- **Memory is the constraint.** A rough rule: a model quantised to 4 bits needs a bit over half a gigabyte of RAM or VRAM per billion parameters, plus room for the context. A 7-8B model runs on most recent laptops; 30B-class models want 24 GB or more; 70B-class models need a workstation or server.
- **Ollama**: one command to download and run a model, with a local API. **LM Studio**: a desktop app with a model browser and chat UI. **llama.cpp**: the engine underneath much of this, for people who want every knob. **vLLM**: a high-throughput server for GPUs, not a desktop tool.
- All four can expose an **OpenAI-compatible API**, so code written for a hosted API can often point at your local model by changing the base URL.
- First time? Follow [run a model locally](../../learn/day-one/run-a-model-locally.md), then come back here to choose for real use.

## The options (as of 2026-10)

| Runner | What it is | Platforms | Interface | Licence | Best for |
|---|---|---|---|---|---|
| **Ollama** | Model manager and runtime with a simple CLI and local API | macOS, Windows, Linux, Docker | CLI, REST API on port 11434, OpenAI-compatible endpoint, Python library `ollama` | MIT | Developers who want the fastest path from zero to a local API |
| **LM Studio** | Desktop app: browse, download and chat with models | Apple Silicon Macs, x64/ARM64 Windows, x64 Linux | GUI, local OpenAI-compatible server, `lms` CLI | Free download; check its terms of use | Non-developers and anyone who prefers a GUI; uses MLX on Apple Silicon as well as llama.cpp |
| **llama.cpp** | C/C++ inference engine for GGUF models | Everything: CPU, NVIDIA CUDA, Apple Metal, Vulkan, AMD, Intel | `llama-cli`, `llama-server` (OpenAI-compatible, with a web UI) | MIT | Tinkerers, edge devices, squeezing big models into limited memory with CPU+GPU hybrid inference |
| **vLLM** | Production inference server using PagedAttention and continuous batching | Linux with NVIDIA (and some other) GPUs | `vllm serve`, OpenAI-compatible API | Apache 2.0 | Serving many concurrent users from one or more GPUs |

Other names you will meet: **Apple MLX** (Apple's array framework, fast on Apple Silicon), **Jan** (an open-source desktop chat app), **SGLang** and **TensorRT-LLM** (server-side engines alongside vLLM). For server-side choices in depth, see [LLM serving](../decisions/llm-serving.md) and [inference servers](../../learn/concepts/inference-servers.md).

## How much hardware do you need?

Model weights dominate memory. At 16-bit precision each parameter takes 2 bytes; quantising to 4 bits takes about half a byte. Add 10 to 30% for the runtime and the [KV cache](../../explainers/concepts/kv-cache.md), which grows with context length.

| Model size | 4-bit weights (approx.) | Runs comfortably on | Feels like |
|---|---|---|---|
| 1-4B | 1-3 GB | Any recent laptop, many phones | Quick helper; weak reasoning |
| 7-9B | 4-6 GB | 16 GB laptop, Apple Silicon Mac, 8 GB GPU | Decent chat, summaries, simple code |
| 12-14B | 7-9 GB | 16-32 GB Mac, 12-16 GB GPU | Noticeably better |
| 27-35B | 15-20 GB | 32 GB+ Mac, 24 GB GPU | Good general model |
| 70B-class | 35-45 GB | 64 GB+ Mac, two 24 GB GPUs, or a 48 GB+ GPU | Strong, slow on consumer hardware |
| Mixture-of-experts, 100B+ total | Varies; all weights must fit even if few are active per token | Workstations and servers | Frontier-adjacent open models |

These are rules of thumb from the arithmetic above, not measurements. Apple Silicon Macs are popular here because CPU and GPU share one large memory pool. Background: [quantization and distillation](../../learn/concepts/quantization-and-distillation.md), [GPTQ and AWQ](../../papers/techniques/86-gptq-awq-quantization/summary.md), [QLoRA](../../papers/techniques/22-qlora/summary.md), [mixture of experts](../../papers/architectures/37-mixture-of-experts/summary.md), [GPUs for AI](../../learn/concepts/gpus-for-ai.md) and the [AI hardware landscape](../../explainers/compute/ai-hardware-landscape.md).

## Getting started with each

**Ollama**

```bash
curl -fsSL https://ollama.com/install.sh | sh     # Linux; macOS and Windows have installers
ollama run gemma4                                  # downloads, then opens a chat
```

Use it from code through the OpenAI-compatible endpoint:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")  # key is required but ignored
resp = client.chat.completions.create(
    model="gemma4",
    messages=[{"role": "user", "content": "Explain RAG in two sentences."}],
)
print(resp.choices[0].message.content)
```

Model names change as new open models arrive; browse the Ollama library for current ones (it carries families such as Gemma, Qwen, Llama, DeepSeek and gpt-oss as of 2026-10).

**LM Studio:** install the app, search for a model, pick a quantisation that fits your memory (the app flags what fits), and chat. Turn on the local server to use it from code.

**llama.cpp:** install via Homebrew, Winget, a release binary, or build from source. Then `llama-server -m model.gguf` (or point it at a Hugging Face model) gives you an OpenAI-compatible server and a web UI. You choose context size, GPU layers, threads and quantisation precisely.

**vLLM:** on a Linux GPU box, `pip install vllm` then `vllm serve <hugging-face-model-id>`. It shines when many requests arrive at once, thanks to [PagedAttention](../../papers/techniques/52-pagedattention-vllm/summary.md). See [run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md).

## Pick X if...

- **Pick Ollama if** you are a developer who wants a local model behind an API in five minutes, or you want to script model downloads.
- **Pick LM Studio if** you want a friendly app, are on a Mac and want MLX speed, or are helping non-technical colleagues run models privately.
- **Pick llama.cpp if** you need the most control, are running on unusual hardware, or want to split a model between CPU and GPU.
- **Pick vLLM if** you are serving a team or an application with concurrent users from a GPU server. It is not aimed at laptops.

## Local vs API: when local makes sense

| Local wins | API wins |
|---|---|
| Data must not leave the device or network | You need the strongest available model |
| Offline or air-gapped use | You do not want to manage hardware |
| High-volume, simple tasks where small models are good enough | Bursty or low volume (you pay only for use) |
| Learning how models actually work | Long context, multimodal, tool use at frontier quality |

Open-weight models and how they compare are covered in [open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md) and the family pages for [Llama](../../explainers/model-families/llama.md), [Qwen](../../explainers/model-families/qwen.md), [Mistral](../../explainers/model-families/mistral.md) and [DeepSeek](../../explainers/model-families/deepseek.md).

## Common mistakes

- **Downloading a model that does not fit.** It will swap to disk and crawl. Check size against free memory first.
- **Expecting frontier quality from a 7B model.** Use local models for tasks they handle well; test before you rely on them.
- **Tiny default context.** Some runners default to a short context window; long documents get silently truncated. Set it explicitly.
- **Exposing the local server to the network.** Local APIs usually have no authentication. Keep them bound to localhost unless you add a proxy with auth.
- **Ignoring licences.** "Open weights" licences differ; some restrict commercial use or large companies. Read the model's licence.
- **Unvetted model files.** Download from reputable sources; see [model supply chain](../../safety/security/model-supply-chain.md).

## Next steps

- [Run a model locally](../../learn/day-one/run-a-model-locally.md) (beginner walkthrough)
- [LLM serving decision guide](../decisions/llm-serving.md) for production
- [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md) to adapt a local model
- [Open-source stack](../../explainers/ecosystem/open-source-stack.md)

## Sources

- Ollama repository (MIT, platforms, install, `ollama run`, port 11434, Python library; as of 2026-10): https://github.com/ollama/ollama
- Ollama, OpenAI compatibility (base URL, Python example): https://docs.ollama.com/api/openai-compatibility
- LM Studio docs (platforms, MLX on Apple Silicon, OpenAI-compatible API, `lms` CLI): https://lmstudio.ai/docs/app
- llama.cpp repository (MIT, `llama-cli`, `llama-server`, GGUF, backends, install options): https://github.com/ggml-org/llama.cpp
- vLLM documentation: https://docs.vllm.ai/
- Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (2023): https://arxiv.org/abs/2309.06180
