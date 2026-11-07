# ML Engineer Roadmap

**In one line:** A staged plan from software or data skills to a classical-plus-LLM ML engineer role, with what to learn, what to build and how it differs from the AI engineer path.
**Last reviewed:** 2026-11-07

---

## The short version

- An **ML engineer** trains, evaluates, deploys and monitors models, including ones you train yourself. An [AI engineer](ai-engineer-roadmap.md) mostly builds on models someone else trained. The line is blurry; see the [AI careers map](ai-careers-map.md).
- Order of learning: Python and data handling, classical ML and evaluation, deep learning, then serving and monitoring, then LLM-specific training and fine-tuning.
- Hiring teams look for end-to-end evidence: a model you trained, measured honestly, deployed and watched. Notebooks alone are weak evidence.
- This page is judgment drawn from this site's own guides. It contains no salary or job-market figures because none were sourced.

## Stage 1: foundations

- [Python for AI](../../learn/day-one/python-for-ai.md), [notebooks and Colab](../../learn/day-one/notebooks-and-colab.md), [maths for ML without fear](../../learn/day-one/maths-for-ml-without-fear.md).
- SQL and data handling. The [data site](https://data.noblerworks.com/) covers this in depth.

## Stage 2: classical ML and honest evaluation

- [What is machine learning](../../learn/concepts/what-is-machine-learning.md), [supervised vs unsupervised](../../learn/concepts/classic-ml-supervised-vs-unsupervised.md), [training, validation and overfitting](../../learn/concepts/training-validation-and-overfitting.md).
- [Decision trees and gradient boosting](../../learn/concepts/decision-trees-and-gradient-boosting.md), [feature engineering](../../learn/concepts/feature-engineering-and-data-prep.md), [time series](../../learn/concepts/time-series-forecasting.md), [recommenders](../../learn/concepts/recommender-systems-basics.md).
- **Build:** [tabular ML end to end](../../build/projects/tabular-ml-end-to-end.md). Keep a simple baseline and beat it by a measured margin.

## Stage 3: deep learning

- [Neural networks in plain English](../../learn/concepts/neural-networks-plain-english.md), [CNNs](../../learn/concepts/convolutional-networks-and-computer-vision.md), [transformer architecture](../../learn/concepts/transformer-architecture.md), [reinforcement learning basics](../../learn/concepts/reinforcement-learning-basics.md).
- Read a few foundational papers with the summaries: [Attention Is All You Need](../../papers/architectures/01-attention-is-all-you-need/summary.md).

## Stage 4: production

- [Deploy an ML model](../../build/projects/deploy-ml-model.md), [set up an eval harness](../../build/projects/set-up-eval-harness.md), [GPUs for AI](../../learn/concepts/gpus-for-ai.md), [inference servers](../../learn/concepts/inference-servers.md), [quantization and distillation](../../learn/concepts/quantization-and-distillation.md).
- Learn what breaks after launch: data drift, silent label changes, training-serving skew, cost. The [cloud site](https://cloud.noblerworks.com/) helps with the infrastructure side.

## Stage 5: LLM-era skills

- [Fine-tuning vs RAG](../../learn/concepts/fine-tuning-vs-rag.md), then [fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md) and [run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md).
- [How LLMs are trained](../../learn/concepts/how-llms-are-trained.md) and [evals for LLMs](../../learn/concepts/evals-for-llms.md).

## What to show

Pick three artefacts: a tabular model with a leakage-safe evaluation, a deployed model with monitoring, and one fine-tune with before and after numbers. Package them as in [build an AI portfolio](build-an-ai-portfolio.md).

## Common mistakes

- Jumping to deep learning before you can beat a baseline with gradient boosting.
- Reporting one lucky split. Use a held-out set you touched once.
- Treating deployment as someone else's job.

## Next steps

- [ML engineer path](../../learn/start-here/ml-engineer-path.md) (the learning order) and [ML engineer interview](../interviews/ml-engineer-interview.md).
- [Data scientist in the LLM era](data-scientist-in-the-llm-era.md) if you lean toward analysis.
- [AI certifications guide](../certifications/ai-certifications-guide.md).

## Sources

- Judgment: the staging above is this site's editorial view, not drawn from a hiring survey.
- Linked pages on this site hold the sourced detail for each topic.
