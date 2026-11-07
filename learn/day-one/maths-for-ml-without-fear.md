# Maths for ML Without Fear

**In one line:** Learn the four pieces of maths behind machine learning (vectors, matrices, probability, gradients) in plain English, with five lines of NumPy you can run to see each one.
**Last reviewed:** 2026-11-07

---

## The short version

- You do not need a maths degree to use or build AI. You need four ideas: **vectors** (a list of numbers), **matrices** (a grid of numbers that transforms a vector), **probability** (how sure we are), and **gradients** (which way to nudge a number to improve a score).
- Almost all of it is multiplying, adding and comparing numbers. Computers do the arithmetic; your job is to know what the arithmetic means.
- Every model you will meet follows one loop: make a guess, score the guess, nudge the numbers to score better. The nudge direction is the gradient.
- Read the page once for the picture, run the code, and come back to the maths only when a later page needs it. [Neural networks in plain English](../concepts/neural-networks-plain-english.md) is the best next page.

## Vectors: a list of numbers that describes one thing

A **vector** is an ordered list of numbers. A house could be `[3, 120, 1995]`: bedrooms, square metres, year built. A word, to a language model, is a vector of hundreds or thousands of numbers called an **embedding**. See [Embeddings and vector search](../concepts/embeddings-and-vector-search.md).

Two operations matter:

- **Dot product.** Multiply matching entries and add them up. `[1, 2, 3] . [4, 5, 6] = 1*4 + 2*5 + 3*6 = 32`. A big dot product means the two vectors point the same way.
- **Cosine similarity.** The dot product divided by the two vectors' lengths, so only direction counts. It runs from -1 (opposite) to 1 (identical direction). This is how a search system decides that two pieces of text mean similar things.

```python
import numpy as np
a = np.array([1.0, 2.0, 3.0]); b = np.array([4.0, 5.0, 6.0])
print("dot:", a @ b)
print("cosine:", round(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)), 4))
```

Output when run (NumPy, Python 3.14, 2026-11-07):

```
dot: 32.0
cosine: 0.9746
```

## Matrices: a machine that turns one vector into another

A **matrix** is a grid of numbers. Multiplying a matrix by a vector produces a new vector, where each output entry is the dot product of one matrix row with the input. A matrix with 2 rows and 3 columns turns a 3-number input into a 2-number output.

```python
W = np.array([[1.0, 0.0, -1.0], [0.5, 0.5, 0.5]])
print("W @ a:", W @ a)
```

```
W @ a: [-2.  3.]
```

Check row one by hand: `1*1 + 0*2 + (-1)*3 = -2`. Row two: `0.5*1 + 0.5*2 + 0.5*3 = 3`.

This is the main trick behind neural networks. One **layer** is a matrix multiply plus a small bend (an activation function). The matrix entries are the **weights**, the numbers training adjusts. A model with 7 billion parameters is mostly 7 billion numbers sitting in matrices. GPUs exist because they multiply big matrices very fast: see [GPUs for AI](../concepts/gpus-for-ai.md).

Shape rule of thumb: to multiply, the inner sizes must match. `(2 x 3) @ (3,)` works; `(2 x 3) @ (2,)` does not. Most beginner errors in ML code are shape errors, so print `.shape` often.

## Probability: being honestly unsure

**Probability** is a number from 0 (impossible) to 1 (certain). Three ideas cover most of what you need:

- **Distribution.** A list of probabilities for every possible outcome, adding up to 1. A language model's output is a distribution over the next token: perhaps 40% "the", 5% "a", and a long tail of tiny chances. Settings like temperature reshape that distribution. See [LLM basics](../concepts/llm-basics.md).
- **Conditional probability.** "How likely is A, given B?" The chance a customer cancels is different from the chance they cancel given three support calls this month. Almost every prediction is a conditional probability.
- **Expected value and averages.** The long-run average if you repeat something many times. Training minimises the *average* error over many examples, not the error on one.

Two traps worth knowing early. A model that says "90% sure" should be right about 90% of the time when it says that; this is called **calibration**, and many models are not calibrated. And rare events fool intuition: a test that is 99% accurate for a condition that 1 in 1,000 people have still produces mostly false alarms. This is why [training and validation](../concepts/training-validation-and-overfitting.md) look at more than accuracy.

## Gradients: which way is downhill

Training needs a single number that says how wrong the model is. That number is the **loss**. Training means changing the weights to make the loss smaller.

Picture standing on a hill in fog, wanting to reach the valley. You cannot see the valley, but you can feel which direction slopes down under your feet. The **gradient** is that slope: for each weight, it says how much the loss goes up if you increase that weight a little. Step the opposite way and the loss falls. This is **gradient descent**.

A one-weight example. Let the loss be `(w - 3)^2`, which is smallest at `w = 3`. Its slope is `2 * (w - 3)`. Start at `w = 0` and step against the slope with a **learning rate** of 0.25:

```python
w = 0.0
for step in range(5):
    grad = 2 * (w - 3)
    w = w - 0.25 * grad
    print(f"step {step+1}: w = {w:.4f}")
```

```
step 1: w = 1.5000
step 2: w = 2.2500
step 3: w = 2.6250
step 4: w = 2.8125
step 5: w = 2.9062
```

Each step closes half the remaining gap to 3. Real models do exactly this, only with billions of weights at once. **Backpropagation** is the bookkeeping that computes every weight's slope efficiently, using the chain rule from calculus (the slope of a chain of operations is the product of the slopes of its links). Libraries such as PyTorch do it for you automatically.

The learning rate is the step size. Too small and training crawls. Too large and you overshoot the valley and the loss bounces or explodes. Almost every "my training diverged" problem starts here.

## Putting it together

A model is a function from input vectors to output vectors, built from matrices. Its output is turned into probabilities. A loss compares those probabilities to the right answer. The gradient of the loss tells every weight which way to move. Repeat millions of times. Nothing else is hiding behind the word "learning".

## Common mistakes

- **Trying to learn all the maths first.** Learn each idea when a project needs it. Running code teaches the shapes faster than reading proofs.
- **Ignoring shapes.** If code fails with a size mismatch, print the shape of every array before debugging anything else.
- **Reading a probability as a guarantee.** 0.9 is a belief, not a promise. Check calibration if decisions depend on the number.
- **Setting the learning rate once and never looking.** If the loss goes up or flatlines, change it first.

## Next steps

- [Neural networks in plain English](../concepts/neural-networks-plain-english.md): these four ideas, assembled into a network
- [What is machine learning?](../concepts/what-is-machine-learning.md)
- [Training, validation and overfitting](../concepts/training-validation-and-overfitting.md)
- [Python for AI](python-for-ai.md) to set up the tools used above
- Sibling site for the statistics side: [Data Zero to Hero](https://data.noblerworks.com/)

## Sources

- Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), free online: https://mml-book.github.io/
- 3Blue1Brown, "Essence of linear algebra" and "Neural networks" video series: https://www.3blue1brown.com/topics/linear-algebra and https://www.3blue1brown.com/topics/neural-networks
- NumPy documentation, "NumPy: the absolute basics for beginners": https://numpy.org/doc/stable/user/absolute_beginners.html
- Goodfellow, Bengio and Courville, *Deep Learning* (MIT Press, 2016), chapters 2 to 4 on linear algebra, probability and numerical computation: https://www.deeplearningbook.org/
- Rumelhart, Hinton and Williams, "Learning representations by back-propagating errors", *Nature* 323 (1986): https://www.nature.com/articles/323533a0
