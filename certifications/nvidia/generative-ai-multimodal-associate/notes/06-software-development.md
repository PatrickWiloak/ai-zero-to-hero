# Section 6: Software Development (15%)

**Last reviewed:** 2026-11-07

Five objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07): collaborate with clients on requirements, data gathering, reporting, deployment and integration; follow best practices for software quality and reliability; use prompt engineering to influence generative output; build a U-Net to generate images from pure noise and as a type of autoencoder; and generate images from English prompts using CLIP and use CLIP to train a text-to-image diffusion model. The last two are hands-on, and I ran them. Code ran on CPU (PyTorch 2.15.0+cpu).

## Build a U-Net

A **U-Net** is an encoder-decoder with skip connections: the encoder downsamples and extracts features, the decoder upsamples back to the input resolution, and each decoder stage receives the matching encoder feature map through a skip connection. That "U" shape makes it the standard denoising network in diffusion models, and with the skips removed the same shape is an **autoencoder** (compress, then reconstruct). The Hugging Face course's description is of "the model" that takes noisy inputs and estimates how to denoise them; the page I read does not name the architecture, so "U-Net" as the denoiser here is the objective's own wording.

**[📖 Hugging Face Diffusion Models Course, Unit 1](https://huggingface.co/learn/diffusion-course/unit1/1)** - Noising, denoising and sampling

Mine takes a noisy 1x16x16 image plus the time step as a second channel, and returns a same-size noise estimate:

```python
class UNet(nn.Module):
    def forward(s, x, t):
        x = torch.cat([x, t[:, None, None, None].expand(-1, 1, 16, 16)], 1)   # time as a channel
        h1 = s.d1(x); h2 = s.d2(F.max_pool2d(h1, 2)); m = s.mid(F.max_pool2d(h2, 2))   # encoder + bottleneck
        u = F.interpolate(m, scale_factor=2); u = s.u2(torch.cat([u, h2], 1))              # skip connection
        u = F.interpolate(u, scale_factor=2); u = s.u1(torch.cat([u, h1], 1))              # skip connection
        return s.out(u)
```

```
U-Net parameters: 53521 | forward shape: (4, 1, 16, 16) (output same size as input: noise estimate)
```

The output shape equals the input shape, because the network predicts the noise that was added to the image. The two `torch.cat(..., [u, h])` lines are the skip connections, which carry fine detail past the bottleneck.

- **U-Net** - an encoder-decoder convolutional network with skip connections between matching resolutions, used as the denoiser in diffusion models.
- **Autoencoder** - a network that compresses its input to a small representation and reconstructs it; a U-Net without skip connections has this shape.

## Generate images from pure noise

Diffusion training adds noise to clean images by a schedule and teaches the U-Net to predict that noise. I used 200 steps with a linear noise schedule, a standard DDPM-style loop:

```python
xt = ab[t].sqrt() * x0 + (1 - ab[t]).sqrt() * eps      # forward: noise the image
loss = F.mse_loss(net(xt, t / T), eps)                  # train: predict the noise
```

```
noise-prediction loss: first 10 steps 0.953 -> last 10 steps 0.077
```

Sampling starts from `torch.randn` and applies the network 200 times, each time subtracting the predicted noise and, except at the last step, adding a little fresh noise. My result was honest, not good:

```
sampled from pure noise: pixel range [-1.43, 7.54]; training-image std 0.83; sample std 0.79
```

The loss fell by an order of magnitude after only 300 training steps, but the samples ranged up to 7.54 when the training images lie in [-1, 1], so this small model did not learn to generate clean images. (The sampling code is a plain DDPM loop; I did not tune the schedule or train longer.) Two real lessons: training loss is not sample quality, and the model needs far more training than a toy loop. A working text-to-image system uses pretrained components.

## Generate images from text with CLIP

CLIP's role in text-to-image generation is to connect language to images: a text encoder and an image encoder trained contrastively, so text embeddings land near the embeddings of matching images (note 1 shows the loss; the paper trained on 400 million image-text pairs and reaches zero-shot ImageNet accuracy comparable to a ResNet-50 trained on 1.28 million labeled examples). Two uses follow:

1. **Guide generation.** Score candidate images against the prompt's text embedding and steer toward higher similarity.
2. **Condition a diffusion model.** Feed the CLIP text embedding to the denoiser as a conditioning input so it learns to produce images matching a prompt. Training a text-to-image diffusion model with CLIP means the U-Net gets the text embedding (in addition to time step) as input and learns to predict noise given both. The reading list pairs the CLIP article with the Hugging Face diffusion course.

I did not train a CLIP-conditioned diffusion model in this guide: it needs pretrained CLIP weights and GPU training time that a CPU walkthrough cannot give, and I could not fetch OpenAI's CLIP page (it returned 403), so the description above rests on the paper's abstract and the objective's wording.

**[📖 CLIP paper (arXiv 2103.00020)](https://arxiv.org/abs/2103.00020)** - Contrastive image-text pretraining

- **Conditioning** - giving a generative model extra input (such as a text embedding) so its output depends on it.

## Prompt engineering for generative output

Prompt engineering shapes output through the prompt rather than the weights: state the task and audience, give context, specify the format, show examples, and iterate on failures. For image models, the same applies to the prompt's subject, style and constraints. The NVIDIA reading list points to the Prompt Engineering Guide, which I did not fetch, so these are standard practices, not quotes.

## Client collaboration and software quality

The page lists collaborating with clients on requirements, data gathering, progress reporting, deployment and integration, and following best practices for quality and reliability. These are professional-practice objectives; the pages fetched give no detail beyond the objective text. Sensible interpretation: write down requirements and acceptance tests, version the code and data, review changes, test the data (note 3) and the model, monitor in production, and report progress with measured results.

## Check yourself against the objectives

Sketch a U-Net and say what the skip connections do; write the diffusion training step; say why a falling loss does not guarantee good samples; and explain how CLIP's text embedding conditions an image generator. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
