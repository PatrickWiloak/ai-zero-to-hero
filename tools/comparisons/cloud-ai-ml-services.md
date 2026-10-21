# Cloud AI/ML Services Compared

**In one line:** Map equivalent AI/ML services across AWS, Google Cloud and Azure so you can pick, or translate between, platforms quickly.
**Last reviewed:** 2026-10-21

---
## Quick Reference

This guide provides a comprehensive comparison of AI/ML services across AWS, Google Cloud Platform (GCP), and Microsoft Azure. Use this to understand equivalent services when building machine learning applications, training models, or deploying AI solutions across cloud providers.

## ML Platforms (End-to-End ML Workflow)

| Feature | AWS SageMaker | GCP Agent Platform (formerly Vertex AI) | Azure Machine Learning |
|---------|---------------|---------------|------------------------|
| **Service Name** | Amazon SageMaker | Agent Platform | Azure Machine Learning |
| **Launch Year** | 2017 | 2021 (unified platform) | 2014 (rebranded 2019) |
| **IDE/Notebooks** | SageMaker Studio, Notebook Instances | Agent Platform Workbench, Colab Enterprise | Azure ML Studio, Compute Instances |
| **Jupyter Integration** | JupyterLab in Studio | JupyterLab, Managed notebooks | JupyterLab, VS Code integration |
| **Data Labeling** | SageMaker Ground Truth | Data Labeling | Azure ML Data Labeling |
| **Feature Store** | SageMaker Feature Store | Agent Platform Feature Store | Azure ML Feature Store (preview) |
| **Training** | Built-in algorithms, custom containers | Pre-built containers, custom training | Designer, AutoML, custom scripts |
| **Distributed Training** | Data parallelism, model parallelism | Multi-node, multi-GPU | Distributed training with Horovod, DeepSpeed |
| **Hyperparameter Tuning** | Automatic Model Tuning | Vertex AI Vizier | HyperDrive |
| **Experiment Tracking** | SageMaker Experiments | Experiments on Agent Platform | Azure ML Experiments, MLflow integration |
| **Model Registry** | SageMaker Model Registry | Agent Platform Model Registry | Azure ML Model Registry |
| **Model Monitoring** | Model Monitor | Model Monitoring on Agent Platform | Model monitoring, data drift detection |
| **Deployment** | Real-time endpoints, batch, serverless | Prediction endpoints, batch | Real-time endpoints, batch endpoints |
| **A/B Testing** | Multi-model endpoints | Traffic splitting | Blue-green deployments |
| **Edge Deployment** | SageMaker Edge Manager, Neo | Edge TPU, TensorFlow Lite | Azure IoT Edge, ONNX Runtime |
| **MLOps** | SageMaker Pipelines, Projects | Agent Platform Pipelines | Azure ML Pipelines |
| **Pipeline Orchestration** | Step Functions, Pipelines | Kubeflow Pipelines, Vertex Pipelines | Azure ML Pipelines, Data Factory |
| **Supported Frameworks** | TensorFlow, PyTorch, scikit-learn, XGBoost, MXNet, Hugging Face | TensorFlow, PyTorch, scikit-learn, XGBoost | TensorFlow, PyTorch, scikit-learn, ONNX |
| **Pricing Model** | Pay per instance hour + storage | Pay per compute hour + predictions | Pay per compute hour + deployments |

**Documentation:**
- **[📖 AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)** - Complete SageMaker guide
- **[📖 GCP Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform)** - Complete Agent Platform guide
- **[📖 Azure Machine Learning Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)** - Complete Azure ML guide
- **[📖 SageMaker Studio Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)** - IDE environment
- **[📖 Agent Platform Workbench Documentation](https://cloud.google.com/vertex-ai/docs/workbench)** - Jupyter notebooks
- **[📖 Azure ML Studio Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning)** - ML workspace

---

## AutoML (Automated Machine Learning)

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Service Name** | SageMaker Autopilot | Agent Platform AutoML | Azure Automated ML |
| **Tabular Data** | Yes | Yes (Tables) | Yes |
| **Image Classification** | Canvas | Yes (Vision) | Yes |
| **Object Detection** | Canvas | Yes (Vision) | Yes |
| **Text Classification** | Canvas | Yes (Natural Language) | Yes |
| **Sentiment Analysis** | Canvas | Yes (Natural Language) | Yes |
| **Forecasting** | Canvas | Yes (Forecasting) | Yes |
| **Video Intelligence** | No native AutoML | Yes (Video) | Video Indexer (separate) |
| **Code Generation** | Automatic feature engineering | AutoML code export | Python SDK generated code |
| **Model Explainability** | Yes | Yes (Explainable AI) | Yes |
| **No-Code Interface** | SageMaker Canvas | Vertex AI UI | Azure ML Studio |
| **Custom Training Time** | Configurable | Configurable budget | Configurable |
| **Output Format** | Model artifact, notebook | Model endpoint, container | ONNX, pickle, Docker |
| **Integration** | SageMaker ecosystem | Agent Platform ecosystem | Azure ML ecosystem |

**Documentation:**
- **[📖 SageMaker Autopilot Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)** - AutoML for tabular data
- **[📖 SageMaker Canvas Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)** - No-code ML
- **[📖 Agent Platform AutoML Documentation](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)** - Automated training
- **[📖 Azure Automated ML Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-automated-ml)** - AutoML overview

---

## Computer Vision Services

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Image Analysis** | Rekognition | Vision AI | Computer Vision |
| **Object Detection** | DetectLabels | Object Localization | Detect objects |
| **Face Detection** | DetectFaces | Face Detection | Face API |
| **Face Recognition** | CompareFaces, SearchFaces | Face Recognition | Face verification, identification |
| **Celebrity Recognition** | RecognizeCelebrities | Celebrity Recognition | N/A |
| **Text in Images (OCR)** | Textract, Rekognition | Vision OCR | Computer Vision OCR, Form Recognizer |
| **Content Moderation** | DetectModerationLabels | SafeSearch Detection | Content Moderator |
| **Custom Models** | Custom Labels | AutoML Vision, Agent Platform | Custom Vision |
| **Image Labeling** | Ground Truth | Data Labeling Service | Azure ML Data Labeling |
| **Video Analysis** | Rekognition Video | Video Intelligence API | Video Indexer |
| **Video Content Moderation** | Yes | Yes | Yes |
| **Streaming Video** | Kinesis Video Streams + Rekognition | N/A | Azure Media Services |
| **Landmark Detection** | Yes | Yes | Yes |
| **Logo Detection** | Yes | Yes | Yes |
| **Explicit Content** | Yes | Yes | Yes |
| **Pricing Model** | Per image/video minute | Per image, video unit | Per transaction |

**Documentation:**
- **[📖 AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/)** - Image and video analysis
- **[📖 AWS Textract Documentation](https://docs.aws.amazon.com/textract/)** - Document text extraction
- **[📖 GCP Vision AI Documentation](https://cloud.google.com/vision/docs)** - Image analysis
- **[📖 GCP Video Intelligence Documentation](https://cloud.google.com/video-intelligence/docs)** - Video analysis
- **[📖 Azure Computer Vision Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/)** - Image analysis
- **[📖 Azure Face API Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/face/)** - Face detection and recognition
- **[📖 Azure Custom Vision Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/)** - Custom models

---

## Natural Language Processing (NLP) & Text Analytics

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Service Name** | Comprehend | Natural Language AI | Text Analytics, Language Service |
| **Sentiment Analysis** | DetectSentiment | analyzeSentiment | Sentiment Analysis |
| **Entity Recognition** | DetectEntities | analyzeEntities | Named Entity Recognition (NER) |
| **Key Phrase Extraction** | DetectKeyPhrases | N/A | Key Phrase Extraction |
| **Language Detection** | DetectDominantLanguage | N/A | Language Detection |
| **Syntax Analysis** | DetectSyntax | analyzeSyntax | N/A |
| **Custom Classification** | Custom Classification | AutoML Natural Language | Custom Text Classification |
| **Custom Entity Recognition** | Custom Entity Recognition | AutoML Entity Extraction | Custom NER |
| **PII Detection** | DetectPiiEntities | DLP API (separate) | PII Detection |
| **Medical NLP** | Comprehend Medical | Healthcare Natural Language API | Text Analytics for Health |
| **Document Classification** | Yes | Yes | Yes |
| **Topic Modeling** | Topic modeling | N/A | N/A |
| **Languages Supported** | 100+ | 100+ | 100+ |

**Documentation:**
- **[📖 AWS Comprehend Documentation](https://docs.aws.amazon.com/comprehend/)** - NLP service
- **[📖 AWS Comprehend Medical Documentation](https://docs.aws.amazon.com/comprehend-medical/)** - Healthcare NLP
- **[📖 GCP Natural Language AI Documentation](https://cloud.google.com/natural-language/docs)** - Text analysis
- **[📖 Azure Text Analytics Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/)** - Language understanding

---

## Speech Services

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Speech-to-Text** | Transcribe | Speech-to-Text | Speech to Text |
| **Text-to-Speech** | Polly | Text-to-Speech | Text to Speech |
| **Real-time Transcription** | Yes (streaming) | Yes (streaming) | Yes (streaming) |
| **Batch Transcription** | Yes | Yes | Yes |
| **Custom Vocabulary** | Yes | Yes | Yes |
| **Speaker Diarization** | Yes | Yes | Yes |
| **Custom Voice** | Polly Brand Voice | Custom voices | Custom Neural Voice |
| **Neural Voices** | Neural TTS | WaveNet, Neural2 | Neural TTS |
| **SSML Support** | Yes | Yes | Yes |
| **Languages** | 30+ | 125+ | 100+ |
| **Medical Transcription** | Transcribe Medical | Healthcare Speech-to-Text | N/A |
| **Call Analytics** | Transcribe Call Analytics | N/A | N/A |
| **Voice Cloning** | N/A | N/A | Custom Neural Voice |
| **Pronunciation Assessment** | N/A | N/A | Pronunciation Assessment |

**Documentation:**
- **[📖 AWS Transcribe Documentation](https://docs.aws.amazon.com/transcribe/)** - Speech-to-text
- **[📖 AWS Polly Documentation](https://docs.aws.amazon.com/polly/)** - Text-to-speech
- **[📖 GCP Speech-to-Text Documentation](https://cloud.google.com/speech-to-text/docs)** - Speech recognition
- **[📖 GCP Text-to-Speech Documentation](https://cloud.google.com/text-to-speech/docs)** - Voice synthesis
- **[📖 Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/)** - Unified speech service

---

## Translation Services

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Service Name** | Translate | Cloud Translation API | Translator |
| **Text Translation** | Yes | Yes | Yes |
| **Real-time Translation** | Yes | Yes | Yes |
| **Batch Translation** | Yes | Yes | Yes (Document Translation) |
| **Custom Translation** | Custom Terminology | AutoML Translation | Custom Translator |
| **Document Translation** | Yes | Yes | Yes |
| **Language Detection** | Yes | Yes | Yes |
| **Languages Supported** | 75+ | 100+ | 100+ |
| **Formality Control** | Yes | N/A | N/A |
| **Profanity Masking** | Yes | N/A | Yes |
| **Pricing Model** | Per character | Per character | Per character |

**Documentation:**
- **[📖 AWS Translate Documentation](https://docs.aws.amazon.com/translate/)** - Neural machine translation
- **[📖 GCP Translation API Documentation](https://cloud.google.com/translate/docs)** - Text translation
- **[📖 Azure Translator Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/)** - Translation service

---

## Generative AI & Large Language Models

> **Refreshed 2026-10-21** from each vendor's documentation (sources below). Catalogs change monthly: new models arrive, old ones are retired, and the same model can have different regional availability per cloud. Confirm in the console before you design around a model. Google renamed Vertex AI to **Gemini Enterprise Agent Platform** on 2026-04-22, and Microsoft's Azure AI Foundry is now **Microsoft Foundry**, with Azure OpenAI delivered inside it. The [AI labs landscape explainer](../../explainers/ecosystem/labs-landscape.md) tracks who ships what.

| Feature | AWS | Google Cloud | Azure |
|---------|-----|-----|-------|
| **Service name** | Amazon Bedrock | Gemini Enterprise Agent Platform (formerly Vertex AI); Model Garden | Microsoft Foundry (formerly Azure AI Foundry); Azure OpenAI in Foundry |
| **Model catalog (examples)** | Amazon Nova and Nova 2; Anthropic Claude; Meta Llama 4 and 3.x; Mistral; Cohere; AI21 Jamba; DeepSeek; Qwen3; Moonshot Kimi; MiniMax; Z.AI GLM; NVIDIA Nemotron; Writer Palmyra; xAI Grok; Google Gemma; OpenAI GPT and gpt-oss | Gemini (4 Argon, 3.x Pro/Flash/Flash-Lite, 2.5); Gemma; partner models: Claude, Llama 4, Mistral, DeepSeek, Qwen3, gpt-oss, Kimi, GLM, MiniMax, Grok | Azure OpenAI (GPT-6, GPT-5.x families, gpt-oss); DeepSeek; Llama 4 and 3.3; Microsoft MAI models; Mistral; Kimi; Grok; Cohere; Black Forest Labs; Claude as a partner model; "more than 10,000 models" in the wider catalog |
| **OpenAI models** | Yes (GPT-6 and GPT-5.x families, gpt-oss) | Open-weight gpt-oss only | Yes (the broadest set, sold directly by Azure) |
| **Anthropic Claude** | Yes (Claude 5.x and 4.x families) | Yes (Model Garden partner models) | Yes (partner model via Azure Marketplace) |
| **Google models** | Gemma (open weights) only | Gemini and Gemma | No Gemini |
| **Own first-party models** | Amazon Nova, Titan embeddings | Gemini, Gemma, Nano Banana image models, Veo, Lyria | Microsoft MAI models, Phi |
| **Image / video generation** | Nova Canvas, Nova Reel, Stability AI, Luma Ray2 | Nano Banana image models, Veo 3.1 | OpenAI image models, MAI-Image, Black Forest Labs |
| **Coding assistant** | Kiro (successor to Amazon Q Developer, itself the successor to CodeWhisperer; Q Developer IDE plugins end support 2027-04-30) | Gemini Code Assist (Standard and Enterprise) | GitHub Copilot |
| **Embeddings** | Titan, Nova Multimodal Embeddings, Cohere Embed v4 | Embedding models in Model Garden (check catalog) | Embedding models in the Foundry catalog, including Cohere |
| **Safety filters** | Bedrock Guardrails | Built-in model safety filters (see each model's docs) | Azure AI Content Safety (Foundry model filters) |
| **RAG / grounding** | Bedrock Knowledge Bases (managed knowledge base GA under AgentCore) | RAG Engine, Agent Search (formerly Vertex AI Search), Grounding with Google Search | Azure AI Search (agentic retrieval, Foundry IQ) |
| **Agents** | Bedrock Agents; Bedrock AgentCore (Runtime, Memory, Gateway for MCP, Identity, Code Interpreter, Browser, Observability; works with LangGraph, CrewAI, Strands, ADK, OpenAI Agents SDK) | Agent Development Kit (ADK), Agent Runtime (formerly Agent Engine), Agent Studio, Agent Garden, Memory Bank, A2A | Foundry Agent Service (prompt, voice and hosted agents; Microsoft Agent Framework, LangGraph, Semantic Kernel) |
| **Pricing model** | Per token, on-demand or provisioned; cross-region and in-region rates differ | Per token (Standard, Priority, Batch); global and regional endpoints differ | Per token; Global, Data Zone and regional deployments differ |

**What actually differs now.** In 2023 the choice was simple: Claude on AWS, PaLM and Gemini on Google, GPT on Azure. By 2026 the catalogs overlap heavily: Claude is on all three, OpenAI models are on AWS and Azure, and most popular open-weight families are everywhere. The deciding factors are usually where your data and identity already live, which **first-party** models you want (Gemini only on Google, Nova only on AWS, the full OpenAI range plus MAI on Azure), regional availability and data residency, and the agent platform you prefer. See [GenAI platforms compared](genai-platforms.md) and [Which model for which job](../decisions/which-model-for-which-job.md).

**Documentation:**
- **[📖 Amazon Bedrock models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)** - current catalog
- **[📖 Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)** - agent platform
- **[📖 Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use.html)** - safety filters
- **[📖 Amazon Q Developer IDE end of support / Kiro](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html)** - coding assistant
- **[📖 Introducing Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)** - the 2026-04-22 rename
- **[📖 Vertex AI name changes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)** - old name to new name map
- **[📖 Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)** and **[📖 agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)**
- **[📖 What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)** - naming history and Agent Service
- **[📖 Models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure)** - Azure OpenAI and other direct models
- **[📖 Claude in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude)**

---

## Conversational AI & Chatbots

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Service Name** | Amazon Lex | Dialogflow CX, Dialogflow ES | Azure Bot Service, Language Understanding (LUIS) |
| **Intent Recognition** | Yes | Yes | Yes |
| **Entity Extraction** | Yes | Yes | Yes |
| **Multi-turn Conversations** | Yes | Yes | Yes |
| **Voice Integration** | Connect, Polly, Transcribe | Speech APIs | Speech Service |
| **Channels** | Web, mobile, SMS, Slack, Facebook | Web, mobile, telephony, integrations | Teams, Slack, Facebook, web |
| **Analytics** | CloudWatch, Conversation logs | Analytics, Insights | Application Insights, Bot Analytics |
| **Sentiment Analysis** | Integration with Comprehend | Built-in | Built-in |
| **Pre-built Agents** | Bot templates | Pre-built agents | Bot templates |
| **Pricing** | Per request | Per session | Per message |

**Documentation:**
- **[📖 AWS Lex Documentation](https://docs.aws.amazon.com/lex/)** - Conversational interfaces
- **[📖 GCP Dialogflow CX Documentation](https://cloud.google.com/dialogflow/cx/docs)** - Advanced conversational AI
- **[📖 GCP Dialogflow ES Documentation](https://cloud.google.com/dialogflow/es/docs)** - Standard edition
- **[📖 Azure Bot Service Documentation](https://learn.microsoft.com/en-us/azure/bot-service/)** - Bot framework

---

## Document Intelligence & Forms Processing

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Document OCR** | Textract | Document AI | Form Recognizer, Document Intelligence |
| **Form Extraction** | Textract (Forms) | Document AI (Forms Parser) | Form Recognizer |
| **Table Extraction** | Textract (Tables) | Document AI (Tables) | Form Recognizer (Tables) |
| **Invoice Processing** | Textract (Invoices) | Document AI (Invoice Parser) | Form Recognizer (Invoices) |
| **Receipt Processing** | Textract (Receipts) | Document AI (Receipt Parser) | Form Recognizer (Receipts) |
| **ID Document Processing** | Textract (ID Documents) | Document AI (ID Parser) | Form Recognizer (ID Documents) |
| **Custom Document Processing** | Custom Textract | Custom Document AI | Custom Form Recognizer |
| **Handwriting Recognition** | Yes | Yes | Yes |
| **Signature Detection** | Yes | Yes | Yes |
| **Layout Analysis** | Yes | Yes | Yes |
| **Queries** | Textract Queries | N/A | N/A |

**Documentation:**
- **[📖 AWS Textract Documentation](https://docs.aws.amazon.com/textract/)** - Document text extraction
- **[📖 GCP Document AI Documentation](https://cloud.google.com/document-ai/docs)** - Document understanding
- **[📖 Azure Form Recognizer Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/form-recognizer/)** - Form processing

---

## Search & Recommendations

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Personalization** | Amazon Personalize | Recommendations AI | Azure Personalizer |
| **Search** | OpenSearch, Kendra | Agent Search, Enterprise Search | Cognitive Search |
| **Recommendation Types** | User personalization, ranking, similar items | Product recommendations, personalized ranking | Contextual bandit, reinforcement learning |
| **Neural Search** | Kendra | Agent Search | Cognitive Search (vector search) |
| **Document Search** | Kendra | Agent Search | Cognitive Search |
| **E-commerce** | Personalize | Recommendations AI (Retail) | Personalizer |
| **Real-time** | Yes | Yes | Yes |
| **Cold Start** | Yes | Yes | Yes |

**Documentation:**
- **[📖 AWS Personalize Documentation](https://docs.aws.amazon.com/personalize/)** - ML-powered recommendations
- **[📖 AWS Kendra Documentation](https://docs.aws.amazon.com/kendra/)** - Intelligent search
- **[📖 GCP Recommendations AI Documentation](https://cloud.google.com/recommendations)** - Product recommendations
- **[📖 Azure Personalizer Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/personalizer/)** - Reinforcement learning

---

## MLOps & Model Management

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Pipeline Orchestration** | SageMaker Pipelines, Step Functions | Agent Platform Pipelines, Cloud Composer | Azure ML Pipelines |
| **Experiment Tracking** | SageMaker Experiments | Experiments on Agent Platform | Azure ML Experiments, MLflow |
| **Model Registry** | SageMaker Model Registry | Agent Platform Model Registry | Azure ML Model Registry |
| **Model Versioning** | Yes | Yes | Yes |
| **Model Lineage** | SageMaker Lineage | Vertex AI Metadata | Azure ML lineage tracking |
| **CI/CD Integration** | CodePipeline, GitLab, GitHub Actions | Cloud Build, GitLab, GitHub Actions | Azure DevOps, GitHub Actions |
| **Model Monitoring** | Model Monitor | Model Monitoring on Agent Platform | Model monitoring, data drift |
| **Data Drift Detection** | Yes | Yes | Yes |
| **Model Performance** | Yes | Yes | Yes |
| **A/B Testing** | Multi-model endpoints | Traffic splitting | Blue-green deployments |
| **Shadow Deployments** | Yes | Yes | Yes |
| **Model Explainability** | Clarify | Explainable AI | InterpretML, responsible AI dashboard |
| **Bias Detection** | Clarify | What-If Tool | Fairlearn integration |
| **Infrastructure as Code** | CloudFormation, CDK, Terraform | Terraform, Deployment Manager | ARM templates, Bicep, Terraform |

**Documentation:**
- **[📖 SageMaker Pipelines Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)** - ML workflows
- **[📖 SageMaker Model Monitor Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)** - Production monitoring
- **[📖 Agent Platform Pipelines Documentation](https://cloud.google.com/vertex-ai/docs/pipelines)** - Pipeline orchestration
- **[📖 Azure ML Pipelines Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)** - Workflow automation

---

## Training Infrastructure & Compute

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **GPU Instances** | P4, P5 (NVIDIA A100, H100) | A2, A3 (NVIDIA A100, H100) | NC, ND, NV series |
| **TPU Support** | No | Yes (TPU v4, v5) | No |
| **Distributed Training** | SageMaker distributed training | Multi-node, multi-GPU | Distributed training libraries |
| **Spot/Preemptible Training** | Managed Spot Training | Spot VMs | Low-priority VMs |
| **Training Cost Savings** | Up to 90% with Spot | Up to 91% with Spot | Up to 80% with Low-priority |
| **Auto-scaling** | Yes | Yes | Yes |
| **Notebook Instances** | SageMaker Notebooks | Agent Platform Workbench | Compute Instances |
| **Managed Jupyter** | Yes | Yes | Yes |
| **Data Parallelism** | Yes | Yes | Yes |
| **Model Parallelism** | Yes (SMP library) | Yes | Yes (DeepSpeed) |

**Documentation:**
- **[📖 SageMaker Training Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)** - Model training
- **[📖 Agent Platform Managed Training Documentation](https://cloud.google.com/vertex-ai/docs/training/overview)** - Custom training
- **[📖 Azure ML Training Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model)** - Training overview

---

## Data Preparation & Feature Engineering

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Data Wrangler** | SageMaker Data Wrangler | Agent Platform Feature Store | Azure ML Data Prep |
| **Feature Store** | SageMaker Feature Store | Agent Platform Feature Store | Azure ML Feature Store (preview) |
| **Data Labeling** | Ground Truth | Data Labeling Service | Data Labeling |
| **AutoML Data Prep** | Autopilot | Agent Platform AutoML | Automated ML |
| **ETL Integration** | Glue, EMR | Dataflow, Dataprep | Data Factory, Synapse |
| **Feature Reuse** | Yes | Yes | Yes |
| **Online/Offline Store** | Yes | Yes | Yes |
| **Point-in-time Joins** | Yes | Yes | Yes |

**Documentation:**
- **[📖 SageMaker Data Wrangler Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)** - Data preparation
- **[📖 SageMaker Feature Store Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)** - Feature management
- **[📖 Agent Platform Feature Store Documentation](https://cloud.google.com/vertex-ai/docs/featurestore)** - Feature serving
- **[📖 Azure ML Feature Store Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-what-is-managed-feature-store)** - Feature engineering

---

## Edge & IoT ML

| Feature | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **Edge Deployment** | SageMaker Edge Manager | Edge TPU, TensorFlow Lite | Azure IoT Edge |
| **Model Optimization** | SageMaker Neo | Model Optimization Toolkit | ONNX Runtime |
| **Supported Devices** | ARM, x86, NVIDIA, IoT devices | Coral devices, mobile, edge | Raspberry Pi, NVIDIA, Intel |
| **On-device Training** | Limited | Yes | Limited |
| **Model Compression** | Neo compiler | TensorFlow Lite | ONNX optimization |
| **OTA Updates** | Yes | Yes | Yes |
| **Monitoring** | Edge Manager | Cloud IoT Core | IoT Hub |

**Documentation:**
- **[📖 SageMaker Edge Manager Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html)** - Edge deployment
- **[📖 SageMaker Neo Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)** - Model optimization
- **[📖 Edge TPU Documentation](https://cloud.google.com/edge-tpu/docs)** - Edge AI accelerator
- **[📖 Azure IoT Edge ML Documentation](https://learn.microsoft.com/en-us/azure/iot-edge/)** - Edge computing

---

## Specialized AI Services

### AWS-Specific Services

| Service | Description |
|---------|-------------|
| **Amazon CodeGuru** | ML-powered code reviews and performance recommendations |
| **Amazon DevOps Guru** | ML-powered operational insights |
| **Amazon Fraud Detector** | Fraud detection service |
| **Amazon Forecast** | Time-series forecasting |
| **Amazon Lookout for Vision** | Anomaly detection in images |
| **Amazon Lookout for Metrics** | Anomaly detection in metrics |
| **Amazon Lookout for Equipment** | Predictive maintenance |
| **Amazon HealthLake** | Healthcare data storage and ML |
| **Amazon Monitron** | Equipment monitoring |

### GCP-Specific Services

| Service | Description |
|---------|-------------|
| **Contact Center AI** | Call center automation |
| **Discovery AI** | Data cataloging and discovery |
| **Anti-Money Laundering AI** | Financial crime detection |
| **Lending DocAI** | Loan document processing |
| **Procurement DocAI** | Purchase order processing |
| **Cloud Talent Solution** | Job search and matching |

### Azure-Specific Services

| Service | Description |
|---------|-------------|
| **Azure Metrics Advisor** | Anomaly detection in metrics |
| **Azure Video Analyzer** | Video analytics |
| **Azure Immersive Reader** | Reading assistance AI |
| **Azure Content Safety** | Content moderation |
| **Azure Applied AI Services** | Industry-specific AI solutions |

---

## Pricing Comparison (Approximate)

### ML Training (1 hour on GPU)

| Provider | Instance Type | GPUs | Cost per Hour |
|----------|--------------|------|---------------|
| **AWS** | ml.p3.2xlarge | 1x V100 | $3.06 |
| **AWS** | ml.p4d.24xlarge | 8x A100 | $32.77 |
| **GCP** | n1-standard-8 + 1 V100 | 1x V100 | $2.48 |
| **GCP** | a2-highgpu-8g | 8x A100 | $24.96 |
| **Azure** | NC6s v3 | 1x V100 | $3.06 |
| **Azure** | ND96asr v4 | 8x A100 | $27.20 |

### Inference/Prediction

| Service | Pricing Model | Cost |
|---------|--------------|------|
| **SageMaker Real-time** | Per instance hour | $0.065/hour (ml.t3.medium) |
| **SageMaker Serverless** | Per compute + invocations | $0.20/hour compute + $0.20/1K requests |
| **Agent Platform Inference** | Per hour | $0.056/hour (n1-standard-2) |
| **Azure ML Online Endpoint** | Per hour | $0.073/hour (Standard_DS2_v2) |

### AutoML Training

| Service | Pricing Model | Approximate Cost |
|---------|--------------|------------------|
| **SageMaker Autopilot** | Per instance hour | ~$0.24/hour (ml.m5.xlarge) |
| **Agent Platform AutoML** | Per node hour | $19.32/hour (tabular) |
| **Azure AutoML** | Per compute hour | ~$0.20/hour (compute) |

### AI Services (Pay-per-use)

| Service Type | AWS | GCP | Azure |
|-------------|-----|-----|-------|
| **Image Analysis** | $0.001/image (Rekognition) | $1.50/1K images (Vision) | $1.00/1K images (Computer Vision) |
| **Text Analysis** | $0.0001/100 chars (Comprehend) | $1.00/1K records (NL) | $2.00/1K records (Text Analytics) |
| **Speech-to-Text** | $0.024/min (Transcribe) | $0.024/min | $1.00/hour |
| **Text-to-Speech** | $4.00/1M chars (Polly) | $4.00/1M chars | $4.00/1M chars |
| **Translation** | $15.00/1M chars | $20.00/1M chars | $10.00/1M chars |

### Generative AI (per 1M tokens, as of 2026-10-21)

Standard on-demand prices, US regions, short prompts. AWS figures are from the AWS Price List API for us-east-1 (Global cross-region inference where listed, which is about 10% below in-region); Google figures from the Agent Platform pricing page (Global endpoint, prompts up to 200K tokens); Azure figures from the Azure Retail Prices API (East US 2, Global Standard). The pricing pages render with JavaScript, so check them before you budget.

| Provider | Model | Input | Output |
|----------|-------|-------|--------|
| **AWS Bedrock** | Claude Sonnet 5.5 (global) | $2.00 | $10.00 |
| **AWS Bedrock** | Claude Haiku 5.5 (global) | $0.10 | $0.50 |
| **AWS Bedrock** | Amazon Nova 2 Lite (global) | $0.30 | $2.50 |
| **AWS Bedrock** | Llama 4 Maverick 17B | $0.24 | $0.97 |
| **AWS Bedrock** | gpt-oss-120b | $0.15 | $0.60 |
| **Google Agent Platform** | Gemini 3.1 Pro (preview) | $2.00 | $12.00 |
| **Google Agent Platform** | Gemini 3.5 Flash-Lite | $0.30 | $2.50 |
| **Google Agent Platform** | Claude Sonnet 5.5 | $2.00 | $10.00 |
| **Google Agent Platform** | gpt-oss-120b | $0.09 | $0.36 |
| **Azure (Foundry)** | GPT-5.6 Sol | $4.00 | $20.00 |
| **Azure (Foundry)** | GPT-5.6 Luna | $0.20 | $1.20 |
| **Azure (Foundry)** | gpt-oss-120b | $0.15 | $0.60 |

Promotional prices are excluded (Gemini 4 Argon and Gemini 3.8 Flash are at introductory prices until 2026-11-30 and 2026-12-31 respectively). Batch processing is typically half price on all three. Turning these into a monthly bill: [AI cost basics](../../learn/concepts/ai-cost-basics.md).

*Note: Prices vary by region and are subject to change. Always use official pricing calculators.*

**Pricing Calculators:**
- **[📖 AWS Pricing Calculator](https://calculator.aws/)** - AWS cost estimates
- **[📖 GCP Pricing Calculator](https://cloud.google.com/products/calculator)** - GCP cost estimates
- **[📖 Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)** - Azure cost estimates

---

## CLI/SDK Command Comparison

### Train a Model

**AWS SageMaker (Python SDK):**
```python
from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri='683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:latest',
    role='arn:aws:iam::123456789012:role/SageMakerRole',
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path='s3://bucket/output'
)

estimator.fit({'train': 's3://bucket/train'})
```

**GCP Agent Platform (Python SDK):**
```python
from google.cloud import aiplatform

aiplatform.init(project='my-project', location='us-central1')

job = aiplatform.CustomTrainingJob(
    display_name='training-job',
    container_uri='gcr.io/my-project/training-image',
    model_serving_container_image_uri='gcr.io/my-project/serving-image'
)

model = job.run(
    dataset=dataset,
    model_display_name='my-model',
    machine_type='n1-standard-4',
)
```

**Azure ML (Python SDK):**
```python
from azure.ai.ml import command

job = command(
    code='./src',
    command='python train.py',
    environment='AzureML-sklearn-0.24:1',
    compute='cpu-cluster',
    experiment_name='training-experiment'
)

ml_client.jobs.create_or_update(job)
```

### Deploy a Model

**AWS SageMaker:**
```python
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.xlarge',
    endpoint_name='my-endpoint'
)

# Make predictions
result = predictor.predict(data)
```

**GCP Agent Platform:**
```python
endpoint = model.deploy(
    machine_type='n1-standard-4',
    min_replica_count=1,
    max_replica_count=10
)

# Make predictions
prediction = endpoint.predict(instances=[data])
```

**Azure ML:**
```python
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment

endpoint = ManagedOnlineEndpoint(name='my-endpoint')
ml_client.online_endpoints.begin_create_or_update(endpoint)

deployment = ManagedOnlineDeployment(
    name='blue',
    endpoint_name='my-endpoint',
    model=model,
    instance_type='Standard_DS2_v2',
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(deployment)
```

### Image Analysis

**AWS Rekognition (CLI):**
```bash
aws rekognition detect-labels \
  --image '{"S3Object":{"Bucket":"my-bucket","Name":"image.jpg"}}' \
  --max-labels 10 \
  --min-confidence 75
```

**GCP Vision AI (gcloud):**
```bash
gcloud ml vision detect-labels gs://my-bucket/image.jpg
```

**Azure Computer Vision (CLI):**
```bash
az cognitiveservices account vision analyze \
  --resource-group myResourceGroup \
  --name myComputerVision \
  --image-url https://example.com/image.jpg \
  --visual-features Categories,Description,Tags
```

### Text Analysis

**AWS Comprehend:**
```bash
aws comprehend detect-sentiment \
  --text "I love this product!" \
  --language-code en
```

**GCP Natural Language:**
```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://language.googleapis.com/v1/documents:analyzeSentiment" \
  -d '{
    "document": {
      "type": "PLAIN_TEXT",
      "content": "I love this product!"
    }
  }'
```

**Azure Text Analytics:**
```bash
az cognitiveservices account text-analytics sentiment \
  --resource-group myResourceGroup \
  --name myTextAnalytics \
  --documents "I love this product!"
```

### Speech-to-Text

**AWS Transcribe:**
```python
import boto3

transcribe = boto3.client('transcribe')

transcribe.start_transcription_job(
    TranscriptionJobName='my-job',
    Media={'MediaFileUri': 's3://bucket/audio.mp3'},
    MediaFormat='mp3',
    LanguageCode='en-US'
)
```

**GCP Speech-to-Text:**
```python
from google.cloud import speech

client = speech.SpeechClient()

audio = speech.RecognitionAudio(uri='gs://bucket/audio.mp3')
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    language_code='en-US'
)

response = client.recognize(config=config, audio=audio)
```

**Azure Speech:**
```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription='your-key',
    region='eastus'
)

audio_config = speechsdk.audio.AudioConfig(filename='audio.wav')
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = speech_recognizer.recognize_once()
```

### Generative AI (LLM)

Model IDs change often and differ per cloud, so the samples use placeholders: copy the exact ID from each catalog page above.

**Amazon Bedrock (Converse API, works the same across model providers):**
```python
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

response = bedrock.converse(
    modelId="<model-id-or-inference-profile-from-the-Bedrock-catalog>",
    messages=[{"role": "user", "content": [{"text": "Explain quantum computing"}]}],
    inferenceConfig={"maxTokens": 1000},
)
print(response["output"]["message"]["content"][0]["text"])
```

**Google Gemini Enterprise Agent Platform (Google Gen AI SDK):**
```python
from google import genai

client = genai.Client(vertexai=True, project="your-project", location="global")
response = client.models.generate_content(
    model="<gemini-model-id-from-Model-Garden>",
    contents="Explain quantum computing",
)
print(response.text)
```

**Azure OpenAI in Microsoft Foundry (OpenAI SDK against the v1 endpoint):**
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://your-resource.openai.azure.com/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
response = client.chat.completions.create(
    model="<your-deployment-name>",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
)
print(response.choices[0].message.content)
```

---

## Decision Tree: Which AI/ML Service?

### ML Platform Selection

**Use AWS SageMaker if:**
- ✅ Already heavily invested in AWS ecosystem
- ✅ Need comprehensive end-to-end ML platform
- ✅ Want strong enterprise features and governance
- ✅ Need specialized services (Forecast, Fraud Detector)
- ✅ Require extensive built-in algorithms

**Use GCP Agent Platform if:**
- ✅ Want Google's Gemini models alongside the ML platform
- ✅ Need TPU support for training
- ✅ Prefer integrated BigQuery and GCP data services
- ✅ Want simplified unified ML platform
- ✅ Need strong AutoML capabilities

**Use Azure ML if:**
- ✅ Microsoft/Azure enterprise integration
- ✅ Need strong MLOps and DevOps integration
- ✅ Want ONNX model format support
- ✅ Require hybrid cloud ML (Azure Arc)
- ✅ Need integration with Microsoft tools (VS Code, Power BI)

### Generative AI Platform Selection

**Use AWS Bedrock if:**
- ✅ Want Amazon Nova or the widest third-party catalog (Claude, OpenAI, Llama, Mistral, DeepSeek, Qwen and more)
- ✅ Need multiple foundation model options
- ✅ Prefer serverless, pay-per-use pricing
- ✅ Want managed RAG with Knowledge Bases
- ✅ Need AI agents (AgentCore) and Bedrock Guardrails

**Use GCP Agent Platform if:**
- ✅ Want Google's Gemini models
- ✅ Need multimodal AI capabilities
- ✅ Prefer Google's AI research advantages
- ✅ Want integrated search and grounding
- ✅ Need tighter BigQuery integration

**Use Microsoft Foundry (Azure OpenAI) if:**
- ✅ Want the full range of OpenAI models sold directly by Azure
- ✅ Require enterprise-grade OpenAI with SLAs
- ✅ Want Azure enterprise security and compliance
- ✅ Need integration with Microsoft ecosystem
- ✅ Require content filtering and responsible AI

### Computer Vision

**Use AWS Rekognition if:**
- ✅ Need celebrity recognition
- ✅ Want facial recognition for security
- ✅ Need video analysis with Kinesis integration
- ✅ Require PPE detection

**Use GCP Vision AI if:**
- ✅ Need best OCR accuracy
- ✅ Want product search in images
- ✅ Need handwriting recognition
- ✅ Require AutoML Vision for custom models

**Use Azure Computer Vision if:**
- ✅ Need spatial analysis
- ✅ Want Read API for document OCR
- ✅ Need Custom Vision for quick custom models
- ✅ Require face verification/identification

### NLP Selection

**Use AWS Comprehend if:**
- ✅ Need PII detection and redaction
- ✅ Want topic modeling
- ✅ Need custom classification
- ✅ Require medical text analysis

**Use GCP Natural Language if:**
- ✅ Need syntax analysis
- ✅ Want content classification
- ✅ Need AutoML for custom models
- ✅ Require healthcare NLP

**Use Azure Text Analytics if:**
- ✅ Need key phrase extraction
- ✅ Want opinion mining
- ✅ Need healthcare-specific text analysis
- ✅ Require conversational language understanding

### Training Infrastructure

**Use SageMaker if:**
- ✅ Need managed Spot training
- ✅ Want comprehensive built-in algorithms
- ✅ Need distributed training library (SMP)
- ✅ Require inference optimization (Neo)

**Use Agent Platform if:**
- ✅ Need TPU support
- ✅ Want best TensorFlow integration
- ✅ Need hyperparameter tuning (Vizier)
- ✅ Require custom containers

**Use Azure ML if:**
- ✅ Need ONNX model support
- ✅ Want automated ML
- ✅ Need designer (no-code training)
- ✅ Require parallel training across regions

---

## Key Takeaways

### AWS AI/ML Strengths
- ✅ Most comprehensive AI/ML service portfolio
- ✅ Strong foundation model selection (Bedrock)
- ✅ Excellent specialized services (Forecast, Fraud Detector, Personalize)
- ✅ Mature MLOps capabilities
- ✅ Best integration with AWS ecosystem
- ✅ Strong document intelligence (Textract)

### GCP AI/ML Strengths
- ✅ Gemini models, available only on Google Cloud
- ✅ TPU support for high-performance training
- ✅ Superior AutoML capabilities
- ✅ Unified Gemini Enterprise Agent Platform
- ✅ Best BigQuery ML integration
- ✅ Strong document AI capabilities
- ✅ Advanced explainable AI

### Azure AI/ML Strengths
- ✅ Broadest OpenAI model range, sold directly by Azure (OpenAI models are no longer Azure-exclusive)
- ✅ Best Microsoft ecosystem integration
- ✅ Strong MLOps and DevOps integration
- ✅ Comprehensive cognitive services
- ✅ Hybrid cloud ML (Azure Arc)
- ✅ ONNX model format support
- ✅ Strong responsible AI tooling

---

## Best Practices Across All Platforms

### Model Development
1. Start with AutoML for baseline
2. Use managed notebooks for experimentation
3. Implement experiment tracking from day one
4. Version your datasets and models
5. Use feature stores for reusable features

### Training
1. Start small, scale up gradually
2. Use spot/preemptible instances for cost savings
3. Implement distributed training for large models
4. Monitor training metrics in real-time
5. Use hyperparameter tuning

### Deployment
1. Use model registry for versioning
2. Implement A/B testing for new models
3. Start with lower-cost instances
4. Enable auto-scaling for production
5. Use batch inference when real-time isn't needed

### Monitoring
1. Implement data drift detection
2. Monitor model performance continuously
3. Set up alerts for anomalies
4. Track prediction latency and costs
5. Regularly retrain models

### Security
1. Use IAM roles/service accounts (never keys)
2. Encrypt data at rest and in transit
3. Implement content filtering for generative AI
4. Use private endpoints for sensitive workloads
5. Enable audit logging

### Cost Optimization
1. Use serverless inference when possible
2. Choose right-sized instances
3. Implement auto-scaling
4. Use spot instances for training
5. Clean up unused models and endpoints
6. Monitor and set budget alerts

---

## Next steps

- [Compute Service Comparison](https://cloud.noblerworks.com/resources/service-comparison-compute/)
- [Storage Service Comparison](https://cloud.noblerworks.com/resources/service-comparison-storage/)
- [Database Service Comparison](https://data.noblerworks.com/resources/service-comparison-databases/)
- [Networking Service Comparison](https://cloud.noblerworks.com/resources/service-comparison-networking/)

---

**Additional Resources:**
- **[📖 AWS AI/ML Blog](https://aws.amazon.com/blogs/machine-learning/)** - Latest ML updates
- **[📖 GCP AI Blog](https://cloud.google.com/blog/products/ai-machine-learning)** - AI announcements
- **[📖 Azure AI Blog](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/bg-p/MachineLearningBlog)** - ML insights
- **[📖 AWS ML University](https://aws.amazon.com/machine-learning/mlu/)** - Free ML courses
- **[📖 Google AI Education](https://ai.google/education/)** - Learning resources
- **[📖 Microsoft Learn AI](https://learn.microsoft.com/en-us/training/browse/?products=azure&subjects=artificial-intelligence)** - AI training paths

---

**Related Guides:**
- [GenAI Platforms Comparison](genai-platforms.md)
- [LLM Observability Comparison](llm-observability.md)
- [Vector Databases Comparison](../decisions/vector-database.md)
- [Agent Frameworks Comparison](agent-frameworks.md)
- [LLM Serving Decision Matrix](../decisions/llm-serving.md)

In the research library:

- [AI labs landscape](../../explainers/ecosystem/labs-landscape.md) - whose models each cloud hosts
- [AI hardware landscape](../../explainers/compute/ai-hardware-landscape.md) - the GPUs and custom chips behind the instance types
- [GenAI platforms compared](genai-platforms.md) - the foundation-model API layer in more depth
- [AI/ML pipeline pattern](../../build/patterns/ai-ml-pipeline.md) - putting the services together

## Sources

Generative AI section refreshed 2026-10-21 from these pages (read that day):

- Amazon Bedrock, models at a glance: https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html
- Amazon Bedrock AgentCore, overview and release notes: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html , https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html
- Amazon Q Developer IDE end of support and upgrade to Kiro: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html , https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/upgrade-to-kiro.html
- AWS Price List API, Amazon Bedrock (us-east-1): https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonBedrockFoundationModels/current/us-east-1/index.json
- Google Cloud, "Introducing Gemini Enterprise Agent Platform" (2026-04-22): https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- Google Cloud, Vertex AI name changes: https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes
- Google Cloud, Agent Platform models and agents: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models , https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents
- Google Cloud, generative AI pricing on Agent Platform: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing
- Gemini Code Assist overview: https://developers.google.com/gemini-code-assist/docs/overview
- Microsoft Learn, "What is Microsoft Foundry?": https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry
- Microsoft Learn, models sold directly by Azure: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
- Microsoft Learn, Claude in Foundry: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude
- Microsoft Learn, Azure AI Search overview: https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search
- Azure Retail Prices API: https://prices.azure.com/api/retail/prices
- Microsoft Learn, Azure OpenAI v1 API (OpenAI client with `base_url`): https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle
- AWS, Bedrock Converse API: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
- OpenAI, "Introducing gpt-oss" (August 2025): https://openai.com/index/introducing-gpt-oss/

The other sections (ML platforms, vision, speech, pricing for classic services) predate this refresh and have not been re-verified; check vendor pages before relying on them.
