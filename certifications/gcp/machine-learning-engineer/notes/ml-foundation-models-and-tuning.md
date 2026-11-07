# ML Foundation Models and Tuning - GCP Professional Machine Learning Engineer

## Overview

The current exam guide threads foundation models through several sections instead of giving them one of their own. This note gathers them:

| Objective | What it asks |
|---|---|
| 1.1 | Fine-tuning Gemini models using BigQuery |
| 1.2 | Selecting a model from Model Garden, tuning for a use case, optimising Gemini applications for cost, latency and availability |
| 2.2 | Prototyping in notebooks with foundational and open-source models from Model Garden |
| 3.1, 3.2 | Choosing an LLM as a model type, fine-tuning foundational models and knowing when tuning should be considered |
| 4.1 | Deploying through Model Garden |

Product facts were checked against Google's documentation on 2026-11-06. Model names change quickly, so check the current lists instead of memorising versions.

## The order of decisions

Most of these questions reward picking the lightest option that meets the requirement. The ladder runs like this:

1. **A task-specific API** when the job is already a product: Document AI for forms, Vision for images, Translate for language.
2. **A foundation model with a good prompt** when the task is general and there is no labelled data.
3. **Grounding or RAG** when the model lacks your facts. This is a knowledge problem, and tuning does not reliably fix it.
4. **Tuning** when prompting has hit its limit on a behaviour you can show by example: a format, a style, a classification habit.
5. **Custom training** when you need a model no foundation model can become.

Each rung costs more to build and maintain than the one above it, so you need a reason to step down.

## Model Garden

[Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) is the library for finding, testing, customising and deploying models from Google and its partners. It connects to tuning, evaluation and serving on the platform. Google groups its contents into foundation models (pretrained and multitask), fine-tunable models (adapted with a notebook or pipeline) and task-specific solutions (mostly ready to use). Every model has a card with its details, and you can filter by task, provider, collection and feature.

### Selecting a model

Google does not publish a formula, so the exam has to test judgement. Work through the scenario's constraints in this order:

- **Task and modality:** text, code, image (Imagen), video (Veo), or several at once (Gemini).
- **Quality against cost and speed:** start with the cheapest model that passes your evaluation. Selecting by evaluation on your own data beats selecting by reputation.
- **Control and data requirements:** whether weights must be custom, or traffic must stay in your network, usually decides the serving route below.
- **Licence and governance:** Model Garden flags models for review, and administrators can [restrict access](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) to vetted models.

### Serving routes: the decision that matters

For open models, [Google describes three routes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option).

**Model as a Service (MaaS)** is a serverless managed API. There is nothing to deploy, no capacity to manage, and you pay for usage. It suits uneven traffic and quick starts, which is why the guide mentions "models as a service" for building solutions.

**Self-deployment from Model Garden** puts the model on an endpoint in your own project and VPC. You then own the capacity and pay for it whether or not it is busy. Google names the reasons to accept that: custom or fine-tuned weights, predictable high-volume traffic, and stringent security or compliance needs.

**Prebuilt serving containers** such as vLLM, Hex-LLM and TGI give you more control over the serving stack. They are the route for tuning the serving itself, and they connect to objective 4.1's custom and prebuilt containers.

Partner models can also be self-deployed after a Google Cloud Marketplace purchase. Their weights cannot be exported, and this feature was labelled Preview in one document when checked.

### Prototyping in notebooks

Objective 2.2 expects you to try these models from Workbench or Colab Enterprise. Model Garden provides tutorial notebooks for deployment, fine-tuning and evaluation, and they make a good starting point. A prototype should end with an evaluation result that justifies the choice, not just a demo that worked once.

## Tuning

### What tuning does and when to consider it

[Supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning) teaches a target behaviour from labelled input and output examples. The tuning job learns additional parameters, and the result is a new model that combines them with the original. Google recommends it for classification, sentiment analysis, entity extraction, simple summarisation and writing domain-specific queries.

Google's advice is to "start with prompting to find the optimal prompt", and to tune when "advanced prompting strategies are not sufficient, and a model tailored to your data is essential". Prompting suits limited labelled data and fast prototyping. Tuning can also pay for itself: it can improve quality and reduce latency and cost, because a tuned model needs less instruction in each prompt.

Three judgement points tend to separate the answers:

- **Tuning teaches behaviour, not facts.** If the model must answer from documents that change, use grounding or RAG. Retuning for every update is the wrong tool.
- **Quality beats quantity.** Google says high-quality labelled data matters more than volume, and advises looking at where the model makes mistakes before adding more. Typical datasets run from about a hundred examples into the thousands.
- **Measure it.** Hold out a test set, score the base model and the tuned model on it, and keep the tuned one only if it wins by enough to justify the extra upkeep.

### Fine-tuning Gemini in BigQuery

Objective 1.1 sits in the low-code section because [BigQuery lets a SQL team tune Gemini](https://docs.cloud.google.com/bigquery/docs/generate-text-tuning) without leaving SQL. If the examples are already in a table and the team works in SQL, this is usually the intended answer.

A remote model takes a tuning query. The query must return the input as `prompt` and the target as `label`:

```sql
CREATE OR REPLACE MODEL `mydataset.gemini_tuned`
  REMOTE WITH CONNECTION DEFAULT
  OPTIONS (
    endpoint = 'gemini-2.5-pro',       -- the base model; check what is tunable today
    max_iterations = 500,              -- how long tuning runs
    data_split_method = 'no_split')    -- this table is all training data
AS
SELECT input AS prompt, output AS label
FROM `mydataset.training_examples`;
```

The Gemini call does not stay inside BigQuery billing. Costs come from BigQuery queries, BigQuery ML model and processing charges, Agent Platform charges for Gemini calls and supervised tuning, and storage.

Evaluate with `ML.EVALUATE`, comparing the model with a held-out table. Run it on the base model too, or you have no way to know whether tuning helped:

```sql
SELECT *
FROM ML.EVALUATE(
  MODEL `mydataset.gemini_tuned`,
  (SELECT input AS prompt, output AS label FROM `mydataset.eval_examples`),
  STRUCT('text_generation' AS task_type));
```

The output includes `bleu4_score` and the `rouge-l` precision, recall and F1 scores. Then call the tuned model with `AI.GENERATE_TEXT`, passing a query with a `prompt` column. Older material may show `ML.GENERATE_TEXT`, but the current tutorial uses `AI.GENERATE_TEXT`.

BLEU and ROUGE measure similarity to the reference text, so they fit tasks with a clear target output. For open-ended quality, use the judge-based evaluation in [Monitoring AI Solutions](ml-monitoring-ai-solutions.md#the-gen-ai-evaluation-service).

### Tuning elsewhere

Tuning also runs through Agent Studio, the Agent Platform API and the SDK. Use these when the team and data are not in BigQuery. Fine-tunable models in Model Garden are adapted with a notebook or pipeline, and that compute bills at custom training rates. Objective 3.2 groups all of this under training because it brings the same concerns: data quality, a validation set, cost and when to stop.

## Optimising Gemini applications

Objective 1.2 asks about cost, latency and availability. Each lever trades one for another, so read which one the scenario cares about.

**Shrink the work first.** Use the smallest model that passes evaluation, shorten prompts, and cap output length. These cost nothing to adopt and help both cost and latency.

**[Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)** cuts the cost and latency of requests that repeat content. Hit rates improve when large, common content sits at the start of the prompt, which is why a long shared system prompt or document comes first and the user's question comes last.

**[Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)** is discounted against real-time calls, and it fits large, non-urgent jobs. Requests may queue when demand is high, so it is wrong for anything a user is waiting on.

**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)** reserves capacity for critical, steady, always-on work where an SLA is needed, removing the queuing that can occur on pay-as-you-go during heavy traffic. You pay for it whether you use it or not, so a common pattern is to cover baseline traffic with it and send overflow elsewhere. It does not bypass quotas on other tools such as Grounding, and batch jobs do not use it.

**Handle failure in the application.** Retries with backoff on quota errors, and a fallback model or region for critical paths, are how an application stays available when a single model is busy.

## How questions tend to read

These are this guide's reading of the objectives, not Google's wording.

- "SQL team, examples in BigQuery, tune Gemini" points to a remote model with `prompt` and `label` columns.
- "No labelled data, tight deadline" points to prompting a Gemini model, not tuning.
- "Answers must reflect our changing documents" points to grounding or RAG, not tuning.
- "Open model, spiky traffic, no ops team" points to MaaS.
- "Custom weights, own VPC, steady high volume" points to self-deployment from Model Garden.
- "Same large document on every request" points to context caching.
- "Millions of overnight summaries" points to batch inference.
- "SLA on a steady production workload" points to Provisioned Throughput.

## Sources

- [Professional ML Engineer exam guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english.pdf)
- [Overview of Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models)
- [Open models overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option)
- [Overview of self-deployed models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models)
- [Introduction to tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)
- [Tune a Gemini model in BigQuery](https://docs.cloud.google.com/bigquery/docs/generate-text-tuning)
- [Consumption options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)
