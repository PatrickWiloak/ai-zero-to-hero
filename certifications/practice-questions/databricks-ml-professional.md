---
last-updated: 2026-08-09
difficulty: advanced
---

# Databricks Certified Machine Learning Professional - Practice Questions

15 questions for the ML Professional exam, weighted toward MLOps and ML pipelines (30%), advanced ML (25%), feature engineering (20%), then deployment and serving (15%) and monitoring (10%).

> **Cert page:** [exams/databricks/ml-professional/](../databricks/ml-professional/README.md)

---

### Question 1
**Scenario:** A feature must be computed from events strictly before each label's timestamp.

A. Ignore the timestamps and join each label to the whole feature table by key
B. A point-in-time join using the feature store's time-aware lookup
C. Use the latest feature values available at training time, joining each label to the most recent computed row in the table
D. Join on the entity key only, without any condition on the event timestamps

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Joining on key alone attaches today's feature values to a label from last year, which is leakage that inflates validation scores and collapses in production. Point-in-time correctness is the reason feature stores track feature timestamps at all.
</details>

---

### Question 2
**Scenario:** A production model must be retrained and redeployed automatically when quality degrades.

A. A monitored trigger feeding a pipeline that retrains, evaluates against the incumbent, and promotes only if it wins
B. Never retrain
C. Retrain daily regardless
D. Manual retraining when someone notices a drop on a dashboard, followed by a hand-run deployment to the production endpoint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The champion-challenger comparison is what makes automation safe: a retrained model on a bad data batch will not be promoted. Without that gate, automated retraining is a mechanism for automatically deploying regressions.
</details>

---

### Question 3
**Scenario:** Two model versions must be compared on live traffic.

A. Offline evaluation only, using a held-out test set from historical data to decide which version serves users, then promoting the winner directly
B. Replace the model entirely
C. An endpoint with traffic split between versions, or shadow serving of the challenger
D. Ask a sample of users which version they prefer after they have used each one for a whole week

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shadow mode measures the challenger on real traffic at zero user risk, which is the right first step when the model affects decisions. A traffic split then gives real outcome data on a bounded share before full promotion.
</details>

---

### Question 4
**Scenario:** Model quality monitoring needs ground truth that arrives days after the prediction.

A. Monitor input drift now, and join delayed labels to predictions when they arrive
B. Skip monitoring
C. Monitor input drift only, and skip quality metrics because labels arrive too late to be useful
D. Assume quality is stable until a customer complaint arrives, then investigate the model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Label delay is normal, so you need both signals: drift as the leading indicator available now, and realized accuracy as the lagging ground truth. Inference tables make the join straightforward because requests and predictions are already in Delta.
</details>

---

### Question 5
**Scenario:** A model artifact must carry its input schema so bad requests fail clearly.

A. Document the schema separately in a wiki page that callers are expected to read and follow
B. No schema
C. Validate in the client only, trusting every caller to send correctly shaped requests
D. Log the model with an MLflow signature and an input example

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The signature makes serving reject malformed input with a clear error instead of silently coercing types and producing nonsense predictions. It also documents the contract for whoever integrates months later.
</details>

---

### Question 6
**Scenario:** Custom preprocessing and postprocessing must ship with the model.

A. Two separate services, one for preprocessing and one for the model, called in sequence by each client
B. Ask callers to reimplement it
C. An `mlflow.pyfunc` custom model wrapping the full logic, logged as one artifact
D. A README

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Packaging preprocessing with the model means every caller gets identical behavior and there is one thing to version. Asking callers to reimplement transformation logic is how training-serving skew re-enters after you removed it from your own pipeline.
</details>

---

### Question 7
**Scenario:** Feature computation is expensive and shared by several models.

A. Cache the computed features in memory inside each notebook session and rebuild them after every restart
B. Compute in each notebook that needs the feature, so each model team owns and schedules its own copy of the logic
C. Materialize features into feature tables on a schedule, with online tables for serving
D. Recompute the features inside each model's own training job and serving code every time it runs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Materialization amortizes the cost across consumers and gives one definition to govern. Online tables replicate the values into a low-latency store so real-time serving does not need to run the batch computation on the request path.
</details>

---

### Question 8
**Scenario:** A pipeline must be promoted across dev, staging, and production workspaces.

A. Copy notebooks
B. Databricks Asset Bundles or CI/CD, with environment-specific catalogs and configuration, and models registered in Unity Catalog
C. Manual export
D. One workspace for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bundles define jobs, pipelines, and models as code with per-target configuration, so the same artifact is promoted rather than reimplemented. Unity Catalog lets a model registered once be referenced from every workspace with governed access.
</details>

---

### Question 9
**Scenario:** An ensemble of models must be served behind one endpoint.

A. Multiple endpoints with client-side logic that calls each one and combines the predictions in the application
B. A pyfunc model that loads the components and combines their predictions, served as one version
C. Retrain as one model
D. It is not possible, because a serving endpoint can host only a single model and cannot run any custom code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Wrapping the ensemble keeps the combination logic versioned with the components, so a change to the weighting is a new model version rather than a client deployment. Client-side ensembling spreads the logic across every consumer.
</details>

---

### Question 10
**Scenario:** Model explanations are required for individual predictions in production.

A. Global feature importance only
B. Compute per-prediction attributions (for example SHAP) and store them alongside the prediction for later inspection
C. Model documentation
D. Training curves

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global importance describes the model; a contested decision needs the attribution for that specific row. Computing it at inference and persisting it means the explanation is available when the question arrives months later, rather than needing a reconstruction.
</details>

---

### Question 11
**Scenario:** A time-series model must be validated correctly.

A. Leave-one-out validation, holding out a single row at a time and training on every remaining row
B. A random stratified split that keeps the class proportions the same in the training and test sets
C. Random k-fold cross-validation, shuffling all rows into folds so that every fold trains on a mix of past and future data
D. Rolling-origin (walk-forward) validation, training on the past and validating on the future

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Random folds let the model learn from the future, which yields validation numbers that cannot be reproduced in production. Walk-forward validation also gives several evaluation windows, which reveals whether performance is stable over time.
</details>

---

### Question 12
**Scenario:** Training data must be versioned so a model can be rebuilt exactly.

A. Overwrite the table each run, and keep the notebook that produced it in Git for later reproduction
B. Keep the latest only
C. Note the date
D. Delta table versions or a snapshot, with the version recorded in the MLflow run

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recording the Delta version number in the run makes rebuild deterministic without duplicating the data, since time travel can read that version directly. A date alone is insufficient when the table is updated multiple times a day.
</details>

---

### Question 13
**Scenario:** An endpoint's latency must be reduced for a large model.

A. Reduce logging to errors only, and turn off the inference table and the request payload capture
B. Add more model versions behind the same endpoint so that the requests are spread across all of them
C. Right-size the compute (GPU if needed), cache repeated responses, consider quantization
D. Increase the batch size so that each request waits until many more rows can be processed together

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Latency work starts with measuring where the time goes: model compute, feature lookup, or queueing. Larger batches improve throughput while worsening latency, so they are the wrong lever for a p99 target.
</details>

---

### Question 14
**Scenario:** Governance requires knowing which data a model was trained on and who can use it.

A. Unity Catalog lineage linking the model to the tables and features it consumed, with grants controlling access to the model
B. Comments in code
C. File permissions
D. A wiki page listing each model with its training tables and owners, updated by hand by the model owner after every single release

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lineage is captured automatically rather than documented manually, which is why it stays accurate. Governing the model in the same catalog as the data means one permission model covers both, which is what an audit is actually asking for.
</details>

---

### Question 15
**Scenario:** A model exhibits degraded performance for one customer segment.

A. Evaluate disaggregated performance by segment, investigate representation and feature quality for that group, and document known limitations
B. Increase the model size
C. Report only aggregate accuracy
D. Remove the segment

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Aggregate metrics average away subgroup failures, so they must be broken out to be seen at all. Removing the segment from evaluation makes the number look better while leaving the harm in production, which is the outcome the practice exists to prevent.
</details>

---

## Where to go deeper

- [ML Professional cert page](../databricks/ml-professional/README.md) - notes, practice plan, strategy
- [ML Associate practice questions](databricks-ml-associate.md) - the prerequisite level
- [Data Engineer Professional practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-professional/) - the pipeline counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - evaluation thinking applied to generative systems
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
