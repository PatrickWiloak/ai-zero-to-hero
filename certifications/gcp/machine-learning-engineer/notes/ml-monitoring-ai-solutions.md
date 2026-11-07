# Monitoring AI Solutions - GCP Professional Machine Learning Engineer

## Overview

This note covers **Section 6 of the exam guide, Monitoring AI solutions (~13%)**, plus the evaluation half of objective 2.3. The section has two objectives: 6.1 Identifying risks to AI solutions and 6.2 Monitoring, testing and troubleshooting AI solutions.

The title is broader than it looks. Older study material treats monitoring as drift charts on an endpoint. The current guide also puts security in this section (data exfiltration, malicious prompting, sensitive data sent to LLMs), along with bias monitoring, explainability and the evaluation of generative AI. The useful way to hold it together is one question: **what could go wrong with this model after launch, and which signal would tell me?**

Product facts here were checked against Google's documentation on 2026-11-06. The guide uses the Gemini Enterprise Agent Platform names, shortened here to "Agent Platform" (formerly Vertex AI).

## 6.1 Identifying risks

### Three ways a generative application leaks or misbehaves

The guide names three failure modes, and each has a different cause.

**Data exfiltration** is an attacker, or an unlucky prompt, getting the system to reveal something it can reach: another customer's record, the contents of a retrieved document, the system prompt. The model is rarely the real weak point. The exposure comes from what the application lets it read, so the first defence is least-privilege access to the data behind retrieval and tools. A filter on the output is the second defence.

**Malicious prompting** covers prompt injection and jailbreaks: text written to make the model ignore its instructions. Injection can also arrive indirectly, inside a web page or document that the application retrieves and passes to the model. A user who never types anything hostile can still trigger it.

**Sharing sensitive data with LLMs** is usually not an attack at all. An employee pastes a customer's card number into a support tool, and now it sits in a prompt, and perhaps in a log. The fix belongs before the model: detect and redact it on the way in.

### Choosing the security tool

The guide lists three example tools, and questions tend to turn on which layer fits the risk.

**Regex** is the cheap, deterministic layer. It is exact, fast and free of model cost, so it suits fixed formats such as an internal ticket ID or a known card pattern. It cannot catch a paraphrase, which makes it a poor answer to prompt injection, where the attacker simply rewords.

**Safety filters** are built into Gemini. [Configurable content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters) score content against harm categories (hate speech, harassment, sexually explicit, dangerous content), and you choose a blocking threshold such as `BLOCK_ONLY_HIGH` or `BLOCK_MEDIUM_AND_ABOVE`. Separate non-configurable filters always block child sexual abuse material and personally identifiable information. When output is blocked, the candidate's content is empty and a finish reason explains why, so application code has to handle an empty response rather than assume text came back. These filters judge harm in content. They are not designed around someone trying to subvert your instructions with polite, harmless-looking text.

**[Model Armor](https://docs.cloud.google.com/model-armor/overview)** is the dedicated screening service, and it is the usual answer when a scenario mentions prompt injection, jailbreaks, or the same policy across several models. It wraps the LLM rather than living inside one model, and Google says it works whether the AI runs on Google Cloud or another cloud. It screens for prompt injection and jailbreaks, sensitive data (through Sensitive Data Protection, in basic or advanced mode), malicious URLs and responsible-AI categories.

Three Model Armor details are worth knowing:

- **Templates** hold the filters and confidence levels. Google advises separate templates for prompts and responses, because the risks differ: injection and uploaded secrets on the way in, leakage and harmful content on the way out.
- **`SanitizeUserPrompt` and `SanitizeModelResponse`** are the API methods. The application calls them and decides what to do with the verdict.
- **Inspect only versus inspect and block** is the rollout path. Inspect only logs violations without stopping traffic, which lets you measure false positives before you enforce.

These layers stack. A strong design redacts sensitive data first, screens the prompt, calls the model with its own filters on, screens the response, and limits what the model can reach in the first place.

### Responsible AI and monitoring for bias

Fairness work does not end at launch. A model can pass a disaggregated review and later degrade for one group, because that group's data shifted or its traffic share changed. An overall metric hides this, since a small group can get much worse while the average barely moves.

So the monitoring design is the same as the launch review, repeated on production data: compute the metric per slice on a schedule, watch the gap between groups as well as each group's value, and alert on the gap. The metric needs ground truth, so it inherits whatever label delay the use case has. Where labels arrive late, the distribution of predictions per slice is an earlier but weaker signal. The [fact sheet](../fact-sheet.md) lists the fairness metrics and tools.

### Explainability on Agent Platform

The guide places model explainability here because explanations are a risk control as well as a development aid. They answer "why did the model decide this?" for a regulator or a customer, and they reveal a model leaning on a feature it should not use.

In practice, you configure explanations on the model, and an online request can ask for them alongside the prediction through Agent Platform Inference. Sampled Shapley suits non-differentiable models such as tree ensembles, and Integrated Gradients and XRAI suit differentiable ones, with XRAI aimed at images. The worked code is in [ML Deployment and Operations](ml-deployment-and-operations.md#agent-platform-explainable-ai).

## 6.2 Monitoring predictive models

### Four kinds of change

The guide names four issues. Keeping them apart answers most questions in this section.

| Issue | What changed | Compared with | Needs labels? |
|---|---|---|---|
| Training-serving skew | Serving inputs differ from training inputs | The training data | No |
| Data drift | Serving inputs change over time | Earlier production data | No |
| Concept drift | The link between inputs and the right answer changes | Actual outcomes | **Yes** |
| Feature attribution drift | How much each feature drives predictions changes | Training or earlier attributions | No, but needs explanations |

**Skew** often appears on day one. It usually means a pipeline bug, such as a feature computed differently in serving, rather than the world changing. The fix is often in the code: shared preprocessing, or a Feature Store. **Drift** appears gradually, and the usual response is to investigate and retrain on fresher data.

**Concept drift** is the trap, because input monitoring cannot see it. Fraudsters change tactics, and the transactions look the same while their meaning has moved. Inputs and predictions can stay perfectly stable while precision falls. The only direct evidence is ground truth, so you log predictions, join them to outcomes when they arrive, and track the real metric over time. This is what the guide means by continuous evaluation metrics. If labels take weeks, your detection also takes weeks, which is a reason to find a faster proxy label.

**Attribution drift** weights change by importance. A large distribution shift in a feature the model barely uses may not matter, while a small shift in its most influential feature may matter a lot. A change in attributions also shows that the model's reasoning moved, which raw feature distributions cannot show.

### Model Monitoring on Agent Platform

[Model Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) comes in two versions, and Google's advice on them is specific.

**v1 is generally available** and is configured on an endpoint. It supports skew detection (baseline: training data) and drift detection (baseline: past production data), and it alerts by email when a feature's distance score passes its threshold, with a default of 0.3. It can sample a fraction of requests to save cost, and a monitoring frequency sets the window it analyses. All models on one endpoint share the detection type, frequency and sampling fraction, which is a reason to think before putting several models on one endpoint. Google recommends v1 when you need production-level support on an endpoint-deployed model.

**v2 is in Preview** and ties monitoring to a model version rather than an endpoint. A *model monitor* holds the schema and default settings, and a *monitoring job* runs the check, either on demand or on a schedule. Its objectives are input feature drift, output inference drift and feature attribution (using SHAP values). Because it is tied to the model version, it can cover custom batch inference, custom online inference and even models outside the platform: you register the model in Model Registry without uploading the artifact. Google recommends v2 for use cases other than the v1 one above.

Both versions use the same distance measures: **L-infinity distance for categorical features and Jensen-Shannon divergence for numerical features**. The monitoring overview scopes the product to tabular models, and it does not say generative models are supported. Generative AI needs the evaluation approach below.

[Attribution monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/monitor-explainable-ai) has extra conditions: tabular AutoML or imported tabular custom models, for classification or regression. Skew detection on attributions also needs a training baseline, which can come from a batch explanation job over the training set.

Setting up monitoring is half the job. An alert needs a defined response: investigate, then fix the pipeline if it is skew, or retrain if it is drift. Retraining policy and its triggers are covered in [ML Deployment and Operations](ml-deployment-and-operations.md#continuous-training).

### Troubleshooting by symptom

Start with the layer that matches the symptom, and resist retraining until you know the cause.

- **Quality was poor from the first day:** suspect skew. Compare the preprocessing in training and serving.
- **Quality declined slowly and inputs moved:** data drift. Retrain on recent data and check the features that moved.
- **Quality declined and inputs look stable:** concept drift, or a change in how labels are produced. Check the labels too.
- **One group got worse and the average did not:** slice the metrics.
- **Endpoint healthy, answers wrong:** infrastructure metrics such as CPU and latency say nothing about prediction quality. You need the model-level signals above.
- **Latency or errors rose and predictions look fine:** this one is infrastructure. See autoscaling and replica settings in the serving notes.

## Monitoring, testing and evaluating generative AI

### Why it differs

A predictive model has one right answer that eventually arrives as a label. A generative model has many acceptable answers, and often no label ever arrives. Exact matching fails, so you score output against criteria instead.

There is also a change that predictive monitoring never had to face. Behaviour can move because you changed a prompt, retrieval returned different documents, or the model version changed, even when your own traffic did not. Each of those needs a re-evaluation.

### The Gen AI evaluation service

The [Gen AI evaluation service](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) supports model migrations, prompt changes and fine-tuning. Its metrics fall into three families:

- **Rubric-based metrics use an LLM to judge.** This is the "LLM-as-a-judge" the guide names in objective 2.3. Adaptive rubrics, Google's recommended option, generate pass/fail tests per prompt, a bit like unit tests. For a request for a four-sentence optimistic summary, the rubrics check the content, the sentence count and the tone, and a response passing two of three scores 66.7%. Static rubrics apply one fixed scale, such as 1 to 5, to every prompt. Ground truth is optional for judge metrics, and qualities like instruction following and writing quality can be scored this way.
- **Computation-based metrics** are deterministic formulas such as ROUGE and BLEU. They need reference answers. They are cheaper and repeatable, but they reward similar wording rather than correct meaning.
- **Custom functions** are your own Python scoring logic, through the SDK.

Two practical points follow. A judge model is itself a model, so treat its scores as a strong signal rather than proof, and spot-check them. And a fixed evaluation dataset is what makes runs comparable between versions, so keep it stable and add to it whenever production shows you a new failure.

Google's SDK guidance has changed: the GenAI Client is the recommended interface, and the older EvalTask module is kept for backward compatibility. Agent evaluation is documented separately and adds agent traces to the metrics.

### Testing before launch, watching after

Before launch, generative testing looks like a regression suite. Run the evaluation dataset on every prompt or model change and block the release if scores drop. Add adversarial cases to it: injection attempts, requests for data the application should refuse, and off-topic prompts.

After launch, Google suggests [sampling production logs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview) to build evaluation datasets, which is how you evaluate real usage rather than the cases you imagined. Log prompts and responses with care, because those logs can contain the sensitive data you are protecting. Google warns of this for Model Armor's own sanitisation logs and advises an access-controlled sink.

Alongside quality, track the operational signals: token usage and cost, latency, error and quota responses, and how often safety filters or Model Armor intervene. A rising block rate might mean an attack, or an over-strict threshold hurting real users. The cost and availability choices behind these signals are in [ML Foundation Models and Tuning](ml-foundation-models-and-tuning.md).

## How questions tend to read

These are this guide's reading of the objectives, not Google's wording.

- "Users try to make the chatbot ignore its instructions" points to Model Armor rather than a stricter content filter.
- "Customer numbers pasted into prompts" points to Sensitive Data Protection or Model Armor, redacting before the model sees them.
- "Compare serving data with training data" is skew. "Compare with last month" is drift.
- "Inputs are stable but accuracy fell" is concept drift, found with delayed labels.
- "Average accuracy is fine but one region complains" means slice the metrics.
- "Score a summariser after each prompt change" is the evaluation service on a fixed dataset.
- "Production support on an endpoint" favours Model Monitoring v1, and "model served outside the platform" favours v2.

## Sources

- [Professional ML Engineer exam guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english.pdf), Section 6 and objective 2.3
- [Introduction to Model Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview)
- [Monitor feature attribution skew and drift](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/monitor-explainable-ai)
- [Model Armor overview](https://docs.cloud.google.com/model-armor/overview)
- [Safety and content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters)
- [Gen AI evaluation service overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview)
