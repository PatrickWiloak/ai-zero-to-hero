# What Is Machine Learning?

**In one line:** Machine learning is writing programs whose behaviour is learned from examples instead of spelled out in rules; this page explains the idea, the three main kinds of learning, how training and testing work, and how today's chatbots fit into the same picture.
**Last reviewed:** 2026-10-21

---

## The short version

- In ordinary programming, a person writes the rules. In **machine learning (ML)**, a person supplies examples and a learning algorithm finds the rules, which are stored as numbers called **parameters** or **weights**. The result is a **model**.
- **Training** is the slow, expensive step where the model's parameters are adjusted to fit the examples. **Inference** is using the finished model on new inputs. Training happens once (or occasionally); inference happens every time someone uses it.
- There are three main kinds of learning: **supervised** (examples come with right answers), **unsupervised** (find structure without answers), and **reinforcement** (learn from rewards for actions). Modern language models use all three at different stages.
- The test of a model is how it does on **data it has never seen**. A model that memorises its training examples but fails on new ones is **overfitting**, and avoiding that is the central discipline of the field.
- **Deep learning** is ML with large neural networks. **Generative AI** is deep learning used to produce new text, images, audio or video. Large language models are generative AI trained mostly to predict the next piece of text.

## Rules versus examples

Imagine writing a program to decide whether an email is spam. The traditional approach is rules: if the subject contains "FREE MONEY", or the sender is on a blocklist, or there are more than five exclamation marks, mark it as spam. You quickly hit two problems. There are endless variations (spammers adapt), and many of the signals are subtle combinations no person would think to write down.

The machine learning approach turns this around. Collect thousands of emails that people have already marked "spam" or "not spam". Choose a model, a flexible mathematical function with many adjustable numbers. Then run a **learning algorithm** that repeatedly nudges those numbers so the function's outputs match the labels on the examples. When it is done, you have a spam filter, and nobody wrote its rules. They were learned from the data.

Andrej Karpathy called this shift "Software 2.0": instead of writing code, you specify a goal and collect data, and the optimisation process writes the program, as weights. The [Software 2.0 summary](../../papers/essays/110-software-2/summary.md) is a short read on why this changes how software gets built.

## A worked example you can follow

Suppose you want to predict the price of a flat from its size. You have past sales:

| Size (m²) | Price (thousands) |
|---|---|
| 40 | 180 |
| 55 | 240 |
| 70 | 300 |
| 85 | 345 |
| 100 | 410 |

A very simple model is a straight line: `price = w x size + b`. The two numbers `w` (slope) and `b` (intercept) are the parameters. Training means finding the `w` and `b` that make the line's predictions closest to the real prices. Here is that process in Python, done the way almost all modern ML is done: start with a guess, measure the error, nudge the parameters to reduce it, repeat.

```python
sizes  = [40, 55, 70, 85, 100]
prices = [180, 240, 300, 345, 410]

w, b = 0.0, 0.0          # start with a bad guess
learning_rate = 0.00015

for step in range(200_000):
    # how wrong are we, and in which direction should w and b move?
    grad_w = grad_b = 0.0
    for x, y in zip(sizes, prices):
        error = (w * x + b) - y
        grad_w += 2 * error * x / len(sizes)
        grad_b += 2 * error / len(sizes)
    w -= learning_rate * grad_w   # nudge downhill
    b -= learning_rate * grad_b

print(f"price ~= {w:.2f} x size + {b:.1f}")
print(f"prediction for 60 m2: {w * 60 + b:.0f}")
# price ~= 3.77 x size + 31.1
# prediction for 60 m2: 257
```

It takes a lot of small steps because the learning rate has to be small to stay stable; real training code rescales the inputs first so it converges much faster.

That loop is **gradient descent**, and it is the same basic idea that trains networks with trillions of parameters. The difference is scale: billions of examples instead of five, a far more flexible function than a straight line, and specialised hardware to do the arithmetic. [Neural networks in plain English](neural-networks-plain-english.md) shows how the function gets more flexible; the [Adam optimiser summary](../../papers/techniques/142-adam/summary.md) covers the improved version of "nudge downhill" that most models use.

## The three kinds of learning

**Supervised learning: learning from labelled examples.** Each training example has an input and the correct output: an email and "spam", an X-ray and "fracture", a house and its sale price. The model learns to map inputs to outputs. This covers most classic business ML: fraud detection, demand forecasting, churn prediction, document classification. When the output is a category it is called **classification**; when it is a number, **regression**.

**Unsupervised learning: finding structure without labels.** You have data but no right answers, and you want the model to find patterns: group customers into segments (**clustering**), compress data into a smaller form, or spot unusual transactions (**anomaly detection**). **Embeddings**, which turn text or images into lists of numbers that capture meaning, come from this family of ideas and power modern search and retrieval; see [Embeddings and vector search](embeddings-and-vector-search.md) and the [word2vec summary](../../papers/techniques/53-word2vec/summary.md).

A crucial variant is **self-supervised learning**, where the labels come free from the data itself. Hide the next word of a sentence and ask the model to predict it; the "label" is just the word you hid. Because the internet supplies endless text, this lets you train on vastly more data than anyone could ever label by hand. It is how large language models are pretrained.

**Reinforcement learning: learning from rewards.** An agent takes actions in an environment and receives rewards or penalties, and learns a strategy that earns more reward over time. It is how systems learned to play games at superhuman level (see the [AlphaZero summary](../../papers/techniques/102-alphazero/summary.md)) and, since 2022, a key step in turning language models into helpful assistants and, more recently, into models that reason step by step. The [InstructGPT summary](../../papers/language-models/05-instructgpt-rlhf/summary.md) and the [reasoning models explainer](../../explainers/concepts/reasoning-models.md) tell that story.

## Training, validation and testing

How do you know a model is any good? Not by checking it on the examples it trained on: it could simply have memorised them. The standard practice is to split your data three ways before you start:

- **Training set** (often around 70 to 80%): what the model learns from.
- **Validation set**: used while developing, to compare model choices and settings.
- **Test set**: locked away and used once at the end, to estimate how the model will do in the real world.

A model that does brilliantly on training data and poorly on the test set has **overfit**: it learned the noise and quirks of its examples rather than the general pattern. A model that does poorly on both has **underfit**: it is too simple to capture the pattern. Most of the craft of ML is steering between the two.

A related trap is **data leakage**: information from the test set sneaking into training, which makes results look better than they will be in reality. It happens in subtle ways (duplicate records, future information in the features), and it is a live problem for language models too, where benchmark questions can end up in the internet text they are trained on. The [contamination and saturation explainer](../../explainers/benchmarks/contamination-and-saturation.md) covers how this distorts AI leaderboards.

## Where deep learning and generative AI fit

These terms nest inside each other:

```
Artificial intelligence    the broad goal: machines doing things we call intelligent
 └─ Machine learning       behaviour learned from data
     └─ Deep learning      ML with large multi-layer neural networks
         └─ Generative AI  deep learning that produces new content
             └─ LLMs       generative models of text (and increasingly images, audio, video)
```

For decades, ML mostly meant smaller models on structured data, and for many business problems with tables of numbers that is still the right tool. Deep learning took over problems involving images, audio and language from around 2012, as more data and GPU computing made large neural networks practical. The [ResNet summary](../../papers/architectures/73-resnet/summary.md) captures that era. Then the [transformer](transformer-architecture.md) in 2017 and the discovery that language models improve predictably with scale ([scaling laws summary](../../papers/techniques/12-scaling-laws/summary.md)) led to today's large language models. The [timeline of AI](../../explainers/history/timeline-of-ai.md) walks through the whole history.

A modern chat assistant combines all three kinds of learning:

1. **Self-supervised pretraining** on huge amounts of text, predicting the next token. The model learns language, facts and patterns of reasoning. ([LLM basics](llm-basics.md), [GPT-3 summary](../../papers/language-models/04-gpt3-few-shot-learners/summary.md))
2. **Supervised fine-tuning** on examples of good assistant answers, so it follows instructions.
3. **Reinforcement learning** from human preferences, or from automatically checkable rewards such as correct maths answers, so it becomes more helpful and better at reasoning.

## What ML cannot do

A model can only learn patterns that are present in its data. If the data is biased, the model will be too. If the world changes after training (new products, new laws, new slang), the model does not know unless it is retrained or given the new information. And because a model is fitted to make its outputs look like its training data, it can produce outputs that look right without being right, which for language models is called [hallucination](hallucinations.md). None of these are bugs to be fixed once; they are properties of learning from examples, to be managed.

## Common mistakes

- **Thinking ML is magic or thinking it is "just statistics".** It is a way to build functions from data. That is both less mysterious and more powerful than either view suggests.
- **Judging a model on its training data.** Always test on held-out data it has never seen.
- **Using a large language model where a simple model would do.** For predicting a number from a table of features, a classic model is usually cheaper, faster, and easier to explain.
- **Ignoring the data.** Most ML failures in practice are data failures: too little, unrepresentative, mislabelled or leaked.

## Next steps

- [Neural networks in plain English](neural-networks-plain-english.md)
- [Classic ML: supervised vs unsupervised](classic-ml-supervised-vs-unsupervised.md) and [Training, validation and overfitting](training-validation-and-overfitting.md): the next level of detail, with runnable code
- [LLM basics](llm-basics.md) and [How LLMs are trained](how-llms-are-trained.md)
- [The Zero to Hero path](../start-here/zero-to-hero-path.md)
- [ML engineer path](../start-here/ml-engineer-path.md) if you want to train models yourself
- [docs/GLOSSARY.md](../../docs/GLOSSARY.md) for terms

## Sources

- Andrej Karpathy, "Software 2.0" (2017): https://karpathy.medium.com/software-2-0-a64152b37c35
- Goodfellow, Bengio and Courville, *Deep Learning* (MIT Press, 2016), chapter 5 "Machine Learning Basics": https://www.deeplearningbook.org/contents/ml.html
- scikit-learn, "Cross-validation: evaluating estimator performance" (train/test splits and overfitting): https://scikit-learn.org/stable/modules/cross_validation.html
- Ouyang et al., "Training language models to follow instructions with human feedback" (2022): https://arxiv.org/abs/2203.02155
- Kaplan et al., "Scaling Laws for Neural Language Models" (2020): https://arxiv.org/abs/2001.08361
