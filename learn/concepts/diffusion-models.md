# Diffusion Models

**In one line:** Diffusion models make images (and video and audio) by starting from pure random noise and removing it a little at a time, guided by your text prompt; this page explains the idea, why it works, how text steers it, and what the main variants are, with a small runnable example of the noising process.
**Last reviewed:** 2026-10-21

---

## The short version

- A diffusion model is trained on a simple game: take a real image, add a known amount of random noise, and ask the network to predict the noise. Do this at every noise level from "barely noisy" to "pure static".
- To **generate**, run the game backwards: start from pure noise and repeatedly ask the network "what noise is in this?", subtract a bit of it, and repeat. After tens of steps, an image emerges.
- **Text prompts** steer each denoising step. A text encoder turns your prompt into numbers, and the network uses them to decide which image to reveal. **Classifier-free guidance** turns up how strongly the prompt is followed.
- **Latent diffusion** (the idea behind Stable Diffusion) does all this in a compressed version of the image, which makes it fast enough to run on a consumer GPU.
- Modern systems use **transformers** instead of the older U-Net, and **flow matching** instead of the original noise schedule, but the core idea of learning to turn noise into data is the same.
- Diffusion is not the only way to generate images. Some recent systems generate images token by token like a language model, or combine the two.

## The core idea: learn to remove noise

Think about sculpture. A sculptor does not build a statue by adding clay; they start with a block and remove what does not belong. A diffusion model does something similar with noise. It starts from a canvas of pure random static and, step by step, removes the parts that do not look like an image.

Removing noise from a slightly noisy photo is a much easier problem than creating a photo from nothing. Diffusion's insight is that you can chain many easy problems together. If you can remove a little noise from any image at any noise level, you can start from pure noise and walk all the way back to a clean image.

The approach was proposed in 2015 and became practical in 2020 with **Denoising Diffusion Probabilistic Models (DDPM)** by Ho, Jain and Abbeel, which showed image quality competitive with the best generative models of the time. The [DDPM summary](../../papers/image-generation/06-diffusion-models/summary.md) walks through the paper.

## Training: the noising game

Training needs no labels beyond the images themselves (plus captions, for text-to-image models). For each training step:

1. Take a real image from the dataset.
2. Pick a random noise level `t` between 1 and, say, 1,000.
3. Mix the image with random noise in the proportion set by `t`: little noise for small `t`, almost all noise for large `t`.
4. Show the network the noisy image and the value of `t`, and ask it to predict the exact noise that was added.
5. Measure how wrong the prediction was and nudge the weights (the standard training loop from [Neural networks in plain English](neural-networks-plain-english.md)).

Because the noise is added by a known formula, you can jump straight to any noise level in one step. Here is that forward process on a five-pixel "image", using the noise schedule from the DDPM paper. It needs only NumPy.

```python
import numpy as np

rng = np.random.default_rng(0)
x0 = np.array([0.9, 0.8, 0.1, -0.7, -0.9])      # a tiny "image" of 5 pixel values
T = 1000
betas = np.linspace(1e-4, 0.02, T)              # the DDPM noise schedule
alpha_bar = np.cumprod(1 - betas)               # how much signal survives by step t

for t in [0, 100, 300, 600, 999]:
    noise = rng.normal(size=x0.shape)
    xt = np.sqrt(alpha_bar[t]) * x0 + np.sqrt(1 - alpha_bar[t]) * noise
    print(f"t={t:4d}  signal kept={np.sqrt(alpha_bar[t]):.2f}  x_t={np.round(xt, 2)}")
```

```text
t=   0  signal kept=1.00  x_t=[ 0.9   0.8   0.11 -0.7  -0.91]
t= 100  signal kept=0.95  x_t=[ 0.97  1.18  0.4  -0.89 -1.26]
t= 300  signal kept=0.63  x_t=[ 0.08  0.53 -1.75 -0.61 -1.53]
t= 600  signal kept=0.16  x_t=[-0.58 -0.41 -0.3   0.29  0.89]
t= 999  signal kept=0.01  x_t=[-0.12  1.37 -0.66  0.35  0.9 ]
```

By step 999, almost nothing of the original survives; it is static. The network's whole job is to learn, for any `x_t` and `t`, what noise was mixed in. A real image has hundreds of thousands of pixel values instead of five, but the formula is the same.

## Generation: running it backwards

To make a new image:

1. Start with pure random noise, the same shape as an image.
2. Ask the trained network to predict the noise in it at the highest noise level.
3. Subtract part of that predicted noise, giving a slightly less noisy image.
4. Repeat at the next lower noise level, and so on down to zero.

Early steps decide the overall layout: where things are, the broad colours. Later steps fill in edges, textures and fine detail. Because you start from random noise, every run gives a different image; fixing the random **seed** gives the same image again.

The original DDPM needed around 1,000 steps per image, which was slow. Later work cut that sharply: [DDIM](../../papers/image-generation/70-ddim/summary.md) showed you could skip most steps with little quality loss, and [consistency models](../../papers/image-generation/120-consistency-models/summary.md) aim for one or a few steps. Many current systems generate an image in tens of steps or fewer.

## How text steers the image

A text-to-image model adds one ingredient: at every denoising step, the network also receives an encoding of your prompt. A separate text encoder turns "a red fox reading a newspaper in the snow, watercolour" into a set of vectors, and the network attends to them (through the same **attention** mechanism transformers use) while deciding what noise to remove. The prompt does not draw the picture; it biases every one of the denoising decisions toward images that match it.

Text encoders trained to connect images and captions, such as [CLIP](../../papers/multimodal/08-clip/summary.md), made this work well. Later systems found that richer text encoders and better training captions improve how faithfully prompts are followed; the [Imagen summary](../../papers/image-generation/91-imagen/summary.md) and [DALL-E 3 summary](../../papers/image-generation/48-dalle3/summary.md) cover that.

**Classifier-free guidance** is the knob that controls how strongly the prompt is followed. During training, the prompt is randomly dropped some of the time, so the same network learns both "denoise toward this prompt" and "denoise toward any plausible image". At generation time it makes both predictions and pushes the result further in the direction of the prompted one. Higher guidance gives images that match the prompt more literally but can look over-saturated; lower guidance gives more natural but looser results. See the [classifier-free guidance summary](../../papers/image-generation/69-classifier-free-guidance/summary.md).

## Latent diffusion: making it affordable

Running hundreds of network passes over a full-resolution image is expensive. **Latent diffusion**, introduced by Rombach and colleagues in late 2021 and the basis of Stable Diffusion, solves this by working in a compressed space:

1. An **autoencoder** is trained separately to compress images into a much smaller grid of numbers (a **latent**) and decompress them back with little visible loss. The [VAE](../../papers/image-generation/57-vae/summary.md) and [VQ-GAN](../../papers/image-generation/90-vq-gan/summary.md) summaries explain these compressors.
2. The diffusion model learns to denoise those small latents instead of full images.
3. At the end, the decoder turns the final latent back into a full-size image.

Because the latent is many times smaller than the image, everything runs far faster, which is what made high-quality image generation possible on consumer GPUs. The [Stable Diffusion summary](../../papers/image-generation/07-stable-diffusion/summary.md) covers the details.

## What changed after 2022

The idea of "learn to turn noise into data" stayed. Three pieces were upgraded:

- **The network.** Early diffusion models used a [U-Net](../../papers/architectures/74-unet/summary.md), a convolutional design originally built for medical image segmentation. **Diffusion transformers (DiT)** replaced it with a transformer operating on patches of the latent, which scales better with size and compute. OpenAI's Sora video model was described as a diffusion transformer working on patches of video; see the [Sora and DiT summary](../../papers/image-generation/44-sora-dit/summary.md).
- **The training objective.** **Flow matching** and **rectified flow** recast the problem as learning a direct path from noise to data, which tends to be simpler to train and to sample in fewer steps. Stable Diffusion 3 adopted it; see the [flow matching summary](../../papers/image-generation/72-flow-matching-sd3/summary.md).
- **Control.** [ControlNet](../../papers/image-generation/71-controlnet/summary.md) lets you steer generation with a sketch, a pose skeleton or a depth map in addition to text, and [DreamBooth](../../papers/image-generation/92-dreambooth/summary.md) fine-tunes a model on a handful of photos so it can generate a specific person, pet or product.

Diffusion also spread beyond still images. Video models extend the denoising across frames. Audio and speech models use similar ideas. In robotics, the [pi0 summary](../../papers/robotics/124-pi0/summary.md) describes a model that uses flow matching to generate robot actions.

## Diffusion versus the alternatives

Before diffusion, the leading image generators were **GANs** ([GAN summary](../../papers/image-generation/02-generative-adversarial-networks/summary.md)), which train a generator against a critic. GANs are fast at generation but notoriously unstable to train and prone to producing a narrow range of outputs. Diffusion models are slower to sample but stable to train and good at covering the full variety of their training data, which is largely why they took over.

Diffusion is not the only approach today. Language-model-style systems can generate images as sequences of discrete tokens, using image tokenizers such as [VQ-VAE](../../papers/image-generation/89-vq-vae/summary.md) and [VQ-GAN](../../papers/image-generation/90-vq-gan/summary.md); the original DALL-E (2021) worked this way, before its successor switched to diffusion ([DALL-E 2 summary](../../papers/image-generation/119-dalle2-unclip/summary.md)). Some multimodal models now generate images natively alongside text. In practice you rarely need to know which method a product uses; the mental model of "a model learned the distribution of images and samples new ones that match your prompt" covers both. [Multimodal models](multimodal-models.md) covers models that handle several kinds of input and output.

## Limits and risks

- **Text and small details.** Older diffusion models were notoriously bad at spelling words inside images and at hands. Newer models are much better, but fine details and exact counts still go wrong.
- **Training data and copyright.** These models learn from very large image collections scraped from the web, and whether that training is lawful, and how close outputs can come to specific copyrighted works, is the subject of ongoing lawsuits and policy debate.
- **Misuse.** Realistic generated images of real people, fake evidence and non-consensual imagery are real harms. Providers add filters and provenance signals such as watermarks or content credentials, with varying effectiveness. [Responsible AI basics](../../safety/governance/responsible-ai-basics.md) covers the governance side.

## Common mistakes

- **Thinking the model searches for or collages existing images.** It generates new pixels from noise. It can, however, reproduce training images closely in some cases, especially ones that appeared many times.
- **Cranking guidance to the maximum.** Very high guidance gives harsh, over-saturated images. Moderate values usually look best.
- **Writing prompts like search queries.** Describe the image: subject, setting, style, lighting, composition.
- **Assuming one seed is representative.** Generate several and pick; variation between seeds is large.

## Next steps

- [Multimodal models](multimodal-models.md)
- [DDPM summary](../../papers/image-generation/06-diffusion-models/summary.md), then [Stable Diffusion](../../papers/image-generation/07-stable-diffusion/summary.md) and [flow matching](../../papers/image-generation/72-flow-matching-sd3/summary.md)
- [Researcher path](../start-here/researcher-path.md), thread 6, for the full generative media reading order
- [GPUs for AI](gpus-for-ai.md)

## Sources

- Sohl-Dickstein et al., "Deep Unsupervised Learning using Nonequilibrium Thermodynamics" (2015): https://arxiv.org/abs/1503.03585
- Ho, Jain and Abbeel, "Denoising Diffusion Probabilistic Models" (2020; linear beta schedule from 1e-4 to 0.02 over 1,000 steps): https://arxiv.org/abs/2006.11239
- Song, Meng and Ermon, "Denoising Diffusion Implicit Models" (2020): https://arxiv.org/abs/2010.02502
- Ho and Salimans, "Classifier-Free Diffusion Guidance" (2022): https://arxiv.org/abs/2207.12598
- Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models" (2021): https://arxiv.org/abs/2112.10752
- Peebles and Xie, "Scalable Diffusion Models with Transformers" (2022): https://arxiv.org/abs/2212.09748
- Lipman et al., "Flow Matching for Generative Modeling" (2022): https://arxiv.org/abs/2210.02747
- Esser et al., "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis" (Stable Diffusion 3, 2024): https://arxiv.org/abs/2403.03206
- OpenAI, "Video generation models as world simulators" (Sora technical report, February 2024): https://openai.com/index/video-generation-models-as-world-simulators/
