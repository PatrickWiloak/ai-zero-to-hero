---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - Multimodal Generative AI (NCA-MMGA) - Practice Questions

15 questions for NCA-MMGA prep, weighted toward multimodal fundamentals (25%) and image and video generation (25%), then text and speech (20%), NVIDIA tooling (15%), and applications (15%).

> **Cert page:** [exams/nvidia/multimodal-genai-associate/](../nvidia/multimodal-genai-associate/README.md)

---

### Question 1
**Scenario:** What makes a model multimodal?

A. It runs on multiple GPUs, with each GPU handling a different input type such as text or images in parallel
B. It chains one prompt per input type and merges the separate text answers
C. It has far more parameters than a text-only model, which is what lets it handle images as well as text alike
D. It accepts or produces more than one modality, such as text and images, in a shared representation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The defining feature is a shared representation space that lets the model relate content across modalities, so an image and its description land near each other. Multi-GPU execution and parameter count are unrelated properties.
</details>

---

### Question 2
**Scenario:** CLIP-style training aligns images and text. What objective does it use?

A. Next-token prediction over captions, where the model learns to write the caption word by word from the image
B. Reinforcement learning from human feedback, with raters scoring how well each caption fits its image
C. Contrastive learning: matched pairs pulled together, others pushed apart
D. Diffusion denoising, where the model learns to remove noise from images conditioned on caption text

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Contrastive pretraining over large image-caption datasets is what produces a joint embedding space, which is what enables zero-shot classification and text-to-image retrieval. Diffusion is the generative mechanism used later, and next-token prediction is the language modeling objective.
</details>

---

### Question 3
**Scenario:** How does a diffusion model generate an image?

A. It uses a GAN discriminator that scores a random image until it looks real
B. It predicts pixels left to right, one at a time, like an autoregressive language model
C. It retrieves the closest training image to the prompt and blends it with random noise
D. It starts from noise and iteratively denoises, guided by the conditioning (such as a text embedding)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Training teaches the model to reverse a noising process; generation runs that reversal from pure noise. The number of denoising steps is the main quality-versus-speed knob, and latent diffusion runs the process in a compressed latent space to make it affordable.
</details>

---

### Question 4
**Scenario:** A text-to-image model must follow the prompt more closely.

A. Raise the classifier-free guidance scale, accepting less diversity at high values
B. Lower the guidance scale, since weaker conditioning lets the model follow the text more literally and more diversely
C. Change the random seed until a sample matches, since each seed changes how strongly the prompt is applied
D. Reduce the number of steps, since fewer denoising passes leave less time for the model to drift from the prompt

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Guidance scale trades prompt adherence against diversity and naturalness. Pushing it too high produces over-saturated, artifact-heavy output, so there is a usable band rather than a "higher is better" relationship. The seed changes which sample you get, not how closely it follows the prompt.
</details>

---

### Question 5
**Scenario:** A vision-language model must answer questions about a chart in an uploaded image.

A. A text-only LLM, by pasting the image's file name and alt text into the prompt along with the question
B. An embedding model alone, matching the chart image to the closest stored caption and returning that text
C. A VLM that encodes the image and reasons jointly over visual and text content
D. OCR only, extracting every number on the chart and letting the user work out the relationships

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Chart question answering needs both reading and reasoning over spatial structure, which a VLM does end to end. OCR extracts text but loses the relationships between axes, series, and values. Embeddings support retrieval rather than answering.
</details>

---

### Question 6
**Scenario:** Which NVIDIA product provides speech recognition and text-to-speech services?

A. NVIDIA Merlin, the framework for building large-scale recommender systems
B. NVIDIA Riva, which covers speech recognition and text-to-speech
C. NVIDIA Morpheus, for cybersecurity AI
D. NVIDIA Clara, the platform for healthcare and medical imaging AI workflows

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Riva is the speech AI stack, covering ASR, TTS, and translation with GPU-optimized deployment. Merlin targets recommenders, Morpheus is cybersecurity AI, and Clara is healthcare.
</details>

---

### Question 7
**Scenario:** Multimodal RAG must retrieve both diagrams and text for a technical question.

A. Index only the text, since the paragraphs around a diagram are enough to answer questions about it
B. Embed images and text in an aligned space, or index captions and metadata next to the text, then retrieve across the index
C. Store every image as a base64 string in the prompt on each query, so the model searches the pictures itself and no separate index or embedding step is ever needed
D. Ignore images and tell the user to open the figure in the source document themselves

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retrieval requires the images to be searchable, which comes from either a joint embedding model or a generated-caption index. Caption-based indexing is often the pragmatic choice because it also gives you readable evidence of why an image was retrieved.
</details>

---

### Question 8
**Scenario:** Generated video is temporally inconsistent: objects flicker between frames.

A. Change the prompt wording only, adding phrases such as "stable" and "consistent" to remove the flicker
B. Temporal coherence is a known challenge; use temporal attention or conditioning on prior frames, and measure consistency explicitly
C. Increase resolution, since more pixels per frame give the model enough detail to keep every object steady between frames, and the flicker then disappears on its own
D. Reduce the frame rate so fewer frames are generated, which removes the flicker while keeping the video length unchanged

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Frame-by-frame generation with no temporal mechanism produces flicker by construction. Video models add temporal layers or condition on preceding frames, and consistency should be measured as its own metric rather than assumed from per-frame quality.
</details>

---

### Question 9
**Scenario:** An image generation feature must not produce content resembling identifiable real people.

A. Rely on the prompt, with a system instruction telling the model never to draw real people
B. Reduce image resolution and compress every output, so faces are too low quality to be recognized as any real person
C. Layered controls: prompt and output classification, restricted model or LoRA selection, and policy with human review for edge cases
D. Add a disclaimer under every image saying that it is synthetic, that any likeness to a real person is coincidental, and that misuse of the tool is prohibited

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Likeness and deepfake risk is a real harm and a legal exposure, so it needs enforcement rather than intent. Input filtering catches the obvious requests, output classification catches what slips through, and provenance metadata such as C2PA credentials supports downstream accountability.
</details>

---

### Question 10
**Scenario:** How should a multimodal model's quality be evaluated?

A. Inference latency measured at the 95th percentile, since a faster model is by definition a better one
B. Human judgment only, with a panel of raters, since automatic metrics cannot reflect perceived quality
C. Task-appropriate metrics plus human evaluation, such as FID or CLIP score for images, WER for speech, and grounded accuracy for VQA
D. Parameter count and training-set size, since a larger model needs no further testing before launch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each modality has its own established metrics, and none of them fully capture perceived quality, which is why human evaluation stays in the loop. Reporting a single number across modalities hides where a system is actually failing.
</details>

---

### Question 11
**Scenario:** An image must be edited so only a specified region changes.

A. Inpainting with a mask, so the model regenerates only the masked region from its surroundings
B. Increase guidance so the model concentrates on the named object, leaving other regions mostly unchanged
C. Regenerate the whole image with a modified prompt, then blend the results by hand in an image editor
D. Use a larger model, since extra capacity lets it preserve the rest of the image

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Masked inpainting preserves the rest of the image exactly, which is what "edit this part" requires. Regenerating from a modified prompt changes everything, including details the user wanted kept. Outpainting is the same mechanism extended beyond the original boundary.
</details>

---

### Question 12
**Scenario:** A custom style must be applied consistently to generated images with only 20 reference examples.

A. LoRA or DreamBooth-style adaptation on the small reference set, keeping the base model frozen
B. Prompt engineering alone, with style adjectives and a seed reused for every image
C. Train a diffusion model from scratch on the 20 reference images so it learns the style exactly and quickly
D. Full fine-tuning of every weight in the base model on the 20 images, which is quick and risk-free at that size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lightweight adaptation methods learn a style or subject from a handful of images while keeping the base model frozen, which is both feasible and reversible. Full training needs orders of magnitude more data, and prompts alone rarely reproduce a specific visual identity consistently.
</details>

---

### Question 13
**Scenario:** Which describes the trade-off in reducing diffusion sampling steps?

A. Steps affect only memory use, since the same amount of denoising work is done in total at every step count, only split into more or fewer passes
B. There is no trade-off, because every sampler reaches the same image at any step count
C. Fewer steps improves quality, because less noise is removed and fine detail is kept intact
D. Fewer steps means faster generation but typically lower fidelity, though distilled models narrow the gap

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Step count directly sets both latency and cost. Distillation techniques have compressed high-quality generation into very few steps, which is why the naive "more steps is better" rule no longer holds across model families.
</details>

---

### Question 14
**Scenario:** Audio transcription accuracy is poor on domain-specific terminology.

A. Raise the microphone gain, so the model hears rare terms at a higher volume and decodes them correctly
B. Adapt the model or use custom vocabulary and language model biasing for the domain terms, then re-measure word error rate
C. Increase the sample rate to 96 kHz, which gives the recognizer more detail on every word
D. Reduce the audio length by splitting each recording into very short clips of a few seconds

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rare proper nouns and jargon are the standard weakness of general ASR models. Custom vocabulary, phrase boosting, or fine-tuning on domain audio directly targets that failure. Audio quality changes help only when quality is actually the problem.
</details>

---

### Question 15
**Scenario:** A multimodal application must run where data cannot leave the premises.

A. Deploy the models on-premises, for example with NIM microservices on local GPUs
B. It is not possible, because multimodal models only run in hosted cloud services with managed GPUs
C. Anonymize the images and audio, then send them to a public API, since removing names is sufficient
D. Use a smaller model in the cloud, which processes less data and so counts as keeping data on the premises

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Self-hosting is the answer to a data residency constraint, and containerized microservices make it a deployment choice rather than a rewrite. Anonymization is rarely sufficient for images and audio, which carry identifying signal that is hard to remove.
</details>

---

## Where to go deeper

- [NCA-MMGA cert page](../nvidia/multimodal-genai-associate/README.md) - notes, practice plan, strategy
- [NCA-GENL practice questions](nvidia-genai-llms-associate.md) - the text-focused sibling
- [Multimodal models](../../learn/concepts/multimodal-models.md) - plain-English primer
- [LLMs and GenAI topic index](../../learn/README.md) - the wider AI stack
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
