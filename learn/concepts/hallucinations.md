# Hallucinations

**In one line:** Language models sometimes state false things fluently and confidently; this page explains why that happens (it is a predictable result of how they are trained and graded, not a random glitch), which tasks are most at risk, and the concrete habits and system designs that reduce the damage.
**Last reviewed:** 2026-10-21

---

## The short version

- A **hallucination** is a model output that sounds plausible but is false or unsupported: an invented citation, a wrong date, a made-up function in a code library, a summary that adds something the source never said.
- It happens because a language model is trained to produce **likely text**, not to check facts. For facts it saw rarely or never, the likeliest-sounding answer is often wrong, and the model has no built-in signal that says "I am guessing".
- Training and evaluation make it worse: most benchmarks give credit for a right answer and nothing for "I don't know", so models learn that **guessing beats admitting uncertainty**.
- Risk is highest for **specific facts from memory**: names, numbers, dates, quotes, citations, URLs, niche topics, recent events, and anything after the model's training cutoff.
- Risk is lowest when the model **works from text you give it** and is asked to quote or cite it. Grounding, retrieval, citations, tool use, and checking are the main defences.
- Hallucination rates have fallen with newer models, but no model is free of them. Design every workflow assuming some answers will be wrong.

## What a hallucination looks like

The word covers several different failures:

- **Fabricated facts.** "The Eiffel Tower was completed in 1892." (It was 1889.)
- **Fabricated sources.** A citation to a paper, court case or book with a realistic title, plausible authors, and no existence. In 2023 a US court sanctioned lawyers who filed a brief citing cases that an AI assistant had invented.
- **Unfaithful summaries.** A summary of a contract that confidently mentions a termination fee the contract does not contain.
- **Invented code.** A call to a function or package that does not exist, written in perfectly idiomatic style. Researchers have shown that models invent package names often and repeatably, which means an attacker could publish a malicious package under a commonly invented name, so blindly installing a suggested package is a security risk; see [Model supply chain](../../safety/security/model-supply-chain.md).
- **Wrong reasoning, confident conclusion.** A maths or logic answer where one step is wrong and the rest follows smoothly from the error.

What these share is that the output is **fluent and assured**. A model's tone does not change when it is wrong, which is exactly what makes hallucinations dangerous.

## Why models hallucinate

Start with what a language model is: a system trained to predict the next token of text, given everything before it ([LLM basics](llm-basics.md)). During pretraining it sees trillions of tokens and becomes extremely good at producing text that looks like the text it was trained on. That is a different goal from producing text that is true. Most of the time the two coincide, because most of what it read was roughly accurate. Hallucinations live in the gap.

A 2025 paper from OpenAI and Georgia Tech, [Why Language Models Hallucinate](../../papers/techniques/149-why-language-models-hallucinate/summary.md), makes this precise with two arguments.

**1. Some errors are unavoidable from pretraining alone.** For facts with no learnable pattern, such as a particular person's birthday, there is nothing to generalise from; the model can only memorise what it saw. The paper links the minimum error rate to how many facts appear only **once** in the training data. If a fact was seen once, the model's knowledge of it is shaky, and when asked it will often produce something birthday-shaped rather than the actual date. Well-known facts (repeated thousands of times) are reliable; obscure ones are not.

**2. Training and grading reward bluffing.** After pretraining, models are tuned and judged on benchmarks that mark answers right or wrong, with no credit for abstaining. Under that scoring, a model that guesses always scores at least as well as one that says "I don't know", exactly like a student on a multiple-choice exam with no penalty for wrong answers. So the models we build learn to guess confidently. The authors' proposed fix is not a new training method but changing how evaluations are scored, so honest uncertainty is rewarded.

A few other causes stack on top:

- **The training cutoff.** A model knows nothing that happened after its training data was collected, but it does not reliably know what it does not know, so it may answer questions about recent events from stale or invented information.
- **Tokenization.** The model sees chunks of text, not letters or digits, which makes some tasks (counting letters, some arithmetic) harder than they look; see [Tokenization](../../explainers/concepts/tokenization.md).
- **Pressure from the prompt.** A question that assumes a false premise ("Why did Einstein win the Nobel Prize for relativity?") invites the model to go along with it. Models also tend to agree with the user's framing, a tendency called **sycophancy**.
- **Sampling.** Models choose each token with some randomness ([Sampling and decoding](../../explainers/concepts/sampling-and-decoding.md)). Lower temperature makes outputs more repeatable but does not make the model know things it does not know.
- **Long contexts.** Models use information in the middle of very long inputs less reliably than at the start and end, so a fact buried on page 40 can be missed and filled in with something plausible ([RULER summary](../../papers/techniques/132-ruler/summary.md), [Context windows](../../explainers/concepts/context-windows.md)).

## Which tasks are risky

A useful mental test: **is the model transforming information you gave it, or recalling information from memory?**

| Lower risk | Higher risk |
|---|---|
| Summarising a document you pasted in | "Summarise the latest research on X" with no sources given |
| Extracting fields from an invoice | "What is this company's revenue?" |
| Rewriting or translating your text | Quotes, statistics, citations, URLs |
| Explaining widely known concepts | Niche topics, small companies, obscure people |
| Answering from retrieved documents with citations | Anything after the training cutoff |
| Code using a popular, stable library | Code using a niche or recently changed API |

Even on the lower-risk side, mistakes happen: summaries can still add or distort details. But the failure rate is much lower, and checking is much easier because the source is right there.

## How to reduce hallucinations as a user

1. **Give it the source.** Paste the document, data or page and say "answer only from the text below". This turns a recall task into a reading task.
2. **Ask for evidence.** "Quote the sentence that supports each point" or "give the clause number". Then spot-check the quotes. A model asked to quote is much less likely to invent, and invented quotes are easy to catch.
3. **Give it permission not to know.** "If the answer is not in the document, say so" measurably helps, because you are removing the pressure to guess.
4. **Use search-enabled modes** for factual questions, and click the sources. A citation is only useful if it actually supports the claim.
5. **Use reasoning modes for hard problems.** Models that work through a problem step by step before answering make fewer reasoning errors on maths and logic ([Reasoning models](../../explainers/concepts/reasoning-models.md)), though they can still hallucinate facts, and their written reasoning is not always a faithful account of how they reached the answer ([reasoning models don't always say what they think](../../papers/techniques/152-reasoning-models-dont-say-what-they-think/summary.md)).
6. **Cross-check what matters.** For a fact you will act on, verify it in a primary source, or at least ask a second model and treat disagreement as a warning.

## How to reduce hallucinations as a builder

If you are building an AI application, you can design hallucinations down much further than a user can prompt them down.

- **Ground with retrieval.** Retrieve relevant documents and put them in the prompt, so answers come from your sources rather than the model's memory. This is [retrieval-augmented generation](rag-explained.md), and the original [RAG paper](../../papers/techniques/13-rag/summary.md) introduced it partly for this reason. Retrieval quality is the bottleneck: if the right passage is not retrieved, the model may fill the gap.
- **Require citations and check them in code.** Ask for the source passage ID with each claim, then verify that the cited passage exists and contains the quoted text. Some APIs offer citation features that return exact source spans.
- **Use tools for facts and arithmetic.** Let the model call a database, a search API or a calculator instead of answering from memory ([Tool use and function calling](tool-use-and-function-calling.md)). The [Toolformer summary](../../papers/techniques/24-toolformer/summary.md) shows why this works.
- **Constrain the output.** [Structured outputs](structured-outputs.md) with enums and schemas stop the model from inventing categories or fields.
- **Let it abstain.** Make "not found" or "needs human review" a valid, rewarded output in your prompt and your evaluation, and route those cases to a person.
- **Check with a second pass.** A verification step (another model call or rules) that checks each claim against the sources catches many errors. [Self-consistency](../../papers/techniques/77-self-consistency/summary.md), sampling several answers and checking whether they agree, is a cheap uncertainty signal for some tasks.
- **Measure it.** Build an evaluation set that includes questions whose answer is not in your documents, and track how often the system invents an answer versus correctly declines. See [Evals for LLMs](evals-for-llms.md) and [Guardrails and safety](guardrails-and-safety.md).
- **Keep a human where it counts.** For legal, medical, financial or customer-facing outputs, design review into the workflow.

## Will it be solved?

Newer models hallucinate less than earlier ones on standard tests, partly through better training, partly through reasoning, and partly because providers now train models to abstain more often. But the paper above argues that some error rate is mathematically unavoidable for facts that appear rarely in training data, and that the incentives in evaluation still favour guessing. Expect hallucinations to keep falling and never reach zero. The durable fix is system design: ground, cite, check, and let the model say "I don't know".

For the wider debate about whether language models "understand" anything at all, see [On the Dangers of Stochastic Parrots](../../papers/essays/150-stochastic-parrots/summary.md) and [Do LLMs reason?](../../explainers/open-questions/do-llms-reason.md).

## Common mistakes

- **Trusting tone.** Confidence in the wording is not evidence of accuracy.
- **Treating citations as proof.** Check that the source exists and says what the model claims.
- **Thinking temperature 0 fixes it.** It makes outputs repeatable, not true.
- **Assuming RAG solves it.** Retrieval helps a lot, but bad retrieval, or a model that ignores the retrieved text, still produces hallucinations. Measure it.
- **Never letting the model say "I don't know".** If your prompt or your evaluation punishes abstaining, you are training the system to bluff.

## Next steps

- [RAG explained](rag-explained.md)
- [Evals for LLMs](evals-for-llms.md)
- [AI for everyone](../start-here/ai-for-everyone.md): the everyday habits
- [Why Language Models Hallucinate (summary)](../../papers/techniques/149-why-language-models-hallucinate/summary.md)

## Sources

- Kalai, Nachum, Vempala and Zhang, "Why Language Models Hallucinate" (September 2025): https://arxiv.org/abs/2509.04664
- Ji et al., "Survey of Hallucination in Natural Language Generation", *ACM Computing Surveys* (2023): https://arxiv.org/abs/2202.03629
- Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023): https://arxiv.org/abs/2307.03172
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020): https://arxiv.org/abs/2005.11401
- Mata v. Avianca, Inc., No. 22-cv-1461 (S.D.N.Y. 2023), sanctions over fabricated case citations: https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
- Spracklen et al., "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs" (2024): https://arxiv.org/abs/2406.10279
- Anthropic, "Reduce hallucinations" (prompting guidance, including allowing the model to say it does not know): https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
