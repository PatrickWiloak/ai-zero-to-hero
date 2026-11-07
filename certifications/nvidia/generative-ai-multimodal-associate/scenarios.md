# NCA-GENM - Scenarios

**Last reviewed:** 2026-11-07

Six original scenarios written for this guide, with answers backed by the code run in the notes.

## 1. Images and captions that do not match

A new image-caption dataset is about to train a CLIP-style model. **First step:** audit it (duplicates, missing paths, empty captions, corrupt images, mismatched pairs); a contrastive model treats every broken pair as a real positive and learns the wrong association.

## 2. The loss exploded at step 40

Check for NaNs, then add gradient clipping (`clip_grad_norm_` returned a total norm of 6,051 in my test and rescaled it to 1.0), lower the learning rate or add warmup.

## 3. The model must fit on an edge device

Quantize to int8 (4.0x smaller in the note 5 run), and consider pruning; compare accuracy before and after, because both can cost some.

## 4. Answers must cite current company documents

Use RAG: embed the query, search the vector index of the documents, retrieve passages, and build the prompt. This is cheaper and faster than retraining and lets you hot-swap sources.

## 5. Adapting a pretrained vision-language model to a niche domain with little data

Freeze the pretrained encoders and train a small head or projection layer (1.9 percent of parameters in the toy example), then evaluate with cross-validation.

## 6. The hiring screener selects one group more often

Measure the selection rate by group (11-point gap in the toy example), review the data and labels, and document and mitigate; NIST's characteristic is "fair, with harmful bias managed".
