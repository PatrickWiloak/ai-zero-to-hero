---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 30 min
---

# 02 Generative AI Apps and Agents

Domain 2 of AI-103: **Implement generative AI and agentic solutions (30-35%)**, the largest domain. Three skill groups: building generative apps with Foundry, building agents, and optimising and operationalising them. Expect code here: reading a snippet and spotting the missing line, choosing the right tool definition, or picking the step that makes a multi-turn conversation work.

All code in this page uses the **Foundry SDK for Python**, `azure-ai-projects` 2.x (`pip install "azure-ai-projects>=2.3.0"`), which talks to the **Foundry projects (new) API**. Microsoft warns that 2.x code "is incompatible with Azure AI Projects 1.x", so if you meet older samples with `threads` and `runs`, they belong to the classic Assistants-style API, not to what AI-103 tests.

## Connecting an application to a Foundry project

Every app starts the same way: create an `AIProjectClient` from the **project endpoint** and an **Entra ID credential**, then get an **OpenAI-compatible client** from it. That client speaks the **Responses API**, the same shape as OpenAI's own SDK, but routed through your project, its deployments, its guardrails and its tracing.

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Format: "https://resource_name.services.ai.azure.com/api/projects/project_name"
FOUNDRY_PROJECT_ENDPOINT = "your_project_endpoint"

# Create project and openai clients to call Foundry API
project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

# Run a responses API call
response = openai.responses.create(
    model="gpt-5-mini",  # supports all Foundry direct models
    input="What is the size of France in square miles?",
)
if not response.output_text or not response.output_text.strip():
    raise RuntimeError("Response output text was empty.")

print(f"Response output: {response.output_text}")
```

(Microsoft's Foundry SDK quickstart, read 2026-10-22.)

Why it is built this way: the project is the security and governance boundary. Going through `project.get_openai_client()` means the call uses your Entra identity and project roles, hits a deployment the project can see, is filtered by that deployment's guardrail, and shows up in the project's traces. Calling a model endpoint directly with a key bypasses most of that.

What the exam checks in this snippet: `model` is the **deployment name** (here `gpt-5-mini` because the quickstart deploys it under that name); `DefaultAzureCredential` needs you signed in (`az login`) locally or a managed identity in Azure; `output_text` is the convenience property that joins the text output items.

## Building generative applications

### Deploying and consuming different kinds of model

The objective lists LLMs, small models, code models and multimodal models. In Foundry they are all consumed the same way once deployed: same client, same `responses.create`, different `model` value. What changes is what you send and what you ask for:

- **Multimodal**: the `input` becomes a list of messages whose content mixes `input_text` with `input_image` (or audio). Domain 3 shows the shape.
- **Code models**: same call, usually with a lower temperature and a system message that fixes the language and output format.
- **Small models**: same call; you compensate for weaker reasoning with tighter instructions, few-shot examples and structured output.

Because the call is identical, routing between models is a one-line change, which is what makes the cascades and routers later in this page cheap to build.

### Retrieval-augmented generation in an application

RAG is three steps: **retrieve** relevant chunks for the question, **augment** the prompt with them, **generate** an answer constrained to them. Foundry gives you two ways to do it.

**Option 1: RAG in your own code.** You call Azure AI Search, then the model. This gives full control over query type, filters (for example security trimming by user group), how many chunks, and the prompt.

```python
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery
from azure.ai.projects import AIProjectClient

credential = DefaultAzureCredential()
search = SearchClient(
    endpoint="https://<search-service>.search.windows.net",
    index_name="policies",
    credential=credential,
)
project = AIProjectClient(endpoint="your_project_endpoint", credential=credential)
openai = project.get_openai_client()

question = "How many days do I have to return an item without a receipt?"

# Retrieve: hybrid (keyword + vector) with semantic reranking.
# VectorizableTextQuery lets the index's vectorizer embed the question.
results = search.search(
    search_text=question,
    vector_queries=[VectorizableTextQuery(text=question, k_nearest_neighbors=5,
                                          fields="contentVector")],
    query_type="semantic",
    semantic_configuration_name="default",
    select=["title", "content"],
    top=5,
)
sources = "\n\n".join(f"[{r['title']}]\n{r['content']}" for r in results)

# Augment and generate: answer only from the sources, cite them.
response = openai.responses.create(
    model="gpt-5-mini",
    instructions=("Answer only from the sources. Cite the source title in brackets. "
                  "If the sources do not contain the answer, say you don't know."),
    input=f"Sources:\n{sources}\n\nQuestion: {question}",
)
print(response.output_text)
```

(Adapted from Microsoft's Azure AI Search vector quickstart, which uses `SearchClient.search` with `vector_queries` and `query_type="semantic"`, and the Foundry SDK quickstart. The index needs a vectorizer for `VectorizableTextQuery`; with no vectorizer, embed the question yourself and pass a `VectorizedQuery`.)

**Option 2: let an agent retrieve.** Attach an **Azure AI Search tool** (or Foundry IQ, or file search) to a prompt agent, and the agent decides when to search and returns citations. Less code, less control. The agent example later in this page shows it.

The trade-off the exam probes: own-code RAG when you need deterministic retrieval, custom filters or a non-agent app; the agent tool when you want the model to decide when and what to retrieve across a conversation.

### Workflows, tool-augmented flows and multistep reasoning pipelines

A single prompt is rarely the whole solution. The patterns you should recognise:

- **Prompt chaining**: step 1 extracts facts, step 2 drafts, step 3 formats. Each step is a separate call with its own instructions; failures are easy to locate.
- **Routing**: a cheap classifier decides which prompt, model or agent handles the request.
- **Tool-augmented flow**: the model can call functions mid-answer (function calling) and continues with the results.
- **Multistep reasoning pipeline**: plan, execute steps (possibly with tools), verify, then answer. Reasoning models do much of this internally; for others you build it as a chain or a workflow.
- **Declarative workflows** in Foundry Agent Service: visual or YAML definitions that sequence agents and logic, covered under multi-agent below.

### Evaluating models and apps

You evaluate to answer four questions the objective names: does it **fabricate** (groundedness), is it **relevant**, is it **good** (coherence, fluency, similarity to an expected answer), and is it **safe**?

The workflow:

1. Build a test dataset: realistic questions, the context retrieved for each, and where possible a ground-truth answer. Include hard and adversarial cases.
2. Choose evaluators and map dataset fields into them (`{{item.query}}`, `{{item.context}}`, `{{item.response}}`), or evaluate an agent directly so it generates responses during the run (`{{sample.output_items}}`).
3. Run the evaluation in the cloud from the SDK or portal; compare runs across model versions, prompts or agent versions.
4. Read the **reasons** for failures, not just the scores.

Two definitions the exam likes, straight from Microsoft: "Groundedness focuses on the *precision* aspect of the response. It doesn't contain content outside of the grounding context." and "Response completeness focuses on the *recall* aspect ... It doesn't miss critical information compared to the expected response or ground truth." A fabricated detail fails groundedness; a missing step fails completeness. Groundedness needs context; completeness needs ground truth; relevance needs only the query and response.

## Building agents

### What an agent is in Foundry

An agent is a model plus **instructions** (role, goal, rules), plus **tools**, plus a way to track the conversation. The service runs the loop: send the conversation to the model, let it call tools, feed results back, repeat until it answers.

Designing one means deciding four things the objective lists:

- **Role and goal**: who the agent is and what success looks like ("You are the returns assistant for Contoso. Resolve return requests within policy.").
- **Conversation tracking**: server-side **conversations** (the default for multi-turn chat), passing `previous_response_id`, or no state for single-shot tasks.
- **Tool schemas**: each tool's name, description and JSON Schema parameters. The model chooses tools from the descriptions, so they are part of the prompt.
- **Boundaries**: what it must refuse, when it must ask a human, how many steps it may take.

### A prompt agent with a conversation

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

FOUNDRY_PROJECT_ENDPOINT = "your_project_endpoint"
FOUNDRY_AGENT_NAME = "your-agent-name"

project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

# Create the agent (or a new version, if it already exists)
project.agents.create_version(
    agent_name=FOUNDRY_AGENT_NAME,
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="You are a helpful assistant that answers general questions",
    ),
)

# Get an OpenAI client pre-bound to the specified agent
openai = project.get_openai_client(agent_name=FOUNDRY_AGENT_NAME)

# Create a conversation for multi-turn chat
conversation = openai.conversations.create()

response = openai.responses.create(
    conversation=conversation.id,
    input="What is the size of France in square miles?",
)
print(response.output_text)

# Ask a follow-up question in the same conversation
response = openai.responses.create(
    conversation=conversation.id,
    input="And what is the capital city?",
)
print(response.output_text)
```

(Microsoft's Foundry SDK quickstart.)

Two details carry exam questions. First, `get_openai_client(agent_name=...)` binds the client to the agent, so `responses.create` uses the agent's instructions and tools and you do not pass `model`. Second, without `conversation=conversation.id` on the second call, "And what is the capital city?" has no referent: the conversation is what holds the history.

### Function calling: integrating your own APIs

A **function tool** lets the agent ask your application to run code. The service never runs your function; it returns a `function_call` item with arguments, your app executes it, and you send back a `function_call_output` with the matching `call_id`.

```python
import json
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, Tool, FunctionTool
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import FunctionCallOutput, ResponseInputParam

def get_horoscope(sign: str) -> str:
    """Generate a horoscope for the given astrological sign."""
    return f"{sign}: Next Tuesday you will befriend a baby otter."

PROJECT_ENDPOINT = "your_project_endpoint"
AGENT_NAME = "MyAgent"

with AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
) as project:
    # Define a function tool for the model to use
    func_tool = FunctionTool(
        name="get_horoscope",
        parameters={
            "type": "object",
            "properties": {
                "sign": {
                    "type": "string",
                    "description": "An astrological sign like Taurus or Aquarius",
                },
            },
            "required": ["sign"],
            "additionalProperties": False,
        },
        description="Get today's horoscope for an astrological sign.",
        strict=True,
    )

    tools: list[Tool] = [func_tool]

    agent = project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model="gpt-4.1-mini",
            instructions="You are a helpful assistant that can use function tools.",
            tools=tools,
        ),
    )

    with project.get_openai_client(agent_name=agent.name) as openai:
        conversation = openai.conversations.create()

        response = openai.responses.create(
            input="What is my horoscope? I am an Aquarius.",
            conversation=conversation.id,
        )

        input_list: ResponseInputParam = []
        for item in response.output:
            if item.type == "function_call":
                if item.name == "get_horoscope":
                    horoscope = get_horoscope(**json.loads(item.arguments))
                    input_list.append(
                        FunctionCallOutput(
                            type="function_call_output",
                            call_id=item.call_id,
                            output=json.dumps({"horoscope": horoscope}),
                        )
                    )

        # Submit function results and get the final response
        response = openai.responses.create(
            input=input_list,
            conversation=conversation.id,
        )
        print(f"Agent response: {response.output_text}")

        openai.conversations.delete(conversation_id=conversation.id)

    project.agents.delete_version(agent_name=agent.name, agent_version=agent.version)
```

(Microsoft's "Use function calling with Microsoft Foundry agents", read 2026-10-22.)

The rules around it, all from the same page and all testable:

- "Runs expire 10 minutes after creation. Submit your tool outputs before they expire." For slow work, return a status immediately and poll.
- The portal can run agents with function tools but "doesn't support adding, removing, or updating function definitions"; use the SDK or REST.
- If the agent "returns function call but no final answer", you forgot to send the `function_call_output` back.
- Several `function_call` items can arrive in one response; handle each and return all results in one call.
- `strict=True` plus `"required"` and `"additionalProperties": False` makes argument JSON conform to the schema.
- Security: "Treat tool arguments and tool outputs as untrusted input," never put secrets in tool output, apply least privilege to the credential, and "require explicit user confirmation for actions that change data."

### Retrieval tools: grounding an agent in your index

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    AzureAISearchTool,
    PromptAgentDefinition,
    AzureAISearchToolResource,
    AISearchIndexResource,
    AzureAISearchQueryType,
)

PROJECT_ENDPOINT = "your_project_endpoint"
AGENT_NAME = "MyAgent"
SEARCH_CONNECTION_NAME = "my-search-connection"
SEARCH_INDEX_NAME = "my-search-index"

with AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
) as project:
    # Resolve the connection ID from the connection name
    azs_connection = project.connections.get(SEARCH_CONNECTION_NAME)
    connection_id = azs_connection.id

    agent = project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model="gpt-4.1-mini",
            instructions="""You are a helpful assistant. You must always provide citations for
            answers using the tool and render them as: `[message_idx:search_idx†source]`.""",
            tools=[
                AzureAISearchTool(
                    azure_ai_search=AzureAISearchToolResource(
                        indexes=[
                            AISearchIndexResource(
                                project_connection_id=connection_id,
                                index_name=SEARCH_INDEX_NAME,
                                query_type=AzureAISearchQueryType.SIMPLE,
                            ),
                        ]
                    )
                )
            ],
        ),
    )
```

(From Microsoft's "Connect an Azure AI Search index to Foundry agents", read 2026-10-22; the page goes on to stream the response and print `url_citation` annotations.)

Note what the agent references: a **project connection** (resolved by name to an ID) and an **index name**, not a search key in code. `query_type` defaults to `vector_semantic_hybrid` if you omit it; the sample sets `SIMPLE` (keyword). Requiring citations in the instructions is how you make grounding auditable.

### Conversation memory

For memory beyond one conversation, attach the **memory search tool** to a prompt agent (or use the memory store APIs). The service extracts facts from conversations, consolidates duplicates and conflicts with an LLM, and retrieves relevant memories later. Microsoft's guidance is to retrieve stable user profile memory "near the beginning of each conversation" and chat summary memory per turn. Memory is in preview, scoped per user (`{{$userId}}` lets the tool resolve scope from the caller's identity), and is a prompt-injection target: a poisoned memory persists, so screen what goes in with Prompt Shields and test adversarially.

### Integrating other tools

The objective lists APIs, knowledge stores, search, content understanding and custom functions. The mapping:

| Tool type | Use for |
|---|---|
| Function tool | Your own code in your process (business logic, internal APIs) |
| OpenAPI tool | A REST API described by an OpenAPI spec, called by the service |
| MCP tool | A Model Context Protocol server's tools; supports approval before calls |
| Azure AI Search / Foundry IQ | Curated organisational knowledge with citations |
| File search | Documents a user uploads during the interaction |
| Code interpreter | Calculations, data analysis, charts in a sandbox |
| Content Understanding | Structured extraction from documents, images, audio or video inside the agent's flow |
| Toolbox | A curated, reusable set of the above, exposed through an MCP-compatible endpoint |

### Multi-agent orchestration

One agent with twenty tools gets confused; several specialised agents with a few tools each are easier to test and govern. Foundry gives you two ways to orchestrate them.

**Foundry workflows** (preview) are declarative: built visually in the portal or as YAML, they sequence agents and logic. Three patterns are named: **human in the loop** ("asks the user a question and awaits user input to proceed"), **sequential** ("passes the result from one agent to the next in a defined order") and **group chat** ("dynamically passes control between agents based on context or rules"). The orchestration "maps directly onto Agent Framework."

**Microsoft Agent Framework** is the code-first route, with built-in orchestrations: sequential, concurrent, handoff, group chat and Magentic. A sequential pipeline in Python:

```python
import os
from agent_framework.foundry import FoundryChatClient
from agent_framework.orchestrations import SequentialBuilder
from azure.identity import AzureCliCredential

chat_client = FoundryChatClient(
    project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    model=os.environ["FOUNDRY_MODEL"],
    credential=AzureCliCredential(),
)

writer = chat_client.as_agent(
    instructions=(
        "You are a concise copywriter. Provide a single, punchy marketing sentence based on the prompt."
    ),
    name="writer",
)

reviewer = chat_client.as_agent(
    instructions=(
        "You are a thoughtful reviewer. Give brief feedback on the previous assistant message."
    ),
    name="reviewer",
)

# Build sequential workflow: writer -> reviewer
workflow = SequentialBuilder(participants=[writer, reviewer]).build()

events = await workflow.run("Write a tagline for a budget-friendly eBike.")
outputs = events.get_outputs()
```

(From Microsoft Agent Framework "Sequential orchestration", read 2026-10-22; `await` runs inside an async function.)

Choosing a pattern: **sequential** when each step builds on the last (draft, review, translate); **concurrent** when independent specialists work in parallel and you merge results; **handoff** when the conversation should pass to whichever agent owns the topic and return to the user between turns; **group chat** when agents debate or collaborate under a manager; **Magentic** for open-ended tasks where a manager plans and assigns dynamically.

### Autonomous and semi-autonomous workflows with approvals

Autonomy is a dial. The safeguards that let you turn it up:

- **Tool approval.** In Agent Framework, mark a tool `@tool(approval_mode="always_require")`. When the agent wants to call it, the workflow pauses and emits a `request_info` event; your app shows the call to a person and resumes with an approval or rejection:

```python
@tool(approval_mode="always_require")
def execute_database_query(query: str) -> str:
    return f"Query executed successfully: {query}"

database_agent = Agent(
    client=chat_client,
    name="DatabaseAgent",
    instructions="You are a database assistant.",
    tools=[execute_database_query],
)

workflow = SequentialBuilder(participants=[database_agent]).build()

async def process_event_stream(stream):
    responses = {}
    async for event in stream:
        if event.type == "request_info" and event.data.type == "function_approval_request":
            responses[event.request_id] = event.data.to_function_approval_response(approved=True)
    return responses if responses else None
```

  (Same Microsoft page. In a real app, `approved=` comes from the person, not a constant.)

- **Review between agents.** `.with_request_info(agents=["editor"])` pauses after a named agent so a person can review its output before the next agent starts.
- **Long waits.** For approvals that may take hours or days, a long-running hosted agent can suspend and resume on the same task ID (preview), surviving restarts.
- **MCP tool approval.** MCP tools can require approval before each call.
- **Guardrails at tool call and tool response** (Domain 1) and **task adherence** controls catch drift without a person in the loop.

**Worked scenario.** A finance agent reconciles invoices and can post journal entries. Reading and matching invoices is low risk: run autonomously. Posting entries changes the ledger: wrap that tool with approval. Entries over a threshold need a manager: route the approval request to a manager's queue. Every decision is logged in traces with the agent version, which satisfies the audit objective in Domain 1.

### Monitoring, evaluating and error analysis for agents

Once deployed, an agent needs the same three things as any service, plus one more:

- **Traces** of every run: model calls, tool calls with arguments and results, retrieval, latency per step, tokens per step.
- **Agent evaluators** on sampled runs: did it resolve the user's intent, adhere to its task, call the right tool with the right arguments?
- **Safety signals**: guardrail blocks and Prompt Shields detections per agent.
- **Error analysis**: cluster failed or low-scoring runs by cause. Typical buckets are retrieval missed (fix the index or query type), wrong tool chosen (fix tool descriptions), bad arguments (tighten the schema, use strict mode), tool failed (fix the API, add retries), answer ungrounded (tighten instructions, require citations), and loop or timeout (cap steps, simplify the plan).

## Optimising and operationalising

### Tuning generation behaviour

Prompt engineering comes first: a clear role, the task, the constraints, the output format, and a few examples. Then parameters:

- **Temperature** (and top-p): lower for consistent, factual or code output; higher for varied creative output. Change one, not both.
- **Maximum output tokens**: caps length and cost; too low truncates answers.
- **Reasoning effort** on reasoning models: more effort, better answers on hard problems, more latency and tokens. Some reasoning models ignore or reject sampling parameters such as temperature; check the model card.
- **Structured output** (a JSON Schema response format) when downstream code parses the result.

### Reflection, chain-of-thought evaluation and self-critique

A **self-critique loop** asks the model to check its own draft against explicit criteria, then revise. It costs extra calls and pays off when errors are expensive and the criteria are checkable.

```python
draft = openai.responses.create(
    model="gpt-5-mini",
    instructions="Write a customer reply. Use only the facts provided.",
    input=f"Facts:\n{facts}\n\nCustomer message:\n{message}",
).output_text

critique = openai.responses.create(
    model="gpt-5-mini",
    instructions=("Check the reply against the facts. List every claim not supported by the facts, "
                  "any promise the policy does not allow, and any missing answer. "
                  "Reply PASS if there are none."),
    input=f"Facts:\n{facts}\n\nReply:\n{draft}",
).output_text

if critique.strip() != "PASS":
    draft = openai.responses.create(
        model="gpt-5-mini",
        instructions="Revise the reply to fix every issue listed. Use only the facts.",
        input=f"Facts:\n{facts}\n\nReply:\n{draft}\n\nIssues:\n{critique}",
    ).output_text
```

(Original illustration built on the Foundry SDK calls above.)

A cheaper variant uses a small model as the critic. **Chain-of-thought evaluation** means evaluating the reasoning steps, not only the final answer: ask for a step-by-step plan or justification and evaluate whether each step is supported, or inspect the tool-call sequence in traces. Reasoning models keep their internal reasoning hidden; what you evaluate there is the visible plan, tool calls and final answer.

### Observability: tracing, token analytics, safety signals, latency

Foundry gives you two layers of tracing, both stored in the Application Insights resource you connect to the project:

- **Server-side tracing**, which Microsoft calls the recommended starting point: once Application Insights is connected, prompt agents, hosted agents and workflows are traced "without changing your code", with 90 days of history in the portal.
- **Client-side tracing** of your own code with OpenTelemetry, so the spans around the agent call (your retrieval, your business logic) join the same trace.

```python
import os

os.environ["AZURE_EXPERIMENTAL_ENABLE_GENAI_TRACING"] = "true"

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
AGENT_NAME = "MyAgent"

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=endpoint, credential=credential) as project,
):
    # Get the Application Insights connection string from the project
    connection_string = project.telemetry.get_application_insights_connection_string()
    configure_azure_monitor(connection_string=connection_string)

    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("agent-tracing-scenario"):
        agent = project.agents.create_version(
            agent_name=AGENT_NAME,
            definition=PromptAgentDefinition(
                model=os.environ["FOUNDRY_MODEL_NAME"],
                instructions="You are a helpful assistant.",
            ),
        )
        with project.get_openai_client(agent_name=agent.name) as openai:
            conversation = openai.conversations.create()
            response = openai.responses.create(
                conversation=conversation.id,
                input="What is the largest city in France?",
            )
```

(Microsoft's "Add client-side tracing to Foundry agents", read 2026-10-22. Install `azure-ai-projects opentelemetry-sdk azure-core-tracing-opentelemetry azure-monitor-opentelemetry`.)

Details that make good questions:

- Tracing instrumentation is opt-in: set `AZURE_EXPERIMENTAL_ENABLE_GENAI_TRACING=true` **before** instrumenting, or no spans appear.
- Message contents are **not** recorded by default. `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true` turns it on; Microsoft says to enable it in development only unless compliance allows it.
- `@trace_function` from `azure.ai.projects.telemetry` adds a span for your own function and always records its parameters and return value.
- Traces "typically take 2-5 minutes to appear."

From traces you get the four signals in the objective: **token analytics** (input and output tokens per call and per tool round trip), **latency breakdowns** (which span is slow: retrieval, model, tool), **safety signals** (guardrail annotations), and the **tool-call sequence** for error analysis.

### Orchestrating multiple models and hybrid LLM-plus-rules engines

Not every decision needs a large model, and some must not be left to one.

- **Cascade**: try a small model first; escalate to a large model when confidence is low or a validator fails.
- **Router**: a classifier (a small model or plain rules) sends each request to the right model, prompt or agent.
- **Hybrid with rules**: deterministic code handles what must be exact and auditable (eligibility thresholds, tax calculations, policy limits), and the LLM handles language (understanding the request, drafting the reply). The LLM proposes, rules dispose.

**Worked scenario.** A bank's assistant answers questions and can approve fee refunds. Policy says refunds up to $25 are automatic for customers in good standing. Letting the LLM decide eligibility is unauditable. The right design: the LLM extracts the request (amount, reason) as structured output; a rules engine checks the amount and the customer's standing; the LLM drafts the reply with the decision. The rules are testable, the decision is explainable, and the model never has authority it should not have.

## Check yourself

1. A follow-up question ignores the previous turn. What is missing? *(Passing the same `conversation` ID to the second `responses.create` call.)*
2. An agent returns a `function_call` but never answers. *(The app must run the function and send a `function_call_output` with the same `call_id`.)*
3. Your function takes 15 minutes. *(Runs expire after 10 minutes: return a status and poll separately.)*
4. Which evaluator catches an invented warranty term not in the retrieved policy? *(Groundedness.)*
5. Which evaluator catches an answer that skips two required steps from the reference answer? *(Response completeness.)*
6. Traces appear but contain no prompts. *(Content recording is off by default; set `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT`.)*
7. A drafting agent, a legal-review agent and a translation agent must run in order. *(Sequential orchestration.)*
8. A tool deletes customer records. *(Require approval on that tool; least-privilege identity; validate arguments.)*

## Sources (read 2026-10-22)

- [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Foundry SDK quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code)
- [Function calling with Foundry agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling)
- [Connect an Azure AI Search index to Foundry agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/ai-search)
- [Azure AI Search vector quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector)
- [RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)
- [What is memory?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory)
- [Build a workflow in Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow)
- [Agent Framework sequential orchestration](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/sequential)
- [Add a human-in-the-loop approval step](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-human-in-the-loop)
- [Set up tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) and [client-side tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-client-side)
- Background on this site: [Agents explained](../../../../learn/concepts/agents-explained.md), [Tool use and function calling](../../../../learn/concepts/tool-use-and-function-calling.md), [Agent architectures](../../../../build/patterns/agent-architectures.md), [Structured outputs](../../../../learn/concepts/structured-outputs.md), [Evaluate an agent end to end](../../../../build/projects/evaluate-an-agent-end-to-end.md)
