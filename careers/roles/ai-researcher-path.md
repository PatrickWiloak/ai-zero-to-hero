# AI Researcher Path

**In one line:** How people become AI researchers, the difference between research scientist, research engineer and applied roles, and a realistic way to build a research record.
**Last reviewed:** 2026-11-07

---

## The short version

- **Research scientist** roles set questions and write papers. **Research engineer** roles build the systems and experiments that make research run. Many labs value both. This split is a judgment from common practice, not a sourced taxonomy.
- The usual signal is a track record: papers, reproduced results, open-source contributions or a thesis. Credentials help but a good public record can stand in.
- A strong path for a self-learner: read papers well, reproduce one, then extend it with a small, honest experiment.
- No salary, admission or hiring numbers are given because none were sourced.

## Step 1: get the base

- [Maths for ML without fear](../../learn/day-one/maths-for-ml-without-fear.md), [neural networks in plain English](../../learn/concepts/neural-networks-plain-english.md), [transformer architecture](../../learn/concepts/transformer-architecture.md).
- The [researcher path](../../learn/start-here/researcher-path.md) gives the learning order.

## Step 2: learn to read papers

- Start with the summaries in this collection, then read the originals. [Attention Is All You Need](../../papers/architectures/01-attention-is-all-you-need/summary.md) and [InstructGPT / RLHF](../../papers/language-models/05-instructgpt-rlhf/summary.md) are good first pairs.
- For each paper, write: the claim, the evidence, what was not tested.
- Use the [ROADMAP](../../docs/ROADMAP.md) and [READING_GUIDE](../../docs/READING_GUIDE.md).

## Step 3: reproduce something small

- Pick a result you can run on one GPU: [run Llama on a single GPU](../../build/projects/run-llama-on-single-gpu.md), [fine-tune with LoRA](../../build/projects/fine-tune-with-lora.md).
- Report what matched, what did not, and your seeds. Negative or partial reproductions are useful.

## Step 4: contribute

- Add an eval, a bug fix or a documented replication to an open-source project. Use [set up an eval harness](../../build/projects/set-up-eval-harness.md) as a starting point.
- Write a short technical note or blog post. Clarity is a research skill.

## Step 5: choose a route

| Route | Fit |
|---|---|
| PhD | Best when you want to set your own questions and are happy with a multi-year commitment. |
| Research engineer | Best when you like building systems; start from the [ML engineer roadmap](ml-engineer-roadmap.md). |
| Applied research in industry | Best when you want measurable product impact; see the [AI engineer roadmap](ai-engineer-roadmap.md). |

## Common mistakes

- Reading only summaries. Read the paper, then check the code.
- Claiming improvement from one seed or a tiny test set.
- Skipping safety and evaluation work; both are active research areas. See [safety](../../safety/README.md).

## Next steps

- [Build an AI portfolio](build-an-ai-portfolio.md) for how to present research-style work.
- [AI careers map](ai-careers-map.md).

## Sources

- Judgment: the route comparison is editorial.
- Paper details are in the linked summaries, each of which cites the original.
