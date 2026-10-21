# Classic ML: Supervised vs Unsupervised

**In one line:** Tell classification, regression and clustering apart, know which classic algorithm to reach for first on a table of data, and run all three in scikit-learn in under 40 lines before you consider a language model.
**Last reviewed:** 2026-10-21

---

> Assumes you have read [What is machine learning?](what-is-machine-learning.md). This page goes one level deeper on the two kinds of learning that cover most business ML.

## The short version

- **Supervised learning** learns from examples that come with the right answer (a **label**). If the answer is a category ("spam", "fraud", "churns") it is **classification**; if it is a number (price, demand, minutes) it is **regression**.
- **Unsupervised learning** has no labels. You ask the algorithm to find structure: groups of similar rows (**clustering**), a smaller summary of many columns (**dimensionality reduction**), or rows that do not fit (**anomaly detection**).
- For a table of numbers and categories (the most common business data), start with a simple baseline (logistic or linear regression), then try **gradient-boosted trees** (XGBoost, LightGBM, scikit-learn's `HistGradientBoosting*`). They win most tabular problems and are cheap to run.
- The hard part is rarely the algorithm. It is deciding what the label is, collecting enough honest examples of it, and testing on data the model has not seen. [Training, validation and overfitting](training-validation-and-overfitting.md) covers the testing half.
- A large language model is rarely the right first tool for predicting a number or a yes/no from a table. Use one when the input is unstructured text, or when you have no labels and need a model that already knows the domain.

## The question that decides everything: do you have labels?

Before picking any algorithm, write down the exact question the model should answer and ask: do I have past examples where the answer is known?

| You have... | You want... | Kind of problem | Example |
|---|---|---|---|
| Rows with a known category | Predict the category for new rows | Classification | Will this customer cancel next month? (yes/no) |
| Rows with a known number | Predict the number for new rows | Regression | How many units will this store sell next week? |
| Rows, no answers | Find natural groups | Clustering | Which customers behave alike? |
| Rows, no answers, many columns | A compact summary you can plot or feed onward | Dimensionality reduction | Squash 300 survey answers into 2 axes |
| Mostly normal rows | Flag the odd ones | Anomaly detection | Which card transactions look unlike this customer's history? |

Labels are expensive. Somebody has to decide that a ticket was "billing" and not "technical", or wait a month to learn whether a customer churned. That cost is the main reason unsupervised methods exist, and it is also why **self-supervised** learning (where the label is hidden inside the data itself, such as the next word of a sentence) made large language models possible. See [LLM basics](llm-basics.md).

## Classification

A classifier takes the features of one example (the columns of one row) and outputs a category, usually with a probability attached. Binary classification has two classes (fraud or not); multi-class has more (which of 12 product lines a complaint is about).

The workhorse algorithms, in the order you should try them:

1. **Logistic regression.** Despite the name, a classifier. It weights each feature, adds them up and squashes the result into a probability between 0 and 1. It is fast, hard to overfit, and you can read the weights to see which features push toward "yes". Always fit it first as a baseline.
2. **Decision trees and their ensembles.** A tree asks a series of yes/no questions ("is tenure under 6 months?", "more than 3 support calls?") and ends at a leaf with a prediction. One tree overfits easily; hundreds of them averaged (**random forest**) or built one after another, each fixing the last one's mistakes (**gradient boosting**), are the strongest general-purpose tools for tables.
3. **Support vector machines, k-nearest neighbours, naive Bayes.** Still useful in niches (naive Bayes is a fine text baseline; k-NN is simple to explain) but rarely the winner on modern tabular data.
4. **Neural networks.** Dominant for images, audio and text. On ordinary tables they usually lose to boosted trees unless the dataset is very large, as Grinsztajn et al. found across 45 benchmark datasets in 2022.

The output is a probability, and you choose the **threshold** that turns it into a decision. A fraud model that flags anything above 0.5 and one that flags anything above 0.1 are the same model with very different behaviour. Choosing that threshold is a business decision about which mistake costs more, and [Training, validation and overfitting](training-validation-and-overfitting.md) shows how to make it with precision and recall.

## Regression

Regression predicts a number. The simplest version, **linear regression**, fits `prediction = w1 x feature1 + w2 x feature2 + ... + b` and is exactly the line-fitting example in [What is machine learning?](what-is-machine-learning.md) with more columns. Tree ensembles do regression too, and capture interactions a straight line misses ("big houses are worth more, but only near the coast").

You judge a regression model by how far off it is, on average, on held-out data:

- **MAE (mean absolute error):** the average size of the miss, in the units you care about ("off by $34,000 on average"). Easy to explain.
- **RMSE (root mean squared error):** like MAE but punishes large misses more. Use it when one big miss is worse than several small ones.
- **R² (coefficient of determination):** the fraction of the variation the model explains, from 1 (perfect) down to 0 (no better than always guessing the average) and below.

Always compare against a dumb baseline: "predict last week's number" or "predict the average". A model that cannot beat that is not ready, however sophisticated it is.

## Clustering

Clustering puts similar rows in the same group without being told what the groups are. **k-means**, the classic algorithm, works like this:

1. Pick `k`, the number of clusters you want.
2. Drop `k` centre points at random.
3. Assign every row to its nearest centre.
4. Move each centre to the average of the rows assigned to it.
5. Repeat 3 and 4 until nothing moves.

It is fast and simple, but it has strong opinions: it assumes roughly round, similar-sized clusters, it needs you to choose `k`, and "nearest" depends entirely on how you scale the columns (a column measured in dollars will swamp one measured in years unless you standardise them). **DBSCAN** and **HDBSCAN** find clusters of any shape and decide the number for you; **hierarchical clustering** gives you a tree of groups you can cut at any level.

The uncomfortable truth about clustering is that there is no right answer to check against. An algorithm will always return clusters, even from random noise. A clustering is useful if the groups are stable (rerun with a different seed and you get roughly the same groups), distinct, and lead to a decision someone can act on ("these 2,000 customers buy only on discount; stop sending them full-price campaigns").

Modern twist: you can cluster text by first turning each document into an **embedding** (a list of numbers that captures meaning) and then clustering the embeddings. That is how support teams discover the twenty themes hidden in 50,000 tickets. [Embeddings and vector search](embeddings-and-vector-search.md) explains embeddings.

## All three in scikit-learn

This runs as is with `pip install scikit-learn` (the housing dataset downloads about 400 KB on first use). It uses three classic teaching datasets that ship with scikit-learn.

```python
from sklearn.datasets import load_breast_cancer, fetch_california_housing, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_absolute_error, adjusted_rand_score

# 1. Classification: is a tumour malignant or benign?
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0, stratify=y)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
clf.fit(X_train, y_train)
print("classification accuracy:", round(accuracy_score(y_test, clf.predict(X_test)), 3))

# 2. Regression: predict a district's median house value
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
for model in [LinearRegression(),
              RandomForestRegressor(n_estimators=100, random_state=0, n_jobs=-1)]:
    model.fit(X_train, y_train)
    mae = mean_absolute_error(y_test, model.predict(X_test))
    print(f"{type(model).__name__}: mean error ${mae * 100_000:,.0f}")

# 3. Clustering: group flowers without looking at the labels
X, y = load_iris(return_X_y=True)
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(StandardScaler().fit_transform(X))
print("cluster sizes:", sorted(int((km.labels_ == k).sum()) for k in range(3)))
print("agreement with true species (ARI):", round(adjusted_rand_score(y, km.labels_), 2))
```

Output with scikit-learn 1.9.1:

```
classification accuracy: 0.958
LinearRegression: mean error $53,690
RandomForestRegressor: mean error $33,838
cluster sizes: [47, 50, 53]
agreement with true species (ARI): 0.62
```

What to notice:

- Every supervised model is scored on `X_test`, rows it never saw during `fit`. That is the whole discipline in one line.
- The forest cuts the regression error by about a third compared with the straight line, because house prices depend on combinations of features (location times size) that a line cannot express.
- The clustering step never sees `y`. We only use the true species afterwards to check how well k-means rediscovered them. An adjusted Rand index of 0.62 means "clearly related, far from perfect": two of the three iris species overlap in measurements, and k-means cannot separate what the data does not separate. In real clustering work you have no `y` to check against, which is why the judgement is harder.
- `StandardScaler` appears twice. Logistic regression and k-means both care about column scale; trees do not.

## Where this sits next to LLMs

Language models changed what is possible with unstructured data, and teams now reach for them by reflex. For structured prediction, a classic model is usually the better engineering choice:

| | Classic model on a table | LLM prompted with the row |
|---|---|---|
| Cost per prediction | Fractions of a millisecond of CPU | Tokens on every call |
| Needs labelled data | Yes, hundreds to thousands of rows | No (zero-shot), but accuracy is unproven until you test |
| Explainability | Weights or feature importances | A plausible-sounding rationale that may not reflect the computation |
| Consistency | Same input, same output | Can vary between calls |
| Good at | Numbers, categories, many rows | Free text, judgement calls, few or no labels |

The hybrid that works well in practice: use an LLM (or an embedding model) to turn messy text into features or draft labels, check a sample by hand, then train a small classic model on them. You get the LLM's understanding once, and the classic model's speed and cost on every prediction after that.

## Common mistakes

- **Starting with the fanciest model.** Fit logistic or linear regression first. If a boosted-tree model only beats it by a hair, ship the simple one.
- **Testing on the training data.** Every number you report must come from rows the model never saw. See [Training, validation and overfitting](training-validation-and-overfitting.md).
- **Calling it classification when it is ranking or forecasting.** "Which 100 leads should sales call?" is a ranking problem; "how many calls next Tuesday?" is a time-series forecast, where a random train/test split leaks the future into the past. Split by time.
- **Forgetting to scale features** for distance-based methods (k-means, k-NN, SVMs, logistic regression with regularisation).
- **Treating clusters as facts.** Clusters are a lens you chose (via `k`, scaling and features). Check they are stable and useful before naming them in a slide.
- **Accuracy on imbalanced data.** If 1% of transactions are fraud, a model that always says "not fraud" is 99% accurate and useless. Use precision and recall instead.

## Next steps

- [Training, validation and overfitting](training-validation-and-overfitting.md): splits, cross-validation, and the metrics that matter
- [Recommender systems basics](recommender-systems-basics.md): a classic ML system you use every day
- [Neural networks in plain English](neural-networks-plain-english.md): what changes when the model is a network
- [ML engineer path](../start-here/ml-engineer-path.md) and [Deploy an ML model](../../build/projects/deploy-ml-model.md)
- For data preparation, pipelines and warehouses, see the sibling site [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- scikit-learn user guide, "Supervised learning" and "Unsupervised learning": https://scikit-learn.org/stable/supervised_learning.html, https://scikit-learn.org/stable/unsupervised_learning.html
- scikit-learn, "Choosing the right estimator": https://scikit-learn.org/stable/machine_learning_map.html
- Grinsztajn, Oyallon and Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (NeurIPS 2022 Datasets and Benchmarks): https://arxiv.org/abs/2207.08815
- Chen and Guestrin, "XGBoost: A Scalable Tree Boosting System" (KDD 2016): https://arxiv.org/abs/1603.02754
- Code output above produced with scikit-learn 1.9.1 on 2026-10-21.
