---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Data Scientist Associate (DP-100) - Practice Questions

15 questions for DP-100 prep, weighted toward exploring data and training models (35-40%), with design and preparation, deployment preparation, and deploy and retrain at 20-25% each.

> **Cert page:** [exams/azure/dp-100/](../azure/dp-100/README.md)

---

### Question 1
**Scenario:** A training job needs a GPU for four hours a week and nothing the rest of the time.

A. Serverless Spark compute, which suits distributed data preparation jobs and would not be the way to provide a GPU for a training job
B. A Compute Cluster with minimum nodes 0 and a GPU VM size
C. A Kubernetes online endpoint, which hosts a model for real-time scoring and keeps nodes running, not a place to run a weekly job
D. An always-on Compute Instance with a GPU, which is a single-user workstation that bills every hour it is running, including idle ones

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Compute clusters scale to zero when idle, so you pay only for the hours the job runs, and they scale out for parallel runs. A compute instance is a personal development box that bills while running. Online endpoints are for inference. Serverless Spark suits distributed data processing rather than single-node GPU training.
</details>

---

### Question 2
**Scenario:** A model is trained with an experiment tracked in Azure Machine Learning. What is the correct order before serving traffic?

A. Register the model, deploy it, and then train it, which reverses the order
B. Deploy directly from the run output folder without registering, which skips the versioning and lineage that a registry entry gives
C. Evaluate, register the model in the workspace registry, then deploy to an endpoint
D. Deploy to the endpoint first, then register the model, then evaluate, which puts untested code in front of live traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Registration gives the artifact a name, version, and lineage back to the run, which is what makes rollback and audit possible. Deploying straight from run output leaves you without a versioned reference. Evaluation before registration prevents promoting a model that underperforms the incumbent.
</details>

---

### Question 3
**Scenario:** You need low-latency real-time predictions with autoscaling and no cluster management.

A. A scheduled pipeline job that runs on a cluster at fixed times, which scores in batches
B. Managed online endpoint, which provides autoscaling, authentication, and low-latency scoring without cluster management
C. A compute instance running a notebook, which is a single-user machine with no autoscaling
D. Batch endpoint, which scores large inputs asynchronously and gives no low-latency responses

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed online endpoints handle the compute, TLS, authentication, and blue-green deployment slots for you. Batch endpoints are asynchronous and optimized for throughput over large inputs. A pipeline job is scheduled work, and a notebook is not a production serving surface.
</details>

---

### Question 4
**Scenario:** A new model version should take 10% of live traffic before full rollout.

A. Retrain the model using only 10% of the data, which changes the training set and has no effect on how much live traffic it receives
B. Add a second deployment under the same online endpoint and set traffic allocation to 90/10
C. Create a second endpoint for the new version and ask clients to alternate between the two URLs at their own discretion in code
D. Use a batch endpoint for the new version, which scores files in jobs and cannot take a share of live online requests

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An online endpoint can host multiple deployments and split traffic by percentage, which is exactly a canary. Callers keep using one URL, so rollback is a traffic change rather than a client change. A second endpoint would require clients to know about it.
</details>

---

### Question 5
**Scenario:** Training data lives in an Azure Data Lake Storage Gen2 account and must be referenced without credentials in code.

A. Register a datastore with identity-based access and use a data asset that points at it, so no secret lives in the code
B. Hard-code a SAS token in the training script, which puts a credential in source control
C. Make the container public so that the job needs no credentials, which exposes the data
D. Copy the data into the notebook's local disk each time, which duplicates the data, loses the link to the lake, and does not scale to large datasets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A datastore holds the connection, and identity-based access uses the workspace or user managed identity so no secret lives in code. Data assets add versioning on top. Hard-coded SAS tokens leak through notebooks and git history, and public containers are a data exposure.
</details>

---

### Question 6
**Scenario:** You want the best model over a search space of learning rates and batch sizes, stopping unpromising runs early.

A. A sweep job with a sampling method and an early termination policy such as bandit or median stopping
B. Manual grid search in a notebook, which is slow and has no early stopping
C. AutoML featurization only, which transforms the input columns but does not search a space of learning rates and batch sizes
D. A single training run with the framework's default values

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sweep jobs define the search space, the sampling strategy (random, grid, or Bayesian), the primary metric to optimize, and a termination policy that kills runs falling behind. That last part is where most of the compute savings come from. Manual search wastes budget and is not reproducible.
</details>

---

### Question 7
**Scenario:** A classification model must be explained to a regulator: which features drove a given prediction?

A. The Responsible AI dashboard with feature importance, including per-prediction explanations and counterfactuals
B. The learning rate schedule used during training, which says nothing about feature influence
C. The ROC curve, which shows threshold trade-offs but not which features drove a prediction
D. The confusion matrix, which counts correct and incorrect predictions per class but does not explain why a given prediction was made

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Responsible AI dashboard bundles interpretability (global and local feature importance), error analysis, fairness assessment, and counterfactuals. A confusion matrix and ROC curve describe aggregate performance, not the reasoning behind an individual decision.
</details>

---

### Question 8
**Scenario:** A dataset has 5% positive cases and the model reports 95% accuracy.

A. Add more features to the model, which does not address the fact that accuracy hides the minority class
B. The model is excellent, because 95% accuracy is high by the usual standard
C. Accuracy is misleading with imbalance; use precision, recall, F1, or AUC-PR and consider resampling, class weights, or threshold tuning
D. Increase the learning rate so that the model fits the positive cases faster, which can destabilize training

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Predicting the majority class every time scores 95% here while catching nothing. Precision and recall on the positive class expose that immediately, and AUC-PR is the more honest summary metric under imbalance than AUC-ROC. Resampling and class weights address the training side.
</details>

---

### Question 9
**Scenario:** Multiple steps (prep, train, evaluate, register) must run in sequence with reusable outputs.

A. One long script that does everything in a single job, which works but gives no reusable steps or separate outputs for each stage
B. Separate manual runs, with a person starting each step
C. A cron job on a VM that calls the scripts in order, which gives scheduling but no tracked inputs, outputs, or reuse of components
D. A pipeline job composed of components, with outputs passed between steps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Components are versioned, reusable units, and a pipeline wires their inputs and outputs into a DAG that can cache unchanged steps. That caching is the practical payoff: changing only the training step does not force data prep to rerun.
</details>

---

### Question 10
**Scenario:** A deployed model's accuracy degrades over months while the code is unchanged.

A. The model file is corrupt, so predictions slowly degrade as the artifact is read from storage, which is unlikely with a file that is unchanged
B. The compute is undersized for the traffic, which causes latency and timeouts but does not make the predictions less accurate
C. The endpoint is misconfigured, which would cause failures from day one
D. Data drift: the input distribution has moved away from the training data, so monitor drift and retrain

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Drift is the normal explanation for silent decay. Azure Machine Learning model monitoring compares production inputs against a baseline and can alert on feature drift and data quality, which is what turns retraining from a guess into a triggered action. Concept drift, where the relationship itself changes, is the related second case.
</details>

---

### Question 11
**Scenario:** An experiment must be reproducible six months later.

A. Note the results in a document, which records outcomes but not the code, data, and environment needed to rerun the experiment
B. Use a registered environment with pinned dependencies, versioned data assets, and logged parameters per run
C. Save the notebook only, which keeps the code but not the dependency versions or the exact data used in the original run
D. Keep the compute instance running, which preserves the packages for now

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reproducibility needs three things pinned: code, data, and environment. Registered environments capture the container and package versions, versioned data assets capture the input, and run logging captures parameters and outputs. A saved notebook without the environment usually will not run later.
</details>

---

### Question 12
**Scenario:** AutoML is used for a tabular classification task. What does it not do for you?

A. Cross-validation, which AutoML runs on the training data when it validates candidate models, so it does that for you
B. Feature engineering, which AutoML performs through its featurization settings, such as imputation and encoding, so it is done for you
C. Decide whether the business problem is well posed and the label is correct
D. Model selection, which AutoML performs by training and ranking many algorithms against the primary metric, so it is done for you

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AutoML automates featurization, algorithm selection, hyperparameter search, and validation. What no tool can do is tell you the target is leaking information from the future, that the label definition is wrong, or that the task should not be a classification problem at all. Target leakage is the failure mode that produces suspiciously perfect AutoML results.
</details>

---

### Question 13
**Scenario:** Scoring 50 million rows nightly with no latency requirement.

A. A single VM script that loops through the rows, which does not scale for 50 million rows
B. Managed online endpoint, which serves low-latency requests one at a time
C. Real-time streaming, which processes events as they arrive and is more complex and costly than a nightly scheduled job needs
D. Batch endpoint with a compute cluster, which parallelizes the scoring across nodes and writes results to storage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Batch endpoints parallelize scoring across cluster nodes, checkpoint progress, and write outputs to storage, which fits large offline jobs. Sending 50 million rows through a real-time endpoint is slow and expensive because you pay per-request overhead for every record.
</details>

---

### Question 14
**Scenario:** A workspace must not expose data over public endpoints.

A. Managed virtual network isolation for the workspace, private endpoints to the workspace and its dependent storage, key vault, and registry
B. A firewall rule on the storage account only
C. Disabling the studio UI
D. An NSG on the compute subnet only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The workspace is not one resource: it depends on storage, Key Vault, Container Registry, and Application Insights, and any of those left public is the gap. Managed VNet isolation plus private endpoints across the dependency set is the complete answer.
</details>

---

### Question 15
**Scenario:** A team wants to share a curated model across several workspaces.

A. Copy the file to each workspace, which creates duplicates that drift apart and have no shared version history or lineage
B. Email the pickle file to teammates, which gives no access control, versioning, or audit trail and is unsafe to load
C. Publish it to an Azure Machine Learning registry, which is cross-workspace and cross-region
D. Store it in a public blob so any workspace can download it, which exposes the model to everyone on the internet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Registries hold models, components, environments, and data assets above the workspace level, so one artifact can be promoted across dev, test, and production workspaces with lineage intact. Copying files loses version history, and a pickle in a public blob is both an integrity and a deserialization risk.
</details>

---

## Where to go deeper

- [DP-100 cert page](../azure/dp-100/README.md) - notes, practice plan, strategy
- [AI-102 practice questions](azure-ai-engineer-ai-102.md) - the applied AI counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - measuring model quality
- [AI/ML systems topic index](../../build/README.md) - MLOps in context
- **[📖 DP-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)** - official skills outline
