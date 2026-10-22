---
last-updated: 2026-10-22
difficulty: intermediate
---

# NVIDIA-Certified Associate - Generative AI Multimodal (NCA-GENM) - Practice Questions

30 questions for NCA-GENM prep, weighted toward experimentation (25%) and core machine learning and AI knowledge (20%), then multimodal data (15%), software development (15%), data analysis (10%), performance optimization (10%), and trustworthy AI (5%).

> **Cert page:** [exams/nvidia/generative-ai-multimodal-associate/](../nvidia/generative-ai-multimodal-associate/README.md)

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

### Question 16
**Scenario:** A latent diffusion model such as Stable Diffusion runs its denoising steps on a small compressed representation rather than on full-resolution pixels.

A. A tokenizer that turns each image into a sequence of words the language model can read
B. A classifier that labels each image so the denoiser knows which object class to draw
C. A super-resolution network that upscales every intermediate step to the final pixel size
D. A variational autoencoder that compresses images into latents and decodes them back

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Latent diffusion trains the denoiser in the latent space of an autoencoder, which is far smaller than pixel space, so each step is much cheaper; the decoder turns the final latent back into an image. A text tokenizer handles the prompt, not the image. Class labels are not part of text-to-image denoising, and upscaling every step would defeat the purpose.

**Key Concept:** [NVIDIA Cosmos documentation](https://docs.nvidia.com/cosmos/latest/index.html)
</details>

---

### Question 17
**Scenario:** A Vision Transformer (ViT) applies a standard transformer encoder to images.

A. It splits the image into fixed-size patches, embeds each as a token, and adds positions
B. It feeds every pixel to the transformer as a separate token, which keeps all of the spatial detail
C. It converts the image into a text caption first and then runs the transformer on the caption words
D. It replaces attention with convolutions, so the model processes images the same way as a CNN

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** ViT cuts the image into patches (for example 16 by 16 pixels), linearly embeds each one as a token, adds position embeddings, and runs a transformer encoder over the sequence. Per-pixel tokens would make attention prohibitively expensive. Captioning first discards visual information, and ViT keeps attention rather than replacing it with convolutions.

**Key Concept:** [NVIDIA TAO Toolkit](https://docs.nvidia.com/tao/tao-toolkit/latest/index.html)
</details>

---

### Question 18
**Scenario:** While fine-tuning an image classifier, training loss keeps falling, but validation loss starts rising after epoch 6.

A. The model is underfitting, so it needs more epochs and a larger learning rate to keep improving
B. The validation set is broken, since validation loss can never rise while the training loss falls
C. The model is overfitting, so use early stopping, augmentation or regularization such as dropout
D. The GPU is throttling, which slows training and makes the validation loss go up over time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Diverging training and validation loss is the classic sign of overfitting: the model memorizes the training set and generalizes worse. Stopping at the best validation checkpoint, adding data augmentation and using regularization all address it. Underfitting shows high loss on both sets, the pattern is expected rather than a broken set, and GPU speed does not change loss values.

**Key Concept:** [NVIDIA TAO Toolkit](https://docs.nvidia.com/tao/tao-toolkit/latest/index.html)
</details>

---

### Question 19
**Scenario:** A defect-detection image dataset has 98% "no defect" and 2% "defect" images. A model reports 98% accuracy, and the team is pleased.

A. Accept the result, because 98% accuracy is high enough for any production image model
B. Check per-class metrics such as recall and F1 on the defect class, using stratified splits
C. Remove the defect images, since rare classes add noise that lowers the overall accuracy
D. Report the training accuracy instead, since validation accuracy is unreliable on small data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With this imbalance, a model that always predicts "no defect" scores 98% accuracy while catching no defects. Per-class recall, precision and F1, with stratified splits so each set keeps both classes, show whether the rare class is detected. Removing the class makes the task meaningless, and training accuracy overstates performance.

**Key Concept:** [NVIDIA TAO Toolkit](https://docs.nvidia.com/tao/tao-toolkit/latest/index.html)
</details>

---

### Question 20
**Scenario:** Two image generation models must be compared on how closely the statistics of their outputs match a set of real images.

A. Word error rate, which counts the words in each generated caption that differ from a reference
B. BLEU score, which measures n-gram overlap between each generated image and a reference image
C. Perplexity, which measures how surprised the model is by each pixel of the generated image
D. Fréchet Inception Distance (FID), which compares feature distributions of real and generated images

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FID embeds real and generated images with a pretrained vision network and measures the distance between the two feature distributions; lower is better, and it reflects both quality and diversity. Word error rate is for speech recognition, BLEU is for text overlap, and perplexity applies to language models.

**Key Concept:** [NVIDIA Cosmos documentation](https://docs.nvidia.com/cosmos/latest/index.html)
</details>

---

### Question 21
**Scenario:** Before training, a team wants to explore 200,000 image embeddings to spot clusters, outliers and possibly mislabeled examples.

A. Project the embeddings to 2D with UMAP or t-SNE, color by label, and inspect clusters and outliers
B. Print the first 100 embedding vectors and read the numbers to find any mislabeled images
C. Sort the images by file size, since mislabeled images are usually larger than the correct ones
D. Train the final model first and look for mislabeled data only if the accuracy is disappointing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Dimensionality reduction such as UMAP or t-SNE projects high-dimensional embeddings into 2D while largely preserving neighborhoods, so points that sit inside another class's cluster stand out as likely label errors; cuML runs these on the GPU for large sets. Raw vectors are unreadable, file size has nothing to do with labels, and checking data only after training wastes compute.

**Key Concept:** [cuML documentation](https://docs.nvidia.com/cuml/latest/)
</details>

---

### Question 22
**Scenario:** A team compares two prompt templates for an image generator, but results change every run, so they cannot tell which template is better.

A. Generate a single image per template and judge the better one by eye
B. Use a new random seed for every image so that the comparison stays fair
C. Raise the number of denoising steps until both templates give identical images
D. Fix the random seeds and generate the same set of images for each template

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Diffusion sampling starts from random noise, so controlled comparisons fix the seeds and generate a set of images per variant, letting differences be attributed to the template rather than to chance. One image per variant is anecdotal. Unfixed seeds add the noise that caused the problem, and more steps do not make different prompts produce identical images.

**Key Concept:** [NVIDIA Cosmos documentation](https://docs.nvidia.com/cosmos/latest/index.html)
</details>

---

### Question 23
**Scenario:** A new captioning pipeline changes the image encoder, the prompt template and the learning rate at once, and quality improves. The team wants to know which change helped.

A. Keep all three changes and stop there, since the reason for an improvement does not matter
B. Run an ablation that changes one factor at a time against the baseline on the same eval set
C. Change all three factors again in a different direction and see whether quality falls back
D. Ask users which of the three changes they prefer, based on a short description of each

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An ablation isolates each factor by changing one at a time against a fixed baseline and evaluation set, showing what each contributes, which matters when one change adds cost or risk. Keeping everything blindly can keep a harmful change hidden by a helpful one. Changing everything again is still confounded, and user preference for descriptions is not a measurement.

**Key Concept:** [NVIDIA TAO Toolkit](https://docs.nvidia.com/tao/tao-toolkit/latest/index.html)
</details>

---

### Question 24
**Scenario:** A speech recognition model trained on 16 kHz audio gives poor transcripts for a new batch of 44.1 kHz recordings.

A. Resample the recordings to the 16 kHz rate that the model expects, before running inference
B. Speed up the recordings by a factor of 2.75 so that their duration matches the training audio
C. Convert the recordings to images with a camera filter, since speech models read only spectrogram photos
D. Retrain the model from scratch on 44.1 kHz audio, since sample rates cannot be converted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Audio models expect a fixed sample rate, and feeding a different rate distorts the features they compute, so resampling to the training rate is a standard preprocessing step. Speeding the audio up changes pitch and timing. Spectrograms are computed from the waveform, not photographed, and retraining is unnecessary when resampling solves the mismatch.

**Key Concept:** [NVIDIA Speech NIM microservices](https://docs.nvidia.com/nim/speech/latest/about/index.html)
</details>

---

### Question 25
**Scenario:** A team scraped millions of image-caption pairs to train a text-to-image model. Many captions do not describe their images.

A. Keep every pair, because the model learns to ignore wrong captions automatically
B. Remove every image larger than 1 MB, since large files are the most likely to be mislabeled
C. Translate every caption into English, which aligns the captions with their images
D. Score each pair with a CLIP-style model and drop pairs whose image-text similarity is low

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An image-text model such as CLIP scores how well a caption matches its image, so filtering out low-similarity pairs is a standard way to clean scraped multimodal data; NeMo Curator supports this kind of filtering at scale. Noisy pairs teach the model wrong associations. File size is unrelated to caption quality, and translation does not fix a caption that describes something else.

**Key Concept:** [NeMo Curator documentation](https://docs.nvidia.com/nemo/curator/home/welcome)
</details>

---

### Question 26
**Scenario:** A trained image generation model is too slow in production on NVIDIA GPUs, and the team wants faster inference from the same model.

A. Convert the model weights to FP64, which the GPU processes faster than other formats
B. Run the model on the CPU, since image models are mainly limited by the GPU's clock speed
C. Optimize it with TensorRT, which fuses layers and uses FP16 or INT8 kernels for the GPU
D. Increase the image resolution, which lets the GPU process more pixels in each kernel

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** TensorRT builds an optimized engine for the target GPU with layer fusion, kernel selection and reduced precision, which commonly speeds up diffusion and vision models substantially. FP64 is much slower on most GPUs. Moving to the CPU is slower, and higher resolution adds work rather than saving it.

**Key Concept:** [NVIDIA TensorRT documentation](https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html)
</details>

---

### Question 27
**Scenario:** Fine-tuning a vision-language model in FP32 is slow, and the GPUs' Tensor Cores are mostly idle.

A. Switch to FP64 training, which keeps the Tensor Cores busy with double-precision math
B. Reduce the dataset to a tenth of its size, so that every epoch finishes faster
C. Train with automatic mixed precision (BF16 or FP16), keeping FP32 where it is needed
D. Disable the GPU's ECC memory protection, which is what slows down FP32 training

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Automatic mixed precision runs most math in BF16 or FP16 on Tensor Cores while keeping sensitive operations and master weights in FP32, which raises throughput and lowers memory with little or no accuracy loss. FP64 is slower. Shrinking the dataset trades away quality, and ECC is not the cause of slow FP32 math.

**Key Concept:** [Train with mixed precision](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html)
</details>

---

### Question 28
**Scenario:** A multimodal training job's GPU utilization swings between 0% and 100%. The team does not know whether data loading or the model is the bottleneck.

A. Buy faster GPUs, since utilization swings always mean that the GPU itself is too slow
B. Profile a few steps with Nsight Systems to see whether the GPU waits for data
C. Double the learning rate, which makes each step finish faster and evens out usage
D. Turn off data augmentation permanently, because augmentation always runs on the GPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Nsight Systems shows a timeline of CPU and GPU activity, so gaps where the GPU waits for the next batch reveal an input bottleneck, which might be fixed with more loader workers or GPU-side decoding such as DALI. Faster GPUs make an input-bound job wait longer. The learning rate does not affect step time, and augmentation often runs on the CPU, which is part of the problem.

**Key Concept:** [Nsight Systems user guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)
</details>

---

### Question 29
**Scenario:** An application already uses the OpenAI Python client and must now send images with questions to a vision language model served by NVIDIA NIM.

A. Rewrite the client in a NIM-specific SDK, since NIM does not accept OpenAI-style requests
B. Encode each image as a filename and let the NIM container search the client's disk for it
C. Send the image to a separate OCR service and pass only the extracted text to the model
D. Point the client's base URL at the NIM endpoint and include the image in the message content

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NIM for vision language models exposes an OpenAI-compatible chat completions API, so the existing client works by changing the base URL and model name, with images sent in the message content (for example as a URL or base64 data). No special SDK is required. A server cannot read the client's disk, and OCR loses the visual information that a VLM uses.

**Key Concept:** [NIM for vision language models](https://docs.nvidia.com/nim/vision-language-models/latest/index.html)
</details>

---

### Question 30
**Scenario:** A live video-conference app must show captions while people are still speaking, with words appearing within a fraction of a second.

A. Use streaming speech recognition, sending audio chunks and receiving partial and final transcripts
B. Record the full meeting, then send the file for offline transcription after the call has ended
C. Send one-minute audio files for batch transcription and show each result when it arrives
D. Use a text-to-speech model, which converts the meeting's audio into on-screen text as it plays

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Streaming ASR, as offered by NVIDIA's Riva-based speech NIM microservices, accepts audio as it is captured and returns interim results that are updated into final transcripts, which gives live captions. Offline or one-minute batch transcription arrives far too late. Text-to-speech works in the opposite direction.

**Key Concept:** [NVIDIA Speech NIM microservices](https://docs.nvidia.com/nim/speech/latest/about/index.html)
</details>

---

## Where to go deeper

- [NCA-GENM cert page](../nvidia/generative-ai-multimodal-associate/README.md) - notes, practice plan, strategy
- [NCA-GENL practice questions](nvidia-genai-llms-associate.md) - the text-focused sibling
- [Multimodal models](../../learn/concepts/multimodal-models.md) - plain-English primer
- [LLMs and GenAI topic index](../../learn/README.md) - the wider AI stack
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
