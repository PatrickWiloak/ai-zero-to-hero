---
last-updated: 2026-10-22
---

# Databricks Generative AI Engineer Associate - Fact Sheet

## Exam Overview

**Exam Name:** Databricks Certified Generative AI Engineer Associate
**Duration:** 90 minutes
**Questions:** 45 scored multiple-choice or multiple-selection items
**Exam guide:** six sections, live since 2026-03-18, no published weights
**Passing Score:** 70% (approximately 32 correct)
**Cost:** $200 USD
**Delivery:** Online proctored
**Valid For:** 2 years

**[📖 Official Exam Page](https://www.databricks.com/learn/certification/genai-engineer-associate)** - Registration and exam details
**[📖 Databricks Academy](https://www.databricks.com/learn)** - GenAI learning paths
**[📖 Generative AI Documentation](https://docs.databricks.com/aws/en/agents)** - GenAI on Databricks

## Target Audience

This certification is designed for:
- Engineers building RAG applications on Databricks
- Data scientists working with LLMs and generative AI
- ML engineers implementing GenAI production systems
- Developers integrating LLMs into data workflows
- Professionals familiar with Databricks and Python

## Exam Outline: six sections, no published weights

The current exam guide (live since 2026-03-18) lists six sections and their objectives, and gives **no weights**. Any percentage split you see elsewhere is not from Databricks. Objective counts are the best available proxy: Design Applications 6, Data Preparation 8, Application Development 13, Assembling and Deploying Applications 15, Governance 4, Evaluation and Monitoring 10.

**[📖 Exam guide (March 2026)](https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf)** - the authoritative outline

The sections below follow the six sections. The older guide's RAG design, RAG implementation and LLM fundamentals material is kept where the current objectives still draw on it.

## Section 1: Design Applications

**[📖 Agent Bricks FAQ](https://docs.databricks.com/aws/en/agents/concepts/faq)** - current status of Agent Bricks
**[📖 Information Extraction](https://docs.databricks.com/aws/en/agents/agent-bricks/info-extraction)** - documents to structured fields

**Key Facts:**
- Start every design by writing the required inputs and outputs; the rest follows from them
- Model task selection: summarization (long text to a short gist), classification (fixed labels), extraction (fields), question answering, translation, generation, embedding
- Chain components: prompt template, retriever, model, output parser, tools; RAG is retriever, prompt, model, parser
- Formatted output: state the format, give an example, parse the result
- Tool ordering: gather knowledge with read-only tools first, take actions with side effects last
- Agent Bricks named by the guide:
  - Knowledge Assistant: question answering over documents, with citations
  - Information Extraction: unstructured documents to structured JSON per a schema you define (UI, SQL or REST API)
  - Multiagent Supervisor (Supervisor Agent in the docs): routes parts of a request to existing agents, Genie spaces and tools
- Since the guide was published, the docs label Knowledge Assistant and Supervisor Agent as legacy (Genie Agents for new low-code agents, Agent Bricks CLI for code); Information Extraction is current
- Genie spaces answer questions over Unity Catalog tables by writing SQL; multi-agent systems call them through the Genie conversation API

## Section 2: Data Preparation (and RAG design background)

### RAG Architecture

**[📖 RAG Overview](https://docs.databricks.com/en/generative-ai/retrieval-augmented-generation.html)** - RAG on Databricks
**[📖 AI Cookbook](https://docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/index.html)** - RAG tutorial
**[📖 Vector Search](https://docs.databricks.com/en/generative-ai/vector-search.html)** - Vector database

**Key Facts:**
- RAG combines retrieval from a knowledge base with LLM generation
- RAG reduces hallucination by grounding responses in retrieved documents
- RAG architecture components:
  1. Document processing pipeline (ingest, chunk, embed)
  2. Vector store (index and search embeddings)
  3. Retriever (find relevant documents for a query)
  4. Generator (LLM produces answer using retrieved context)
- RAG vs fine-tuning:
  - RAG: use when knowledge changes frequently, no training needed
  - Fine-tuning: use when you need to change model behavior/style
  - Prompt engineering: use for simple instruction-following tasks

### Chunking Strategies

**[📖 Document Processing](https://docs.databricks.com/aws/en/agents/retrieval-augmented-generation)** - Chunking approaches

**Key Facts:**
- Fixed-size chunking: split by character/token count (simple, fast)
- Recursive character splitting: split by separators hierarchically
- Semantic chunking: split by meaning boundaries
- Document-aware chunking: respect document structure (headers, paragraphs)
- Chunk size considerations:
  - Smaller chunks: more precise retrieval, may lose context
  - Larger chunks: more context, may include irrelevant information
  - Typical range: 256-1024 tokens
- Chunk overlap: 10-20% overlap prevents losing context at boundaries
- Metadata enrichment: add source, title, section to each chunk

### Embedding Models

**[📖 Foundation Model APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html)** - Model serving
**[📖 External Models](https://docs.databricks.com/en/generative-ai/external-models/index.html)** - Third-party model access

**Key Facts:**
- Embedding models convert text to dense vector representations
- Databricks-hosted embedding models (e.g., BGE, GTE)
- External model endpoints (OpenAI, Cohere embeddings)
- Embedding dimensions affect storage and retrieval performance
- Similarity metrics: cosine similarity, dot product, Euclidean distance
- Embedding model selection: domain relevance, dimension size, latency

### Extraction, Delta and Retrieval Evaluation

**Key Facts:**
- Choose the extraction package by format: scanned images need OCR (`pytesseract`); PDFs use `pypdf` or `PyMuPDF`; mixed layouts `unstructured`; HTML `beautifulsoup`
- Strip headers, footers, navigation and boilerplate before chunking; it degrades retrieval
- Write chunks with metadata and a primary key to a Delta table in Unity Catalog, enable Change Data Feed, then build a Delta Sync index on it
- Larger chunks and less overlap mean fewer records; a smaller embedding model does not reduce the count
- Advanced chunking: structure-aware, parent-child (small-to-big), chunk summaries
- Retrieval metrics: precision@k, recall@k, MRR, NDCG; MLflow retrieval judges score relevance and sufficiency
- Re-ranking re-scores a generous candidate set with a cross-encoder: better precision, more latency

### Retrieval Strategies

**Key Facts:**
- Similarity search: find nearest vectors to query embedding
- Maximum Marginal Relevance (MMR): balance relevance and diversity
- Filtered search: combine vector similarity with metadata filters
- Hybrid search: combine dense (vector) and sparse (keyword) retrieval
- Re-ranking: use a cross-encoder to re-score retrieved documents
- Top-k selection: number of documents to retrieve (typically 3-10)
- Multi-query retrieval: generate multiple query variations for better recall

## Sections 3 and 4: Application Development, Assembling and Deploying Applications

### Databricks Vector Search

**[📖 Vector Search Setup](https://docs.databricks.com/en/generative-ai/vector-search.html)** - Configuration guide
**[📖 Vector Search Index](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html)** - Creating indexes
**[📖 Query Vector Search](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html#query)** - Querying indexes

**Key Facts:**
- Vector Search is a managed vector database service on Databricks
- Two index types:
  - Delta Sync Index: automatically syncs from a Delta table (managed embeddings)
  - Direct Vector Access Index: manually manage embeddings (more control)
- Delta Sync Index modes:
  - Triggered: sync on demand
  - Continuous: real-time sync as Delta table changes
- Embedding source:
  - Compute embeddings: Vector Search computes embeddings using specified model
  - Use pre-computed embeddings: provide your own embedding column
- Vector Search endpoint: serves the index for low-latency queries
- Query with `similarity_search()` or REST API
- Filter support: combine vector search with column filters
- Endpoint types: standard (about 320M vectors at 768 dimensions, lowest latency) versus storage-optimized (about 1B vectors at 768 dimensions, 10-20x faster indexing, priced for scale, about 250 ms extra latency, no continuous sync, dimensions divisible by 16)
- Hybrid search and re-ranking add relevance and latency; the guide's latency-critical sample turns both off and fine-tunes the embedding model instead

### Foundation Model APIs

**[📖 Foundation Models](https://docs.databricks.com/en/machine-learning/foundation-models/index.html)** - Model serving overview
**[📖 Pay-per-Token](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)** - Pay-per-token models
**[📖 Provisioned Throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)** - Dedicated capacity

**Key Facts:**
- Pay-per-token: shared compute, pay for tokens used (variable latency)
- Provisioned throughput: dedicated compute, guaranteed throughput (consistent latency)
- Available models: DBRX, Llama (Meta), Mixtral, and more
- External model endpoints: proxy to OpenAI, Anthropic, Google, etc.
- Unified API: consistent interface regardless of model provider
- Token limits: model-specific context window sizes
- Temperature: controls randomness (0 = deterministic, 1 = creative)
- Top-p (nucleus sampling): probability threshold for token selection

### Mosaic AI Agent Framework

**[📖 Agent Framework](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents)** - Building AI agents
**[📖 Agent Deployment](https://docs.databricks.com/en/generative-ai/agent-framework/deploy-agent.html)** - Deploying agents

**Key Facts:**
- Agent Framework for building compound AI systems
- Supports LangChain, custom pyfunc, and code-based agents
- Agents can use tools: Vector Search, SQL, Python code execution
- Chain components: retriever, LLM, tools, memory
- Agent deployment to Model Serving endpoints
- MLflow integration for logging and tracing agents
- `mlflow.models.set_model()` to register the chain
- Playground UI for testing agents interactively

### LangChain on Databricks

**[📖 LangChain Integration](https://docs.databricks.com/aws/en/agents/custom-agents/author-agent)** - LangChain on Databricks

**Key Facts:**
- LangChain provides building blocks for LLM applications
- `ChatDatabricks`: LangChain chat model for Databricks endpoints
- `DatabricksVectorSearch`: LangChain retriever for Vector Search
- `DatabricksEmbeddings`: LangChain embeddings wrapper
- Chain construction: prompt template -> LLM -> output parser
- RAG chain: retriever -> prompt with context -> LLM
- Memory management for conversational RAG

### MLflow for GenAI

**[📖 MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview)** - LLM observability
**[📖 MLflow GenAI](https://docs.databricks.com/aws/en/mlflow/logged-model)** - Logging GenAI models

**Key Facts:**
- MLflow Tracing: traces LLM calls for debugging and monitoring
- `mlflow.langchain.autolog()` auto-traces LangChain calls
- Log chains as MLflow models for deployment
- Model signatures for GenAI: input/output schema definition
- Artifact logging for prompts, configs, and evaluation data
- Experiment tracking for prompt engineering iterations

### Added in the 2026 outline (Sections 3 and 4)

**[📖 Prompt Registry](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/)** - versioned prompts
**[📖 MCP on Databricks](https://docs.databricks.com/aws/en/generative-ai/mcp/)** - managed, external and custom servers

**Key Facts:**
- pyfunc chain: `load_context()` loads once, `predict()` does pre-processing, model call and post-processing
- A deployable RAG model needs flavor, embedding model, retriever, dependencies, input example and signature
- Register to Unity Catalog: `mlflow.set_registry_uri("databricks-uc")` and a `catalog.schema.model` name
- Serving access: declare dependent resources so Databricks provisions a scoped identity, or use on-behalf-of-user auth for per-user data; never embed personal tokens
- `ai_query()` runs a serving endpoint over table rows in SQL; the answer for batch inference
- Persistent memory: a transactional store (Lakebase) for conversation state and long-term memory, Delta for analytical history
- Prompt Registry: `mlflow.genai.register_prompt()` creates immutable versions in Unity Catalog; aliases (`staging`, `production`) promote and roll back; load with `prompts:/catalog.schema.name@production`
- CI/CD: sync the index after source updates, promote prompts by alias, test retriever, tools and prompt separately
- MCP: managed (Databricks-hosted, platform features) first, external (third-party, keys in Databricks Secrets) next, custom (built on Databricks Apps) last
- Interfaces: Databricks Apps for internal web UIs, Slack or Teams for meet-them-where-they-work bots; keep credentials on the server side
- Embedding model context length should cover the chunk size and no more when cost and latency matter
- Read model cards (task, languages, context, licence, limits) before choosing from a hub or marketplace

## Sections 5 and 6: Governance, Evaluation and Monitoring

### RAG Evaluation

**[📖 Agent Evaluation](https://docs.databricks.com/en/generative-ai/agent-evaluation/index.html)** - Evaluation framework
**[📖 MLflow Evaluate](https://mlflow.org/docs/latest/llms/llm-evaluate/index.html)** - LLM evaluation

**Key Facts:**
- Evaluation dimensions:
  - Retrieval quality: are the right documents retrieved?
  - Answer relevance: does the answer address the question?
  - Faithfulness/groundedness: is the answer supported by retrieved context?
  - Answer correctness: is the answer factually correct?
- Mosaic AI Agent Evaluation:
  - Automated evaluation with LLM-as-judge
  - Human evaluation workflows
  - Evaluation datasets with ground truth
  - Per-request quality scores
- `mlflow.evaluate()` with GenAI metrics
- Evaluation metrics: answer_correctness, faithfulness, relevance
- Custom evaluation metrics for domain-specific quality
- Evaluation harness: standardized testing across model versions

### Governance for GenAI

**[📖 AI Governance](https://docs.databricks.com/aws/en/ai-gateway/ai-governance)** - GenAI governance
**[📖 Unity Catalog Models](https://docs.databricks.com/en/mlflow/models-in-uc.html)** - Model governance

**Key Facts:**
- Unity Catalog for model and data governance
- PII detection and handling in training data
- Guardrails: input/output filtering for safety
- Content filtering: block harmful or inappropriate content
- Data lineage for GenAI: track data used in embeddings
- Cost management: monitor token usage and compute costs
- Compliance: audit logging for GenAI requests
- Inference table logging: capture all requests and responses
- Data retention policies for inference logs

### Added in the 2026 outline (Sections 5 and 6)

**[📖 Built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/)** - which judges need ground truth
**[📖 AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/)** - usage, inference tables, rate limits

**Key Facts:**
- Evaluate with `mlflow.genai.evaluate()` plus MLflow tracing: the score says something is wrong, the trace says where
- Judges needing ground truth: `Correctness`, `RetrievalSufficiency`, `ToolCallCorrectness`
- Judges without ground truth (usable on live traffic): `RelevanceToQuery`, `RetrievalRelevance`, `RetrievalGroundedness`, `Safety`, `Guidelines`, `ToolCallEfficiency`
- Custom scorers: code-based for deterministic rules, custom LLM judges for judgment calls
- SME feedback: review app and labeling sessions; calibrate experts on clear rubrics, then use aligned judgments in evaluation
- Evaluation is before release on a chosen dataset; monitoring is after release on live traffic
- AI Gateway: inference tables (payload logging to Unity Catalog), usage tables, rate limits, guardrails, traffic splitting, fallbacks
- Agent Monitoring runs scorers on sampled production traces
- Cost control: smallest model that passes evaluation, pay-per-token versus provisioned throughput, scale to zero, `ai_query()` for batch, rate limits
- Governance: mask sensitive values before the model, layer guardrails against prompt injection, check data and model licences, clean problematic text at the source

## Background: LLM Fundamentals (no longer its own section)

The current outline has no fundamentals section, but its model selection objectives in Sections 3 and 6 assume this material.

### Transformer Architecture

**[📖 Foundation Models Overview](https://docs.databricks.com/en/machine-learning/foundation-models/index.html)** - Available models

**Key Facts:**
- Transformers use self-attention mechanism
- Tokens: text is split into subword units (tokenization)
- Context window: maximum number of tokens a model can process
- Attention: allows model to focus on relevant parts of input
- Encoder-only: BERT-style (good for classification, embeddings)
- Decoder-only: GPT-style (good for generation)
- Encoder-decoder: T5-style (good for translation, summarization)

### Generation Parameters

**Key Facts:**
- Temperature: controls randomness of output
  - 0: deterministic (greedy decoding)
  - 0.1-0.3: focused, factual responses
  - 0.7-1.0: creative, diverse responses
- Top-p (nucleus sampling): cumulative probability threshold
- Top-k: limit sampling to top-k most likely tokens
- Max tokens: maximum length of generated response
- Stop sequences: tokens that signal generation completion
- Frequency penalty: reduce repetition of tokens
- Presence penalty: encourage diversity of topics

### Prompt Engineering

**[📖 Prompt Engineering](https://docs.databricks.com/aws/en/large-language-models/ai-playground)** - Prompt techniques

**Key Facts:**
- System prompt: defines the model's role and behavior
- Zero-shot: no examples provided
- Few-shot: provide examples of desired input-output pairs
- Chain-of-thought: instruct model to reason step-by-step
- Retrieval-augmented prompts: include retrieved context in prompt
- Prompt template variables: dynamically insert context and queries
- Output formatting: instruct model to respond in specific format (JSON, etc.)
- Prompt injection awareness: sanitize user inputs

### Model Selection

**Key Facts:**
- Model size vs quality tradeoff: larger models generally better but slower/costlier
- Latency requirements drive model selection
- Cost per token varies significantly between models
- Open-source models (Llama, Mixtral): more control, self-hosted
- Proprietary models (GPT-4, Claude): typically higher quality, API-based
- Domain-specific fine-tuned models for specialized tasks
- DBRX: Databricks' open-source foundation model
- Benchmark evaluation: MMLU, HellaSwag, etc. for model comparison

## Exam Tips

1. **No official weights** - Sections 3 and 4 hold the most objectives (13 and 15)
2. **Agent Bricks by output** - cited answers (Knowledge Assistant), structured fields (Information Extraction), delegation (Multiagent Supervisor)
3. **Vector Search endpoint choice** - standard for latency, storage-optimized for scale and cost
4. **Batch inference** - `ai_query()` over a table
5. **Prompt Registry aliases** - promotion and rollback without redeploying
6. **MCP order of preference** - managed, then external, then custom
7. **Ground-truth judges** - Correctness, RetrievalSufficiency, ToolCallCorrectness
8. **AI Gateway** - inference tables, usage tables, rate limits
9. **SME feedback** - calibrate on rubrics; do not average or replace experts
10. **Hands-on practice** - build, evaluate and deploy at least one agent on Databricks

## Quick Reference

### Essential Code Patterns
```python
# Vector Search Index Creation
from databricks.vector_search.client import VectorSearchClient
vsc = VectorSearchClient()
index = vsc.create_delta_sync_index(
    endpoint_name="vs_endpoint",
    source_table_name="catalog.schema.chunks",
    index_name="catalog.schema.chunks_index",
    pipeline_type="TRIGGERED",
    primary_key="chunk_id",
    embedding_source_column_name="text",
    embedding_model_endpoint_name="databricks-bge-large-en"
)

# Query Vector Search
results = index.similarity_search(
    query_text="What is Delta Lake?",
    columns=["text", "source"],
    num_results=5
)

# Foundation Model API
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
response = w.serving_endpoints.query(
    name="databricks-meta-llama-3-1-70b-instruct",
    messages=[{"role": "user", "content": "What is RAG?"}],
    temperature=0.1,
    max_tokens=500
)

# LangChain RAG Chain
from langchain_community.chat_models import ChatDatabricks
from langchain_community.vectorstores import DatabricksVectorSearch
retriever = DatabricksVectorSearch(index, text_column="text").as_retriever()
llm = ChatDatabricks(endpoint="databricks-meta-llama-3-1-70b-instruct")

# Agent evaluation (MLflow 3)
import mlflow
from mlflow.genai.scorers import Correctness, RelevanceToQuery, RetrievalGroundedness
results = mlflow.genai.evaluate(
    data=eval_dataset,            # records with inputs and, for Correctness, expectations
    predict_fn=my_agent,
    scorers=[Correctness(), RelevanceToQuery(), RetrievalGroundedness()],
)

# Batch inference in SQL
# SELECT ai_query('databricks-meta-llama-3-3-70b-instruct', CONCAT('Sentiment of: ', review)) FROM reviews
```
