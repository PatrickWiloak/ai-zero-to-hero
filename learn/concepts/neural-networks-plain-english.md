# Neural Networks in Plain English

**In one line:** A neural network is a big stack of simple adjustable calculations that learns by nudging millions or billions of numbers to reduce its mistakes; this page explains neurons, layers, weights, training and why scale matters, with no calculus and one small network you can run.
**Last reviewed:** 2026-10-21

---

## The short version

- A **neuron** is a tiny calculation: multiply each input by a weight, add them up, add a bias, then pass the total through a simple bend (an **activation function**). That is all.
- A **layer** is many neurons side by side. A **network** is layers stacked so each layer's outputs are the next layer's inputs. "Deep" learning just means many layers.
- The **weights** and **biases** are the network's **parameters**: the adjustable numbers that store everything it has learned. Today's large models have billions to trillions of them.
- **Training** repeats three steps millions of times: make a prediction (**forward pass**), measure how wrong it was (**loss**), and work out how to nudge every weight to be a little less wrong (**backpropagation** and **gradient descent**).
- Neural networks are powerful because stacked layers can represent extremely complicated functions, and because they keep getting better as you add data, parameters and compute.
- Nobody writes the knowledge in. It ends up spread across the weights in ways we only partly understand, which is why studying the inside of a trained network is its own research field.

## Start with one neuron

Think of a neuron as a tiny judge that weighs evidence. Suppose it is deciding whether you will enjoy a film, using three inputs: is it a comedy (1 or 0), its average review score out of 10, and its length in hours.

```
inputs:   comedy = 1     score = 7.5     length = 2.5
weights:  +2.0           +0.8            -0.6
bias:     -4.0

total  = (1 x 2.0) + (7.5 x 0.8) + (2.5 x -0.6) + (-4.0)
       = 2.0 + 6.0 - 1.5 - 4.0
       = 2.5
output = squash(2.5)   ->  about 0.92   ("you will probably like it")
```

The **weights** say how much each piece of evidence matters, and in which direction: this neuron likes comedies and good reviews, and mildly dislikes long films. The **bias** shifts the threshold: how much positive evidence it needs before it says yes. The **activation function** (here a "squash" that maps any number to between 0 and 1) bends the straight-line sum into a curve. Without that bend, stacking neurons would add nothing, because a stack of straight lines is still a straight line.

One neuron can only draw one simple boundary. The power comes from combining many.

## Layers: neurons feeding neurons

Put several neurons side by side and they form a **layer**. Each one looks at the same inputs with its own weights, so each learns to detect something different. Feed that layer's outputs into another layer, and the second layer can combine the first layer's detections into something more complex.

The classic picture is image recognition. In a network trained to recognise objects in photos, researchers found that early layers respond to simple things like edges and patches of colour, middle layers to textures and shapes, and later layers to parts of objects such as eyes or wheels. Nobody told the network to organise itself that way. It emerged because that structure is useful for the task.

```
input       hidden layer 1     hidden layer 2     output
(pixels) ->  (edges, colours) -> (shapes, parts) -> ("cat": 0.97)
```

The layers between input and output are called **hidden layers**. A network with many of them is **deep**, which is where "deep learning" gets its name.

## Weights are where the knowledge lives

Every connection between neurons has a weight, so the number of parameters grows fast. A layer with 1,000 inputs and 1,000 neurons has a million weights. Modern language models stack dozens of much wider layers and reach billions or trillions of parameters.

When people say a model "has 8 billion parameters", they mean it is 8 billion of these adjustable numbers. When you download an open-weight model ([Run a model locally](../day-one/run-a-model-locally.md)), the multi-gigabyte file you get is essentially that list of numbers. Everything the model learned (grammar, facts, coding patterns, styles of reasoning) is encoded in them, spread across many weights rather than stored in any one place.

## How a network learns

A freshly created network has random weights and produces garbage. Training fixes that through a loop:

1. **Forward pass.** Feed in a training example and let the numbers flow through the layers to an output.
2. **Measure the loss.** Compare the output with the right answer and compute a single number for how wrong it was. Bigger is worse.
3. **Backpropagation.** Work backwards from the output to figure out, for every single weight, which direction to nudge it (up or down, and how strongly) to make the loss a little smaller. This is calculus done automatically by the software; you never do it by hand.
4. **Update.** Nudge every weight a small step in its helpful direction. This is **gradient descent**: picture walking downhill in fog, feeling which way the ground slopes and taking one small step.
5. **Repeat** with the next batch of examples, millions of times.

The size of each step is the **learning rate**. Too big and training overshoots and becomes unstable; too small and it takes forever. Smarter step rules such as Adam adjust the step size per weight automatically; the [Adam summary](../../papers/techniques/142-adam/summary.md) explains how, and [What is machine learning?](what-is-machine-learning.md) shows plain gradient descent on a two-parameter model.

## A tiny network you can run

Here is a complete two-layer network learning **XOR**, the classic problem a single neuron cannot solve: output 1 when exactly one of two inputs is 1. It needs only NumPy (`pip install numpy`).

```python
import numpy as np

rng = np.random.default_rng(0)

# XOR: output is 1 when exactly one input is 1. No straight line separates these.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

# One hidden layer of 8 neurons, one output neuron
W1, b1 = rng.normal(size=(2, 8)), np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)), np.zeros(1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for step in range(5000):
    # forward pass: inputs -> hidden layer -> output
    h = np.tanh(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)

    # backward pass: how should each weight change to reduce the error?
    d_out = out - y                         # error signal at the output
    d_h = (d_out @ W2.T) * (1 - h ** 2)     # passed back through the hidden layer
    W2 -= 0.1 * h.T @ d_out
    b2 -= 0.1 * d_out.sum(axis=0)
    W1 -= 0.1 * X.T @ d_h
    b1 -= 0.1 * d_h.sum(axis=0)

print(out.round(2).ravel())   # [0. 1. 1. 0.]
```

You do not need to follow every line of the backward pass. The point is the shape: forward, measure, backward, update, repeat. Real frameworks such as PyTorch compute the backward pass for you, and the same loop trains networks billions of times larger. Try changing the hidden layer to 2 neurons and running it with a few different seeds: sometimes it gets stuck. Capacity and luck both matter.

## Why bigger keeps working

For decades, researchers expected that very large networks would just memorise their training data. Instead, given enough data, bigger networks generalised better. In 2020, researchers at OpenAI showed that language model quality improves smoothly and predictably as you scale up parameters, data and compute together ([scaling laws summary](../../papers/techniques/12-scaling-laws/summary.md)), and DeepMind's Chinchilla work refined how to balance model size against data ([Chinchilla summary](../../papers/techniques/18-chinchilla/summary.md)). Rich Sutton's essay [The Bitter Lesson](../../papers/essays/111-bitter-lesson/summary.md) argues this is the main lesson of 70 years of AI research: general methods that scale with computation beat clever hand-built knowledge.

How far that continues is one of the field's big open questions; see [Scaling limits](../../explainers/open-questions/scaling-limits.md).

## Different shapes for different data

The neuron-and-layer idea is constant, but networks are wired differently for different kinds of data:

- **Convolutional networks** slide small filters across an image, reusing the same weights at every position. They dominated computer vision for a decade ([ResNet summary](../../papers/architectures/73-resnet/summary.md), [U-Net summary](../../papers/architectures/74-unet/summary.md)).
- **Recurrent networks** process a sequence one step at a time, carrying a memory forward. They were the standard for language until 2017 ([The Unreasonable Effectiveness of RNNs](../../papers/essays/109-unreasonable-effectiveness-of-rnns/summary.md), [seq2seq summary](../../papers/architectures/55-seq2seq/summary.md)).
- **Transformers** let every position in a sequence look directly at every other position through **attention**, and train efficiently in parallel. They now power almost all language models and many image models. See [Transformer architecture](transformer-architecture.md) and the [Attention Is All You Need summary](../../papers/architectures/01-attention-is-all-you-need/summary.md).

A large language model is a very large transformer trained to predict the next token. [LLM basics](llm-basics.md) picks up from here.

## What we do not understand

We know exactly what calculations a trained network performs, because we can read every weight. What we mostly do not know is *why* those billions of numbers produce the behaviour they do: which weights encode which concepts, and how they combine into reasoning. **Interpretability** research tries to answer that, and has made real progress in finding human-understandable features and circuits inside language models. The [induction heads](../../papers/techniques/126-induction-heads/summary.md), [sparse autoencoders](../../papers/techniques/82-sparse-autoencoders/summary.md) and [circuit tracing](../../papers/techniques/151-circuit-tracing/summary.md) summaries show what has been found so far.

## Common mistakes

- **Taking the brain analogy literally.** Artificial neurons were loosely inspired by biological ones, but a neural network is a mathematical function, not a simulation of a brain.
- **Thinking more parameters is always better.** Bigger models need more data and compute to train well, and cost more to run. A well-trained smaller model often beats a poorly trained bigger one.
- **Thinking the network "looks up" answers.** There is no database inside. Knowledge is spread across weights, which is why models can generalise and also why they can confidently produce wrong answers ([Hallucinations](hallucinations.md)).
- **Believing you need the calculus first.** Frameworks handle the derivatives. Understanding the loop matters far more than deriving it.

## Next steps

- [LLM basics](llm-basics.md)
- [Transformer architecture](transformer-architecture.md)
- [GPUs for AI](gpus-for-ai.md): why this arithmetic needs special hardware
- [ML engineer path](../start-here/ml-engineer-path.md) to train networks yourself

## Sources

- Rumelhart, Hinton and Williams, "Learning representations by back-propagating errors", *Nature* 323 (1986): https://www.nature.com/articles/323533a0
- Zeiler and Fergus, "Visualizing and Understanding Convolutional Networks" (2013), on what each layer of an image network responds to: https://arxiv.org/abs/1311.2901
- Kaplan et al., "Scaling Laws for Neural Language Models" (2020): https://arxiv.org/abs/2001.08361
- Rich Sutton, "The Bitter Lesson" (2019): http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- 3Blue1Brown, "Neural networks" video series (visual intuition for layers and backpropagation): https://www.3blue1brown.com/topics/neural-networks
- Goodfellow, Bengio and Courville, *Deep Learning* (MIT Press, 2016), chapter 6 "Deep Feedforward Networks": https://www.deeplearningbook.org/contents/mlp.html
