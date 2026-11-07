# Agent Platform Fundamentals

## What is Agent Platform?

Agent Platform (formerly Vertex AI) is Google Cloud's unified machine learning platform that combines AutoML and AI Platform into a unified API, client library, and user interface, providing tools for every step of the ML workflow.

> **Naming (checked 2026-11-06).** Google renamed Vertex AI to **Gemini Enterprise Agent Platform** on 2026-04-22 ("Agent Platform" for short); Vertex AI Search is now Agent Search and Vertex AI Agent Engine is Agent Runtime ([release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes), [name-change map](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)). Prose here uses the new names. The rename did not reach every identifier: the API host is still `aiplatform.googleapis.com`, IAM roles are still `roles/aiplatform.*`, the ML SDK is still `google.cloud.aiplatform`, and the Gen AI SDK's Agent Search class is still `VertexAISearch`.

### Key Benefits
- **Unified platform**: One place for all ML workflows
- **MLOps integration**: Built-in experiment tracking and model management
- **Scalable infrastructure**: Automatic scaling and optimization
- **Pre-built solutions**: AutoML and pre-trained models
- **Custom development**: Full flexibility for custom models

## Agent Platform Components

### Agent Platform Workbench
**Jupyter-based development environment**

#### Features
- **Managed notebooks**: Fully managed Jupyter instances
- **User-managed notebooks**: More control over environment
- **Built-in libraries**: Pre-installed ML frameworks
- **Data science tools**: Integrated development experience
- **Version control**: Git integration

#### Instance Types
| Type | Description | Use Case |
|------|-------------|----------|
| **Managed** | Google-managed infrastructure | Quick start, experimentation |
| **User-managed** | Custom VM configuration | Production workloads, specific requirements |

### Agent Platform Managed Training
**Scalable model training service**

#### Training Options
- **Custom training**: Your own training code
- **AutoML training**: Automated model development
- **Hyperparameter tuning**: Automated hyperparameter optimization
- **Distributed training**: Multi-GPU and multi-node training

#### Custom Training Example
```python
from google.cloud import aiplatform

# Initialize Agent Platform
aiplatform.init(project='my-project', location='us-central1')

# Create custom training job
job = aiplatform.CustomTrainingJob(
    display_name='my-training-job',
    script_path='train.py',
    container_uri='gcr.io/cloud-aiplatform/training/pytorch-gpu.1-9:latest',
    requirements=['scikit-learn', 'pandas'],
    model_serving_container_image_uri='gcr.io/cloud-aiplatform/prediction/pytorch-gpu.1-9:latest'
)

# Run training
model = job.run(
    dataset=my_dataset,
    replica_count=1,
    machine_type='n1-standard-4',
    accelerator_type='NVIDIA_TESLA_K80',
    accelerator_count=1
)
```

### Agent Platform Endpoints
**Model serving infrastructure**

#### Deployment Options
- **Online prediction**: Real-time inference
- **Batch prediction**: Offline batch processing
- **Private endpoints**: VPC-native serving
- **Multi-model endpoints**: Host multiple models

```python
# Deploy model to endpoint
endpoint = model.deploy(
    machine_type='n1-standard-2',
    min_replica_count=1,
    max_replica_count=10,
    accelerator_type='NVIDIA_TESLA_T4',
    accelerator_count=1
)

# Make predictions
predictions = endpoint.predict(instances=test_data)
```

### Agent Platform Pipelines
**ML workflow orchestration**

#### Pipeline Components
- **Components**: Reusable pipeline steps
- **Experiments**: Track and compare pipeline runs
- **Artifacts**: Track inputs, outputs, and metadata
- **Lineage**: Data and model lineage tracking

```python
from kfp.v2 import dsl
from kfp.v2.dsl import component, pipeline, Input, Output, Dataset, Model

@component(
    base_image='python:3.9',
    packages_to_install=['pandas', 'scikit-learn']
)
def preprocess_data(
    input_data: Input[Dataset],
    output_data: Output[Dataset]
):
    import pandas as pd
    
    # Load and preprocess data
    df = pd.read_csv(input_data.path)
    # ... preprocessing logic
    df.to_csv(output_data.path, index=False)

@component(
    base_image='python:3.9',
    packages_to_install=['scikit-learn']
)
def train_model(
    training_data: Input[Dataset],
    model: Output[Model]
):
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    
    # Train model
    # ... training logic
    
    # Save model
    with open(model.path, 'wb') as f:
        pickle.dump(trained_model, f)

@pipeline(name='ml-pipeline')
def ml_pipeline():
    preprocess_task = preprocess_data(input_data=dataset)
    train_task = train_model(training_data=preprocess_task.outputs['output_data'])
```

### Agent Platform Model Registry
**Model versioning and management**

#### Features
- **Model versioning**: Track model versions
- **Model lineage**: Understand model ancestry
- **Model evaluation**: Compare model performance
- **Model aliases**: Stable references to models

```python
# Register model
model = aiplatform.Model.upload(
    display_name='my-model',
    artifact_uri='gs://my-bucket/model/',
    serving_container_image_uri='gcr.io/cloud-aiplatform/prediction/sklearn-cpu.0-24:latest',
    description='My custom model'
)

# Create model version
model_version = model.upload(
    parent_model=model,
    version_description='Updated model with new features'
)
```

## Generative AI on Agent Platform

### Agent Studio
**Experiment with generative AI models through unified interface**

#### Capabilities
- **Text generation**: Create and edit text content
- **Chat**: Conversational AI applications
- **Code generation**: Programming assistance
- **Multimodal**: Text and image understanding
- **Prompt design**: Test and iterate on prompts
- **Model tuning**: Fine-tune foundation models
- **Model evaluation**: Compare model outputs

#### Studio Components

**Language Section**
- Design and test prompts
- Create structured prompts with examples
- Tune language models with supervised learning
- Evaluate model quality and safety

**Vision Section**
- Image captioning and analysis
- Visual question answering
- Object detection and segmentation
- Image generation with Gemini image models

**Speech Section**
- Speech-to-text conversion
- Text-to-speech synthesis
- Audio understanding

**Conversation Section**
- Build conversational agents
- Multi-turn dialog management
- Context preservation
- Intent classification

### The SDK these notes use

Generative code on Agent Platform goes through the **Google Gen AI SDK** (`pip install --upgrade google-genai`), not the older `vertexai` package. Google deprecated the generative modules of the Vertex AI SDK (`vertexai.generative_models`, `vertexai.language_models`, `vertexai.vision_models`, `vertexai.caching`, `vertexai.tuning`) and removed them from SDK releases after June 24, 2026, so any tutorial that starts with `GenerativeModel(...)` or `TextGenerationModel.from_pretrained(...)` will no longer run. `google-cloud-aiplatform` itself stays: it is still how you run custom training, endpoints and pipelines, which is why both packages appear below.

The client reads its target from the environment, so the samples in this guide never hard-code a project. Set these once:

```bash
export GOOGLE_CLOUD_PROJECT=my-project
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_ENTERPRISE=True
```

```python
from google import genai
from google.genai import types

client = genai.Client()   # or genai.Client(enterprise=True, project="my-project", location="global")
```

You will still see `genai.Client(vertexai=True, ...)` and `GOOGLE_GENAI_USE_VERTEXAI` in some of Google's own samples; the client accepts both spellings of the flag. Blocks later in this guide that show no imports continue from the setup above.

The location matters more than it used to. Current Gemini models are served from `global` and the `us` and `eu` multi-regions rather than from single regions, so older advice to pass `us-central1` no longer applies to them. If a question is about data residency, the answer is a multi-region endpoint (`eu`), because `global` does not pin where processing happens.

### Model Garden

Model Garden is the catalog: Google's first-party models, partner models served as managed APIs, and open-weight models you can deploy yourself. Google names Anthropic Claude, Grok and Mistral AI as partner examples, and DeepSeek, Llama and Qwen as open-weight examples ([model overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)). Partner line-ups change often, so treat the catalog as the source of truth rather than memorizing version numbers. Google's own open family is Gemma, including specialized variants such as ShieldGemma and PaliGemma.

### Foundation Models

The first-party line-up splits by job. The table below is what Google lists as of 2026-11-06 ([model lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions), [pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)). Prices are per 1M tokens, input / output, on the global endpoint.

| Model ID | Role | Token limits | Price | Retires |
|----------|------|--------------|-------|---------|
| `gemini-4-argon` | Frontier model for deep, complex work | 1,048,576 shared by input and output | $2 / $10 through 2026-11-30, then $4 / $20 | Oct 13, 2027 or later |
| `gemini-3.8-flash` | Workhorse: the default in this guide | 1,048,576 in, 65,536 out | $0.75 / $3.75 through 2026-12-31, then $1.50 / $7.50 | Sep 2, 2027 or later |
| `gemini-3.5-flash` | Previous workhorse; supports tuning | 1,048,576 in, 65,536 out | $1.50 / $9 | May 19, 2027 or later |
| `gemini-3.5-flash-lite` | High-volume, low-cost classification, routing and extraction; supports tuning | 1,048,576 in, 65,536 out | $0.30 / $2.50 | Jul 21, 2027 or later |
| `gemini-3.1-flash-image` | Image generation and editing (Nano Banana 2) | See model page | Per image, by resolution | May 28, 2027 or later |
| `veo-3.1-generate-001` | Video generation | n/a | See pricing page | May 4, 2027 or later |
| `gemini-embedding-001` | Text embeddings, up to 3,072 dimensions | 2,048 per input | $0.00015 per 1,000 count | No sooner than May 20, 2028 |
| `gemini-embedding-2` | Multimodal embeddings, up to 3,072 dimensions | 8,192 per input | See pricing page | Not listed |

**Retirement is part of the design.** Every Gemini version has a published retirement date, and Google publishes a recommended replacement for each. The Gemini 2.5 family (`gemini-2.5-pro`, `-flash`, `-flash-lite`) was listed for retirement on October 20, 2026, even though the model catalog still shows it and some vendor samples still name it, so do not start new work on it. Build the assumption in: keep the model ID in configuration and check the lifecycle page before you pin one.

**A note on history.** PaLM 2 (`text-bison`, `chat-bison`) and the Codey models (`code-gecko` and friends) were the first generation on this platform. They were retired on April 21, 2025 and Gemini replaced them; older study material that names them is out of date, and specialized code models no longer exist as a separate category.

#### Generating text

One call does most of the work. Everything optional, including temperature and token limits, moves into a `GenerateContentConfig`:

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a product description for a smartwatch with health monitoring features",
    config=types.GenerateContentConfig(
        system_instruction="You are a concise product copywriter.",
        temperature=0.7,          # randomness; the default on this model is 1.0
        top_p=0.95,               # nucleus sampling
        max_output_tokens=2048,
        stop_sequences=["\n\n"],
    ),
)

print(response.text)
print(response.usage_metadata.total_token_count)
```

Three behaviors of current models trip up people who learned on older ones. First, these models **think** before they answer, and that reasoning is billed as output. `gemini-3.8-flash` takes `thinking_level` of `LOW`, `MEDIUM` (default) or `HIGH`; `gemini-3.5-flash-lite` defaults to minimal thinking for speed. A very small `max_output_tokens` can leave too little room for a useful answer, and lowering the thinking level is the lever when cost or latency matters:

```python
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW),
)
```

Second, not every parameter applies to every model. `gemini-4-argon` ignores custom `temperature`, `top_p` and `top_k`, and returns an error if you set `thinking_budget` or `thinking_level="MINIMAL"`. Read the model's page before assuming a parameter transfers.

Third, safety filtering is opt-in. For `gemini-3.5-flash` and later the default threshold is `OFF`, meaning no automated blocking and no safety metadata in the response, so an application that needs filtering must pass `safety_settings` ([safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters)). A blocked response does not raise an exception: check `response.prompt_feedback.block_reason` and `candidates[0].finish_reason`.

Streaming and async are separate entry points rather than flags:

```python
for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents="Write a guide to setting up a CI/CD pipeline",
):
    print(chunk.text, end="")

# Inside an async function:
# response = await client.aio.models.generate_content(model="gemini-3.8-flash", contents="...")
```

#### Conversations

The chat helper keeps history for you, so each `send_message` carries the earlier turns. What older APIs called `context` is now the system instruction, and few-shot examples are simply earlier turns passed as `history`:

```python
chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a cloud architect assistant specializing in Google Cloud.",
        temperature=0.3,
    ),
    history=[
        types.Content(role="user", parts=[types.Part.from_text(text="What is Agent Platform?")]),
        types.Content(role="model", parts=[types.Part.from_text(text="Agent Platform is Google Cloud's unified AI platform...")]),
    ],
)

print(chat.send_message("What are the benefits of using it?").text)
print(chat.send_message("How does it compare to AWS SageMaker?").text)   # keeps context
print(chat.get_history())
```

Code is not a special case any more. There is no separate code model to choose: `gemini-3.8-flash` handles generation, explanation and review through the same call, usually with a lower temperature for more repeatable output.

#### Embeddings

An embedding turns text into a vector so that similar meanings land close together, which is the basis of semantic search, clustering and RAG. `gemini-embedding-001` returns 3,072 dimensions by default and unifies the older specialized models. Use `output_dimensionality` to trade a little quality for storage, and set `task_type` so documents and queries are embedded for their role:

```python
import numpy as np
from google import genai
from google.genai import types

client = genai.Client()

texts = [
    "Agent Platform is a machine learning platform",
    "BigQuery is a data warehouse",
    "Cloud Storage stores objects",
]

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT",
        output_dimensionality=768,
    ),
)
vectors = [e.values for e in response.embeddings]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(cosine_similarity(vectors[0], vectors[1]))
```

Whatever dimensionality you choose must match the vector index you store it in. Google's REST reference says a `gemini-embedding-001` request carries a single input text while its Python sample passes a list, so if a list call errors, send one text per call ([embeddings guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings)). `text-embedding-004`, `text-embedding-005` and `text-multilingual-embedding-002` retire on April 1, 2027.

#### Multimodal input

All current Gemini models take images, audio, video and PDFs as input through the same call, so there is no separate vision model. You combine parts in `contents`. Use a Cloud Storage URI for large files and raw bytes for small ones:

```python
image = types.Part.from_uri(file_uri="gs://my-bucket/architecture-diagram.png", mime_type="image/png")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=["Explain the components and data flow in this diagram", image],
)
print(response.text)

video = types.Part.from_uri(file_uri="gs://my-bucket/tutorial-video.mp4", mime_type="video/mp4")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=["Summarize the key points of this video", video],
)

with open("screenshot.jpg", "rb") as f:
    screenshot = types.Part.from_bytes(data=f.read(), mime_type="image/jpeg")
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=["Extract all text from this screenshot", screenshot],
)
```

#### Generating images

Imagen was retired on June 30, 2026. Image generation now runs through Gemini image models with `generate_content`, and Google's replacement line-up is `gemini-nano-banana-2.1`, `gemini-3.1-flash-lite-image`, `gemini-3.1-flash-image` and `gemini-3-pro-image`:

```python
from io import BytesIO
from PIL import Image

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="Generate an image of a futuristic city at sunset",
    config=types.GenerateContentConfig(
        response_modalities=[types.Modality.TEXT, types.Modality.IMAGE],
    ),
)

for part in response.candidates[0].content.parts:
    if part.inline_data:
        Image.open(BytesIO(part.inline_data.data)).save("city.png")
```

#### Function calling

Function calling lets the model ask your code to do something. The model never runs anything itself: it returns the function name and arguments, your code runs the function, and you send the result back for the final answer. With the Gen AI SDK the shortest form is to pass a plain Python function, and the SDK calls it for you:

```python
def get_current_weather(location: str) -> str:
    """Returns the current weather.

    Args:
        location: The city and state, e.g. San Francisco, CA
    """
    return "sunny"

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is the weather in Boston?",
    config=types.GenerateContentConfig(tools=[get_current_weather]),
)
print(response.text)
```

When you need to control execution, such as checking an action before it runs, declare the function and handle the turn yourself. This is the loop to understand for the exam:

```python
get_weather = types.FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City and state"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
    },
)
tool = types.Tool(function_declarations=[get_weather])

chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(tools=[tool]),
)
response = chat.send_message("What's the weather like in Boston?")

call = response.function_calls[0]
result = {"location": call.args["location"], "temperature": 72, "conditions": "Partly cloudy"}

response = chat.send_message(
    types.Part.from_function_response(name=call.name, response={"content": result})
)
print(response.text)
```

#### Structured output

When another program will read the answer, ask for JSON and give a schema, so the shape is enforced rather than requested in prose:

```python
import json

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents='Extract the company and price: "Acme Corp offers CloudSync Pro for $99/month."',
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "OBJECT",
            "properties": {
                "company": {"type": "STRING"},
                "price_usd": {"type": "NUMBER"},
            },
            "required": ["company", "price_usd"],
        },
    ),
)
print(json.loads(response.text))
```

### Model Tuning

Tuning adapts a model's weights to labeled examples of your task. Reach for it last: Google's guidance is to find the best prompt first, then tune only if you still see recurring errors or need to shorten prompts to lower inference cost. It does not give the model new facts, so changing information belongs in RAG or grounding.

| Scenario | Fine-tuning | Prompt engineering | RAG |
|----------|-------------|--------------------|-----|
| Domain terminology or strict output format | Yes | Maybe | No |
| Recent information or a large knowledge base | No | No | Yes |
| Few examples available, requirements changing | No | Yes | No |
| Consistent style or tone | Yes | Maybe | No |
| Limited budget | No | Yes | Maybe |

**Which models tune.** Not all of them. Supervised fine-tuning is listed for `gemini-3.5-flash`, `gemini-3.5-flash-lite` and `gemini-3.1-flash-lite`. The `gemini-3.8-flash` and `gemini-4-argon` model pages both say tuning is not supported, so the workhorse in the rest of this guide is not the model you tune here.

**Three methods.** Supervised fine-tuning trains on labeled input and output pairs and suits classification, extraction and strict formatting; it needs hundreds to thousands of examples, and Google suggests starting with 100 to 500. Preference tuning trains on pairs of chosen and rejected responses, which suits subjective goals like tone. Reinforcement learning fine-tuning scores generated reasoning against up to 16 weighted reward functions, and suits verifiable multi-step tasks such as code or SQL generation with dozens to a few hundred prompts. Older material calls the human-feedback approach RLHF; the current product names are the two above ([tuning overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)).

**Adapter or full.** Parameter-efficient (adapter) tuning updates a small subset of parameters, so it trains faster and cheaper on less data. Full fine-tuning updates everything for potentially higher quality on highly complex tasks, at higher tuning and serving cost.

Training data is JSONL in Cloud Storage, one example per line, in the same `contents` shape the API uses ([dataset format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/prepare-data)):

```json
{"systemInstruction": {"parts": [{"text": "Classify ticket urgency as HIGH, MEDIUM or LOW."}]}, "contents": [{"role": "user", "parts": [{"text": "Database is down, customers can't check out"}]}, {"role": "model", "parts": [{"text": "HIGH"}]}]}
```

Jobs for Gemini 3 and later models run on the `us` or `eu` multi-region, so a tuning client sets its location explicitly. The job returns both a model and an endpoint, and you call the endpoint like any other model ([supervised tuning guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use)):

```python
import time
from google import genai
from google.genai import types

client = genai.Client(
    enterprise=True,
    project="my-project",
    location="us",
    http_options=types.HttpOptions(api_version="v1beta1"),
)

tuning_job = client.tunings.tune(
    base_model="gemini-3.5-flash",
    training_dataset=types.TuningDataset(gcs_uri="gs://my-bucket/tuning/train.jsonl"),
    config=types.CreateTuningJobConfig(
        tuned_model_display_name="urgency-classifier-v1",
        validation_dataset=types.TuningValidationDataset(gcs_uri="gs://my-bucket/tuning/val.jsonl"),
        epoch_count=5,
    ),
)

while tuning_job.state in ("JOB_STATE_PENDING", "JOB_STATE_RUNNING"):
    time.sleep(60)
    tuning_job = client.tunings.get(name=tuning_job.name)

response = client.models.generate_content(
    model=tuning_job.tuned_model.endpoint,
    contents="Classify the urgency: Email server responding slowly",
)
print(response.text)
```

### Grounding

**Grounding** connects model responses to external knowledge sources, reducing hallucinations and providing citations.

#### Grounding with Google Search

```python
from google import genai
from google.genai import types

client = genai.Client()

# Initialize model with Google Search grounding
model = "gemini-3.8-flash"

# Create grounding tool
google_search_tool = types.Tool(google_search=types.GoogleSearch())

# Generate with grounding
response = client.models.generate_content(
    model=model,
    contents="What are the latest developments in quantum computing announced in 2024?",
    config=types.GenerateContentConfig(
        tools=[google_search_tool],
        temperature=0.3,
        max_output_tokens=1024,
    ),
)

print(f"Response: {response.text}")

# Access grounding metadata
if response.candidates[0].grounding_metadata:
    grounding_metadata = response.candidates[0].grounding_metadata
    print(f"\nGrounding sources:")
    for chunk in grounding_metadata.grounding_chunks:
        print(f"  - {chunk.web.uri}")
        print(f"    Title: {chunk.web.title}")

    print(f"\nGrounding support: {grounding_metadata.grounding_supports}")
```

#### Grounding with Agent Search

```python
from google import genai
from google.genai import types

client = genai.Client()

# Create Agent Search datastore
# (Done via Console or gcloud CLI)
# gcloud alpha discovery-engine data-stores create my-datastore \
#   --location=global \
#   --collection=default_collection \
#   --industry-vertical=GENERIC

# Agent Search grounding is listed for gemini-4-argon, not for the Flash models.
# The SDK class keeps its old name, VertexAISearch.
vertex_search_tool = types.Tool(
    retrieval=types.Retrieval(
        vertex_ai_search=types.VertexAISearch(
            datastore="projects/my-project/locations/global/collections/default_collection/dataStores/my-datastore"
        )
    )
)

model = "gemini-4-argon"

# Query with grounded responses
response = client.models.generate_content(
    model=model,
    contents="What is our company's return policy for electronics?",
    config=types.GenerateContentConfig(
        tools=[vertex_search_tool],
    ),
)

print(f"Grounded response: {response.text}")

# Get source documents
for chunk in response.candidates[0].grounding_metadata.grounding_chunks:
    print(f"Source: {chunk.retrieved_context.uri}")
    print(f"Content: {chunk.retrieved_context.text[:200]}...")
```

#### Grounding with Custom Data Sources

```python
# Grounding using Vector Search
from google.cloud import aiplatform_v1
from google import genai
import numpy as np

client = genai.Client()

# Step 1: Create vector embeddings of your documents

embedding_model = "gemini-embedding-001"

documents = [
    {
        "id": "doc1",
        "text": "Our return policy allows returns within 30 days...",
        "category": "policy"
    },
    {
        "id": "doc2",
        "text": "Product warranty covers manufacturing defects for 1 year...",
        "category": "warranty"
    },
    # ... more documents
]

# Generate embeddings
for doc in documents:
    embedding = client.models.embed_content(model=embedding_model, contents=[doc["text"]]).embeddings[0]
    doc["embedding"] = embedding.values

# Step 2: Store in Vector Search
# Create index (done via API or Console)

# Step 3: Query-time retrieval
def retrieve_relevant_docs(query, top_k=5):
    # Get query embedding
    query_embedding = client.models.embed_content(model=embedding_model, contents=[query]).embeddings[0].values

    # Search vector index
    # (Simplified - actual implementation uses the Vector Search API)
    similarities = []
    for doc in documents:
        similarity = np.dot(query_embedding, doc["embedding"]) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc["embedding"])
        )
        similarities.append((similarity, doc))

    # Return top-k most similar
    similarities.sort(reverse=True)
    return [doc for _, doc in similarities[:top_k]]

# Step 4: Use retrieved docs as context
query = "What is the return policy?"
relevant_docs = retrieve_relevant_docs(query)

# Build context from retrieved documents
context = "\n\n".join([
    f"[Source {i+1}]\n{doc['text']}"
    for i, doc in enumerate(relevant_docs)
])

# Generate with context
model = "gemini-3.8-flash"
prompt = f"""Based on the following information, answer the question.

Context:
{context}

Question: {query}

Answer:"""

response = client.models.generate_content(
    model=model,
    contents=prompt,
)
print(f"Answer: {response.text}")
print(f"\nSources used:")
for i, doc in enumerate(relevant_docs):
    print(f"  {i+1}. {doc['id']}: {doc['text'][:100]}...")
```

### Extensions and Function Calling

#### API Integration

```python
from google import genai
from google.genai import types
import requests

client = genai.Client()

# Define function to call external API
get_stock_price_func = types.FunctionDeclaration(
    name="get_stock_price",
    description="Get current stock price for a ticker symbol",
    parameters={
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol (e.g., GOOGL, AAPL)"
            }
        },
        "required": ["ticker"]
    }
)

get_exchange_rate_func = types.FunctionDeclaration(
    name="get_exchange_rate",
    description="Get currency exchange rate",
    parameters={
        "type": "object",
        "properties": {
            "from_currency": {
                "type": "string",
                "description": "Source currency code (e.g., USD)"
            },
            "to_currency": {
                "type": "string",
                "description": "Target currency code (e.g., EUR)"
            }
        },
        "required": ["from_currency", "to_currency"]
    }
)

# Create tool
financial_tool = types.Tool(
    function_declarations=[get_stock_price_func, get_exchange_rate_func]
)

# Initialize model
model = "gemini-3.8-flash"
config = types.GenerateContentConfig(tools=[financial_tool])

# Implementation of functions
def get_stock_price(ticker):
    # Call actual financial API
    # response = requests.get(f"https://api.example.com/stock/{ticker}")
    # return response.json()

    # Simulated response
    return {
        "ticker": ticker,
        "price": 142.50,
        "currency": "USD",
        "timestamp": "2024-01-15T10:30:00Z"
    }

def get_exchange_rate(from_currency, to_currency):
    # Call actual exchange rate API
    return {
        "from": from_currency,
        "to": to_currency,
        "rate": 0.85,
        "timestamp": "2024-01-15T10:30:00Z"
    }

# Use model with function calling
chat = client.chats.create(model=model)

response = chat.send_message(
    "What is the current price of Google stock and convert it to Euros?"
)

# Process function calls
while response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call

    # Execute appropriate function
    if function_call.name == "get_stock_price":
        result = get_stock_price(function_call.args["ticker"])
    elif function_call.name == "get_exchange_rate":
        result = get_exchange_rate(
            function_call.args["from_currency"],
            function_call.args["to_currency"]
        )

    # Send result back to model
    response = chat.send_message(
        types.Part.from_function_response(
            name=function_call.name,
            response={"content": result}
        )
    )

# Final natural language response
print(f"Answer: {response.text}")
```

#### Multi-Tool Orchestration

```python
# Define multiple tools for complex workflows
database_query_func = types.FunctionDeclaration(
    name="query_database",
    description="Query the customer database",
    parameters={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "SQL query to execute"},
            "database": {"type": "string", "description": "Database name"}
        },
        "required": ["query", "database"]
    }
)

send_email_func = types.FunctionDeclaration(
    name="send_email",
    description="Send an email to a customer",
    parameters={
        "type": "object",
        "properties": {
            "to": {"type": "string", "description": "Recipient email"},
            "subject": {"type": "string", "description": "Email subject"},
            "body": {"type": "string", "description": "Email body"}
        },
        "required": ["to", "subject", "body"]
    }
)

create_ticket_func = types.FunctionDeclaration(
    name="create_support_ticket",
    description="Create a customer support ticket",
    parameters={
        "type": "object",
        "properties": {
            "customer_id": {"type": "string"},
            "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
            "description": {"type": "string"}
        },
        "required": ["customer_id", "description"]
    }
)

# Create tool with multiple functions
support_tool = types.Tool(
    function_declarations=[database_query_func, send_email_func, create_ticket_func]
)

# Initialize model
model = "gemini-3.8-flash"
config = types.GenerateContentConfig(tools=[support_tool])

# Complex multi-step request
chat = client.chats.create(model=model)
response = chat.send_message(
    """
    Customer John Doe (john@example.com) reported that his order #12345 hasn't arrived.
    Please:
    1. Look up the order status in the database
    2. Create a high-priority support ticket
    3. Send an email to the customer acknowledging the issue
    """
)

# Process multiple function calls
function_responses = []
while True:
    if not response.candidates[0].content.parts[0].function_call:
        break

    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Executing: {function_call.name}")

    # Execute function based on name
    if function_call.name == "query_database":
        result = query_database(function_call.args["query"], function_call.args["database"])
    elif function_call.name == "create_support_ticket":
        result = create_support_ticket(**dict(function_call.args))
    elif function_call.name == "send_email":
        result = send_email(**dict(function_call.args))

    # Send result back
    response = chat.send_message(
        types.Part.from_function_response(
            name=function_call.name,
            response={"content": result}
        )
    )

    function_responses.append({
        "function": function_call.name,
        "result": result
    })

print(f"Final response: {response.text}")
print(f"Functions executed: {len(function_responses)}")
```

### RAG (Retrieval Augmented Generation)

**RAG Architecture** combines generative AI with information retrieval to provide accurate, grounded responses with citations.

#### RAG Components

**1. Document Processing Pipeline**
```python
from google.cloud import storage, documentai_v1
from google import genai
import PyPDF2
import json

client = genai.Client()

# Initialize services
storage_client = storage.Client()
embedding_model = "gemini-embedding-001"

# Step 1: Extract text from documents
def extract_text_from_pdf(gcs_uri):
    """Extract text from PDF in Cloud Storage"""
    bucket_name, blob_name = gcs_uri.replace("gs://", "").split("/", 1)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Download PDF
    pdf_bytes = blob.download_as_bytes()

    # Extract text
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

# Step 2: Chunk documents
def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# Step 3: Generate embeddings
def embed_chunks(chunks, metadata=None):
    """Generate embeddings for text chunks"""
    embedded_chunks = []

    # Batch process for efficiency
    batch_size = 250
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        embeddings = client.models.embed_content(
            model=embedding_model,
            contents=batch,
            config=types.EmbedContentConfig(output_dimensionality=768),
        ).embeddings

        for j, embedding in enumerate(embeddings):
            embedded_chunks.append({
                "text": batch[j],
                "embedding": embedding.values,
                "metadata": metadata[i + j] if metadata else {}
            })

    return embedded_chunks

# Process document
document_uri = "gs://my-bucket/documents/product-manual.pdf"
text = extract_text_from_pdf(document_uri)
chunks = chunk_text(text, chunk_size=500, overlap=50)

metadata = [
    {
        "source": document_uri,
        "chunk_id": i,
        "document_type": "product_manual"
    }
    for i in range(len(chunks))
]

embedded_chunks = embed_chunks(chunks, metadata)
print(f"Processed {len(embedded_chunks)} chunks")
```

**2. Vector Search**

```python
from google.cloud import aiplatform
import json

# Initialize Agent Platform
aiplatform.init(project="my-project", location="us-central1")

# Create Vector Search index
def create_vector_index(embedded_chunks, index_name):
    """Create vector search index"""

    # Prepare data for index
    vectors = []
    for i, chunk in enumerate(embedded_chunks):
        vectors.append({
            "id": str(i),
            "embedding": chunk["embedding"],
            "restricts": [
                {"namespace": "document_type", "allow_list": [chunk["metadata"]["document_type"]]}
            ]
        })

    # Save vectors to GCS
    vectors_file = f"gs://my-bucket/vector-index/vectors.json"
    with open("vectors.json", "w") as f:
        for vector in vectors:
            f.write(json.dumps(vector) + "\n")

    # Upload to GCS
    bucket = storage_client.bucket("my-bucket")
    blob = bucket.blob("vector-index/vectors.json")
    blob.upload_from_filename("vectors.json")

    # Create index
    index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
        display_name=index_name,
        contents_delta_uri=vectors_file,
        dimensions=768,  # must match output_dimensionality on the embedding calls
        approximate_neighbors_count=10,
        distance_measure_type="DOT_PRODUCT_DISTANCE",
        leaf_node_embedding_count=500,
        leaf_nodes_to_search_percent=5,
    )

    return index

# Create index
# index = create_vector_index(embedded_chunks, "document-index-v1")

# Deploy index to endpoint
def deploy_index(index):
    """Deploy index to endpoint"""
    endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
        display_name="document-search-endpoint",
        public_endpoint_enabled=True
    )

    endpoint.deploy_index(
        index=index,
        deployed_index_id="doc_index_deployed",
        display_name="Document Search",
        machine_type="n1-standard-2",
        min_replica_count=1,
        max_replica_count=5
    )

    return endpoint

# endpoint = deploy_index(index)
```

**3. Query and Retrieval**

```python
def search_similar_chunks(query, endpoint, top_k=5):
    """Search for similar chunks using vector similarity"""

    # Generate query embedding
    query_embedding = client.models.embed_content(
        model=embedding_model,
        contents=[query],
        config=types.EmbedContentConfig(output_dimensionality=768),
    ).embeddings[0].values

    # Query index endpoint
    response = endpoint.find_neighbors(
        deployed_index_id="doc_index_deployed",
        queries=[query_embedding],
        num_neighbors=top_k
    )

    # Get matching chunks
    matches = []
    for neighbor in response[0]:
        chunk_id = int(neighbor.id)
        chunk = embedded_chunks[chunk_id]
        matches.append({
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "score": neighbor.distance
        })

    return matches

# Search for relevant information
query = "How do I troubleshoot connectivity issues?"
relevant_chunks = search_similar_chunks(query, endpoint, top_k=5)

for i, chunk in enumerate(relevant_chunks):
    print(f"\n{i+1}. Score: {chunk['score']:.4f}")
    print(f"   Text: {chunk['text'][:200]}...")
    print(f"   Source: {chunk['metadata']['source']}")
```

**4. Generate with Retrieved Context**

```python
from google import genai
from google.genai import types

client = genai.Client()

def rag_query(question, endpoint, model_name="gemini-3.8-flash"):
    """RAG: Retrieve relevant context and generate answer"""

    # Step 1: Retrieve relevant chunks
    relevant_chunks = search_similar_chunks(question, endpoint, top_k=5)

    # Step 2: Build context
    context = "\n\n".join([
        f"[Source {i+1}: {chunk['metadata']['source']}]\n{chunk['text']}"
        for i, chunk in enumerate(relevant_chunks)
    ])

    # Step 3: Generate with context
    model = model_name

    prompt = f"""Answer the question based on the provided context. If the answer is not in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}

Answer:"""

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1024,
            top_p=0.8,
        ),
    )

    return {
        "answer": response.text,
        "sources": [chunk["metadata"] for chunk in relevant_chunks],
        "context_chunks": [chunk["text"] for chunk in relevant_chunks]
    }

# Use RAG system
result = rag_query("How do I troubleshoot connectivity issues?", endpoint)

print(f"Answer: {result['answer']}\n")
print(f"Sources:")
for i, source in enumerate(result['sources']):
    print(f"  {i+1}. {source['source']} (chunk {source['chunk_id']})")
```

**5. Advanced RAG: Hybrid Search**

```python
def hybrid_search(query, endpoint, keyword_index, top_k=10):
    """Combine vector search with keyword search"""

    # Vector search
    vector_results = search_similar_chunks(query, endpoint, top_k=top_k)

    # Keyword search (using BigQuery or Elasticsearch)
    # Simplified example
    keyword_results = []
    query_words = query.lower().split()
    for chunk in embedded_chunks:
        chunk_words = chunk["text"].lower().split()
        overlap = len(set(query_words) & set(chunk_words))
        if overlap > 0:
            keyword_results.append({
                "chunk": chunk,
                "keyword_score": overlap / len(query_words)
            })

    keyword_results.sort(key=lambda x: x["keyword_score"], reverse=True)

    # Combine and re-rank
    # Using Reciprocal Rank Fusion (RRF)
    combined_scores = {}

    for i, result in enumerate(vector_results):
        chunk_id = result["metadata"]["chunk_id"]
        combined_scores[chunk_id] = combined_scores.get(chunk_id, 0) + 1 / (i + 1)

    for i, result in enumerate(keyword_results[:top_k]):
        chunk_id = result["chunk"]["metadata"]["chunk_id"]
        combined_scores[chunk_id] = combined_scores.get(chunk_id, 0) + 1 / (i + 1)

    # Sort by combined score
    ranked_chunks = sorted(
        [(chunk_id, score) for chunk_id, score in combined_scores.items()],
        key=lambda x: x[1],
        reverse=True
    )

    return [embedded_chunks[chunk_id] for chunk_id, _ in ranked_chunks[:top_k]]

# Use hybrid search
results = hybrid_search("connectivity troubleshooting", endpoint, None, top_k=5)
```

**6. RAG with Query Rewriting**

```python
def rag_with_query_expansion(question, endpoint):
    """Improve retrieval with query expansion"""

    # Generate alternative query formulations
    model = "gemini-3.8-flash"

    expansion_prompt = f"""Generate 3 alternative ways to ask this question:

Original: {question}

Alternatives (one per line):"""

    response = client.models.generate_content(
        model=model,
        contents=expansion_prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
        ),
    )
    alternative_queries = [q.strip() for q in response.text.split("\n") if q.strip()]

    # Search with all queries
    all_chunks = []
    seen_chunks = set()

    for query in [question] + alternative_queries:
        chunks = search_similar_chunks(query, endpoint, top_k=3)
        for chunk in chunks:
            chunk_id = chunk["metadata"]["chunk_id"]
            if chunk_id not in seen_chunks:
                all_chunks.append(chunk)
                seen_chunks.add(chunk_id)

    # Build context and generate
    context = "\n\n".join([
        f"[Source {i+1}]\n{chunk['text']}"
        for i, chunk in enumerate(all_chunks[:10])
    ])

    prompt = f"""Based on the context, answer the question.

Context:
{context}

Question: {question}

Answer:"""

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    return response.text

# Use query expansion
answer = rag_with_query_expansion(
    "What should I do if the device won't connect?",
    endpoint
)
print(f"Answer: {answer}")
```

**7. RAG Evaluation**

```python
def evaluate_rag_system(test_questions, endpoint):
    """Evaluate RAG system quality"""

    results = []

    for question_data in test_questions:
        question = question_data["question"]
        expected_answer = question_data.get("expected_answer")

        # Get RAG result
        result = rag_query(question, endpoint)

        # Evaluate retrieval
        relevant_retrieved = any(
            source["chunk_id"] in question_data.get("relevant_chunks", [])
            for source in result["sources"]
        )

        # Evaluate answer quality (using model)
        model = "gemini-3.8-flash"
        eval_prompt = f"""Evaluate if the answer correctly addresses the question.

Question: {question}
Answer: {result['answer']}
Expected: {expected_answer}

Is the answer correct and complete? (YES/NO):"""

        eval_response = client.models.generate_content(
            model=model,
            contents=eval_prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
            ),
        )

        results.append({
            "question": question,
            "retrieval_success": relevant_retrieved,
            "answer_quality": eval_response.text.strip(),
            "num_sources": len(result["sources"])
        })

    # Calculate metrics
    retrieval_success_rate = sum(r["retrieval_success"] for r in results) / len(results)
    print(f"Retrieval Success Rate: {retrieval_success_rate:.2%}")

    return results

# Test RAG system
test_cases = [
    {
        "question": "How do I reset the device?",
        "expected_answer": "Press and hold the power button for 10 seconds",
        "relevant_chunks": [5, 12, 23]
    },
    # ... more test cases
]

# evaluation_results = evaluate_rag_system(test_cases, endpoint)
```

### Enterprise Features

#### Private Endpoints

```python
from google.cloud import aiplatform

# Initialize with VPC configuration
aiplatform.init(
    project="my-project",
    location="us-central1",
)

# Deploy model with private endpoint
def deploy_private_endpoint(model, vpc_network):
    """Deploy model to private VPC endpoint"""

    # Create private endpoint
    endpoint = aiplatform.Endpoint.create(
        display_name="private-genai-endpoint",
        network=f"projects/{PROJECT_NUMBER}/global/networks/{vpc_network}",
        encryption_spec_key_name=f"projects/{PROJECT_ID}/locations/{LOCATION}/keyRings/{KEY_RING}/cryptoKeys/{KEY}"
    )

    # Deploy model
    endpoint.deploy(
        model=model,
        deployed_model_display_name="private-model",
        machine_type="n1-standard-4",
        min_replica_count=2,
        max_replica_count=10,
        traffic_split={"0": 100},
        enable_access_logging=True
    )

    return endpoint

# Use private endpoint
private_endpoint = deploy_private_endpoint(
    model,
    vpc_network="my-vpc"
)

# Prediction from within VPC
prediction = private_endpoint.predict(instances=data)
```

#### VPC Peering and Private Service Connect

```python
# Configure VPC peering for Agent Platform
# (Done via gcloud or Console)

# gcloud compute networks peerings create vertex-ai-peering \
#     --network=my-vpc \
#     --peer-project=vertex-ai-project \
#     --peer-network=vertex-ai-network \
#     --import-custom-routes \
#     --export-custom-routes

# Use Private Service Connect
from google.cloud import aiplatform

# Create endpoint with PSC
psc_endpoint = aiplatform.Endpoint.create(
    display_name="psc-genai-endpoint",
    private_service_connect_config={
        "enable_private_service_connect": True,
        "project_allowlist": [PROJECT_ID]
    }
)

# Access via Private Service Connect attachment
# Requests stay within Google's network
```

#### Data Residency and Compliance

```python
# Specify data residency requirements
from google import genai

client = genai.Client()


# Load model from specific region

model = "gemini-3.8-flash"

# Predictions processed in specified region
response = client.models.generate_content(
    model=model,
    contents="Sensitive data processing...",
)

# Tuning job and tuned model stay in the EU multi-region
tuning_job = client.tunings.tune(
    base_model="gemini-3.5-flash",
    training_dataset=types.TuningDataset(gcs_uri="gs://eu-bucket/training-data.jsonl"),
    config=types.CreateTuningJobConfig(tuned_model_display_name="eu-compliant-model"),
)
```

#### Security and Encryption

```python
from google.cloud import aiplatform
from google.cloud import kms_v1

# Customer-Managed Encryption Keys (CMEK)
def deploy_with_cmek(model):
    """Deploy model with CMEK encryption"""

    # KMS key resource name
    kms_key = f"projects/{PROJECT_ID}/locations/{LOCATION}/keyRings/{KEY_RING}/cryptoKeys/{KEY}"

    # Create endpoint with CMEK
    endpoint = aiplatform.Endpoint.create(
        display_name="cmek-encrypted-endpoint",
        encryption_spec_key_name=kms_key
    )

    # Deploy model
    endpoint.deploy(
        model=model,
        deployed_model_display_name="encrypted-model",
        machine_type="n1-standard-4"
    )

    return endpoint

# VPC Service Controls
# Define security perimeter
from google.cloud import accesscontextmanager_v1

def create_service_perimeter():
    """Create VPC Service Controls perimeter"""

    client = accesscontextmanager_v1.AccessContextManagerClient()

    perimeter = {
        "name": f"accessPolicies/{POLICY_ID}/servicePerimeters/vertex_ai_perimeter",
        "title": "Agent Platform Perimeter",
        "perimeter_type": "PERIMETER_TYPE_REGULAR",
        "status": {
            "resources": [
                f"projects/{PROJECT_NUMBER}"
            ],
            "restricted_services": [
                "aiplatform.googleapis.com"
            ],
            "vpc_accessible_services": {
                "enable_restriction": True,
                "allowed_services": [
                    "aiplatform.googleapis.com",
                    "storage.googleapis.com"
                ]
            }
        }
    }

    # Create perimeter
    # operation = client.create_service_perimeter(...)
    return perimeter

# Audit logging
def enable_audit_logging():
    """Enable comprehensive audit logging"""

    # Cloud Logging configuration
    logging_config = {
        "log_type": "DATA_ACCESS",
        "exempted_members": []
    }

    # All Agent Platform API calls logged
    # View in Cloud Logging:
    # resource.type="aiplatform.googleapis.com/Endpoint"
    # protoPayload.methodName="google.cloud.aiplatform.v1.PredictionService.Predict"
```

#### Identity and Access Management

```python
# IAM roles for Agent Platform Gen AI
from google.cloud import resourcemanager_v3

def configure_iam_for_genai():
    """Configure IAM roles for Gen AI workloads"""

    # Predefined roles
    roles = {
        "roles/aiplatform.user": "Use Agent Platform resources",
        "roles/aiplatform.admin": "Full Agent Platform administration",
        "roles/aiplatform.modelUser": "Use deployed models",
        "roles/aiplatform.viewer": "View Agent Platform resources",
        "roles/aiplatform.featurestoreUser": "Access feature store",
        "roles/aiplatform.customCodeServiceAgent": "Custom code execution"
    }

    # Grant model user access to service account
    # gcloud projects add-iam-policy-binding PROJECT_ID \
    #     --member="serviceAccount:genai-app@PROJECT_ID.iam.gserviceaccount.com" \
    #     --role="roles/aiplatform.user"

    # Fine-grained permissions with custom role
    custom_permissions = [
        "aiplatform.endpoints.predict",
        "aiplatform.endpoints.get",
        "aiplatform.models.get"
    ]

    # Create custom role
    # gcloud iam roles create genaiModelUser \
    #     --project=PROJECT_ID \
    #     --permissions=aiplatform.endpoints.predict,aiplatform.endpoints.get

# Workload Identity for GKE
def configure_workload_identity():
    """Configure Workload Identity for Agent Platform access from GKE"""

    # Link Kubernetes SA to Google SA
    # gcloud iam service-accounts add-iam-policy-binding \
    #     genai-app@PROJECT_ID.iam.gserviceaccount.com \
    #     --role roles/iam.workloadIdentityUser \
    #     --member "serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KSA_NAME]"

    # Use from pod
    k8s_manifest = """
apiVersion: v1
kind: ServiceAccount
metadata:
  name: genai-app-sa
  annotations:
    iam.gke.io/gcp-service-account: genai-app@PROJECT_ID.iam.gserviceaccount.com
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: genai-app
spec:
  template:
    spec:
      serviceAccountName: genai-app-sa
      containers:
      - name: app
        image: gcr.io/PROJECT_ID/genai-app:latest
"""
```

#### Rate Limiting and Quotas

```python
# Implement rate limiting for Gen AI endpoints
from functools import wraps
import time
from collections import deque
from google import genai

client = genai.Client()

class RateLimiter:
    """Token bucket rate limiter"""

    def __init__(self, requests_per_minute=60):
        self.requests_per_minute = requests_per_minute
        self.requests = deque()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove requests older than 1 minute
            while self.requests and self.requests[0] < now - 60:
                self.requests.popleft()

            # Check if rate limit exceeded
            if len(self.requests) >= self.requests_per_minute:
                sleep_time = 60 - (now - self.requests[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)

            # Record request
            self.requests.append(time.time())

            return func(*args, **kwargs)

        return wrapper

# Use rate limiter
@RateLimiter(requests_per_minute=60)
def call_genai_model(prompt):
    model = "gemini-3.8-flash"
    return client.models.generate_content(
        model=model,
        contents=prompt,
    )

# Monitor quotas
from google.cloud import monitoring_v3

def check_quota_usage():
    """Monitor Agent Platform API quota usage"""

    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{PROJECT_ID}"

    # Query quota metrics
    interval = monitoring_v3.TimeInterval(
        {
            "end_time": {"seconds": int(time.time())},
            "start_time": {"seconds": int(time.time()) - 3600},
        }
    )

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": 'metric.type="serviceruntime.googleapis.com/quota/rate/net_usage" AND resource.service="aiplatform.googleapis.com"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )

    for result in results:
        print(f"Quota: {result.metric.labels['quota_metric']}")
        for point in result.points:
            print(f"  Usage: {point.value.int64_value}")

# check_quota_usage()
```

### Agent Platform Gen AI Scenarios

#### Scenario 1: Enterprise Document Q&A System

```python
"""
Scenario: Build a Q&A system for internal company documentation
Requirements:
- Process 10,000+ internal documents
- Provide accurate answers with citations
- Support multiple document formats (PDF, DOCX, HTML)
- Maintain data privacy and security
- Scale to handle 1000+ concurrent users
"""

from google import genai
from google.genai import types
from google.cloud import storage, aiplatform
import PyPDF2
from docx import Document

client = genai.Client()

class EnterpriseDocumentQA:
    def __init__(self, project_id, location="us-central1"):
        self.project_id = project_id
        self.location = location

        # Initialize models
        aiplatform.init(project=project_id, location=location)
        self.embedding_model = "gemini-embedding-001"
        self.generation_model = "gemini-3.8-flash"

        # Storage
        self.storage_client = storage.Client()
        self.document_chunks = []

    def process_documents(self, gcs_folder_uri):
        """Process all documents in GCS folder"""

        # Extract bucket and prefix
        bucket_name = gcs_folder_uri.replace("gs://", "").split("/")[0]
        prefix = "/".join(gcs_folder_uri.replace("gs://", "").split("/")[1:])

        bucket = self.storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)

        for blob in blobs:
            if blob.name.endswith('.pdf'):
                text = self._extract_pdf(blob)
            elif blob.name.endswith('.docx'):
                text = self._extract_docx(blob)
            elif blob.name.endswith('.html'):
                text = self._extract_html(blob)
            else:
                continue

            # Chunk and embed
            chunks = self._chunk_document(text, blob.name)
            self.document_chunks.extend(chunks)

        # Create vector index
        self._create_vector_index()

    def _chunk_document(self, text, source):
        """Chunk document intelligently"""
        # Split by paragraphs
        paragraphs = text.split('\n\n')

        chunks = []
        current_chunk = ""

        for para in paragraphs:
            if len(current_chunk) + len(para) < 1000:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append({
                        "text": current_chunk.strip(),
                        "source": source
                    })
                current_chunk = para + "\n\n"

        if current_chunk:
            chunks.append({"text": current_chunk.strip(), "source": source})

        return chunks

    def answer_question(self, question):
        """Answer question using RAG"""

        # Retrieve relevant chunks
        relevant_chunks = self._retrieve_chunks(question, top_k=5)

        # Build context
        context = "\n\n".join([
            f"[Document: {chunk['source']}]\n{chunk['text']}"
            for chunk in relevant_chunks
        ])

        # Generate answer
        prompt = f"""You are an AI assistant helping employees find information in company documents.
Answer the question based on the provided context. Include the document source in your answer.
If the information is not in the context, say so.

Context:
{context}

Question: {question}

Answer:"""

        response = client.models.generate_content(
            model=self.generation_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=1024,
            ),
        )

        return {
            "answer": response.text,
            "sources": [chunk["source"] for chunk in relevant_chunks]
        }

# Usage
qa_system = EnterpriseDocumentQA("my-project")
qa_system.process_documents("gs://my-bucket/internal-docs/")

result = qa_system.answer_question("What is our remote work policy?")
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
```

#### Scenario 2: Code Generation and Review Assistant

```python
"""
Scenario: Build an AI assistant for code generation and review
Requirements:
- Generate code from natural language descriptions
- Review code for bugs and improvements
- Explain complex code sections
- Suggest optimizations
- Support multiple programming languages
"""

from google import genai
from google.genai import types

client = genai.Client()

class CodeAssistant:
    def __init__(self):
        self.code_model = "gemini-3.8-flash"
        self.code_chat = "gemini-3.8-flash"
        self.review_model = "gemini-3.8-flash"

    def generate_code(self, description, language="python"):
        """Generate code from description"""

        prompt = f"""# Language: {language}
# Task: {description}
# Generate complete, production-ready code with error handling and documentation

"""

        response = client.models.generate_content(
            model=self.code_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=2048,
            ),
        )

        return response.text

    def review_code(self, code, focus_areas=None):
        """Review code for issues and improvements"""

        focus = focus_areas if focus_areas else ["bugs", "performance", "security", "best practices"]

        prompt = f"""Review this code and provide feedback on: {', '.join(focus)}

Code:
{code}

Provide:
1. Issues found (with severity: HIGH/MEDIUM/LOW)
2. Suggested improvements
3. Security concerns
4. Performance optimization opportunities

Format as structured report:"""

        response = client.models.generate_content(
            model=self.review_model,
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=2048),
        )

        return response.text

    def explain_code(self, code):
        """Explain complex code"""

        chat = client.chats.create(model=self.code_chat)

        response = chat.send_message(
            f"""Explain this code in detail:

{code}

Include:
1. Purpose and functionality
2. Algorithm or approach used
3. Time and space complexity
4. Potential edge cases"""
        )

        return response.text

    def optimize_code(self, code, optimization_goal="performance"):
        """Optimize code for specific goal"""

        chat = client.chats.create(model=self.code_chat)

        response = chat.send_message(
            f"""Optimize this code for {optimization_goal}:

{code}

Provide:
1. Optimized code
2. Explanation of changes
3. Performance improvements
4. Trade-offs"""
        )

        return response.text

# Usage
assistant = CodeAssistant()

# Generate code
code = assistant.generate_code(
    "Create a rate limiter using token bucket algorithm",
    language="python"
)
print(f"Generated code:\n{code}")

# Review code
review = assistant.review_code(code)
print(f"\nCode review:\n{review}")

# Explain code
explanation = assistant.explain_code(code)
print(f"\nExplanation:\n{explanation}")
```

#### Scenario 3: Multi-Lingual Customer Support Chatbot

```python
"""
Scenario: Build a multi-lingual customer support chatbot
Requirements:
- Support 20+ languages
- Access company knowledge base
- Escalate complex issues to humans
- Track conversation history
- Provide sentiment analysis
"""

from google import genai
from google.genai import types
from google.cloud import translate_v2 as translate
from google.cloud import firestore

client = genai.Client()

class MultiLingualSupportBot:
    def __init__(self, project_id):
        self.project_id = project_id
        self.chat_model = "gemini-3.8-flash"
        self.gemini_model = "gemini-3.8-flash"
        self.translate_client = translate.Client()
        self.db = firestore.Client()

    def start_conversation(self, user_id, language="en"):
        """Start new conversation"""

        conversation = {
            "user_id": user_id,
            "language": language,
            "messages": [],
            "sentiment_scores": [],
            "escalated": False
        }

        doc_ref = self.db.collection("conversations").document()
        doc_ref.set(conversation)

        return doc_ref.id

    def send_message(self, conversation_id, message):
        """Process user message"""

        # Get conversation
        doc_ref = self.db.collection("conversations").document(conversation_id)
        conversation = doc_ref.get().to_dict()

        # Detect language if needed
        if conversation["language"] == "auto":
            detection = self.translate_client.detect_language(message)
            conversation["language"] = detection["language"]

        # Translate to English for processing
        if conversation["language"] != "en":
            translated = self.translate_client.translate(
                message,
                target_language="en"
            )
            message_en = translated["translatedText"]
        else:
            message_en = message

        # Analyze sentiment
        sentiment_score = self._analyze_sentiment(message_en)
        conversation["sentiment_scores"].append(sentiment_score)

        # Check if escalation needed
        if sentiment_score < -0.5 or "speak to manager" in message_en.lower():
            conversation["escalated"] = True
            response = "I understand you're frustrated. Let me connect you with a human agent."

        else:
            # Generate response
            response = self._generate_response(message_en, conversation["messages"])

        # Translate response back
        if conversation["language"] != "en":
            response = self.translate_client.translate(
                response,
                target_language=conversation["language"]
            )["translatedText"]

        # Update conversation
        conversation["messages"].append({
            "user": message,
            "bot": response,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        doc_ref.set(conversation)

        return {
            "response": response,
            "escalated": conversation["escalated"],
            "sentiment": sentiment_score
        }

    def _generate_response(self, message, history):
        """Generate contextual response"""

        # Build conversation context
        context = "You are a helpful customer support agent. Be empathetic and professional."
        if history:
            context += "\n\nPrevious conversation:\n"
            for msg in history[-3:]:  # Last 3 exchanges
                context += f"User: {msg['user']}\nAgent: {msg['bot']}\n"

        chat = client.chats.create(
            model=self.chat_model,
            config=types.GenerateContentConfig(
                system_instruction=context,
            ),
        )
        response = chat.send_message(message)

        return response.text

    def _analyze_sentiment(self, text):
        """Analyze message sentiment"""

        prompt = f"""Analyze the sentiment of this message.
Return a score from -1 (very negative) to +1 (very positive).

Message: {text}

Score (number only):"""

        response = client.models.generate_content(
            model=self.gemini_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=10,
            ),
        )

        try:
            return float(response.text.strip())
        except:
            return 0.0

# Usage
bot = MultiLingualSupportBot("my-project")

# Start conversation
conv_id = bot.start_conversation("user123", language="es")

# Send messages
response1 = bot.send_message(conv_id, "Hola, tengo un problema con mi pedido")
print(f"Bot: {response1['response']}")
print(f"Sentiment: {response1['sentiment']}")

response2 = bot.send_message(conv_id, "El producto no funciona correctamente")
print(f"Bot: {response2['response']}")
```

#### Scenario 4: Content Moderation System

```python
"""
Scenario: Build an AI-powered content moderation system
Requirements:
- Detect harmful content (hate speech, violence, etc.)
- Multi-modal (text and images)
- Provide confidence scores
- Support custom policies
- Handle high throughput (10K+ requests/sec)
"""

from google import genai
from google.genai import types

client = genai.Client()

class ContentModerationSystem:
    def __init__(self):
        self.text_model = "gemini-3.8-flash"
        self.vision_model = "gemini-3.8-flash"

    def moderate_text(self, text, custom_policies=None):
        """Moderate text content"""

        # Use built-in safety settings
        safety_settings = [
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
        ]

        response = client.models.generate_content(
            model=self.text_model,
            contents=text,
            config=types.GenerateContentConfig(
                safety_settings=safety_settings,
            ),
        )

        # Extract safety ratings
        safety_ratings = {}
        for rating in response.candidates[0].safety_ratings:
            safety_ratings[rating.category.name] = {
                "probability": rating.probability.name,
                "blocked": rating.blocked
            }

        # Custom policy check
        policy_violations = []
        if custom_policies:
            policy_violations = self._check_custom_policies(text, custom_policies)

        return {
            "approved": not response.candidates[0].finish_reason.name.startswith("SAFETY"),
            "safety_ratings": safety_ratings,
            "policy_violations": policy_violations,
            "confidence": self._calculate_confidence(safety_ratings)
        }

    def moderate_image(self, image_uri, text_overlay=None):
        """Moderate image content"""

        prompt = """Analyze this image for inappropriate content.
Check for:
1. Nudity or sexual content
2. Violence or gore
3. Hate symbols
4. Illegal activities

Provide a safety rating (SAFE/CAUTION/UNSAFE) and explanation:"""

        parts = [prompt, types.Part.from_uri(file_uri=image_uri, mime_type="image/jpeg")]
        if text_overlay:
            parts.append(f"\nText overlay: {text_overlay}")

        response = client.models.generate_content(
            model=self.vision_model,
            contents=parts,
        )

        # Parse response
        result_text = response.text.lower()
        if "unsafe" in result_text:
            rating = "UNSAFE"
        elif "caution" in result_text:
            rating = "CAUTION"
        else:
            rating = "SAFE"

        return {
            "approved": rating == "SAFE",
            "rating": rating,
            "explanation": response.text,
            "safety_ratings": {
                rating.category.name: rating.probability.name
                for rating in response.candidates[0].safety_ratings
            }
        }

    def _check_custom_policies(self, text, policies):
        """Check against custom company policies"""

        violations = []

        for policy in policies:
            prompt = f"""Check if this text violates the following policy:

Policy: {policy['description']}
Examples of violations: {policy.get('examples', [])}

Text: {text}

Does this violate the policy? (YES/NO):
Explanation:"""

            response = client.models.generate_content(
                model=self.text_model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                ),
            )

            if response.text.strip().upper().startswith("YES"):
                violations.append({
                    "policy": policy["name"],
                    "explanation": response.text
                })

        return violations

    def _calculate_confidence(self, safety_ratings):
        """Calculate overall confidence score"""

        # Simplified confidence calculation
        high_risk_count = sum(
            1 for rating in safety_ratings.values()
            if rating["probability"] in ["HIGH", "MEDIUM"]
        )

        if high_risk_count == 0:
            return 0.95
        elif high_risk_count == 1:
            return 0.75
        else:
            return 0.50

# Usage
moderator = ContentModerationSystem()

# Moderate text
result = moderator.moderate_text(
    "This is a sample message to moderate",
    custom_policies=[
        {
            "name": "no_competitor_mentions",
            "description": "Do not mention competitor products",
            "examples": ["Check out AcmeCorp instead"]
        }
    ]
)

print(f"Approved: {result['approved']}")
print(f"Confidence: {result['confidence']}")
print(f"Safety ratings: {result['safety_ratings']}")
```

## AutoML Services

### AutoML Tables
**Automated machine learning for structured data**

#### Capabilities
- **Classification**: Predict categories
- **Regression**: Predict numerical values
- **Feature engineering**: Automatic feature selection
- **Model selection**: Algorithm selection and tuning

```python
# Create AutoML tabular dataset
dataset = aiplatform.TabularDataset.create(
    display_name='my-tabular-dataset',
    gcs_source='gs://my-bucket/data.csv'
)

# Train AutoML model
job = aiplatform.AutoMLTabularTrainingJob(
    display_name='automl-tabular-training',
    optimization_prediction_type='classification',
    optimization_objective='minimize-log-loss'
)

model = job.run(
    dataset=dataset,
    target_column='target',
    training_fraction_split=0.8,
    validation_fraction_split=0.1,
    test_fraction_split=0.1
)
```

### AutoML Vision
**Automated computer vision models**

#### Model Types
- **Image classification**: Categorize images
- **Object detection**: Detect and locate objects
- **Image segmentation**: Pixel-level image understanding

```python
# Create image dataset
dataset = aiplatform.ImageDataset.create(
    display_name='my-image-dataset',
    gcs_source='gs://my-bucket/images.csv'
)

# Train AutoML image classification model
job = aiplatform.AutoMLImageTrainingJob(
    display_name='automl-image-training',
    prediction_type='classification'
)

model = job.run(
    dataset=dataset,
    model_display_name='my-image-model',
    training_fraction_split=0.8,
    validation_fraction_split=0.1,
    test_fraction_split=0.1
)
```

### AutoML Natural Language
**Automated NLP models**

#### Capabilities
- **Text classification**: Categorize text documents
- **Entity extraction**: Identify and extract entities
- **Sentiment analysis**: Analyze text sentiment

```python
# Create text dataset
dataset = aiplatform.TextDataset.create(
    display_name='my-text-dataset',
    gcs_source='gs://my-bucket/text-data.jsonl'
)

# Train AutoML text classification model
job = aiplatform.AutoMLTextTrainingJob(
    display_name='automl-text-training',
    prediction_type='classification'
)

model = job.run(
    dataset=dataset,
    training_fraction_split=0.8,
    validation_fraction_split=0.1,
    test_fraction_split=0.1
)
```

## MLOps with Agent Platform

### Experiment Tracking
```python
from google.cloud import aiplatform

# Initialize experiment
aiplatform.init(experiment='my-experiment')

# Start experiment run
with aiplatform.start_run('run-1') as run:
    # Log parameters
    run.log_params({
        'learning_rate': 0.01,
        'batch_size': 32,
        'epochs': 100
    })
    
    # Log metrics
    run.log_metrics({
        'accuracy': 0.95,
        'loss': 0.05
    })
    
    # Log artifacts
    run.log_artifact('model.pkl')
```

### Model Monitoring
```python
# Enable model monitoring
monitoring_job = aiplatform.ModelDeploymentMonitoringJob.create(
    display_name='model-monitoring',
    endpoint=endpoint,
    prediction_sampling_rate=0.1,
    monitoring_alert_config=aiplatform.monitoring.EmailAlertConfig(
        user_emails=['admin@company.com']
    ),
    monitoring_objective_configs=[
        aiplatform.monitoring.ObjectiveConfig(
            feature_name='feature1',
            feature_drift_detection_config=aiplatform.monitoring.DriftDetectionConfig(
                drift_threshold=0.05
            )
        )
    ]
)
```

### Feature Store
**Centralized feature management**

```python
# Create feature store
feature_store = aiplatform.Featurestore.create(
    featurestore_id='my-feature-store',
    location='us-central1'
)

# Create entity type
entity_type = feature_store.create_entity_type(
    entity_type_id='user',
    description='User entities'
)

# Create features
feature = entity_type.create_feature(
    feature_id='age',
    value_type='INT64',
    description='User age'
)

# Ingest feature values
entity_type.ingest_from_gcs(
    feature_ids=['age', 'income'],
    gcs_source_uris=['gs://my-bucket/features.csv'],
    entity_id_field='user_id',
    feature_time_field='timestamp'
)
```

## Data Integration

### BigQuery Integration
```python
# Train model with BigQuery data
dataset = aiplatform.TabularDataset.create_from_bigquery(
    display_name='bq-dataset',
    bq_source='bq://my-project.my_dataset.my_table'
)

# Export predictions to BigQuery
batch_job = model.batch_predict(
    job_display_name='batch-prediction',
    bigquery_source='bq://my-project.my_dataset.input_table',
    bigquery_destination_prefix='my-project.my_dataset.predictions'
)
```

### Data Labeling
```python
# Create data labeling job
labeling_job = aiplatform.DataLabelingJob.create(
    display_name='image-labeling',
    datasets=[image_dataset],
    instruction_uri='gs://my-bucket/labeling-instructions.pdf',
    inputs_schema_uri=aiplatform.schema.dataset.ioformat.image.single_label_classification,
    annotation_schema_uri=aiplatform.schema.dataset.annotation.classification
)
```

## Performance Optimization

### Compute Resources
```python
# Specify machine types and accelerators
job = aiplatform.CustomTrainingJob(
    display_name='optimized-training',
    script_path='train.py',
    container_uri='gcr.io/cloud-aiplatform/training/pytorch-gpu.1-9:latest'
)

model = job.run(
    replica_count=4,  # Multi-node training
    machine_type='n1-highmem-16',  # High-memory machine
    accelerator_type='NVIDIA_TESLA_V100',  # GPU acceleration
    accelerator_count=4  # Multiple GPUs
)
```

### Model Optimization
```python
# Hyperparameter tuning
tuning_job = aiplatform.HyperparameterTuningJob(
    display_name='hyperparameter-tuning',
    custom_job=custom_job,
    metric_spec={'accuracy': 'maximize'},
    parameter_spec={
        'learning_rate': hpt.DoubleParameterSpec(min=0.001, max=0.1, scale='log'),
        'batch_size': hpt.IntegerParameterSpec(min=16, max=128, scale='linear')
    },
    max_trial_count=20,
    parallel_trial_count=4
)
```

## Security and Compliance

### IAM and Security
```python
# Service account for Agent Platform
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'path/to/service-account-key.json'
)

aiplatform.init(
    project='my-project',
    location='us-central1',
    credentials=credentials
)
```

### VPC and Network Security
```python
# Deploy with VPC configuration
endpoint = model.deploy(
    machine_type='n1-standard-2',
    network='projects/my-project/global/networks/my-vpc',
    encryption_spec_key_name='projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key'
)
```

#### Scenario 5: Medical Diagnosis Assistant with RAG

```python
"""
Scenario: Build an AI assistant for medical information retrieval
Requirements:
- Access medical literature and guidelines
- Provide evidence-based answers with citations
- Comply with healthcare regulations
- Maintain audit trail
- Support medical terminology
"""

class MedicalDiagnosisAssistant:
    def __init__(self, project_id):
        self.project_id = project_id
        self.embedding_model = "gemini-embedding-001"
        self.model = "gemini-3.8-flash"

        # Load medical knowledge base
        self.medical_kb = self._load_medical_knowledge()

    def query_medical_information(self, query, patient_context=None):
        """Query medical information with context"""

        # Retrieve relevant medical literature
        relevant_docs = self._retrieve_medical_docs(query, top_k=10)

        # Build context
        context = "Medical Literature:\n\n"
        for i, doc in enumerate(relevant_docs):
            context += f"[{i+1}] {doc['title']}\n{doc['content']}\n\n"

        if patient_context:
            context += f"\nPatient Context:\n{patient_context}\n\n"

        # Generate evidence-based response
        prompt = f"""You are a medical information assistant. Provide evidence-based information based on the medical literature provided.

IMPORTANT: Always cite sources and include disclaimers about consulting healthcare professionals.

{context}

Question: {query}

Response (with citations):"""

        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                max_output_tokens=2048,
            ),
        )

        # Log for audit trail
        self._log_query({
            "query": query,
            "response": response.text,
            "sources": [doc['source'] for doc in relevant_docs],
            "timestamp": datetime.now().isoformat()
        })

        return {
            "response": response.text,
            "sources": relevant_docs,
            "disclaimer": "This information is for educational purposes only. Please consult with a healthcare professional."
        }
```

#### Scenario 6: Financial Report Analysis and Summarization

```python
"""
Scenario: Build an AI system for financial report analysis
Requirements:
- Extract key metrics from financial documents
- Generate executive summaries
- Compare year-over-year performance
- Detect anomalies
- Support regulatory compliance
"""

class FinancialReportAnalyzer:
    def __init__(self):
        self.vision_model = "gemini-3.8-flash"
        self.text_model = "gemini-3.8-flash"

    def analyze_financial_report(self, report_uri):
        """Analyze financial report PDF"""

        # Extract data from report
        prompt = """Analyze this financial report and extract:
1. Revenue and profit figures
2. Key performance indicators
3. Year-over-year changes
4. Notable trends
5. Risk factors mentioned

Provide structured output as JSON."""

        report_part = types.Part.from_uri(file_uri=report_uri, mime_type="application/pdf")

        response = client.models.generate_content(
            model=self.vision_model,
            contents=[prompt, report_part],
            config=types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json",
            ),
        )

        financial_data = json.loads(response.text)

        # Generate executive summary
        summary = self._generate_executive_summary(financial_data)

        # Detect anomalies
        anomalies = self._detect_anomalies(financial_data)

        return {
            "data": financial_data,
            "summary": summary,
            "anomalies": anomalies
        }

    def _generate_executive_summary(self, financial_data):
        """Generate executive summary"""

        prompt = f"""Based on this financial data, generate a concise executive summary (3-5 paragraphs):

{json.dumps(financial_data, indent=2)}

Focus on:
- Overall financial health
- Key achievements
- Areas of concern
- Future outlook

Executive Summary:"""

        response = client.models.generate_content(
            model=self.text_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
            ),
        )

        return response.text

    def compare_reports(self, current_report_uri, previous_report_uri):
        """Compare two financial reports"""

        # Analyze both reports
        current_data = self.analyze_financial_report(current_report_uri)
        previous_data = self.analyze_financial_report(previous_report_uri)

        # Generate comparison
        prompt = f"""Compare these two financial reports and provide analysis:

Current Period:
{json.dumps(current_data['data'], indent=2)}

Previous Period:
{json.dumps(previous_data['data'], indent=2)}

Provide:
1. Key changes and trends
2. Performance improvements/declines
3. Strategic insights
4. Recommendations

Analysis:"""

        response = client.models.generate_content(
            model=self.text_model,
            contents=prompt,
        )

        return {
            "current": current_data,
            "previous": previous_data,
            "comparison": response.text
        }
```

#### Scenario 7: Real-Time Translation and Transcription Service

```python
"""
Scenario: Build a real-time translation service for meetings
Requirements:
- Real-time speech transcription
- Multi-language translation
- Speaker identification
- Meeting summarization
- Action item extraction
"""

from google.cloud import speech_v1
from google.cloud import translate_v2
from google import genai
from google.genai import types

client = genai.Client()

class RealTimeTranslationService:
    def __init__(self):
        self.speech_client = speech_v1.SpeechClient()
        self.translate_client = translate_v2.Client()
        self.summarization_model = "gemini-3.8-flash"

    def transcribe_and_translate(self, audio_uri, target_languages):
        """Transcribe audio and translate to multiple languages"""

        # Transcribe with speaker diarization
        config = speech_v1.RecognitionConfig(
            encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
            enable_speaker_diarization=True,
            diarization_speaker_count=5,
            enable_automatic_punctuation=True,
        )

        audio = speech_v1.RecognitionAudio(uri=audio_uri)
        operation = self.speech_client.long_running_recognize(
            config=config,
            audio=audio
        )

        response = operation.result()

        # Extract transcript with speakers
        transcript = []
        for result in response.results:
            alternative = result.alternatives[0]
            for word_info in alternative.words:
                transcript.append({
                    "speaker": word_info.speaker_tag,
                    "word": word_info.word,
                    "start_time": word_info.start_time.total_seconds(),
                    "end_time": word_info.end_time.total_seconds()
                })

        # Translate to target languages
        full_transcript = " ".join([w["word"] for w in transcript])
        translations = {}

        for language in target_languages:
            result = self.translate_client.translate(
                full_transcript,
                target_language=language
            )
            translations[language] = result["translatedText"]

        # Generate meeting summary
        summary = self._generate_meeting_summary(full_transcript)

        # Extract action items
        action_items = self._extract_action_items(full_transcript)

        return {
            "transcript": transcript,
            "full_text": full_transcript,
            "translations": translations,
            "summary": summary,
            "action_items": action_items
        }

    def _generate_meeting_summary(self, transcript):
        """Generate meeting summary"""

        prompt = f"""Summarize this meeting transcript. Include:
1. Main topics discussed
2. Key decisions made
3. Open questions
4. Next steps

Transcript:
{transcript}

Summary:"""

        response = client.models.generate_content(
            model=self.summarization_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            ),
        )

        return response.text

    def _extract_action_items(self, transcript):
        """Extract action items from transcript"""

        prompt = f"""Extract action items from this meeting transcript.
For each action item, provide:
- Task description
- Assigned to (if mentioned)
- Due date (if mentioned)
- Priority

Format as JSON array.

Transcript:
{transcript}

Action Items (JSON):"""

        response = client.models.generate_content(
            model=self.summarization_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json",
            ),
        )

        return json.loads(response.text)
```

#### Scenario 8: E-commerce Product Recommendation Engine

```python
"""
Scenario: Build a personalized product recommendation engine
Requirements:
- Analyze user behavior and preferences
- Generate personalized recommendations
- Create product descriptions
- Handle multi-modal product data (text, images)
- Real-time recommendations
"""

class ProductRecommendationEngine:
    def __init__(self):
        self.embedding_model = "gemini-embedding-001"
        self.generation_model = "gemini-3.8-flash"
        self.vision_model = "gemini-3.8-flash"

    def generate_recommendations(self, user_id, context=None):
        """Generate personalized product recommendations"""

        # Get user profile and history
        user_profile = self._get_user_profile(user_id)
        purchase_history = self._get_purchase_history(user_id)
        browsing_history = self._get_browsing_history(user_id)

        # Generate user embedding
        user_description = f"""
User preferences: {user_profile['preferences']}
Recent purchases: {', '.join([p['name'] for p in purchase_history[:5]])}
Recent views: {', '.join([b['name'] for b in browsing_history[:10]])}
"""

        user_embedding = client.models.embed_content(model=self.embedding_model, contents=[user_description]).embeddings[0].values

        # Find similar products
        candidate_products = self._find_similar_products(user_embedding, top_k=50)

        # Rank and personalize
        prompt = f"""Given this user profile, rank and select the top 10 product recommendations.

User Profile:
{user_description}

Candidate Products:
{json.dumps([p['name'] + ': ' + p['description'] for p in candidate_products], indent=2)}

Context: {context if context else 'General browsing'}

Provide:
1. Top 10 recommended products (with reasoning)
2. Personalized message for each recommendation

Format as JSON:"""

        response = client.models.generate_content(
            model=self.generation_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.5,
                response_mime_type="application/json",
            ),
        )

        recommendations = json.loads(response.text)

        return recommendations

    def generate_product_description(self, product_image_uri, product_data):
        """Generate compelling product description"""

        image_part = types.Part.from_uri(file_uri=product_image_uri, mime_type="image/jpeg")

        prompt = f"""Create a compelling product description for e-commerce.

Product Data:
{json.dumps(product_data, indent=2)}

Generate:
1. Short title (60 characters)
2. Brief description (150 characters)
3. Full description (300 words)
4. Key features (bullet points)
5. SEO keywords

Analyze the product image and incorporate visual details.

Response (JSON):"""

        response = client.models.generate_content(
            model=self.vision_model,
            contents=[prompt, image_part],
            config=types.GenerateContentConfig(
                temperature=0.7,
                response_mime_type="application/json",
            ),
        )

        return json.loads(response.text)

    def analyze_product_reviews(self, reviews):
        """Analyze product reviews for insights"""

        reviews_text = "\n\n".join([
            f"Rating: {r['rating']}/5\nReview: {r['text']}"
            for r in reviews
        ])

        prompt = f"""Analyze these product reviews and provide:
1. Overall sentiment
2. Common positive points
3. Common negative points
4. Suggestions for product improvement
5. Key themes

Reviews:
{reviews_text}

Analysis (JSON):"""

        response = client.models.generate_content(
            model=self.generation_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                response_mime_type="application/json",
            ),
        )

        return json.loads(response.text)
```

## Cost Optimization for Gen AI

### Pricing Models

Gemini bills per token, split by input and output, with output including the model's reasoning. Prices move and two of these are promotional, so check the [pricing page](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing) before quoting one. Global-endpoint prices as of 2026-11-06, per 1M tokens:

| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| `gemini-4-argon` | $2.00 | $10.00 | Through 2026-11-30, then $4 / $20 |
| `gemini-3.8-flash` | $0.75 | $3.75 | Through 2026-12-31, then $1.50 / $7.50 |
| `gemini-3.5-flash` | $1.50 | $9.00 | |
| `gemini-3.5-flash-lite` | $0.30 | $2.50 | |

Non-global (`us`, `eu`) endpoints cost about 10% more on the models where Google publishes both rates. Three discounts change the math at volume. Batch inference runs asynchronously at 50% off. Implicit caching is on by default and gives 90% off cached input tokens, with no storage charge. Explicit caching lets you declare what to cache and adds a storage charge based on how long it is kept. On Gemini 3 and later the batch and cache discounts stack, to 95% off cached input.

### Cost Optimization Strategies

```python
# 1. Reuse a stable prompt prefix: implicit caching applies automatically.
#    This helper just keeps the common context in one place.
class PromptCache:
    """Cache common prompt prefixes"""

    def __init__(self):
        self.cache = {}

    def get_cached_prompt(self, context_key, user_query):
        """Reuse common context"""
        if context_key in self.cache:
            return self.cache[context_key] + user_query
        return user_query

# 2. Optimize token usage
def optimize_prompt(long_prompt):
    """Reduce unnecessary tokens"""

    # Remove extra whitespace
    optimized = " ".join(long_prompt.split())

    # Use abbreviations where appropriate
    # Summarize long examples

    return optimized

# 3. Batch requests
def batch_predictions(prompts, model):
    """Batch multiple predictions"""

    # Combine prompts
    combined_prompt = "\n\n---\n\n".join([
        f"Query {i+1}: {prompt}"
        for i, prompt in enumerate(prompts)
    ])

    # Single API call
    response = client.models.generate_content(
        model=model,
        contents=combined_prompt,
    )

    # Parse responses
    return response.text.split("---")

# 4. Use cheaper models when appropriate
def select_model_by_complexity(task):
    """Choose cost-effective model"""

    if task["requires_reasoning"]:
        return "gemini-3.8-flash"
    elif task["requires_code"]:
        return "gemini-3.8-flash"
    else:
        return "gemini-3.5-flash-lite"

# 5. Implement response caching
from functools import lru_cache
import hashlib
from google import genai

client = genai.Client()

@lru_cache(maxsize=1000)
def get_cached_response(prompt_hash):
    """Cache frequent queries"""
    # Return cached response if available
    pass

def query_with_cache(prompt, model):
    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()

    cached = get_cached_response(prompt_hash)
    if cached:
        return cached

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    get_cached_response.cache_info()  # Monitor cache hits

    return response

# 6. Tune models to reduce prompt size
def compare_costs(base_model, tuned_model, num_requests):
    """Compare costs: prompt engineering vs tuning"""

    # Prompt engineering approach
    long_prompt_cost = (1000 / 1_000_000 * 1.50) * num_requests  # 1,000 input tokens at $1.50 per 1M

    # Tuned model approach
    tuning_cost = 100  # One-time tuning cost
    short_prompt_cost = (100 / 1_000_000 * 1.50) * num_requests

    print(f"Prompt engineering: ${long_prompt_cost:.2f}")
    print(f"Tuned model: ${tuning_cost + short_prompt_cost:.2f}")

    return tuning_cost + short_prompt_cost < long_prompt_cost

# 7. Monitor and optimize
def track_api_costs():
    """Monitor API usage and costs"""

    # Track per-request costs
    costs = {
        "total_input_tokens": 0,
        "total_output_tokens": 0,
        "total_requests": 0
    }

    # Calculate estimated cost
    # gemini-3.8-flash standard rates per 1M tokens, from 2027-01-01
    input_cost = (costs["total_input_tokens"] / 1_000_000) * 1.50
    output_cost = (costs["total_output_tokens"] / 1_000_000) * 7.50

    return input_cost + output_cost
```

## Exam Tips: Agent Platform Gen AI

### Key Exam Topics

**1. Model Selection**
- Choose the right Gemini tier for the job (Argon, Flash, Flash-Lite, image, embedding)
- Understand context window limits
- Know when to use embeddings vs generation
- Multimodal input, which every current Gemini model accepts

**2. Prompt Engineering**
- Few-shot learning with examples
- System instructions and context
- Temperature and sampling parameters
- Stop sequences and constraints

**3. Fine-Tuning**
- When to tune vs prompt engineering
- Training data requirements (100+ examples)
- Adapter tuning vs full fine-tuning
- Evaluation and validation

**4. Grounding and RAG**
- Google Search grounding
- Agent Search integration
- Custom retrieval with Vector Search
- Document chunking strategies

**5. Function Calling**
- Function declaration format
- Multi-turn function calling
- Structured outputs
- API integration patterns

**6. Enterprise Features**
- Private endpoints and VPC
- CMEK encryption
- Data residency
- IAM roles and permissions
- Audit logging

**7. Cost Optimization**
- Model pricing differences
- Prompt optimization
- Caching strategies
- When to use tuned models

### Common Exam Scenarios

**Scenario 1: Choose the Right Model**
- **Question**: "You need to analyze images and generate descriptions. Which model?"
- **Answer**: `gemini-3.8-flash` - every current Gemini model takes image input, so you pick on cost and quality
- **Why Not**: an image model such as `gemini-3.1-flash-image` is built to generate images; use it when the output is a picture

**Scenario 2: Reduce Hallucinations**
- **Question**: "How to reduce hallucinations in generated responses?"
- **Answer**: Use grounding with Google Search or Agent Search
- **Additional**: Lower temperature (0.1-0.3), provide context, use RAG

**Scenario 3: Fine-Tuning Decision**
- **Question**: "When should you fine-tune vs use prompt engineering?"
- **Answer**: Fine-tune for:
  - Domain-specific terminology
  - Consistent output format
  - Reducing prompt length for cost
  - Task-specific performance
- **Prompt Engineering for**:
  - Few examples available
  - Changing requirements
  - Quick experimentation

**Scenario 4: Enterprise Security**
- **Question**: "Deploy Gen AI model with data residency in EU"
- **Answer**:
  ```python
  client = genai.Client(enterprise=True, project="my-project", location="eu")
  tuning_job = client.tunings.tune(
      base_model="gemini-3.5-flash",
      training_dataset=types.TuningDataset(gcs_uri="gs://eu-bucket/data.jsonl"),
  )
  ```

**Scenario 5: RAG Implementation**
- **Question**: "Build Q&A system for company documents"
- **Answer**:
  1. Use `gemini-embedding-001` for embeddings
  2. Store in Vector Search
  3. Retrieve top-k relevant chunks
  4. Use `gemini-3.8-flash` for generation with retrieved context
  5. Implement citation tracking

**Scenario 6: Function Calling**
- **Question**: "Enable model to query database and send emails"
- **Answer**: Use `gemini-3.8-flash` with function declarations
  - Define functions with clear descriptions
  - Handle multi-turn execution
  - Return results to model for natural language response

**Scenario 7: Cost Optimization**
- **Question**: "Reduce costs for high-volume generation workload"
- **Answer**:
  - Use `gemini-3.5-flash-lite` if quality is sufficient
  - Implement response caching
  - Batch requests where possible
  - Optimize prompts to reduce tokens
  - Consider tuning to shorten prompts

### Decision Trees for Exam

**Model Selection Decision Tree**
```
Output is an image?
  YES → gemini-3.1-flash-image (or gemini-3-pro-image for higher quality)
Output is a video?
  YES → veo-3.1-generate-001
Output is a vector for search or RAG?
  YES → gemini-embedding-001
Must tune the model on your own examples?
  YES → gemini-3.5-flash or gemini-3.5-flash-lite
High volume, simple classification or extraction?
  YES → gemini-3.5-flash-lite
Hardest reasoning, cost is secondary?
  YES → gemini-4-argon
Everything else, including chat, code, multimodal input and function calling
  → gemini-3.8-flash
```

**Grounding Decision Tree**
```
Need current information (news, events)?
  YES → Google Search grounding
  NO → Continue

Have custom knowledge base?
  YES → Continue
    Structured data (FAQ, policies)?
      YES → Agent Search
      NO → Continue
    Unstructured documents?
      YES → RAG with Vector Search
      NO → Prompt engineering
  NO → Use base model with prompts
```

**Enterprise Deployment Decision Tree**
```
Data residency requirements?
  YES → Deploy in specific region
  NO → Continue

Private network access only?
  YES → Private endpoints with VPC
  NO → Continue

Need encryption at rest?
  YES → CMEK with Cloud KMS
  NO → Continue

Compliance requirements (HIPAA, SOC 2)?
  YES → VPC Service Controls + audit logging
  NO → Standard deployment
```

### Exam Question Patterns

**Pattern 1: "Which model should you use..."**
- Look for: multimodal, code, conversation, context length clues
- Answer: Match capabilities to requirements

**Pattern 2: "How do you reduce hallucinations..."**
- Look for: factual accuracy, citations needed
- Answer: Grounding (Search or RAG)

**Pattern 3: "What's the most cost-effective..."**
- Look for: high volume, repeated patterns
- Answer: Tuning, caching, cheaper models, optimization

**Pattern 4: "How do you ensure data stays in EU..."**
- Look for: compliance, data residency
- Answer: Region selection, CMEK, VPC SC

**Pattern 5: "Best way to handle..."**
- Look for: specific use case description
- Answer: Match pattern to solution (RAG, function calling, etc.)

### Quick Reference Tables

**Model Capabilities Comparison**
| Feature | `gemini-4-argon` | `gemini-3.8-flash` | `gemini-3.5-flash` | `gemini-3.5-flash-lite` |
|---------|------------------|--------------------|--------------------|-------------------------|
| Image, audio, video input | Yes | Yes | Yes | Yes |
| Function calling | Yes | Yes | Yes | Yes |
| Structured output | Yes | Yes | Yes | Yes |
| Explicit context caching | No (implicit only) | Yes | Yes | Yes |
| RAG Engine | No | Yes | Yes | Yes |
| Supervised tuning | No | No | Yes | Yes |
| Grounding with Google Search | Yes | Yes | Yes | Yes |
| Grounding with Agent Search | Yes | Not listed | Not listed | Not listed |
| Context window | 1,048,576 | 1,048,576 | 1,048,576 | 1,048,576 |

**Common IAM Roles**
| Role | Permissions | Use Case |
|------|------------|----------|
| aiplatform.user | Use endpoints, models | Application access |
| aiplatform.admin | Full admin | Platform management |
| aiplatform.modelUser | Predict only | Production inference |
| aiplatform.viewer | Read-only | Monitoring, auditing |

### Key Formulas and Limits

**Token Limits**
- `gemini-3.8-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`: 1,048,576 context window, 65,536 maximum output
- `gemini-4-argon`: 1,048,576 shared by input and output
- `gemini-embedding-001`: 2,048 per input text

**Cost Calculation**
```
Cost = (input_tokens / 1,000,000) * input_price + (output_tokens / 1,000,000) * output_price

Example, on gemini-3.8-flash at its standard rate ($1.50 / $7.50):
- 5,000 input tokens
- 2,000 output tokens, including thinking

Cost = (5,000 / 1,000,000) * $1.50 + (2,000 / 1,000,000) * $7.50
     = $0.0075 + $0.015
     = $0.0225 per request
```

**Tuning Data Requirements**
- Minimum: 100 examples (recommended: 500+)
- Quality > Quantity
- Balanced dataset
- Representative of production use

## Best Practices

### Development Workflow
1. **Start with AutoML**: Begin with automated solutions
2. **Experiment tracking**: Use Agent Platform experiments
3. **Version control**: Track model and data versions
4. **Gradual complexity**: Start simple, add complexity as needed

### Gen AI Development Best Practices

**1. Prompt Engineering First**
- Test with few-shot examples before tuning
- Iterate on prompts using Agent Studio
- Document successful prompt patterns
- Version control your prompts

**2. Evaluation and Testing**
- Create test datasets with ground truth
- Use model-based evaluation for quality
- Monitor safety scores
- A/B test different approaches

**3. Production Readiness**
- Implement rate limiting
- Add response caching
- Monitor costs and quotas
- Plan for fallbacks

**4. Security and Compliance**
- Use private endpoints for sensitive data
- Enable audit logging
- Implement data filtering
- Regular security reviews

### Production Deployment
1. **Model validation**: Thorough testing before deployment
2. **Monitoring**: Implement comprehensive monitoring
3. **A/B testing**: Compare model versions in production
4. **Rollback strategy**: Plan for model rollbacks

### Cost Optimization
1. **Right-size resources**: Match compute to workload requirements
2. **Use preemptible instances**: For fault-tolerant training
3. **Optimize serving**: Scale endpoints based on demand
4. **Storage management**: Archive old models and data
5. **Model selection**: Use cheaper models when sufficient
6. **Prompt optimization**: Reduce token usage
7. **Caching**: Implement response caching
8. **Batching**: Batch requests when possible

### Performance Tuning
1. **Data preprocessing**: Optimize data pipeline performance
2. **Model architecture**: Choose efficient model designs
3. **Hardware acceleration**: Use GPUs and TPUs appropriately
4. **Batch optimization**: Optimize batch sizes for training and inference
5. **Streaming**: Use streaming for better UX
6. **Parallel requests**: Parallelize independent operations

## Summary

Agent Platform provides a comprehensive Gen AI platform with:
- **Foundation Models**: Gemini, image and video models, embeddings
- **Tuning**: Supervised, preference and reinforcement learning fine-tuning
- **Grounding**: Search, RAG, custom sources
- **Enterprise**: Security, compliance, private deployment
- **Cost Effective**: Multiple pricing tiers, optimization options

**Key Takeaways for Exam**:
1. Know model capabilities and selection criteria
2. Understand RAG architecture and implementation
3. Master function calling and structured outputs
4. Know enterprise security features
5. Understand cost optimization strategies
6. Be familiar with common patterns and scenarios