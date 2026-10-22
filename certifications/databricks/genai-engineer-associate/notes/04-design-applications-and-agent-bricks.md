# Design Applications and Agent Bricks - Databricks GenAI Engineer Associate

## Overview

This note covers **Section 1: Design Applications** of the exam guide live since 2026-03-18, plus the agent-design objectives that the guide files under Section 3 (multi-agent systems that call Genie spaces). Databricks publishes no section weights, so judge importance by the objectives themselves: Section 1 has six, and they set up almost every scenario question on the exam, because a design mistake made here (the wrong task, the wrong component, the wrong Agent Brick) makes every later answer wrong too.

**[📖 Exam guide (March 2026)](https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf)** - the six-section outline
**[📖 Agent Bricks FAQ](https://docs.databricks.com/aws/en/agents/concepts/faq)** - current status of the Agent Bricks offerings
**[📖 Information Extraction](https://docs.databricks.com/aws/en/agents/agent-bricks/info-extraction)** - unstructured documents to structured fields

---

## 1. From a business goal to inputs and outputs

The guide asks you to "translate business use case goals into a description of the desired inputs and outputs for the AI pipeline". This is the first move in every design question, and the exam rewards doing it literally. Before thinking about models or tools, write down what goes in (a customer question plus an account ID, a folder of PDFs, a SQL table of tickets) and what must come out (a one-sentence answer with a citation, a JSON record with five fields, a label from a fixed list). Once the input and output are explicit, most of the remaining choices follow from them.

Take the guide's own sample about an automotive parts assistant that answers billing questions well but fails on shipping dates. The input is a customer question plus `account_id` and `transaction_id`; the output needs a delivery date. The design gap is that nothing in the pipeline supplies delivery dates keyed by transaction. The correct fix is a structured lookup (a feature or online table keyed by `transaction_id` holding the expected delivery date), not a vector store of shipping policies and not fine-tuning. Reading the scenario as "what data must reach the model for this output to be possible" is the skill being tested.

## 2. Selecting the model task

Many questions name a business requirement and ask which NLP task category to evaluate models against. The categories to recognize are summarization (long text to a short gist that keeps the meaning), classification (text to one of a fixed set of labels), extraction or named entity recognition (text to specific fields), question answering (question plus context to an answer), translation, text generation (open-ended writing), and embedding (text to a vector for similarity search). The guide's sample about shrinking a paragraph-long memo to a single-sentence gist is summarization, not "text2text generation" in general and not classification. When two answers both sound plausible, pick the most specific task that matches the output you wrote down in step 1.

## 3. Choosing chain components

A chain is a sequence of components, each with a defined input and output, and the guide asks you to "select chain components for a desired model input and output". The common building blocks are a prompt template (fills variables into instructions), a retriever (turns a query into relevant chunks), a model call (chat or completion), an output parser (turns model text into JSON or a typed object), and tools (functions the model can call). A RAG chain is retriever then prompt then model then parser. A structured-output chain is prompt then model then parser, with no retriever. If a scenario needs data that changes daily, the chain needs a retriever or a tool, not a bigger prompt. If it needs strictly formatted output, it needs a format-eliciting prompt plus a parser, which is also what the first Section 1 objective ("design a prompt that elicits a specifically formatted response") is about: state the format explicitly, give an example, and ask for that format only.

## 4. Defining and ordering tools for multi-stage reasoning

Agents reason in several steps, and the order in which they gather knowledge and take actions matters. The guide's phrase is "define and order tools that gather knowledge or take actions for multi-stage reasoning". A sound order is to gather before acting: look up the customer, then retrieve the relevant policy, then decide, and only then call the tool that changes something (issue the refund, file the ticket). Read-only tools should come first and be safe to repeat; tools with side effects should come last and should require that the earlier steps succeeded. Each tool needs a clear name and a description that says when to use it, because the model chooses tools from those descriptions. On Databricks, tools are commonly Unity Catalog functions (governed SQL or Python functions the agent can call), Vector Search retrievers, Genie spaces for questions over tables, and MCP servers (covered in note 05).

## 5. Agent Bricks: which one solves which problem

The guide asks you to "determine how and when to use Agent Bricks (Knowledge Assistant, Multiagent Supervisor, Information Extraction) to solve problems". Agent Bricks are Databricks' declarative, low-code agents: you describe the task and point at your data, and Databricks builds, evaluates and tunes the agent. The exam tests choosing between the three named ones, so learn what each takes in and gives back.

**Knowledge Assistant** takes a set of documents and produces a question-answering chat agent that cites its sources. Choose it when the requirement is "let people ask questions over our documents and get grounded answers", such as an HR policy assistant or a product manual helper. It does not fill a table and it does not take actions.

**Information Extraction** takes unstructured documents or text and returns structured fields that follow a schema you define, as JSON. Choose it when the requirement is "turn these contracts, invoices or notes into rows with these columns", such as pulling party names, renewal dates and notice periods out of 50,000 contracts. Databricks documents it as available through the Agent Bricks UI, in SQL and through the REST API, and results can be written out by running it in SQL or in a Lakeflow pipeline. If the question says "structured", "fields", "schema" or "table" about unstructured input, this is the answer.

**Multiagent Supervisor** (the docs call it Supervisor Agent) coordinates several existing agents and tools, such as a Genie space for sales figures, a Knowledge Assistant for policies and a Unity Catalog function for actions, and routes each part of a request to the right one. Choose it when one user request spans several specialist capabilities that already exist. It does not replace building those specialists.

A note on currency. The exam guide dated 2026-03-18 names these three. Since then the Databricks documentation has started to label Knowledge Assistant and Supervisor Agent as legacy offerings, recommending Genie Agents for new low-code agents and the Agent Bricks CLI for agents written in code, while Information Extraction remains current. Answer exam questions using the guide's three names and the problem each one solves; in real work, check the current docs before starting a new build.

## 6. Multi-agent systems that use Genie spaces

Section 3 adds the objective "enable multi-agent systems to leverage Genie Spaces or conversational API to retrieve data". A Genie space is a curated natural-language interface over a set of Unity Catalog tables: a business user (or an agent) asks a question in plain English, Genie writes and runs the SQL, and returns the answer. In a multi-agent design, Genie is the right specialist whenever the data is structured and lives in tables, because generating SQL against governed tables is more accurate than retrieving text chunks about numbers. The supervisor sends "what were last quarter's sales by region" to the Genie space, sends "what does our travel policy say about upgrades" to a document agent, and combines the results. Programmatic access goes through the Genie conversation API, which lets an agent or app start a conversation, post questions and read the results. The exam pattern to recognize: numbers and tables mean Genie; documents and prose mean retrieval.

## 7. Exam tips for this section

The most reliable way through a design question is to restate the required output in one line, then eliminate answers that cannot produce it. Prefer the lowest-effort component that meets the requirement: a prompt change before a new chain, an Agent Brick before a hand-built agent, retrieval before fine-tuning. Distinguish the three Agent Bricks by their output (cited answers, structured fields, coordinated delegation). Send structured-data questions to Genie, not to a vector index. Order tools so knowledge-gathering comes before side effects.

## Documentation Links Summary

| Topic | Link |
|-------|------|
| Exam guide | [Generative AI Engineer Associate guide, March 2026](https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf) |
| Agent Bricks status | [Agent Bricks FAQ](https://docs.databricks.com/aws/en/agents/concepts/faq) |
| Information Extraction | [Information Extraction](https://docs.databricks.com/aws/en/agents/agent-bricks/info-extraction) |
| Supervisor Agent | [Supervisor Agent (legacy)](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor) |
| Building agents | [Use agents on Databricks](https://docs.databricks.com/aws/en/agents/custom-agents/build-agents) |
