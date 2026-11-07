# Databricks ML Associate - Exam-Style Scenarios

**Last reviewed:** 2026-11-07

Eight original scenarios, one or two per section, written for this guide (not taken from any exam). Read the situation, decide, then open the answer. Section weights: Databricks Machine Learning 38%, Data Processing 19%, Model Development 31%, Model Deployment 12%.

---

## Scenario 1 (Section 1): Promoting a better model

**Situation.** A team registers a new version of a model in Unity Catalog. Validation shows version 7 beats version 6, which production inference jobs read with `models:/main.sales.churn@champion`. They want the jobs to use version 7 on the next run without editing any job.

**What do they do?** Reassign the `champion` alias to version 7 with `MlflowClient().set_registered_model_alias("main.sales.churn", "champion", 7)`.

**Why.** An alias is a mutable named reference to a version, so the jobs that load the alias pick up the new version automatically. Version 6 still exists, so rolling back is one more call. Stage transitions are not supported for Unity Catalog models, a tag does not change what the alias resolves to, and deleting version 6 is destructive and unnecessary.

---

## Scenario 2 (Section 1): Features for training and scoring

**Situation.** A data scientist stores customer features in a Unity Catalog feature table and trains a model using them. Later a batch job has only `customer_id` values and must score them.

**What do they do?** Build the training set with `create_training_set` and `FeatureLookup`, train on the DataFrame from `load_df`, log the model with `fe.log_model`, then call `fe.score_batch(model_uri=..., df=batch_df)` with only the keys.

**Why.** Logging with the feature client stores the feature references, so scoring fetches the features itself. Logging with a plain `mlflow.sklearn.log_model` would lose that link and force the job to join features by hand.

---

## Scenario 3 (Section 2): Which imputation?

**Situation.** A `household_income` column is strongly right-skewed with a few multi-million values, and 3 percent of rows are null. A `region` column is text and also has nulls.

**What do they do?** Median-impute income and mode-impute region.

**Why.** The mean of a skewed column is dragged up by the extreme values (in this guide's run, 60,961 against a median of 38,030), so mean imputation would assign unusually high incomes. A mean has no meaning for text, so the most frequent value is the usual fill.

---

## Scenario 4 (Section 2): Outliers on a bell curve versus a skewed column

**Situation.** An analyst must remove outliers from a sensor reading that is close to normal, and from a transaction amount that is heavily skewed.

**What do they do?** Use a standard deviation cut (about 3) for the sensor and the IQR rule for the transaction amount.

**Why.** A standard deviation cut assumes a roughly bell-shaped column; on skewed data the mean and standard deviation are themselves distorted by the extremes. The IQR rule uses quartiles, which a few extreme values barely move.

---

## Scenario 5 (Section 3): Fraud with a 1 percent positive rate

**Situation.** A fraud model is 99 percent accurate but catches almost no fraud. The business says a missed fraud costs far more than a false alarm.

**What do they do?** Stop using accuracy. Use recall (or F-beta weighted toward recall) with a cost-sensitive class weight or resampling, and use a stratified split to keep the 1 percent in every part.

**Why.** Predicting "not fraud" always already scores 99 percent. The fix has to act on the minority class and the metric has to reflect the cost.

---

## Scenario 6 (Section 3): How many models?

**Situation.** A random forest is tuned over `max_depth` in {4, 8, 12}, `n_estimators` in {50, 100}, and `min_samples_leaf` in {1, 5}, with 4-fold cross-validation.

**How many models are trained during the search?** 3 x 2 x 2 = 12 combinations, times 4 folds, is 48 models (plus one if the best parameters are refit on all the data, which many libraries do). With a single train-validation split instead of folds the count is 12.

---

## Scenario 7 (Section 3): The RMSE that looks too good

**Situation.** A house-price model is trained on `log(price)`. The team reports RMSE of 0.21 and says it beats the old model, which had an RMSE of 48,000 dollars.

**What is wrong?** The two numbers are in different units. Exponentiate the predictions (`exp`) and compute RMSE against the raw price before comparing.

**Why.** An RMSE of 0.21 is on the log scale. The same predictions compared with the raw target, without exponentiating, give an absurd error; after exponentiating you get a number in dollars that can be compared fairly.

---

## Scenario 8 (Section 4): Sending 5 percent to a challenger

**Situation.** A model serving endpoint serves `current` (Unity Catalog model, version 3). A new version was validated offline, and the team wants 5 percent of live requests to go to it while they watch.

**What do they do?** Add the new version as a second served entity on the same endpoint and set `traffic_config` routes of 95 and 5 percent.

**Why.** One endpoint can serve several models of the same kind and split traffic by percentage. Querying the new served model directly bypasses the split, so clients must call the endpoint. If the challenger holds up, promote it (Section 1) and move the traffic to 100 percent.
