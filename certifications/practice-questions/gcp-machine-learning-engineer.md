---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Machine Learning Engineer - Practice Questions

15 questions for the Professional ML Engineer exam, covering problem framing, data and model development on Agent Platform (formerly Vertex AI), pipeline automation, serving, and monitoring.

> **Cert page:** [exams/gcp/machine-learning-engineer/](../gcp/machine-learning-engineer/README.md)

---

### Question 1
**Scenario:** A business wants to "use AI to improve retention." What is the first engineering step?

A. Choose a model architecture such as gradient-boosted trees or a deep network, then prototype it on whatever customer data is already available
B. Provision a GPU cluster and managed notebooks so that the data scientists can begin experimenting as soon as the business gives approval
C. Frame it as an ML problem: define the prediction target, the decision it informs, the label source, and the success metric
D. Collect more data from every system the company owns first, since more data always improves a model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The exam consistently rewards framing before building. A churn model is useless unless someone acts on the score, so the decision and intervention define the label window, the prediction horizon, and the metric. Skipping this produces a technically fine model nobody uses.
</details>

---

### Question 2
**Scenario:** Features must be shared consistently between training and online serving.

A. Agent Platform Feature Store, serving the same feature values offline for training and online for inference
B. A shared spreadsheet documenting each feature's formula, which engineers then reimplement separately in training and serving code
C. Recompute them in each system from the raw data, using whatever library each team knows
D. Cache the computed values in the application's memory and read them back during training runs as well as serving

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A feature store exists to remove training-serving skew by making one definition the source for both paths, and it provides point-in-time correct historical retrieval so training does not accidentally use future values. Recomputing in two systems guarantees eventual divergence.
</details>

---

### Question 3
**Scenario:** Which Agent Platform capability trains a model with no code on tabular data?

A. Model Garden
B. Agent Platform Workbench
C. AutoML
D. Custom training with a container

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AutoML handles feature engineering, architecture search, and tuning for tabular, image, text, and video tasks. Custom training is the escape hatch when you need your own code, and Model Garden is the catalog of pretrained and foundation models.
</details>

---

### Question 4
**Scenario:** A training job needs to run reproducibly with data prep, training, evaluation, and conditional deployment.

A. Agent Platform Pipelines (Kubeflow Pipelines or TFX) with components and a conditional deploy step
B. A shell script on a VM that runs each step in order and is started by a cron entry every night, with logs kept on the disk
C. Cloud Functions chained together by Pub/Sub messages, each function running one step of the workflow
D. A notebook run manually by a data scientist, with results saved in a shared folder

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipelines give a versioned DAG with artifact lineage and caching, and the conditional step turns the evaluation into an enforced gate. Notebooks are for exploration; they do not produce the reproducibility or audit trail a production model needs.
</details>

---

### Question 5
**Scenario:** An online prediction endpoint must serve two model versions with traffic split.

A. Two endpoints, each serving one model version, with clients choosing which endpoint to call
B. A load balancer in front of two separate services that each host one of the model versions
C. One endpoint with multiple deployed models and a traffic split percentage
D. Batch prediction jobs that score a sample of requests with the new model version and compare the results

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Agent Platform endpoints support several deployed models with a traffic split, so canary rollout and rollback are configuration changes rather than client changes. Each deployed model has its own machine type and autoscaling settings.
</details>

---

### Question 6
**Scenario:** Predictions are needed for 100 million rows overnight.

A. Batch prediction reading from BigQuery or Cloud Storage and writing results back
B. A Cloud Function per row, invoked in parallel by a Pub/Sub message for each of the 100 million rows
C. Online prediction from a single endpoint, scaled out with a high maximum replica count overnight
D. One request per row sent in a loop from a script running on a single VM

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch prediction parallelizes across workers and avoids paying per-request overhead 100 million times. Online endpoints are for latency-sensitive single predictions, and using them for bulk scoring is both slow and disproportionately expensive.
</details>

---

### Question 7
**Scenario:** A deployed model's inputs are drifting from the training distribution.

A. Cloud Monitoring CPU and memory metrics on the endpoint, with an alert whenever utilization stays high for long
B. Model Monitoring on Agent Platform, comparing serving inputs to a training baseline to alert on skew and drift
C. Nothing can be detected until users complain about the quality
D. Manual sampling of predictions by an analyst each quarter, checked against later labels

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Monitoring distinguishes training-serving skew (serving data differs from training data) from prediction drift (serving data changes over time), and alerts per feature. Infrastructure metrics show a perfectly healthy endpoint serving increasingly wrong answers.
</details>

---

### Question 8
**Scenario:** A model must explain individual predictions for a regulated decision.

A. Model size, since a smaller model has fewer parameters and is therefore easier to explain to a regulator
B. Agent Platform Explainable AI with feature attributions (integrated gradients, sampled Shapley, or XRAI)
C. The training loss curve, which shows how well the model fit the data it saw during training
D. The confusion matrix, which shows true and false prediction counts for each class

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Explainable AI attributes a specific prediction to input features, which is what an adverse-decision explanation requires. The method depends on the model type: gradient-based for differentiable models, sampled Shapley for non-differentiable ones.
</details>

---

### Question 9
**Scenario:** Training data in BigQuery must be prepared for a TensorFlow model at scale.

A. Export to CSV and load it all into pandas on a large notebook instance, then convert the rows to tensors
B. Process each row one at a time in a Python loop that reads from BigQuery through the client library
C. BigQuery for aggregation, then Dataflow (Apache Beam) or TFX for distributed transformation, writing TFRecords
D. Use a single large VM with as much memory as possible and run the preprocessing script there

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pushing aggregation into BigQuery and heavy transformation into Dataflow keeps the work distributed, and TFX Transform has the important property that the same transformation graph is applied at serving time, which prevents skew.
</details>

---

### Question 10
**Scenario:** Hyperparameter tuning must be efficient on an expensive training job.

A. Random search over the full space with no stopping, running every trial to the end of training
B. Grid search over every combination of the parameter values, which tests the whole space exhaustively
C. One configuration chosen by the team's most experienced engineer and trained for a long time
D. Agent Platform hyperparameter tuning with Bayesian optimization and early stopping

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bayesian search conditions each trial on previous results, so it converges in far fewer runs than grid search when each run is expensive. Early stopping of underperforming trials is where the rest of the savings comes from.
</details>

---

### Question 11
**Scenario:** A team wants a foundation model grounded in their own documents on Google Cloud.

A. Fine-tune on the documents so that the model memorizes every fact they contain
B. Paste the documents into every prompt, even past the context window
C. Train a new LLM from scratch on the documents so that it knows the content natively, with no retrieval step
D. Agent Search and grounding, or a RAG pipeline with embeddings and Vector Search for retrieval

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Grounding keeps answers tied to retrievable sources with citations and updates as the documents update. Fine-tuning would encode a snapshot of the knowledge into weights, which is both expensive to refresh and impossible to cite.
</details>

---

### Question 12
**Scenario:** A training job must use preemptible or Spot VMs safely.

A. Checkpoint to Cloud Storage often and resume from the last checkpoint after preemption
B. Never checkpoint, because writing to Cloud Storage slows training more than a restart would cost
C. Use only on-demand VMs, since Spot capacity cannot run training workloads that last longer than an hour
D. Restart from scratch each time, because a checkpoint written before a preemption is always corrupted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Spot capacity cuts cost substantially, and checkpointing is what converts a preemption from a lost run into a short delay. The checkpoint interval is a trade-off between storage writes and the work you are willing to lose.
</details>

---

### Question 13
**Scenario:** A model must not be trained on personally identifiable information.

A. Trust the data, because the source system's owners already agreed that it contains no personal data at all, in writing
B. Use Cloud DLP to inspect and de-identify (mask, tokenize, or bucket) before training, and document it
C. Encrypt the training job and disks with a customer-managed key
D. Delete the model after training, because a deleted model can no longer reveal anything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models memorize training data, so PII in the corpus can resurface in outputs and in membership inference attacks. Inspecting and de-identifying before training addresses it at the source, and documenting the transformation is what makes the claim auditable.
</details>

---

### Question 14
**Scenario:** An ML system must retrain automatically when performance drops.

A. Retrain manually when a stakeholder notices that the predictions look worse than they used to, then redeploy
B. Trigger retraining from monitoring signals (drift or degraded metrics) through a pipeline with an evaluation gate
C. Retrain on a fixed schedule regardless of whether the data or the model performance has changed since
D. Never retrain, because a model validated once at launch keeps its accuracy as the incoming data changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven retraining responds to the actual condition rather than the calendar, and the evaluation gate is what prevents automatically deploying a model trained on a bad data batch. Fixed schedules are a reasonable fallback when a good trigger signal does not exist.
</details>

---

### Question 15
**Scenario:** Which best describes the responsible AI step before launching a model that affects people?

A. Get legal sign-off only, since the legal team is responsible for every risk that the model creates for people
B. Check overall accuracy only, on a held-out test set that matches the training distribution closely
C. Add a disclaimer to the product page saying that predictions may be wrong and are not guaranteed
D. Evaluate disaggregated performance across affected groups, document intended use and limits, and define a human review path

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Aggregate accuracy hides subgroup failure, so disaggregated evaluation is the measurement that matters. Model cards document intended use and limits, and a human path handles the cases the model gets wrong, which is the part that determines real-world harm.
</details>

---

## Where to go deeper

- [Professional ML Engineer cert page](../gcp/machine-learning-engineer/README.md) - notes, practice plan, strategy
- [GCP Data Engineer practice questions](https://data.noblerworks.com/resources/practice-questions/gcp-data-engineer/) - the data platform beneath this
- [DP-100 practice questions](azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
