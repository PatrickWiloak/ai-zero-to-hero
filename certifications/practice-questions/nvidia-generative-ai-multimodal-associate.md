---
last-updated: 2026-11-07
difficulty: intermediate
---

# NVIDIA-Certified Associate - Generative AI Multimodal (NCA-GENM) - Practice Questions

30 original questions in the weights of NVIDIA's blueprint: Core ML and AI Knowledge (20%, 6 questions), Data Analysis (10%, 3), Experimentation (25%, 7), Multimodal Data (15%, 4), Performance Optimization (10%, 3), Software Development (15%, 5) and Trustworthy AI (5%, 2). They are written for this guide, not taken from the exam, and the explanations cite the code run in the notes or the named documentation.

> **Cert page:** [exams/nvidia/generative-ai-multimodal-associate/](../nvidia/generative-ai-multimodal-associate/README.md)

---

### Question 1
**Section: Core ML. Scenario:** In a CLIP-style batch of 8 matched image-text pairs, what does the contrastive loss train to be the largest similarity in each row of the similarity matrix?

A. The entry for the caption with the most words
B. The smallest entry in the row
C. The diagonal entry, the image's own caption
D. The average of the row

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The loss applies cross-entropy with the diagonal as the label in both directions; in my run matched pairs gave 0.000 and a random pairing gave 10.715.
</details>

---

### Question 2
**Section: Core ML. Scenario:** A 40-layer network without skip connections trains badly while the same network with residual connections trains well. What is the best explanation?

A. Residual connections reduce the number of parameters to zero
B. Residual connections give gradients a direct path, avoiding vanishing gradients
C. They remove the need for a loss function
D. They convert the network into a single linear layer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In my test the first-block gradient norm was 1.41e-11 without residuals and 1.34e+01 with them.
</details>

---

### Question 3
**Section: Core ML. Scenario:** What does torch.nn.utils.clip_grad_norm_ return?

A. The clipped parameters
B. The learning rate
C. The loss value
D. The total norm of the gradients, computed before clipping

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The PyTorch documentation says it modifies gradients in place and returns the total norm of the parameter gradients; mine returned 6051.6 and rescaled the norm to 1.0.
</details>

---

### Question 4
**Section: Core ML. Scenario:** A team has 200 labeled images in a niche domain and a pretrained image encoder. Which approach is the cheapest reasonable start?

A. Freeze the pretrained encoder and train a small head on the new labels
B. Train the full encoder from random weights
C. Skip training and use random labels
D. Double the image resolution and train nothing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Transfer learning with a frozen backbone trained only 1.9 percent of the parameters in my toy example.
</details>

---

### Question 5
**Section: Core ML. Scenario:** Why is one train-validation split a weak basis for a model comparison on a small dataset?

A. Because validation sets cannot be used for scoring
B. The score depends on which rows landed in which part, so repeating with cross-validation gives a more reliable estimate
C. Because splits always leak labels
D. Because cross-validation is faster than a single split

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Repeated evaluation reports a mean and spread; cross-validation costs more compute but is more reliable. My forest scored 0.947 +- 0.025 over five folds.
</details>

---

### Question 6
**Section: Core ML. Scenario:** Which statement describes zero-shot classification with CLIP?

A. Training a new classifier head on every class
B. Classifying images using only pixel counts
C. Classifying images into categories given as text, by comparing the image embedding with text embeddings, without training on those labels
D. Generating labels with a diffusion model

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The CLIP paper describes training on 400 million image-text pairs so that concepts described in plain language can be recognized without task-specific training.
</details>

---

### Question 7
**Section: Data analysis. Scenario:** An audit of an image-caption table reports 1 duplicate, 1 empty caption and 2 zero-width images in 5 rows. What is the right action before training?

A. Train anyway because averages hide it
B. Fix or drop the broken rows and block training until the checks pass
C. Delete the whole dataset
D. Add more captions at random

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Broken pairs train the model on wrong associations; dataset checks should be code that blocks training, like unit tests.
</details>

---

### Question 8
**Section: Data analysis. Scenario:** What does each row of an attention map from nn.MultiheadAttention (averaged over heads) represent?

A. A probability distribution over the key positions, summing to 1
B. A list of pixel values
C. The model's loss
D. The gradient norm

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In my run the weights had shape (1, 5, 5) and every row summed to 1.0.
</details>

---

### Question 9
**Section: Data analysis. Scenario:** Permutation importance gives [0.0, 0.005, 0.075, 0.0, 0.001, 0.513] on six features. What does it indicate?

A. The model relies mostly on the last feature and somewhat on the third; the others barely matter
B. All six features matter equally
C. The model ignores every feature
D. The last feature has a data leak by definition

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Importance is the score drop when a feature is shuffled. A large drop means reliance; near zero means little reliance. (A large value is not by itself proof of leakage.)
</details>

---

### Question 10
**Section: Experimentation. Scenario:** A diffusion model's training loss falls from 0.95 to 0.08, but samples from pure noise are not clean images. What is the right conclusion?

A. The model is perfect because the loss is low
B. Training loss is a diagnostic, not a measure of sample quality; evaluate generated outputs separately
C. Diffusion models cannot generate from noise
D. The test set must be wrong

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** My toy run showed this: the loss fell by an order of magnitude yet samples ranged up to 7.54 on images in [-1, 1].
</details>

---

### Question 11
**Section: Experimentation. Scenario:** In diffusion training, what does the network learn to predict?

A. The caption of the image
B. The class label only
C. The noise that was added to the image
D. The next token

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Hugging Face course describes adding noise in different amounts and training the model to denoise; the standard loss compares predicted and actual noise.
</details>

---

### Question 12
**Section: Experimentation. Scenario:** How does generation start in a diffusion model?

A. From a blank white image with no noise
B. From a fully trained classifier output
C. From the training set's mean image
D. From random noise, applying the model repeatedly to update the input slightly each time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The course says generation starts from random noise and the model is applied repeatedly, gradually producing an image.
</details>

---

### Question 13
**Section: Experimentation. Scenario:** Which is a sound way to check an explanation that points at a feature?

A. Shuffle or remove that feature and see whether the prediction changes
B. Trust it because it looks plausible
C. Count the pixels in the image
D. Retrain with a larger batch size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Permutation importance is an intervention: a real dependence shows as a score drop.
</details>

---

### Question 14
**Section: Experimentation. Scenario:** A team compares early fusion and late fusion. Which description is correct?

A. Early fusion joins the modalities' features before one model; late fusion trains a model per modality and combines outputs
B. Early fusion trains one model per modality; late fusion joins raw files
C. Both are the same
D. Early fusion cannot use more than one modality

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In my toy run early fusion scored 0.86, late fusion 0.82 and a single modality 0.82 on 100 test points, a small gap that shows the mechanism rather than a ranking.
</details>

---

### Question 15
**Section: Experimentation. Scenario:** Which check best tests data consistency across modalities?

A. The dataset folder has a short name
B. Every image has a non-empty caption, and image dimensions match what the encoder expects
C. The captions are alphabetized
D. The file sizes are all different

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Consistency means the modalities line up per sample; mismatches become silent training noise.
</details>

---

### Question 16
**Section: Multimodal data. Scenario:** What are the steps of a RAG loop?

A. Fine-tune the LLM on the query, then delete the index
B. Retrieve the answer from the LLM's weights only
C. Embed the query, search the knowledge-base index, retrieve matches, augment the prompt, generate the answer
D. Translate the query to pixels, then classify

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVIDIA's explainer describes converting the query to an embedding, comparing it with indexed vectors, retrieving matches as text and passing them to the LLM, which can cite sources.
</details>

---

### Question 17
**Section: Multimodal data. Scenario:** Why is RAG often preferred to retraining an LLM when facts change?

A. Retraining is impossible
B. RAG makes the model larger
C. RAG removes the need for any data
D. It is cheaper and faster, and sources can be hot-swapped without retraining

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NVIDIA lists efficiency among RAG's benefits, alongside accuracy, trust through citations and clarifying ambiguous queries.
</details>

---

### Question 18
**Section: Multimodal data. Scenario:** In my TF-IDF retrieval example, why did only one document get a nonzero score for 'which tool does speech recognition'?

A. Only that document shared words with the query; dense embeddings would also match paraphrases
B. TF-IDF ignores all words
C. The other documents were deleted
D. Cosine similarity cannot be negative

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Term-based vectors match shared words; embedding models place similar meanings close together, which is why real RAG uses them.
</details>

---

### Question 19
**Section: Multimodal data. Scenario:** What does a spaCy blank English pipeline with a sentencizer provide, with no model download?

A. Tokenization and sentence boundaries
B. Named entity recognition for 20 languages
C. A trained question-answering model
D. GPU acceleration

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** In my run it returned tokens such as 'NVIDIA', 'NIM', 'serves' and three sentences.
</details>

---

### Question 20
**Section: Performance optimization. Scenario:** Under torch.autocast on CPU with bfloat16, which dtypes appeared in my check?

A. float16 weights and a bfloat16 loss
B. int8 everything
C. float64 weights
D. bfloat16 linear output, float32 loss, float32 stored weights

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Autocast runs eligible ops in lower precision while keeping others (and master weights) in float32.
</details>

---

### Question 21
**Section: Performance optimization. Scenario:** When is GradScaler needed?

A. Only for bfloat16 on CPU
B. For int8 quantization
C. For float16 training, to scale the loss so small gradients do not underflow
D. Never

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The PyTorch docs say bfloat16 needs only autocast, while float16 uses autocast and GradScaler together.
</details>

---

### Question 22
**Section: Performance optimization. Scenario:** What does PyTorch pruning do to a layer's parameters, according to the tutorial?

A. Deletes the layer
B. Doubles the weight values
C. Converts weights to strings
D. Replaces weight with weight_orig and adds a weight_mask buffer; prune.remove makes the pruning permanent

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** I reproduced it: params ['bias', 'weight_orig'], buffer ['weight_mask'], 50.0 percent sparsity, then ['bias', 'weight'] after prune.remove.
</details>

---

### Question 23
**Section: Software development. Scenario:** What do a U-Net's skip connections do for a denoiser?

A. Carry fine detail from encoder stages to matching decoder stages, past the bottleneck
B. Replace the loss function
C. Convert images to text
D. Reduce the batch size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The U shape downsamples, upsamples, and concatenates matching feature maps; without the skips the same shape is an autoencoder.
</details>

---

### Question 24
**Section: Software development. Scenario:** A noise-prediction U-Net takes a 1x16x16 noisy image and a time step. What shape is its output?

A. A single scalar
B. 1x16x16, the same as the input, because it estimates the noise
C. A 10-class vector
D. A sentence

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** My forward pass returned (4, 1, 16, 16) for a batch of four, the same as the input.
</details>

---

### Question 25
**Section: Software development. Scenario:** How can a CLIP text embedding be used to build a text-to-image diffusion model?

A. Replace the images with the text
B. Delete the noise schedule
C. Use the embedding as the learning rate
D. Give the embedding to the denoiser as conditioning input so it predicts noise given the prompt

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** CLIP maps text and images into a shared space; conditioning the denoiser on the text embedding ties generated images to the prompt.
</details>

---

### Question 26
**Section: Software development. Scenario:** Which is an example of prompt engineering rather than retraining?

A. Changing the model's weights with a new optimizer
B. Quantizing the model
C. Specifying the task, context, output format and examples in the prompt
D. Pruning attention heads

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Prompt engineering shapes output through the input, with no weight updates.
</details>

---

### Question 27
**Section: Software development. Scenario:** Which is a software quality practice named in the blueprint's spirit?

A. Ship without tests to save time
B. Keep requirements verbal only
C. Avoid reporting progress
D. Version the code and data, test the data and the model, and monitor after deployment

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The objective is to follow best practices for software quality and reliability; the practices listed are the standard interpretation.
</details>

---

### Question 28
**Section: Trustworthy AI. Scenario:** Which is one of NVIDIA's four stated trustworthy AI principles?

A. Maximum model size
B. Secrecy of training data
C. Nondiscrimination: minimize bias and give all groups an equal opportunity to benefit
D. Latency

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVIDIA's page lists privacy, safety and security, transparency and nondiscrimination.
</details>

---

### Question 29
**Section: Trustworthy AI. Scenario:** In NIST's AI RMF, which function applies across all stages of an organization's AI risk management?

A. MAP only
B. GOVERN
C. MEASURE only
D. MANAGE only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NIST AI 100-1: while GOVERN applies to all stages, MAP, MEASURE and MANAGE can be applied in AI system-specific contexts and at specific stages.
</details>

---

### Question 30
**Section: Experimentation. Scenario:** A new image generator is compared with the old one by one number from one run. What is a more sound way to test accuracy and effectiveness?

A. Pick the best single run and report only that
B. Use the training set as the test set
C. Compare only the training loss
D. Repeat runs or folds, report mean and spread on held-out data, and keep a fixed set of test prompts for regression checks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Repeated, held-out evaluation shows the variation between runs; my five-fold result was 0.947 +- 0.025, and a single split can mislead.
</details>

---

## Where to go deeper

- [NCA-GENM cert page](../nvidia/generative-ai-multimodal-associate/README.md) - notes, plan, strategy
- **[📖 NVIDIA Generative AI Multimodal exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/)** - official blueprint
- **[📖 NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** - trustworthy AI framework
