# AI Copyright, Training Data and Model Licenses: What a Builder Needs to Know

**In one line:** Sort any AI copyright question into one of four buckets (how the model was trained, what it outputs, what you feed it, what licence you accepted) and know which one is yours to manage.
**Last reviewed:** 2026-11-15

---

> This page is general information for builders. It is not legal advice. Copyright law differs by country and several key cases are still moving, so check the current status with a lawyer before you rely on any point here.

## The short version

- "Is AI legal to use?" is four questions, not one. Training, outputs, inputs and licences each have a different owner and a different risk.
- **Training** (did the model maker copy works to build the model?) is mostly the model maker's legal problem. It becomes yours only if you train or fine-tune a model yourself.
- **Outputs** are where most builders are exposed: your output may copy something, and your output may not be protected by copyright at all.
- **Inputs** (what you paste in, what you index for RAG, what you fine-tune on) are fully yours. This is the bucket you control best.
- **Licences** (the model licence, the API terms, the data licence) are contracts. Read them. They bind you even when copyright law is unsettled.
- Keep a record of what data went where. It is the cheapest protection you have.

## The four buckets

| Bucket | The question | Who carries the main risk | What you can do |
|--------|--------------|---------------------------|-----------------|
| 1. Training data | Was copyrighted work copied to train the model, and was that allowed? | The model maker | Pick vendors who document their data and offer indemnities. If you train yourself, you carry it |
| 2. Outputs | Can the output infringe? Can you own it? | You, mostly | Review outputs, avoid prompts that ask for a named work or style, keep human authorship |
| 3. Inputs | Do you have the right to use this data in a prompt, an index or a fine-tune? | You | Track the source and licence of every dataset |
| 4. Licences | What does the contract let you do with the model and its outputs? | You | Read it, record it, check it again on upgrade |

Most confusion online comes from mixing these. A court ruling about training (bucket 1) says little about whether your chatbot's answer is safe to publish (bucket 2).

## Bucket 1: training data

Model makers train on very large collections of text, images and code, much of it under copyright. Whether that is lawful is being decided in courts and legislatures right now. Three things are worth knowing as a builder.

**The law is not settled and differs by place.**

- In the United States the question is mostly fair use. In 2025 two federal district courts in California ruled on it in book-training cases (Bartz v. Anthropic and Kadrey v. Meta). Both rulings went in the defendants' favour on the records before them, but they used different reasoning, and one judge stressed that other plaintiffs with better evidence of harm to their market could win. Another district court (Thomson Reuters v. Ross, Delaware) found that training a non-generative legal search tool was not fair use. Appeals and further cases were pending when this page was written.
- Separately, the Bartz case showed that *how* the data was obtained matters: the court treated copies from pirate libraries differently from books the company bought, and the case ended in a large settlement. If you assemble training data yourself, where it came from is a legal fact, not a detail.
- In the European Union the Copyright in the Digital Single Market Directive (2019/790), Article 4, allows text and data mining unless the rights holder has reserved their rights in a machine-readable way. The AI Act then asks general-purpose model providers to have a copyright policy that respects those reservations (Article 53(1)(c)) and to publish a summary of training content (Article 53(1)(d)). See [EU AI Act compliance](./eu-ai-act-compliance.md).
- In the United Kingdom, a High Court decision in Getty Images v. Stability AI (2025) rejected the claim that the trained model itself was an infringing copy. It was a narrow ruling on that claim and is not a general licence to train on anything.

**Why it matters to you even if you never train a model.** Disputes can lead to a model being withdrawn, retrained or restricted, and to vendor terms changing. That is a supply risk, the same kind you manage for any dependency. Ask vendors three things: do they publish what they trained on (a summary is a start), do they offer an IP indemnity for outputs, and what are the conditions on that indemnity.

**If you train or fine-tune.** Then you are the model maker for that step. Keep a data register (source, licence, date, who approved). Prefer data you own, data you have licensed, or data under a licence that allows this use. "It was public on the web" is not a licence. For personal data in the same sets, see [privacy and data protection with AI](./privacy-and-data-protection-with-ai.md).

## Bucket 2: outputs

Two separate problems live here, and they point in opposite directions.

**Problem A: can your output infringe someone else's work?** Models can sometimes reproduce text, code or images from their training data, especially when the prompt names a specific work or when a passage appears many times in the data. An image model asked for a famous character will often draw it. You publish the output, so you are the one who publishes the copy.

Practical rules:

1. Do not prompt for a named, protected work, character or living artist's style in anything you ship.
2. For code, run licence and similarity scanning on generated code before it merges, the same way you would for any third-party code. Many coding assistants have a setting that filters suggestions matching public code.
3. For images, see [diffusion models](../../learn/concepts/diffusion-models.md) for how they learn, and treat brand logos, characters and celebrity likenesses as off limits unless you hold the rights.
4. A human review step before publication catches most of the obvious cases.

**Problem B: can you own the output?** In the United States, the Copyright Office has said in its report on copyrightability (January 2025, at copyright.gov/ai) that copyright protects human authorship. Prompts alone, in its view, do not give enough control over the output to make the user the author, though human-made selection, arrangement and edits can be protected. A federal appeals court in Thaler v. Perlmutter (D.C. Circuit, 2025) confirmed that a work with no human author cannot be registered. Other countries take different positions.

What this means in practice: text or images that are purely machine generated may have thin or no copyright protection, so a competitor may be free to copy them. If an asset matters to your business (a logo, a game character, a core document), make a human the real author of it and keep drafts that show their contribution.

## Bucket 3: inputs

This is the bucket where you have the most control, so it is where to spend your effort.

| Input | Typical mistake | Safer habit |
|-------|-----------------|-------------|
| Prompts | Pasting a client's confidential or licensed document into a consumer chat tool | Use an approved tool with terms that say your data is not used to train the model |
| RAG index | Indexing a paid report library whose licence forbids copying or machine use | Check licence terms before ingest, store the source and licence as metadata |
| Fine-tuning set | Scraping a site whose terms forbid it | Record the source, use licensed or owned data, remove opt-outs |
| Evaluation sets | Copying customer data into a test file kept forever | Apply the same retention rules as production data |

For RAG in particular, a retrieved passage shown to a user or quoted in an answer is a copy. Quoting short snippets with a link to the source is a different risk from reproducing whole articles. See [RAG explained](../../learn/concepts/rag-explained.md) for how retrieval works.

A worked example: a team builds a support bot over its own help centre, a vendor's product manual that it resells under a distribution licence, and a folder of scraped competitor pages. The help centre is theirs. The vendor manual needs a licence check: "distribute" may not mean "feed to a model and quote". The competitor pages are the real exposure: drop them, or get permission. One short data register with three rows would have caught this before launch.

## Bucket 4: licences

Copyright law is slow and unsettled. Contracts are not. The terms you accepted apply today.

**Three documents to read:**

1. **The model licence** (for open-weight models). Some are standard permissive licences (Apache 2.0, MIT). Others are custom: they may cap use for very large companies, require you to display a credit, force derived model names, attach an acceptable use policy, or limit what you may do with outputs (for example training another model). For a side-by-side table with dated sources, use the licences section of [open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md) and re-read the licence file on the model's own page, because it can differ per version.
2. **The API or service terms** (for hosted models). Look for who owns outputs, whether your inputs are used for training (and whether this differs by plan), data retention, and any IP indemnity and its conditions.
3. **The data licence** for every dataset you use. Common ones: CC0 and CC BY (permissive), CC BY-SA (share-alike), CC BY-NC (no commercial use), and custom terms that forbid machine learning use.

**Licence traps worth checking:**

- Non-commercial licences on datasets and some model weights: fine for research, a breach in a product.
- Derivatives inherit. A model fine-tuned from a restricted base usually keeps the base's terms.
- "Open" is not "open source". A model with downloadable weights may be under a custom licence that the Open Source Initiative would not call open source.
- Terms change by version. A licence on version 1 does not guarantee the same on version 2.
- Acceptable use policies are part of the contract, and some must be passed on to your own users.

For the security side of choosing and verifying a model file, see [model supply chain security](../security/model-supply-chain.md).

## A short decision checklist

Before you ship an AI feature, answer these in writing:

1. Which model, which version, under which licence or terms? (Link the exact text and note the date you read it.)
2. Does the vendor offer an IP indemnity, and do we meet its conditions?
3. What data goes in at runtime, and are we allowed to use it that way?
4. If we fine-tuned or built an index, what is in the data register, and is each source cleared?
5. Can this output copy a named work, and what is our review step?
6. Do we need to own the output? If so, which human authors it?
7. Who re-checks all of this when the model version changes, and when?

If you cannot answer one, that is where to ask a lawyer.

## Common mistakes

- **Treating a court win for a model maker as a green light for your use.** A ruling on training does not cover your outputs or your inputs.
- **Treating "public on the internet" as "free to use".** Public is not licensed.
- **Assuming you own what the model wrote.** Ownership needs human authorship in several major jurisdictions.
- **Reading the licence once.** Re-read when the version or the plan changes.
- **No data register.** Without it you cannot answer a rights holder, an auditor or your own customer.
- **Relying on an indemnity you have not read.** They usually have conditions, such as using the vendor's safety filters.

## Next steps

- [EU AI Act compliance](./eu-ai-act-compliance.md) - the transparency and copyright duties for model providers
- [Privacy and data protection with AI](./privacy-and-data-protection-with-ai.md) - the personal-data side of the same inputs
- [AI risk assessment](./ai-risk-assessment.md) - where to record these risks
- [Open vs closed weights](../../explainers/concepts/open-vs-closed-weights.md) - open-weight licences with dated examples
- [Model supply chain security](../security/model-supply-chain.md) - verifying what you download

## Sources

- US Copyright Office, Copyright and Artificial Intelligence, reports and guidance. https://www.copyright.gov/ai/ (copyrightability report, January 2025). Checked from memory of the published report, not re-fetched on 2026-11-15; confirm against the site.
- Thaler v. Perlmutter, US Court of Appeals for the D.C. Circuit (2025): human authorship requirement.
- Bartz v. Anthropic and Kadrey v. Meta, US District Court for the Northern District of California (June 2025); Thomson Reuters v. Ross Intelligence, US District Court for the District of Delaware (2025). Check each docket for appeals and settlements.
- Getty Images v. Stability AI, High Court of England and Wales (2025).
- Directive (EU) 2019/790 on copyright in the Digital Single Market, Article 4; Regulation (EU) 2024/1689 (AI Act), Article 53(1)(c) and (d).
- Each model's own licence file and each vendor's current terms: read the live text, they change.
