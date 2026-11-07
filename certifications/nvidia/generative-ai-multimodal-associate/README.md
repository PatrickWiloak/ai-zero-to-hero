# NVIDIA-Certified Associate - Generative AI Multimodal (NCA-GENM)

**Last reviewed:** 2026-11-07, against the [official exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/).

## Exam Overview

An associate-level certification for developers contributing to multimodal generative AI (text, image and audio): model development, programming and quality assurance. NVIDIA's name for it is "NVIDIA Generative AI Multimodal Certification Exam"; the code is **NCA-GENM** (this guide called it NCA-MMGA until 2026-10-22).

**Exam facts (from the exam page, 2026-11-07):**
- **Exam code:** NCA-GENM
- **Duration:** 1 hour
- **Questions:** 50 multiple choice (the page says "50-60" in one place and 50 in another)
- **Price:** $125
- **Delivery:** Online, proctored remotely; a digital badge and optional certificate follow a pass
- **Level:** Associate
- **Validity:** Two years from issuance; recertify by retaking the exam
- **Language:** English
- **Labs:** None listed
- **Prerequisites:** A basic understanding of generative AI
- **Passing score:** Not published
- **Study guide PDF:** None listed; the page links reading materials and courses only

## Exam Blueprint

Seven sections in NVIDIA's order. Each note covers one section, objective by objective.

| # | Section | Weight | Note |
|---|---------|-------:|------|
| 1 | Core Machine Learning and AI Knowledge | 20% | [01-core-ml-and-ai-knowledge.md](notes/01-core-ml-and-ai-knowledge.md) |
| 2 | Data Analysis | 10% | [02-data-analysis.md](notes/02-data-analysis.md) |
| 3 | Experimentation | 25% | [03-experimentation.md](notes/03-experimentation.md) |
| 4 | Multimodal Data | 15% | [04-multimodal-data.md](notes/04-multimodal-data.md) |
| 5 | Performance Optimization | 10% | [05-performance-optimization.md](notes/05-performance-optimization.md) |
| 6 | Software Development | 15% | [06-software-development.md](notes/06-software-development.md) |
| 7 | Trustworthy AI | 5% | [07-trustworthy-ai.md](notes/07-trustworthy-ai.md) |

The notes were rewritten on 2026-11-07 to match this blueprint one-to-one. The earlier notes (May 2026) used a different outline, had no data analysis coverage, and described NVIDIA products without running anything.

## How the code in these notes was checked

Unlike the other NVIDIA exams, this one can be practiced entirely on a laptop CPU. The code in the notes ran in a throwaway virtual environment (PyTorch 2.15.0+cpu, scikit-learn 1.9.1, spaCy 3.8.18) and the outputs shown are real. The models are tiny toys that demonstrate mechanisms (contrastive loss, residual gradients, a small U-Net, quantization, pruning); one result is a deliberate lesson, not a success: the toy diffusion model's loss fell sharply but its samples were not clean images. Nothing in these notes was run on a GPU or against NVIDIA services (Triton, NeMo, Riva, NIM), so those are described from NVIDIA documentation.

## What the sources could not fill

Said where it occurs in the notes: the exam page names objectives but no study guide exists, and several reading-list items were not fetched (Prompt Engineering Guide, Molnar's book, the FID paper, the Hugging Face Evaluate docs, the data augmentation guide). OpenAI's CLIP page returned 403; the CLIP description rests on the paper's abstract.

## NVIDIA's recommended training (from the exam page)

Fundamentals of Deep Learning (open-source course materials) and Building AI Agents With Multimodal Models (NVIDIA DLI course C-FX-17). The page also lists a long reading list (CLIP, diffusion, fusion, RAG, spaCy, NumPy, Keras, MLflow, Triton, mixed precision, quantization, pruning, NeMo, NIST AI RMF).

## Quick Links

- **[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/)** - Blueprint, price, registration
- **[📖 NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)** - Serving
- **[📖 NVIDIA NeMo Framework](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)** - Training and customization
- **[📖 NVIDIA Riva ASR](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html)** - Speech recognition

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Logistics, blueprint and key facts with documentation links |
| [practice-plan.md](practice-plan.md) | Study schedule |
| [scenarios.md](scenarios.md) | Short exam-style scenarios |
| [strategy.md](strategy.md) | Exam tactics |
| [notes/](notes/01-core-ml-and-ai-knowledge.md) | The seven section notes |
