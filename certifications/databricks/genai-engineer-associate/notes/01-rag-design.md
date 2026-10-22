# RAG Application Design - Databricks GenAI Engineer Associate

## Overview

This note covers **Section 2: Data Preparation** of the exam guide live since 2026-03-18, plus the retrieval background that Sections 3 and 4 build on. (It was written for the older four-domain outline, where RAG design was its own domain; the current guide has six sections and publishes no weights.) You need to understand RAG architecture, chunking strategies, embedding models and retrieval approaches, and, new in the current outline, extracting content from source files, writing chunks into Unity Catalog, and evaluating retrieval. Those additions are in section 5 below.

**[📖 RAG Overview](https://docs.databricks.com/en/generative-ai/retrieval-augmented-generation.html)** - RAG on Databricks
**[📖 Vector Search](https://docs.databricks.com/en/generative-ai/vector-search.html)** - Vector database

## Key Topics

### 1. RAG Architecture

**[📖 AI Cookbook](https://docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/index.html)** - RAG tutorial

**RAG Pipeline Components:**
```
Documents -> Chunking -> Embedding -> Vector Store -> Retrieval -> LLM Generation -> Response
```

| Component | Purpose |
|-----------|---------|
| Document processing | Ingest, parse, and chunk source documents |
| Embedding model | Convert text chunks to dense vector representations |
| Vector store | Index and search embeddings for similarity |
| Retriever | Find relevant documents for a given query |
| Generator (LLM) | Produce an answer using retrieved context |

**Key Concepts:**
- RAG combines retrieval from a knowledge base with LLM generation
- Reduces hallucination by grounding responses in retrieved documents
- No model training required - knowledge is updated by refreshing the document store
- Suitable when knowledge changes frequently or is domain-specific

**RAG vs Fine-Tuning vs Prompt Engineering:**
| Approach | When to Use | Training Required |
|----------|-------------|-------------------|
| Prompt engineering | Simple instruction-following tasks | No |
| RAG | Knowledge changes frequently, factual grounding needed | No |
| Fine-tuning | Need to change model behavior, style, or format | Yes |

### 2. Chunking Strategies

**[📖 Chunking](https://docs.databricks.com/aws/en/agents/retrieval-augmented-generation)** - Chunking approaches

| Strategy | How It Works | Pros | Cons |
|----------|-------------|------|------|
| Fixed-size | Split by character/token count | Simple, predictable | May split mid-sentence |
| Recursive character | Split by separators hierarchically | Respects text boundaries | Slightly more complex |
| Semantic | Split by meaning boundaries | Best quality chunks | Computationally expensive |
| Document-aware | Respect structure (headers, sections) | Preserves document logic | Requires format parsing |

**Chunk Size Considerations:**
| Size | Retrieval Precision | Context Coverage |
|------|--------------------|--------------------|
| Small (128-256 tokens) | High (more targeted) | Low (may miss context) |
| Medium (256-512 tokens) | Balanced | Balanced |
| Large (512-1024 tokens) | Lower (may include noise) | High (more context) |

**Key Concepts:**
- Chunk overlap (10-20%) prevents losing context at chunk boundaries
- Metadata enrichment adds source, title, section, and page number to each chunk
- Smaller chunks improve retrieval precision but may lose surrounding context
- Larger chunks provide more context but may retrieve irrelevant information
- Typical production range: 256-512 tokens with 10-20% overlap

### 3. Embedding Models

**[📖 Foundation Model APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html)** - Model serving

**Available Options:**
| Provider | Models | Integration |
|----------|--------|-------------|
| Databricks-hosted | BGE, GTE | Direct endpoint access |
| External (proxied) | OpenAI, Cohere | External model endpoints |
| Custom | Fine-tuned embeddings | Custom serving endpoint |

**Key Concepts:**
- Embedding models convert text to dense vector representations
- Vectors capture semantic meaning (similar text has similar vectors)
- Embedding dimensions affect storage, performance, and quality (768-1536 typical)
- Use the same embedding model for both indexing and querying
- Similarity metrics: cosine similarity (most common), dot product, Euclidean distance

### 4. Retrieval Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| Similarity search | Find nearest vectors to query | Basic retrieval |
| MMR (Maximum Marginal Relevance) | Balance relevance and diversity | Avoid redundant results |
| Filtered search | Combine vector similarity with metadata filters | Scoped search (by date, source) |
| Hybrid search | Combine dense (vector) and sparse (keyword) | Best of both approaches |
| Re-ranking | Use cross-encoder to re-score retrieved docs | Improved precision |
| Multi-query | Generate multiple query variations | Better recall |

**Key Concepts:**
- Top-k selection: typically retrieve 3-10 documents
- More documents provide more context but risk diluting relevance
- Filtered search narrows results by metadata before vector similarity
- Hybrid search combines semantic understanding with keyword matching
- Re-ranking is a second pass that improves precision at the cost of latency

### 5. Data preparation objectives added in the 2026 outline

**Extracting content from source files.** The guide asks you to "choose the appropriate Python package to extract document content from provided source data and format". Match the package to the format. Scanned pages saved as images (`.png`, `.jpeg`) contain no text layer, so they need optical character recognition, and `pytesseract` (a wrapper around the Tesseract OCR engine) is the guide's own sample answer. Digital PDFs have a text layer, so a PDF library such as `pypdf` or `PyMuPDF` reads them directly, and `unstructured` handles mixed document types and layout. HTML pages want an HTML parser such as `beautifulsoup`. Web crawlers such as `scrapy` fetch pages but do not read images, which is why they are distractors on image questions.

**Filtering extraneous content.** Headers, footers, navigation menus, legal boilerplate, tables of contents and repeated disclaimers end up in chunks and then in retrieval results, where they crowd out the passage that answers the question. The guide asks you to "filter extraneous content in source documents that degrades quality of a RAG application"; the fix is to strip that material during parsing, before chunking, rather than hoping the model ignores it.

**Choosing the right sources.** "Identify needed source documents that provide necessary knowledge and quality" is a coverage question. If the application answers shipping questions badly, ask whether any source actually contains shipping dates. Adding the right source (or a structured lookup, when the answer is a per-customer fact) beats tuning the chunker.

**Writing chunks to Delta in Unity Catalog.** The sequence the guide expects is: read the raw files (for example from a Unity Catalog volume), parse them to text, chunk the text, add metadata (source path, title, section, page), give each chunk a stable primary key, and write the result to a Delta table in Unity Catalog. Enable Change Data Feed on that table, because a Delta Sync Vector Search index reads changes from it. Then create the index on the table. Writing straight to the index, or skipping the primary key, breaks incremental sync.

**Chunk counts and limits.** Chunk size and overlap decide how many records you store. The guide's sample has 150 million embeddings and a 100 million limit: increasing chunk size and decreasing overlap both reduce the record count, while a smaller embedding model changes vector size, not the number of vectors.

**Advanced chunking.** "Design retrieval systems using advanced chunking strategies" covers structure-aware chunking (split on headings so a chunk is one section), parent-child or small-to-big retrieval (match on small chunks, return the larger parent for context), and adding summaries or titles to each chunk so short chunks still carry their context.

**Evaluating retrieval and re-ranking.** "Use tools and metrics to evaluate retrieval performance" means measuring the retriever on its own with a labelled set of queries and the chunks that should come back. Precision at k (how many of the top k are relevant), recall at k (how many of the relevant chunks made the top k), mean reciprocal rank (how high the first relevant chunk appears) and NDCG (whether the most relevant chunks are ranked highest) are the standard measures, and MLflow's retrieval judges (`RetrievalRelevance`, `RetrievalSufficiency`) score the same thing with an LLM. Re-ranking is a second stage: the vector search returns a generous candidate set quickly, then a more expensive model (typically a cross-encoder that reads query and chunk together) re-scores those candidates so the best few go to the LLM. It raises precision at the cost of latency, which is why it is switched off in latency-critical designs.

## Exam Tips for This Domain

1. **RAG vs fine-tuning** - RAG for changing knowledge; fine-tuning for changing behavior
2. **Chunking tradeoffs** - Smaller chunks = more precise retrieval; larger = more context
3. **Embedding consistency** - Same model for indexing and querying
4. **Retrieval strategies** - Know MMR, filtered search, hybrid search, and re-ranking
5. **Chunk overlap** - Prevents information loss at boundaries
6. **Format decides the parser** - Images need OCR (`pytesseract`); PDFs, HTML and mixed files have their own libraries
7. **Delta first, then index** - Chunks go to a Unity Catalog Delta table with a primary key and Change Data Feed, then a Delta Sync index reads it

## Documentation Links Summary

| Topic | Link |
|-------|------|
| RAG Overview | [docs.databricks.com/en/generative-ai/retrieval-augmented-generation.html](https://docs.databricks.com/en/generative-ai/retrieval-augmented-generation.html) |
| AI Cookbook | [docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/index.html](https://docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/index.html) |
| Chunking | [docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/quality-iteration/chunking.html](https://docs.databricks.com/aws/en/agents/retrieval-augmented-generation) |
| Vector Search | [docs.databricks.com/en/generative-ai/vector-search.html](https://docs.databricks.com/en/generative-ai/vector-search.html) |
| Foundation Models | [docs.databricks.com/en/machine-learning/foundation-models/index.html](https://docs.databricks.com/en/machine-learning/foundation-models/index.html) |
