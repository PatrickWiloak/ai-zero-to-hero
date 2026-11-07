# Databricks Certified Machine Learning Associate

## Exam Overview

The Databricks Certified Machine Learning Associate certification validates foundational knowledge of machine learning on the Databricks Lakehouse Platform. This certification demonstrates proficiency in using MLflow, Spark MLlib, and Databricks tools for building, tracking, and deploying machine learning models.

**Exam Details:**
- **Exam Code:** Databricks Certified Machine Learning Associate
- **Duration:** 90 minutes
- **Number of Questions:** 48 scored multiple-choice and multiple-selection questions (up to 10 more unscored)
- **Passing Score:** Not published by Databricks
- **Cost:** $200 USD
- **Delivery:** Online proctored or test center
- **Validity:** 2 years
- **Prerequisites:** None (6+ months ML experience on Databricks recommended)

## Exam Domains

> **Checked 2026-11-06** against the [official exam page](https://www.databricks.com/learn/certification/machine-learning-associate) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf). The exam page calls Section 2 "ML Workflows"; the guide calls it "Data Processing". The notes, fact sheet body, practice plan and scenarios in this folder still follow the old five-domain outline, so use the list below as the source of truth for what is tested.

### Section 1: Databricks Machine Learning (38%)
- MLOps strategy best practices and the advantages of ML runtimes
- AutoML: model and feature selection, and what it adds to model development
- Feature store tables in Unity Catalog: create, write, train and score; account level vs workspace level; online vs offline tables
- MLflow: find the best run with the Client API, log metrics, artifacts and models manually, read the MLflow UI
- Unity Catalog model registry: register a model, why it beats the workspace registry, set or remove tags
- Promoting code vs promoting models; promoting a challenger to champion with aliases

### Section 2: Data Processing (19%)
- Summary statistics with `.summary()` or dbutils data summaries
- Removing outliers by standard deviation or IQR
- Visualizing and comparing categorical and continuous features
- Imputing missing values with the mean, median or mode, and choosing between them
- One-hot encoding: how to use it and which models or data sets suit it
- When a log scale transformation is appropriate

### Section 3: Model Development (31%)
- Choosing an algorithm for a scenario, and mitigating data imbalance
- Estimators vs transformers, and building a training pipeline
- Hyperopt `fmin`; random, grid and Bayesian search; parallelizing single-node models for tuning
- Cross-validation vs a train-validation split, and counting the models trained by grid search with cross-validation
- Classification metrics (F1, Log Loss, ROC/AUC) and regression metrics (RMSE, MAE, R-squared); choosing one for a scenario
- Exponentiating log-transformed variables before calculating metrics or interpreting predictions
- Model complexity and the bias-variance tradeoff

### Section 4: Model Deployment (12%)
- Serving approaches: batch, realtime and streaming
- Deploying a custom model to a model endpoint
- Batch inference with pandas
- Streaming inference with Delta Live Tables
- Deploying and querying a model for realtime inference; splitting data between endpoints

## Key Concepts to Master

### MLflow
- Tracking API (log_param, log_metric, log_artifact, log_model)
- Experiment organization and comparison
- Model Registry workflow (staging, production, archived)
- Model flavors (sklearn, spark, tensorflow, pytorch)
- Model serving basics
- Autologging capabilities

### Feature Engineering
- Numerical feature scaling (StandardScaler, MinMaxScaler)
- Categorical encoding (StringIndexer, OneHotEncoder)
- Feature selection techniques
- Handling missing values
- Feature importance analysis
- Time-series feature engineering

### Model Evaluation
- Classification metrics (confusion matrix, ROC, precision-recall)
- Regression metrics (RMSE, MAE, R-squared)
- Model comparison techniques
- Visualization of model performance

## Study Approach

### Phase 1: Foundation (Week 1-2)
1. Review ML fundamentals (supervised/unsupervised learning, bias-variance)
2. Get comfortable with Databricks ML Runtime
3. Learn MLflow tracking and experiment management
4. Understand the Feature Store concept

### Phase 2: Core Skills (Week 3-4)
1. Practice building Spark MLlib pipelines
2. Learn hyperparameter tuning with Hyperopt
3. Study deep learning basics on Databricks
4. Practice model evaluation and selection

### Phase 3: Exam Prep (Week 5-6)
1. Take practice exams and review incorrect answers
2. Focus on MLflow and ML workflow (58% of exam)
3. Review scaling and distributed ML concepts
4. Time yourself on practice questions

## Study Resources

- **[Databricks Academy](https://www.databricks.com/learn)** - ML learning paths
- **[Exam Guide](https://www.databricks.com/learn/certification/machine-learning-associate)** - Official exam page
- **[MLflow Documentation](https://mlflow.org/docs/latest/index.html)** - MLflow reference
- **[Spark MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)** - Spark ML reference
- **[Databricks ML Documentation](https://docs.databricks.com/en/machine-learning/index.html)** - Databricks ML docs

## Tips for Success

1. **Section 1 is the biggest** - Databricks Machine Learning (MLflow, Feature Store, AutoML, Unity Catalog) is 38% of the exam
2. **Know the Pipeline API** - Transformers, Estimators, and Pipeline stages
3. **Understand metrics** - Know when to use each evaluation metric
4. **Feature Store basics** - How to create, read, and use feature tables
5. **AutoML awareness** - Know what AutoML does and its limitations
6. **Hyperopt for tuning** - Understand Bayesian optimization basics
7. **Unity Catalog registry** - Know aliases, tags and challenger-to-champion promotion
8. **Deployment** - Know batch vs realtime vs streaming serving
9. **Hands-on practice** - Use Databricks Community Edition for experimentation
10. **Read questions carefully** - Some answers are correct but not the best answer

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Comprehensive reference with documentation links |
| [practice-plan.md](practice-plan.md) | Week-by-week study schedule with checkboxes |
| [scenarios.md](scenarios.md) | Exam-style scenarios with solutions |
| [strategy.md](strategy.md) | Study phases, resources, and exam tactics |
| [notes/01-ml-workloads.md](notes/01-ml-workloads.md) | Databricks ML ecosystem and MLflow |
| [notes/02-ml-workflow.md](notes/02-ml-workflow.md) | End-to-end ML lifecycle |
| [notes/03-spark-ml.md](notes/03-spark-ml.md) | Spark MLlib pipelines |
| [notes/04-deep-learning.md](notes/04-deep-learning.md) | Deep learning on Databricks |
| [notes/05-scaling-ml.md](notes/05-scaling-ml.md) | Scaling ML workloads |
