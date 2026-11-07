---
last-updated: 2026-11-07
---

# NVIDIA-Certified Associate - Generative AI Multimodal (NCA-GENM) - Fact Sheet

## Quick Reference

**Exam code:** NCA-GENM  
**Exam name:** NVIDIA Generative AI Multimodal Certification Exam  
**Duration:** 1 hour  
**Questions:** 50 multiple choice (page also says 50-60 in one place)  
**Cost:** $125 USD (exam page, 2026-11-07)  
**Delivery:** Online, remotely proctored  
**Level:** Associate  
**Validity:** 2 years from issuance  
**Language:** English  
**Prerequisites:** A basic understanding of generative AI  
**Passing score:** Not published  

**[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/)** - Blueprint, price and registration

## Exam Blueprint

| Topic | Weight | Note |
|---|---|---|
| Core Machine Learning and AI Knowledge | 20% | [01](notes/01-core-ml-and-ai-knowledge.md) |
| Data Analysis | 10% | [02](notes/02-data-analysis.md) |
| Experimentation | 25% | [03](notes/03-experimentation.md) |
| Multimodal Data | 15% | [04](notes/04-multimodal-data.md) |
| Performance Optimization | 10% | [05](notes/05-performance-optimization.md) |
| Software Development | 15% | [06](notes/06-software-development.md) |
| Trustworthy AI | 5% | [07](notes/07-trustworthy-ai.md) |

## Key Facts by Section

- **Core ML:** contrastive loss ([CLIP paper](https://arxiv.org/abs/2103.00020)); residual connections keep gradients alive in deep networks; `clip_grad_norm_` rescales gradients in place and returns the total norm; transfer learning freezes a backbone and trains a head.
- **Data analysis:** audit data (duplicates, missing, empties, corrupt files); attention maps are row-normalized weight matrices; permutation importance shows which input a model relies on.
- **Experimentation:** diffusion = noise, predict the noise, sample by repeated denoising ([Hugging Face course](https://huggingface.co/learn/diffusion-course/unit1/1)); training loss is not sample quality; early versus late fusion.
- **Multimodal data:** RAG = embed query, search index, retrieve, augment prompt, generate ([NVIDIA RAG explainer](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)); spaCy for tokenization and sentences; NumPy for array math.
- **Performance optimization:** autocast keeps weights and some ops in float32 ([PyTorch AMP](https://docs.pytorch.org/docs/2.15/amp.html)); GradScaler is for float16; dynamic int8 quantization shrank a model 4.0x; pruning uses `weight_orig` plus `weight_mask`; Triton does dynamic batching ([Triton docs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)).
- **Software development:** U-Net = encoder-decoder with skip connections, predicts noise at input size; CLIP supplies text embeddings to condition image generation.
- **Trustworthy AI:** NVIDIA principles: privacy, safety and security, transparency, nondiscrimination ([NVIDIA page](https://www.nvidia.com/en-us/ai-data-science/trustworthy-ai/)); NIST AI RMF functions GOVERN, MAP, MEASURE, MANAGE ([NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)).
