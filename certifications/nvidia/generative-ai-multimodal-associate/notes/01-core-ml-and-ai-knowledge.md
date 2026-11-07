# Section 1: Core Machine Learning and AI Knowledge (20%)

**Last reviewed:** 2026-11-07

The first section is the fundamentals: how multimodal models are trained stably, what loss functions tie modalities together, ML basics (feature engineering, model comparison, cross-validation), residual connections, transfer learning, prompt engineering and the frameworks. The ten objectives are on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07); NVIDIA publishes no separate study guide PDF, only the blueprint and a reading list. This note follows the objectives in order.

All code ran on CPU in a scratch virtual environment (PyTorch 2.15.0+cpu, scikit-learn 1.9.1); the outputs are real. The models are tiny toys built to show a mechanism, not to say anything about production models.

## Multimodal loss functions

A multimodal model must learn that an image and its caption belong together. The standard tool is a **contrastive loss**: embed images and texts into the same space, compute all pairwise similarities in a batch, and train the matching pairs to score highest. OpenAI's CLIP paper describes its pre-training task as "predicting which caption goes with which image", run on a dataset of 400 million (image, text) pairs collected from the internet, which lets the model recognize concepts described in plain language, including ones it never saw labeled.

**[📖 CLIP paper (arXiv 2103.00020)](https://arxiv.org/abs/2103.00020)** - Contrastive image-text pretraining and zero-shot transfer

I wrote the loss in a few lines: normalize image and text embeddings, compute a temperature-scaled similarity matrix, and apply cross-entropy in both directions with the diagonal as the label:

```python
logits = scale * img @ txt.T            # scale = 1/0.07
labels = torch.arange(B)
loss = (F.cross_entropy(logits, labels) + F.cross_entropy(logits.T, labels)) / 2
```

```
contrastive loss matched pairs 0.000 | random pairing 10.715 | diag acc 1.00
```

With embeddings built so that each text sits next to its image, the loss is near zero; shuffle the pairing and it jumps to 10.7. The loss measures whether the right pair wins against every other pair in the batch, which is why contrastive training likes large batches (more negatives).

- **Contrastive loss** - a loss that pulls matching pairs (an image and its caption) together in embedding space and pushes non-matching pairs apart.
- **Zero-shot classification (CLIP)** - classifying images into categories described in text without training on those labels, by comparing the image embedding with text embeddings of the class names.

## Training stability in multimodal settings

Multimodal training is fragile because two encoders with different scales and learning dynamics are optimized together. Tools for stability: gradient clipping, a learning-rate warmup and decay, normalizing embeddings before comparing them, mixed precision with care for overflow, and monitoring the loss for NaNs. PyTorch's `clip_grad_norm_` rescales gradients in place so their total norm does not exceed `max_norm`, and returns the total norm before clipping. I clipped a deliberately exploding gradient:

```
grad norm before clip 6051.6 -> after 1.000 (returned total norm 6051.6)
```

**[📖 torch.nn.utils.clip_grad_norm_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.clip_grad_norm_.html)** - Parameters and return value

The `error_if_nonfinite` option raises an error when the norm is NaN or infinite, which turns silent divergence into a visible failure.

- **Gradient clipping** - rescaling gradients so their norm does not exceed a limit, which prevents exploding updates.

## ML fundamentals: feature engineering, model comparison, cross-validation

Feature engineering turns raw data into inputs a model can use (scaling, encoding, imputing; for multimodal work, extracting embeddings per modality). Model comparison means evaluating candidates on the same data with the same metric. Cross-validation estimates generalization by training k times on different splits and averaging; in my run a random forest on a 600-row problem scored `0.947 +- 0.025` over five folds, a better summary than one split's single number. The exam objective says "apply ML fundamentals"; the scikit-learn reading list item covers cross-validation, model evaluation and imputation.

- **Cross-validation** - estimating performance by training on k different splits and averaging the held-out scores.

## Nonsequential networks and residual connections

A **residual connection** adds a layer's input to its output (`x + f(x)`), giving gradients a direct path back through a deep network. I built a 40-layer tanh stack with and without it and looked at the gradient reaching the first and last blocks:

```
depth 40 residual=False: first-block grad norm 1.41e-11, last-block grad norm 2.59e-02
depth 40 residual=True: first-block grad norm 1.34e+01, last-block grad norm 5.35e+00
```

Without residuals, the gradient at the first block is about nine orders of magnitude smaller than at the last (vanishing gradients); with them it is the same order of magnitude. That is why ResNets, transformers and U-Nets all use skip connections. "Nonsequential" refers to this: networks whose data flow is not a single chain (skip connections, branches, multiple encoders feeding a fusion layer).

- **Residual connection** - a skip connection that adds a block's input to its output, so gradients flow through deep networks.

## Statistical analyses for multimodal pipelines

Evaluating a pipeline statistically means reporting more than one run's accuracy: repeat with different seeds or folds and report mean and spread, compare systems on the same splits, and use a test (a paired comparison) before claiming one is better. My cross-validation result shows the pattern (mean with standard deviation). This objective is about method; the sources fetched for this guide do not prescribe a specific test.

## Transfer learning for multimodal models

Transfer learning starts from a pretrained model and adapts it. The cheapest form freezes the pretrained backbone and trains only a new head. On a toy backbone plus head:

```
transfer learning: trainable 325 of 16901 parameters (1.9%)
```

Only 1.9 percent of the parameters train. Multimodal-specific variants: reuse a pretrained image encoder and a pretrained text encoder and learn only the projection or fusion layers, or fine-tune both encoders with a small learning rate.

- **Transfer learning** - adapting a pretrained model to a new task, often by freezing its backbone and training a new head.

## Prompt engineering, frameworks, emerging trends, and trustworthy models

- **Prompt engineering principles** (be specific, give context and format, give examples, iterate) are on NVIDIA's reading list via the Prompt Engineering Guide; this guide did not fetch it, so the principles are standard practice rather than quoted.
- **Frameworks:** the objective names TensorFlow and PyTorch. Everything here is PyTorch; the Keras developer guide is on the reading list.
- **Emerging trends** (the objective is to track them) cannot be tested from fixed facts; the NVIDIA page lists CLIP, diffusion and fusion as the current core ideas.
- **Energy-efficient, trustworthy models:** efficiency tools are in note 5 (mixed precision, quantization, pruning) and trustworthiness in note 7.

## Check yourself against the objectives

Write the contrastive loss from memory; say why residual connections matter; say what clipping does; compute what fraction of a model trains when its backbone is frozen; and explain why cross-validation gives a better estimate than one split. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
