# Reinforcement Learning Basics

**In one line:** Learn what an agent, environment, reward and policy are, how reinforcement learning differs from supervised learning, and where it shows up in today's language models (RLHF and reasoning models).
**Last reviewed:** 2026-11-07

---

## The short version

- **Reinforcement learning (RL)** trains a decision-maker by trial and error. It acts, gets a **reward** (a number), and learns to collect more reward over time.
- There are no labelled right answers. There is only a score that arrives, often late, after many actions.
- The pieces: an **agent** (the learner), an **environment** (the world), **states** (what the agent sees), **actions** (what it can do), a **reward**, and a **policy** (its rule for choosing actions).
- The hard problems are **credit assignment** (which earlier action earned this reward?) and **exploration versus exploitation** (try something new, or repeat what works?).
- RL matters for LLMs. It is how models are tuned from human preferences (RLHF) and how reasoning models learn to think longer with checkable rewards.

## Supervised learning versus RL

In [supervised learning](classic-ml-supervised-vs-unsupervised.md), each example comes with the right answer. A teacher marks every question.

In RL there is no teacher marking each move. Think of learning to play a video game: nobody tells you the correct button press each frame, you only see the score and whether you survived. The agent's own actions change what data it sees next, which is why RL is harder to make stable.

## The loop

1. The agent observes the current **state**.
2. Its **policy** picks an **action**.
3. The environment responds with a new state and a **reward**.
4. The agent updates its policy to earn more total reward in future.

The goal is not the biggest immediate reward but the biggest **return**, the sum of rewards over time, usually with later rewards discounted slightly. A chess move that sacrifices a piece has negative short-term value and positive long-term value.

## A tiny example: the multi-armed bandit

Imagine three slot machines with unknown payout rates. Each pull is an action and the payout is the reward. Pulling the best-looking machine every time (exploit) may miss a better one you barely tried. Pulling random machines forever (explore) wastes money. A simple rule, **epsilon-greedy**, pulls the best-known machine most of the time and a random one with small probability epsilon, say 10%. This is the exploration problem in miniature, and it is the same trade-off a recommender faces when deciding whether to show a new item: see [Recommender systems basics](recommender-systems-basics.md).

## Main families of methods

| Family | Idea | Examples |
|---|---|---|
| Value-based | Learn how good each state or action is, then pick the best | Q-learning, DQN |
| Policy-based | Adjust the policy directly to make rewarding actions more likely | REINFORCE, PPO |
| Model-based | Learn a model of the world and plan inside it | Dyna, MuZero-style planners |

**Deep RL** uses a neural network to represent the value or policy. DeepMind's DQN (2015) learned to play many Atari games from raw pixels, which made deep RL famous. PPO (2017), a policy method designed to avoid destructive large updates, became a default for many practical systems.

## RL inside language models

- **RLHF.** Humans rank model answers; a reward model learns those preferences; the language model is then tuned with RL (PPO) to score higher. See [InstructGPT and RLHF](../../papers/language-models/05-instructgpt-rlhf/summary.md) and the overview in [How LLMs are trained](how-llms-are-trained.md).
- **Simpler alternatives.** Direct Preference Optimization reaches a similar goal without a separate RL loop: [DPO](../../papers/language-models/19-dpo/summary.md).
- **Reasoning with verifiable rewards.** For maths and code, the answer can be checked automatically, so the reward is cheap and honest. [DeepSeek-R1](../../papers/language-models/26-deepseek-r1/summary.md) used RL this way to elicit long chains of reasoning.
- **Agents.** Sutton and Silver argue the field should move toward learning from experience in the world: [The era of experience](../../papers/essays/116-era-of-experience/summary.md). Agentic loops in practice are covered in [Agentic loops](agentic-loops.md).

## Where RL fails

- **Reward hacking.** The agent finds a way to score without doing what you meant, such as a boat-racing agent circling to collect bonuses instead of finishing. Whatever you measure is what you get. The same risk applies to reward models for LLMs.
- **Sample hunger.** Games allow millions of free simulated tries. Real robots, factories or customers do not.
- **Instability.** Results vary a lot with random seeds and settings, so report several runs.
- **Simulator gap.** A policy that works in simulation can fail on real hardware.

If you have past data with labels, supervised learning is almost always simpler. Reach for RL when decisions chain together over time and you can safely simulate or measure the outcome.

## Common mistakes

- **Using RL when supervised learning would do.** If a labelled dataset exists, start there.
- **A reward that is easy to game.** Test what behaviour the reward actually encourages before long training runs.
- **Judging from one run.** Repeat with several seeds.
- **Confusing RLHF with training from scratch.** It is a late tuning stage after pretraining.

## Next steps

- [How LLMs are trained](how-llms-are-trained.md)
- [Neural networks in plain English](neural-networks-plain-english.md)
- [Guardrails and safety](guardrails-and-safety.md): why reward design is a safety issue
- [The Bitter Lesson](../../papers/essays/111-bitter-lesson/summary.md): why general methods that learn from experience scale

## Sources

- Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed. (2018), free online: http://incompleteideas.net/book/the-book-2nd.html
- Mnih et al., "Human-level control through deep reinforcement learning", *Nature* 518 (2015): https://www.nature.com/articles/nature14236
- Schulman et al., "Proximal Policy Optimization Algorithms" (2017): https://arxiv.org/abs/1707.06347
- Ouyang et al., "Training language models to follow instructions with human feedback" (2022): https://arxiv.org/abs/2203.02155
- Rafailov et al., "Direct Preference Optimization" (2023): https://arxiv.org/abs/2305.18290
- DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" (2025): https://arxiv.org/abs/2501.12948
- OpenAI Spinning Up, "Key Concepts in RL": https://spinningup.openai.com/en/latest/spinningup/rl_intro.html

## Check yourself

1. What does RL learn from, if there are no labelled right answers?
   <details><summary>Answer</summary>From a reward, a number that arrives after actions and often late. The agent learns by trial and error to collect more reward over time ("The short version").</details>
2. What is the difference between exploring and exploiting, and what does epsilon-greedy do?
   <details><summary>Answer</summary>Exploiting repeats what seems to work and exploring tries something new. Epsilon-greedy pulls the best-known machine most of the time and a random one with small probability epsilon, say 10% ("A tiny example: the multi-armed bandit").</details>
3. Why is the goal 'return' rather than the biggest immediate reward?
   <details><summary>Answer</summary>Return is the sum of rewards over time, so a move like a chess sacrifice with negative short-term value can have positive long-term value ("The loop").</details>
4. What is reward hacking, and what example does the page give?
   <details><summary>Answer</summary>The agent finds a way to score without doing what you meant, such as a boat-racing agent circling to collect bonuses instead of finishing. Whatever you measure is what you get ("Where RL fails").</details>
