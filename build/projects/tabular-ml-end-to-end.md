# Tabular ML End to End

**In one line:** Train, compare, evaluate and save a classic machine learning model on a table of data with scikit-learn, in about 40 lines of Python and under an hour.
**Last reviewed:** 2026-11-07

---

Build a model that predicts a yes/no outcome from a table of numbers, the kind of problem most business ML really is. You will fit a baseline, a simple model and a gradient-boosted model, test them honestly, and save the winner to a file you can load elsewhere.

**Estimated Time:** 45 minutes
**Difficulty:** Beginner
**Prerequisites:** Python basics ([Python for AI](../../learn/day-one/python-for-ai.md)); no cloud account, GPU or API key needed

## What was run

Everything below was executed on 2026-11-07 with Python 3.14, scikit-learn 1.9.1, pandas 3.1.1 and joblib, in a throwaway virtual environment outside the repo. The output shown is the real output. Exact digits can differ slightly on other versions. The dataset ships inside scikit-learn, so nothing is downloaded.

## Step 1: Set up

```bash
python3 -m venv ~/.cache/tabular-venv
~/.cache/tabular-venv/bin/pip install scikit-learn pandas joblib
```

(Or use `uv venv` then `uv pip install`; either works.) Keep the environment outside your project so it never lands in git.

## Step 2: Load the data and split it

We use scikit-learn's built-in breast cancer dataset: 569 rows, 30 measurements per row, label 0 for malignant and 1 for benign. It is a stand-in for any table with a yes/no label, such as churn or fraud. This is a teaching dataset, not a medical tool.

```python
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

data = load_breast_cancer(as_frame=True)
X, y = data.data, data.target
print("rows, columns:", X.shape)
print("class counts (0=malignant, 1=benign):", y.value_counts().to_dict())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)
```

```
rows, columns: (569, 30)
class counts (0=malignant, 1=benign): {1: 357, 0: 212}
```

`stratify=y` keeps the class mix the same in both parts. `random_state` makes the split repeatable. The 20% test set is locked away until the very end: choose models using only the training data.

## Step 3: Compare a baseline, a simple model and a boosted model

Always start with a baseline that does nothing clever. If a real model cannot beat it, something is wrong. Five-fold **cross-validation** splits the training data five ways, trains on four parts and scores on the fifth, so the result does not hinge on one lucky split. The score is ROC AUC (1.0 is perfect, 0.5 is a coin flip).

```python
models = {
    "baseline (most common class)": DummyClassifier(strategy="most_frequent"),
    "logistic regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "gradient boosting": HistGradientBoostingClassifier(random_state=42),
}
for name, m in models.items():
    scores = cross_val_score(m, X_train, y_train, cv=5, scoring="roc_auc")
    print(f"{name:30s} CV AUC {scores.mean():.3f} +/- {scores.std():.3f}")
```

```
baseline (most common class)   CV AUC 0.500 +/- 0.000
logistic regression            CV AUC 0.993 +/- 0.011
gradient boosting              CV AUC 0.991 +/- 0.015
```

The two real models are statistically indistinguishable (the differences sit inside the spread). When a simple model ties a complex one, pick the simple one: it is faster, smaller and easier to explain. Note `StandardScaler` sits inside a pipeline, so scaling is learned from training folds only, which avoids [leakage](../../learn/concepts/feature-engineering-and-data-prep.md). This particular dataset is easy; on messier business tables, boosted trees often pull ahead (see [Decision trees and gradient boosting](../../learn/concepts/decision-trees-and-gradient-boosting.md)).

## Step 4: Evaluate the chosen model once on the test set

```python
best = models["logistic regression"]
best.fit(X_train, y_train)
pred = best.predict(X_test)
proba = best.predict_proba(X_test)[:, 1]
print("Test AUC:", round(roc_auc_score(y_test, proba), 3))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=["malignant", "benign"]))
```

```
Test AUC: 0.995
[[41  1]
 [ 1 71]]
              precision    recall  f1-score   support

   malignant       0.98      0.98      0.98        42
      benign       0.99      0.99      0.99        72

    accuracy                           0.98       114
   macro avg       0.98      0.98      0.98       114
weighted avg       0.98      0.98      0.98       114
```

How to read it:

- The **confusion matrix** has true classes as rows and predictions as columns. Of 42 malignant cases, 41 were caught and 1 was missed; of 72 benign, 71 were right and 1 was flagged wrongly.
- **Precision** asks: of the rows the model flagged, how many were right? **Recall** asks: of the rows that really were positive, how many did it find? Which matters more depends on the cost of each mistake. Missing a malignant case is worse than a false alarm, so recall on "malignant" is the number to watch.
- With only 114 test rows, one error moves the numbers by about a point. Report this as "around 98%", not "98.2%".

Look at the test set once. If you keep re-tuning against it, it stops being a fair test. See [Training, validation and overfitting](../../learn/concepts/training-validation-and-overfitting.md).

## Step 5: Save the model and load it back

```python
joblib.dump(best, "model.joblib")
loaded = joblib.load("model.joblib")
print("reloaded model agrees on all test rows:", (loaded.predict(X_test) == pred).all())
print("one new row ->", data.target_names[loaded.predict(X_test.iloc[[0]])[0]])
```

```
reloaded model agrees on all test rows: True
one new row -> malignant
```

The saved file was 3,105 bytes. Because the scaler and the classifier live in one pipeline object, the file carries both, so serving code cannot forget to scale. Load it in the same scikit-learn version it was saved with: the scikit-learn documentation warns that pickled models may not load across versions, and that loading untrusted files can run arbitrary code. Only load model files you made or trust.

## Step 6: What deploying would take (not run here)

I did not deploy anything for this page. The usual path, in order of effort:

1. **A script or scheduled job** that loads `model.joblib` and scores a file of new rows. Often enough.
2. **A small web API** (FastAPI or Flask) that loads the model once at start-up and returns a prediction per request.
3. **A managed endpoint** with a model registry and drift monitoring. The cloud walkthrough is [Deploy a machine learning model](deploy-ml-model.md).

Before any of them, record the scikit-learn version, the training data date and the test score next to the file.

## Common mistakes

- **Scaling or imputing before the split.** Keep preprocessing inside the pipeline.
- **Choosing the model on the test set.** Compare with cross-validation; test once.
- **Reporting accuracy alone** on imbalanced data. Use precision, recall and AUC.
- **Forgetting the baseline.** "98% accurate" means little when guessing the common class already scores 63% here (357 of 569).
- **Loading model files from strangers.** Pickle-based files can execute code.

## Next steps

- Try your own table: load a CSV with `pandas.read_csv`, pick a label column and rerun Steps 2 to 4. Prep tips: [Feature engineering and data prep](../../learn/concepts/feature-engineering-and-data-prep.md)
- Tune the boosted model with `RandomizedSearchCV` on the training set only
- [Classic ML: supervised vs unsupervised](../../learn/concepts/classic-ml-supervised-vs-unsupervised.md)
- [Deploy a machine learning model](deploy-ml-model.md)
- For data in warehouses and pipelines feeding a model like this: [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- scikit-learn user guide, "Cross-validation: evaluating estimator performance": https://scikit-learn.org/stable/modules/cross_validation.html
- scikit-learn user guide, "Metrics and scoring: quantifying the quality of predictions": https://scikit-learn.org/stable/modules/model_evaluation.html
- scikit-learn user guide, "Model persistence" (joblib, version and security caveats): https://scikit-learn.org/stable/model_persistence.html
- scikit-learn, `load_breast_cancer` dataset (Wisconsin Diagnostic Breast Cancer): https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html
- scikit-learn, "Common pitfalls and recommended practices": https://scikit-learn.org/stable/common_pitfalls.html
