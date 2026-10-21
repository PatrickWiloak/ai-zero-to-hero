# Python for AI

**In one line:** The small slice of Python you need to start building with AI - installing it, virtual environments, packages, the core data types, functions, files and JSON - taught through one worked example that ends in a real model call.
**Last reviewed:** 2026-10-21

---

## The short version

- Python is the default language of AI. The official SDKs for Anthropic, OpenAI and Google, the main ML frameworks, and almost every tutorial use it. TypeScript is a strong second for web apps.
- You do not need all of Python. You need: variables, strings, lists, dictionaries, `if`, `for`, functions, reading files, JSON, installing packages, and virtual environments. That is roughly a weekend.
- Install a recent Python 3 (as of 2026-10 the Anthropic and OpenAI Python SDKs need **3.10 or newer**), and always work inside a **virtual environment** so each project has its own packages.
- The data shape you will see everywhere is **a list of dictionaries**. A conversation with a model is a list of `{"role": ..., "content": ...}` dictionaries, and most API responses are JSON that Python turns into dictionaries.
- Learn by typing, not reading. Every snippet on this page runs; change it and run it again.

## Step 1: Install Python and check it

On macOS and Linux, Python 3 is often already installed. Open a terminal and run:

```bash
python3 --version
```

If you see `Python 3.10` or higher, you are set. If not, install the latest stable release from [python.org](https://www.python.org/downloads/) (Windows and macOS installers), or with your system package manager on Linux. On Windows, tick "Add python.exe to PATH" in the installer, then use `python` instead of `python3` in the commands below.

If you would rather not install anything yet, use a hosted notebook: [Notebooks and Colab](notebooks-and-colab.md) runs Python in your browser. Come back here when you want to work locally.

## Step 2: Make a project with a virtual environment

A **virtual environment** is a private folder of packages for one project. Without one, installing packages for project A can break project B. Make one per project; it takes ten seconds.

```bash
mkdir my-first-ai-project
cd my-first-ai-project
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python --version                 # now "python" points at the venv
```

Your prompt now starts with `(.venv)`. Anything you `pip install` goes into `.venv/` and nowhere else. To leave, type `deactivate`. When you come back to the project, run the `activate` line again.

Install the packages you will use on this site:

```bash
pip install anthropic openai python-dotenv
```

To record what you installed so someone else (or future you) can recreate the environment:

```bash
pip freeze > requirements.txt
# later, on another machine:
pip install -r requirements.txt
```

There are faster tools for this (`uv` is popular), and you can switch to them later. The ideas are the same.

## Step 3: The data types you will actually use

Create a file called `basics.py`, paste this in, and run it with `python basics.py`.

```python
# Strings: text. f-strings let you drop variables into text.
name = "Ada"
topic = "transformers"
prompt = f"Explain {topic} to {name} in two sentences."
print(prompt)

# Numbers
price_per_million_tokens = 3.00
tokens_used = 1_250
cost = tokens_used / 1_000_000 * price_per_million_tokens
print(f"Cost: ${cost:.6f}")

# Lists: ordered collections
models = ["model-small", "model-medium", "model-large"]
print(models[0])          # first item
print(len(models))        # how many
models.append("model-local")

# Dictionaries: key -> value lookups. This is what JSON becomes.
message = {"role": "user", "content": "Hello!"}
print(message["role"])
print(message.get("missing_key", "default value"))

# A list of dictionaries: the shape of every chat conversation
conversation = [
    {"role": "user", "content": "What is an embedding?"},
    {"role": "assistant", "content": "A list of numbers that represents meaning."},
    {"role": "user", "content": "Give me an example."},
]
for turn in conversation:
    print(f"{turn['role']:>9}: {turn['content']}")
```

The last block is worth staring at. When you call a model API, you send exactly this kind of list, and the model replies with the next `assistant` turn. [Your first LLM API call](first-llm-api-call.md) uses it directly.

## Step 4: Control flow and functions

```python
def estimate_cost(input_tokens, output_tokens, input_price, output_price):
    """Return the cost in dollars. Prices are per million tokens."""
    return (input_tokens * input_price + output_tokens * output_price) / 1_000_000


requests = [
    {"id": 1, "input_tokens": 1200, "output_tokens": 300},
    {"id": 2, "input_tokens": 54000, "output_tokens": 900},
    {"id": 3, "input_tokens": 800, "output_tokens": 2500},
]

total = 0.0
for r in requests:
    c = estimate_cost(r["input_tokens"], r["output_tokens"], 3.00, 15.00)
    total += c
    if c > 0.05:
        print(f"Request {r['id']} is expensive: ${c:.4f}")

print(f"Total: ${total:.4f}")
```

Three ideas here carry most programs: a **function** (`def`) packages a calculation you will reuse, a **loop** (`for`) does something to each item, and a **condition** (`if`) chooses. The prices in this example are made up; real ones are on each provider's pricing page.

A **list comprehension** is a compact loop you will see in every codebase:

```python
expensive_ids = [r["id"] for r in requests if r["output_tokens"] > 1000]
print(expensive_ids)   # [3]
```

## Step 5: Files and JSON

Models read text, and you will constantly read text from files and write results back.

```python
import json
from pathlib import Path

# Write a text file, then read it back
Path("notes.txt").write_text("Meeting moved to Thursday. Bring the Q3 numbers.")
text = Path("notes.txt").read_text()
print(text)

# JSON: the format APIs speak
record = {"task": "summarise", "input_file": "notes.txt", "max_words": 20}
Path("job.json").write_text(json.dumps(record, indent=2))

loaded = json.loads(Path("job.json").read_text())
print(loaded["task"], loaded["max_words"])
```

`json.dumps` turns a Python dictionary into a JSON string; `json.loads` turns JSON text back into a dictionary. When you ask a model for [structured output](../concepts/structured-outputs.md), you will `json.loads` its answer.

## Step 6: Errors and how to read them

Your code will fail. That is normal. Python tells you where and why, at the **bottom** of the message:

```text
Traceback (most recent call last):
  File "basics.py", line 12, in <module>
    print(message["model"])
KeyError: 'model'
```

Read the last line first (`KeyError: 'model'`: you asked a dictionary for a key it does not have), then the line number above it. The most common beginner errors in AI code:

- `ModuleNotFoundError: No module named 'anthropic'`: you are not in your virtual environment, or did not `pip install` the package. Run `source .venv/bin/activate`.
- `KeyError`: you guessed the shape of a response wrong. `print()` the whole object and look.
- An authentication error from an API: your key is missing or wrong. See [API keys and environment variables](api-keys-and-env-vars.md).

When you call APIs over the network, wrap the call so one failure does not crash a batch job:

```python
try:
    result = risky_call()
except Exception as e:
    print(f"Failed: {e}")
```

In real code, catch the specific error types the SDK provides, not every exception.

## Step 7: Put it together

Here is a complete small program that uses everything above: it reads a file, builds a prompt, calls a model, and saves the result as JSON. It needs an API key set up first ([API keys and environment variables](api-keys-and-env-vars.md)); if you do not have one yet, read it now and run it later.

```python
import json
from pathlib import Path

import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment


def summarise(text: str, max_words: int = 50) -> str:
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"Summarise this in at most {max_words} words:\n\n{text}",
        }],
    )
    return "".join(block.text for block in response.content if block.type == "text")


source = Path("notes.txt").read_text()
summary = summarise(source, max_words=15)
Path("summary.json").write_text(json.dumps({"source": "notes.txt", "summary": summary}, indent=2))
print(summary)
```

The model ID `claude-haiku-5-5` is Anthropic's smallest current model as of 2026-10; model names change, so check the provider's models page if this one is rejected. [Your first LLM API call](first-llm-api-call.md) explains each line and shows the OpenAI equivalent.

## What to learn next, and what to skip for now

**Next, when you need them:** `async`/`await` for making many API calls at once; `pandas` for tables; `requests` or `httpx` for calling any web API; type hints and `pydantic` for validating structured outputs; `pytest` for testing.

**Skip for now:** classes and inheritance beyond the basics, decorators, metaclasses, packaging your own library. You can build a great deal without them.

## Common mistakes

- **Installing packages globally.** Leads to "it works on my machine" and version conflicts. Always activate a virtual environment first.
- **Pasting API keys into code.** It ends up in Git, then on GitHub, then in someone else's bill. Use environment variables.
- **Mixing up `python` and `python3`, `pip` and `pip3`.** Inside an activated venv, `python` and `pip` are always the right ones.
- **Not printing things.** When unsure what a variable holds, `print(variable)` or `print(type(variable))`. Professionals do this constantly.
- **Copying code you do not understand into a project you will maintain.** It is fine to copy to learn; then rewrite it in your own words.

## Next steps

- [Notebooks and Colab](notebooks-and-colab.md)
- [API keys and environment variables](api-keys-and-env-vars.md)
- [Your first LLM API call](first-llm-api-call.md)
- The command-line, Git and HTTP basics on the sibling site's [Day One](https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/learn/day-one/) section

## Sources

- Python downloads: https://www.python.org/downloads/
- Python tutorial (official): https://docs.python.org/3/tutorial/
- `venv` documentation: https://docs.python.org/3/library/venv.html
- PyPI, `anthropic` package (Requires-Python >=3.10, read 2026-10-21): https://pypi.org/project/anthropic/
- PyPI, `openai` package (Requires-Python >=3.10, read 2026-10-21): https://pypi.org/project/openai/
- Anthropic, Models overview (model IDs, as of 2026-10): https://platform.claude.com/docs/en/about-claude/models/overview
