---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 12 min
---

# 02 Generative AI Apps and Agents in Foundry

Part of Domain 2, **Implement AI solutions by using Microsoft Foundry (55-60%)**: prompts, deploying and testing a model in the portal, a lightweight chat client with the Foundry SDK, and a single agent with a client app.

## Foundry in one picture

- A **Foundry resource** in your Azure subscription holds one or more **projects**.
- A **project** is where you work: deploy models, open playgrounds, build agents, run evaluations, connect data. It has a **project endpoint** of the form `https://<resource>.services.ai.azure.com/api/projects/<project>`.
- The **model catalog** lists models: those **sold directly by Azure** (Azure OpenAI models, and others such as DeepSeek, Llama, Mistral and Microsoft's own) and partner models (for example Claude via Azure Marketplace).
- A **deployment** makes a model callable from the project under a deployment name.
- **Foundry Tools** (formerly Azure AI Services) provide prebuilt speech, language, vision and Content Understanding capabilities.

## Deploy a model and use the playground

The portal flow the exam expects you to know:

1. Create (or open) a project in the Foundry portal.
2. Find a model in the **model catalog**; check its capabilities, region availability and pricing.
3. **Deploy** it, choosing a deployment name and type (for example Global Standard).
4. Open the **chat playground**, set the **system message**, adjust parameters (temperature, max tokens), and test prompts.
5. Use the playground's code view to get sample code with the endpoint for your app.

## Effective system and user prompts

- The **system prompt** (system message, or "instructions" for agents) sets the role, scope, rules, tone and output format for the whole conversation. The **user prompt** is the specific request.
- Good prompts are **specific** (what, for whom, how long, what format), give **context** and **examples** (few-shot), and state **constraints** ("If the answer is not in the provided text, say you don't know").
- Ground answers by including relevant data in the prompt; ask for citations.
- Iterate: change one thing, test, compare.

Example system message for a support assistant:

```text
You are the support assistant for Contoso Outdoor. Answer only questions about
Contoso products and orders, using the information provided. If you don't know,
say so and offer to connect the customer to a human. Keep answers under 100 words
and use a friendly, professional tone.
```

See [Prompt engineering](../../../../learn/concepts/prompt-engineering.md).

## A lightweight chat client with the Foundry SDK

The Foundry SDK for Python is the `azure-ai-projects` package. You create an `AIProjectClient` with the project endpoint and an Entra ID credential, get an OpenAI-compatible client from it, and call the **Responses API**. This is Microsoft's quickstart pattern (as of 2026-10-21):

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Format: "https://resource_name.services.ai.azure.com/api/projects/project_name"
FOUNDRY_PROJECT_ENDPOINT = "your_project_endpoint"

project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

response = openai.responses.create(
    model="gpt-5-mini",   # your deployment name
    input="What is the size of France in square miles?",
)
print(response.output_text)
```

What to recognise in an exam snippet:

- **Endpoint**: the project endpoint, not a raw model URL.
- **Credential**: `DefaultAzureCredential()` uses Microsoft Entra ID (your signed-in identity locally, a managed identity in Azure). Keys are the alternative; Entra ID is preferred.
- **Model**: the **deployment name**.
- **Call**: `responses.create` with `input`; read `output_text`.

To make it a chat client, loop: read the user's line, send it with the conversation so far (or use a server-side **conversation**), print the reply.

## A single agent in the portal

An **agent** in Foundry Agent Service combines a model, **instructions** (the system prompt) and **tools**. In the portal you:

1. Create an agent, pick a deployed model, write instructions.
2. Add tools as needed: knowledge (for example files or Foundry IQ for grounding), code interpreter, function calling, web search where available.
3. Test it in the agent playground; inspect its tool calls and answers.

Agent types in Foundry include **prompt agents** (configured with instructions and tools), **voice prompt agents** and **hosted agents** (your own agent code, such as Microsoft Agent Framework or LangGraph, run by the service).

## A lightweight client app for an agent

Microsoft's quickstart creates an agent version and chats with it in a conversation:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

FOUNDRY_PROJECT_ENDPOINT = "your_project_endpoint"
FOUNDRY_AGENT_NAME = "your-agent-name"

project = AIProjectClient(endpoint=FOUNDRY_PROJECT_ENDPOINT,
                          credential=DefaultAzureCredential())

project.agents.create_version(
    agent_name=FOUNDRY_AGENT_NAME,
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="You are a helpful assistant that answers general questions",
    ),
)

openai = project.get_openai_client(agent_name=FOUNDRY_AGENT_NAME)
conversation = openai.conversations.create()          # holds multi-turn state

response = openai.responses.create(conversation=conversation.id,
                                   input="What is the size of France in square miles?")
print(response.output_text)
response = openai.responses.create(conversation=conversation.id,
                                   input="And what is the capital city?")
print(response.output_text)
```

Key ideas: the agent definition (model + instructions + tools) is stored and **versioned** in the project; the **conversation** keeps the history so the follow-up question ("And what is the capital city?") is understood.

## Check yourself

1. Where do you set the rules and tone that apply to every turn? *(The system message, or the agent's instructions.)*
2. In SDK code, what do you pass as `model`? *(The deployment name.)*
3. What makes a follow-up question work in the agent client? *(The conversation, which keeps prior turns.)*
4. Which credential does the quickstart use, and why? *(`DefaultAzureCredential`, Microsoft Entra ID; avoids handling keys.)*
5. What three things define a prompt agent? *(A model, instructions, tools.)*

## Sources

- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)
- [Foundry quickstart: get started with code](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) (code above, read 2026-10-21)
- [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
