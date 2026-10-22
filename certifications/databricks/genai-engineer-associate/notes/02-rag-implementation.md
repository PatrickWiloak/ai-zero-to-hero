# RAG Application Implementation - Databricks GenAI Engineer Associate

## Overview

This note covers the platform basics behind **Section 3: Application Development** and **Section 4: Assembling and Deploying Applications** of the exam guide live since 2026-03-18 (the guide publishes no weights; these two sections hold the most objectives). You need to master Vector Search, Foundation Model APIs, Mosaic AI Agent Framework and LangChain integration. Section 3 objectives added in the current outline are in section 6 below; Section 4's additions (endpoint types, `ai_query()`, prompt registry, MCP, interfaces) are in [note 05](05-assembling-deploying-and-mcp.md).

**[📖 Vector Search](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html)** - Vector index management
**[📖 Agent Framework](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents)** - Building AI agents

## Key Topics

### 1. Databricks Vector Search

**[📖 Vector Search Setup](https://docs.databricks.com/en/generative-ai/vector-search.html)** - Configuration guide

**Index Types:**
| Type | Description | Embedding Management |
|------|-------------|---------------------|
| Delta Sync Index | Auto-syncs from Delta table | Managed or pre-computed |
| Direct Vector Access Index | Manually manage embeddings | You provide embeddings |

**Delta Sync Index Modes:**
| Mode | Behavior | Use Case |
|------|----------|----------|
| Triggered | Sync on demand | Batch updates |
| Continuous | Real-time sync as Delta table changes | Always up-to-date |

```python
from databricks.vector_search.client import VectorSearchClient

vsc = VectorSearchClient()

# Create a Delta Sync index with managed embeddings
index = vsc.create_delta_sync_index(
    endpoint_name="vs_endpoint",
    source_table_name="catalog.schema.chunks",
    index_name="catalog.schema.chunks_index",
    pipeline_type="TRIGGERED",
    primary_key="chunk_id",
    embedding_source_column_name="text",
    embedding_model_endpoint_name="databricks-bge-large-en"
)

# Query the index
results = index.similarity_search(
    query_text="What is Delta Lake?",
    columns=["text", "source", "title"],
    num_results=5
)
```

**Key Concepts:**
- Vector Search endpoint serves the index for low-latency queries
- Delta Sync with compute embeddings: Vector Search generates embeddings automatically
- Delta Sync with pre-computed embeddings: you provide an embedding column
- Direct Vector Access: full control over embedding computation and updates
- Filter support: combine vector similarity with column-level metadata filters

### 2. Foundation Model APIs

**[📖 Pay-per-Token](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)** - Shared compute
**[📖 Provisioned Throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)** - Dedicated compute

| Serving Type | Compute | Latency | Cost Model |
|-------------|---------|---------|------------|
| Pay-per-token | Shared | Variable | Per token used |
| Provisioned throughput | Dedicated | Consistent | Per compute unit |

**[📖 External Models](https://docs.databricks.com/en/generative-ai/external-models/index.html)** - Third-party model access

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()

# Query a foundation model
response = w.serving_endpoints.query(
    name="databricks-meta-llama-3-1-70b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is RAG?"}
    ],
    temperature=0.1,
    max_tokens=500
)
```

**Key Concepts:**
- Databricks hosts popular open models (Llama, Mixtral, DBRX)
- External model endpoints proxy to third-party APIs (OpenAI, Anthropic, Google)
- Unified API provides consistent interface regardless of model provider
- Temperature controls randomness (0 = deterministic, 1 = creative)
- Max tokens limits response length

### 3. Mosaic AI Agent Framework

**[📖 Agent Framework](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents)** - Building agents
**[📖 Agent Deployment](https://docs.databricks.com/en/generative-ai/agent-framework/deploy-agent.html)** - Deploying agents

**Key Concepts:**
- Framework for building compound AI systems (RAG, agents with tools)
- Supports LangChain, custom pyfunc, and code-based agent implementations
- Agents can use tools: Vector Search retrieval, SQL queries, Python code execution
- MLflow integration for logging, tracing, and deploying agents
- `mlflow.models.set_model()` registers the chain/agent for deployment
- Playground UI for interactive testing before deployment

### 4. LangChain on Databricks

**[📖 LangChain Integration](https://docs.databricks.com/aws/en/agents/custom-agents/author-agent)** - LangChain on Databricks

```python
from langchain_community.chat_models import ChatDatabricks
from langchain_community.vectorstores import DatabricksVectorSearch
from langchain_community.embeddings import DatabricksEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Components
embeddings = DatabricksEmbeddings(endpoint="databricks-bge-large-en")
llm = ChatDatabricks(endpoint="databricks-meta-llama-3-1-70b-instruct", temperature=0.1)
retriever = DatabricksVectorSearch(index, text_column="text").as_retriever(
    search_kwargs={"k": 5}
)

# RAG chain
prompt = ChatPromptTemplate.from_template("""
Answer based on the following context:
{context}

Question: {question}
""")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Query
response = chain.invoke("What is Delta Lake?")
```

**Key Concepts:**
- `ChatDatabricks`: LangChain chat model wrapper for Databricks endpoints
- `DatabricksVectorSearch`: LangChain retriever for Vector Search indexes
- `DatabricksEmbeddings`: LangChain embeddings wrapper
- Chain construction: retriever -> prompt template -> LLM -> output
- Memory management for conversational RAG (chat history)

### 5. MLflow for GenAI

**[📖 MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview)** - LLM observability

```python
import mlflow

# Enable autologging for LangChain
mlflow.langchain.autolog()

# Log chain as MLflow model
with mlflow.start_run():
    mlflow.langchain.log_model(chain, "rag_chain",
        input_example={"question": "What is Delta Lake?"})
```

**Key Concepts:**
- MLflow Tracing records every LLM call for debugging and monitoring
- `mlflow.langchain.autolog()` automatically traces LangChain calls
- Log chains as MLflow models for versioning and deployment
- Model signatures define input/output schemas
- Experiment tracking for prompt engineering iterations

### 6. Application development objectives added in the 2026 outline

**Choosing a framework.** "Select LangChain/similar tools for use in a Generative AI application" asks when a framework helps. LangChain (and LangGraph for stateful, multi-step agents) supplies ready-made retrievers, prompt templates, parsers and tool-calling loops; the OpenAI Agents SDK and others offer similar building blocks. Databricks supports these through MLflow, so the choice turns on what the application needs: a simple retrieve-then-answer chain needs little framework, a multi-step agent with tools and memory benefits from one.

**Prompt augmentation and adjustment.** Two objectives describe prompt work. "Augment a prompt with additional context from a user's input based on key fields, terms, and intents" means pulling structured details out of the request (an order number, a product name, the user's goal) and using them to fetch and insert the right context. "Create a prompt that adjusts an LLM's response from a baseline to a desired output" means iterating on instructions, examples and format until the response matches a target: state the role, the constraints and the exact output format, and add an example when instructions alone are not enough.

**Qualitative review and guardrails.** "Qualitatively assess responses to identify common issues such as quality and safety" is reading outputs with a critical eye before measuring them: is it answering the question, is it grounded, is it safe, is the tone right. "Implement LLM guardrails to prevent negative outcomes" then turns what you found into controls: input filters, output safety filters, topic restrictions, PII detection and refusal instructions, applied in the chain or through AI Gateway.

**Model and embedding selection.** Four objectives are about picking models. "Select the best LLM based on the attributes of the application" weighs quality, latency, cost, context window and licence against the use case. "Select a model from a model hub or marketplace for a task based on model metadata/model cards" means reading the card for the intended task, languages, context length, licence, training data and known limitations before choosing. "Select an embedding model context length based on source documents, expected queries, and optimization strategy" has a clean rule: the embedding model's context length must cover your chunk size, and anything longer costs more and runs slower without benefit; with chunks of at most 512 tokens and cost and latency mattering more than quality, choose the smallest model with a 512-token context (the guide's own sample). "Select chunking strategy based on model and retrieval evaluation" closes the loop: change chunk size and method, re-run the retrieval evaluation from note 01, and keep what scores best.

**Agentic systems with MLflow and Agent Framework.** "Utilize MLflow and Agent Framework for developing agentic systems" means authoring the agent in code, logging it with MLflow (with tracing on), evaluating it with `mlflow.genai.evaluate()` and deploying it to a serving endpoint. The evaluation and monitoring side, and the comparison between the two phases, are in [note 06](06-evaluation-monitoring-and-governance.md); multi-agent systems that call Genie spaces are in [note 04](04-design-applications-and-agent-bricks.md).

## Exam Tips for This Domain

1. **Delta Sync vs Direct Vector Access** - Know when to use each index type
2. **Triggered vs Continuous sync** - Tradeoff between freshness and cost
3. **Pay-per-token vs provisioned throughput** - Variable vs consistent latency
4. **LangChain components** - ChatDatabricks, DatabricksVectorSearch, DatabricksEmbeddings
5. **Agent Framework** - Know how to build, log, and deploy agents
6. **MLflow Tracing** - Debugging and monitoring LLM applications

## Documentation Links Summary

| Topic | Link |
|-------|------|
| Vector Search | [docs.databricks.com/en/generative-ai/vector-search.html](https://docs.databricks.com/en/generative-ai/vector-search.html) |
| Create/Query Index | [docs.databricks.com/en/generative-ai/create-query-vector-search.html](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html) |
| Foundation Models | [docs.databricks.com/en/machine-learning/foundation-models/index.html](https://docs.databricks.com/en/machine-learning/foundation-models/index.html) |
| Agent Framework | [docs.databricks.com/en/generative-ai/agent-framework/index.html](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents) |
| LangChain | [docs.databricks.com/en/generative-ai/agent-framework/langchain.html](https://docs.databricks.com/aws/en/agents/custom-agents/author-agent) |
| MLflow Tracing | [docs.databricks.com/en/mlflow/llm-tracing.html](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview) |
