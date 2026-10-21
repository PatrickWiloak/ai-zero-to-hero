# AWS Certified Machine Learning Engineer - Associate (MLA-C01) - Practice Questions

25 scenario-based questions for MLA-C01 prep. The current AWS ML credential, replacing the retired MLS-C01 (Specialty).

> **Cert page:** [exams/aws/associate/ml-engineer-mla-c01/](../aws/associate/ml-engineer-mla-c01/README.md)

---

### Question 1
**Scenario:** A team has 1 TB of training data in S3 and runs SageMaker training jobs. The job is read-bound. What feature optimizes I/O?

A. Use SageMaker FastFile mode or Pipe mode (stream data, no full download)
B. Use SageMaker File mode, which downloads the whole dataset to the instance volume before training starts
C. Move the data to an EBS volume attached to the training instance, so reads no longer cross the network
D. Use smaller instances so each one needs to read less of the dataset from S3 during the job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** File mode downloads everything before training (slow startup). FastFile / Pipe streams from S3 during training, faster startup and lower disk needs. FastFile is the modern default; Pipe is legacy.
</details>

---

### Question 2
**Scenario:** Hyperparameter tuning across 100 candidate configs - what SageMaker feature?

A. SageMaker Automatic Model Tuning (AMT) with Bayesian search
B. EC2 Spot Fleet, which launches many cheap instances to run the candidate configs in parallel
C. SageMaker Pipelines, which picks the next hyperparameter values from the results of earlier steps
D. Manual grid search via shell scripts that launch one training job per combination

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AMT runs hyperparameter tuning jobs with Bayesian, random, grid, or Hyperband strategies. Bayesian is most efficient for expensive training. Stop early if a config underperforms (early stopping).
</details>

---

### Question 3
**Scenario:** A batch inference job needs to score 10M records overnight. What endpoint type?

A. Lambda, invoking one function per record and relying on its concurrency to finish overnight
B. SageMaker Batch Transform, which runs distributed offline scoring
C. A real-time endpoint sized for the peak, sending the 10M requests one at a time over HTTPS
D. SageMaker Serverless inference, sending the records as concurrent requests with no endpoint to manage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch Transform is purpose-built for large-scale batch inference - distributed, fault-tolerant, no idle endpoint cost. Real-time endpoints have idle cost; Serverless has cold-start latency; Lambda has 15-min limit.
</details>

---

### Question 4
**Scenario:** A team needs A/B testing between model v1 and v2. Which SageMaker feature?

A. Two separate endpoints with manual routing in the client, switching a share of users over by hand during the test
B. SageMaker endpoints with multiple production variants and a traffic split (e.g., 90/10)
C. Inference Recommender, which splits live traffic across variants
D. A Lambda function with random routing that invokes either model's endpoint at the chosen ratio

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SageMaker endpoints support production variants - multiple models behind one endpoint with weighted traffic split. Built-in for A/B and canary patterns.
</details>

---

### Question 5
**Scenario:** Data drift detection on a deployed model - which SageMaker feature?

A. AWS Config, which records configuration changes and flags drift in the model's input data
B. CloudWatch only, using the built-in CPU and memory metrics to detect shifts in the input data
C. SageMaker Model Monitor, comparing live data against a training baseline
D. Amazon Macie, which scans the captured inference data and reports changes in feature distributions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Model Monitor watches input/output distributions for drift (data drift, model quality drift, bias drift, feature attribution drift). Captures inference data, compares against a baseline computed from training data, alerts on deviation.
</details>

---

### Question 6
**Scenario:** A team trains a custom image classifier. They want to use a pre-trained backbone (ResNet) and fine-tune the final layers. Which approach?

A. Train from scratch on your own images, which converges faster than starting from a pre-trained backbone
B. Use only Amazon Rekognition, since its stock labels can be fine-tuned layer by layer through the API
C. Custom hardware, such as Trainium instances, which replaces the need for pre-trained weights
D. Transfer learning with a pre-trained model from SageMaker JumpStart

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Transfer learning is the standard pattern for image/NLP - start with a pre-trained backbone, fine-tune on your task. JumpStart provides 500+ pre-trained models with one-click deployment and fine-tuning.
</details>

---

### Question 7
**Scenario:** Data labeling at scale - which AWS service?

A. AWS Lambda, running a function that applies labels as objects land in S3
B. SageMaker Ground Truth (managed labeling with human workforce + ML-assisted labeling)
C. SageMaker Studio, whose notebooks include a built-in labeling workforce
D. Amazon Mechanical Turk only, where you build the task UI, quality checks, and routing yourself

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ground Truth manages labeling jobs - public workforce (Mechanical Turk), private workforce (your employees), or vendors. ML-assisted active labeling reduces cost (~70%) by auto-labeling high-confidence items.
</details>

---

### Question 8
**Scenario:** A SageMaker Pipelines pipeline orchestrates: preprocess → train → evaluate → register → deploy. What's the value vs raw scripts?

A. Versioned, reproducible, lineage-tracked, integrated with Model Registry, and supports conditional steps
B. Faster execution, because pipeline steps always run on larger instances
C. They're identical, since a pipeline just runs the same script commands in the same order
D. Lower cost, because the service runs the steps for free and only bills for the storage used, and the compute savings are guaranteed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Pipelines provide ML-aware orchestration with experiment tracking, model lineage, conditional logic, and Model Registry integration. Better than raw scripts for production ML reliability.
</details>

---

### Question 9
**Scenario:** A model needs to serve predictions in <100ms. What endpoint configuration?

A. Batch Transform, which starts a job per request and writes results to S3
B. Lambda only, hosting the model in the function package with provisioned concurrency for every request
C. Serverless inference, which has no cold starts and so always answers in under a hundred milliseconds
D. Real-time endpoint with provisioned instances; enable auto-scaling on InvocationsPerInstance

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Real-time endpoints with appropriately-sized instances meet sub-100ms latency. Auto-scaling adapts to traffic. Serverless has variable cold start (could be slower). Batch is high-throughput, not low-latency.
</details>

---

### Question 10
**Scenario:** Which is the AWS-managed feature store?

A. Amazon RDS, a managed relational database that stores features for training and serving
B. SageMaker Feature Store, with online and offline stores
C. DynamoDB, which is the managed feature store with offline S3 storage built in
D. ElasticSearch, which indexes the features for low-latency serving and training exports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SageMaker Feature Store is the managed feature store: online (low-latency lookup) + offline (S3-backed for training). Solves train/serve skew by ensuring features are computed identically for both.
</details>

---

### Question 11
**Scenario:** A model is in production. Its accuracy slowly degrades over weeks. What's the most likely cause?

A. The model was always broken, and the degradation only became visible once enough traffic had arrived
B. Hardware failure on the instance, which slowly lowers prediction accuracy as the GPU memory degrades
C. Network latency between the client and the endpoint, which makes responses arrive after the timeout
D. Concept drift (the relationship between features and target shifts over time, e.g., user preferences change)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Concept drift = the world changes, so a model trained on yesterday's patterns underperforms. Mitigated by periodic retraining, online learning, or change-detection alarms (Model Monitor).
</details>

---

### Question 12
**Scenario:** A model trained on US data underperforms in EU markets. What's the issue?

A. Model size, since a model trained on US data is too large to generalize to a smaller EU population
B. The model is broken, because the training job failed to converge when it was run in the US region
C. Network latency from EU users to a US-hosted endpoint, which causes timeouts and bad predictions
D. Distribution shift / data drift between training and deployment populations

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Distribution shift = the deployed population differs from the training population (different demographics, behaviors, etc.). Mitigation: train per-region, ensemble, fine-tune on local data, or domain adaptation techniques.
</details>

---

### Question 13
**Scenario:** SageMaker Clarify is for:

A. Bias detection in data and models, plus model explainability (SHAP values)
B. Encryption of training data and model artifacts with KMS keys
C. Cost optimization, recommending cheaper instance types for training and hosting based on past usage
D. Networking, configuring VPC endpoints and security groups for training containers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Clarify analyzes datasets and models for bias across protected attributes, and provides SHAP-based explanations of individual predictions. Required for high-stakes regulated applications.
</details>

---

### Question 14
**Scenario:** Multi-model endpoint vs multiple single-model endpoints?

A. Multi-model endpoints hold only a handful of models, so they suit high-traffic models
B. They're identical, since each model type bills per instance hour and loads every model at endpoint start
C. A multi-model endpoint hosts many models on shared compute (low traffic per model = cost savings)
D. Multi-model is always slower, because each request must reload the model from S3 before it can run, however often it is called

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Multi-model endpoints (MME) host hundreds of models on shared instances - models loaded on demand. Best when you have many low-traffic models (per-customer model). Bigger ratio of models to instances = bigger savings.
</details>

---

### Question 15
**Scenario:** Bedrock vs SageMaker - high-level distinction?

A. Bedrock is for non-ML workloads such as data pipelines, while SageMaker is where all machine learning runs
B. Bedrock = managed API access to foundation models with no hosting; SageMaker = full ML platform for custom training, hosting, MLOps
C. Identical, since the two services host the same models and differ only in console layout and pricing
D. SageMaker only does training and cannot host a model; Bedrock only does inference on its own models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bedrock = "I want to call Claude/Llama via API." SageMaker = "I want to train, tune, deploy, and monitor my own models" (with optional access to foundation models via JumpStart). They complement each other - many architectures use both.
</details>

---

### Question 16
**Scenario:** A team trains a model that exceeds memory on a single GPU. The dataset is 800 GB. Best SageMaker training pattern?

A. SageMaker distributed training: data parallel (sharded data, replicated model) for moderate models, model parallel (sharded model) when the model itself is the bottleneck
B. Local mode only, since it runs the training container on the notebook instance's GPU and streams the 800 GB dataset from S3 without needing more memory
C. Train on a smaller sample of the data so that the model fits in a single GPU's memory, accepting the accuracy loss and avoiding any distributed setup
D. An inference-only instance type with a large amount of RAM, which can train models larger than a single GPU can hold in memory

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SageMaker offers SMDDP (data parallel) and SMP (model parallel) libraries. Choose based on what's saturating: data volume → data parallel, model size → model parallel. Both can stack for large LLMs. Local mode is for dev iteration only.
</details>

---

### Question 17
**Scenario:** A model in production drifts after 6 months - predictions degrade as inputs shift. Which feature catches this?

A. CloudTrail, which records every API call to the endpoint and flags inputs whose values drift from training, then sends the findings to an SNS topic for the on-call team
B. Manual quarterly review of a sample of predictions by a data scientist, who files a ticket
C. SageMaker Model Monitor with data quality and model quality baselines, scheduled to compare live traffic with the baseline and emit CloudWatch alerts
D. AWS Config rules that report a violation when the input data distribution changes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Model Monitor detects data drift (input distribution change), model quality drift (accuracy regression on labeled subset), bias drift, feature attribution drift. Run on an endpoint with a captured baseline.
</details>

---

### Question 18
**Scenario:** A real-time endpoint must scale from 1-200 instances based on traffic with a sub-100 ms p99 SLA. Best configuration?

A. A real-time endpoint with auto-scaling on a target-tracking policy (e.g., InvocationsPerInstance), a minimum instance count above zero, and an instance type matched to the model's latency profile
B. Batch transform, which scales to hundreds of instances automatically and is the cheapest way to hold a sub-100 ms p99 for interactive users, returning results when the whole job finishes, with no endpoint left running between jobs
C. A static fleet of 200 instances held permanently, which guarantees capacity for the peak and removes any need for scaling policies or scale-out delay, at a fixed hourly cost
D. Lambda with the model in a layer, which scales to thousands of concurrent executions and keeps the p99 low because functions never start cold with a large model

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Real-time endpoints support target-tracking auto-scaling. A sensible minimum instance count and scale-out target keep latency stable while capacity grows. For very bursty workloads, async endpoints buffer to SQS-style queue. Lambda has cold-start and 250 MB layer limits incompatible with most ML models.
</details>

---

### Question 19
**Scenario:** Cost optimization: workload runs predictable, mixed batch + real-time. Which combination saves most?

A. On-demand only, which keeps full flexibility and avoids any commitment or interruption risk, at the cost of paying list price for a baseline that never changes
B. Reserved EC2 instances bought for the whole fleet, applied automatically to every SageMaker instance and endpoint
C. SageMaker Savings Plans for steady usage, managed Spot training with checkpoints, and Multi-Model Endpoints for low-traffic models
D. Disable everything outside business hours and run batch jobs by hand, stopping real-time traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Savings Plans cut steady-state cost ~30-60%. Managed Spot Training saves up to 90% on interruptible jobs (training with checkpointing). Multi-Model Endpoints amortize host cost across many small models. Layer the levers.
</details>

---

### Question 20
**Scenario:** Bedrock - which feature lets you ground responses on private documents without managing a vector store?

A. Bedrock Knowledge Bases - managed RAG that ingests S3 documents, chunks and embeds them, and retrieves from a vector store at inference
B. Bedrock Studio, a collaborative workspace for building and sharing prompt-based apps; you would still need to create and populate a vector store yourself
C. Bedrock Agents, which orchestrate multistep tasks by calling APIs you describe, and which do not by themselves ingest and index your documents
D. Bedrock Guardrails, which filter harmful content and sensitive information in prompts and responses but do not retrieve documents

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Knowledge Bases is Bedrock's managed RAG. You point at an S3 bucket, pick an embedding model and vector store, and Bedrock handles ingestion, chunking, retrieval, and re-ranking. Skip if you need full control over the retrieval pipeline.
</details>

---

### Question 21
**Scenario:** Bias detection during training - which SageMaker feature?

A. Model Monitor only, which compares the live endpoint's input data against a baseline once the model is deployed in production
B. Ground Truth, which manages human labeling jobs for training data and reports annotator agreement for each batch
C. SageMaker Clarify: measures pre-training bias (class and label imbalance), post-training bias (predictions varying by sensitive feature), and explainability (SHAP)
D. Pipelines, which orchestrates preprocessing, training, and evaluation steps as a versioned DAG and registers the resulting model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Clarify measures bias in data and model, with multiple metrics (DPL, KL divergence, etc.). Output is a report tied to the training job. Model Monitor handles drift in production. Ground Truth labels data.
</details>

---

### Question 22
**Scenario:** A team versions training code, hyperparameters, and model artifacts for reproducibility. Which native combo?

A. S3 only, with versioning enabled on the bucket so every object keeps its earlier versions, but nothing ties code, parameters, and artifacts together
B. CodeCommit only, committing the training scripts and parameter files so each run can be rebuilt, but model artifacts and metrics stay untracked
C. Manual notebook saves with dated file names, kept in the team's shared Studio space and copied to S3 whenever someone remembers
D. SageMaker Pipelines for the workflow, Model Registry for versioned models with approval, git for code, and Experiments for run metrics

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pipelines + Model Registry is the SageMaker MLOps backbone. Pipelines defines the workflow as code; Model Registry tracks versions with approval gates feeding deployment. Experiments captures metrics + hyperparams. Git holds the code.
</details>

---

### Question 23
**Scenario:** Data labeling at scale (50,000 images for object detection) with quality control?

A. Hire freelancers offline to draw boxes in a drawing tool and send the files back by email, with a manager spot-checking a few batches
B. Manual emails to staff with image batches attached and a spreadsheet to collect their answers, reviewed by one person at the end
C. SageMaker Ground Truth with built-in workflows, automated labeling (active learning) to cut cost, and consensus review across annotators, plus a private workforce option for sensitive images
D. Bedrock, whose foundation models label images through the API; you would still design the consensus and review workflow yourself

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Ground Truth supports public (Mechanical Turk), private, or vendor workforces. Active learning trains a small model that auto-labels easy examples and routes hard cases to humans, cutting labeling cost. Quality controls: consensus across N annotators.
</details>

---

### Question 24
**Scenario:** A team wants reproducible feature engineering across training and serving. Best AWS service?

A. S3 only, storing the engineered features as Parquet files that each side transforms itself
B. RDS, a relational database holding the features as table columns that training and serving code each query, with no feature versioning or lineage between the two
C. DynamoDB, a key-value store serving features at low latency, with the training data exported separately and the logic duplicated
D. SageMaker Feature Store: offline storage for training and online storage for low-latency inference, with consistent and versioned features

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Feature Store solves the train/serve skew problem. Same features, same logic, queryable at training time (offline) and at inference (online). Versioned, governed. Critical for production ML at scale.
</details>

---

### Question 25
**Scenario:** Securing a SageMaker training job that processes PII?

A. Public S3 buckets with open read access, so the training job can pull the PII without any credentials
B. VPC-only training with no internet access (use VPC endpoints), KMS-encrypted data and artifacts, least-privilege IAM roles, network isolation, and inter-container traffic encryption
C. Open security groups on the training instances, so that data scientists can reach the containers while debugging
D. Disable encryption on the training volumes and artifacts to avoid the performance overhead of encrypting large datasets, since the job runs in a private subnet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Defense in depth: network isolation (no egress), KMS at rest, in-flight encryption, scoped IAM. Network isolation flag prevents the training container from making outbound calls. VPC endpoints keep S3/STS traffic on the AWS network.
</details>

---

## Scoring guide

- **22-25:** Schedule the exam.
- **17-21:** Re-read SageMaker / Bedrock sections.
- **<17:** Hands-on with SageMaker Studio + re-read fact-sheet.

MLA-C01: 65 questions, 130 minutes, 720/1000 passing. Tests applied SageMaker / Bedrock judgment. Less algorithmic depth than MLS-C01, more MLOps + GenAI focus.
