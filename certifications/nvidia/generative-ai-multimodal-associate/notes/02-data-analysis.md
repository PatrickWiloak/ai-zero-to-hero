# Section 2: Data Analysis (10%)

**Last reviewed:** 2026-11-07

Data analysis here means getting insight out of datasets before and after modeling: mining and visualizing, attention maps in multimodal models, charts, and spotting relationships and trends that could affect results. The four objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07) were the gap the old guide listed as "not covered". The page names no tools beyond "specialized software"; the reading list includes Interpretable Machine Learning (Molnar), Hugging Face Evaluate and the Hugging Face LLM Course. Code ran on CPU (PyTorch 2.15.0+cpu, pandas, scikit-learn).

## Extracting insight from large datasets

Mining and visualization answer three questions before any model is trained: what is in the data (distributions, class balance, missing values), how its parts relate (correlations, associations between modalities), and what is wrong with it (duplicates, empties, outliers). For multimodal data the checks run per modality and across pairs: image sizes and corrupt files, caption length and empties, and whether each image has a caption. I ran a small data-quality audit on an image-caption table:

```python
df = pd.DataFrame({"img": ["a.png","b.png","c.png","c.png",None],
                   "caption": ["a cat","","a dog","a dog","a bird"], "w": [224,224,0,0,224]})
```

```
data quality: duplicates 1 | missing {'img': 1, 'caption': 0, 'w': 0} | empty captions 1 | zero-width images 2
```

Five rows, and four distinct problems: a duplicate pair, a missing image path, an empty caption and zero-width (corrupt) images. A model trained on this would learn from broken pairs. The exam objective is the habit: audit first, report counts, then decide to fix or drop.

## Attention maps in multimodal settings

An **attention map** shows how much each position attends to every other: a matrix of weights where each row sums to one. In a multimodal model, cross-attention maps show which image regions a word attends to (or which words a patch attends to), and they are a common way to inspect what the model is looking at. PyTorch's `nn.MultiheadAttention` returns them when asked:

```python
mha = nn.MultiheadAttention(16, 2, batch_first=True)
out, w = mha(q, q, q, need_weights=True, average_attn_weights=True)
```

```
attention weights shape (1, 5, 5) rows sum to [1.0, 1.0, 1.0, 1.0, 1.0]
```

For five tokens the map is 5 by 5, and each row is a probability distribution. To visualize, plot the matrix as a heat map (matplotlib's `imshow`), or for image patches reshape one row back to the patch grid and overlay it on the image. Attention maps show where the model attended, which is related to but not the same as why it predicted something; Molnar's *Interpretable Machine Learning* (on the reading list) discusses the limits of explanation methods, and I did not fetch it.

- **Attention map** - the matrix of attention weights between positions (tokens or image patches), where each row is a probability distribution; used to inspect what a model attends to.
- **Cross-attention** - attention where queries come from one modality and keys and values from another (for example text attending to image patches).

## Graphs, charts and visualizations

The objective is to "create graphs, charts, and other visualizations with specialized software". Match the plot to the question: histograms for distributions, scatter plots and heat maps for relationships, line plots for training curves over steps, confusion matrices for classification errors, and image grids with captions for multimodal spot checks. I did not render any plots for this guide, so no plot output is shown; the skill being tested is the choice of plot for the question, not the plotting call.

## Relationships, trends and confounders

To identify "relationships, trends, and factors that could affect research results", look for correlation (but do not infer causation), shifts over time (data collected in different periods), and imbalance across subgroups. A useful concrete check is **permutation importance**: shuffle one feature at a time and measure how much the score drops. I ran it on a six-feature problem with two informative features:

```
permutation importance (6 features, 2 informative): [0.0, 0.005, 0.075, 0.0, 0.001, 0.513]
```

Two features carry almost all the importance (0.513 and 0.075) and the rest are near zero, which matches how the data was built. The same method tells you which input a model really relies on, such as whether a multimodal classifier depends on the image or only on the text.

- **Permutation importance** - a measure of how much a model's score drops when one feature's values are shuffled; a large drop means the model relies on that feature.

## Check yourself against the objectives

Run an audit that reports duplicates, missing values and empties; say what an attention map is and how to plot one; choose a chart for a question; and use permutation importance to say which input a model relies on. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
