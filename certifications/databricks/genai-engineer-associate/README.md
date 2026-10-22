# Databricks Certified Generative AI Engineer Associate

## Exam Overview

The Databricks Certified Generative AI Engineer Associate certification validates the ability to design, build and deploy LLM-enabled solutions on Databricks: RAG applications, LLM chains and, since the 2026 outline, agents. It covers problem decomposition, model and tool selection, Vector Search, Model Serving, MLflow for the solution lifecycle and Unity Catalog for governance.

**Exam Details:**
- **Exam Code:** Databricks Certified Generative AI Engineer Associate
- **Duration:** 90 minutes
- **Number of Questions:** 45 scored multiple-choice or multiple-selection items (unscored items may be added)
- **Passing Score:** 70% (approximately 32 correct answers)
- **Cost:** $200 USD
- **Delivery:** Online proctored
- **Validity:** 2 years
- **Prerequisites:** None (related training and six months of hands-on experience recommended)
- **Exam guide version:** live since 2026-03-18 ([guide PDF](https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf); checked 2026-10-22)

## Exam Outline

The exam guide covering the version live since **2026-03-18** organizes the exam into **six sections**. Unlike most vendors, **Databricks publishes no weights** for them: the guide lists objectives and nothing else. Some third-party sites circulate a percentage split, but it does not come from Databricks, so treat it as a guess. The most honest proxy for where the questions fall is the number of objectives in each section, shown below; the two sections with the most objectives (Application Development and Assembling and Deploying) are where most of your hours should go.

| Section | Objectives in the guide | What it tests | Notes |
|---|---|---|---|
| 1. Design Applications | 6 | Turning a business goal into inputs and outputs, choosing the model task and chain components, ordering tools, choosing among Agent Bricks | [04](notes/04-design-applications-and-agent-bricks.md) |
| 2. Data Preparation | 8 | Chunking, filtering source content, choosing an extraction package, writing chunks to Delta in Unity Catalog, retrieval evaluation, re-ranking | [01](notes/01-rag-design.md) |
| 3. Application Development | 13 | Frameworks, prompt augmentation, guardrails, model and embedding selection, MLflow and Agent Framework, evaluation versus monitoring, Genie spaces in multi-agent systems | [02](notes/02-rag-implementation.md), [04](notes/04-design-applications-and-agent-bricks.md) |
| 4. Assembling and Deploying Applications | 15 | pyfunc chains, Unity Catalog registration, serving access control, Vector Search configuration, `ai_query()`, persistent memory, CI/CD and prompt versioning, MCP servers, user interfaces | [02](notes/02-rag-implementation.md), [05](notes/05-assembling-deploying-and-mcp.md) |
| 5. Governance | 4 | Masking, guardrails against malicious input, data licensing, mitigating problematic text | [03](notes/03-governance-evaluation.md), [06](notes/06-evaluation-monitoring-and-governance.md) |
| 6. Evaluation and Monitoring | 10 | Choosing models from metrics, MLflow scoring and tracing, judges that need ground truth, inference tables and Agent Monitoring, AI Gateway, cost control, custom scorers, SME feedback | [03](notes/03-governance-evaluation.md), [06](notes/06-evaluation-monitoring-and-governance.md) |

### What changed from the older outline

The previous guide had four domains (RAG design, RAG implementation, governance and evaluation, LLM fundamentals). The current one moves the centre of gravity from RAG pipelines towards **agents in production**. The new material you will not find in older study guides is: Agent Bricks (Knowledge Assistant, Multiagent Supervisor, Information Extraction), Genie spaces as data sources for multi-agent systems, MCP servers (managed, external and custom), the MLflow Prompt Registry with aliases for promotion and rollback, persistent memory stores, `ai_query()` for batch inference, choosing a Vector Search endpoint type by scale, latency and cost, AI Gateway inference and usage tables and rate limits, built-in judges and which of them need ground truth, custom scorers, and incorporating SME feedback. LLM fundamentals are no longer a section of their own, but model selection objectives in Sections 3 and 6 still assume them.

### Section 1: Design Applications

This section is about decisions made before any code. You read a business requirement and turn it into a precise description of what goes into the pipeline and what must come out, then choose the model task (summarization, classification, extraction and so on), the chain components, and the order in which tools gather knowledge before they take actions. It also asks when to reach for an Agent Brick: Knowledge Assistant for cited question answering over documents, Information Extraction for turning unstructured documents into structured fields, and Multiagent Supervisor for coordinating several existing agents. Since the guide was published, Databricks has begun labelling Knowledge Assistant and Supervisor Agent as legacy in its docs; answer exam questions with the guide's names.

### Section 2: Data Preparation

Everything a RAG application knows comes through this pipeline, so this section tests the steps in order: pick the right sources, extract their text with the right package for the format (OCR for scanned images, a PDF library for PDFs, an HTML parser for web pages), strip headers, footers and boilerplate, chunk to suit the document structure and the model's limits, and write the chunks with metadata and a primary key to a Delta table in Unity Catalog that a Vector Search index can sync from. It ends with measuring retrieval on its own and understanding where re-ranking fits.

### Section 3: Application Development

The largest block of everyday engineering judgment. You choose frameworks such as LangChain, augment prompts with context drawn from the user's request, shape prompts until responses match a target, and add guardrails. You select models by reading model cards and experiment metrics, and pick an embedding model whose context length fits your chunks without paying for more. You build agentic systems with MLflow and Agent Framework, explain how evaluation before release differs from monitoring after it, and let multi-agent systems query structured data through Genie spaces.

### Section 4: Assembling and Deploying Applications

The section with the most objectives. It covers coding chains as pyfunc models with pre- and post-processing, the elements a deployable RAG model needs (flavor, embedding model, retriever, dependencies, input example, signature), registering to Unity Catalog, and controlling what a serving endpoint may access. It goes deep on Vector Search (creating and querying indexes, and choosing standard or storage-optimized endpoints and sync modes by size, freshness, latency and cost), serving with Foundation Model APIs, batch inference with `ai_query()`, persistent memory, CI/CD for indexes, prompts and agent components, prompt versioning with the MLflow Prompt Registry, integrating managed, external and custom MCP servers, and choosing a user interface (Databricks Apps, Slack, Teams).

### Section 5: Governance

Four objectives, each a judgment call: masking sensitive values before they reach the model, layering guardrails against malicious input such as prompt injection, respecting the licence and terms of every data source, and recommending how to deal with toxic, biased or sensitive text in a source rather than trusting the model to ignore it.

### Section 6: Evaluation and Monitoring

How you know the application works, before and after launch. You choose models from quantitative metrics, evaluate agents with `mlflow.genai.evaluate()` and tracing, know which built-in judges need ground truth (`Correctness`, `RetrievalSufficiency`, `ToolCallCorrectness`), monitor live endpoints with inference tables and Agent Monitoring, use AI Gateway inference tables, usage tables and rate limits, control cost, write custom scorers, and turn SME feedback into consistent evaluation data by calibrating reviewers on clear rubrics.

## Study Approach

### Phase 1: Foundations (Weeks 1-2)
1. Data preparation: parsing, chunking and writing to Delta in Unity Catalog (note 01)
2. Vector Search, Foundation Model APIs and Agent Framework basics (note 02)
3. Design decisions and Agent Bricks (note 04)

### Phase 2: Build and deploy (Weeks 3-4)
1. Build and deploy a RAG agent end to end, then add a Genie space and an MCP tool
2. Practice prompt versioning with the Prompt Registry and batch inference with `ai_query()` (note 05)
3. Evaluate with built-in and custom scorers, then turn on monitoring (notes 03 and 06)

### Phase 3: Exam prep (Weeks 5-6)
1. Take practice exams and review every wrong answer against the guide's objectives
2. Spend the most time on Sections 3 and 4, which hold the most objectives
3. Re-read the guide's sample questions; several of their answers are counter-intuitive

## Study Resources

- **[Databricks Academy](https://www.databricks.com/learn)** - GenAI learning paths
- **[Exam Guide](https://www.databricks.com/learn/certification/genai-engineer-associate)** - Official exam page
- **[Vector Search Documentation](https://docs.databricks.com/en/generative-ai/vector-search.html)** - Vector Search guide
- **[Foundation Model APIs](https://docs.databricks.com/en/machine-learning/foundation-models/index.html)** - Model serving docs
- **[Mosaic AI Documentation](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents)** - Agent framework guide
- **[RAG Tutorial](https://docs.databricks.com/en/generative-ai/tutorials/ai-cookbook/index.html)** - Hands-on RAG guide

## Tips for Success

1. **No official weights** - study in proportion to the objectives, which puts Sections 3 and 4 first
2. **Agents are now central** - Agent Bricks, Genie spaces, MCP servers and memory are all in scope
3. **Know the Agent Bricks by their output** - cited answers, structured fields, or coordinated delegation
4. **Vector Search configuration** - standard versus storage-optimized endpoints, triggered versus continuous sync, and when hybrid search and re-ranking cost too much latency
5. **Batch means `ai_query()`** - a table of rows with nobody waiting is not a job for a real-time endpoint
6. **Prompts are versioned assets** - register them, promote with aliases, roll back by moving the alias
7. **Judges and ground truth** - `Correctness`, `RetrievalSufficiency` and `ToolCallCorrectness` need it; relevance, groundedness and safety do not
8. **AI Gateway** - inference tables, usage tables and rate limits for anything in production
9. **Governance is judgment** - mask before the model, layer guardrails, respect licences
10. **Hands-on practice** - build, evaluate and deploy at least one agent on Databricks

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Comprehensive reference with documentation links |
| [practice-plan.md](practice-plan.md) | 6-week study schedule with checkboxes |
| [notes/01-rag-design.md](notes/01-rag-design.md) | Section 2: data preparation, chunking, retrieval |
| [notes/02-rag-implementation.md](notes/02-rag-implementation.md) | Sections 3 and 4 basics: Vector Search, serving, Agent Framework, LangChain |
| [notes/03-governance-evaluation.md](notes/03-governance-evaluation.md) | Sections 5 and 6 basics: evaluation and governance |
| [notes/04-design-applications-and-agent-bricks.md](notes/04-design-applications-and-agent-bricks.md) | Section 1: design, tools, Agent Bricks, Genie spaces |
| [notes/05-assembling-deploying-and-mcp.md](notes/05-assembling-deploying-and-mcp.md) | Section 4: endpoints, `ai_query()`, memory, prompt registry, MCP, interfaces |
| [notes/06-evaluation-monitoring-and-governance.md](notes/06-evaluation-monitoring-and-governance.md) | Sections 5 and 6: judges, AI Gateway, monitoring, scorers, SME feedback, masking |
