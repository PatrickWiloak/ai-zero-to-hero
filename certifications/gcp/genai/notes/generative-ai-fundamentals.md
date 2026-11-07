# Generative AI Fundamentals on Google Cloud

Code samples in these notes use the Google Gen AI SDK (`pip install --upgrade google-genai`) and assume `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION=global` and `GOOGLE_GENAI_USE_ENTERPRISE=True` are set, so `genai.Client()` needs no arguments; see [the SDK setup](vertex-ai.md#the-sdk-these-notes-use). A sample that starts without imports continues from an earlier one, with `client` and `model` already defined. Model IDs were checked on 2026-11-06.

## Introduction to Generative AI

### What is Generative AI?

**Definition**
- AI systems that create new content (text, images, code, audio, video)
- Learn patterns from training data
- Generate novel outputs similar to training data
- Goes beyond classification/prediction to creation

**vs Traditional AI**
- **Discriminative AI**: Classifies, predicts (Y given X)
- **Generative AI**: Creates new data (generates X)
- Both use similar underlying techniques (neural networks)

### Types of Generative Models

**Large Language Models (LLMs)**
- Generate human-like text
- Trained on massive text corpora
- Examples: Gemini, GPT, Claude
- Capabilities: Writing, coding, analysis, translation

**Image Generation Models**
- Create images from text descriptions
- Diffusion models, GANs, VAEs
- Examples: Gemini image models (Nano Banana), Stable Diffusion, DALL-E
- Use cases: Art, design, product visualization

**Multimodal Models**
- Process and generate multiple modalities
- Text, images, audio, video
- Example: Gemini (text, image, video understanding)
- Cross-modal understanding and generation

**Code Generation Models**
- Generate code from natural language
- Complete code snippets
- Examples: Gemini, GitHub Copilot, Amazon Q Developer
- Use cases: Developer productivity, code completion

## Foundation Models

### Characteristics

**Scale**
- Billions to trillions of parameters
- Trained on diverse, large-scale datasets
- Massive computational requirements
- Emergent capabilities at scale

**Transfer Learning**
- Pre-trained on broad data
- Adaptable to specific tasks
- Fine-tuning with domain data
- Few-shot and zero-shot learning

**Emergent Abilities**
- Unexpected capabilities at scale
- Reasoning, problem-solving
- In-context learning
- Chain-of-thought reasoning

### Google's Foundation Models

Google's current models are all members of the Gemini family, and the family is organized by job rather than by input type. Every text model accepts text, images, audio, video and PDFs as input, so there is no longer a separate vision or code model to choose. You pick a tier by how hard the task is and how much you want to pay.

**`gemini-4-argon`** is the frontier model, aimed at deep work in coding, finance, legal, cybersecurity and science. Its 1,048,576-token limit is shared by input and output. It behaves differently from the Flash models: it ignores custom `temperature`, `top_p` and `top_k`, and it cannot be tuned.

**`gemini-3.8-flash`** is the workhorse and the default in this guide. Google describes it as often approaching the performance of higher-cost frontier models. It has a 1,048,576-token context window and a 65,536-token output limit, and handles chat, coding, multimodal input and function calling. It also cannot be tuned.

**`gemini-3.5-flash`** and **`gemini-3.5-flash-lite`** cover the tasks the workhorse does not. Both support supervised tuning. Flash-Lite is the low-cost line for high-volume classification, routing and extraction.

**Image and video.** Image generation runs through Gemini image models such as `gemini-3.1-flash-image` (Nano Banana 2), which replaced Imagen when it retired on June 30, 2026. Video generation is `veo-3.1-generate-001`. Imagen's underlying technique, cascaded diffusion with a text encoder, is still worth knowing as a concept.

**Embeddings.** `gemini-embedding-001` produces text vectors of up to 3,072 dimensions; `gemini-embedding-2` extends that to images, audio, video and PDFs.

**Gemini Nano** is a separate, on-device model that runs on Android devices through AICore rather than through Agent Platform ([Android docs](https://developer.android.com/ai/gemini-nano)). It comes up when the requirement is offline or on-device inference.

**A note on history.** PaLM 2 (`text-bison`, `chat-bison`) and the Codey code models were the first generation on this platform. They retired on April 21, 2025 and Gemini replaced them. Older material that teaches their size names or their 8K context windows is out of date.

### Foundation Model Comparison

| Model | Strengths | Use Cases | Context Window |
|-------|-----------|-----------|----------------|
| `gemini-4-argon` | Maximum capability, long outputs | Hard reasoning, research, complex agents | 1,048,576 (input + output) |
| `gemini-3.8-flash` | Balanced, fast, multimodal | Default: chat, code, documents, tools | 1,048,576 |
| `gemini-3.5-flash` | Tunable | Tasks that need a tuned model | 1,048,576 |
| `gemini-3.5-flash-lite` | Lowest cost, fast, tunable | Classification, routing, extraction | 1,048,576 |
| `gemini-3.1-flash-image` | Image generation and editing | Design, marketing, content | See model page |
| `gemini-embedding-001` | Text vectors, up to 3,072 dimensions | Search, RAG, clustering | 2,048 per input |

Limits and retirement dates come from the [model lifecycle page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions) and each model's page, checked 2026-11-06. Pin them yourself before relying on them, because Google retires Gemini versions on a published schedule.

### Open Source Models on Agent Platform

Model Garden also carries open-weight models you can deploy to your own endpoint, such as Llama, DeepSeek, Qwen and Google's Gemma family, and partner models you call as managed APIs, such as Anthropic Claude, Grok and Mistral AI. Use an open-weight model when you need to control the weights, the serving stack or the tuning process. Check the catalog for current versions, since they change quickly.

**Model Garden Access**
```python
from google.cloud import aiplatform

aiplatform.init(project='my-project', location='us-central1')

# Call an open-weight model you deployed from Model Garden
endpoint = aiplatform.Endpoint(
    endpoint_name='projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID'
)

response = endpoint.predict(
    instances=[{"prompt": "Explain quantum computing"}]
)
```

### Transformer Architecture Fundamentals

**Core Components**
1. **Input Embedding**
   - Token to vector conversion
   - Positional encoding
   - Vocabulary mapping

2. **Self-Attention Mechanism**
   - Query, Key, Value matrices
   - Scaled dot-product attention
   - Multi-head attention (parallel processing)

3. **Feed-Forward Networks**
   - Position-wise transformations
   - Non-linear activations (GELU, ReLU)
   - Layer normalization

4. **Output Layer**
   - Projection to vocabulary
   - Softmax for probability distribution
   - Token prediction

**Attention Mechanism**
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V

Where:
- Q (Query): What we're looking for
- K (Key): What information is available
- V (Value): The actual information
- d_k: Dimension of keys (scaling factor)
```

**Multi-Head Attention Benefits**
- Parallel attention in different representation subspaces
- Capture different types of relationships
- Improved model expressiveness
- Better context understanding

**Encoder-Decoder vs Decoder-Only**

| Architecture | Examples | Strengths | Use Cases |
|--------------|----------|-----------|-----------|
| Encoder-Decoder | T5, BART | Translation, summarization | Seq2seq tasks |
| Decoder-Only | GPT, Gemini | Generation, completion | Text generation, chat |
| Encoder-Only | BERT | Understanding, classification | Embeddings, classification |

### Tokenization

**What is Tokenization?**
- Converting text to numerical tokens
- Subword tokenization for efficiency
- Vocabulary size determines model size
- Affects context window capacity

**Tokenization Methods**

**Byte-Pair Encoding (BPE)**
- Merges frequent character pairs
- Balances vocabulary size and coverage
- Used by GPT models

**WordPiece**
- Google's tokenization method
- Used by BERT
- Likelihood-based merging

**SentencePiece**
- Language-agnostic tokenization
- No pre-tokenization needed
- Used by T5, Gemini

**Tokenization Example**
```python
# Text to tokens
text = "Generative AI is transforming technology"

# Tokenized (approximate):
# ["Gener", "ative", " AI", " is", " transform", "ing", " technology"]

# Each token → unique integer ID
# Token IDs: [1234, 5678, 910, 11, 1213, 1415, 1617]
```

**Token Limits**
- Flash and Flash-Lite models: 1,048,576 tokens of context, 65,536 maximum output
- `gemini-4-argon`: 1,048,576 tokens shared by input and output
- Thinking is billed as output, so count it when you estimate cost

**Exam Tip**: 1 token ≈ 4 characters or ≈ 0.75 words in English

## Agent Studio

### Overview

**Purpose**
- Experiment with generative AI models
- No-code/low-code environment
- Prompt engineering and testing
- Model customization

**Key Features**
- Model Garden: Access to foundation models
- Prompt design and testing
- Tuning and customization
- Deployment to production

### Language Models

**Text Generation**
- `gemini-3.8-flash` as the default, `gemini-3.5-flash-lite` for high volume
- Adjustable parameters (temperature, top-k, top-p)
- Safety filters and content moderation

**Parameters**
- **Temperature** (0.0-1.0): Randomness/creativity
  - Low (0.0-0.3): Deterministic, focused
  - Medium (0.4-0.7): Balanced
  - High (0.8-1.0): Creative, diverse

- **Top-k**: Consider top k tokens
  - Lower: More focused
  - Higher: More diverse

- **Top-p** (nucleus sampling): Cumulative probability
  - 0.1: Very focused
  - 0.5: Balanced
  - 0.9: Diverse

- **Max output tokens**: Length limit
- **Stop sequences**: Custom stopping conditions

**Example Configuration**
```python
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-flash"

response = client.models.generate_content(
    model=model,
    contents="Write a short story about AI",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1024,
        top_k=40,
        top_p=0.95,
    ),
)

print(response.text)
```

### Chat Models

**Conversational AI**
- Multi-turn conversations
- Context maintenance
- Persona/role assignment
- Examples and instructions

**Chat Structure**
- System message: Instructions and role
- Context: Background information
- Examples: Few-shot demonstrations
- Messages: Conversation history

```python
from google import genai

client = genai.Client()

chat_model = "gemini-3.8-flash"

chat = client.chats.create(
    model=chat_model,
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful Python programming tutor",
    ),
    history=[
        types.Content(role="user", parts=[types.Part.from_text(text="What is a list?")]),
        types.Content(role="model", parts=[types.Part.from_text(text="A list in Python is an ordered, mutable collection...")]),
    ],
)

response = chat.send_message("How do I create a dictionary?")
print(response.text)

response = chat.send_message("Can you show an example?")
print(response.text)
```

### Code Tasks

**Code Generation**
- `gemini-3.8-flash` handles code through the same API as text; there is no separate code model
- Code completion
- Code explanation
- Unit test generation

**Code Chat**
- Interactive coding assistance
- Debugging help
- Code review
- Best practices

```python
from google import genai

client = genai.Client()

code_model = "gemini-3.8-flash"

response = client.models.generate_content(
    model=code_model,
    contents="Write a Python function to calculate fibonacci numbers",
)

print(response.text)
```

### Image Generation

Image generation runs through Gemini image models and the normal `generate_content` call, with the response modalities set to include images. To edit an image, you send the source image along with an instruction in `contents`.

```python
from io import BytesIO

from PIL import Image
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="Generate an image of a futuristic city at sunset, cyberpunk style",
    config=types.GenerateContentConfig(
        response_modalities=[types.Modality.TEXT, types.Modality.IMAGE],
    ),
)

for part in response.candidates[0].content.parts:
    if part.inline_data:
        Image.open(BytesIO(part.inline_data.data)).save("generated_image.png")
```

## Prompt Engineering

### Principles

**1. Be Clear and Specific**
- Detailed instructions
- Specify format and style
- Include constraints
- Define success criteria

**2. Provide Context**
- Background information
- Domain knowledge
- User intent
- Expected output format

**3. Use Examples**
- Few-shot learning
- Show desired format
- Demonstrate reasoning
- Edge case handling

**4. Iterate and Refine**
- Test variations
- Analyze outputs
- Adjust parameters
- A/B testing

### Prompt Patterns

**Zero-Shot**
```
Task: Summarize the following article in 3 sentences.

Article: [article text]

Summary:
```

**Zero-Shot Example - Complete**
```
Prompt:
Translate the following English text to French:
"The weather is beautiful today."

Output:
"Le temps est magnifique aujourd'hui."
```

**When to Use Zero-Shot**
- Model has sufficient pre-training
- Task is straightforward
- No labeled examples available
- Quick prototyping

**Few-Shot**
```
Classify customer reviews as positive, negative, or neutral.

Review: "This product is amazing!"
Sentiment: Positive

Review: "It broke after one day."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "I absolutely love this purchase!"
Sentiment:
```

**Few-Shot Best Practices**
- Use 2-5 examples (diminishing returns after)
- Examples should be diverse and representative
- Show edge cases when relevant
- Maintain consistent format across examples

**Few-Shot Complete Example**
```python
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-flash"

prompt = """
Extract the product name and price from the following text:

Text: "Buy the iPhone 15 Pro for $999"
Product: iPhone 15 Pro
Price: $999

Text: "Get the Samsung Galaxy S24 now at $849.99"
Product: Samsung Galaxy S24
Price: $849.99

Text: "MacBook Air M2 available for $1199"
Product:"""

response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=50,
    ),
)
print(response.text)
# Output: MacBook Air M2
# Price: $1199
```

**Chain-of-Thought**
```
Solve this problem step by step:

Problem: A store has 48 apples. They sell 3/4 of them. How many are left?

Solution:
Let me work through this step by step:
1. First, find 3/4 of 48
2. Calculate: 3/4 × 48 = 36
3. Subtract from original: 48 - 36 = 12
Therefore, 12 apples are left.

Now solve: A class has 32 students. 5/8 are girls. How many boys?
```

**Chain-of-Thought Complete Example**
```
Prompt:
Solve this problem step by step:
A company's revenue was $500,000 in Year 1. It increased by 20% in Year 2,
then decreased by 15% in Year 3. What is the revenue in Year 3?

Let's solve this step by step:

Output:
1. Year 1 revenue: $500,000
2. Year 2 increase: 20% of $500,000 = $100,000
3. Year 2 revenue: $500,000 + $100,000 = $600,000
4. Year 3 decrease: 15% of $600,000 = $90,000
5. Year 3 revenue: $600,000 - $90,000 = $510,000

Therefore, the revenue in Year 3 is $510,000.
```

**Chain-of-Thought Benefits**
- Improves reasoning accuracy
- Provides explainability
- Reduces logical errors
- Better for multi-step problems

**Role-Based**
```
You are an expert cybersecurity analyst with 15 years of experience.

A client asks: "What are the best practices for cloud security?"

Provide a professional response including:
1. Key security principles
2. Specific recommendations
3. Common pitfalls to avoid
4. Tools and services to consider
```

**Role-Based Complete Example**
```python
chat_model = "gemini-3.8-flash"

chat = client.chats.create(
    model=chat_model,
    config=types.GenerateContentConfig(
        system_instruction="""You are a senior DevOps engineer specializing in Kubernetes
    and cloud-native architectures. You provide practical, production-ready
    advice with security best practices in mind.""",
    ),
)

response = chat.send_message(
    "How should I structure my Kubernetes deployments for a microservices app?"
)
print(response.text)

# Output will be tailored to the DevOps engineer persona
```

**Structured Output**
```
Extract information from the following text and return as JSON:

Text: "John Smith works at Google in Mountain View, CA. His email is john@google.com"

Output format:
{
  "name": "",
  "company": "",
  "location": "",
  "email": ""
}
```

**Structured Output Complete Example**
```
Prompt:
Extract entities from the following text and return as JSON:

Text: "Apple Inc. announced on March 15, 2024, that CEO Tim Cook will
speak at the conference in San Francisco."

Return JSON with: company, date, person, role, location

Output:
{
  "company": "Apple Inc.",
  "date": "March 15, 2024",
  "person": "Tim Cook",
  "role": "CEO",
  "location": "San Francisco"
}
```

### Prompt Design Patterns

**1. Instruction-Following Pattern**
```
Task: Write a professional email

Requirements:
- Formal tone
- 3-4 paragraphs
- Include call to action
- Subject: Project Update

Context: Updating stakeholders on Q4 project status

Email:
```

**2. Template Pattern**
```
Generate a product description using this template:

[Product Name] is a [category] that [main benefit].
Key features include [feature 1], [feature 2], and [feature 3].
Perfect for [target audience] who want to [desired outcome].

Product: Smart Water Bottle
Category: Health & Fitness Device
```

**3. Reasoning Pattern**
```
Question: Should we migrate our application to microservices?

Analyze this decision by considering:
1. Current pain points
2. Benefits of microservices
3. Challenges and risks
4. Alternative approaches
5. Recommendation with reasoning
```

**4. Constraint-Based Pattern**
```
Write a blog post about cloud computing.

Constraints:
- Exactly 500 words
- Include 3 real-world examples
- Technical level: Beginner
- No jargon without explanation
- End with actionable takeaway
```

**5. Multi-Step Pattern**
```
Help me create a project plan:

Step 1: Identify the main project phases
Step 2: For each phase, list key deliverables
Step 3: Estimate timeline for each phase
Step 4: Identify potential risks
Step 5: Create mitigation strategies

Project: Building a customer data platform
```

### Advanced Techniques

**System Instructions**
- Define model behavior
- Set constraints
- Specify output format
- Safety guidelines

**Context Window Management**
- Track token usage
- Summarize long conversations
- Sliding window approach
- Context compression

**Temperature Tuning**
- Low temperature: Factual, consistent
- High temperature: Creative, diverse
- Task-dependent optimization

**Temperature Guidelines**

| Temperature | Best For | Example Use Cases |
|-------------|----------|-------------------|
| 0.0 - 0.3 | Deterministic, factual | Classification, extraction, code |
| 0.4 - 0.7 | Balanced | General chat, Q&A, summarization |
| 0.8 - 1.0 | Creative, diverse | Brainstorming, creative writing, art |

**Top-k and Top-p Tuning**

**Top-k Sampling**
- Limits vocabulary to top k probable tokens
- k=1: Greedy (most likely token)
- k=40: Balanced diversity
- k=100+: High diversity

**Top-p (Nucleus) Sampling**
- Dynamic vocabulary based on cumulative probability
- p=0.1: Very focused, deterministic
- p=0.5: Balanced
- p=0.95: Diverse but coherent

**Combining Parameters**
```python
# Factual, consistent output
response = client.models.generate_content(
    model=model,
    contents="What is the capital of France?",
    config=types.GenerateContentConfig(
        temperature=0.2,
        top_k=40,
        top_p=0.8,
    ),
)

# Creative, diverse output
response = client.models.generate_content(
    model=model,
    contents="Write a creative story about space exploration",
    config=types.GenerateContentConfig(
        temperature=0.9,
        top_k=100,
        top_p=0.95,
    ),
)
```

**Negative Prompts** (for image generation)
- Specify what to avoid
- Reduce unwanted elements
- Improve quality

**Describing what to exclude**

Gemini image models take instructions in the prompt, so state exclusions there in plain language, such as "a portrait of a person, no text or watermarks". Check the [image generation guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/image-generation) for the options each model supports.

### Prompt Engineering Best Practices

**1. Specificity Over Ambiguity**
```
Bad: "Write about AI"
Good: "Write a 300-word explanation of generative AI for business executives,
focusing on practical applications and ROI"
```

**2. Provide Output Examples**
```
Extract dates from text in ISO 8601 format (YYYY-MM-DD):

Input: "The meeting is on March 15th, 2024"
Output: 2024-03-15

Input: "Submit by December 1, 2023"
Output: 2023-12-01

Input: "The deadline is next Friday, April 20"
Output:
```

**3. Break Complex Tasks**
```
Instead of: "Analyze this code, find bugs, fix them, and optimize performance"

Use:
Step 1: Review the code and identify potential bugs
Step 2: For each bug, explain the issue and impact
Step 3: Provide corrected code for each bug
Step 4: Suggest performance optimizations
```

**4. Use Delimiters**
```
Summarize the text between the triple quotes:

"""
[Long text content here]
"""

Summary:
```

**5. Specify Output Format**
```
Return your response as a bulleted list with exactly 5 items.
Each item should be a complete sentence under 20 words.
```

### Prompt Engineering for Different Tasks

**Text Summarization**
```python
prompt = """
Summarize the following article in 3 bullet points, focusing on:
- Main topic or thesis
- Key findings or arguments
- Practical implications

Article:
[Article text here]

Summary:
"""
```

**Code Generation**
```python
prompt = """
Write a Python function that:
- Takes a list of numbers as input
- Returns the median value
- Handles even and odd length lists
- Includes error handling for empty lists
- Add docstring and type hints

Function:
"""
```

**Data Extraction**
```python
prompt = """
Extract the following information from the resume:
- Name
- Email
- Phone
- Years of experience
- Top 3 skills
- Most recent job title

Return as JSON.

Resume:
[Resume text]

JSON:
"""
```

**Content Creation**
```python
prompt = """
Create a LinkedIn post about:
Topic: Cloud migration success story
Tone: Professional but conversational
Length: 150-200 words
Include: Specific metrics, lessons learned, call-to-action
Hashtags: 3-5 relevant tags

Post:
"""
```

**Translation**
```python
prompt = """
Translate the following technical documentation from English to Spanish:
- Maintain technical terms in English where appropriate
- Preserve formatting and structure
- Keep code snippets unchanged

Text:
[Documentation text]

Translation:
"""
```

### Exam Tips for Prompt Engineering

1. **Zero-shot vs Few-shot**: Few-shot improves accuracy but uses more tokens
2. **Chain-of-thought**: Use for reasoning tasks, math problems, multi-step logic
3. **Temperature**: Low for factual/deterministic, high for creative tasks
4. **Context window**: Monitor token usage; current Flash models take about 1M tokens of input and 65,536 of output
5. **System instructions**: Set behavior and constraints for chat models
6. **Structured output**: Use JSON format with explicit schema definition
7. **Iteration**: Prompt engineering is iterative - test and refine
8. **Safety**: Always consider responsible AI and content filtering

## Model Tuning and Customization

### Tuning Methods

**Prompt Tuning (Soft Prompts)**
- Learn task-specific prompts
- No model weight changes
- Fast and efficient
- Limited data required

**Adapter Tuning**
- Add small adapter layers
- Freeze base model weights
- Task-specific adapters
- Parameter-efficient

**Fine-Tuning**
- Update model weights
- Requires more data and compute
- Best performance on specific tasks
- Can overfit with small data

### When to Tune

**Prompt Engineering First**
- Quick iteration
- No training required
- Zero-shot or few-shot
- Cost-effective

**Tune When**
- Specific domain terminology
- Consistent output format
- Brand voice requirements
- Performance improvement needed

### Tuning Process

**1. Prepare Data**
```json
{"contents": [{"role": "user", "parts": [{"text": "Translate: Hello"}]}, {"role": "model", "parts": [{"text": "Hola"}]}]}
{"contents": [{"role": "user", "parts": [{"text": "Translate: Goodbye"}]}, {"role": "model", "parts": [{"text": "Adiós"}]}]}
```

**2. Create Tuning Job**
```python
from google import genai
from google.genai import types

# Tuning for Gemini 3 and later runs on the us or eu multi-region.
# gemini-3.8-flash cannot be tuned, so this uses gemini-3.5-flash.
client = genai.Client(enterprise=True, project="my-project", location="us")

tuning_job = client.tunings.tune(
    base_model="gemini-3.5-flash",
    training_dataset=types.TuningDataset(gcs_uri="gs://my-bucket/training_data.jsonl"),
    config=types.CreateTuningJobConfig(tuned_model_display_name="translator-v1"),
)
```

**3. Evaluate**
- Test on validation set
- Compare with base model
- Measure task-specific metrics

**4. Deploy**
- Deploy tuned model
- A/B test against base model
- Monitor performance

## Model Capabilities

### Text Generation

**Capabilities**
- Long-form content creation
- Story writing
- Article generation
- Email composition
- Product descriptions
- Marketing copy

**Best Practices**
- Specify desired length
- Define target audience
- Set tone and style
- Include key points to cover
- Use examples for format

**Example: Blog Post Generation**
```python
prompt = """
Write a 500-word blog post for a technical audience about:
Topic: Kubernetes security best practices
Tone: Professional, informative
Structure: Introduction, 3 main sections, conclusion
Include: Code examples, specific tools, actionable tips
"""

response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1024,
    ),
)
```

### Code Generation

**Capabilities**
- Function implementation
- Code completion
- Algorithm implementation
- Unit test generation
- Documentation generation
- Code translation

**Supported Languages**
- Python, Java, JavaScript, TypeScript
- Go, C++, C#, Ruby, PHP
- SQL, Bash, YAML, JSON
- 20+ programming languages

**Example: Function Generation**
```python
from google import genai

client = genai.Client()

code_model = "gemini-3.8-flash"

prompt = """
Write a Python function that:
1. Takes a list of dictionaries as input
2. Each dict has 'name', 'age', 'salary' keys
3. Returns the top 3 employees by salary
4. Handle edge cases (empty list, ties)
5. Include type hints and docstring
"""

response = client.models.generate_content(
    model=code_model,
    contents=prompt,
)
print(response.text)
```

### Summarization

**Types of Summarization**

**Extractive Summarization**
- Selects key sentences from original
- Maintains original wording
- Preserves factual accuracy
- Less natural flow

**Abstractive Summarization**
- Generates new sentences
- Rephrases and synthesizes
- More natural language
- LLMs excel at this

**Summarization Strategies**

| Strategy | Use Case | Temperature | Prompt Example |
|----------|----------|-------------|----------------|
| Concise | Quick overview | 0.2-0.4 | "Summarize in 2 sentences" |
| Detailed | Comprehensive | 0.3-0.5 | "Create detailed summary with key points" |
| Bullet Points | Scannable | 0.2-0.3 | "List 5 main takeaways as bullets" |
| Executive | Leadership | 0.3-0.5 | "Executive summary for C-level" |

**Summarization Example**
```python
prompt = """
Summarize the following research paper abstract:

Abstract: [Long technical abstract about quantum computing]

Provide:
1. One-sentence summary for non-technical audience
2. Three key findings
3. Practical implications

Summary:
"""

response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=256,
    ),
)
```

### Translation

**Capabilities**
- Broad multilingual support across current Gemini models
- Context-aware translation
- Technical terminology preservation
- Cultural adaptation
- Maintains formatting

**Translation Best Practices**
- Specify source and target languages explicitly
- Provide context for ambiguous terms
- Indicate formality level
- Preserve technical terms when needed
- Test with native speakers

**Translation Example**
```python
prompt = """
Translate the following from English to Japanese:
- Maintain professional business tone
- Keep technical terms in English where standard
- Preserve markdown formatting

Text:
"Our API supports REST and GraphQL endpoints. Authentication uses OAuth 2.0."

Translation:
"""
```

### Question Answering

**QA Types**

**Factual QA**
```python
prompt = "What is the capital of Australia?"
# Temperature: 0.1-0.2 (deterministic)
```

**Analytical QA**
```python
prompt = "Explain why microservices architecture is beneficial for large applications."
# Temperature: 0.4-0.6 (balanced)
```

**Contextual QA**
```python
prompt = """
Context: [Document or passage]

Question: Based on the context above, what were the main causes of the event?

Answer:
"""
# Temperature: 0.2-0.4
```

**Multi-hop QA** (requires reasoning)
```python
prompt = """
Information:
- Company A acquired Company B in 2020
- Company B was founded by John Smith
- John Smith started Company C in 2022

Question: Who started a new company two years after their previous company was acquired?

Think step by step:
"""
```

### Embeddings

**What are Embeddings?**
- Dense vector representations of text
- Capture semantic meaning
- Enable similarity comparisons
- Foundation for search and classification

**Use Cases**
- Semantic search
- Document clustering
- Recommendation systems
- Anomaly detection
- Classification

**Agent Platform text embeddings**
```python
from google import genai
from google.genai import types

client = genai.Client()

embedding_model = "gemini-embedding-001"

# Single text embedding
text = "What is machine learning?"
embeddings = client.models.embed_content(model=embedding_model, contents=[text], config=types.EmbedContentConfig(output_dimensionality=768)).embeddings
vector = embeddings[0].values  # 768-dimensional vector

# Batch embeddings
texts = ["AI is transforming industries", "Machine learning enables predictions"]
embeddings = client.models.embed_content(model=embedding_model, contents=texts, config=types.EmbedContentConfig(output_dimensionality=768)).embeddings
```

**Embedding Dimensions**
- `gemini-embedding-001`: up to 3,072 dimensions by default; the samples here request 768 with `output_dimensionality`
- Older `text-embedding-005` models produce up to 768 and retire on April 1, 2027
- Optimized for semantic similarity

**Similarity Calculation**
```python
import numpy as np

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Compare document similarity
similarity = cosine_similarity(embeddings[0].values, embeddings[1].values)
```

### Multimodal Capabilities (Gemini)

**Vision Understanding**
- Image description and captioning
- Object detection and recognition
- Visual question answering
- Image-text reasoning

**Gemini Vision Example**
```python
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-flash"

image_part = types.Part.from_uri(file_uri="gs://my-bucket/image.jpg", mime_type="image/jpeg")
text_part = "What objects are in this image? Describe their arrangement."

response = client.models.generate_content(
    model=model,
    contents=[image_part, text_part],
)
print(response.text)
```

**Document Understanding**
- Extract information from PDFs
- Table extraction and analysis
- Form processing
- Invoice data extraction

**Video Understanding**
```python
video_part = types.Part.from_uri(file_uri="gs://my-bucket/video.mp4", mime_type="video/mp4")
prompt = "Summarize the key events in this video."

response = client.models.generate_content(
    model=model,
    contents=[video_part, prompt],
)
```

## Responsible AI

### Google AI Principles

1. **Be socially beneficial**
   - Consider broad social and economic impacts
   - Expand benefits to diverse populations
   - Respect cultural and social norms

2. **Avoid creating or reinforcing unfair bias**
   - Avoid unjust impacts on people
   - Seek diverse perspectives
   - Test for bias across demographics

3. **Be built and tested for safety**
   - Develop safety best practices
   - Test rigorously before deployment
   - Monitor for unintended behaviors

4. **Be accountable to people**
   - Provide appropriate transparency
   - Subject to human direction and control
   - Enable feedback mechanisms

5. **Incorporate privacy design principles**
   - Provide notice and consent
   - Encourage architectures with privacy safeguards
   - Provide appropriate data governance

6. **Uphold high standards of scientific excellence**
   - Rigorous methodology
   - Peer review and reproducibility
   - Share knowledge responsibly

7. **Be made available for uses that accord with these principles**
   - Beneficial applications
   - Consider likelihood of harmful uses
   - Limit potentially harmful applications

### AI Principles

**Fairness**
- Avoid bias in outputs
- Representative training data
- Bias detection and mitigation
- Inclusive design

**Safety**
- Content filtering
- Harmful content detection
- Toxicity screening
- Safety thresholds

**Privacy**
- Data protection
- PII detection and removal
- User consent
- Secure processing

**Transparency**
- Explainability
- Model cards
- Documentation
- Limitations disclosure

### Safety Filters

**Content Categories**
- Hate speech
- Harassment
- Sexually explicit content
- Dangerous content
- Violence and gore

**Harm Categories in Agent Platform**
```python
from google import genai
from google.genai import types

client = genai.Client()

safety_settings = [
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_ONLY_HIGH),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
]

response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        safety_settings=safety_settings,
    ),
)
```

**Filter Levels**

The default changed, and older material gets this wrong. For `gemini-3.5-flash` and later models the default threshold is **`OFF`**: no automated blocking and no safety metadata in the response. If your application needs filtering, you must now ask for it ([safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters)).

- **OFF**: No blocking and no metadata (default on current models)
- **BLOCK_NONE**: No blocking, but scores are still returned so you can apply your own rules
- **BLOCK_ONLY_HIGH**: Block when the score is high
- **BLOCK_MEDIUM_AND_ABOVE**: Block when the score is medium or high
- **BLOCK_LOW_AND_ABOVE**: Block when the score is low, medium or high (most restrictive)

**Handling Blocked Responses**
```python
# A block does not raise an exception: check the response.
response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(safety_settings=safety_settings),
)

if response.prompt_feedback and response.prompt_feedback.block_reason:
    print(f"Prompt blocked: {response.prompt_feedback.block_reason}")
elif response.candidates[0].finish_reason == types.FinishReason.SAFETY:
    print("Response blocked by safety filters")
    # Implement fallback logic
else:
    print(response.text)
```

### Bias Detection and Mitigation

**Types of Bias**

**Training Data Bias**
- Underrepresentation of groups
- Historical biases in data
- Skewed data distributions
- Cultural bias in annotations

**Model Bias**
- Amplification of training biases
- Stereotypical associations
- Demographic performance gaps
- Language-specific biases

**Deployment Bias**
- Unequal access to technology
- Different use patterns across groups
- Context-dependent fairness

**Detection Methods**

**1. Diverse Input Testing**
```python
# Test across demographic variations
test_prompts = [
    "The engineer solved the problem. {pronoun} was skilled.",
    # Test with: he, she, they

    "The {profession} arrived at work.",
    # Test with: doctor, nurse, CEO, assistant
]
```

**2. Fairness Metrics**
- Demographic parity
- Equal opportunity
- Equalized odds
- Individual fairness

**3. Adversarial Testing**
- Red-teaming exercises
- Edge case evaluation
- Stress testing with controversial topics

**Mitigation Strategies**

**1. Data Level**
- Balanced training data
- Augmentation for underrepresented groups
- Debiasing techniques
- Curated datasets

**2. Model Level**
- Fairness constraints during training
- Adversarial debiasing
- Bias correction layers

**3. Post-Processing**
- Output filtering
- Bias detection in responses
- Human-in-the-loop review
- Confidence thresholding

**4. Prompt Engineering**
```python
# Include fairness instructions in prompt
prompt = """
Provide career advice for a software engineer.

Important: Ensure advice is inclusive and does not make assumptions
based on gender, age, ethnicity, or other protected characteristics.
Focus on skills, experience, and professional development.

Question: What skills should I develop to advance my career?
"""
```

### Content Moderation

**Moderation Layers**

**1. Input Moderation**
- Filter harmful queries
- Detect jailbreak attempts
- PII detection
- Malicious intent detection

**2. Output Moderation**
- Safety filter application
- Toxicity detection
- Factuality checking
- Bias detection

**3. Context Moderation**
- Conversation history review
- Pattern detection
- Abuse detection

**Implementation Example**
```python
def safe_generate(prompt, model):
    # Input moderation
    if contains_pii(prompt):
        return "Error: Please remove personal information"

    if is_harmful_request(prompt):
        return "Error: Request violates content policy"

    # Generate with safety settings
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            safety_settings=STRICT_SAFETY_SETTINGS,
        ),
    )

    # Output moderation
    if is_toxic(response.text):
        return "Response filtered due to content policy"

    return response.text
```

### PII Detection and Handling

**Types of PII**
- Names, addresses, phone numbers
- Email addresses
- Social Security numbers
- Credit card numbers
- Medical information
- Biometric data

**Detection Strategies**
```python
from google.cloud import dlp_v2

def detect_pii(text):
    dlp = dlp_v2.DlpServiceClient()

    info_types = [
        {"name": "EMAIL_ADDRESS"},
        {"name": "PHONE_NUMBER"},
        {"name": "CREDIT_CARD_NUMBER"},
        {"name": "US_SOCIAL_SECURITY_NUMBER"},
    ]

    inspect_config = {"info_types": info_types}
    item = {"value": text}

    response = dlp.inspect_content(
        request={"parent": f"projects/{project_id}",
                "inspect_config": inspect_config,
                "item": item}
    )

    return response.result.findings
```

**Redaction Example**
```python
def redact_pii(text):
    findings = detect_pii(text)

    for finding in findings:
        text = text.replace(finding.quote, "[REDACTED]")

    return text

# Use before sending to model
safe_prompt = redact_pii(user_input)
response = client.models.generate_content(
    model=model,
    contents=safe_prompt,
)
```

### Responsible AI Checklist

**Pre-Deployment**
- [ ] Define use case and limitations
- [ ] Assess potential harms and benefits
- [ ] Test with diverse user groups
- [ ] Implement safety filters
- [ ] Set up bias detection
- [ ] Enable PII protection
- [ ] Document model capabilities and limitations
- [ ] Create incident response plan

**During Deployment**
- [ ] Monitor for bias and fairness issues
- [ ] Track safety filter activations
- [ ] Log and review problematic outputs
- [ ] Collect user feedback
- [ ] A/B test safety configurations
- [ ] Regular security audits

**Post-Deployment**
- [ ] Continuous monitoring
- [ ] Regular bias audits
- [ ] Update safety configurations
- [ ] Retrain or tune models as needed
- [ ] Transparency reporting
- [ ] Incident documentation and learning

### Exam Tips for Responsible AI

1. **Google AI Principles**: Know all 7 principles and their application
2. **Safety Filters**: Understand harm categories and blocking thresholds
3. **Bias Types**: Recognize training, model, and deployment bias
4. **Content Moderation**: Multi-layer approach (input, output, context)
5. **PII Handling**: Use Cloud DLP for detection and redaction
6. **Fairness**: Test across demographics, use diverse datasets
7. **Transparency**: Model cards, documentation, limitations disclosure
8. **Human Oversight**: Critical for high-stakes applications

## Integration and Deployment

### API Integration

**REST API**
```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3.8-flash:generateContent \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "What is machine learning?"}]}],
    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1024}
  }'
```

**Python SDK**
```python
from google import genai

client = genai.Client()


model = "gemini-3.8-flash"
response = client.models.generate_content(
    model=model,
    contents="Explain quantum computing",
)
```

### Deployment Options

**Serverless (Agent Platform)**
- Managed infrastructure
- Auto-scaling
- Pay-per-use
- Low maintenance

**Containers (GKE)**
- Custom control
- Self-managed scaling
- Kubernetes orchestration
- Advanced configurations

**Edge Deployment**
- On-device inference
- Gemini Nano
- Low latency
- Privacy-preserving

### Production Patterns

**Caching**
- Cache common queries
- Reduce latency and cost
- Memorystore integration
- TTL configuration

**Rate Limiting**
- Prevent abuse
- Cost control
- Fair usage
- API quotas

**Fallback Strategies**
- Multiple model tiers
- Graceful degradation
- Error handling
- Retry logic

**Monitoring**
- Request/response logging
- Latency tracking
- Error rates
- Cost monitoring

## Generative AI Use Cases

### Document Processing

**Use Case**: Automated document analysis and extraction

**Capabilities**
- Extract key information from contracts
- Summarize legal documents
- Parse invoices and receipts
- Analyze medical records
- Generate document summaries

**Implementation Example**
```python
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.8-flash"

# Process invoice image
invoice_image = types.Part.from_uri(file_uri="gs://bucket/invoice.pdf", mime_type="application/pdf")

prompt = """
Extract the following information from this invoice:
- Invoice number
- Date
- Vendor name
- Total amount
- Line items with descriptions and prices

Return as structured JSON.
"""

response = client.models.generate_content(
    model=model,
    contents=[invoice_image, prompt],
)
print(response.text)
```

**Best Practices**
- Current Gemini models read scanned documents directly
- Specify output format (JSON, CSV)
- Include validation rules
- Handle multi-page documents
- Implement error handling for missing fields

### Chatbots and Virtual Assistants

**Use Case**: Customer service and support automation

**Capabilities**
- Multi-turn conversations
- Context-aware responses
- FAQ answering
- Issue troubleshooting
- Appointment scheduling

**Implementation Example**
```python
from google import genai

client = genai.Client()

chat_model = "gemini-3.8-flash"

# Configure chatbot with context
chat = client.chats.create(
    model=chat_model,
    config=types.GenerateContentConfig(
        system_instruction="""You are a customer service agent for TechCorp, a cloud services company.
    You help customers with:
    - Account issues
    - Billing questions
    - Technical support
    - Service information

    Be helpful, professional, and concise. Escalate complex issues to human agents.
    """,
    ),
    history=[
        types.Content(role="user", parts=[types.Part.from_text(text="How do I reset my password?")]),
        types.Content(role="model", parts=[types.Part.from_text(text="To reset your password: 1) Go to techcorp.com/login 2) Click 'Forgot Password' 3) Enter your email 4) Follow the link in your email. Let me know if you need help!")]),
        types.Content(role="user", parts=[types.Part.from_text(text="What's the status of my ticket #12345?")]),
        types.Content(role="model", parts=[types.Part.from_text(text="Let me check that for you. Could you please provide your account email address so I can look up your ticket?")]),
    ],
)

# Multi-turn conversation
response = chat.send_message("I can't login to my account")
print(response.text)

response = chat.send_message("I tried resetting my password but didn't get an email")
print(response.text)
```

**Advanced Features**
- Intent classification
- Entity extraction
- Sentiment analysis
- Conversation summarization
- Handoff to human agents

### Content Creation

**Use Case**: Marketing and creative content generation

**Capabilities**
- Blog posts and articles
- Social media posts
- Product descriptions
- Email campaigns
- Ad copy

**Implementation Example**
```python
def generate_product_description(product_info):
    prompt = f"""
    Create a compelling product description for:

    Product: {product_info['name']}
    Category: {product_info['category']}
    Key Features: {', '.join(product_info['features'])}
    Target Audience: {product_info['audience']}

    Requirements:
    - Length: 150-200 words
    - Tone: {product_info['tone']}
    - Include benefits, not just features
    - Add call-to-action
    - SEO-friendly

    Description:
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.8,
            max_output_tokens=512,
        ),
    )
    return response.text

# Example usage
product = {
    'name': 'CloudSync Pro',
    'category': 'Cloud Storage',
    'features': ['256-bit encryption', 'Real-time sync', 'Team collaboration'],
    'audience': 'Small businesses',
    'tone': 'Professional yet approachable'
}

description = generate_product_description(product)
```

**Content Variations**
```python
def generate_content_variations(base_content, num_variations=3):
    """Generate multiple variations for A/B testing"""
    variations = []

    for i in range(num_variations):
        prompt = f"""
        Rewrite the following content with a different approach while maintaining the core message:

        Original: {base_content}

        Variation {i+1} should be:
        - Unique in structure and word choice
        - Same length (±10%)
        - Maintain key information

        Rewritten version:
        """

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.9,
            ),
        )
        variations.append(response.text)

    return variations
```

### Code Assistance

**Use Case**: Developer productivity and code generation

**Capabilities**
- Function implementation
- Code documentation
- Unit test generation
- Code review and suggestions
- Bug fixing
- Code translation

**Implementation Example**
```python
from google import genai

client = genai.Client()

code_model = "gemini-3.8-flash"
codechat_model = "gemini-3.8-flash"

# Generate function
function_prompt = """
Create a Python function that implements a rate limiter using the token bucket algorithm:
- Max capacity: 100 tokens
- Refill rate: 10 tokens per second
- Thread-safe implementation
- Include type hints and docstring
"""

code = client.models.generate_content(
    model=code_model,
    contents=function_prompt,
)
print(code.text)

# Generate unit tests
test_prompt = f"""
Write comprehensive pytest unit tests for the following function:

{code.text}

Include tests for:
- Normal operation
- Edge cases (empty bucket, max capacity)
- Concurrent access
- Time-based refill
"""

tests = client.models.generate_content(
    model=code_model,
    contents=test_prompt,
)
print(tests.text)

# Code review
codechat = client.chats.create(model=codechat_model)
review = codechat.send_message(f"""
Review this code for:
- Security vulnerabilities
- Performance issues
- Code quality and best practices
- Potential bugs

Code:
{code.text}
""")
print(review.text)
```

### Data Augmentation

**Use Case**: Synthetic data generation for ML training

**Capabilities**
- Generate training examples
- Create diverse variations
- Balance dataset classes
- Generate edge cases
- Synthetic PII for testing

**Implementation Example**
```python
def generate_training_data(category, num_examples, existing_examples=None):
    """Generate synthetic training examples"""

    prompt = f"""
    Generate {num_examples} diverse examples of {category}.

    Requirements:
    - Each example should be unique
    - Cover different scenarios and edge cases
    - Realistic and varied
    - Include both common and uncommon cases

    {f"Existing examples for reference: {existing_examples}" if existing_examples else ""}

    Generate examples as JSON array:
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.9,
            max_output_tokens=2048,
        ),
    )

    return response.text

# Example: Generate customer support queries
support_queries = generate_training_data(
    category="customer support queries about billing issues",
    num_examples=20
)

# Example: Generate product reviews
reviews = generate_training_data(
    category="product reviews for a smartphone",
    num_examples=50,
    existing_examples=["Great camera quality!", "Battery lasts all day"]
)
```

**Variation Generation**
```python
def augment_dataset(examples, variations_per_example=3):
    """Create variations of existing examples"""
    augmented_data = []

    for example in examples:
        prompt = f"""
        Create {variations_per_example} variations of the following text:
        - Maintain the core meaning
        - Use different phrasing
        - Vary sentence structure
        - Keep the same sentiment/intent

        Original: {example}

        Variations:
        """

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.8,
            ),
        )
        augmented_data.extend([example] + response.text.split('\n'))

    return augmented_data
```

### Semantic Search and RAG

**Use Case**: Retrieval-Augmented Generation for Q&A

**Capabilities**
- Search through documents
- Find relevant context
- Answer questions with citations
- Combine multiple sources
- Update knowledge dynamically

**Implementation Example**
```python
from google import genai
from google.genai import types
import numpy as np

client = genai.Client()

# Initialize models
embedding_model = "gemini-embedding-001"
generation_model = "gemini-3.8-flash"

def create_knowledge_base(documents):
    """Create embeddings for document corpus"""
    embeddings = client.models.embed_content(model=embedding_model, contents=documents).embeddings
    return {
        'documents': documents,
        'embeddings': [emb.values for emb in embeddings]
    }

def semantic_search(query, knowledge_base, top_k=3):
    """Find most relevant documents"""
    query_embedding = client.models.embed_content(model=embedding_model, contents=[query]).embeddings[0].values

    # Calculate similarities
    similarities = []
    for doc_embedding in knowledge_base['embeddings']:
        sim = np.dot(query_embedding, doc_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
        )
        similarities.append(sim)

    # Get top k documents
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [knowledge_base['documents'][i] for i in top_indices]

def answer_with_rag(question, knowledge_base):
    """Answer question using RAG"""
    # Retrieve relevant documents
    relevant_docs = semantic_search(question, knowledge_base)

    # Generate answer with context
    prompt = f"""
    Context:
    {chr(10).join(f"- {doc}" for doc in relevant_docs)}

    Question: {question}

    Based on the context above, provide a detailed answer.
    If the context doesn't contain enough information, say so.

    Answer:
    """

    response = client.models.generate_content(
        model=generation_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        ),
    )
    return response.text

# Example usage
knowledge_base = create_knowledge_base([
    "Cloud Run is a fully managed serverless platform for containers.",
    "Agent Platform provides ML model training and deployment services.",
    "BigQuery is a serverless data warehouse for analytics."
])

answer = answer_with_rag(
    "What is Cloud Run?",
    knowledge_base
)
```

### Translation and Localization

**Use Case**: Multi-language content adaptation

**Implementation Example**
```python
def localize_content(content, target_language, target_region):
    """Translate and culturally adapt content"""

    prompt = f"""
    Translate and localize the following content:

    Source: {content}
    Target Language: {target_language}
    Target Region: {target_region}

    Requirements:
    - Accurate translation
    - Cultural adaptation for {target_region}
    - Maintain tone and intent
    - Adapt idioms and expressions
    - Keep formatting (markdown, etc.)

    Localized content:
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        ),
    )
    return response.text
```

## Generative AI Scenarios and Solutions

### Scenario 1: Customer Review Sentiment Analysis

**Problem**: Analyze thousands of customer reviews and categorize sentiment

**Requirements**
- Classify as positive, negative, neutral
- Extract key topics/issues
- Identify actionable feedback
- Generate summary report

**Solution**
```python
def analyze_review_batch(reviews):
    """Analyze multiple reviews efficiently"""

    # Create structured prompt
    prompt = """
    Analyze the following customer reviews and provide:
    1. Sentiment (positive/negative/neutral) for each
    2. Key topics mentioned (features, issues, suggestions)
    3. Overall summary with action items

    Reviews:
    """

    for i, review in enumerate(reviews, 1):
        prompt += f"\nReview {i}: {review}"

    prompt += """

    Return analysis as JSON:
    {
      "reviews": [
        {"id": 1, "sentiment": "positive", "topics": ["feature1", "feature2"], "key_points": "..."}
      ],
      "summary": "...",
      "action_items": ["..."]
    }
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=2048,
        ),
    )

    return response.text

# Example
reviews = [
    "The product is amazing! Fast shipping and great quality.",
    "Disappointed. Item arrived broken and customer service was unhelpful.",
    "It's okay. Does what it says but nothing special."
]

analysis = analyze_review_batch(reviews)
```

**Exam Tip**: Use low temperature (0.1-0.3) for classification tasks to ensure consistency

### Scenario 2: Code Documentation Generation

**Problem**: Generate comprehensive documentation for existing codebase

**Requirements**
- Function/class docstrings
- API documentation
- Usage examples
- Parameter descriptions

**Solution**
```python
from google import genai

client = genai.Client()

codechat = client.chats.create(model="gemini-3.8-flash")

def generate_documentation(code):
    """Generate comprehensive code documentation"""

    prompt = f"""
    Generate comprehensive documentation for the following code:

    ```python
    {code}
    ```

    Include:
    1. Function/class description
    2. Parameters with types and descriptions
    3. Return value description
    4. Usage examples
    5. Notes about edge cases or limitations

    Use Google-style docstring format.
    """

    response = codechat.send_message(prompt)
    return response.text

# Example
code = """
def process_data(items, threshold=0.5, validate=True):
    results = []
    for item in items:
        if validate and not is_valid(item):
            continue
        score = calculate_score(item)
        if score > threshold:
            results.append(item)
    return results
"""

documentation = generate_documentation(code)
```

**Prompt Engineering Tip**: Specify documentation format (Google, NumPy, Sphinx) for consistency

### Scenario 3: Multi-Language Customer Support

**Problem**: Provide customer support in multiple languages with consistent quality

**Requirements**
- Auto-detect language
- Respond in customer's language
- Maintain consistent brand voice
- Translate internal knowledge base

**Solution**
```python
def multilingual_support_bot(customer_message, knowledge_base):
    """Handle customer support in any language"""

    # First, detect intent in original language
    intent_prompt = f"""
    Customer message: {customer_message}

    Identify:
    1. Language of the message
    2. Customer intent (billing, technical_support, account, general_inquiry)
    3. Urgency level (low, medium, high)
    4. Key entities (account numbers, product names, etc.)

    Return as JSON.
    """

    intent_response = client.models.generate_content(
        model=model,
        contents=intent_prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
        ),
    )

    # Generate response
    support_prompt = f"""
    You are a customer support agent. A customer sent this message:

    Message: {customer_message}

    Context from knowledge base:
    {knowledge_base}

    Provide:
    1. Helpful response in the SAME language as the customer's message
    2. Professional and empathetic tone
    3. Step-by-step instructions if applicable
    4. Escalation recommendation if needed

    Response:
    """

    response = client.models.generate_content(
        model=chat_model,
        contents=support_prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
        ),
    )
    return response.text

# Example
customer_msg = "Bonjour, je n'arrive pas à me connecter à mon compte"
knowledge_base = "Login issues: Check password, clear cache, verify email"

response = multilingual_support_bot(customer_msg, knowledge_base)
```

**Exam Tip**: Gemini handles many languages directly. No need to translate first; ask it to respond in the detected language.

### Scenario 4: Contract Analysis and Extraction

**Problem**: Extract key terms from legal contracts automatically

**Requirements**
- Identify parties involved
- Extract dates and deadlines
- Find financial terms
- Identify obligations and restrictions
- Flag unusual clauses

**Solution**
```python
def analyze_contract(contract_text):
    """Extract structured information from contract"""

    prompt = f"""
    Analyze the following contract and extract:

    Contract:
    {contract_text}

    Extract:
    1. Parties (names and roles)
    2. Effective date and term
    3. Financial terms (amounts, payment schedule)
    4. Key obligations for each party
    5. Termination conditions
    6. Unusual or high-risk clauses

    Return as structured JSON with confidence scores for each extraction.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.1,
            max_output_tokens=2048,
        ),
    )

    return response.text

# For multi-page PDFs with Gemini Vision
def analyze_contract_pdf(pdf_uri):
    """Analyze contract from PDF"""
    vision_model = "gemini-3.8-flash"

    pdf_part = types.Part.from_uri(file_uri=pdf_uri, mime_type="application/pdf")

    prompt = """Extract key contract terms from this PDF:
    - Parties and roles
    - Dates and deadlines
    - Financial terms
    - Key obligations
    - Risk factors

    Format as JSON.
    """

    response = client.models.generate_content(
        model=vision_model,
        contents=[pdf_part, prompt],
    )
    return response.text
```

**Exam Tip**: Current Gemini models read PDF and image documents directly. Use low temperature (0.1-0.2) for factual extraction.

### Scenario 5: Content Moderation Pipeline

**Problem**: Implement multi-stage content moderation for user-generated content

**Requirements**
- Detect harmful content
- Classify severity
- Identify specific violations
- Suggest automated actions
- Maintain audit trail

**Solution**
```python
from google import genai
from google.genai import types

client = genai.Client()

def moderate_content(user_content):
    """Multi-stage content moderation"""

    # Stage 1: Safety filter check
    safety_settings = [
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
        types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
    ]

    # Stage 2: Detailed analysis
    analysis_prompt = f"""
    Analyze this user-generated content for policy violations:

    Content: {user_content}

    Check for:
    1. Hate speech or harassment
    2. Violence or dangerous content
    3. Spam or misleading information
    4. Personal attacks
    5. Policy-specific violations

    Return:
    {{
      "is_safe": true/false,
      "violations": ["type1", "type2"],
      "severity": "low/medium/high",
      "confidence": 0.0-1.0,
      "explanation": "...",
      "recommended_action": "approve/review/reject"
    }}
    """

    try:
        response = client.models.generate_content(
            model=model,
            contents=analysis_prompt,
            config=types.GenerateContentConfig(
                safety_settings=safety_settings,
            ),
        )

        moderation_result = response.text

        # Stage 3: PII check
        if contains_pii(user_content):
            moderation_result['pii_detected'] = True
            moderation_result['recommended_action'] = 'review'

        return moderation_result

    except Exception as e:
        # Fail closed: an API error here means the content went unchecked
        return {
            'is_safe': False,
            'violations': ['safety_filter_triggered'],
            'severity': 'high',
            'recommended_action': 'reject',
            'error': str(e)
        }
```

**Exam Tip**: Layer safety filters (automated) with prompt-based analysis (detailed) for comprehensive moderation.

### Scenario 6: Automated Test Case Generation

**Problem**: Generate comprehensive test cases for software features

**Requirements**
- Unit tests
- Integration tests
- Edge cases
- Performance tests
- Multiple frameworks

**Solution**
```python
def generate_test_suite(feature_description, code=None):
    """Generate comprehensive test suite"""

    prompt = f"""
    Generate a comprehensive test suite for:

    Feature: {feature_description}
    {f"Implementation: {code}" if code else ""}

    Create:
    1. Unit tests for core functionality
    2. Edge case tests (empty inputs, boundaries, nulls)
    3. Integration tests if applicable
    4. Performance/load tests
    5. Security tests (injection, validation)

    Requirements:
    - Use pytest framework
    - Include setup and teardown
    - Add descriptive test names
    - Include assertions with messages
    - Cover positive and negative cases

    Test suite:
    """

    response = client.models.generate_content(
        model=code_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=2048,
        ),
    )
    return response.text

# Example
feature = """
API endpoint: POST /api/users
- Creates new user account
- Validates email format
- Checks for duplicate emails
- Requires password (min 8 chars)
- Returns user ID on success
"""

test_suite = generate_test_suite(feature)
```

**Prompt Engineering Tip**: Specify framework and style (pytest, unittest, Jest) for consistent output.

### Scenario 7: Personalized Email Campaign

**Problem**: Generate personalized emails for different customer segments

**Requirements**
- Segment-specific messaging
- Personalization at scale
- A/B test variations
- Consistent brand voice
- Call-to-action optimization

**Solution**
```python
def generate_personalized_email(customer_segment, campaign_goal, customer_data):
    """Generate personalized email content"""

    prompt = f"""
    Create a personalized email for:

    Customer Segment: {customer_segment}
    Campaign Goal: {campaign_goal}

    Customer Data:
    - Name: {customer_data.get('name', 'Valued Customer')}
    - Purchase History: {customer_data.get('purchase_history', 'New customer')}
    - Interests: {', '.join(customer_data.get('interests', []))}
    - Engagement Level: {customer_data.get('engagement', 'medium')}

    Email Requirements:
    - Subject line (compelling, under 50 chars)
    - Greeting (personalized)
    - Body (2-3 paragraphs, conversational tone)
    - Personalized product recommendations
    - Clear call-to-action
    - Sign-off

    Brand Voice: Professional yet friendly, helpful, not pushy

    Email:
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=512,
        ),
    )

    return response.text

def generate_ab_variations(base_email, num_variations=3):
    """Create A/B test variations"""
    variations = []

    for i in range(num_variations):
        prompt = f"""
        Create a variation of this email that tests a different approach:

        Original:
        {base_email}

        Variation {i+1} should:
        - Keep the same core message
        - Try a different hook/opening
        - Vary the CTA placement or wording
        - Adjust tone slightly (more urgent, more casual, etc.)

        Variation:
        """

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.8,
            ),
        )
        variations.append(response.text)

    return variations

# Example
customer = {
    'name': 'Sarah',
    'purchase_history': 'Purchased laptop 3 months ago',
    'interests': ['productivity software', 'tech gadgets'],
    'engagement': 'high'
}

email = generate_personalized_email(
    customer_segment='tech_enthusiast',
    campaign_goal='Promote new software bundle',
    customer_data=customer
)

variations = generate_ab_variations(email, num_variations=2)
```

**Exam Tip**: Use temperature 0.7-0.8 for creative content that needs variation while maintaining consistency.

### Scenario 8: Meeting Summarization and Action Items

**Problem**: Automatically summarize meetings and extract action items

**Requirements**
- Key discussion points
- Decisions made
- Action items with owners
- Follow-up questions
- Sentiment analysis

**Solution**
```python
def summarize_meeting(transcript):
    """Generate comprehensive meeting summary"""

    prompt = f"""
    Analyze this meeting transcript and provide:

    Transcript:
    {transcript}

    Generate:
    1. Executive Summary (2-3 sentences)
    2. Key Discussion Points (bulleted list)
    3. Decisions Made (list with context)
    4. Action Items (task, owner, deadline if mentioned)
    5. Open Questions or Follow-ups
    6. Next Steps

    Format as structured JSON for easy parsing.

    Summary:
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=1024,
        ),
    )

    return response.text

def extract_action_items(transcript):
    """Extract specific action items with tracking"""

    prompt = f"""
    Extract all action items from this meeting transcript:

    {transcript}

    For each action item, identify:
    - Task description
    - Person responsible (if mentioned)
    - Deadline (if mentioned)
    - Priority (inferred from context)
    - Dependencies

    Return as JSON array:
    [
      {{
        "task": "...",
        "owner": "...",
        "deadline": "...",
        "priority": "high/medium/low",
        "dependencies": [...]
      }}
    ]
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
        ),
    )
    return response.text
```

**Exam Tip**: Use chain-of-thought prompting for complex extraction: "First identify speakers, then topics, then decisions..."

### Scenario 9: SQL Query Generation from Natural Language

**Problem**: Convert natural language questions to SQL queries

**Requirements**
- Understand database schema
- Generate correct SQL syntax
- Handle complex joins
- Optimize queries
- Explain query logic

**Solution**
```python
def generate_sql_query(question, schema):
    """Generate SQL from natural language"""

    prompt = f"""
    Database Schema:
    {schema}

    Question: {question}

    Generate:
    1. SQL query to answer the question
    2. Explanation of the query logic
    3. Expected result format

    Requirements:
    - Use proper joins and indexes
    - Include appropriate filters
    - Optimize for performance
    - Use standard SQL syntax

    SQL Query:
    """

    response = client.models.generate_content(
        model=code_model,
        contents=prompt,
    )

    return response.text

# Example
schema = """
Tables:
- customers (id, name, email, created_at)
- orders (id, customer_id, total, status, order_date)
- order_items (id, order_id, product_id, quantity, price)
- products (id, name, category, price)
"""

question = "What are the top 5 customers by total order value in the last 6 months?"

sql = generate_sql_query(question, schema)
```

**Exam Tip**: Include schema in prompt for accurate query generation. `gemini-3.8-flash` handles SQL generation; there is no separate code model.

### Scenario 10: Image Analysis for Product Defects

**Problem**: Analyze product images to detect defects

**Requirements**
- Identify defects visually
- Classify defect severity
- Suggest corrective actions
- Generate quality report

**Solution**
```python
from google import genai
from google.genai import types

client = genai.Client()

def analyze_product_image(image_uri, product_type):
    """Analyze product image for defects"""

    vision_model = "gemini-3.8-flash"

    image = types.Part.from_uri(file_uri=image_uri, mime_type="image/jpeg")

    prompt = f"""
    Analyze this {product_type} image for quality control:

    Look for:
    1. Surface defects (scratches, dents, discoloration)
    2. Assembly issues (misalignment, gaps)
    3. Labeling problems (incorrect, missing, damaged)
    4. Packaging condition
    5. Overall quality assessment

    Provide:
    - Defects found (with locations)
    - Severity (minor, moderate, critical)
    - Pass/Fail recommendation
    - Detailed description
    - Suggested corrective actions

    Format as JSON.

    Analysis:
    """

    response = client.models.generate_content(
        model=vision_model,
        contents=[image, prompt],
    )
    return response.text

# Batch processing
def batch_quality_inspection(image_uris, product_type):
    """Inspect multiple product images"""
    results = []

    for uri in image_uris:
        analysis = analyze_product_image(uri, product_type)
        results.append({
            'image': uri,
            'analysis': analysis
        })

    # Generate summary report
    summary_prompt = f"""
    Quality inspection results for {len(image_uris)} {product_type} items:

    {results}

    Generate summary report:
    - Total items inspected
    - Pass/fail breakdown
    - Common defects
    - Defect rate by category
    - Recommendations for process improvement

    Report:
    """

    summary = client.models.generate_content(
        model=model,
        contents=summary_prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        ),
    )
    return results, summary.text
```

**Exam Tip**: Any current Gemini model can analyze images; `gemini-3.8-flash` is the sensible default. Provide structured output format (JSON) for easy parsing.

## Best Practices

### Development

1. **Start with Prompt Engineering**
   - Iterate quickly
   - Test variations
   - Document effective prompts

2. **Use Appropriate Model Size**
   - `gemini-3.5-flash-lite`: Simple, high-volume tasks
   - `gemini-3.8-flash`: General use, best balance
   - `gemini-4-argon`: Hardest reasoning

3. **Optimize Parameters**
   - Temperature for creativity vs consistency
   - Token limits for cost control
   - Safety filters for content moderation

4. **Test Thoroughly**
   - Diverse inputs
   - Edge cases
   - Bias evaluation
   - Safety testing

### Production

1. **Monitor Performance**
   - Response quality
   - Latency metrics
   - Error rates
   - User feedback

2. **Cost Optimization**
   - Appropriate model selection
   - Caching strategies
   - Batch processing
   - Token usage optimization

3. **Safety and Compliance**
   - Content filtering
   - PII detection
   - Audit logging
   - Compliance requirements

4. **Version Control**
   - Track model versions
   - Prompt versioning
   - A/B testing
   - Rollback capability

## Exam Tips

### Key Concepts to Master

**Foundation Models**
- `gemini-3.8-flash`: Default for text, code, chat and multimodal input
- `gemini-4-argon`: Most capable, complex reasoning
- `gemini-3.5-flash-lite`: Low cost, high volume
- `gemini-3.5-flash`: Tunable base model
- Gemini Nano: On-device, privacy-preserving, not served through Agent Platform
- `gemini-3.1-flash-image`: Image generation and editing (replaced Imagen)
- Open models such as Llama and Gemma via Model Garden

**Architecture Knowledge**
- Understand transformer architecture (attention, encoder/decoder)
- Know tokenization impact on context window
- Multi-head attention benefits
- Decoder-only vs encoder-decoder architectures
- Temperature, top-k, top-p sampling methods

**Prompt Engineering Mastery**
- Zero-shot: No examples, direct instruction
- Few-shot: 2-5 examples, improves accuracy
- Chain-of-thought: Step-by-step reasoning for complex tasks
- Role-based: Set persona/expertise level
- Structured output: Request JSON/CSV format
- Low temp (0.1-0.3) for factual, high (0.7-0.9) for creative

**Responsible AI Principles**
- Know all 7 Google AI Principles
- Safety filters: 4 harm categories, blocking thresholds from OFF to BLOCK_LOW_AND_ABOVE, off by default on current models
- Bias detection and mitigation strategies
- PII handling with Cloud DLP
- Content moderation (input, output, context layers)
- Human oversight for high-stakes applications

### Model Selection Decision Tree

```
Question requires:
├─ Generating an image → gemini-3.1-flash-image
├─ Generating a video → veo-3.1-generate-001
├─ Understanding images, video, audio or PDFs → gemini-3.8-flash
├─ Code generation, review or completion → gemini-3.8-flash
├─ Text
│  ├─ General, including long context and many languages → gemini-3.8-flash
│  ├─ High volume, low cost → gemini-3.5-flash-lite
│  ├─ Hardest reasoning → gemini-4-argon
│  ├─ Must be tuned → gemini-3.5-flash or gemini-3.5-flash-lite
│  └─ On-device → Gemini Nano (Android, not Agent Platform)
└─ Embeddings/similarity → gemini-embedding-001
```

### Service Selection Matrix

| Use Case | Primary Model | Alternative | Key Parameters |
|----------|--------------|-------------|----------------|
| Text generation | gemini-3.8-flash | gemini-3.5-flash-lite | temp=0.7, max_output_tokens=1024 |
| Chatbot | gemini-3.8-flash | gemini-3.5-flash-lite | system_instruction + history |
| Code generation | gemini-3.8-flash | gemini-4-argon | temp=0.2-0.4 |
| Summarization | gemini-3.8-flash | gemini-3.5-flash-lite | temp=0.3, concise prompt |
| Translation | gemini-3.8-flash | gemini-3.5-flash-lite | temp=0.3, specify languages |
| Image generation | gemini-3.1-flash-image | gemini-3-pro-image | response_modalities |
| Image analysis | gemini-3.8-flash | gemini-3.5-flash-lite | structured output |
| Embeddings | gemini-embedding-001 | gemini-embedding-2 | output_dimensionality |
| Classification | gemini-3.5-flash-lite | gemini-3.8-flash | temp=0.1-0.2, few-shot |
| Q&A with docs | gemini-3.8-flash + embeddings | gemini-4-argon | RAG pattern |

### Common Exam Scenarios and Solutions

**Scenario Type 1: Model Selection**
- Question: "Need to analyze PDF invoices and extract structured data"
- Answer: `gemini-3.8-flash` (reads PDFs directly, returns structured output)
- Why not others: an image model generates images, and an embedding model only returns vectors

**Scenario Type 2: Prompt Engineering**
- Question: "Generate consistent product classifications"
- Answer: Few-shot prompting + low temperature (0.1-0.2)
- Include: 3-5 examples, explicit categories, structured output format

**Scenario Type 3: Responsible AI**
- Question: "Implement content moderation for user posts"
- Answer: Multi-layer approach:
  1. Safety filters (HarmCategory + HarmBlockThreshold)
  2. Prompt-based analysis
  3. PII detection (Cloud DLP)
  4. Human review for edge cases

**Scenario Type 4: Performance Optimization**
- Question: "Reduce latency and costs for FAQ chatbot"
- Answer:
  - Cache common queries (Memorystore)
  - Use a smaller model (`gemini-3.5-flash-lite` for simple tasks)
  - Batch requests when possible
  - Implement rate limiting
  - Monitor token usage

**Scenario Type 5: Fine-tuning Decision**
- Question: "When to fine-tune vs prompt engineering?"
- Answer: Start with prompts. Fine-tune when:
  - Domain-specific terminology needed
  - Consistent output format required
  - Have sufficient training data (100+ examples)
  - Prompt engineering plateaus in performance

### Temperature Selection Guidelines

| Task Type | Temperature | Rationale |
|-----------|-------------|-----------|
| Classification | 0.0 - 0.2 | Deterministic, consistent output |
| Data extraction | 0.1 - 0.2 | Factual accuracy critical |
| Summarization | 0.2 - 0.4 | Balanced, coherent synthesis |
| Q&A (factual) | 0.2 - 0.3 | Accurate information |
| Q&A (analytical) | 0.4 - 0.6 | Allow reasoning variation |
| Chat/conversation | 0.5 - 0.7 | Natural, engaging responses |
| Content creation | 0.7 - 0.8 | Creative, varied output |
| Brainstorming | 0.8 - 0.9 | Maximum creativity |
| Code generation | 0.2 - 0.4 | Correct syntax, logical |
| Translation | 0.2 - 0.3 | Accurate, consistent |

### Context Window Management

**Token Limits**
- Flash and Flash-Lite models: 1,048,576 tokens of context, 65,536 maximum output
- `gemini-4-argon`: 1,048,576 tokens shared by input and output
- `gemini-embedding-001`: 2,048 tokens per input
- Remember: Input + output counts toward limit

**When Exceeding Context**
1. Summarize conversation history
2. Use sliding window (keep recent messages)
3. Extract and store key information
4. Use context caching for a large repeated prefix
5. Implement RAG pattern with embeddings

### Safety Filter Configuration

**Filter Strictness by Use Case**

| Use Case | Recommended Settings | Rationale |
|----------|---------------------|-----------|
| Children's content | BLOCK_LOW_AND_ABOVE all categories | Maximum protection |
| Customer support | BLOCK_MEDIUM_AND_ABOVE all | Professional, safe |
| Creative writing | BLOCK_ONLY_HIGH, selective | Allow creative freedom |
| Internal tools | BLOCK_MEDIUM_AND_ABOVE | Balance safety/utility |
| Research/analysis | BLOCK_ONLY_HIGH | Minimize false positives |

**Always monitor and log**:
- Safety filter activations
- User feedback on blocked content
- False positive rates
- Adjust thresholds based on data

### Embeddings and RAG Pattern

**When to Use Embeddings**
- Semantic search over documents
- Find similar items/recommendations
- Cluster/categorize content
- RAG (Retrieval-Augmented Generation)
- Q&A with dynamic knowledge base

**RAG Implementation Pattern**
```python
# 1. Create embeddings for knowledge base
embeddings = client.models.embed_content(model=embedding_model, contents=documents).embeddings

# 2. Store vectors (Vector Search, Firestore)

# 3. For query:
#    a. Embed query
#    b. Find top-k similar documents (cosine similarity)
#    c. Include in prompt as context

# 4. Generate answer with context
response = client.models.generate_content(
    model=model,
    contents=f"Context: {context}\nQuestion: {query}",
)
```

**Exam Tip**: RAG updates knowledge without retraining. Use for dynamic information.

### Agent Studio Features

**Know These Capabilities**
1. **Model Garden**: Access to foundation models (Google + open source)
2. **Prompt Design**: Test and iterate prompts
3. **Tuning**: Supervised fine-tuning, adapter tuning
4. **Evaluation**: Compare model responses
5. **Deployment**: One-click deploy to endpoints
6. **Batch Prediction**: Process multiple inputs efficiently
7. **Safety Settings**: Configure filters per request

### Code Generation Best Practices

**For Exam**
- Use `gemini-3.8-flash` for generation, completion and review alike
- Use a chat session for conversational assistance
- Use a lower temperature when you want repeatable output
- Temperature 0.2-0.4 for correct syntax
- Include language specification in prompt
- Request docstrings and type hints
- Ask for error handling and edge cases

**Example Prompt Structure**
```python
"""
Write a [language] [function/class] that:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

Include:
- Type hints / annotations
- Docstring
- Error handling
- Edge case handling

[Language] code:
"""
```

### Multimodal (Gemini) Capabilities

**Image Understanding**
- Image description and captioning
- Object detection and counting
- OCR (text extraction)
- Visual question answering
- Image comparison

**Document Processing**
- PDF analysis (multi-page)
- Form/invoice extraction
- Table extraction
- Diagram understanding

**Video Understanding**
- Video summarization
- Event detection
- Frame-by-frame analysis
- Visual Q&A

**Exam Tip**: Gemini is natively multimodal (not separate models bolted together)

### Common Pitfalls to Avoid

1. **Using wrong model**
   - Don't reach for an image model to read an image → Use `gemini-3.8-flash`
   - Don't plan on tuning `gemini-3.8-flash` → It isn't supported; use `gemini-3.5-flash`

2. **Temperature mistakes**
   - High temp for classification → Inconsistent results
   - Low temp for creative tasks → Repetitive output

3. **Context window**
   - Forgetting input + output counts toward limit
   - Not monitoring token usage
   - Exceeding limit causes truncation/errors

4. **Safety filters**
   - Too restrictive → False positives, poor UX
   - Too lenient → Policy violations
   - Not handling blocked responses gracefully

5. **Prompt engineering**
   - Vague instructions → Poor results
   - No examples for complex tasks → Lower accuracy
   - Not iterating and testing → Suboptimal performance

6. **Responsible AI**
   - Skipping bias testing
   - No PII detection
   - Missing content moderation
   - Inadequate human oversight

### Exam Question Patterns

**Pattern 1: "Which model should you use for...?"**
- Look for keywords: generate an image (image model), tune (a tunable model), high volume (Flash-Lite)
- Consider context window requirements
- Think about specialized capabilities

**Pattern 2: "How to improve prompt performance?"**
- Add examples (few-shot)
- Use chain-of-thought for reasoning
- Specify output format
- Adjust temperature
- Provide more context

**Pattern 3: "Responsible AI requirement..."**
- Always layer multiple approaches
- Use safety filters + prompt engineering
- Implement PII detection (Cloud DLP)
- Add human review for critical applications
- Monitor and audit continuously

**Pattern 4: "Optimize cost/performance..."**
- Right-size model selection
- Implement caching
- Batch requests
- Monitor token usage
- Use cheaper models for simple tasks

**Pattern 5: "Fine-tuning vs prompt engineering?"**
- Start with prompts (faster, cheaper)
- Fine-tune for: domain terminology, consistent format, better performance
- Need 100+ quality examples for fine-tuning
- Adapter tuning as middle ground

### Quick Reference: Key APIs

**Text Generation**
```python
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-flash"
response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1024,
    ),
)
```

**Chat**
```python
from google import genai

client = genai.Client()
chat_model = "gemini-3.8-flash"
chat = client.chats.create(
    model=chat_model,
    config=types.GenerateContentConfig(system_instruction="..."),
    history=[...],  # few-shot examples as earlier turns
)
response = chat.send_message("message")
```

**Code Generation**
```python
from google import genai

client = genai.Client()
code_model = "gemini-3.8-flash"
response = client.models.generate_content(
    model=code_model,
    contents="prompt",
)
```

**Gemini (Multimodal)**
```python
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-flash"
image = types.Part.from_uri(file_uri="gs://bucket/image.jpg", mime_type="image/jpeg")
response = client.models.generate_content(
    model=model,
    contents=[image, "prompt"],
)
```

**Embeddings**
```python
from google import genai

client = genai.Client()
embedding_model = "gemini-embedding-001"
embeddings = client.models.embed_content(model=embedding_model, contents=["text1", "text2"]).embeddings
```

**Safety Settings**
```python
from google import genai
from google.genai import types
safety_settings = [
    types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE),
]
```

### Final Exam Preparation Checklist

**Conceptual Understanding**
- [ ] Generative AI vs discriminative AI
- [ ] Foundation models and transfer learning
- [ ] Transformer architecture basics
- [ ] Tokenization and context windows
- [ ] Attention mechanisms
- [ ] Temperature and sampling methods

**Google Models**
- [ ] Gemini tiers (Argon, Flash, Flash-Lite) and which ones can be tuned
- [ ] Model retirement dates and how to check them
- [ ] Gemini image models for image generation
- [ ] Text embeddings with `gemini-embedding-001`

**Prompt Engineering**
- [ ] Zero-shot vs few-shot
- [ ] Chain-of-thought reasoning
- [ ] Role-based prompting
- [ ] Structured output formats
- [ ] Temperature selection by task
- [ ] Context window management

**Responsible AI**
- [ ] 7 Google AI Principles
- [ ] Harm categories and blocking levels
- [ ] Bias detection and mitigation
- [ ] PII handling with Cloud DLP
- [ ] Content moderation strategies
- [ ] Transparency and accountability

**Implementation**
- [ ] Agent Studio
- [ ] Python SDK usage
- [ ] REST API endpoints
- [ ] Model Garden access
- [ ] Fine-tuning process
- [ ] RAG pattern with embeddings

**Use Cases**
- [ ] Chatbots and customer support
- [ ] Content generation
- [ ] Code assistance
- [ ] Document processing
- [ ] Summarization and translation
- [ ] Image analysis and generation

**Best Practices**
- [ ] Model selection criteria
- [ ] Performance optimization
- [ ] Cost management
- [ ] Safety and compliance
- [ ] Monitoring and iteration
- [ ] Production deployment patterns

### Study Strategy

1. **Hands-on Practice**: Use Agent Studio
2. **Prompt Engineering**: Practice zero-shot, few-shot, chain-of-thought
3. **Model Comparison**: Test different models on same tasks
4. **Responsible AI**: Implement safety filters and bias testing
5. **Scenarios**: Work through real-world use cases
6. **APIs**: Practice with Python SDK and REST APIs
7. **Documentation**: Review official Google Cloud Gen AI docs

**Exam Focus**: Understanding when and why to use specific models, prompt engineering techniques, and responsible AI practices.
