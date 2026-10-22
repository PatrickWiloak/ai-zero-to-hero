# Assembling and Deploying Applications - Databricks GenAI Engineer Associate

## Overview

This note covers **Section 4: Assembling and Deploying Applications**, the section with the most objectives in the exam guide live since 2026-03-18 (fifteen of them; Databricks publishes no weights). Note 02 already covers the basics of Vector Search indexes, Foundation Model APIs and logging a chain with MLflow. This note adds what the current outline introduced: choosing a Vector Search endpoint type, batch inference with `ai_query()`, access control from serving endpoints, registering to Unity Catalog, persistent memory, CI/CD and prompt versioning, MCP servers, and user-facing interfaces.

**[📖 Vector Search](https://docs.databricks.com/aws/en/vector-search/vector-search)** - endpoints, indexes and limits
**[📖 Prompt Registry](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/)** - versioned prompts in Unity Catalog
**[📖 MCP on Databricks](https://docs.databricks.com/aws/en/generative-ai/mcp/)** - managed, external and custom servers

---

## 1. Coding a chain as a pyfunc model

When a chain needs logic that no framework flavor gives you, you wrap it in an MLflow pyfunc model: a Python class that subclasses `mlflow.pyfunc.PythonModel`, loads anything expensive once in `load_context()`, and does its work in `predict()`. The value for the exam is the pre- and post-processing hooks. Pre-processing happens at the start of `predict()` (clean the input, look up an account, build the prompt); post-processing happens at the end (parse the model's text into JSON, strip anything that should not be shown, attach citations). Because the whole thing is one logged model, it deploys to a serving endpoint as a single unit, with the processing travelling with it. For agents, Databricks provides higher-level interfaces built on the same idea (such as `ResponsesAgent`), but the pyfunc pattern is what the objective "code a chain using a pyfunc model with pre- and post-processing" refers to.

The guide also asks you to "choose the basic elements needed to create a RAG application": the model flavor (pyfunc, LangChain and so on), the embedding model, the retriever, the dependencies (pinned packages so the endpoint can rebuild the environment), input examples (a sample request logged with the model) and the model signature (the declared input and output schema). Signature and input example are easy to forget and are exactly what a question will leave out of a "why does this deployment fail or behave oddly" scenario.

## 2. Registering to Unity Catalog and controlling access

Models are registered to Unity Catalog with MLflow by pointing the registry at Unity Catalog (`mlflow.set_registry_uri("databricks-uc")`) and using a three-level name, `catalog.schema.model`. Registering there gives the model the same governance as tables: permissions, lineage back to the data and experiment, versioning and aliases such as `champion`.

A deployed chain usually needs to reach other resources: a Vector Search index, a Foundation Model endpoint, a Genie space, a SQL warehouse, a Unity Catalog function. The objective "control access to resources from model serving endpoints" is about how those calls are authorized. The preferred pattern is to declare the resources the agent depends on when you log or configure it, so Databricks provisions an identity (a service principal) with exactly those permissions and handles credentials for you. When different users must see different data, use user authorization (on-behalf-of-user), where the agent calls downstream resources with the identity of the person making the request, so Unity Catalog permissions and audit trails apply per user. Hard-coding a personal access token in the model is the wrong answer in every version of this question.

## 3. Vector Search: concepts, endpoints and configuration

Mosaic AI Vector Search has three layers to keep straight. An **endpoint** is the compute that serves queries. An **index** lives on an endpoint and is either a Delta Sync index (kept in step with a source Delta table, with embeddings computed for you or supplied by you) or a Direct Vector Access index (you write vectors through the API yourself). The **source table** in Unity Catalog holds the chunks.

The objective "configure vector search for a particular solution based on number of embeddings, update frequency, latency, and cost requirements" is mostly about endpoint type and sync mode. A standard endpoint holds roughly 320 million vectors at 768 dimensions (fewer at higher dimensions) and is the choice when query latency matters most. A storage-optimized endpoint holds roughly a billion vectors at 768 dimensions, indexes 10 to 20 times faster and is priced for large vector counts, in exchange for about 250 ms of extra query latency; it does not support continuous sync and needs embedding dimensions divisible by 16. For sync mode, triggered sync updates the index when you run it (cheaper, fine for daily or hourly batches), and continuous sync keeps it within seconds of the table (more expensive, for data that must be fresh). Hybrid search (keyword plus vector) and re-ranking improve relevance, but each adds work to every query and so adds latency. The guide's own sample shows how these trade off: 80 queries per second over 100 million items, latency the most critical metric, and up-front development cost acceptable if it buys accuracy without hurting latency. The official answer is a fine-tuned custom embedding model on a standard endpoint with hybrid search and re-ranking turned off. The reasoning is that a standard endpoint keeps query latency low, the extra re-ranking and hybrid steps would cost latency on every query, and fine-tuning the embedding model moves the accuracy gain into a one-time development cost instead.

## 4. Serving: Foundation Model APIs and batch inference with ai_query()

Foundation Model APIs serve Databricks-hosted models either pay-per-token (shared capacity, good for development and variable traffic) or with provisioned throughput (dedicated capacity, predictable latency, required for some production and compliance cases). External models put third-party providers behind the same endpoint interface.

Not every workload is interactive. "Identify batch inference workloads and apply ai_query() appropriately" is about recognizing jobs like "classify the sentiment of ten million reviews in a table" or "summarize every support ticket from last month". `ai_query()` is a SQL function that sends each row to a serving endpoint and returns the result as a column, so a batch job is a single SQL statement or a scheduled job rather than a loop of API calls. The signs that a question wants `ai_query()` are a table as input, no user waiting for each answer, and a large row count.

## 5. Persistent memory and structured state

Agents that hold a conversation over days, or remember facts about a user, need state that outlives a single request. The guide's objective is to "configure a persistent datastore to store and retrieve intermediate memory or structured information". On Databricks the usual answer is a managed transactional database (Lakebase, Databricks' managed Postgres) for short-term conversation state and long-term memories, with Delta tables for analytical records. The judgment the exam tests is matching store to access pattern: low-latency reads and writes per conversation want a transactional store; large-scale history for analysis wants Delta. Stuffing every past message back into the prompt is not memory; it is a growing cost and context problem.

## 6. CI/CD, prompt versioning and testing components

Generative AI applications have more moving parts than a model file, so the guide asks you to "apply CI/CD best practices such as updating a Vector Search index, promoting prompts across environments, and testing individual components of an agent" and to "apply prompt version control and manage prompt lifecycle".

The MLflow Prompt Registry is the tool for prompts. You register a prompt with `mlflow.genai.register_prompt()`, which stores it as a named Unity Catalog object and creates an immutable, numbered version each time it changes. Aliases such as `staging` and `production` are movable pointers to versions, and the application loads a prompt by alias, for example `mlflow.genai.load_prompt("prompts:/catalog.schema.support@production")`. Promotion means moving the alias after tests pass; rollback means pointing the alias back at the previous version. No code redeploy is needed for either, and the version history is kept. This is why the guide's sample answer is "track prompts as MLflow versions and promote them using aliases" rather than branch merges or overwriting a file.

For the index, CI/CD means the pipeline that writes new chunks to the source table also triggers the index sync (or relies on continuous sync) and then runs retrieval checks. For the agent, test components individually as well as end to end: the retriever on a fixed query set, each tool function with unit tests, and the prompt with an evaluation run, so a failure points at one part instead of "the agent got worse".

## 7. MCP servers

The Model Context Protocol (MCP) is the open standard for exposing tools and data to agents, and the guide asks you to "integrate managed, external, and custom MCP servers based on given application requirements". The three kinds differ by who runs them. **Managed** MCP servers are provided and hosted by Databricks and expose platform capabilities (such as Databricks SQL and Genie) as tools without you running anything; choose them first when the need is a Databricks feature. **External** MCP servers are third-party or self-hosted servers (a SaaS vendor's server, for example) that you register with Databricks and share with your team under governed connections; choose them when the tool already exists outside Databricks. **Custom** MCP servers are ones you build, typically from Databricks Apps templates, to expose your own logic or wrap an internal REST API as MCP tools; choose them when neither of the others covers the requirement. The decision rule is the same as everywhere on this exam: use the most managed option that meets the need. The guide's sample makes the pattern concrete: when Databricks offers a managed server for one data source and a vendor offers an external server (needing an API key) for another, the low-maintenance answer is to configure the managed server by its identifier and register the external one with its connection details, keeping the key in Databricks Secrets. Building one custom server that wraps both adds code you then have to maintain.

## 8. User-facing interfaces

The last Section 4 objective is to "develop an appropriate interactive user facing interface for an agent usage scenario (Apps, Slack, Teams, etc.)". Databricks Apps hosts web applications (Streamlit, Dash, Gradio, React and similar) inside the workspace with Databricks identity and permissions, which suits an internal chat UI or a review tool. Slack or Microsoft Teams integration suits agents that should meet people where they already work, such as an IT helpdesk bot. Whatever the surface, credentials stay on the server side: the guide's sample has a Databricks App whose backend calls the agent endpoint with the app's credentials and enforces each user's identity through the app's authenticated context, rather than a personal access token in browser JavaScript or a public endpoint guarded by an API key in the frontend. The right surface follows the scenario: a data-heavy internal tool points to Apps; a quick-question assistant for a whole company points to the chat platform people already use; a programmatic consumer points to the serving endpoint's REST API with no UI at all.

## Exam tips for this section

Know the two Vector Search endpoint types and their numbers (about 320 million versus about a billion vectors at 768 dimensions, about 250 ms extra latency, no continuous sync on storage-optimized). Recognize batch work and answer `ai_query()`. Promote prompts with registry aliases. Declare resources or use on-behalf-of-user auth rather than embedding tokens. Pick managed MCP, then external, then custom.

## Documentation Links Summary

| Topic | Link |
|-------|------|
| Vector Search | [Vector Search overview](https://docs.databricks.com/aws/en/vector-search/vector-search) |
| Prompt Registry | [Prompt Registry](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/) |
| MCP | [MCP on Databricks](https://docs.databricks.com/aws/en/generative-ai/mcp/) |
| Agent authentication | [Agent authentication](https://docs.databricks.com/aws/en/generative-ai/agent-framework/agent-authentication) |
| Batch inference | [ai_query function](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_query) |
