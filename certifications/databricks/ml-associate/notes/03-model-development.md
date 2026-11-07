# Section 3: Model Development (31%)

**Last reviewed:** 2026-11-07

This section is the classic machine learning core: choose an algorithm, build a training pipeline, tune it, validate it, score it with the right metric and diagnose bias and variance. Follow the order of the [official exam guide (August 2026)](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf). All outputs below are real: scikit-learn 1.9.1, PySpark 4.3.0 (local mode) and Hyperopt, run in a throwaway environment outside the repo. Anything that needs a Databricks workspace is marked not run.

**Hyperopt caveat.** The guide still lists Hyperopt's `fmin`, so you must know it. But Databricks' own docs now say the open-source Hyperopt "is no longer being maintained", that it is not included in Databricks Runtime ML after 16.4 LTS ML, and that Databricks recommends Optuna or Ray Tune instead. Expect `fmin` on the exam, and Optuna in real work.

**[📖 Hyperparameter tuning on Databricks](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/)** - Optuna, Ray Tune and Hyperopt status

## Choosing an algorithm for a scenario

"Use ML foundations to select the appropriate algorithm" means reading the problem: what is the target, how much data, do you need to explain it, and how large is the data.

| If the scenario says | Think | Typical choices |
|---|---|---|
| Predict a number | Regression | Linear regression (baseline, interpretable), random forest or gradient-boosted trees (non-linear) |
| Predict one of several labels | Classification | Logistic regression, random forest, gradient-boosted trees |
| No labels, find groups | Clustering | k-means |
| Predict a value over time, with seasonality | Forecasting | Prophet, ARIMA (the AutoML forecasting options) |
| Must explain to a regulator | Interpretability first | Linear or logistic regression, a shallow decision tree |
| Tabular data, want strong accuracy | Ensembles of trees | Random forest, XGBoost, LightGBM |

The table is a general guide; the Spark ML and AutoML docs list these same families (AutoML classification uses decision trees, random forests, logistic regression, XGBoost and LightGBM). The reasoning step the exam rewards is to match the *target type* first and the *constraint* second.

## Mitigating data imbalance

Imbalance means one class dominates (churners are 10 percent of customers). A model can look excellent by predicting the majority every time. I built a dataset with an 11 percent minority class and trained logistic regression with and without `class_weight="balanced"`:

```
minority share 0.110
class_weight None recall 0.25 precision 0.62 F1 0.36 AUC 0.838 logloss 0.257 acc 0.901
class_weight balanced recall 0.77 precision 0.28 F1 0.41 AUC 0.839 logloss 0.499 acc 0.755
always-majority accuracy 0.890
```

Read that table slowly. Plain accuracy of 0.901 barely beats the 0.890 you get by always predicting the majority, while recall on the minority is only 0.25. The cost-sensitive version raises recall to 0.77, and accuracy falls to 0.755, because it now makes more false alarms (precision 0.28). The AUC is almost unchanged, which tells you the ranking ability is the same and what changed is where the decision threshold sits. Log loss got worse because the class weights distort the probabilities. So: accuracy is the wrong metric for imbalance, and the right fix is chosen by what mistakes cost.

Methods the exam expects you to name:

- **Cost-sensitive learning**: give the minority class a higher misclassification weight (`class_weight` in scikit-learn, a weight column in Spark ML). This is the direct answer to "mitigate the bias toward the majority" in the guide's sample question.
- **Resampling**: oversample the minority class (including synthetic samples such as SMOTE) or undersample the majority.
- **Better metrics and thresholds**: judge by precision, recall, F1 or area under the precision-recall curve, and move the threshold.
- **Stratified splits**: keep the class ratio in every training and validation split.

Feature scaling, a simpler model, or more majority-class rows do not address imbalance.

- **Class imbalance** - a training set where one class is far more common than another, so a model can score high accuracy while missing the minority class.
- **Cost-sensitive learning** - training with a higher penalty for misclassifying the minority class, so the model stops favoring the majority.
- **Stratified split** - a train/validation split that preserves the class proportions in every part.

## Estimators and transformers; building a training pipeline

Spark ML draws one clean line. A **Transformer** "can transform one DataFrame into another DataFrame", through a `transform()` method that generally appends columns. An **Estimator** "can be fit on a DataFrame to produce a Transformer", through `fit()`, which returns a `Model` that is itself a Transformer. A **Pipeline** chains stages (Transformers and Estimators) in order, and "A Pipeline is an Estimator": `fit()` produces a `PipelineModel`, which is a Transformer in which every Estimator has become a fitted Transformer.

**[📖 ML Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html)** - Definitions of Transformer, Estimator, Pipeline and PipelineModel

Run on my small dataset (median imputer, string indexer, one-hot encoder, vector assembler, logistic regression):

```
pipeline type: Pipeline fit -> PipelineModel ; stages: ['ImputerModel', 'StringIndexerModel', 'OneHotEncoderModel', 'VectorAssembler', 'LogisticRegressionModel']
```

`Imputer`, `StringIndexer`, `OneHotEncoder` and `LogisticRegression` are estimators that became `...Model` transformers on `fit`; `VectorAssembler` is a plain Transformer and stays as is. The pipeline's real value is that the same learned imputation and encoding are applied to training and to new data, with no hand-copied steps, and the fitted pipeline is what you log and register.

```python
# Spark ML training pipeline (run locally on PySpark 4.3.0 for this guide)
pipe = Pipeline(stages=[imp, idx, oh, va, lr])
model = pipe.fit(train_df)        # PipelineModel
preds = model.transform(test_df)
```

- **Transformer** - a Spark ML component with a `transform()` method that turns one DataFrame into another, usually by adding columns.
- **Estimator** - a Spark ML component with a `fit()` method that learns from a DataFrame and returns a Model, which is a Transformer.
- **Pipeline** - an ordered chain of transformers and estimators that is itself an estimator; fitting it returns a PipelineModel.

## Hyperparameter tuning: Hyperopt, random, grid and Bayesian search

A hyperparameter is a setting you choose before training (tree depth, regularization strength). Tuning is a search over them, and the search strategies differ in cost:

- **Grid search** tries every combination of the values you list. Thorough but the cost multiplies with each added hyperparameter.
- **Random search** samples combinations at random from ranges you set. It often finds good settings with far fewer trials, especially when only a few hyperparameters matter.
- **Bayesian search** uses the results of earlier trials to decide the next one. Hyperopt's TPE (Tree of Parzen Estimators, `tpe.suggest`) is Bayesian-style.

Hyperopt's `fmin` takes the objective function `fn`, the search `space`, the algorithm `algo` (the docs say the most commonly used are `hyperopt.rand.suggest` for random search and `hyperopt.tpe.suggest` for TPE), `max_evals` ("the number of models to fit") and a `trials` object. I ran both algorithms on a random forest with 15 evaluations each:

```
tpe best {'max_depth': 11.0, 'n_estimators': 80.0} best F1 0.906 models fit (trials): 15
rand best {'max_depth': 11.0, 'n_estimators': 80.0} best F1 0.906 models fit (trials): 15
```

They found the same best settings here: on a tiny two-parameter space and only 15 trials, a smart search has little to be smart about. The advantage of Bayesian search shows when evaluations are expensive and the space is large; do not read this run as proof that the two are equivalent.

```python
# Hyperopt fmin as run above
best = fmin(fn=obj, space=space, algo=tpe.suggest, max_evals=15, trials=Trials())
```

**[📖 Hyperopt concepts](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-concepts)** - fmin arguments, Trials versus SparkTrials, parallelism and MLflow logging

### Parallelizing single-node models

This is the objective "Parallelize single node models for hyperparameter tuning". The docs split it cleanly: `SparkTrials` distributes tuning of **single-machine models** (scikit-learn, for example) across Spark workers, with each trial a one-task Spark job; `Trials` is for objective functions that are already distributed (MLlib or Horovod), and the docs say not to use `SparkTrials` with those. `parallelism` sets how many trials run at once (default: number of executors, max 128), and there is a trade-off: higher parallelism is faster but each trial sees fewer past results, which weakens an adaptive search like TPE. With `SparkTrials`, `fmin` is logged as a parent MLflow run with each trial as a child run.

```python
# Not run here: needs a Spark cluster and a Databricks runtime that includes Hyperopt (from the Databricks docs pattern)
from hyperopt import SparkTrials
with mlflow.start_run():
    best = fmin(fn=obj, space=space, algo=tpe.suggest, max_evals=32,
                trials=SparkTrials(parallelism=4))
```

- **Hyperopt** - a Python library for hyperparameter search; `fmin` minimizes an objective over a search space (not maintained upstream, and not in Databricks Runtime ML after 16.4 LTS ML).
- **fmin** - the Hyperopt function that runs a search, taking an objective function, a search space, an algorithm, `max_evals` and a trials object.
- **SparkTrials** - the Hyperopt trials class that runs single-machine model trials in parallel as Spark tasks; do not use it with distributed algorithms such as MLlib.
- **Random search** - tuning by sampling hyperparameter combinations at random from the allowed ranges.
- **Bayesian search** - tuning that uses the results of earlier trials to choose the next hyperparameters, as TPE does.

## Cross-validation versus a train-validation split

A **train-validation split** divides the data once: fit on one part, score on the other. It is cheap, and the score depends on which rows landed in which part. **k-fold cross-validation** splits the data into k folds, trains k times (each time holding out one fold) and averages the scores. The Spark docs put the cost trade-off precisely: `TrainValidationSplit` "only evaluates each combination of parameters once, as opposed to k times in the case of CrossValidator. It is, therefore, less expensive, but will not produce as reliable results when the training dataset is not sufficiently large."

**[📖 ML Tuning: model selection and hyperparameter tuning](https://spark.apache.org/docs/latest/ml-tuning.html)** - CrossValidator, TrainValidationSplit and ParamGridBuilder

I measured how unstable a single split is by repeating it with five random seeds on 300 rows, against 5-fold cross-validation:

```
5 different single splits: [0.883 0.933 0.85  0.883 0.85 ] range 0.083
5-fold CV mean 0.893 std 0.036
```

The same model scored anywhere from 0.85 to 0.933 depending on the split, a range of 8 points, while the cross-validated mean (0.893) with its spread (0.036) is a more honest summary. Benefits of cross-validation: a more reliable estimate, and every row is used for both training and validation. Downsides: k times the training cost, and it needs care with time series (you cannot shuffle the future into the past). With large data, a single split is often good enough and much cheaper.

In Spark ML, "perform cross-validation as part of model fitting" is `CrossValidator(estimator=pipe, estimatorParamMaps=grid, evaluator=..., numFolds=3)`, followed by `.fit(df)`. `CrossValidator` re-fits the Estimator on the entire dataset using the best parameter map at the end.

- **Cross-validation** - estimating performance by training k times, each time validating on a different fold, and averaging the scores.
- **Train-validation split** - estimating performance from one split of the data; cheaper than cross-validation but noisier on small data.
- **ParamGridBuilder** - the Spark ML utility that builds the grid of hyperparameter combinations (a list of param maps) for a tuner.

### Counting the models trained

The guide asks you to "identify the number of models being trained in conjunction with a grid-search and cross-validation process". The formula is simple:

> models = (product of the number of values of each hyperparameter) x (number of folds)

The Spark docs show the pattern: 3 values times 2 values with 2 folds is (3 x 2) x 2 = 12 models. The guide's sample question has C with 3 values, kernel with 2 and gamma with 3, so 18 combinations, and with 5 folds that is 90 fits. I checked it by running scikit-learn's `GridSearchCV`:

```
combos 18 fits 90 +1 refit = 91
```

scikit-learn by default refits the best parameters on all the data afterwards, which is one extra model; the exam answer is 90. Spark's `CrossValidator` also re-fits on the full dataset at the end. I ran it with 3 folds and a 3 x 2 grid:

```
param maps 6
avgMetrics entries 6 ; submodels 18 (folds x maps) + 1 refit on all data
TVS submodels 6
```

6 parameter maps x 3 folds = 18 models during the search, plus the final refit; the `TrainValidationSplit` equivalent trains 6 (one per parameter map). The exam question will say "how many models are trained during the search", and the answer is combinations times folds.

## Classification metrics: F1, log loss, ROC/AUC

- **Accuracy**: share of correct predictions. Misleading on imbalanced data (above: 0.901 with recall 0.25).
- **Precision**: of the rows predicted positive, how many are positive. **Recall**: of the actual positives, how many were found.
- **F1**: scikit-learn describes the F-measure as "a weighted harmonic mean of the precision and recall"; F1 weights them equally and is best at 1 and worst at 0. Use it when both false positives and false negatives matter and the classes are imbalanced.
- **ROC AUC**: area under the ROC curve, which plots true positive rate against false positive rate across all thresholds. It measures ranking quality independent of any threshold: 0.5 is chance, 1.0 is perfect.
- **Log loss**: scikit-learn: "also called logistic regression loss or cross-entropy loss, is defined on probability estimates". It punishes confident wrong predictions heavily, so it is the metric when you care about calibrated probabilities. Lower is better.

**[📖 Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)** - Definitions of F1, log loss and ROC AUC

The imbalance table above is a good model for how metrics disagree: balanced weights left AUC at 0.839 but moved F1 from 0.36 to 0.41 and nearly doubled log loss from 0.257 to 0.499. Neither number is wrong; they answer different questions.

## Regression metrics: RMSE, MAE, R-squared

- **MAE** (mean absolute error): the average size of the error in the target's units; each error counts in proportion to its size, so it is robust to outliers.
- **RMSE** (root mean squared error): squares errors before averaging, so large errors are penalized more; in the target's units. Choose it when big misses are especially costly.
- **R-squared**: the share of variance in the target the model explains; unit-free, 1 is perfect. scikit-learn notes R-squared gives the same ranking as squared error.

On my log-target regression, evaluated correctly in original units: `RMSE 10.6 ; MAE 5.5 ; R2 0.922`. RMSE is about twice MAE, which means some large errors exist (the target is skewed, so big values have big errors).

## Choosing the metric for the scenario

The guide asks you to "choose the most appropriate metric for a given scenario objective". Work backwards from the cost of a mistake:

| Scenario objective | Metric |
|---|---|
| Missing a positive is expensive (fraud, disease) | Recall, or F-beta weighted toward recall |
| A false alarm is expensive (spam folder) | Precision |
| Imbalanced data, both errors matter | F1 or area under the precision-recall curve |
| Rank customers by likelihood, threshold set later | ROC AUC |
| Well-calibrated probabilities needed | Log loss |
| Regression where large misses are very costly | RMSE |
| Regression with outliers you do not want to dominate | MAE |
| Explain how much variation the model captures | R-squared |

## Exponentiating log-transformed variables

If you train on `log(y)`, the model predicts `log(y)`. To interpret a prediction in original units, or to compute RMSE comparable to other models, you must apply the inverse: `exp`. Forgetting is the classic error. My results from the same model, with the same predictions:

```
RMSE in log units 0.189
RMSE wrong (log preds vs raw y) 49.6
RMSE after np.exp 10.6 ; MAE 5.5 ; R2 0.922
```

Comparing log-scale predictions against raw targets gives an absurd 49.6; exponentiating first gives 10.6 in the target's own units. (An RMSE in log units, 0.189, is a valid number but it is in different units, so you cannot compare it with a model trained on the raw scale.) One more subtlety worth knowing: `exp` of the mean of the log is the geometric-mean-type estimate, not the mean of the original variable, so back-transformed predictions can be slightly biased low; the exam only asks that you do the transformation back.

- **Exponentiate** - apply the inverse of a log transform (`exp`) so predictions and metrics are in original units.

## Model complexity and the bias-variance tradeoff

**Bias** is error from a model too simple to capture the pattern (underfitting): high error on both training and validation data. **Variance** is error from a model so flexible it learns the noise (overfitting): very low training error and much higher validation error. Complexity pushes bias down and variance up; the best model is in between. I fit decision trees of increasing depth to noisy sine-wave data:

```
depth 1 train RMSE 0.435 val RMSE 0.403
depth 3 train RMSE 0.318 val RMSE 0.362
depth None train RMSE 0.000 val RMSE 0.423
```

Depth 1 is underfit (both errors high). Depth 3 is the best on validation (0.362). The unlimited tree memorizes the training set (train RMSE 0.000) and does worse on validation than depth 3 (0.423). That is the guide's sample question in numbers. The fixes for overfitting are simpler models, regularization, more training data or fewer features; for underfitting, richer models or better features.

- **Bias** - error from a model that is too simple, which shows as high error on training and validation data (underfitting).
- **Variance** - error from a model that is too sensitive to the training data, which shows as low training error and high validation error (overfitting).
- **Regularization** - a penalty that constrains model complexity to reduce overfitting.

## Check yourself against the objectives

Name the algorithm family for a scenario and justify it; list the imbalance remedies and say which one the problem asks for; state the Estimator and Transformer difference in one sentence; explain what `SparkTrials` is for and when not to use it; count models for a grid and fold count; pick a metric from a cost statement; and diagnose over- and underfitting from two error numbers. Questions for this section are in the [Databricks ML Associate bank](../../../practice-questions/databricks-ml-associate.md).
