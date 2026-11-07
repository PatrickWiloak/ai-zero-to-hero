# AI for Product and Design Teams

**In one line:** Use AI to compress research synthesis, spec drafting, copy variants and prototyping, and keep the human work of choosing what to build, talking to users and judging quality.
**Last reviewed:** 2026-11-07

---

## The short version

- Best uses: synthesising interview notes, drafting PRDs and user stories from your notes, generating copy and layout variants, writing test cases and acceptance criteria, quick clickable prototypes.
- AI is fast at producing options and bad at knowing which option your users need. Spend the saved time with real users.
- Do not use AI "synthetic users" as a replacement for talking to customers. They tell you what is plausible, not what is true. This is a judgment, not a measured result.
- Check generated images, copy and code for licence, brand and accessibility problems before shipping.
- If you are building an AI feature (not just using AI), read [the AI product manager role](../../careers/roles/ai-product-manager.md) and [evals for LLMs](../../learn/concepts/evals-for-llms.md).

## Where it fits

| Task | AI helps with | You still own |
|---|---|---|
| Discovery | Clustering interview notes, drafting question lists | Who you talk to, what you conclude |
| Strategy | Stress-testing arguments, listing assumptions | The bet |
| Specs | PRD and story drafts, edge-case lists | Scope and trade-offs |
| Design | Layout and copy variants, image drafts, design critique prompts | Taste, usability, accessibility |
| Prototyping | Throwaway front ends and demos | Whether it solves the problem |
| QA | Test-case lists, bug-report cleanup | Release decision |

## Copyable prompts

**Interview synthesis** (paste anonymised notes)
```
Here are notes from [N] user interviews about [topic]: [notes].
List recurring problems with a count of how many interviews mention each,
verbatim quotes as evidence, and anything only one person said. Separate
what users did from what they said they would do.
```

**Pre-mortem for a spec**
```
Here is our draft spec: [paste]. Assume it shipped and failed. List the 10
most likely reasons, ordered by likelihood, and for each a cheap test we
could run before building.
```

**Copy variants with constraints**
```
Write 5 variants of this button and error message for [audience]. Max 4
words for the button. Plain, no exclamation marks. Keep the meaning of
every message exactly the same. Original: [text]
```

## Designing AI features

- Show users when they are talking to AI and what it can get wrong.
- Design the failure state first: what happens when the model is wrong or declines.
- Decide where a human can intervene. See [guardrails architecture](../../build/patterns/guardrails-architecture.md).

## Common mistakes

- Shipping generated copy or imagery unreviewed.
- Letting a model rank features by "impact" with no data.
- Using AI output as the research instead of as a first pass over it.

## Next steps

- [Prompt engineering](../../learn/concepts/prompt-engineering.md)
- [Image and video generation compared](../../tools/comparisons/image-and-video-generation.md)

## Sources

- No external sources: this is a judgment page based on common practice, not on measured studies.
