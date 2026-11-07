# Section 3: Experimentation (25%)

**Last reviewed:** 2026-11-07

The largest section: assist in developing and testing multimodal models, manage and preprocess data from different sources, use multimodal models to improve explainability, test data quality and consistency, and test models for accuracy and effectiveness. The five objectives are on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07). Reading-list items for it include the Hugging Face Diffusion Models course (Units 1 and 2), data augmentation, the two-time-scale update rule paper (FID), CLIP and early versus late fusion. Code ran on CPU (PyTorch 2.15.0+cpu, scikit-learn).

## Developing and testing multimodal models: how diffusion models are built

Image generation is the multimodal experiment the exam names (the Software Development section asks you to build a U-Net). The Hugging Face course describes the recipe: during training, noise is added to dataset images "in different amounts", so the model learns to fix both very noisy and nearly clean images; at generation, you start from random noise and apply the model repeatedly, updating the input slightly each time, which gradually produces an image. Because each step changes the image only slightly, early estimate errors can be corrected in later steps.

**[📖 Hugging Face Diffusion Models Course, Unit 1](https://huggingface.co/learn/diffusion-course/unit1/1)** - The noising and denoising loop

I trained a tiny noise-prediction U-Net (details in note 6) on 16 by 16 circle and square images. The training loss fell from 0.953 over the first ten steps to 0.077 over the last ten. That is the experiment's first check: the loss goes down. But a falling loss does not prove generation works. When I then sampled from pure noise with that same tiny model, the pixel range came out as `[-1.43, 7.54]` against training images in `[-1, 1]`, so the samples were not clean images. The lesson to carry into the exam: training loss is a diagnostic, not a quality metric; evaluate generated outputs separately.

- **Diffusion model** - a generative model trained to remove noise from images that were noised by a known process; generation starts from noise and denoises step by step.

## Managing and preprocessing multi-source data

Data from several sources has different formats, resolutions, label conventions and quality. Preprocessing makes them consistent: resize and normalize images, tokenize text, resample audio, align each sample's modalities by an id, and split train/validation/test before any fitting so that no information leaks. Data augmentation (flips and crops for images, paraphrasing for text) expands limited data; it is on NVIDIA's reading list (a DataCamp guide), which I did not fetch.

## Test data quality and consistency

Write the checks as code so they run on every dataset version. My audit (note 2) counted duplicates, missing paths, empty captions and corrupt images. For consistency across modalities add checks that every image has a caption, captions are in the expected language, and image dimensions match what the encoder expects. A dataset test that fails should block training, in the same way a unit test blocks a release.

## Use multimodal models to improve explainability

Models that join modalities can help explain each other: an image-captioning model describes what a classifier sees, and attention maps show which words or regions drove a decision (note 2). A model-agnostic method like permutation importance also works across modalities; in my run it correctly identified the two informative features out of six (importances 0.513 and 0.075, the rest near zero). A caution from the same family of methods: an explanation can look convincing without being faithful, so check it against an intervention (remove or shuffle the part the explanation points to and see whether the prediction changes), which is exactly what permutation importance does.

## Test models for accuracy and effectiveness

Choose metrics per task: accuracy, precision and recall for classification; for generation, human review plus automated measures. The reading list names the two-time-scale update rule paper (the source of the Fréchet Inception Distance, FID, for image generation) and the Hugging Face Evaluate library; I did not fetch either, so I do not describe FID's formula here. Basic discipline: report cross-validated or repeated-run results (my forest scored `0.947 +- 0.025` over five folds), test on held-out data, and keep a regression set of fixed prompts to compare versions.

## Early versus late fusion

The reading list includes "Early vs. Late Fusion". **Early fusion** combines the modalities' features first and trains one model on the joined input. **Late fusion** trains a model per modality and combines their predictions. I compared them on two noisy views of the same label (each view alone is weakly informative):

```
fusion: single modality 0.82 | early fusion 0.86 | late fusion 0.82
```

Early fusion was best here at 0.86, against 0.82 for one modality alone and for late fusion. On 100 test points a 0.04 gap is about four samples, so this shows the mechanism and not a general ranking. Early fusion can learn interactions between modalities; late fusion is simpler, tolerates a missing modality, and lets each part be trained and replaced separately.

- **Early fusion** - combining the features of several modalities before the model, so one model learns from the joined input.
- **Late fusion** - training a model per modality and combining their outputs (for example by averaging scores).

## Check yourself against the objectives

Describe the diffusion training and sampling loop; explain why a falling training loss does not prove good samples; list data checks that should block training; describe one explainability method and how to test it; and say when to choose early or late fusion. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
