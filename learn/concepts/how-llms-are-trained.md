# How LLMs Are Trained

**In one line:** Follow a language model from raw web text to finished assistant (pretraining, supervised fine-tuning, preference tuning with RLHF or DPO, and reinforcement learning on verifiable rewards), so you know what each stage adds, what it costs, and which behaviours you see in a chat window come from which step.
**Last reviewed:** 2026-10-21

---

> Assumes [LLM basics](llm-basics.md) and [Neural networks in plain English](neural-networks-plain-english.md). You will not train a frontier model, but knowing the pipeline explains why models behave the way they do and what fine-tuning can and cannot change.

## The short version

- A modern assistant is built in stages. **Pretraining** on trillions of tokens of text teaches language and knowledge, and costs almost all the compute. Everything after it is **post-training**, which is much cheaper and shapes behaviour.
- **Supervised fine-tuning (SFT)** shows the model examples of the conversations you want: an instruction and a good answer. It turns a text-completer into something that answers questions.
- **Preference tuning** teaches the model which of two answers people prefer. **RLHF** does it by training a reward model and then optimising against it with reinforcement learning; **DPO** gets a similar effect with one simple supervised-style loss and no separate reward model.
- **Reinforcement learning from verifiable rewards (RLVR)** gives the model problems whose answers a program can check (maths, code with tests) and rewards correct results. It is the main ingredient behind reasoning models since 2024 to 2025.
- Each stage has a characteristic failure: pretraining bakes in the data's errors and biases, SFT can teach confident style without substance, preference tuning invites flattery and verbosity, and RL invites **reward hacking**.

## The pipeline at a glance

```mermaid
flowchart LR
  D[Web text, books, code<br/>filtered and deduplicated] --> P[Pretraining<br/>predict the next token]
  P --> B[Base model<br/>completes text]
  B --> S[SFT<br/>imitate good answers]
  S --> PT[Preference tuning<br/>RLHF or DPO]
  PT --> RL[RLVR<br/>reward checkable correctness]
  RL --> A[Assistant / reasoning model]
  A --> SAFE[Safety training, evals,<br/>red teaming, release]
```

Labs vary the order and repeat stages (several rounds of SFT and RL are common), but these are the building blocks. The open [Tulu 3 summary](../../papers/language-models/148-tulu-3/summary.md) is the clearest public end-to-end recipe: SFT, then DPO, then RLVR, with every dataset released.

## Stage 1: Pretraining

**What happens.** The model starts as billions of random numbers. It is shown text one chunk at a time and asked, at every position, to predict the next [token](../../explainers/concepts/tokenization.md). The loss is how surprised it was by the real next token. Gradient descent nudges every weight to be a little less surprised next time, trillions of times over. Nobody labels anything: the text supplies its own answers, which is why this is called **self-supervised** learning.

**Why it works.** Predicting the next word of arbitrary text well requires knowing grammar, facts, how arguments go, how code compiles in a programmer's head, and what a character in a story would do next. The objective is simple; the skills needed to do well at it are not. The [GPT-2](../../papers/language-models/64-gpt2/summary.md) and [GPT-3](../../papers/language-models/04-gpt3-few-shot-learners/summary.md) summaries tell the story of discovering how far this goes.

**The data.** Scale matters, but quality and mix matter as much. A pretraining corpus is crawled web text, aggressively filtered (language detection, quality classifiers, removal of spam and boilerplate), deduplicated, and mixed with books, papers, code and maths. Meta reported pretraining Llama 3 on about 15 trillion tokens. [FineWeb](../../papers/techniques/133-fineweb/summary.md) documents how much the filtering choices alone move the final model's scores, and [Textbooks are all you need (phi-1)](../../papers/language-models/135-phi-1-textbooks/summary.md) shows small models punching above their weight on carefully chosen data.

**How big, for how long.** [Scaling laws](../../papers/techniques/12-scaling-laws/summary.md) showed loss falls predictably as parameters, data and compute grow; [Chinchilla](../../papers/techniques/18-chinchilla/summary.md) showed that for a fixed compute budget you should grow data and parameters together (roughly 20 tokens per parameter is compute-optimal). Modern small models are deliberately trained far past that point, because a smaller model that took longer to train is cheaper to serve forever after.

**The cost.** Pretraining is where the money goes: thousands of GPUs for weeks to months, coordinated with the parallelism tricks in the [ZeRO and Megatron summary](../../papers/techniques/76-zero-megatron/summary.md) and the [mixed precision summary](../../papers/techniques/143-mixed-precision-training/summary.md). The [cost of training explainer](../../explainers/compute/cost-of-training.md) works through the arithmetic.

**What you get.** A **base model**. Ask it "What is the capital of France?" and it may answer, or it may continue with three more quiz questions, because on the web a question is often followed by more questions. It knows a great deal and has no notion of being helpful.

## Stage 2: Supervised fine-tuning (SFT)

**What happens.** Collect tens of thousands to millions of example conversations: an instruction or a multi-turn chat, and the ideal assistant reply. Continue training on just these, with the same next-token loss, but only scoring the model on the reply tokens. The format (system prompt, user turn, assistant turn, special tokens between them) becomes the **chat template** the model expects for the rest of its life.

**Where the data comes from.** Human contractors writing ideal answers (expensive, high quality), existing datasets reformatted as instructions (the [FLAN summary](../../papers/techniques/80-flan/summary.md)), and increasingly synthetic data generated by stronger models and filtered (the [Self-Instruct summary](../../papers/techniques/79-self-instruct/summary.md)). Skill-specific mixes (maths, code, tool calls, refusals, multilingual) are tuned by trial: add data, retrain, check which evals moved.

**What it adds and what it cannot.** SFT teaches format, tone, following instructions and when to use tools. It surfaces knowledge the base model already has; it is a poor way to add new knowledge. Training a model to answer confidently on facts it never learned in pretraining teaches it to answer confidently, full stop, which is one route to [hallucination](hallucinations.md). This is the same reason [fine-tuning vs RAG](fine-tuning-vs-rag.md) usually comes down on the side of RAG for knowledge.

## Stage 3: Preference tuning (RLHF and DPO)

Writing the perfect answer is hard; judging which of two answers is better is much easier, for people and for models. Preference tuning exploits that.

**RLHF (reinforcement learning from human feedback)**, the recipe behind InstructGPT and the first ChatGPT:

1. Sample two or more answers from the SFT model for many prompts.
2. People rank them.
3. Train a **reward model**: a copy of the language model with a scoring head that predicts which answer people would prefer.
4. Run reinforcement learning (classically [PPO](../../papers/techniques/63-ppo/summary.md)) so the policy model produces answers the reward model scores highly, with a penalty (a **KL penalty**) for drifting too far from the SFT model, which keeps it from exploiting the reward model with gibberish that happens to score well.

The [InstructGPT summary](../../papers/language-models/05-instructgpt-rlhf/summary.md) has the headline result: labellers preferred outputs from a 1.3B-parameter RLHF model over the 175B GPT-3 base model. The lineage goes back through [learning to summarise from human feedback](../../papers/techniques/147-learning-to-summarize-from-human-feedback/summary.md) to [deep RL from human preferences](../../papers/techniques/146-deep-rl-from-human-preferences/summary.md).

**DPO (direct preference optimisation)** showed in 2023 that you can skip the reward model and the RL loop. Given pairs of (preferred, rejected) answers, a single loss pushes up the probability of the preferred one and down the rejected one, relative to a frozen reference copy. It is simpler, more stable and much cheaper, so it became the default for open models. See the [DPO summary](../../papers/language-models/19-dpo/summary.md) and its relative [KTO](../../papers/techniques/103-kto/summary.md), which works from simple thumbs-up and thumbs-down labels instead of pairs.

**AI feedback.** Human labels are slow and expensive, so labs increasingly use models to generate preference labels against a written set of principles, as in [Constitutional AI](../../papers/language-models/14-constitutional-ai/summary.md) (RLAIF).

**What it adds and the side effects.** Preference tuning is what makes models feel helpful, polite and well-organised. It also optimises for what raters like, and raters like confident, long, agreeable answers. **Sycophancy** (agreeing with the user's mistaken premise), verbosity and over-hedging are known side effects that labs then work to counter.

## Stage 4: Reinforcement learning from verifiable rewards (RLVR)

For some tasks you do not need anyone's opinion: the maths answer is right or wrong, the code passes its tests or not, the output matches the required format or not. **RLVR** gives the model such problems, lets it generate attempts (including long chains of reasoning), and rewards only the attempts that a program verifies. The term was named in the [Tulu 3](../../papers/language-models/148-tulu-3/summary.md) paper; [DeepSeek-R1](../../papers/language-models/26-deepseek-r1/summary.md) showed at scale what it can do.

The striking result from DeepSeek-R1-Zero: RL alone, starting from a base model with no SFT, raised AIME 2024 maths accuracy from 15.6% to 71.0% pass@1, and the model spontaneously learned to write longer reasoning, check its own work and backtrack. Nobody wrote examples of that behaviour; it was rewarded into existence. The RL algorithm used, [GRPO](../../papers/techniques/38-grpo/summary.md) (introduced earlier in DeepSeekMath), scores each attempt against the average of a group of attempts at the same problem, which removes the need for a separate value model and makes the RL step much cheaper than PPO. [DAPO](../../papers/techniques/155-dapo/summary.md) documents the engineering fixes needed to make it stable at scale.

This is the training behind **reasoning models**; the [reasoning models explainer](../../explainers/concepts/reasoning-models.md) and the [RLVR summary](../../papers/techniques/39-rlvr/summary.md) go further, including test-time compute (thinking longer at answer time).

**The failure mode: reward hacking.** RL optimises whatever you measure, literally. If the test suite only checks that a function returns without error, the model may learn to special-case the tests or delete the failing assertion. If the format checker only looks for a final boxed answer, it may learn to guess. Verifiers have to be robust, and labs monitor for models that game them.

## Safety training and evaluation

Running alongside the stages above: refusal and harm-avoidance data in SFT and preference sets, red-teaming (people and models trying to break it; see the [red teaming summary](../../papers/techniques/129-red-teaming-lms/summary.md)), safety classifiers, and pre-release evaluations for dangerous capabilities under each lab's published policy (the [frontier safety frameworks explainer](../../explainers/policy/frontier-safety-frameworks.md)). Research such as the [sleeper agents](../../papers/techniques/83-sleeper-agents/summary.md) and [emergent misalignment](../../papers/techniques/153-emergent-misalignment/summary.md) summaries shows why post-training is not a guarantee: behaviour trained in can be narrow, and narrow fine-tuning can have broad side effects.

## What this means for you

| What you notice in a chat window | Where it comes from |
|---|---|
| It knows a lot about the world, up to a date | Pretraining data and its cutoff |
| It answers in a helpful assistant voice | SFT |
| It is polite, structured, sometimes flattering or wordy | Preference tuning |
| It "thinks" before answering hard maths or code | RLVR and reasoning training |
| It refuses some requests | Safety data across SFT and preference tuning |
| It invents plausible facts | Pretraining objective plus training that rewards answering over abstaining (see the [Why LMs hallucinate summary](../../papers/techniques/149-why-language-models-hallucinate/summary.md)) |

And for your own projects: fine-tuning an open model (for example with [LoRA](../../build/projects/fine-tune-with-lora.md)) is SFT or DPO on a small scale. It is very good at style, format and narrow task behaviour, and poor at teaching new facts. If you need the model to know your documents, use [RAG](rag-explained.md).

## Common mistakes

- **Thinking a model "learns from your chats".** Inference does not change weights. Your conversation only matters if a provider later uses it as training data, which is a data-policy question, not a technical one.
- **Expecting fine-tuning to add knowledge.** It mostly changes behaviour.
- **Assuming RLHF makes a model truthful.** It makes a model preferred by raters, which correlates with truthfulness only partly.
- **Confusing base and instruct models** when downloading open weights. A base model will not follow your chat prompt well; use the `-Instruct` or `-chat` variant unless you plan to fine-tune.

## Next steps

- [Reasoning models explainer](../../explainers/concepts/reasoning-models.md) and [cost of training explainer](../../explainers/compute/cost-of-training.md)
- [Fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md): SFT yourself, on one GPU
- [Small language models](small-language-models.md): what training choices make a small model good
- [Synthetic data and model collapse](../../explainers/open-questions/synthetic-data-and-model-collapse.md)
- The [Researcher path](../start-here/researcher-path.md) for reading the papers in order

## Sources

- Ouyang et al., "Training language models to follow instructions with human feedback" (2022): https://arxiv.org/abs/2203.02155
- Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model" (2023): https://arxiv.org/abs/2305.18290
- Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (2022): https://arxiv.org/abs/2212.08073
- Lambert et al., "Tulu 3: Pushing Frontiers in Open Language Model Post-Training" (2024), which introduces the name RLVR: https://arxiv.org/abs/2411.15124
- DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2025): https://arxiv.org/abs/2501.12948
- Shao et al., "DeepSeekMath" (2024), which introduces GRPO: https://arxiv.org/abs/2402.03300
- Hoffmann et al., "Training Compute-Optimal Large Language Models" (2022): https://arxiv.org/abs/2203.15556
- Meta AI, "Introducing Meta Llama 3" (April 2024), 15T-token pretraining: https://ai.meta.com/blog/meta-llama-3/
