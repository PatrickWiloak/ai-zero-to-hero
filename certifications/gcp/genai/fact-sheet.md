---
last-updated: 2026-11-06
---

# Google Cloud Generative AI - Fact Sheet

## Quick Reference

**Certification Focus:** Generative AI on Google Cloud
**Target Audience:** ML Engineers, AI Developers, Data Scientists
**Core Platform:** Agent Platform (formerly Vertex AI) with Gen AI capabilities
**Key Technologies:** Gemini (Argon, Flash, Flash-Lite), Gemini image models, Veo, Gemini embeddings, Chirp
**Prerequisites:** Understanding of ML fundamentals and GCP basics

## Core Domains

| Domain | Focus |
|--------|-------|
| Foundation Models | Gemini tiers, model lifecycle, understanding model capabilities |
| Agent Studio | Prompt design, model tuning, experimentation |
| MLOps for GenAI | Production deployment, monitoring, versioning |
| Responsible AI | Safety, fairness, bias mitigation, governance |
| Application Integration | API usage, embeddings, grounding, RAG patterns |

## Essential Google Cloud GenAI Services

### Agent Studio

**Model Garden**
- Pre-trained foundation models
- Task-specific models (text, code, chat, embeddings)
- Partner models (Anthropic Claude, Grok, Mistral AI) and open-weight models (Llama, DeepSeek, Qwen, Gemma)
- Model versioning and comparison
- **[📖 Model Garden Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)** - Browse and deploy models

**Agent Studio**
- Prompt design and testing interface
- Few-shot learning examples
- Parameter tuning (temperature, top-k, top-p)
- Prompt templates and management
- **[📖 Agent Studio Guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide)** - Studio overview

**Gemini Models**
- `gemini-4-argon`: frontier model; 1,048,576 tokens shared by input and output; not tunable
- `gemini-3.8-flash`: the default workhorse; 1,048,576 in, 65,536 out; not tunable
- `gemini-3.5-flash`: previous workhorse; supports supervised tuning
- `gemini-3.5-flash-lite`: lowest cost for high-volume tasks; supports supervised tuning
- All accept text, image, audio, video and PDF input
- PaLM 2 and Codey retired on April 21, 2025 and Gemini replaced them
- **[📖 Model lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions)** - IDs, retirement dates, replacements
- **[📖 Google Gen AI SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/sdks/overview)** - The SDK to use
- **[📖 Prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/introduction-prompt-design)** - Optimization guide

### Embeddings and Grounding

**Text Embeddings (`gemini-embedding-001`)**
- Generate vector representations
- Semantic search and similarity
- Up to 3,072 dimensions, adjustable with `output_dimensionality`
- Batch processing support
- **[📖 Embeddings API Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings)** - Embedding generation
- **[📖 Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview)** - Similarity search at scale

**Grounding with Google Search**
- Ground model responses with real-time search
- Reduce hallucinations with factual data
- Citation and source attribution
- Configurable grounding sources
- **[📖 Grounding Documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)** - Grounding setup
- **[📖 Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs)** - Enterprise search

**Retrieval Augmented Generation (RAG)**
- Ground responses with your own data
- Vector database integration
- Context injection patterns
- Document retrieval and ranking
- **[📖 RAG Patterns](https://cloud.google.com/blog/products/ai-machine-learning/rag-patterns-with-vertex-ai)** - Implementation guide

### Specialized Models

**Gemini image models (`gemini-3.1-flash-image`, `gemini-3-pro-image`)**
- Text-to-image generation through `generate_content`
- Image editing by sending the source image with an instruction
- Replaced Imagen, which retired on June 30, 2026
- **[📖 Generate images with Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/image-generation)** - Image generation

**Chirp (Universal Speech Model)**
- Speech-to-text with high accuracy
- 100+ language support
- Model adaptation and tuning
- Streaming and batch processing
- **[📖 Chirp Documentation](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3)** - Speech recognition

## Model Tuning and Customization

### Prompt Engineering

**Prompt Design Principles**
```
- Clear instructions and context
- Few-shot examples for guidance
- Output format specification
- Role and persona definition
- Constraints and boundaries
```

**Parameter Tuning**
- **Temperature (0-1):** Randomness control (0=deterministic, 1=creative)
- **Top-k:** Limit to top k tokens
- **Top-p (nucleus sampling):** Cumulative probability threshold
- **Max output tokens:** Response length control
- **[📖 Prompt Design Guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies)** - Best practices

### Model Tuning

**Supervised fine-tuning**
- Trains on labeled input and output pairs; start with 100 to 500 examples
- Suits classification, extraction and strict output formats
- Supported on `gemini-3.5-flash`, `gemini-3.5-flash-lite` and `gemini-3.1-flash-lite`; not on `gemini-3.8-flash` or `gemini-4-argon`
- Parameter-efficient (adapter) tuning updates a small subset of parameters, so it costs less than full fine-tuning
- **[📖 Supervised tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning)** - Tuning process

**Preference and reinforcement learning fine-tuning**
- Preference tuning learns from pairs of chosen and rejected responses
- Reinforcement learning fine-tuning maximizes scores from up to 16 weighted reward functions
- These are the current names for what older material calls RLHF
- **[📖 Tuning overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)** - Compares the methods

## MLOps for Generative AI

### Deployment and Serving

**Agent Platform Endpoints**
- Deploy models to prediction endpoints
- Auto-scaling based on traffic
- A/B testing with traffic splitting
- Monitoring and logging integration
- **[📖 Deploy Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment)** - Endpoint configuration
- **[📖 Online Prediction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions)** - Inference APIs

**Agent Platform Pipelines for GenAI**
- Automate model training and deployment
- Data preprocessing workflows
- Model evaluation and validation
- Continuous training pipelines
- **[📖 Pipelines Guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction)** - Workflow automation
- **[📖 Kubeflow Integration](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline)** - Pipeline development

### Monitoring and Evaluation

**Model Monitoring**
- Prediction drift detection
- Input/output analysis
- Latency and throughput tracking
- Error rate monitoring
- **[📖 Model Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview)** - Production monitoring

**Evaluation Metrics for GenAI**
- ROUGE scores (summarization)
- BLEU scores (translation)
- Perplexity (language models)
- Human evaluation frameworks
- **[📖 Model Evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction)** - Metrics and methods

## Responsible AI Practices

### Safety and Filtering

**Content Filtering**
- Toxicity detection and filtering
- PII (Personally Identifiable Information) detection
- Harmful content categories
- Configurable thresholds, with `OFF` the default on `gemini-3.5-flash` and later
- **[📖 Safety Filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters)** - Content safety

**Bias Mitigation**
- Fairness evaluation
- Demographic parity assessment
- Bias detection in outputs
- Inclusive dataset curation
- **[📖 Responsible AI Toolkit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai)** - Fairness tools

### Privacy and Governance

**Data Privacy**
- Customer data isolation
- No training on customer data (opt-in model tuning only)
- GDPR and regulatory compliance
- Data residency options
- **[📖 Data Governance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations)** - Regional compliance

**AI Principles**
- Google's AI Principles
- Transparency and explainability
- Accountability frameworks
- Ethical AI development
- **[📖 Google AI Principles](https://ai.google/principles/)** - Ethical guidelines

## Application Integration Patterns

### API Integration

**Python SDK**
```python
# Google Gen AI SDK. Set GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION=global
# and GOOGLE_GENAI_USE_ENTERPRISE=True first.
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Write a haiku about cloud computing",
    config=types.GenerateContentConfig(temperature=0.8, max_output_tokens=256),
)
print(response.text)
```
- **[📖 Gen AI SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/sdks/overview)** - Client library
- **[📖 REST API Reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest)** - HTTP API

### Common Architectures

**Chatbot with Context**
- Cloud Run frontend
- `gemini-3.8-flash` through a chat session
- Firestore for conversation history
- Cloud Functions for orchestration

**Document Q&A System**
- Document embedding generation
- Vector Search for retrieval
- `gemini-3.8-flash` for answer generation
- Cloud Storage for document storage

**Code Assistant**
- `gemini-3.8-flash` for generation
- GitHub/GitLab integration
- IDE plugins (VS Code, IntelliJ)
- Real-time code completion

## Cost Optimization

**Pricing Models**
- Pay per token, with thinking billed as output
- Batch inference at a 50% discount
- Model selection based on task complexity
- Implicit caching, 90% off cached input tokens
- **[📖 Pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)** - Cost structure

**Best Practices**
- Use appropriate model size for task
- Implement prompt caching
- Batch requests when possible
- Monitor token usage
- Set max output token limits

## Essential gcloud Commands

```bash
# Enable Agent Platform API
gcloud services enable aiplatform.googleapis.com

# List available models
gcloud ai models list --region=us-central1

# Call a model you deployed to your own endpoint
gcloud ai endpoints predict ENDPOINT_ID \
  --region=us-central1 \
  --json-request=request.json

# Deploy custom model
gcloud ai models upload \
  --region=us-central1 \
  --display-name=my-genai-model \
  --container-image-uri=gcr.io/project/image
```
- **[📖 gcloud AI Commands](https://cloud.google.com/sdk/gcloud/reference/ai)** - Command reference

## Key Concepts to Master

### Model Selection
- `gemini-3.8-flash` for text, chat, code and multimodal input
- `gemini-4-argon` for the hardest reasoning
- `gemini-3.5-flash-lite` for high-volume, low-cost tasks
- `gemini-3.5-flash` when the model must be tuned
- `gemini-3.1-flash-image` for image generation

### Prompt Engineering
- Clear and specific instructions
- Few-shot learning examples
- System prompts and personas
- Output format specification
- Iterative prompt refinement

### Production Deployment
- Model endpoint configuration
- Auto-scaling and load balancing
- Monitoring and alerting
- Version management
- A/B testing strategies

### Responsible AI
- Content safety filtering
- Bias detection and mitigation
- Privacy and data governance
- Transparency and explainability
- Human oversight and review

## Common Scenarios

**Scenario 1: Customer Support Chatbot**
- Solution: Agent Platform `gemini-3.8-flash` + Dialogflow CX + Firestore + Cloud Run

**Scenario 2: Document Summarization Pipeline**
- Solution: Cloud Storage + Cloud Functions + `gemini-3.8-flash` + BigQuery

**Scenario 3: Code Review Assistant**
- Solution: GitHub webhooks + `gemini-3.8-flash` + Cloud Functions + Slack integration

**Scenario 4: Content Generation Platform**
- Solution: `gemini-3.8-flash` + `gemini-3.1-flash-image` + Cloud Run + Cloud CDN + Firebase

**Scenario 5: Enterprise Search with GenAI**
- Solution: Agent Search + `gemini-4-argon` grounding + Vector Search + IAM for access control

## Study Resources

### Official Google Resources

**[📖 Generative AI Learning Path](https://www.cloudskillsboost.google/paths/118)** - Free Google Cloud Skills Boost path

**[📖 Agent Platform Generative AI documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)** - Complete documentation

**[📖 GenAI on Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning)** - Latest updates and tutorials

**[📖 Google Colab Notebooks](https://github.com/GoogleCloudPlatform/generative-ai)** - Hands-on examples

### Hands-On Practice

1. **Basic Text Generation**
   - Use Agent Studio
   - Test different prompts and parameters
   - Compare model outputs
   - Export code for application integration

2. **Embeddings and Vector Search**
   - Generate text embeddings
   - Store in Vector Search
   - Implement similarity search
   - Build RAG application

3. **Model Tuning**
   - Prepare training dataset
   - Tune `gemini-3.5-flash` with supervised tuning
   - Evaluate tuned vs base model
   - Call the endpoint the tuning job creates

4. **Multimodal with Gemini**
   - Process images with text prompts
   - Extract information from documents
   - Compare `gemini-3.8-flash` and `gemini-3.5-flash-lite`
   - Build multimodal application

5. **Production Deployment**
   - Deploy model to endpoint
   - Implement monitoring
   - Set up A/B testing
   - Configure auto-scaling

## Exam Tips

### Focus Areas
- Understand model capabilities and selection criteria
- Master prompt engineering techniques
- Know RAG and grounding patterns
- Understand tuning options (supervised, preference, reinforcement learning) and which models support them
- Be familiar with responsible AI practices
- Know deployment and monitoring strategies

### Common Question Topics
- When to use Argon vs Flash vs Flash-Lite
- RAG vs fine-tuning trade-offs
- Content filtering configuration
- Token limits and context windows
- Cost optimization strategies
- Multi-model architectures

### Hands-On Skills Required
- Use Agent Studio effectively
- Write effective prompts
- Implement embeddings and vector search
- Deploy models to endpoints
- Configure monitoring and alerts
- Use the Google Gen AI SDK

---

**Last Updated:** 2026-11-06
**Technology Focus:** Agent Platform Generative AI
**Total Documentation Links:** 50+

---

## Notes

This fact sheet covers generative AI capabilities on Google Cloud Platform using Agent Platform. The GenAI landscape evolves rapidly, so always refer to the latest Google Cloud documentation for current model availability and capabilities.

**Good luck with your Google Cloud GenAI journey!**
