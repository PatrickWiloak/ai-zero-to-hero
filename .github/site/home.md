<!--
  Site-only landing page. Written over the staged copy of README.md by
  scripts/build_manifest.py - MkDocs maps README.md to the site root exactly
  as it does index.md. The repo's own README.md is never touched and stays
  the GitHub front page.

  The two pages have different jobs. README.md is a repo front page: badges,
  repository structure, contributing, "star this repo". This is a website
  landing page: what the site is, who it is for, and the handful of links a
  first-time visitor actually needs.

  Never hard-code a count here. Every number is a double-braced token filled by
  render_home() in scripts/build_manifest.py from the same parsed papers list
  that builds papers.json and INDEX.md, so a number on this page cannot drift
  away from the tree. Adding a new number means adding a token, not typing a
  figure.

  No `hide: toc` here. With toc.integrate the page's headings fold into the left
  sidebar, and hiding them would make Home the one page whose sections do not
  appear where every other page's do.
-->
<!-- markdownlint-disable MD030 -->
<!-- Material's card grids use `-   ` (three spaces) so the card body lines up at
     a four-space indent and stays part of the list item. MD030 wants one. -->


<div class="home-hero" markdown>

# AI, from zero to hero { .home-title }

<p class="home-intro">Everything AI in one place, free. Start from nothing and learn what a model is, use AI well in your job, roll it out to a team, build real systems, pick the right tools, secure and govern them, and get hired - {{guides_total}} guides in all. Then go as deep as you like: {{papers}} research papers rewritten in plain language and {{explainers}} explainers on the models, the benchmarks, the money and the rules.</p>

<p class="home-sub">No maths degree assumed, no paywall, no signup. Press <kbd>/</kbd> to search all {{words}} words.</p>

[Start from zero](learn/start-here/zero-to-hero-path.md){ .md-button .md-button--primary }
[AI for your job](work/README.md){ .md-button }
[Build something](build/README.md){ .md-button }
[Read the research](INDEX.md){ .md-button }

<div class="stat-strip" markdown>

- **{{guides_total}}** guides
- **{{papers}}** papers
- **{{explainers}}** explainers
- **{{source_words}}** words of research read
- **{{compression}}x** shorter
- **$0** to read

</div>

<p class="stat-note">Research figure measured, not estimated: every word <code>pdftotext</code> extracts from {{measured_papers}} of the {{papers}} papers. The other {{unmeasured}} sit behind journal paywalls or are published as web pages with no PDF, so they are excluded - the real total is higher. <a href="https://github.com/PatrickWiloak/genai-research-papers-summarized/blob/main/scripts/measure_sources.py">See the script</a>.</p>

</div>

<p class="home-kicker">Pick your way in</p>

## Where are you starting?

<div class="grid cards" markdown>

-   :material-school-outline:{ .lg .middle } **Learn - from absolute zero**

    ---

    Paths by audience (everyone, leaders, engineers, researchers), the day-one basics - your first API call, running a model on your laptop - and the core ideas in plain English. {{pillar_learn}} pages.

    [:octicons-arrow-right-24: Start here](learn/README.md)

-   :material-briefcase-outline:{ .lg .middle } **AI at Work - use it, then roll it out**

    ---

    Playbooks by role, real use cases, and the team-enablement kit: adoption plan, acceptable-use policy, training, measuring ROI. {{pillar_work}} pages.

    [:octicons-arrow-right-24: AI at work](work/README.md)

-   :material-hammer-wrench:{ .lg .middle } **Build - hands-on projects**

    ---

    Chatbots, RAG, agents with MCP, evals, fine-tuning, voice - step by step with runnable code, plus the architecture patterns behind production systems. {{pillar_build}} pages.

    [:octicons-arrow-right-24: Build](build/README.md)

-   :material-scale-balance:{ .lg .middle } **Tools - what to pick**

    ---

    Chat assistants, coding assistants, agent frameworks, vector stores, serving stacks, and which model for which job. Comparisons with dates on them. {{pillar_tools}} pages.

    [:octicons-arrow-right-24: Tools](tools/README.md)

-   :material-shield-lock-outline:{ .lg .middle } **Safety & Governance**

    ---

    Prompt injection, the OWASP LLM Top 10, agent security, red teaming - and the governance side: NIST AI RMF, ISO 42001, the EU AI Act, risk assessment. {{pillar_safety}} pages.

    [:octicons-arrow-right-24: Safety & governance](safety/README.md)

-   :material-account-tie-outline:{ .lg .middle } **Careers**

    ---

    The AI roles and how to get there, interview prep with real questions, and which certifications are worth it. {{pillar_careers}} pages.

    [:octicons-arrow-right-24: Careers](careers/README.md)

</div>

<p class="home-kicker">Go deeper</p>

## The research library

Every major paper from the Transformer to today's reasoning models, read in full and rewritten to be finished: {{source_words}} words of research in, {{summary_words}} words out. Plus {{explainers}} dated explainers on everything a single paper does not cover.

<div class="grid cards" markdown>

-   :material-timeline-clock-outline:{ .lg .middle } **Start with the story**

    ---

    Seventy-five years of AI in one page, every milestone linked to its summary.

    [:octicons-arrow-right-24: Timeline of AI](explainers/history/timeline-of-ai.md)

-   :material-compass-outline:{ .lg .middle } **Understand the landscape**

    ---

    Model families, benchmarks, compute and cost, policy, open questions.

    [:octicons-arrow-right-24: All explainers](EXPLAINERS.md)

-   :material-map-marker-path:{ .lg .middle } **Read in order**

    ---

    A staged reading order from Word2Vec to reasoning models.

    [:octicons-arrow-right-24: Research roadmap](docs/ROADMAP.md)

</div>

<p class="home-kicker">The library</p>

## Papers by category

<div class="cat-grid" markdown>

{{category_chips}}

</div>

[Full index with titles, authors, and years](INDEX.md){ .md-button }

<p class="home-kicker">Start with the classics</p>

## Twelve papers worth reading first

<div class="home-links" markdown>

- [Attention Is All You Need](papers/architectures/01-attention-is-all-you-need/summary.md) - the Transformer
- [GPT-3](papers/language-models/04-gpt3-few-shot-learners/summary.md) - few-shot learning at scale
- [InstructGPT](papers/language-models/05-instructgpt-rlhf/summary.md) - how a base model becomes an assistant
- [DPO](papers/language-models/19-dpo/summary.md) - alignment without the RL loop
- [DeepSeek-R1](papers/language-models/26-deepseek-r1/summary.md) - reasoning models, method published
- [Chain-of-Thought Prompting](papers/techniques/09-chain-of-thought/summary.md) - thinking out loud
- [LoRA](papers/techniques/10-lora/summary.md) - cheap fine-tuning
- [RAG](papers/techniques/13-rag/summary.md) - retrieval-augmented generation
- [FlashAttention](papers/techniques/16-flash-attention/summary.md) - fast exact attention
- [Scaling Laws](papers/techniques/12-scaling-laws/summary.md) - why bigger worked
- [Stable Diffusion](papers/image-generation/07-stable-diffusion/summary.md) - latent diffusion
- [Model Context Protocol](papers/techniques/59-model-context-protocol/summary.md) - connecting tools to models

</div>

<p class="home-kicker">New</p>

## Recently added

<div class="home-links" markdown>

{{recent_papers}}

</div>

<p class="home-kicker">Quick links</p>

## Jump to what you need

<div class="home-links" markdown>

- [Explainers](EXPLAINERS.md) - model families, benchmarks, compute, policy, open questions
- [Timeline of AI](explainers/history/timeline-of-ai.md) - 1950 to today, milestone by milestone
- [Learning Roadmap](docs/ROADMAP.md) - the staged order to read them in
- [Reading Guide](docs/READING_GUIDE.md) - what is still current, what is history
- [Quick Reference](docs/QUICK_REFERENCE.md) - every paper in one line
- [Comparisons](docs/COMPARISONS.md) - decision guides for real build choices
- [Glossary](docs/GLOSSARY.md) - the vocabulary, defined once
- [Coverage & Gaps](docs/GAPS.md) - what is not here yet, and why
- [Browse visually](BROWSE.md) - grid view with a three-line pitch each
- [By topic tag](TAGS.md) - {{topics}} tags across the collection
- [papers.json](papers.json) - the whole collection as machine-readable data
- [Contributing](CONTRIBUTING.md) - how to add a paper, and the house style

</div>

## What each summary gives you

Every paper here was read in full, then rewritten to a fixed shape so you can move between them without relearning the format each time:

- **Why this matters** - the one thing that changed, stated before any notation.
- **The problem** - what people were stuck on, and why the obvious fix did not work.
- **The core innovation** - the actual idea, with diagrams instead of proofs.
- **Key results** - the numbers the paper reported, not the numbers people remember.
- **Real-world impact** - what shipped because of it.
- **Limitations** - what it does not do, including where the field has since moved past it.
- **Related in this collection** - generated cross-links, so following a thread never dead-ends.

Summaries are not a substitute for the paper. Every one links to the original, and the good ones are worth your time once the summary has told you what to look for.

## Who made this

Built by **[Patrick Wiloak](https://patricklukewilson.com)** - ex-AWS Solutions Architect, 10 years in tech, multi-cloud certified.
[YouTube](https://youtube.com/@patrickwiloak) · [LinkedIn](https://www.linkedin.com/in/patricklukewilson/) · [Source on GitHub](https://github.com/PatrickWiloak/genai-research-papers-summarized)

Learning the cloud, data, and security side too? **[Cloud, Data, AI and Security - Zero to Hero](https://patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero/)** is the sibling site: concepts, hands-on builds, and the most comprehensive certification library on GitHub.

We build custom software and products at **[Nobler Works](https://noblerworks.com/)**. Open-source training like this is how we give back - we are nothing without the community that supports us. If you need software built, [get in touch](https://noblerworks.com/).

!!! tip "Want the reps as well as the reading?"

    [![gitGood.dev - practice questions, coding challenges, system design and cloud certification practice exams for engineers, data, security, DevOps and product technologists](assets/brand/gitgood-banner.png){ width="300" }](https://gitgood.dev)

    This site gives you the material. **[gitGood](https://gitgood.dev)** gives you the reps, and tells you whether you actually know it - including ML and AI practice paths built for exactly the material on this site.

    A 7-day free trial, then $8/month or $64/year. The free tier needs no card.

## Fine print

Summaries are original work, released under [CC BY 4.0](LICENSE) - free to use with attribution. The papers themselves belong to their authors and are linked, never reproduced.

This is an independent educational resource. It is not affiliated with, endorsed by, or sponsored by OpenAI, Google, Anthropic, Meta, or any other organisation whose work is summarised here. All trademarks belong to their respective owners.

Found something wrong or out of date? [Contributions welcome](CONTRIBUTING.md).
