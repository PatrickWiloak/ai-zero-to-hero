# Convolutional Networks and Computer Vision

**In one line:** Understand how a convolutional neural network (CNN) reads an image, what filters, pooling and transfer learning mean, and when to use a CNN, a vision transformer or a hosted vision model.
**Last reviewed:** 2026-11-07

---

## The short version

- An image is a grid of numbers (pixel brightness per colour channel). A plain network that flattens it into one long list throws away the fact that neighbouring pixels belong together.
- A **convolutional layer** slides a small grid of weights, a **filter**, across the image and records how strongly each patch matches. Early filters find edges; later layers combine them into textures, parts and objects.
- The same filter is reused at every position, so a CNN has far fewer weights than a fully connected network and spots a pattern wherever it appears.
- **Pooling** shrinks the picture between layers, keeping the strongest signals.
- You almost never train a vision model from scratch. **Transfer learning**, starting from a model pretrained on millions of images, works with a few hundred of your own.
- Vision transformers and multimodal LLMs now compete with CNNs. CNNs remain a sensible, cheap choice for many tasks, especially on small devices.

## What a filter does

Take a 3 by 3 filter. Place it over a 3 by 3 patch of the image, multiply matching numbers, add them up: one number. Slide it one step and repeat. The result is a new grid, a **feature map**, bright where the patch looked like the filter.

A filter with negative numbers on the left column and positive on the right lights up on vertical edges. Nobody designs these by hand in a modern network; training discovers filters that reduce the loss. This is the same dot product described in [Maths for ML without fear](../day-one/maths-for-ml-without-fear.md), applied to patches.

A layer has many filters (16, 64, 256), producing a stack of feature maps. The next layer's filters look across that whole stack, which is how edges become corners, then eyes, then faces. Zeiler and Fergus (2013) visualised what the layers respond to, cited in [Neural networks in plain English](neural-networks-plain-english.md).

## The usual building blocks

| Piece | What it does |
|---|---|
| Convolution | Finds local patterns with shared filters |
| Activation (ReLU) | Adds the bend that lets layers stack usefully |
| Pooling or stride | Halves the width and height, keeps the strongest responses |
| Batch normalisation | Keeps numbers in a range that trains stably |
| Final dense layers | Turn the pooled features into class scores |

A classic design repeats convolution, activation and pooling a few times, then flattens into a small classifier. The image shrinks while the number of feature maps grows.

## Going deeper: residual connections

Very deep plain stacks got harder to train, not better. He et al. (2015) added **skip connections**, which let a block pass its input straight through and learn only the correction. That made networks of 100+ layers trainable and won the 2015 ImageNet classification contest. Read the summary: [ResNet](../../papers/architectures/73-resnet/summary.md). Skip connections are now everywhere, including inside transformers.

## Tasks beyond "what is in this picture"

- **Classification**: one label per image.
- **Object detection**: boxes and labels for each object. Common families are the YOLO line and two-stage detectors.
- **Segmentation**: a label for every pixel. The U-Net design is the standard for medical and diffusion work: [U-Net](../../papers/architectures/74-unet/summary.md).
- **Embeddings and search**: turn images into vectors for similarity search. See [Embeddings and vector search](embeddings-and-vector-search.md).
- **Generation**: diffusion models often use convolutional U-Nets inside. See [Diffusion models](diffusion-models.md).

## CNN, vision transformer, or a hosted model?

- **Vision transformers** cut the image into patches and treat them like tokens: [Vision Transformer](../../papers/architectures/11-vision-transformer/summary.md). With lots of pretraining data they match or beat CNNs; with little data, CNNs' built-in assumption about locality helps.
- **Multimodal LLMs** answer questions about images and read documents with no training on your side: [Multimodal models](multimodal-models.md). Good for flexible, low-volume tasks; slower and costlier per image than a small CNN, and less predictable.
- **A small CNN** wins when you need millions of cheap, fast, repeatable predictions (factory inspection, on-phone features) with a fixed set of labels.

A reasonable order: try a hosted multimodal model first to see whether the task is feasible, then fine-tune a pretrained CNN if volume or cost demands it.

## Transfer learning in practice

1. Load a model pretrained on a large image set from a model hub (torchvision and Keras Applications both ship several).
2. Replace the last layer with one sized for your classes.
3. Train only that layer first, then optionally unfreeze deeper layers at a low learning rate.
4. Add **augmentation** (random crops, flips, brightness changes) so a small dataset behaves like a larger one.

Always split by *source*, not by image. If several photos of the same product land in both training and test sets, your score is inflated. See [Training, validation and overfitting](training-validation-and-overfitting.md).

## Common mistakes

- **Training from scratch on a few hundred images.** Start from pretrained weights.
- **Leaky splits.** Near-duplicate images across train and test inflate scores.
- **Different preprocessing at serving time.** Resize, crop and colour normalisation must match training exactly.
- **Ignoring where the data came from.** A model trained on clean studio photos fails on blurry phone photos. Test on images like the real ones.
- **Treating accuracy as the whole story.** Check per-class results; a rare defect class can be badly missed while overall accuracy looks fine.

## Next steps

- [Neural networks in plain English](neural-networks-plain-english.md)
- [Multimodal models](multimodal-models.md)
- [Diffusion models](diffusion-models.md)
- [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md) for the adapter-style way to customise big models
- [GPUs for AI](gpus-for-ai.md): why convolutions run well on them

## Sources

- He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition" (2015): https://arxiv.org/abs/1512.03385
- Ronneberger, Fischer and Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation" (2015): https://arxiv.org/abs/1505.04597
- Dosovitskiy et al., "An Image is Worth 16x16 Words" (2020): https://arxiv.org/abs/2010.11929
- Zeiler and Fergus, "Visualizing and Understanding Convolutional Networks" (2013): https://arxiv.org/abs/1311.2901
- Stanford CS231n, "Convolutional Neural Networks for Visual Recognition" course notes: https://cs231n.github.io/convolutional-networks/
- PyTorch tutorial, "Transfer Learning for Computer Vision": https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
