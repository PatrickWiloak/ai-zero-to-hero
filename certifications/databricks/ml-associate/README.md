# Databricks Certified Machine Learning Associate

**Last reviewed:** 2026-11-07. Logistics and outline checked against the [official exam page](https://www.databricks.com/learn/certification/machine-learning-associate) and the [exam guide PDF](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf) (title "August 2026"; its update table still shows March 1, 2025 for publication and update).

## Exam Overview

The certification assesses whether you can use Databricks for basic machine learning tasks: AutoML, Unity Catalog and selected MLflow features, data exploration and feature engineering, model training, tuning and evaluation, and deployment. Passing means you can complete basic ML tasks with Databricks and its tools.

**Exam Details (from the exam guide):**
- **Exam name:** Databricks Certified Machine Learning Associate (Databricks publishes no exam code)
- **Duration:** 90 minutes (time for unscored items is already included)
- **Number of Questions:** 48 scored multiple-choice and multiple-selection questions; up to 10 more unscored items may appear and are not identified
- **Passing Score:** Not published by Databricks
- **Registration fee:** USD 200 plus applicable taxes (as stated in the guide on 2026-11-07)
- **Delivery:** Online proctored or test center
- **Languages:** English, Japanese, Brazilian Portuguese, Korean
- **Test aids:** None allowed
- **Validity:** 2 years; recertify by taking the current live exam
- **Prerequisites:** None required; related training highly recommended. Six months of hands-on Databricks experience is recommended

## Exam Outline

Four sections, in the guide's order. Each note in [notes/](notes/01-databricks-machine-learning.md) covers one section, objective by objective.

| # | Section | Weight | Note |
|---|---------|-------:|------|
| 1 | Databricks Machine Learning | 38% | [01-databricks-machine-learning.md](notes/01-databricks-machine-learning.md) |
| 2 | Data Processing | 19% | [02-data-processing.md](notes/02-data-processing.md) |
| 3 | Model Development | 31% | [03-model-development.md](notes/03-model-development.md) |
| 4 | Model Deployment | 12% | [04-model-deployment.md](notes/04-model-deployment.md) |

The exam page names Section 2 "ML Workflows"; the guide calls it "Data Processing". The old five-domain outline (deep learning, scaling ML, Spark ML as a domain) is gone from these notes: the current guide has no deep learning section, and Spark ML appears only as estimators, transformers, pipelines, cross-validation and tuning inside Section 3.

### Section 1: Databricks Machine Learning (38%)
MLOps best practices, ML runtimes, AutoML, Unity Catalog feature tables (create, write, train, score, online versus offline), the MLflow Client API and UI, the Unity Catalog model registry, promoting code versus models, and aliases for champion and challenger.

### Section 2: Data Processing (19%)
Summary statistics, outlier removal (standard deviation or IQR), visualizing and comparing features, imputing with mean, median or mode, one-hot encoding and when it fits, and when a log transform is appropriate.

### Section 3: Model Development (31%)
Choosing algorithms, mitigating imbalance, estimators versus transformers, training pipelines, Hyperopt `fmin`, random, grid and Bayesian search, parallelizing single-node models, cross-validation versus a train-validation split and counting models, classification and regression metrics, exponentiating log-transformed variables, and the bias-variance tradeoff.

### Section 4: Model Deployment (12%)
Batch, real-time and streaming serving, deploying a custom model to an endpoint, batch inference with pandas, streaming inference with Delta Live Tables, querying a real-time model, and splitting traffic between endpoints.

## Things that changed or are easy to get wrong

- **Hyperopt is on the exam but on its way out.** Databricks docs say open-source Hyperopt is no longer maintained and is not in Databricks Runtime ML after 16.4 LTS ML; they recommend Optuna or Ray Tune. Learn `fmin`, then know the replacements.
- **Unity Catalog models use aliases, not stages.** "Staging" and "Production" stage transitions belong to the legacy workspace registry.
- **Create feature tables with `FeatureEngineeringClient.create_table`**, then write data. There is no SQL `AS FEATURE STORE` clause.
- **Delta Live Tables** is now called Lakeflow Spark Declarative Pipelines in the docs; the exam guide still uses the old name.

## Study Approach

Read the four notes in order; each ends with the objectives to check yourself against. Run the small code samples in a scratch virtual environment (scikit-learn, MLflow and PySpark all run locally) and use Databricks Free Edition (named in the exam guide) for the Unity Catalog, feature table and serving parts, which cannot be reproduced locally. Then work through the [practice questions](../../practice-questions/databricks-ml-associate.md). See [practice-plan.md](practice-plan.md) for a schedule and [strategy.md](strategy.md) for exam tactics.

## Study Resources

- **[📖 Exam page](https://www.databricks.com/learn/certification/machine-learning-associate)** - Official logistics and the exam guide link
- **[📖 Databricks documentation](https://docs.databricks.com/)** - The guide says to study the current, non-deprecated docs for each platform area
- **[📖 MLflow documentation](https://mlflow.org/docs/latest/index.html)** - Open-source MLflow reference
- **[📖 Spark ML guide](https://spark.apache.org/docs/latest/ml-guide.html)** - Pipelines, features and tuning

Databricks lists these courses as recommended preparation: instructor-led Machine Learning with Databricks, and self-paced Data Preparation for Machine Learning, Machine Learning Model Development, Machine Learning Model Deployment and Machine Learning Operations in Databricks Academy.

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Exam logistics, the outline and the key facts with documentation links |
| [practice-plan.md](practice-plan.md) | Week-by-week study schedule |
| [scenarios.md](scenarios.md) | Exam-style scenarios with solutions |
| [strategy.md](strategy.md) | Exam tactics and time management |
| [notes/01-databricks-machine-learning.md](notes/01-databricks-machine-learning.md) | Section 1 |
| [notes/02-data-processing.md](notes/02-data-processing.md) | Section 2 |
| [notes/03-model-development.md](notes/03-model-development.md) | Section 3 |
| [notes/04-model-deployment.md](notes/04-model-deployment.md) | Section 4 |
