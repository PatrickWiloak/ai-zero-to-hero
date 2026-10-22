# Optimize Language Models for AI Applications (25-30%)

> **DP-100 retired on 2026-06-01.** This note covers the fourth domain of its final skills outline (skills measured as of 2025-04-11) and is kept as reference. The concepts carry straight over to current Azure generative AI work and to [AI-103](../../ai-103/README.md); product names have moved on (Azure AI Foundry is now Microsoft Foundry, for example), so check current docs before building.

**[📖 DP-100 study guide (archived)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)** - the final outline
**[📖 Prompt flow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow)** - flows, variants and tracing
**[📖 RAG with Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)** - retrieval for generative AI
**[📖 Fine-tuning in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning)** - preparing data and running jobs

---

## Why this domain was added

By 2024 most new machine learning work on Azure involved language models, and a data scientist's job increasingly meant choosing, adapting and evaluating a model someone else trained rather than training one from scratch. Microsoft added this domain to DP-100 so the certification reflected that, and gave it 25-30% of the exam, the joint largest share. It has four objective groups that follow the order you would work in: prepare, then try prompting, then RAG, then fine-tuning.

## 1. Prepare for model optimization

**Selecting and deploying a model from the model catalog.** The model catalog in Azure AI Foundry (and Azure Machine Learning) lists models from Microsoft, OpenAI, Meta, Mistral and others. Each has a model card describing its tasks, context length, languages, licence and limitations. Deployment options differ by model: serverless API deployments bill per token with no infrastructure to manage, while managed compute deployments run the model on virtual machines you pay for by the hour. Choose serverless when traffic is variable or you want to start quickly; choose managed compute when you need a model only available that way, full control of the environment, or steady high volume.

**Comparing models using benchmarks.** The catalog's benchmark views compare models on quality measures (accuracy on standard datasets such as reasoning and knowledge tests), and on cost and throughput. Benchmarks narrow the shortlist; they do not replace testing on your own task, because a model that leads on a public benchmark can still be the wrong choice for your data, language or latency budget.

**Testing in the playground.** The playground lets you send prompts to a deployed model, adjust the system message and parameters (temperature, top-p, maximum response length, stop sequences) and see the effect before writing code. It is where you check that a model can do the task at all.

**Selecting an optimization approach.** This is the central judgment of the domain, and the exam rewarded getting the order right. Start with **prompt engineering**, which is cheap, fast and reversible. If the model lacks knowledge it needs (your documents, recent facts, private data), add **retrieval augmented generation**, which supplies that knowledge at query time without changing the model. Turn to **fine-tuning** only when the model needs to behave differently in a way prompting cannot make reliable: a consistent output format, a house style, a specialised task, or shorter prompts at high volume. A useful rule: RAG changes what the model knows; fine-tuning changes how it behaves. Fine-tuning a model to teach it facts that change is the classic wrong answer, because the facts go stale and the model still hallucinates around them.

## 2. Optimize through prompt engineering and prompt flow

**Manual evaluation and variants.** Prompt work starts by running a small set of representative inputs and reading the outputs against what good looks like. A **prompt variant** is an alternative version of a prompt (different instructions, examples or parameters) tracked side by side so you can compare them on the same inputs instead of overwriting the previous attempt.

**Prompt templates.** A template separates the fixed instructions from the variable parts, using placeholders (for example `{{question}}` and `{{context}}`) that are filled in at run time. Templates make prompts reusable, testable and safe to change in one place.

**Prompt flow and chaining.** Prompt flow is Azure's tool for building LLM applications as a flow: a directed graph of nodes, where each node is an LLM call, a Python function or a prompt, and the output of one feeds the next. Typical chains are "classify the question, then route it", or "retrieve context, build the prompt, call the model, post-process the answer". Flows can be authored visually or with the prompt flow SDK in code, run in bulk over a dataset, and deployed as endpoints. The objective "define chaining logic with the prompt flow SDK" is about expressing those steps and their connections in code.

**Tracing.** Tracing records each step of a flow run: the inputs, outputs, latency and token usage of every node. When an answer is wrong, the trace shows whether retrieval returned the wrong documents, the prompt was assembled badly or the model misread good context. Evaluation flows then score outputs at scale for qualities such as groundedness, relevance, coherence and fluency, often using a language model as the judge.

## 3. Optimize through Retrieval Augmented Generation

RAG answers questions from your own content by retrieving the relevant passages and putting them in the prompt.

**Preparing data.** Clean the source documents (strip boilerplate, headers and footers, fix encoding), **chunk** them into passages small enough to be specific but large enough to carry meaning (often a few hundred tokens with some overlap between neighbours), and **embed** each chunk by passing it through an embedding model, which turns text into a vector so that similar meanings sit close together.

**Configuring a vector store and an Azure AI Search index.** The vectors and their text go into a store that can search by similarity. Azure AI Search is the main option on Azure: you define an index with fields for the text, the vector and metadata, and choose the search mode. Vector search finds passages by meaning; keyword (full-text) search finds exact terms such as product codes; **hybrid search** runs both and merges the results, and the **semantic ranker** re-orders the top results with a language-aware model. Hybrid search with semantic ranking is usually the strongest default, because users ask in natural language but also type identifiers that pure vector search can miss.

**Evaluating the RAG solution.** Measure retrieval and generation separately. For retrieval, check whether the right passages come back for a set of test questions. For generation, score **groundedness** (is every claim supported by the retrieved passages), **relevance** (does the answer address the question) and overall quality. A grounded but irrelevant answer points to retrieval; an ungrounded answer with good passages points to the prompt or model.

## 4. Optimize through fine-tuning

**Preparing data.** Fine-tuning data is a set of examples of the behaviour you want, usually in JSONL with one conversation per line (system, user and assistant messages). Quality beats quantity: a few hundred clean, consistent, representative examples outperform thousands of noisy ones. Hold back a validation set so you can detect overfitting.

**Selecting a base model.** Only some models support fine-tuning, and the choice trades capability against cost: a smaller model fine-tuned on a narrow task can match a much larger general model on that task at a fraction of the inference cost and latency, which is often the business reason to fine-tune at all.

**Running the job.** You upload training and validation files, choose the base model and hyperparameters (number of epochs, batch size, learning rate multiplier; sensible defaults exist), and start the job. The result is a new custom model that must be deployed before use, and that deployment has its own hosting cost.

**Evaluating the fine-tuned model.** Watch training and validation loss during the job (validation loss rising while training loss falls means overfitting), then compare the fine-tuned model against the base model, ideally the base model with your best prompt, on the same held-out test set. If the fine-tuned model is not clearly better on the metric that justified it, the extra cost is not worth it.

## Exam Tips (for reference)

- Order of approaches: prompt engineering, then RAG, then fine-tuning
- RAG fixes missing knowledge; fine-tuning fixes behaviour, format and style
- Serverless API deployments bill per token; managed compute bills for the VMs
- Prompt variants compare alternatives; templates separate fixed text from placeholders
- Prompt flow chains nodes (LLM, Python, prompt); tracing shows each node's inputs, outputs and latency
- Hybrid search plus semantic ranking is the strong default in Azure AI Search
- Groundedness asks whether claims are supported by retrieved context
- Fine-tuning data is JSONL conversations; compare against the base model with a good prompt

## Study Checklist

- [ ] I can explain when to choose prompting, RAG or fine-tuning
- [ ] I can compare two catalog models by benchmark and by a test on my own data
- [ ] I have built a prompt flow with a retrieval step and traced a run
- [ ] I can describe chunking, embedding and an Azure AI Search hybrid index
- [ ] I can explain how to tell from validation loss that a fine-tuned model is overfitting
