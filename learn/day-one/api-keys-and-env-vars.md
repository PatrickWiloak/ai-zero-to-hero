# API Keys and Environment Variables

**In one line:** How to get an API key for a model provider, store it in an environment variable or `.env` file instead of your code, keep it out of Git, cap what it can cost you, and what to do in the first ten minutes if one leaks.
**Last reviewed:** 2026-10-21

---

## The short version

- An **API key** is a password that lets a program spend money on your account. Treat it exactly like a credit card number.
- Never put a key in your source code, a notebook cell, a screenshot, or a chat message. Put it in an **environment variable**, which your code reads at run time.
- The official SDKs look for standard variable names automatically: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`. Set the variable and the client finds it.
- For local projects, keep keys in a `.env` file and add `.env` to `.gitignore` **before your first commit**.
- In each provider's console, set a **spending limit** and create **one key per project** so you can revoke one without breaking the others.
- If a key leaks, **revoke it first**, then investigate. Keys pushed to public GitHub are found by automated scanners quickly.

## Why this matters more for AI

Most beginner API keys guard something free or cheap. Model API keys guard pay-per-use compute, and a leaked key can be used to run large volumes of requests on your account until you notice. Developers who have accidentally published keys commonly report unexpected charges before they caught it. The habits on this page cost five minutes to set up and remove that risk.

## Step 1: Get a key

Each provider has a developer console separate from its consumer chat app. A paid chat subscription (Claude Pro, ChatGPT Plus and so on) does **not** include API access; the API is billed separately, per token.

| Provider | Console | Variable the SDK reads |
|---|---|---|
| Anthropic (Claude) | [platform.claude.com](https://platform.claude.com/) | `ANTHROPIC_API_KEY` |
| OpenAI (GPT) | [platform.openai.com](https://platform.openai.com/) | `OPENAI_API_KEY` |
| Google (Gemini) | [Google AI Studio](https://aistudio.google.com/) | `GEMINI_API_KEY` |

In each console, find the API keys page, create a key, give it a name that says what it is for (`laptop-learning`, `rag-demo`), and copy it. **You usually see the full key only once.** If you lose it, delete it and make a new one.

While you are in the console:

- **Add a spending limit or budget alert.** Each console has billing settings for this. Set a low limit while you are learning.
- **Note the rate limits** for your account tier, so you recognise a "429 Too Many Requests" error when you see one.

## Step 2: What an environment variable is

Every running program inherits a set of named text values from the shell that started it: its **environment**. `PATH` and `HOME` are environment variables you already have. Your API key can be one too. The code then asks for it by name, and the key itself never appears in a file you share.

Set one for the current terminal session:

```bash
# macOS / Linux
export ANTHROPIC_API_KEY="sk-ant-...your key..."
echo $ANTHROPIC_API_KEY | cut -c1-10   # check it is set without printing all of it
```

```powershell
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-...your key..."
```

This lasts until you close the terminal. You can add the `export` line to your shell profile (`~/.bashrc`, `~/.zshrc`) to make it permanent, but per-project `.env` files (next step) are tidier once you have more than one project.

Then any Python started from that terminal can read it:

```python
import os
key = os.environ.get("ANTHROPIC_API_KEY")
print("key is set" if key else "key is MISSING")
```

You rarely need even that. The SDK clients read the standard variable for you:

```python
import anthropic
client = anthropic.Anthropic()      # finds ANTHROPIC_API_KEY on its own

from openai import OpenAI
client = OpenAI()                   # finds OPENAI_API_KEY on its own
```

## Step 3: A `.env` file per project

A `.env` file is a plain text file of `NAME=value` lines that lives in your project folder:

```text
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

Load it at the top of your program with the `python-dotenv` package (`pip install python-dotenv`):

```python
from dotenv import load_dotenv
load_dotenv()   # copies the .env values into the environment

import anthropic
client = anthropic.Anthropic()
```

Now the critical part. **Before your first commit**, tell Git to ignore the file:

```bash
echo ".env" >> .gitignore
git status        # .env must NOT appear in the list
```

It is also good practice to commit a `.env.example` with the names but not the values, so others know which variables to set:

```text
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
```

## Step 4: Keys in other places

- **Colab:** use the Secrets panel, described in [Notebooks and Colab](notebooks-and-colab.md).
- **curl:** reference the variable, never the literal key, so the key stays out of your shell history:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-haiku-5-5", "max_tokens": 200,
       "messages": [{"role": "user", "content": "Say hello"}]}'
```

- **Deployed apps:** use your platform's secret store (GitHub Actions secrets, AWS Secrets Manager or SSM Parameter Store, Google Secret Manager, Azure Key Vault, or your host's environment settings). The code still reads an environment variable; only where the value comes from changes.
- **Browsers and mobile apps:** **never ship a key to a client device.** Anything in front-end JavaScript or an app bundle can be extracted. Put a small server in between that holds the key and calls the model on the user's behalf, with its own authentication and per-user limits.

## Step 5: Limit the blast radius

Assume a key will leak one day and make that day boring:

- **One key per project and per environment.** Revoke one without touching the others.
- **Spending limits** on the account, set low while learning.
- **Workspaces or projects** in the provider console where available, to separate budgets and keys for different apps.
- **Rotate** long-lived keys periodically: create a new one, deploy it, then delete the old one.
- **Check usage dashboards** now and then. An unexplained spike is the first sign of a leak.

## If a key leaks

Do these in order. Speed matters more than understanding.

1. **Revoke the key** in the provider console. Do this first, before investigating.
2. **Create a new key** and update wherever it is used.
3. **Check usage and billing** for activity you did not cause. Contact the provider's support if you see any.
4. **Remove it from history.** Deleting the line in a new commit is not enough; the key is still in Git history. Since the key is already revoked this is now hygiene rather than urgent, but tools like `git filter-repo` can rewrite history if needed.
5. **Turn on secret scanning.** GitHub's push protection blocks pushes that contain recognised secret formats, and secret scanning alerts on ones that slipped through.

## Common mistakes

- **Committing `.env`.** Add it to `.gitignore` before the first commit, and check `git status` before every commit.
- **Printing the key while debugging.** It ends up in logs and screenshots. Print whether it is set, or its first few characters.
- **Hard-coding "just for a quick test".** Quick tests become committed code. Use the variable from the start.
- **Putting a key in front-end code.** Anyone can open developer tools and copy it.
- **Sharing one key across everything.** When it leaks, everything breaks at once.
- **Confusing a chat subscription with API access.** They are billed separately. The API needs its own billing set up in the developer console.

## Next steps

- [Your first LLM API call](first-llm-api-call.md)
- [Agent security](../../safety/security/agent-security.md): what to think about when a program, not you, holds the keys
- [Model supply chain](../../safety/security/model-supply-chain.md)

## Sources

- Anthropic, "Get started with Claude" (API key and `ANTHROPIC_API_KEY`, read 2026-10-21): https://platform.claude.com/docs/en/get-started
- OpenAI, "Developer quickstart" (`OPENAI_API_KEY`, read 2026-10-21): https://developers.openai.com/api/docs/quickstart
- Google, "Gemini API quickstart" (`GEMINI_API_KEY`, read 2026-10-21): https://ai.google.dev/gemini-api/docs/quickstart
- python-dotenv: https://pypi.org/project/python-dotenv/
- GitHub, "About push protection": https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- GitHub, "Removing sensitive data from a repository": https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
