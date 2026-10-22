# AI Cost Basics

**In one line:** Turn "dollars per million tokens" into a cost per request, per user and per month for your own application, find which of the four prices on a price sheet dominates your bill, and know the five levers (model choice, caching, batching, trimming context, capping output) that cut it.
**Last reviewed:** 2026-10-21

---

> Assumes [LLM basics](llm-basics.md) and [Tokenization](../../explainers/concepts/tokenization.md). For why prices are falling and how providers set them, read the [inference economics explainer](../../explainers/compute/inference-economics.md); for the cost of building models, the [cost of training explainer](../../explainers/compute/cost-of-training.md). This page is about your bill.

## The short version

- Hosted models charge per **token**, roughly three-quarters of an English word. Prices are quoted **per million tokens (MTok)**, separately for **input** (everything you send) and **output** (everything the model writes). Output costs about five times input.
- A price sheet is really four prices: **input**, **output**, **cached input** (a repeated prompt prefix, at a tenth of the input price or less) and **batch** (about half price, results within hours). Your bill depends on the mix.
- For most chat and RAG apps, **input dominates**: the system prompt, retrieved documents, tool definitions and conversation history are resent on every call. For reasoning models, **output dominates**, because thinking tokens are billed as output.
- Cost per call = `input_tokens x input_price + output_tokens x output_price`, divided by a million. Multiply by calls per user and users per day. Do this on paper before you build.
- The five levers, roughly in order of impact: **pick a smaller model** where quality allows (often 10x to 20x), **cache** stable prefixes, **batch** anything not interactive, **trim context**, and **cap output and reasoning effort**.

## What you are billed for

Every API call has a token count on each side, and the response tells you both. Things that count as **input**:

- The system prompt, every time.
- The whole conversation so far: chat APIs are stateless, so turn 10 resends turns 1 to 9.
- Retrieved documents in a RAG app.
- Tool definitions (each tool's name, description and JSON schema), on every call where tools are enabled.
- Tool results fed back in an agent loop.
- Images, audio and PDFs, converted to tokens at rates the provider documents (a single image is often around a thousand tokens or more depending on size).

Things that count as **output**:

- The visible answer.
- **Reasoning or thinking tokens** on reasoning models, even when you do not see them in full. A short answer can carry thousands of thinking tokens. See the [reasoning models explainer](../../explainers/concepts/reasoning-models.md).
- Tool-call requests the model writes.

## Prices as of 2026-10-21

A sample from the providers' own pricing pages, US dollars per million tokens, standard (not batch) API. These change often; always check the source before you commit to a budget.

| Model | Input | Cached input (read) | Output | Source |
|---|---|---|---|---|
| Claude Opus 5.5 | $4.00 | $0.20 | $20.00 | Anthropic |
| Claude Sonnet 5.5 | $2.00 | $0.10 | $10.00 | Anthropic |
| Claude Haiku 5.5 (prompts up to 100K tokens) | $0.10 | $0.01 | $0.50 | Anthropic |
| gpt-6-astra | $10.00 | $1.00 | $50.00 | OpenAI |
| gpt-6.1-sol | $2.00 | $0.10 | $10.00 | OpenAI |
| gpt-6-luna | $0.10 | $0.01 | $0.50 | OpenAI |
| gemini-3.5-flash-lite | $0.30 | $0.03 | $2.50 | Google |

Notes that matter as much as the numbers:

- **Batch:** Anthropic, OpenAI and Google all list batch processing at 50% off input and output, with results returned asynchronously.
- **Cache writes cost extra.** On Anthropic, writing a prefix to the 5-minute cache costs 1.25x the normal input price and to the 1-hour cache 2x; reads then cost a small fraction. Caching pays off from the second hit. See [Prompt caching](prompt-caching.md).
- **Long-context and tier surcharges exist.** Claude Haiku 5.5 costs more on prompts over 100K tokens; OpenAI lists a long-context tier at 2x and a priority tier; Anthropic charges 1.1x for US-only inference. Read the footnotes.
- **Promotional prices expire.** Some current Google prices are introductory and double at a stated date.
- **Clouds resell the same models** (Amazon Bedrock, Google's Gemini Enterprise Agent Platform, Microsoft Foundry), sometimes at the same list price and sometimes with regional premiums. See [Cloud AI/ML services compared](../../tools/comparisons/cloud-ai-ml-services.md).

The spread is the headline. From the smallest to the largest model on that table, output prices differ by 100x. Model choice is the biggest cost decision you will make.

## A worked example

A customer-support assistant answers 2,000 conversations a day, about four model calls per conversation. Each call sends:

| Part of the prompt | Tokens |
|---|---|
| System prompt (instructions, policies, tone) | 2,000 |
| Retrieved help-centre passages | 3,000 |
| Conversation history (average) | 800 |
| The customer's new message | 100 |
| **Input total** | **5,900** |
| Answer (output) | 300 |

Here it is as code you can adapt:

```python
# Prices in USD per million tokens, as of 2026-10-21 (see Sources)
PRICES = {
    "claude-sonnet-5.5": {"in": 2.00, "out": 10.00, "cache_read": 0.10, "cache_write": 2.50},
    "claude-haiku-5.5":  {"in": 0.10, "out": 0.50,  "cache_read": 0.01, "cache_write": 0.125},
}

def cost_per_call(model, input_tokens, output_tokens, cached_tokens=0, cache_write_tokens=0):
    p = PRICES[model]
    uncached = input_tokens - cached_tokens - cache_write_tokens
    dollars = (uncached * p["in"] + cached_tokens * p["cache_read"]
               + cache_write_tokens * p["cache_write"] + output_tokens * p["out"])
    return dollars / 1_000_000

# A support assistant: 2,000 conversations a day, 4 model calls each
calls_per_day = 2_000 * 4
system, retrieved, history, question, answer = 2_000, 3_000, 800, 100, 300
inp = system + retrieved + history + question

for model in PRICES:
    plain = cost_per_call(model, inp, answer)
    cached = cost_per_call(model, inp, answer, cached_tokens=system)
    print(f"{model}: ${plain:.4f}/call  ${plain * calls_per_day * 30:,.0f}/month  "
          f"with cached system prompt ${cached * calls_per_day * 30:,.0f}/month")
```

```
claude-sonnet-5.5: $0.0148/call  $3,552/month  with cached system prompt $2,640/month
claude-haiku-5.5: $0.0007/call  $178/month  with cached system prompt $134/month
```

What the numbers teach:

1. **Input is 80% of the bill.** On Sonnet, 5,900 input tokens cost $0.0118 and 300 output tokens cost $0.0030. Shortening the answer barely matters; shortening the retrieved context matters a lot.
2. **Caching the system prompt saves about a quarter** with no quality change at all. (The example ignores the occasional cache write, which is small when traffic is steady.)
3. **The small model is 20x cheaper.** Whether you can use it is a quality question that only your [evals](evals-for-llms.md) can answer. A common design is a **router**: the small model handles routine questions and escalates hard ones to the larger model.
4. **Per conversation, not per call,** is the number the business understands: about 6 cents on Sonnet, under half a cent on Haiku. Compare that with what a human-handled ticket costs, and with what the feature earns.

Now change one assumption and watch it move. Switch to an agent that makes 12 calls per task with growing tool results, or a reasoning model that writes 4,000 thinking tokens per answer, and the cost per task rises by an order of magnitude. Always model the real loop, not a single call.

## The five levers

1. **Use the smallest model that passes your evals.** Test the cheap tier first and move up only when it fails specific cases. Route by difficulty. See [Which model for which job](../../tools/decisions/which-model-for-which-job.md) and [Small language models](small-language-models.md).
2. **Cache stable prefixes.** Put everything that does not change (instructions, tool definitions, reference documents) at the start of the prompt and mark it cacheable. [Prompt caching](prompt-caching.md) covers the rules that make hits happen.
3. **Batch what is not interactive.** Nightly classification, document extraction, eval runs and backfills belong on the batch API at half price.
4. **Send less context.** Retrieve five good passages instead of twenty mediocre ones, summarise old conversation turns, load tools only when needed. Better retrieval usually improves quality and cost together. See [Context windows and management](context-windows-and-management.md).
5. **Cap output and thinking.** Set `max_tokens`, ask for concise formats, and set the lowest reasoning effort or thinking budget that passes your evals.

[Cost and latency control](../../build/patterns/cost-and-latency-control.md) covers these as production patterns, with routing, caching layers and budgets.

## Hosted API or self-hosted?

Running an open-weight model on your own GPUs swaps a per-token price for a per-hour price. The GPU costs the same whether it is busy or idle, so self-hosting only wins when you can keep it busy: steady, high volume, or a hard requirement for data to stay on your hardware. At low or spiky volume a hosted API is almost always cheaper, because the provider batches your requests with everyone else's. Work it out as cost per million tokens actually served (GPU hourly price divided by tokens per hour at your real utilisation) and compare. [GPUs for AI](gpus-for-ai.md), [Inference servers](inference-servers.md) and the [LLM serving decision](../../tools/decisions/llm-serving.md) help with the inputs.

## Hidden costs that are not tokens

- **Embeddings and vector storage** for RAG (usually small next to generation).
- **Grounding and search tools** priced per query (Google lists search grounding per 1,000 queries).
- **Evals and development**: every prompt change re-run across your eval set is real money. Use the batch API for it.
- **Observability** tooling and log storage.
- **People**: reviewing outputs, labelling, maintaining prompts. Often the largest line.

## Common mistakes

- **Pricing a single call** instead of a whole task. Agents and multi-turn chats multiply calls and resend context every time.
- **Ignoring reasoning tokens.** Check `usage` in the response; thinking is billed as output.
- **Budgeting from the playground.** Real traffic has longer documents, longer conversations and retries.
- **Forgetting the conversation grows.** Turn 20 costs far more than turn 1 unless you trim or summarise history.
- **No spend limits.** Set a monthly cap and alerts in the provider console from day one; see [API keys and environment variables](../day-one/api-keys-and-env-vars.md).
- **Optimising cost before quality.** A cheap answer that is wrong costs more downstream. Measure quality first, then cut cost without letting the eval score drop.

## Next steps

- [Prompt caching](prompt-caching.md) and [Cost and latency control](../../build/patterns/cost-and-latency-control.md)
- [Inference economics explainer](../../explainers/compute/inference-economics.md): why prices fall and how they are set
- [Measuring AI ROI](../../work/enablement/measuring-ai-roi.md): putting the cost next to the value
- [LLMOps and observability](../../build/patterns/llmops-observability.md): tracking cost per request in production
- For cloud billing, budgets and FinOps in general, see the sibling site [Cloud Zero to Hero](https://cloud.noblerworks.com/)

## Sources

- Anthropic, "Pricing" (Claude model prices, cache multipliers, batch 50%, long-context and US-only inference rates), read 2026-10-21: https://platform.claude.com/docs/en/about-claude/pricing
- OpenAI, "Pricing" (GPT-6 family, cached input, batch, long-context and priority tiers), read 2026-10-21: https://developers.openai.com/api/docs/pricing
- Google, "Gemini Developer API pricing", table-checked 2026-10-22 (3.5 Flash-Lite standard and batch; Gemini 4 Argon and 3.8 Flash promo prices and end dates): https://ai.google.dev/gemini-api/docs/pricing
- Google Cloud, "Generative AI pricing" on Gemini Enterprise Agent Platform (grounding prices), read 2026-10-21: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing
- Calculator output above produced on 2026-10-21 from the Anthropic prices listed.
