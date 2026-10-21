# Notebooks and Colab

**In one line:** Notebooks let you run Python one small piece at a time and see the result immediately, which is the fastest way to learn and experiment with AI; this page shows you how to use Google Colab (free, in the browser) and Jupyter (on your own machine), including secrets, GPUs and the traps that catch everyone.
**Last reviewed:** 2026-10-21

---

## The short version

- A **notebook** is a document made of **cells**. Code cells run Python and show their output right underneath; text cells hold notes. You run cells one at a time, in any order.
- **Google Colab** runs notebooks in your browser on Google's machines, free, with nothing to install. It is the quickest start on this site's paths, and it offers limited free GPU time.
- **Jupyter** (JupyterLab or the notebook view in VS Code) runs the same kind of notebook on your own computer, with your own files and no time limits.
- Notebooks are for **exploring**. When something works and you want to run it again and again, move it into a `.py` file.
- Never paste an API key into a notebook cell. Colab has a **Secrets** panel for exactly this; locally, use environment variables.
- The classic notebook bug: cells run out of order, so the notebook works for you and fails for everyone else. Before you share one, **restart and run all**.

## Why notebooks suit AI work

AI work is iterative. You load some data, look at it, try a prompt, look at the output, tweak the prompt, try again. In a normal script you would rerun everything from the top each time, including the slow parts. In a notebook you load the data once in one cell, then rerun only the cell with the prompt as often as you like. Results, tables and even images appear inline, so a notebook doubles as a record of what you tried.

That is why most ML tutorials, Kaggle competitions, and research code demos are notebooks, and why model providers often publish "cookbook" notebooks of example code.

## Getting started with Colab

1. Go to [colab.research.google.com](https://colab.research.google.com/) and sign in with a Google account.
2. Choose **New notebook**.
3. Click into the first cell, type `print("hello")`, and press **Shift+Enter** to run it. The output appears underneath and the cursor moves to a new cell.

That is the whole interface. A few things worth knowing straight away:

- **Shift+Enter** runs the current cell and moves on. **Ctrl+Enter** (Cmd+Enter on Mac) runs it and stays.
- The number in square brackets next to a cell, like `[3]`, is the order cells ran in. Watch it; it tells you the true history of your session.
- Use **+ Text** to add notes in Markdown. Future you will be grateful.
- Lines starting with `!` run as shell commands. That is how you install packages:

```python
!pip install anthropic openai
```

Colab already includes many common libraries (NumPy, pandas, PyTorch, scikit-learn), so you only install what is missing.

## Keeping API keys out of the notebook

Notebooks get shared, uploaded to GitHub and pasted into chats. A key written in a cell leaks with them. Colab's **Secrets** feature stores keys against your account instead:

1. Click the key icon in the left sidebar.
2. Add a secret named `ANTHROPIC_API_KEY` (or `OPENAI_API_KEY`) and paste the key as its value.
3. Toggle **Notebook access** on for this notebook.
4. Read it in code:

```python
import os
from google.colab import userdata

os.environ["ANTHROPIC_API_KEY"] = userdata.get("ANTHROPIC_API_KEY")
```

The SDKs read the key from the environment, so after that cell the code from [Your first LLM API call](first-llm-api-call.md) runs unchanged. The full story of keeping secrets safe is in [API keys and environment variables](api-keys-and-env-vars.md).

## A first experiment

Put each block in its own cell and run them in order. This is a pattern you will use constantly: set up once, then iterate on one cell.

```python
# Cell 1: setup (run once)
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"   # Anthropic's smallest current model as of 2026-10
```

```python
# Cell 2: a helper (run once)
def ask(prompt, max_tokens=500):
    r = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in r.content if b.type == "text")
```

```python
# Cell 3: iterate here (run as often as you like)
review = "The battery life is great but the screen scratches if you look at it."
print(ask(f"Classify the sentiment of this review as positive, negative or mixed. "
          f"Answer with one word.\n\n{review}"))
```

Now change the review, or the instruction, and rerun only Cell 3. In a minute you can try ten variations. That speed is the point of notebooks.

## GPUs in Colab

To use a GPU, go to **Runtime > Change runtime type** and choose a GPU accelerator. Check it worked:

```python
!nvidia-smi
```

Be realistic about the free tier. Google's own FAQ says that in the free version "access to expensive resources like GPUs is heavily restricted", that notebooks "can run for at most 12 hours, depending on availability and your usage patterns", and that runtimes time out when idle. Resources are not guaranteed and limits change over time. Free GPU time is fine for learning (training a small network, running a small open model) but not for anything long-running. Paid Colab plans and cloud GPU rentals exist when you outgrow it.

You do not need a GPU to call hosted model APIs. The model runs on the provider's hardware; your notebook just sends text. GPUs only matter when you run or train models yourself, as in [Run a model locally](run-a-model-locally.md) and the [ML engineer path](../start-here/ml-engineer-path.md). [GPUs for AI](../concepts/gpus-for-ai.md) explains why they matter so much.

## Files in Colab

A Colab session runs on a temporary machine. **Files you create there disappear when the session ends.** To keep work:

- The notebook itself saves to your Google Drive automatically.
- For data files, upload through the folder icon in the sidebar (temporary), or mount your Drive:

```python
from google.colab import drive
drive.mount("/content/drive")
# your Drive is now at /content/drive/MyDrive/
```

## Jupyter on your own machine

When you want your own files, no session limits, and your local GPU if you have one, run notebooks locally. Inside a project with a virtual environment (see [Python for AI](python-for-ai.md)):

```bash
pip install jupyterlab
jupyter lab
```

A browser tab opens with the JupyterLab interface. Alternatively, VS Code opens `.ipynb` files directly once the Python and Jupyter extensions are installed, and lets you pick your virtual environment as the **kernel** (the Python process that runs the cells).

Locally, keep keys in a `.env` file and load them in the first cell:

```python
from dotenv import load_dotenv
load_dotenv()   # reads .env into environment variables
```

## From notebook to script

Notebooks are a poor fit for code that runs unattended, is tested, or is shared as a tool. Hidden state (variables from cells you deleted), out-of-order execution and awkward version control all bite. The usual workflow:

1. Explore in a notebook until the approach works.
2. Move the working functions into a `.py` file.
3. Import them back into the notebook if you still want to experiment.
4. Run the script for real jobs.

## Common mistakes

- **Out-of-order execution.** You ran Cell 5, then edited Cell 2 and did not rerun Cell 3, and now nothing makes sense. Use **Runtime > Restart and run all** (Colab) or **Kernel > Restart Kernel and Run All Cells** (Jupyter) whenever in doubt, and always before sharing.
- **Keys in cells.** Use Colab Secrets or a `.env` file. Check old notebooks before you publish them.
- **Losing files.** Colab's machine is temporary. Save outputs to Drive or download them.
- **Burning GPU quota on CPU work.** Only select a GPU runtime when your code actually uses one.
- **Giant notebooks.** A 200-cell notebook is a script that cannot be tested. Split it up.

## Next steps

- [API keys and environment variables](api-keys-and-env-vars.md)
- [Your first LLM API call](first-llm-api-call.md)
- [Run a model locally](run-a-model-locally.md)
- [Chatbot in an afternoon](../../build/projects/chatbot-in-an-afternoon.md)

## Sources

- Google Colab FAQ (free tier: GPU access "heavily restricted", up to 12 hours, idle timeouts, limits not guaranteed; read 2026-10-21): https://research.google.com/colaboratory/faq.html
- Google Colab: https://colab.research.google.com/
- Project Jupyter, JupyterLab documentation: https://jupyterlab.readthedocs.io/
- VS Code, Jupyter notebooks: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
- Anthropic, Models overview (model IDs, as of 2026-10): https://platform.claude.com/docs/en/about-claude/models/overview
