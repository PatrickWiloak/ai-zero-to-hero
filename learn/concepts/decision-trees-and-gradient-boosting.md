# Decision Trees and Gradient Boosting

**In one line:** Understand how a decision tree makes predictions and why hundreds of small trees, built one after another (gradient boosting), are the default winner on tables of data.
**Last reviewed:** 2026-11-07

---

## The short version

- A **decision tree** is a flowchart learned from data: a chain of yes/no questions about the columns, ending in a prediction. You can read it.
- One deep tree memorises its training data and does worse on new data. That is overfitting.
- A **random forest** averages many different trees. **Gradient boosting** builds trees in sequence, each one correcting the errors left by the ones before it.
- On rows-and-columns data, gradient-boosted trees (XGBoost, LightGBM, CatBoost, scikit-learn's `HistGradientBoosting*`) are usually the strongest option and a strong default. Deep networks are often not better on this kind of data.
- Trees do not need feature scaling and cope with mixed column types and missing values, which saves prep work. See [Feature engineering and data prep](feature-engineering-and-data-prep.md).

## How one tree decides

At each step the algorithm picks the single question that best separates the examples, such as "is `worst radius` at most 16.8?". "Best" means the two groups come out as pure as possible, measured by a score like **Gini impurity** or entropy. It then repeats inside each group until it hits a stopping rule (maximum depth, minimum group size) and writes down the majority answer at each end point, called a **leaf**.

Here is a real depth-2 tree fitted to scikit-learn's built-in breast cancer dataset (569 rows, 30 measurements, benign or malignant):

```
|--- worst radius <= 16.80
|   |--- worst concave points <= 0.14
|   |   |--- class: 1
|   |--- worst concave points >  0.14
|   |   |--- class: 0
|--- worst radius >  16.80
|   |--- texture error <= 0.47
|   |   |--- class: 1
|   |--- texture error >  0.47
|   |   |--- class: 0
```

You can follow it by hand. That readability is the tree's selling point, and it is why trees are common where decisions must be explained.

## The overfitting problem

Let a tree grow without limit and it will carve out a leaf for nearly every training row. Measured on the same dataset (run 2026-11-07, scikit-learn 1.9.1, 80/20 split, same seed):

| Model | Accuracy on training rows | Accuracy on held-out rows |
|---|---|---|
| Unlimited single tree | 1.000 | 0.912 |
| Depth-2 tree | 0.958 | 0.895 |
| Gradient boosting | 1.000 | 0.956 |

A perfect training score with a lower test score is the signature of memorising. See [Training, validation and overfitting](training-validation-and-overfitting.md). One small test split is noisy, so treat the gaps as a picture of the idea, not a benchmark; the [tabular project](../../build/projects/tabular-ml-end-to-end.md) uses cross-validation for firmer numbers.

## Ensembles: many weak trees beat one strong one

- **Bagging and random forests.** Train many trees, each on a random resample of the rows (and a random subset of columns at each split), then average their votes. Errors that are random cancel out. Trees train independently, so it parallelises easily. Breiman introduced the random forest in 2001.
- **Boosting.** Train a small tree. Look at where it is wrong. Train the next tree to predict those *errors* (more precisely, the gradient of the loss, hence "gradient" boosting). Add it in with a small weight called the **learning rate**. Repeat a few hundred times. Each tree is weak; the sum is strong. Friedman described the method in 2001.

The same gradient idea powers neural network training; see [Maths for ML without fear](../day-one/maths-for-ml-without-fear.md). The difference is that boosting adds a new tree each round, while a network adjusts weights it already has.

## The main libraries

| Library | Note |
|---|---|
| scikit-learn `HistGradientBoostingClassifier` / `Regressor` | Built in, fast, handles missing values; a good first stop |
| XGBoost | The library behind many competition wins; described in Chen and Guestrin (2016) |
| LightGBM | Fast on large data; grows trees leaf-wise |
| CatBoost | Handles text-like category columns natively |

Check each project's documentation for current options; defaults and features change between versions.

## Knobs that matter

- **Number of trees** and **learning rate**: they trade against each other. Lower rate needs more trees. Use early stopping on a validation set to choose the count.
- **Tree depth**: shallow trees (3 to 8 levels) usually generalise best in boosting.
- **Minimum samples per leaf** and regularisation: bigger values smooth the model.

Tune on a validation split or cross-validation, never on the final test set.

## Why not always use a neural network?

Grinsztajn, Oyallon and Varoquaux (2022) compared tree-based models against deep learning on a set of medium-sized tabular datasets and found trees still ahead, with the gap explained partly by uninformative columns and uneven, jumpy relationships that trees handle well. That is a finding for medium-sized tables, not a law: with very large data, mixed text or images, networks win. Always run the baseline first.

## Common mistakes

- **Reporting training accuracy.** Report held-out or cross-validated scores.
- **Leaking the answer.** A column computed after the outcome (for example "refund issued" when predicting cancellation) makes scores look wonderful and fail in production.
- **Trusting feature importance as cause.** Importance says what the model used, not what would change the outcome.
- **Skipping the simple baseline.** If logistic regression ties the boosted model, ship the simple one.

## Next steps

- [Classic ML: supervised vs unsupervised](classic-ml-supervised-vs-unsupervised.md)
- [Feature engineering and data prep](feature-engineering-and-data-prep.md)
- [Tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md): train, compare, evaluate and save a model
- [Time-series forecasting](time-series-forecasting.md): boosted trees are a common forecasting tool too
- Tables, pipelines and warehouses: [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- scikit-learn user guide, "Decision Trees": https://scikit-learn.org/stable/modules/tree.html
- scikit-learn user guide, "Ensembles: gradient boosting, random forests, bagging, voting, stacking": https://scikit-learn.org/stable/modules/ensemble.html
- Breiman, "Random Forests", *Machine Learning* 45 (2001): https://link.springer.com/article/10.1023/A:1010933404324
- Friedman, "Greedy function approximation: a gradient boosting machine", *Annals of Statistics* 29 (2001): https://doi.org/10.1214/aos/1013203451
- Chen and Guestrin, "XGBoost: A Scalable Tree Boosting System" (2016): https://arxiv.org/abs/1603.02754
- Grinsztajn, Oyallon and Varoquaux, "Why do tree-based models still outperform deep learning on tabular data?" (2022): https://arxiv.org/abs/2207.08815
- Code in this page run locally with scikit-learn 1.9.1 on 2026-11-07, using the dataset bundled with scikit-learn (`load_breast_cancer`).
