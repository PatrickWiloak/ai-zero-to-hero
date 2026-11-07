---
last-updated: 2026-11-06
---

# GCP Professional Machine Learning Engineer (PMLE) - Exam Strategy

## Format reminder

- 50-60 questions, 120 minutes
- Pass mark not published by Google (commonly estimated around 70%)
- Multiple choice + multiple response

## Top traps

1. **GCP ML service ladder**: pre-trained APIs (Vision, NL, Speech, Translate, Document AI) → AutoML (your data, no code) → custom training on Agent Platform (formerly Vertex AI) → on-prem / Anthos. Climb only when needed.

2. **Agent Platform vs legacy AI Platform**: Agent Platform is the unified platform (launched as Vertex AI in 2021, renamed in 2026). AI Platform is legacy. Pick Agent Platform in modern questions.

3. **AutoML vs Custom Training on Agent Platform**: AutoML for tabular / image / text / video without writing model code. Custom for full control with TensorFlow / PyTorch / XGBoost / scikit-learn.

4. **Feature Store**: solves training-serving skew. Online store for low-latency serving (Bigtable-backed). Offline store for training (BigQuery-backed). Sync between them.

5. **Model Monitoring**: training-serving skew, prediction drift, feature attribution drift. Configure thresholds + alerts.

6. **Vizier (HPT service)**: Bayesian, Grid, Random; supports parallel trials and early stopping.

7. **Pipelines**: KFP SDK or TFX. Reproducible, parameterizable, conditional execution.

8. **TPUs vs GPUs**:
   - TPUs: best for large transformer models on TensorFlow / JAX (and now PyTorch via XLA)
   - GPUs (A100, H100, L4): general-purpose ML
   Pick TPU for large-scale training that fits the TF/JAX ecosystem.

9. **Explainability**: Agent Platform Explainable AI provides feature attribution (Sampled Shapley, Integrated Gradients, XRAI for images). For regulated workloads.

10. **Endpoints vs batch prediction**: Endpoints for sync low-latency. Batch for offline scoring at scale (Dataflow under the hood).

## High-yield topics easy to miss

- Agent Search (RAG-as-a-service)
- Agent Builder on Agent Platform (no-code agents)
- Agent Studio (foundation model playground)
- Agent Platform Workbench (managed Jupyter)
- Agent Platform Notebooks Executor (scheduled notebooks)
- Custom Container Training (BYO Docker image)
- Reduced-precision training (BF16 on TPU, FP16 on GPU)
- DataPlex for data governance + lineage

## Time management

120 / ~55 = ~2.2 min/question. Pace: half done by minute 60.

## When stuck

1. **Identify the problem type** - tabular / image / text / time series.
2. **Match to the right service** - AutoML for fast, custom for control, pre-trained for off-the-shelf.
3. **Default to managed Agent Platform services** over custom infrastructure.
4. **Eliminate "build it from scratch"** when an MLOps service exists.

## Day-of logistics

120 min, ~55 questions. Bring two IDs.

## After

**Pass:** Cert valid 2 years.

**Fail:** Re-review your weakest sections first. By weight, the largest are Scaling prototypes (~21%), Serving and scaling (~20%) and Pipelines (~18%). Do not skip Monitoring AI solutions (~13%), which now includes security and generative AI evaluation.

## PMLE patterns

- "Off-the-shelf NLP / vision / speech" = pre-trained API
- "Tabular / image classification, no code" = AutoML
- "Custom model with full control" = Agent Platform custom training
- "Training-serving skew" = Agent Platform Feature Store
- "Drift monitoring" = Model Monitoring on Agent Platform
- "HPT" = Agent Platform Vizier
- "Reproducible pipelines" = Agent Platform Pipelines (KFP)
- "Cheap large-scale training" = Spot + checkpointing + distributed
- "Per-prediction explanation" = Agent Platform Explainable AI
- "Foundation model + RAG" = Agent Search + Agent Studio
- "SQL team tunes Gemini on a BigQuery table" = BigQuery remote model with `prompt` and `label`
- "Open model, no capacity to manage" = Model as a Service in Model Garden
- "Custom weights in our own VPC" = self-deploy from Model Garden
- "Prompt injection or jailbreak" = Model Armor
- "Inputs stable, accuracy falling" = concept drift, found with delayed labels
- "Score generative output after each prompt change" = Gen AI evaluation service on a fixed dataset
