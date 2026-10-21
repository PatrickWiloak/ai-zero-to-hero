# Your First LLM API Call

**In one line:** Send a prompt to a hosted language model from code and read the answer - the same request with curl, the Anthropic Python SDK and the OpenAI Python SDK - then add a system prompt, a conversation, streaming and a cost estimate.
**Last reviewed:** 2026-10-21

---

## The short version

- A model API call is an HTTPS request: you send JSON with a **model name**, your **messages**, and a few settings; you get back JSON with the model's reply and a count of **tokens** used.
- The API is **stateless**. The model remembers nothing between calls. To have a conversation, you resend the whole message history every time.
- You pay per token, separately for input (what you send) and output (what the model writes). Output tokens cost several times more than input tokens.
- Use the official SDK for your language. It handles authentication, retries and response parsing. Drop to curl when you want to see exactly what goes over the wire.
- Model names change often. Copy the current ID from the provider's models page rather than from an old tutorial. The IDs below are correct as of 2026-10.

## Before you start

You need: Python 3.10 or newer in a virtual environment ([Python for AI](python-for-ai.md)), and an API key in an environment variable ([API keys and environment variables](api-keys-and-env-vars.md)). Install both SDKs:

```bash
pip install anthropic openai
```

API use is billed per token and is separate from any chat subscription. Every example on this page costs a fraction of a cent.

## Choosing a model for your first calls

Providers sell models in tiers: a large, most-capable model and smaller, faster, cheaper ones. As of 2026-10:

| Provider | Model IDs (largest to smallest) | Price per million tokens, input / output |
|---|---|---|
| Anthropic | `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5` | $10/$50, $4/$20, $2/$10, from $0.10/$0.50 |
| OpenAI | `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna` | $10/$50, $2/$10, $0.10/$0.50 |

For learning, start with a small model. It is fast, cheap, and good enough to see how everything works. Move up a tier when a task needs it. [Which model for which job](../../tools/decisions/which-model-for-which-job.md) goes deeper.

## The request, in raw HTTP

Seeing the raw request once makes every SDK make sense. Here is a call to Anthropic's Messages API with curl:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-haiku-5-5",
    "max_tokens": 300,
    "messages": [
      {"role": "user", "content": "In two sentences, what is a token in a language model?"}
    ]
  }'
```

The reply is JSON. Trimmed, it looks like this:

```json
{
  "id": "msg_01...",
  "type": "message",
  "role": "assistant",
  "model": "claude-haiku-5-5",
  "content": [
    {"type": "text", "text": "A token is a chunk of text, often part of a word, ..."}
  ],
  "stop_reason": "end_turn",
  "usage": {"input_tokens": 21, "output_tokens": 48}
}
```

Four fields carry the meaning:

- `content` is a **list of blocks**, not a single string. For a plain answer it holds one `text` block. Other block types (tool calls, thinking) appear in more advanced use, which is why code loops over the blocks and picks the text.
- `stop_reason` says why the model stopped. `end_turn` means it finished. `max_tokens` means it ran into your limit mid-answer; raise `max_tokens` if you see that.
- `usage` is what you are billed for.
- `max_tokens` in the request is a **ceiling** on output length, not a target.

OpenAI's equivalent uses its Responses API, a different URL and header, and a simpler input field:

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-6-luna",
    "input": "In two sentences, what is a token in a language model?"
  }'
```

The shapes differ in detail but the idea is identical: model, input, settings in; text and usage out.

## The same call with the Anthropic Python SDK

Save as `first_call.py` and run with `python first_call.py`:

```python
import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "In two sentences, what is a token in a language model?"}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print(response.stop_reason, response.usage.input_tokens, response.usage.output_tokens)
```

## The same call with the OpenAI Python SDK

```python
from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY from the environment

response = client.responses.create(
    model="gpt-6-luna",
    input="In two sentences, what is a token in a language model?",
)

print(response.output_text)
print(response.usage)
```

`output_text` is a convenience property that joins the text parts of the reply for you.

## Adding a system prompt

A **system prompt** sets the model's role, rules and tone for the whole conversation. It is the single most useful setting you have. With Anthropic it is a separate `system` parameter; with OpenAI's Responses API it is `instructions`:

```python
response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    system="You are a patient tutor for complete beginners. Use one everyday analogy. No jargon.",
    messages=[{"role": "user", "content": "What is a token in a language model?"}],
)
```

```python
from openai import OpenAI

openai_client = OpenAI()
response = openai_client.responses.create(
    model="gpt-6-luna",
    instructions="You are a patient tutor for complete beginners. Use one everyday analogy. No jargon.",
    input="What is a token in a language model?",
)
```

Run both with and without the system prompt and compare. [Prompt engineering](../concepts/prompt-engineering.md) covers how to write good ones.

## Having a conversation

The model has no memory between calls. A chat app works by keeping the history in a list and sending all of it every turn:

```python
import anthropic

client = anthropic.Anthropic()
history = []

def chat(user_text):
    history.append({"role": "user", "content": user_text})
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        system="You are a concise assistant.",
        messages=history,
    )
    reply = "".join(b.text for b in response.content if b.type == "text")
    history.append({"role": "assistant", "content": reply})
    return reply

print(chat("My name is Sam and I am learning about embeddings."))
print(chat("What did I say I was learning about?"))   # works because we resent the history
```

Two consequences follow. First, every turn costs more than the last, because the input grows. Second, eventually the history outgrows the model's **context window**. [Context windows](../../explainers/concepts/context-windows.md) and [Context windows and management](../concepts/context-windows-and-management.md) explain what to do about that, and [Prompt caching](../concepts/prompt-caching.md) shows how to make the repeated prefix much cheaper.

## Streaming

For anything a person waits on, stream the reply so text appears as it is generated instead of all at once after several seconds:

```python
with client.messages.stream(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Write a four-line poem about gradient descent."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
```

The OpenAI SDK has the equivalent with `stream=True` on `responses.create`, yielding events you iterate over.

## Working out the cost

Every response tells you the tokens used, so you can compute the exact cost. With the prices from the table above:

```python
PRICES = {  # dollars per million tokens, as of 2026-10
    "claude-haiku-5-5": (0.10, 0.50),   # "from" price; check the pricing page
    "claude-sonnet-5-5": (2.00, 10.00),
}

def cost(model, usage):
    in_price, out_price = PRICES[model]
    return (usage.input_tokens * in_price + usage.output_tokens * out_price) / 1_000_000

print(f"${cost('claude-sonnet-5-5', response.usage):.6f}")
```

A typical question and answer of a few hundred tokens costs well under a cent on a small model. Costs grow with long documents, long conversations and agent loops that make many calls, which is why production systems log tokens on every request. [Inference economics](../../explainers/compute/inference-economics.md) explains why prices are structured this way.

## When it fails

| Error | What it means | Fix |
|---|---|---|
| 401 / authentication error | Key missing, wrong, or revoked | Check the environment variable is set in *this* terminal |
| 404 / model not found | Model ID wrong or retired | Copy the current ID from the provider's models page |
| 400 / invalid request | Malformed request | Read the error message; it usually names the bad field |
| 429 / rate limited | Too many requests or tokens per minute | Wait and retry; the SDKs retry automatically a couple of times |
| 5xx / overloaded | Provider-side problem | Retry with backoff |
| `stop_reason: max_tokens` | Answer was cut off | Raise `max_tokens` |

## Try this next

1. Ask the same question to a small and a large model and compare quality, speed and cost.
2. Ask for JSON with three named fields, then parse it with `json.loads`. Then read [Structured outputs](../concepts/structured-outputs.md) for the reliable way.
3. Send the contents of a text file and ask for a summary.
4. Point the OpenAI SDK at a model on your own laptop ([Run a model locally](run-a-model-locally.md)) and run the same code with no API bill.
5. Build the full version: [Chatbot in an afternoon](../../build/projects/chatbot-in-an-afternoon.md).

## Common mistakes

- **Copying model IDs from old tutorials.** They get retired. Check the models page.
- **Expecting the model to remember.** It does not. Resend the history.
- **Reading `content` as a string.** In the Anthropic API it is a list of blocks; loop over them and take the `text` ones.
- **Setting `max_tokens` too low.** The answer gets cut off silently except for `stop_reason`. Check it.
- **Not logging token usage.** You will want it the first time a bill surprises you.
- **Calling the API from browser code.** That exposes your key. Call it from a server.

## Next steps

- [Prompt engineering](../concepts/prompt-engineering.md)
- [Tool use and function calling](../concepts/tool-use-and-function-calling.md): letting the model call your code
- [Run a model locally](run-a-model-locally.md)
- [AI engineer path](../start-here/ai-engineer-path.md)
- The model families behind these IDs: [Claude](../../explainers/model-families/claude.md), [GPT](../../explainers/model-families/gpt.md), [Gemini](../../explainers/model-families/gemini.md)

## Sources

- Anthropic, "Get started with Claude" (endpoint, headers, `anthropic-version: 2023-06-01`, Python example; read 2026-10-21): https://platform.claude.com/docs/en/get-started
- Anthropic, Models overview (model IDs and prices as of 2026-10): https://platform.claude.com/docs/en/about-claude/models/overview
- Anthropic, Streaming messages: https://platform.claude.com/docs/en/build-with-claude/streaming
- OpenAI, "Developer quickstart" (Responses API, curl and Python examples; read 2026-10-21): https://developers.openai.com/api/docs/quickstart
- OpenAI, Models page (model IDs and prices as of 2026-10): https://developers.openai.com/api/docs/models
