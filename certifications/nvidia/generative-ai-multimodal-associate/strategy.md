# NCA-GENM - Exam Strategy

**Last reviewed:** 2026-11-07

## What the exam looks like

One hour, about 50 multiple-choice questions, online and remotely proctored. That is roughly 70 seconds a question, so know the vocabulary cold. Experimentation (25%) and Core ML (20%) are almost half the exam.

## Tactics

1. **Map each question to a blueprint section.** Section names mislead (the "Multimodal Data" section is mostly RAG, chatbots, spaCy and NumPy), so go by the objective wording.
2. **Know the mechanisms, not just the names.** Contrastive loss pulls matching pairs together; residual connections add the input to the output; diffusion trains a network to predict added noise; mixed precision keeps master weights in float32.
3. **Training loss is not quality.** If an option says a falling loss proves good samples, it is wrong.
4. **Match the technique to the goal.** Smaller model for serving: quantization or pruning. Less memory in training: mixed precision. Unstable training: gradient clipping. Few labels: transfer learning. Missing facts in an LLM: RAG.
5. **Trustworthy AI questions reward the framework words**: NVIDIA's privacy, safety and security, transparency, nondiscrimination; NIST's GOVERN, MAP, MEASURE, MANAGE.
