---
last-updated: 2026-10-22
difficulty: advanced
---

# AWS Certified Machine Learning - Specialty (MLS-C01) - Practice Questions

30 questions for MLS-C01 prep, weighted toward modeling (36%), exploratory data analysis (24%), then data engineering and ML implementation and operations (20% each).

MLS-C01 is retired: AWS delivered the exam for the last time on March 31, 2026, and existing credentials stay valid for three years from the date earned. New candidates should prepare for the Machine Learning Engineer Associate instead; this bank is kept for review.

> **Cert page:** [exams/aws/specialty/machine-learning-mls-c01/](../aws/specialty/machine-learning-mls-c01/README.md)

---

### Question 1
**Scenario:** A binary classifier must catch as many fraudulent transactions as possible, accepting some false alarms.

A. Optimize training speed, since fraud models must be retrained often on fresh transactions
B. Optimize precision, so that nearly every flagged transaction turns out to be real fraud
C. Optimize accuracy, which counts every correct prediction and so reflects fraud detection well
D. Optimize recall, and tune the decision threshold accordingly

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recall is the fraction of actual fraud you catch, which is what "miss as few as possible" means. Precision is the cost you are choosing to pay in false positives. Accuracy is meaningless at 0.1% fraud, where predicting "not fraud" always scores 99.9%.
</details>

---

### Question 2
**Scenario:** Training accuracy is 99% and validation accuracy is 70%.

A. Underfitting; use a larger model with more layers so it can fit the validation set better
B. Overfitting; add regularization, dropout, more data, or early stopping
C. The learning rate is too low, so training has not converged
D. The data is corrupt, since the validation labels must have been shuffled during upload

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A large train-validation gap is the definition of overfitting: the model memorized the training set. Regularization, more data, simpler models, and early stopping all attack it. Underfitting shows as poor performance on both sets.
</details>

---

### Question 3
**Scenario:** A categorical feature has 10,000 distinct values.

A. One-hot encode it into 10,000 binary columns, which keeps every category separate and works for every model
B. Drop it, since a feature with that many values cannot carry useful signal for any model
C. Use target encoding, hashing, or a learned embedding, depending on the model and how it is trained
D. Label encode it for a linear model, treating each integer as a magnitude

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** One-hot at that cardinality creates a huge sparse matrix. Hashing bounds the dimension, target encoding compresses to a statistic (with care to avoid leakage, using out-of-fold encoding), and embeddings learn a dense representation. Label encoding imposes a false ordinal relationship on a linear model.
</details>

---

### Question 4
**Scenario:** SageMaker must serve a model with variable, spiky traffic and scale to zero between bursts.

A. An EC2 instance running the model container behind a load balancer sized for the peak
B. Serverless Inference, which scales with traffic and down to zero
C. A real-time endpoint with a fixed instance count
D. Batch Transform, started on a schedule to process the requests that accumulated since the last run

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Serverless Inference scales with traffic and to zero, at the cost of cold starts. Real-time endpoints give consistent latency but bill continuously. Asynchronous Inference is the third option, suited to large payloads and long processing where a queue is acceptable.
</details>

---

### Question 5
**Scenario:** Two model versions must be compared on live traffic without risking full exposure.

A. Deploy the versions behind one endpoint as production variants with weighted traffic, or use a shadow variant
B. Two separate endpoints, with manual switching of the client's URL between them during the test
C. Offline evaluation only, using a held-out test set, since live traffic cannot be sampled safely
D. Deploy the new one fully, then roll back if the error rate rises over the old model's baseline

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Production variants split traffic by weight behind a single endpoint, so rollback is a weight change. Shadow testing sends a copy of traffic to the new variant without returning its responses, which measures behavior with zero user risk.
</details>

---

### Question 6
**Scenario:** A dataset is highly imbalanced at 100:1.

A. Combine resampling (SMOTE or undersampling), class weights, and precision-recall evaluation rather than accuracy
B. Do nothing, since a sufficiently large dataset lets the model learn the minority class unaided
C. Use a bigger model, because more capacity lets it fit the rare class without any other change
D. Collect more of the majority class, which rebalances the ratio once the data volume doubles

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Imbalance affects both training and evaluation, so it needs handling in both places. Apply resampling only to the training split, never to validation or test, or your measured performance will be optimistic and wrong.
</details>

---

### Question 7
**Scenario:** Hyperparameter tuning must find good values efficiently on an expensive training job.

A. Random guessing of values within the documented ranges, repeated until the metric looks fine
B. Manual tuning by an engineer, who edits the hyperparameters after reading each job's logs
C. Grid search over every combination of values, which is exhaustive and so finds the best result quickly and cheaply
D. SageMaker automatic model tuning with Bayesian search, early stopping, and a limit on parallel jobs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Bayesian optimization uses the results of previous trials to choose the next configuration, which finds good values in far fewer runs than grid search on an expensive objective. Early stopping kills unpromising trials, which is where the remaining savings come from.
</details>

---

### Question 8
**Scenario:** Feature values computed at training time differ from those computed at inference time.

A. Training-serving skew: use a feature store or shared transformation code so each path computes features identically
B. Increase model size so it can learn to compensate for the differences in feature values
C. Retrain more often on fresher data, since every new training run will bring the two feature computations back into line and fix the gap
D. Ignore it, because small differences in feature values average out over many predictions and rarely move the results by much

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Skew produces a model that performs well offline and badly in production, and it is one of the most common causes of that gap. SageMaker Feature Store, or at minimum a single shared transformation library, removes the possibility of the two paths diverging.
</details>

---

### Question 9
**Scenario:** Which SageMaker capability detects data drift on a deployed endpoint?

A. CloudWatch alarms on CPU and memory utilization, which rise whenever the input data distribution shifts
B. Clarify only, run once at deployment time to compare the live feature statistics with the training set
C. Batch Transform jobs that re-score the endpoint's recent traffic and report any change in the predictions
D. Model Monitor with a baseline from the training data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Model Monitor captures endpoint traffic, compares statistics against a baseline, and reports violations for data quality, model quality, bias drift, and feature attribution drift. Clarify computes bias and explainability, and its outputs feed two of those monitor types.
</details>

---

### Question 10
**Scenario:** A time series must be split for validation.

A. Chronological split, training on earlier data and validating on later data, or rolling-origin cross-validation
B. Random shuffle split, so both sets contain examples from every period of the series
C. Stratified split on the target, so that each set keeps the same share of high and low values
D. K-fold with shuffling, repeated five times so every record is used for validation once

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Random splitting on time series lets the model see the future, which produces excellent validation scores and a useless model. Chronological splitting and rolling-origin cross-validation preserve the causal order, and lag features must be computed with the same care.
</details>

---

### Question 11
**Scenario:** Large training data lives in S3 and the job spends most of its time downloading.

A. Use a bigger instance with more vCPUs, since download time scales down with compute
B. Compress with gzip only, then keep File mode so that the job still copies every object at the start
C. Use Pipe or FastFile mode to stream from S3, or FSx for Lustre for repeated access to the data
D. Reduce the dataset by dropping older partitions, accepting a smaller training set

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** File mode copies the whole dataset before training starts, which dominates the wall clock for large data. Streaming modes overlap download with compute, and FSx for Lustre is the right answer when many jobs repeatedly read the same dataset.
</details>

---

### Question 12
**Scenario:** A model must explain individual predictions to satisfy a regulator.

A. SageMaker Clarify with SHAP values for feature attribution
B. Model size, reported as the parameter count, which shows regulators how complex each decision was
C. The confusion matrix on the test set, which lists the true and false predictions for each applicant
D. Training loss curves, which show the reasons behind each prediction over the training epochs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SHAP attributes a prediction to its input features in a locally accurate way, which is what "why did this application get declined" requires. Aggregate performance metrics describe the model overall and say nothing about an individual decision.
</details>

---

### Question 13
**Scenario:** Which algorithm suits anomaly detection on streaming numeric data?

A. Linear Learner, a supervised algorithm for regression and classification
B. Random Cut Forest, an unsupervised anomaly detector
C. Seq2Seq, a sequence-to-sequence model for translation and text summarization
D. XGBoost, a gradient boosted tree algorithm that needs labeled examples

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Random Cut Forest is the built-in unsupervised anomaly detection algorithm and is available both in SageMaker and in Kinesis Data Analytics for streaming. The supervised algorithms need labeled anomalies, which is precisely what you usually lack.
</details>

---

### Question 14
**Scenario:** Training must use spot capacity without losing progress on interruption.

A. Restart from scratch on interruption, accepting that a long job may never finish
B. On-demand only, at a higher price
C. Managed spot training with checkpointing to S3
D. Reserved instances, which guarantee capacity for a one-year term and so need no checkpoints

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Managed spot training can cut costs substantially, and checkpointing is what makes interruption survivable: the job resumes from the last checkpoint rather than the beginning. Without checkpoints, a long job on spot is a gamble that gets worse the longer it runs.
</details>

---

### Question 15
**Scenario:** An ML pipeline must run data prep, training, evaluation, and conditional registration.

A. A shell script run by cron that calls each stage in order and emails the log to the team
B. SageMaker Pipelines with steps and a condition step that gates model registration on the metric
C. A single notebook with all four stages in separate cells, re-run by hand after every data update by whoever is on call
D. Manual steps in a runbook, with a reviewer approving each stage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pipelines gives a versioned DAG with lineage tracking and caching, and the condition step is what turns "we evaluated it" into an enforced quality gate. Notebooks are for exploration; they do not give reproducibility or auditability.
</details>

---

### Question 16
**Scenario:** A retailer streams clickstream events as JSON and wants them landed in Amazon S3 as Parquet files for later training, with as little custom code and infrastructure to run as possible.

A. Run an EC2 fleet that consumes the stream, converts each batch with a script, and writes the files to S3
B. Have a Lambda function write each event to S3 as its own JSON object, then convert the bucket weekly
C. Use Amazon Data Firehose with record format conversion to Parquet, using a schema in the Glue Data Catalog
D. Load the events into Amazon RDS first, then export the tables to S3 as Parquet once a night

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Firehose is a managed delivery stream that can convert incoming JSON to Parquet or ORC using a table schema from the AWS Glue Data Catalog before writing to S3, so there is nothing to run. An EC2 fleet and Lambda plus a weekly job are custom code to maintain, and millions of tiny objects are slow to read. A relational database is the wrong store for a clickstream landing zone.
</details>

---

### Question 17
**Scenario:** A data scientist wants to explore several terabytes of partitioned Parquet data in S3 using SQL, without loading it into a database or managing any servers.

A. Copy the data into an Amazon Redshift cluster and run the queries there after each load
B. Use Amazon Athena with the tables defined in the AWS Glue Data Catalog
C. Launch an Amazon EMR cluster with Hive and keep it running for the analysis
D. Download the files to a SageMaker notebook instance and query them with pandas

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Athena is serverless SQL directly over data in S3, priced per data scanned, and Parquet with partitions keeps that scan small. Redshift and EMR need data loading or a cluster to manage. Pulling terabytes into one notebook's memory is not practical.
</details>

---

### Question 18
**Scenario:** Before a training project starts, the security team must find out whether any objects in a large S3 data lake contain personal data such as names or credit card numbers.

A. Amazon Inspector, which scans the bucket contents for sensitive data and known software flaws
B. AWS Config, which records the configuration of each bucket and flags any personal data inside it
C. Amazon GuardDuty, which reads every object and reports those that contain personal data
D. Amazon Macie, which uses pattern matching and ML to discover sensitive data in S3 objects

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Macie is the AWS service for discovering and classifying sensitive data such as PII in S3. Inspector assesses workloads for vulnerabilities, Config tracks resource configuration rather than object contents, and GuardDuty detects threats from logs and activity.
</details>

---

### Question 19
**Scenario:** A numeric feature with a strongly right-skewed distribution has about 4% missing values, scattered at random across rows. The dataset is not large, so dropping rows is costly.

A. Drop every row with a missing value, since imputation always adds bias to the trained model
B. Replace the missing values with zero, since zero marks clearly where data was not recorded
C. Impute with the median, which is not pulled by the long tail, and consider a missing-value flag
D. Impute with the mean, since the mean uses every observed value and so carries more information

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** For a skewed feature the median is a robust central value, while the mean is dragged toward the tail. Adding an indicator column keeps the fact that a value was missing. Dropping rows wastes scarce data, and zero is a real value that distorts the distribution.
</details>

---

### Question 20
**Scenario:** A linear regression model uses household income as a feature. Income is heavily right-skewed with a long tail of very high values, and residuals are poorly behaved.

A. One-hot encode income into one column for every distinct value that appears in the data
B. Apply a log transformation to income to compress the tail and make the relationship more linear
C. Remove every household above the 90th percentile of income from the training data entirely
D. Multiply income by a constant so that all of its values fall between zero and one hundred

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A log transform reduces right skew and often linearizes multiplicative relationships, which suits linear models. One-hot encoding a continuous value makes no sense, dropping the top 10% throws away real data, and scaling by a constant leaves the shape of the distribution unchanged.
</details>

---

### Question 21
**Scenario:** A team runs k-means clustering on customer data where age ranges from 18 to 90 and annual spend ranges from 0 to 500,000. The clusters split almost entirely on spend.

A. Standardize or normalize the features so that each contributes on a comparable scale
B. Increase the number of clusters until age begins to influence how customers are assigned
C. Remove the spend feature, since it is the one that dominates the distance calculation
D. Run k-means for many more iterations so that the age feature has time to take effect

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Distance-based methods like k-means and k-nearest neighbors are dominated by features with large ranges, so features should be put on a comparable scale first. More clusters or iterations do not change the distance calculation, and dropping spend removes a useful feature to hide the scaling problem.
</details>

---

### Question 22
**Scenario:** A regression model must be explained to auditors through its coefficients, but two features are highly correlated and their coefficients change sign between training runs.

A. Increase the size of the test set so that the coefficients are measured with more precision
B. Add an interaction term between the two features so that the model captures both of them
C. Switch to a deep neural network, since it handles correlated features without any problems
D. Check correlation or variance inflation factors, then drop or combine one of the features

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multicollinearity makes individual coefficients unstable and hard to interpret even when predictions are fine. Measuring it (correlation matrix, VIF) and then dropping one feature, combining them, or using PCA restores stable coefficients. A larger test set does not affect training, an interaction term adds more correlation, and a neural network is harder to explain, not easier.
</details>

---

### Question 23
**Scenario:** A company needs to classify millions of short product descriptions into categories and wants a SageMaker built-in algorithm that trains quickly on text.

A. K-means, which groups the descriptions into categories without needing any labels
B. DeepAR, which learns the sequence of words in each description to predict its label
C. BlazingText in supervised mode, which provides fast text classification
D. Linear Learner on the raw description strings, without any feature extraction step

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** BlazingText's supervised mode is a fast text classifier built for this kind of workload. K-means is unsupervised and cannot learn given labels. DeepAR forecasts time series, and Linear Learner needs numeric feature vectors, not raw strings.
</details>

---

### Question 24
**Scenario:** A media site wants to predict clicks from very sparse, high-dimensional data: user ID, item ID and a few context fields, most combinations of which never appear in training.

A. K-nearest neighbors, which finds similar users by comparing their full rows of raw data
B. Factorization Machines, which models interactions between features in sparse data
C. Random Cut Forest, which scores each user and item pair for how unusual it looks
D. Principal Component Analysis, which predicts clicks from the main directions of variation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Factorization Machines are designed for sparse datasets such as click prediction and recommendations, learning interactions between features even for combinations seen rarely. KNN struggles in very sparse high-dimensional space, Random Cut Forest detects anomalies, and PCA reduces dimensions rather than predicting a target.
</details>

---

### Question 25
**Scenario:** A delivery-time model is evaluated by a business that cares about the typical size of an error and does not want a handful of extreme late deliveries to dominate the metric.

A. RMSE, because squaring the errors gives more weight to the typical size of each prediction error
B. R squared, because it reports the error in minutes in a form that the business can read directly
C. Accuracy, because it counts how many predicted delivery times exactly match the actual times
D. MAE, because it averages absolute errors, so large outliers are not given extra weight

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Mean absolute error treats every error linearly, which keeps a few extreme cases from dominating. RMSE squares errors and so is more sensitive to outliers. R squared is a proportion of variance explained, not an error in minutes, and exact-match accuracy is meaningless for a continuous target.
</details>

---

### Question 26
**Scenario:** While training a neural network, the training loss jumps up and down sharply from epoch to epoch and sometimes grows instead of falling.

A. Reduce the learning rate, since steps that are too large overshoot the minimum
B. Add more layers to the network so it has the capacity to fit the training data
C. Increase the number of epochs so that the loss has more time to settle down
D. Remove the validation set so all data goes to training and the loss becomes steadier

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Oscillating or diverging loss is the classic sign of a learning rate that is too high. More capacity, more epochs, or more data do not fix steps that overshoot, and removing the validation set only loses the ability to detect overfitting.
</details>

---

### Question 27
**Scenario:** A team uses k-means to segment customers but does not know how many segments to use.

A. Pick the value of k that gives the lowest training error, since more clusters always fit better
B. Set k equal to the number of features, since each feature should produce one segment
C. Plot within-cluster sum of squares against k and choose the point where gains level off
D. Use k equal to the number of customers, so every customer becomes a segment of their own

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The elbow method looks for where adding clusters stops giving a meaningful drop in within-cluster variance, which balances fit against simplicity. The lowest error always comes at the largest k, which is useless, as is one cluster per customer. The number of features has no relationship to the number of segments.
</details>

---

### Question 28
**Scenario:** A SaaS provider trains a separate model for each of 2,000 customers. Each model gets only a few requests per hour, and keeping 2,000 endpoints running is too expensive.

A. Run a single large instance per customer and stop the instances outside business hours
B. Use a SageMaker multi-model endpoint that loads models from S3 on demand behind one endpoint
C. Use Batch Transform for every request, since it starts compute only when there is data to score
D. Combine all 2,000 models into one ensemble that averages their predictions for each request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-model endpoints host many models on shared instances, loading each from S3 when invoked and caching popular ones, which suits many low-traffic models. Per-customer instances keep the cost problem. Batch Transform is for offline scoring, not request-time inference, and averaging customers' models gives each customer the wrong model.
</details>

---

### Question 29
**Scenario:** Once a month a bank must score 50 million customer records in S3 for churn risk. Nobody needs predictions in real time.

A. Deploy a real-time endpoint and call it once for each record from a script on a laptop
B. Use SageMaker Serverless Inference and send the records one at a time over a few days
C. Load the model into a notebook instance and score the records in memory in a single loop
D. Run a SageMaker Batch Transform job that reads from S3 and writes the results back to S3

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Batch Transform runs inference over a whole dataset in S3, provisions compute only for the job, and writes results back to S3, which fits periodic offline scoring. A persistent or serverless endpoint called record by record is slow and costly for 50 million rows, and a notebook loop does not scale.
</details>

---

### Question 30
**Scenario:** A healthcare company requires that SageMaker training containers have no internet access, while still reading training data from S3.

A. Remove the IAM role from the training job so that the container cannot reach anything outside
B. Encrypt the S3 bucket with a KMS key so that data cannot leave over the internet during training
C. Run training in a private VPC subnet with an S3 VPC endpoint, and enable network isolation
D. Use a public subnet with a security group that blocks all inbound traffic to the instances

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Placing the job in private subnets with an S3 gateway endpoint keeps S3 access off the internet, and network isolation blocks outbound calls from the training container. Removing the role breaks access to S3 entirely, encryption protects data at rest rather than controlling network paths, and blocking inbound traffic still allows outbound internet access.
</details>

---

## Where to go deeper

- [MLS-C01 cert page](../aws/specialty/machine-learning-mls-c01/README.md) - notes, practice plan, strategy
- [ML Engineer Associate practice questions](aws-ml-engineer-associate.md) - the current-generation exam
- [DP-100 practice questions](azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../build/README.md) - MLOps across the repo
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
