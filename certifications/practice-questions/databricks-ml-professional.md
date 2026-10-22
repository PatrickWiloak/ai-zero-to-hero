---
last-updated: 2026-10-22
difficulty: advanced
---

# Databricks Certified Machine Learning Professional - Practice Questions

30 questions for the ML Professional exam, weighted toward MLOps and ML pipelines (30%), advanced ML (25%), feature engineering (20%), then deployment and serving (15%) and monitoring (10%).

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

### Question 16
**Scenario:** Production data cannot be read from the dev workspace, and the audit team wants the production model built only from reviewed code. The team is choosing between promoting a model artifact and promoting the training code.

A. Train in dev on a copy of production data, then move the resulting model file into production by hand
B. Train once in dev on sample data and promote that same artifact, since retraining adds risk
C. Promote the reviewed training code through staging, then let the production job train on production data
D. Let data scientists train in the production workspace from notebooks, then register their best result

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When production data is only reachable in production, Databricks' "deploy code" pattern promotes the reviewed pipeline code and runs training there, so the model is built from audited code on the right data. Copying production data into dev breaks the access rule, a model trained on samples may not hold up, and ad hoc notebook training in production skips review.
</details>

---

### Question 17
**Scenario:** Dev and prod use separate Unity Catalog catalogs. Data scientists must train on production tables but must never write to the production catalog.

A. Grant the dev group `USE CATALOG`, `USE SCHEMA` and `SELECT` on prod, and write outputs to the dev catalog
B. Give the dev group `ALL PRIVILEGES` on the prod catalog and ask the team not to write anything to it
C. Copy all production tables into the dev catalog each night so that the dev group never touches prod
D. Share one service principal's token with the dev group so that it can read from the prod catalog

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Unity Catalog privileges can give read-only access to production data while the team's own writes go to the dev catalog, which is the least-privilege setup. `ALL PRIVILEGES` with a request not to write is not a control. Nightly copies duplicate data and governance, and sharing a service principal's token breaks individual accountability.
</details>

---

### Question 18
**Scenario:** A model registered in Unity Catalog must be loaded by a production job that runs as a service principal in a different workspace attached to the same metastore.

A. Export the model files from the source workspace and import them into the production workspace
B. Register the model a second time in the production workspace's own model registry
C. Give the service principal the workspace admin role in the workspace where the model was trained
D. Grant the service principal `EXECUTE` on the model, plus `USE CATALOG` and `USE SCHEMA`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Models in Unity Catalog are governed securables visible from every workspace on the metastore, so access is a grant: `EXECUTE` on the model plus usage on its catalog and schema. Copying or re-registering creates duplicates without lineage, and workspace admin in another workspace is far broader than needed.
</details>

---

### Question 19
**Scenario:** A nightly retraining job runs as the data scientist who created it. When she goes on leave and her account is deactivated, the job starts failing.

A. Recreate the job under another data scientist's account each time the current owner is away
B. Set the job to run as a service principal that has only the privileges the pipeline needs
C. Store the data scientist's personal access token in the job so it keeps working after deactivation
D. Move the job's logic into a notebook that a team member runs by hand each night instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Production jobs should run as a service principal with least-privilege grants, so they do not depend on any one person's account. Moving ownership between people repeats the problem, a deactivated user's token should not keep working and would be a security issue if it did, and manual runs remove the automation.
</details>

---

### Question 20
**Scenario:** A bug in a feature function shipped to production and silently produced wrong features for a week. The team wants to catch this kind of error before deployment.

A. Retrain the model more often so that any wrong feature values are soon replaced by correct ones
B. Add more monitoring dashboards so that the wrong features are noticed after deployment
C. Ask reviewers to read every feature function carefully before each release goes to production
D. Add unit tests for feature functions and integration tests on sample data, run in CI before deploy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Automated unit and integration tests in a CI pipeline catch logic errors before code reaches production, every time. Retraining on wrong features learns the bug, dashboards detect after the damage, and manual reading is valuable but not a reliable gate on its own.
</details>

---

### Question 21
**Scenario:** A pandas UDF that scores a Spark DataFrame loads a 2 GB model from storage on every call, and most of the job's time goes into reloading it.

A. Use an iterator-of-series pandas UDF that loads the model once per task, then scores each batch
B. Increase the batch size to one row so that each call to the UDF finishes faster than before
C. Collect the DataFrame to the driver and score it there, so the model is only loaded once
D. Save the model inside every row of the DataFrame so that each worker already has a copy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The `Iterator[pd.Series] -> Iterator[pd.Series]` form of a pandas UDF runs setup code once per task before iterating over batches, which is the documented pattern for expensive state such as loading a model. Smaller batches mean more calls, collecting to the driver gives up parallelism, and storing a model in every row is absurdly wasteful.
</details>

---

### Question 22
**Scenario:** On a dataset with 2% positives, a team oversamples the minority class with SMOTE and then splits into train and validation. Validation recall looks excellent, but production recall is poor.

A. Apply SMOTE to the production data as well so that it matches what the model saw in training
B. Increase the SMOTE ratio until the classes are exactly balanced in the validation data as well
C. Split first and resample only the training data, so validation keeps the real class balance
D. Remove the validation step, since resampled data cannot be used to measure a model reliably

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Resampling before the split leaks synthetic points derived from validation rows into training and makes validation unrealistic. Resample after splitting and only on training data, so evaluation reflects the real distribution. Production data cannot be resampled, more balancing worsens the leak, and dropping validation removes the check.
</details>

---

### Question 23
**Scenario:** A team builds a stacking ensemble. The meta-model is trained on the base models' predictions for the same rows the base models were trained on, and it overfits badly.

A. Train the meta-model on the base models' predictions for the test set and evaluate it there too
B. Train the meta-model on out-of-fold predictions from cross-validation of the base models
C. Use a deeper meta-model so that it can learn which base model to trust in each situation
D. Average the base models' predictions instead, since stacking cannot work with overfit models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Base models are overconfident on their own training rows, so the meta-model must learn from out-of-fold predictions that mimic unseen data. Training and evaluating on the test set leaks it, a deeper meta-model overfits further, and averaging gives up stacking rather than fixing it.
</details>

---

### Question 24
**Scenario:** A hyperparameter search runs 200 trials of a model that trains for 50 epochs each. Most trials are clearly poor after 5 epochs but still run to the end.

A. Reduce every trial to 5 epochs, so that the full search finishes in a tenth of the time
B. Run all 200 trials one after another on a single node so that each gets the full machine
C. Increase the number of trials so that the search finds good settings despite the waste
D. Use a tuner with pruning, such as Optuna, to stop poor trials early using their metrics

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pruning stops trials whose intermediate results are clearly worse than others, freeing resources for promising ones, while good trials still train fully. Cutting every trial to 5 epochs misjudges models that improve later, sequential single-node runs are slower, and more trials add to the waste.
</details>

---

### Question 25
**Scenario:** A fraud model served on a Model Serving endpoint needs the customer's latest feature values at request time with millisecond latency. The features live in a Unity Catalog feature table.

A. Publish the feature table to an online store and let the endpoint look up features by key
B. Have the endpoint query the offline Delta feature table with a SQL warehouse on every request
C. Make the caller compute all features itself and pass them in with each scoring request
D. Cache a copy of the whole feature table inside the model artifact when it is registered

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An online store serves feature lookups at low latency and is kept in sync with the offline feature table, and models logged with feature metadata can look up features automatically at serving time. Querying Delta per request is too slow, making callers compute features invites skew, and a snapshot in the artifact goes stale.
</details>

---

### Question 26
**Scenario:** A recommendation model needs a "clicks in the last 10 minutes" feature that stays fresh, computed from a Kafka click stream.

A. Recompute the feature once a night with a batch job that scans the full click history table
B. Use Structured Streaming to compute windowed aggregates and write them to the feature table
C. Ask the application to count clicks in memory and send the count with each scoring request
D. Compute the feature at training time only, since recent clicks do not change between retrains

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Structured Streaming with windowed aggregations keeps a near-real-time feature updated in the feature table, from which it can be published for serving. A nightly batch cannot provide a 10-minute window, in-app counting duplicates logic outside the governed pipeline, and a training-only value is stale by definition.
</details>

---

### Question 27
**Scenario:** A tree model uses a merchant ID with 200,000 values. One-hot encoding is too wide, so the team uses target encoding, and validation scores look far better than production.

A. Switch back to one-hot encoding and accept the wide feature set to avoid any encoding issue
B. Replace merchant ID with a random integer per merchant, since trees can split on any number
C. Compute the encoding out-of-fold on training data with smoothing, then apply it to validation
D. Compute the target encoding on the full dataset once so that the values are as accurate as possible

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Target encoding computed with each row's own label leaks the target, which inflates validation scores. Out-of-fold encoding with smoothing toward the global mean prevents that leak and handles rare categories. Encoding on the full dataset is the leak, random integers carry no signal, and one-hot at this cardinality is the problem the team was avoiding.
</details>

---

### Question 28
**Scenario:** A Model Serving endpoint with scale-to-zero enabled serves a checkout flow. After quiet periods, the first requests take many seconds, which breaks the checkout timeout.

A. Move the model to a batch job that scores checkout requests every few minutes instead
B. Add retries in the checkout client so that the slow first request is sent a second time
C. Increase the endpoint's maximum concurrency so that it can scale up further during peaks
D. Disable scale-to-zero and keep minimum capacity provisioned so the endpoint stays warm

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Scale-to-zero saves cost but adds cold-start latency when traffic resumes, which a latency-critical path cannot accept, so it needs capacity kept warm. Retries add to the wait, a higher maximum does not help the first request after idle, and batch scoring cannot serve a synchronous checkout.
</details>

---

### Question 29
**Scenario:** The team wants every request and response sent to a model serving endpoint captured in a Delta table for debugging, drift analysis and later label joins.

A. Add logging code to every client application that calls the endpoint and merge the logs weekly
B. Enable inference tables on the endpoint so payloads are logged automatically to Unity Catalog
C. Export the endpoint's metrics page each day and store the screenshots in a shared folder
D. Turn on cluster logs for the workspace, since they record each request that the endpoint serves

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inference tables log endpoint requests and responses to a Delta table in Unity Catalog, which feeds debugging, monitoring and joins with delayed labels. Client-side logging is inconsistent across apps, metrics pages hold aggregates rather than payloads, and cluster logs are not a request log.
</details>

---

### Question 30
**Scenario:** A team wants scheduled drift and quality metrics on its model's inference table, compared with the training data, without writing custom monitoring code.

A. Create a data profile (formerly Lakehouse Monitoring) of inference type with the training data as baseline
B. Write a notebook that computes summary statistics by hand and emails them each Monday
C. Check the endpoint's latency graph, since drift in the inputs always shows up as higher latency
D. Retrain the model every day, which removes the need to measure drift in the input data at all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data profiling, the renamed Lakehouse Monitoring, supports an inference profile type for request logs and computes profile and drift metric tables, including drift against a baseline table, on a schedule. A hand-written notebook is the custom code the team wants to avoid, latency does not measure drift, and blind daily retraining hides problems instead of measuring them.
</details>

---

## Where to go deeper

- [ML Professional cert page](../databricks/ml-professional/README.md) - notes, practice plan, strategy
- [ML Associate practice questions](databricks-ml-associate.md) - the prerequisite level
- [Data Engineer Professional practice questions](https://data.noblerworks.com/resources/practice-questions/databricks-data-engineer-professional/) - the pipeline counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - evaluation thinking applied to generative systems
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
