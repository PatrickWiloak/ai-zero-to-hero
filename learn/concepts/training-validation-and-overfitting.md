# Training, Validation and Overfitting

**In one line:** Split your data so every score you report comes from examples the model never saw, spot overfitting from the gap between training and validation scores, and pick the metric (precision, recall, F1, ROC-AUC) that matches the mistake you can least afford.
**Last reviewed:** 2026-10-21

---

> Assumes [What is machine learning?](what-is-machine-learning.md) and ideally [Classic ML: supervised vs unsupervised](classic-ml-supervised-vs-unsupervised.md). The same ideas apply to LLM apps; [Evals for LLMs](evals-for-llms.md) is the LLM version of this page.

## The short version

- A model's score on its own training data tells you almost nothing. Hold data back: a **training set** to fit on, a **validation set** to make choices with, and a **test set** you look at once, at the end.
- **Overfitting** is when the training score keeps improving while the validation score stalls or falls: the model is memorising quirks instead of learning the pattern. **Underfitting** is when both are poor: the model is too simple.
- **Cross-validation** reuses a small dataset fairly: split it into k folds, train k times, each time validating on a different fold, and average.
- **Accuracy** misleads whenever classes are imbalanced. Use **precision** (of the things I flagged, how many were right?), **recall** (of the things I should have flagged, how many did I catch?), their balance **F1**, and threshold-free **ROC-AUC** or **PR-AUC**.
- The decision **threshold** is a business choice. Moving it trades precision for recall; the model does not change.
- **Leakage** (information from the answer sneaking into the inputs, or test rows into training) makes a bad model look brilliant. It is the most common reason a model that scored well in the notebook fails in production.

## Why you hold data back

A model is fitted to make its errors small on the examples it is given. A flexible enough model can make them zero, by memorising. A lookup table of every training row scores 100% on those rows and is useless on the next customer. So the only honest question is: how does it do on rows it has never seen?

The standard answer is three splits:

| Split | Typical share | Used for | Touched |
|---|---|---|---|
| Training | 60 to 80% | Fitting the model's parameters | Every experiment |
| Validation | 10 to 20% | Choosing between models, features, settings and thresholds | Every experiment |
| Test | 10 to 20% | One final, unbiased estimate | Once, at the end |

Why two held-out sets and not one? Because every time you look at a validation score and change something, you are fitting to the validation set too, just more slowly. After fifty experiments the best validation score is optimistic. The test set, untouched until you have stopped making choices, is the one number you can believe. If you peek at it and go back to tuning, it becomes a second validation set and you need a new test set.

How to split depends on how the model will be used:

- **Random split** when rows are independent (one row per customer, no time order). Use a **stratified** split for classification so each split has the same share of each class.
- **Time-based split** when you will predict the future from the past (demand, churn, fraud). Train on January to September, validate on October, test on November. A random split would let the model learn from November rows when "predicting" October, and its score would be fiction.
- **Group split** when rows come in clumps (many transactions per customer, many images per patient). Keep each group in one split, or the model learns to recognise the customer rather than the pattern.

## Cross-validation

With a few hundred rows, a single 20% validation slice is small and noisy: a lucky split can swing the score by several points. **k-fold cross-validation** fixes that. Split the training data into k equal folds (5 or 10 is typical). Train on k-1 folds, validate on the remaining one, and repeat so each fold takes a turn as validation. Report the mean and the spread of the k scores. It costs k times the training, which is nothing for classic models and prohibitive for large neural networks, which is why deep learning usually sticks to one fixed validation set.

## Overfitting and underfitting, made visible

The example below builds a fraud-like dataset (10,000 rows, about 3% positives) and fits decision trees of increasing depth. Deeper trees can carve the data into finer pieces, so they can memorise more.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (precision_score, recall_score, f1_score,
                             roc_auc_score, confusion_matrix, accuracy_score)

# A fraud-like problem: 10,000 rows, about 3% positives
X, y = make_classification(n_samples=10_000, n_features=20, n_informative=6,
                           weights=[0.97], flip_y=0.01, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# Overfitting, made visible: tree depth vs train and validation score
for depth in [2, 5, 10, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=0)
    tree.fit(X_train, y_train)
    train_auc = roc_auc_score(y_train, tree.predict_proba(X_train)[:, 1])
    cv_auc = cross_val_score(tree, X_train, y_train, cv=5, scoring="roc_auc").mean()
    print(f"depth={str(depth):>4}  train AUC={train_auc:.3f}  5-fold CV AUC={cv_auc:.3f}")
```

Output (scikit-learn 1.9.1):

```
depth=   2  train AUC=0.659  5-fold CV AUC=0.613
depth=   5  train AUC=0.830  5-fold CV AUC=0.714
depth=  10  train AUC=0.893  5-fold CV AUC=0.710
depth=None  train AUC=1.000  5-fold CV AUC=0.704
```

Read it as a story. At depth 2 both scores are low: **underfitting**. At depth 5 validation peaks. After that the training score climbs all the way to a perfect 1.000 while validation drifts down: **overfitting**. The unlimited tree has memorised every training row and learned nothing extra that transfers. The gap between the two columns is the signal to watch; the depth at which validation peaks is the one to keep.

The general cures for overfitting: more data, a simpler model, **regularisation** (a penalty for large weights or complex trees), **early stopping** (stop training when the validation score stops improving, the standard practice for neural networks), and ensembles that average many overfit models into one stable one. The cures for underfitting: a more flexible model, better features, or training longer.

## Metrics for classification

Continuing the example with a logistic regression and the held-out test set:

```python
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
proba = model.predict_proba(X_test)[:, 1]
print("always-'no' baseline accuracy:", round(accuracy_score(y_test, [0] * len(y_test)), 3))
for threshold in [0.5, 0.2, 0.1]:
    pred = (proba >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    print(f"threshold {threshold}: TP={tp} FP={fp} FN={fn} "
          f"precision={precision_score(y_test, pred):.2f} "
          f"recall={recall_score(y_test, pred):.2f} F1={f1_score(y_test, pred):.2f}")
print("ROC-AUC:", round(roc_auc_score(y_test, proba), 3))
```

```
always-'no' baseline accuracy: 0.965
threshold 0.5: TP=15 FP=0 FN=55 precision=1.00 recall=0.21 F1=0.35
threshold 0.2: TP=25 FP=36 FN=45 precision=0.41 recall=0.36 F1=0.38
threshold 0.1: TP=39 FP=113 FN=31 precision=0.26 recall=0.56 F1=0.35
ROC-AUC: 0.846
```

First line: a "model" that always answers "not fraud" is 96.5% accurate. That is why accuracy is the wrong metric here. Everything below comes from the **confusion matrix**, the four counts every classification metric is built from:

| | Model says yes | Model says no |
|---|---|---|
| **Actually yes** | True positive (TP): caught | False negative (FN): missed |
| **Actually no** | False positive (FP): false alarm | True negative (TN): correctly ignored |

- **Precision = TP / (TP + FP).** Of everything flagged, the share that was real. Low precision means analysts waste their day on false alarms.
- **Recall = TP / (TP + FN).** Of everything real, the share you caught. Low recall means fraud gets through. Also called sensitivity or true positive rate.
- **F1** is the harmonic mean of the two, `2 x P x R / (P + R)`. It is high only when both are; use it when you need one number and both errors matter.
- **ROC-AUC** looks at every possible threshold at once. It is the probability that the model scores a random positive above a random negative: 0.5 is a coin flip, 1.0 is perfect. Here 0.846 says the model ranks well even though no single threshold looks great.
- **PR-AUC (average precision)** is the area under the precision-recall curve. On heavily imbalanced data it is more informative than ROC-AUC, which can look flattering when negatives vastly outnumber positives.

Now look at the threshold rows. Same model, three behaviours. At 0.5 every flag is right (precision 1.00) but four in five frauds slip through. At 0.1 you catch more than half, at the cost of 113 false alarms. Which is better depends on what each mistake costs: if a missed fraud costs $500 and reviewing a false alarm costs $5, the 0.1 threshold wins easily. Write the costs down, compute the expected cost on the validation set at each threshold, and pick the cheapest. That turns a modelling argument into an arithmetic one.

For regression, the metrics are MAE, RMSE and R²; see [Classic ML](classic-ml-supervised-vs-unsupervised.md#regression).

## Leakage: the bug that makes bad models look good

Leakage is any path by which the model, during training or validation, gets information it will not have at prediction time. Classic forms:

- **Target leakage:** a feature that is a consequence of the answer. A churn model with "account closed date" as a feature scores perfectly and predicts nothing. Subtler: "number of support calls in the 30 days after the prediction date".
- **Train-test contamination:** duplicated rows that land in both splits, or preprocessing (scaling, imputing missing values, selecting features) fitted on the whole dataset before splitting. Fit every preprocessing step on the training fold only; scikit-learn `Pipeline` objects do this for you inside cross-validation.
- **Temporal leakage:** random splits on time-ordered data, as above.
- **Benchmark contamination:** the LLM version, where test questions were in the pretraining data. See the [contamination and saturation explainer](../../explainers/benchmarks/contamination-and-saturation.md).

The tell is a score that is too good. If a first model scores 0.99 on a problem humans find hard, assume leakage until you have proved otherwise: look at the top features and ask of each one, "would I know this at the moment I need the prediction?"

## The same ideas for LLM applications

You rarely train an LLM yourself, but every idea here carries over to building on one. Your prompt and pipeline are the "model" you tune; your **eval set** is the validation set; a held-back set of real user queries is your test set. Prompt-tuning against the same 20 examples for a week overfits to them exactly as the deep tree did. Precision and recall reappear in retrieval (did the retriever return the right chunks, and only those?) and in guardrails (how many harmful outputs did the filter catch, and how many good ones did it block?). [Evals for LLMs](evals-for-llms.md) and [Set up an eval harness](../../build/projects/set-up-eval-harness.md) apply this page to LLM apps.

## Common mistakes

- **Reporting the training score**, or a validation score after fifty rounds of tuning on it, as the expected real-world performance.
- **Random splits on time-series data.** Split by time whenever predictions run forward in time.
- **Preprocessing before splitting.** Scaling or imputing on the full dataset leaks test statistics into training.
- **Accuracy on imbalanced classes.** Always print the always-majority baseline next to it.
- **Leaving the threshold at 0.5** because it is the default. It is a cost decision.
- **Comparing models on different splits.** Fix the random seed and split once, or use the same cross-validation folds for every candidate.

## Next steps

- [Evals for LLMs](evals-for-llms.md): the same discipline for prompts and agents
- [How LLMs are trained](how-llms-are-trained.md): what training means at the scale of a language model
- [Deploy an ML model](../../build/projects/deploy-ml-model.md): shipping the model you validated
- [MMLU summary](../../papers/techniques/137-mmlu/summary.md) and [contamination explainer](../../explainers/benchmarks/contamination-and-saturation.md): held-out testing at the scale of the whole field

## Sources

- scikit-learn, "Cross-validation: evaluating estimator performance": https://scikit-learn.org/stable/modules/cross_validation.html
- scikit-learn, "Metrics and scoring" (precision, recall, F1, ROC-AUC, average precision): https://scikit-learn.org/stable/modules/model_evaluation.html
- scikit-learn, "Common pitfalls and recommended practices" (data leakage): https://scikit-learn.org/stable/common_pitfalls.html
- Saito and Rehmsmeier, "The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets", PLOS ONE (2015): https://doi.org/10.1371/journal.pone.0118432
- Kaufman et al., "Leakage in Data Mining: Formulation, Detection, and Avoidance", ACM TKDD (2012): https://doi.org/10.1145/2382577.2382579
- Code output above produced with scikit-learn 1.9.1 on 2026-10-21.
