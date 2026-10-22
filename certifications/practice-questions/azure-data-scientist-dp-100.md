---
last-updated: 2026-10-22
difficulty: intermediate
---

# Azure Data Scientist Associate (DP-100) - Practice Questions

30 questions for DP-100 prep. DP-100 retired on 2026-06-01, so this bank is reference material. Questions 1-15 follow the older outline (exploring data and training models at 35-40%). Questions 16-30 follow the final skills outline (as of 2025-04-11): design and prepare a machine learning solution (20-25%), explore data and run experiments (20-25%), train and deploy models (25-30%), and optimize language models for AI applications (25-30%).

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

### Question 16
**Scenario:** Tabular training data is spread over hundreds of CSV files in a folder. Several teams read it, and the column types and the rows to skip should be defined once, not in every script.

A. A uri_file data asset pointing at one of the CSV files
B. A uri_folder data asset, with each script parsing the files its own way
C. An MLTable data asset with the schema in its definition
D. A local copy of the files on each compute instance

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** MLTable stores how to read tabular data (paths, column types, transformations) alongside the asset, so every consumer reads it the same way. uri_file covers one file. uri_folder points at the files but leaves parsing to each script, which is the duplication to avoid. Local copies drift and lose lineage.
</details>

### Question 17
**Scenario:** Several training jobs need the same Python packages, and runs must use exactly the same dependencies months later.

A. A registered, versioned custom environment (base image plus conda file)
B. Run `pip install` at the start of every training script
C. Use whichever curated environment is newest at the time of each run, so packages stay up to date
D. Install the packages by hand on the compute cluster nodes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A registered, versioned environment pins dependencies and is reused across jobs, which gives reproducibility. Installing at run time pulls whatever version is current. "Newest curated" changes over time. Cluster nodes are recreated as they scale, so hand-installed packages vanish.
</details>

### Question 18
**Scenario:** The monthly bill shows data scientists' compute instances running every night and weekend while nobody uses them.

A. Delete every compute instance at the end of each day and recreate it each morning
B. Move all work to a single shared compute instance
C. Switch every instance to the largest VM size so jobs finish sooner
D. Configure idle shutdown and start/stop schedules on the compute instances

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Idle shutdown stops an instance after a period of inactivity, and schedules stop and start it at set times, so it is not billed when unused. Deleting and recreating loses the workspace setup. A shared single-user instance does not fit how compute instances work. Larger VMs cost more per hour.
</details>

### Question 19
**Scenario:** A data preparation step must run distributed Spark code over large files during a pipeline, without the team managing a Spark cluster.

A. A compute instance, which is a single-user development VM
B. Serverless Spark compute (or an attached Synapse Spark pool) in Azure Machine Learning
C. A managed online endpoint
D. A Kubernetes compute target with one node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Serverless Spark compute runs Spark jobs on demand without cluster management, and an attached Synapse Spark pool is the alternative. A compute instance is one VM. Online endpoints serve models. A one-node Kubernetes target is not a Spark environment.
</details>

### Question 20
**Scenario:** A training script uses scikit-learn. The team wants parameters, metrics and the model logged without writing a log call for each one.

A. Print every value to the console and read the job's output log later
B. Call `mlflow.autolog()` before training
C. Save metrics to a CSV file in the outputs folder
D. Register the model first and add metrics to its description

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MLflow autologging captures parameters, metrics and the model for supported libraries, and Azure Machine Learning tracks MLflow runs natively. Console output and CSV files are not queryable run metadata. A model description is not experiment tracking.
</details>

### Question 21
**Scenario:** A model's overall accuracy is good, but the team suspects it fails badly for some groups of customers and wants to find which ones.

A. Retrain the model with more epochs
B. Look only at the overall confusion matrix
C. Raise the decision threshold for every prediction
D. Error analysis in the Responsible AI dashboard

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Error analysis breaks errors down by feature cohorts, showing where the model underperforms. More epochs do not reveal anything. An overall confusion matrix hides subgroup differences. Changing the threshold changes all predictions without diagnosing the problem.
</details>

### Question 22
**Scenario:** After 60 experiment runs, the team needs to find the run with the best validation AUC programmatically and read its parameters.

A. Query the runs with `mlflow.search_runs`, ordered by the metric
B. Open each run in the studio and copy values into a spreadsheet
C. Re-run all 60 experiments and watch which finishes with the highest score
D. Ask each team member which run they remember as best

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MLflow search returns runs with their parameters and metrics, filtered and ordered, so the best run can be found in code and repeatably. Manual copying is slow and error-prone. Re-running wastes compute. Memory is not a record.
</details>

### Question 23
**Scenario:** A training script in a local `src` folder must run on a compute cluster with a registered data asset as input, using SDK v2.

A. Upload the script to a blob container and start it from the Azure portal
B. Create a managed online endpoint and send the training data to it
C. A command job submitted with `ml_client.jobs.create_or_update`
D. Copy the script into a notebook on the cluster and run it cell by cell

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A command job packages the code, the command line, the environment, the compute target and inputs, and submitting it runs the script on the cluster with full tracking. Endpoints serve models rather than training them. Uploading or copying scripts skips job tracking and input handling.
</details>

### Question 24
**Scenario:** A new deployment on a managed online endpoint should receive a copy of live requests for testing, while users still get responses only from the current deployment.

A. Send 50% of live traffic to the new deployment
B. Mirror a percentage of traffic to the new deployment
C. Delete the current deployment and watch the error rate
D. Create a second endpoint and ask users to switch their URLs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mirrored traffic sends copies of requests to a deployment for testing while clients receive only the primary deployment's responses. Splitting traffic exposes users to the new model. Deleting the current deployment is a risky cut-over. Asking users to change URLs is not a test strategy.
</details>

### Question 25
**Scenario:** A model was logged in MLflow format. The team wants to deploy it to a managed online endpoint as quickly as possible.

A. Write a scoring script and a custom environment, since every deployment needs both
B. Convert the model to ONNX first, since endpoints only accept ONNX
C. Deploy it to a compute instance and expose the instance's port
D. Deploy it with no scoring script or environment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** For MLflow models, Azure Machine Learning generates the scoring logic and environment from the MLflow model's metadata, so no scoring script is required. Custom models need one, but MLflow models do not. Endpoints accept many formats, not just ONNX. A compute instance is not a serving platform.
</details>

### Question 26
**Scenario:** A pipeline that retrains a model must run every Monday at 06:00 without anyone starting it.

A. Create a schedule for the pipeline job with a cron or recurrence trigger
B. Ask the on-call engineer to submit the pipeline every Monday
C. Keep a compute instance running a loop that checks the time
D. Deploy the pipeline to a managed online endpoint

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Schedules trigger pipeline jobs on a cron or recurrence. A person is not automation. A time-checking loop wastes compute and fails silently. Online endpoints serve predictions; they do not run pipelines on a timetable.
</details>

### Question 27
**Scenario:** A team must pick a language model for summarising support tickets and wants to compare candidates on quality, cost and speed before deploying one.

A. Pick the model with the most parameters
B. Fine-tune every model in the catalog and keep the best
C. Shortlist from model cards and benchmarks, then test on sample tickets
D. Choose the model used in a popular blog post, since other teams have already tested it on a different task

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The model catalog lists models with cards and benchmark data, which narrows the field, and testing on your own data confirms the choice. Parameter count is not quality for your task. Fine-tuning every model is costly and premature. Someone else's task is not evidence about yours.
</details>

### Question 28
**Scenario:** A language model must answer employee questions from HR policies that change every week.

A. Fine-tune the model on the policies every week
B. Retrieval augmented generation over an Azure AI Search index
C. Put all the policies in the system prompt, whatever their size
D. Raise the temperature so the model draws on more knowledge

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAG keeps answers current by retrieving the latest documents at query time; updating the index is cheap. Weekly fine-tuning is slow, costly and still lags. A huge system prompt hits context and cost limits. Temperature controls randomness, not knowledge.
</details>

### Question 29
**Scenario:** A model must reply in a very specific company style and format. Long prompts with many examples work but are expensive, and RAG does not help because the issue is style, not knowledge.

A. Increase the number of retrieved documents
B. Switch to a smaller model with no other change, since smaller models follow formats more closely
C. Lower the max tokens setting
D. Fine-tune on example conversations in the required style

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Fine-tuning teaches consistent style and format, which can replace long few-shot prompts. More retrieved documents add knowledge, not style. A smaller model alone does not learn the style. Shorter output does not change its form.
</details>

### Question 30
**Scenario:** A team has three prompt variants for a summarisation flow and needs to know which performs best on a test dataset before release.

A. Run the variants in prompt flow against the dataset and score them with an evaluation flow
B. Ask a single reviewer to pick the variant that reads best on one example
C. Deploy all three to production and see which gets fewer complaints
D. Pick the longest prompt, since more instructions give better summaries

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prompt flow supports variants and batch runs over a dataset, and evaluation flows compute metrics so the variants can be compared. One reviewer on one example is anecdote. Production complaints arrive late and are biased. Prompt length is not a measure of quality.
</details>

---

## Where to go deeper

- [DP-100 cert page](../azure/dp-100/README.md) - notes, practice plan, strategy
- [AI-102 practice questions](azure-ai-engineer-ai-102.md) - the applied AI counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - measuring model quality
- [AI/ML systems topic index](../../build/README.md) - MLOps in context
- **[📖 DP-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)** - official skills outline
