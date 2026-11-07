# Section 4: Multimodal Data (15%)

**Last reviewed:** 2026-11-07

Despite its name, this section on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07) is about the building-block skills around data and LLM applications: assisting with deployment and evaluation under supervision, building LLM use cases (RAG, chatbots, summarizers), Python NLP packages and vector databases (spaCy and NumPy are named), identifying data, hardware and software components, monitoring experiments, using Python packages for classical ML, and writing components under supervision. Code ran on CPU in a scratch environment (spaCy 3.8.18, scikit-learn 1.9.1).

## LLM use cases: RAG, chatbots, summarizers

**Retrieval-augmented generation (RAG)** improves a language model's answers with retrieved, source-grounded data. NVIDIA's explanation: the user's query is converted into an embedding; an embedding model compares it with vectors in an index of the knowledge base; matches are retrieved, converted back to text and passed to the LLM, which combines them with its own response into the final answer, potentially citing sources. The benefits NVIDIA lists are trust (citations), accuracy (fewer hallucinations), clarifying ambiguous queries, and efficiency, since it is cheaper and faster than retraining and lets you "hot-swap new sources on the fly".

**[📖 What is retrieval-augmented generation? (NVIDIA)](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)** - How RAG works and NVIDIA's RAG tooling

A **chatbot** wraps an LLM in a conversation loop with a system prompt and (usually) memory and retrieval. A **summarizer** is a prompt (or fine-tune) that compresses a document; for long documents it chunks the text, summarizes the chunks and summarizes the summaries. NVIDIA's page also lists NeMo Retriever (retrieval accuracy), NIM microservices (deployment) and the NVIDIA AI Blueprint for RAG as starting points.

I built the retrieval step with TF-IDF vectors as a stand-in for an embedding model:

```python
v = TfidfVectorizer().fit(docs); D = v.transform(docs); q = v.transform(["which tool does speech recognition"])
sims = (D @ q.T).toarray().ravel()
```

```
retrieval top doc: Riva provides speech recognition and text to speech | scores [0.68, 0.0, 0.0, 0.0]
```

The query shares words with only one document, and that document comes back with a score of 0.68. A real system swaps TF-IDF for dense embeddings (so "speech recognition" would also match "transcribing audio"), and stores them in a vector database. The loop is the same: embed, search, retrieve, build the prompt, generate.

- **RAG (retrieval-augmented generation)** - answering with an LLM that is given relevant passages retrieved from a knowledge base, which improves accuracy and allows citations.
- **Embedding** - a numeric vector representing text or an image so that similar items are close together.
- **Vector database** - a store that indexes embeddings and returns the nearest ones to a query vector.

## Python NLP packages and vector databases

spaCy is an NLP library for tokenization, sentence splitting and (with trained pipelines) tagging and entity recognition. A blank English pipeline with a sentencizer needs no model download:

```python
nlp = spacy.blank("en"); nlp.add_pipe("sentencizer")
doc = nlp("NVIDIA NIM serves models. Riva handles speech. Triton serves many frameworks.")
```

```
spaCy blank pipeline: ['NVIDIA', 'NIM', 'serves', 'models', '.', 'Riva'] | sentences: 3
```

Tokens and three sentences, which is the preprocessing for chunking text before embedding. NumPy provides the arrays under all of this (the similarity computation above is a matrix product); the reading list names *Advanced NLP with spaCy* and *NumPy Absolute Basics*. The objective also lists "Use Python packages (e.g., spaCy, NumPy, Keras) for traditional ML analyses" and Keras developer guides, covered by the same practice of using library calls for tokenization, array math and standard models.

- **Tokenization** - splitting text into tokens (words, subwords or punctuation) that a model or pipeline processes.

## Identify the data, hardware and software components

Given a user need, list what it takes: data (sources, volume, modalities, labels, licensing), hardware (GPUs with enough memory for the model and batch size; storage and network for data), and software (framework, serving layer, vector store, monitoring). NVIDIA's serving software is covered in note 6. The objective is a requirements habit, not a memorized table.

## Monitor experiments and write supervised components

"Monitor data collection, experiments, and other software processes" is experiment tracking: log parameters, metrics and artifacts per run so runs can be compared. MLflow is on the reading list; I used it in the Databricks guide in this collection but did not run it in this one. "Assist with deployment and evaluation of scalability, performance and reliability" and "write software components or scripts" are stated "under a senior team member's supervision", so the exam expects the associate level of independence: follow the spec, test, and escalate.

## Check yourself against the objectives

Describe the five steps of a RAG loop; say what retrieval returned for a query and why; explain what a chunking pipeline needs from spaCy; and list the three kinds of components to identify for a requirement. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
