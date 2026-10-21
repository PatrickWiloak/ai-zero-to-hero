# The Researcher Path

**In one line:** A route for people who want to understand AI research itself - how to read papers, which papers to read in what order, how to reproduce results, and how to find open questions - built on this site's paper summaries and the reading roadmap.
**Last reviewed:** 2026-10-21

---

## The short version

- Research literacy is a skill you can learn without a PhD: **read a paper for its claim, its evidence, and its limits**, in that order.
- This site's paper summaries are the spine of the path. [docs/ROADMAP.md](../../docs/ROADMAP.md) gives paper-by-paper reading orders; this page tells you how to use them and what to do alongside them.
- Read in **threads**, not by date: follow one idea (attention, scaling, alignment, reasoning, retrieval, diffusion) from its origin to today. Each thread takes one to three weeks.
- Reproduce something. Re-running even a small result teaches you more about a paper than reading it five times.
- The frontier is mostly in the open questions: what models actually compute inside, why they generalise, how far scaling goes, and how to evaluate systems smarter than the test.

## Who this is for

Students considering research, engineers who want to read papers fluently, analysts who need to judge claims about AI, and anyone curious enough to want the primary sources. You should have done Phases 0 and 1 of the [Zero to Hero path](zero-to-hero-path.md). For the deeper threads, Stages 1 and 3 of the [ML engineer path](ml-engineer-path.md) (applied maths and deep learning) will help a lot.

## How to read a paper

Most people read papers front to back and stall in the method section. Read in passes instead.

**Pass 1 (10 minutes):** title, abstract, figures, the conclusion, and the headings. Write one sentence: "This paper claims that X, shown by Y." If you cannot write it, read the abstract again.

**Pass 2 (1 hour):** introduction, the method at the level of "what goes in, what comes out, what is trained", the main results table, and the limitations section. Ask: what is the baseline, what is the metric, and is the gain larger than the noise?

**Pass 3 (as needed):** the details, the appendix, the code. Do this only for papers you will build on or try to reproduce.

The summaries on this site are written as a structured Pass 2: each one says why the paper matters, explains the core idea in plain language, walks through the components, and lists limitations and what came next. A good way to work is to read the summary first, then the paper's abstract and main results table, then decide whether to go deeper. Every summary links to the original.

Questions to ask of any result:

- **Compared to what?** A big improvement over a weak baseline is a small result.
- **Measured how?** Benchmarks leak into training data and saturate. The [contamination and saturation explainer](../../explainers/benchmarks/contamination-and-saturation.md) shows how this happens.
- **At what cost?** A method that needs ten times the compute for a 2% gain may not matter.
- **Does it replicate?** Has anyone else reproduced it, or built on it successfully?

## The core threads

[docs/ROADMAP.md](../../docs/ROADMAP.md) has full paper-by-paper sequences (its "ML Student/Researcher" and "Reasoning and Agents" paths are the ones built for this page). [docs/READING_GUIDE.md](../../docs/READING_GUIDE.md) separates papers that matter historically from ones that matter for current practice. Here is the shape of each thread, with its entry points.

**1. Architectures.** From recurrent models to attention to the transformer, and the search for what comes after. Start at [seq2seq](../../papers/architectures/55-seq2seq/summary.md) and [Bahdanau attention](../../papers/architectures/66-bahdanau-attention/summary.md), then [Attention Is All You Need](../../papers/architectures/01-attention-is-all-you-need/summary.md), then the efficiency line ([FlashAttention](../../papers/techniques/16-flash-attention/summary.md), [GQA](../../papers/architectures/75-grouped-query-attention/summary.md), [multi-head latent attention](../../papers/architectures/141-multi-head-latent-attention/summary.md), [mixture of experts](../../papers/architectures/37-mixture-of-experts/summary.md)) and the alternatives ([Mamba](../../papers/architectures/20-mamba/summary.md), [Mamba-3](../../papers/architectures/156-mamba-3/summary.md)).

**2. Scaling and data.** Why bigger worked, and its limits. [Scaling laws](../../papers/techniques/12-scaling-laws/summary.md), [Chinchilla](../../papers/techniques/18-chinchilla/summary.md), [emergent abilities (and the critique)](../../papers/techniques/81-emergent-abilities/summary.md), [FineWeb](../../papers/techniques/133-fineweb/summary.md), [model collapse](../../papers/techniques/140-model-collapse/summary.md), with the essays [The Bitter Lesson](../../papers/essays/111-bitter-lesson/summary.md) and [The Scaling Hypothesis](../../papers/essays/112-scaling-hypothesis/summary.md). Then [scaling limits](../../explainers/open-questions/scaling-limits.md) and [synthetic data and model collapse](../../explainers/open-questions/synthetic-data-and-model-collapse.md).

**3. Alignment and post-training.** How a next-token predictor becomes a helpful assistant. [Deep RL from human preferences](../../papers/techniques/146-deep-rl-from-human-preferences/summary.md), [learning to summarize from human feedback](../../papers/techniques/147-learning-to-summarize-from-human-feedback/summary.md), [InstructGPT](../../papers/language-models/05-instructgpt-rlhf/summary.md), [Constitutional AI](../../papers/language-models/14-constitutional-ai/summary.md), [DPO](../../papers/language-models/19-dpo/summary.md), [weak-to-strong generalization](../../papers/techniques/128-weak-to-strong/summary.md).

**4. Reasoning.** From prompting tricks to trained reasoning. [Chain-of-thought](../../papers/techniques/09-chain-of-thought/summary.md), [self-consistency](../../papers/techniques/77-self-consistency/summary.md), [STaR](../../papers/techniques/97-star/summary.md), [process reward models](../../papers/techniques/51-process-reward-models/summary.md), [OpenAI o1](../../papers/language-models/31-openai-o1/summary.md), [DeepSeek-R1](../../papers/language-models/26-deepseek-r1/summary.md), [test-time compute](../../papers/techniques/50-test-time-compute/summary.md), [s1](../../papers/techniques/154-s1-simple-test-time-scaling/summary.md). Pair with [do LLMs reason?](../../explainers/open-questions/do-llms-reason.md).

**5. Agents.** [ReAct](../../papers/techniques/21-react/summary.md), [Toolformer](../../papers/techniques/24-toolformer/summary.md), [Voyager](../../papers/techniques/100-voyager/summary.md), [generative agents](../../papers/techniques/58-generative-agents/summary.md), [SWE-bench](../../papers/techniques/84-swe-bench/summary.md), [OSWorld](../../papers/techniques/139-osworld/summary.md), [METR time horizons](../../papers/techniques/145-metr-time-horizons/summary.md).

**6. Generative media.** [VAE](../../papers/image-generation/57-vae/summary.md), [GANs](../../papers/image-generation/02-generative-adversarial-networks/summary.md), [DDPM](../../papers/image-generation/06-diffusion-models/summary.md), [latent diffusion](../../papers/image-generation/07-stable-diffusion/summary.md), [flow matching](../../papers/image-generation/72-flow-matching-sd3/summary.md), [DiT and Sora](../../papers/image-generation/44-sora-dit/summary.md). [Diffusion models](../concepts/diffusion-models.md) is the plain-English entry.

**7. Interpretability and safety.** What is going on inside, and what could go wrong. [Induction heads](../../papers/techniques/126-induction-heads/summary.md), [sparse autoencoders](../../papers/techniques/82-sparse-autoencoders/summary.md), [circuit tracing](../../papers/techniques/151-circuit-tracing/summary.md), [reasoning models don't always say what they think](../../papers/techniques/152-reasoning-models-dont-say-what-they-think/summary.md), [sleeper agents](../../papers/techniques/83-sleeper-agents/summary.md), [emergent misalignment](../../papers/techniques/153-emergent-misalignment/summary.md), [adversarial attacks](../../papers/techniques/127-gcg-adversarial-attacks/summary.md), and [frontier safety frameworks](../../explainers/policy/frontier-safety-frameworks.md).

**8. Science and the wider field.** [AlphaFold](../../papers/techniques/68-alphafold/summary.md), [AlphaZero](../../papers/techniques/102-alphazero/summary.md), [AlphaEvolve](../../papers/techniques/62-alphaevolve/summary.md), robotics ([RT-2](../../papers/robotics/123-rt2/summary.md), [pi0](../../papers/robotics/124-pi0/summary.md)), and world models ([DreamerV3](../../papers/techniques/105-dreamerv3/summary.md), [Genie](../../papers/techniques/104-genie/summary.md)).

Browse everything by tag in [TAGS.md](../../TAGS.md) or by category in [INDEX.md](../../INDEX.md).

## Reproduce something

Reading tells you what a paper says. Reproducing tells you whether you understood it. Good first targets, roughly in increasing difficulty:

1. Train a tiny GPT on a small text corpus and plot loss against model size for three sizes. You have just seen a scaling curve.
2. Implement [LoRA](../../papers/techniques/10-lora/summary.md) by hand on a small model and compare it with full fine-tuning.
3. Re-run [self-consistency](../../papers/techniques/77-self-consistency/summary.md) on a small maths benchmark with an open-weight model: sample five answers, take the majority, and measure the gain over one answer.
4. Train a small diffusion model on a simple image dataset following [DDPM](../../papers/image-generation/06-diffusion-models/summary.md).
5. Measure the real usable context of a local model with a needle-in-a-haystack test, then compare with [RULER](../../papers/techniques/132-ruler/summary.md).

Keep a lab notebook: what you ran, the exact settings, the result, and what surprised you. Negative and partial results are still results.

## Find open questions

Every summary on this site ends with limitations and what came next; those sections are a ready-made list of open problems. The [open questions explainers](../../explainers/open-questions/do-llms-reason.md) cover the biggest debates ([do LLMs reason](../../explainers/open-questions/do-llms-reason.md), [scaling limits](../../explainers/open-questions/scaling-limits.md), [synthetic data](../../explainers/open-questions/synthetic-data-and-model-collapse.md)). [docs/GAPS.md](../../docs/GAPS.md) lists papers this collection has not yet covered, which is a good place to look for something to summarise yourself.

To stay current, follow arXiv's cs.CL, cs.LG and cs.AI listings, and read lab technical reports critically. A technical report from a company is not peer-reviewed and often omits the details that would let you check it; the [model family explainers](../../explainers/model-families/gpt.md) track how disclosure has changed.

## Common mistakes

- **Reading only the newest papers.** New papers assume the old ones. Follow a thread from its origin.
- **Taking the abstract at its word.** Abstracts sell. The results tables and limitations section tell you what was actually shown.
- **Treating benchmark gains as capability gains.** Check for contamination, saturation, and whether the comparison was fair.
- **Never writing code.** You understand a method when you can implement it, not when you can paraphrase it.
- **Working alone.** Reading groups, open-source projects and public write-ups get you feedback that solitary reading never does.

## Next steps

- [docs/ROADMAP.md](../../docs/ROADMAP.md): the paper-by-paper reading orders
- [docs/GLOSSARY.md](../../docs/GLOSSARY.md) for terms
- [Timeline of AI](../../explainers/history/timeline-of-ai.md) for the big picture
- [ML engineer path](ml-engineer-path.md) for the engineering skills research needs

## Sources

- S. Keshav, "How to Read a Paper" (the three-pass method), ACM SIGCOMM Computer Communication Review, 2007: https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf
- arXiv listings: https://arxiv.org/list/cs.CL/recent, https://arxiv.org/list/cs.LG/recent, https://arxiv.org/list/cs.AI/recent
