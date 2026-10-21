# ML Engineer Interview Guide

**In one line:** ML engineer interviews test ML fundamentals, deep learning, ML coding, ML system design and production operations; use the sample questions and strong-answer outlines below to prepare each round, and practise explaining trade-offs out loud.
**Last reviewed:** 2026-10-21

---

## The short version

- ML engineer loops usually have **five kinds of rounds**: coding, ML fundamentals, ML coding (implement an algorithm or training loop), ML system design, and behavioural. Larger companies may add a research-depth or domain round.
- Interviewers want to see that you can **frame a problem as ML**, pick a sensible **baseline**, choose the right **metric**, avoid **leakage**, and **ship and monitor** a model, not only train it.
- The LLM era added questions on **fine-tuning, efficient training and serving, and evaluation of generative models**. Classical ML has not disappeared from interviews.
- Prepare one or two projects where you can discuss data, metric choice, model choice, failures and production results in detail.

## What the loop usually looks like

| Round | What they test | Preparation |
|---|---|---|
| Coding | Data structures, algorithms, clean Python | Standard coding practice |
| ML fundamentals | Theory and intuition: bias-variance, regularisation, metrics, evaluation | Questions below; a classic textbook |
| ML coding | Implement an algorithm or a training loop from scratch | NumPy and PyTorch practice |
| ML system design | Design an end-to-end ML system | Framework below; [AI system design interview](ai-system-design-interview.md) for LLM systems |
| Production / MLOps | Deployment, monitoring, drift, retraining | [Deploy an ML model](../../build/projects/deploy-ml-model.md), [AI/ML pipeline](../../build/patterns/ai-ml-pipeline.md) |
| Behavioural | Ownership, collaboration, judgement | STAR stories |

## ML fundamentals

**Q: Explain the bias-variance trade-off and how you diagnose which one you have.**

- Bias: error from a model too simple to capture the pattern (underfitting). Variance: error from sensitivity to the particular training data (overfitting).
- Diagnose with learning curves: high training and validation error means high bias; low training error with a large gap to validation error means high variance.
- High bias: bigger model, better features, less regularisation. High variance: more data, regularisation, simpler model, early stopping, augmentation.
- Note that very large neural networks complicate the classic picture (double descent), but the diagnostic habit still applies.

**Q: You have a fraud dataset with 0.1% positives. What metric do you use and why?**

- Accuracy is useless (99.9% by predicting "not fraud").
- Use precision and recall, the precision-recall curve and its area, and choose an operating threshold from business costs (cost of a missed fraud vs a blocked legitimate customer).
- ROC AUC can look good with heavy imbalance; PR AUC is more informative.
- Handle imbalance with class weights, resampling or threshold tuning, and evaluate on the real distribution.

**Q: What is data leakage? Give two examples.**

- Information available at training time that would not be available at prediction time, inflating offline metrics.
- Examples: a feature computed using the target or future data (for example "account closed" when predicting churn); normalising with statistics computed on the whole dataset before splitting; random splits on time-series data; the same user in train and test.
- Prevent with time-based splits, feature pipelines fitted on training data only, and group-aware splits.

**Q: L1 vs L2 regularisation?**

- L2 penalises squared weights, shrinking them smoothly; L1 penalises absolute values and drives some weights exactly to zero (feature selection).
- In neural networks, weight decay is the common L2-style form; dropout and early stopping are other regularisers.

**Q: How do you choose between gradient-boosted trees and a neural network for tabular data?**

- Gradient-boosted trees (XGBoost, LightGBM) are usually the strong default for tabular data: fast, robust, little tuning, handle mixed types.
- Neural networks help with very large datasets, unstructured inputs combined with tabular features, or when you need embeddings shared with other models.
- Always start with a simple baseline and compare.

## Deep learning

**Q: Walk me through backpropagation.**

- Forward pass computes outputs and loss; backward pass applies the chain rule layer by layer from the loss to compute the gradient of the loss with respect to every parameter; an optimiser updates parameters with those gradients.
- Frameworks do this with automatic differentiation over the computation graph.

**Q: Why is Adam popular, and when might you not use it?**

- Adam keeps running averages of gradients and squared gradients, giving per-parameter adaptive step sizes with momentum; it converges quickly with little tuning.
- AdamW decouples weight decay and is the standard for transformers. SGD with momentum can generalise better in some vision settings. Newer optimisers such as Muon are being explored for large models.
- Read: [Adam](../../papers/techniques/142-adam/summary.md), [Muon](../../papers/techniques/144-muon/summary.md).

**Q: Explain self-attention and why transformers replaced RNNs.**

- Each token builds a query, key and value; attention weights come from query-key similarity (scaled dot product, softmax); output is the weighted sum of values. Multiple heads attend to different patterns.
- Transformers process all positions in parallel during training (RNNs are sequential), handle long-range dependencies better, and scale well on GPUs.
- Cost: attention is quadratic in sequence length, which motivated FlashAttention, grouped-query attention and state-space alternatives.
- Read: [Attention Is All You Need](../../papers/architectures/01-attention-is-all-you-need/summary.md), [transformer architecture](../../learn/concepts/transformer-architecture.md), [FlashAttention](../../papers/techniques/16-flash-attention/summary.md), [GQA](../../papers/architectures/75-grouped-query-attention/summary.md), [Mamba](../../papers/architectures/20-mamba/summary.md).

**Q: Your training loss is not going down. What do you check?**

- Data and labels (are they aligned? shuffled correctly?), learning rate (too high diverges, too low stalls), initialisation, a bug in the loss or masking, gradients (vanishing or exploding; check norms), normalisation.
- First try to overfit a tiny batch: if you cannot, there is a bug.

**Q: How does LoRA work, and why is it popular for fine-tuning LLMs?**

- Freeze the pre-trained weights and learn a low-rank update (two small matrices) for selected layers; the update is added to the frozen weights.
- Trains a tiny fraction of parameters, cuts memory and storage, lets you keep many adapters for one base model. QLoRA adds 4-bit quantisation of the frozen base to fit larger models on one GPU.
- Read: [LoRA](../../papers/techniques/10-lora/summary.md), [QLoRA](../../papers/techniques/22-qlora/summary.md), [fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md).

**Q: How are very large models trained across many GPUs?**

- Data parallelism (replicate the model, split the batch), tensor parallelism (split layers across GPUs), pipeline parallelism (split layers into stages), and sharding of optimiser states, gradients and parameters (ZeRO / FSDP).
- Mixed precision to save memory and increase speed.
- Read: [ZeRO and Megatron-LM](../../papers/techniques/76-zero-megatron/summary.md), [mixed precision training](../../papers/techniques/143-mixed-precision-training/summary.md).

## ML coding

A common prompt: "Implement logistic regression with gradient descent in NumPy." A clean answer:

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def train_logreg(X, y, lr=0.1, epochs=1000, l2=0.0):
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    for _ in range(epochs):
        p = sigmoid(X @ w + b)                 # predictions, shape (n,)
        grad_w = X.T @ (p - y) / n + l2 * w    # gradient of mean log loss + L2
        grad_b = np.mean(p - y)
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b

def log_loss(X, y, w, b, eps=1e-12):
    p = np.clip(sigmoid(X @ w + b), eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
```

Talk while you write: shapes, why the gradient is `X.T @ (p - y) / n`, numerical stability (clipping, or a stable sigmoid), how you would test it (a separable toy dataset; compare with scikit-learn), and how you would add mini-batches. Other common asks: k-means, a decision-tree split, a PyTorch training loop with validation, scaled dot-product attention, or top-k sampling.

## ML system design

Use a consistent structure:

1. **Clarify the goal and constraints**: business objective, scale, latency, what "good" means.
2. **Frame as ML**: prediction target, input, label source, offline metric that tracks the business metric.
3. **Data**: sources, labelling, splits (time-aware), leakage risks, privacy.
4. **Features and baseline**: start simple (heuristic or linear model, then gradient-boosted trees).
5. **Model**: what and why; candidate generation and ranking stages for recommenders.
6. **Evaluation**: offline metrics, then online A/B test with guardrail metrics.
7. **Serving**: batch vs real-time, latency budget, feature store, caching.
8. **Monitoring and retraining**: data and prediction drift, performance with delayed labels, retraining triggers, rollback.
9. **Risks**: fairness, feedback loops, abuse.

**Practice prompts:** design a recommendation system for an e-commerce home page; design fraud detection for card payments; design spam detection for a messaging app; design search ranking for a marketplace; design an ETA prediction service for deliveries.

**Q: How do you detect and handle model drift in production?**

- Monitor input feature distributions (population stability, statistical distance), prediction distributions, and, when labels arrive, actual performance by segment.
- Distinguish data drift (inputs change) from concept drift (the relationship changes).
- Respond with alerts, investigation, retraining on recent data, or rollback; schedule retraining if drift is regular.

**Q: When is an offline improvement not an online improvement?**

- Offline metric does not match the business metric; leakage inflated offline results; feedback loops (the model changes the data it later sees); latency changes user behaviour; novelty effects in A/B tests.
- Always confirm with a controlled online experiment.

## LLM-era questions for ML engineers

- "How would you evaluate a fine-tuned LLM?" Task-specific test sets, held-out data, human or LLM-judge evaluation with calibration, regression checks on general capability, safety checks. See [evals for LLMs](../../learn/concepts/evals-for-llms.md).
- "How do RLHF and DPO differ?" RLHF trains a reward model on preferences then optimises the policy with RL (often PPO); DPO optimises directly on preference pairs without a separate reward model or RL loop. See [InstructGPT](../../papers/language-models/05-instructgpt-rlhf/summary.md), [PPO](../../papers/techniques/63-ppo/summary.md), [DPO](../../papers/language-models/19-dpo/summary.md).
- "How would you serve a 70B model cost-effectively?" Quantisation, a serving engine with continuous batching and paged KV cache, tensor parallelism across GPUs, speculative decoding, autoscaling on queue depth. See [LLM serving](../../tools/decisions/llm-serving.md), [PagedAttention](../../papers/techniques/52-pagedattention-vllm/summary.md), [speculative decoding](../../papers/techniques/45-speculative-decoding/summary.md).
- "What are scaling laws and why do they matter?" Loss falls predictably with compute, data and parameters; Chinchilla showed many models were under-trained on data for their size. See [scaling laws](../../papers/techniques/12-scaling-laws/summary.md), [Chinchilla](../../papers/techniques/18-chinchilla/summary.md).

## Behavioural

- "Tell me about a model that failed in production." Detection, diagnosis, fix, prevention.
- "Describe a time you chose a simpler model." Judgement over novelty.
- "How did you handle a disagreement with a data scientist or product manager about a metric?"

## Common mistakes

- **Jumping to a deep model** before a baseline.
- **Not mentioning the metric** or picking accuracy for imbalanced data.
- **Forgetting leakage and time-based splits.**
- **Stopping at training.** Production, monitoring and retraining are half of the job.
- **Memorised answers without intuition.** Interviewers follow up with "why?".

## Next steps

- [AI engineer interview](ai-engineer-interview.md) and [AI system design interview](ai-system-design-interview.md)
- [ML engineer path](../../learn/start-here/ml-engineer-path.md) and [AI careers map](../roles/ai-careers-map.md)
- Hands-on: [deploy an ML model](../../build/projects/deploy-ml-model.md), [fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md)
- Concepts: [what is machine learning](../../learn/concepts/what-is-machine-learning.md), [neural networks in plain English](../../learn/concepts/neural-networks-plain-english.md)

## Sources

- Kingma and Ba, "Adam: A Method for Stochastic Optimization" (2014): https://arxiv.org/abs/1412.6980
- Loshchilov and Hutter, "Decoupled Weight Decay Regularization" (AdamW, 2017): https://arxiv.org/abs/1711.05101
- Hu et al., "LoRA" (2021): https://arxiv.org/abs/2106.09685
- Rafailov et al., "Direct Preference Optimization" (2023): https://arxiv.org/abs/2305.18290
- Davis and Goadrich, "The Relationship Between Precision-Recall and ROC Curves" (ICML 2006): https://www.biostat.wisc.edu/~page/rocpr.pdf
- Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022): https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/
