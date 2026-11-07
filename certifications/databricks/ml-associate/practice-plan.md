# Databricks ML Associate - Study Plan

**Last reviewed:** 2026-11-07

A four-week reading and hands-on schedule built on the four official sections, with time in proportion to the weights (38 / 19 / 31 / 12). It assumes about 1 to 2 hours a day. Everything here is reading and trying things out; there are no graded exercises. Local work (scikit-learn, MLflow, PySpark) needs only a Python virtual environment. The Unity Catalog, feature table and serving parts need a Databricks workspace (the exam guide names Databricks Free Edition for hands-on practice).

## Week 1: Section 1, Databricks Machine Learning (38%)

- [ ] Read [README.md](README.md) and skim [fact-sheet.md](fact-sheet.md)
- [ ] Read [notes/01-databricks-machine-learning.md](notes/01-databricks-machine-learning.md) through the AutoML section
- [ ] Read the Databricks [MLOps workflow](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow) page and write down in your own words when you would promote a model instead of code
- [ ] Open the AutoML docs, then run an AutoML experiment on a sample table in a workspace and open the best trial's notebook
- [ ] Finish note 01: feature tables, MLflow runs, registry and aliases
- [ ] Reproduce the MLflow OSS script in the note locally (four runs, `search_runs`, two versions, aliases, tags)

## Week 2: Section 3, Model Development (31%)

- [ ] Read [notes/03-model-development.md](notes/03-model-development.md) up to cross-validation
- [ ] Run the imbalance experiment from the note and compare accuracy, recall and F1 for yourself
- [ ] Read the Spark ML [Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html) and [Tuning](https://spark.apache.org/docs/latest/ml-tuning.html) pages
- [ ] Build the small Spark pipeline from the note in local PySpark and print the fitted stage types
- [ ] Finish note 03: counting models, metrics, exponentiating log targets, bias and variance

## Week 3: Sections 2 and 4 (19% and 12%)

- [ ] Read [notes/02-data-processing.md](notes/02-data-processing.md); run the outlier and imputation examples on a skewed column
- [ ] Read [notes/04-model-deployment.md](notes/04-model-deployment.md)
- [ ] Score a logged model with `pyfunc.load_model` on pandas, then with `spark_udf`
- [ ] In a workspace, create a serving endpoint for a registered model and read its traffic settings

## Week 4: Review

- [ ] Read [scenarios.md](scenarios.md) and the [strategy](strategy.md) page
- [ ] Take the [practice questions](../../practice-questions/databricks-ml-associate.md) in one sitting of about 45 minutes and read every explanation, right or wrong
- [ ] Re-read the notes for the sections where explanations surprised you
- [ ] Two weeks before the exam date, check the exam guide on the Databricks site again (the guide asks you to) for changes
