# Research and Analysis with AI

**In one line:** Use AI search and "deep research" tools to find, read and synthesise sources much faster, but treat every claim and citation as unverified until you have opened the source yourself - because these tools still misquote and invent references.
**Last reviewed:** 2026-10-21

---

## The short version

- AI research tools come in three kinds: **chat with your documents** (you supply the sources), **AI search** (the tool searches the web and cites results), and **deep research agents** (the tool runs many searches over minutes and writes a long report).
- They are excellent for getting oriented in a new topic, finding sources you would have missed, summarising long material, and structuring a comparison.
- They are unreliable as a final authority. In a 2025 Tow Center test of eight AI search tools, the tools failed to correctly identify the source of news excerpts in more than 60% of queries, and some produced fabricated links.
- The rule: **AI finds and drafts; you verify and conclude.** Open every source you cite. Check that it says what the summary claims.
- In 2023, lawyers in *Mata v. Avianca* were sanctioned for filing a brief citing cases ChatGPT had invented. That is the failure mode to design against.

## Choosing the right mode

| Mode | Best for | Main risk |
|---|---|---|
| Chat with your own documents | Summarising reports, comparing documents you trust, Q&A over a fixed set | Misreading or missing a detail |
| AI search with citations | Quick factual orientation, finding recent sources | Wrong or mismatched citations |
| Deep research agents | Broad landscape reviews, first drafts of briefings | Long, confident reports mixing good and weak sources |
| Model's own knowledge (no search) | Explaining concepts, brainstorming angles | Outdated or invented facts; no sources |

When accuracy matters, prefer modes where **you control the sources**: gather the documents yourself, then ask the AI to work only from them. This is the same idea as [retrieval-augmented generation](../../learn/concepts/rag-explained.md).

## A research workflow that holds up

```
1. Frame     - write the question, the decision it informs, and what
               "good enough" evidence looks like
2. Explore   - AI search / deep research to map the topic and find sources
3. Collect   - open the sources; keep the ones that are primary or credible
4. Extract   - AI pulls claims, numbers and quotes from YOUR collected
               sources, with locations
5. Verify    - check every number and quote you will use against the source
6. Synthesise- AI drafts the structure; you write the conclusions
7. Record    - list sources with links and dates; note what you could not verify
```

## Copyable prompts

**Frame the question**
```
I need to research [topic] to decide [decision] by [date]. Before searching,
help me break this into 5-8 specific questions, and for each say what kind
of source would be credible (primary data, regulator, peer-reviewed study,
vendor documentation, etc.).
```

**Explore with sources**
```
Find recent, credible sources on [question]. For each source: title,
publisher, date, link, and one sentence on what it claims. Prefer primary
sources (official data, original studies, filings) over articles about
them. Say clearly if you could not find a good source for part of the
question.
```

**Extract from sources you collected**
```
Here are [N] documents I have collected: [paste or attach].
For the question "[question]", extract every relevant claim as a table:
claim, exact quote, document, page/section. Do not use any information
that is not in these documents. Then list where the documents disagree.
```

**Steelman and gaps**
```
Here is my draft conclusion and the evidence: [paste]. Give the strongest
case against my conclusion, which evidence is weakest, and what single piece
of evidence would most change my mind.
```

**Executive brief**
```
From this verified evidence table [paste], write a one-page brief for
[audience]: the answer in two sentences, the three key supporting points
with their sources, the main uncertainty, and a recommendation. Use only
the evidence in the table.
```

## Verifying citations, quickly

For each citation you intend to use:

1. **Does the link open?** Fabricated URLs are common.
2. **Is it the source it claims to be?** Same title, author, publisher, date.
3. **Does it say what the summary says?** Search the page for the number or quote. Watch for "up to", "in one case", and the wrong year.
4. **Is it primary?** If it is an article reporting a study, find the study.
5. **Is it current enough?** Prices, laws and product features change; note the date.

This takes a few minutes per source and is the step that separates research from rumour.

## Before and after

**Before.** A strategy analyst is asked for a two-page briefing on a new regulation's impact on the company. She spends two days finding and reading the regulation, official guidance and law-firm commentary.

**After.** A deep research tool produces a long report with dozens of citations in under half an hour, which she uses as a map, not an answer. She collects the regulation text, the official guidance and three law-firm analyses, then uses the extraction prompt on just those documents. Verifying the report's citations, she finds two that point to the wrong article and one date that refers to an earlier draft of the law. The briefing takes a day instead of two, and every claim in it traces to a source she opened.

## Where AI research is weakest

- **Very recent events**, where sources are thin and the tool may rely on old training data.
- **Niche or specialised fields**, where few sources exist and the model fills gaps plausibly.
- **Numbers.** Statistics get rounded, mixed up between sources, or attached to the wrong year.
- **Contested topics**, where the tool may present one side's framing as consensus.
- **Paywalled and internal sources**, which it cannot read unless you provide them.

## Data and confidentiality

Your research questions can themselves be sensitive (an acquisition target, a product plan). Use your approved tool, and remember that web-search features send queries outside your organisation. See the [acceptable use policy](../enablement/acceptable-use-policy.md).

## Common mistakes

- Citing something you have not opened.
- Accepting a deep research report as the deliverable.
- Asking the model's memory for facts instead of asking it to search or to read your sources.
- Not recording what could not be verified.
- Letting AI write the conclusion. The judgment is the part your organisation is paying for.

## Next steps

- Analysis on data rather than documents: [AI for analysts](../playbooks/for-analysts.md)
- Extracting from documents at scale: [document processing](document-processing.md)
- How grounding works: [RAG explained](../../learn/concepts/rag-explained.md), [the RAG paper](../../papers/techniques/13-rag/summary.md)
- Why AI invents things: [hallucinations](../../learn/concepts/hallucinations.md), [Why Language Models Hallucinate](../../papers/techniques/149-why-language-models-hallucinate/summary.md)

## Sources

- Jaźwińska and Chandrasekar, *AI Search Has a Citation Problem*, Tow Center for Digital Journalism / Columbia Journalism Review (March 2025): <https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php>; summary in Nieman Lab: <https://www.niemanlab.org/2025/03/ai-search-engines-fail-to-produce-accurate-citations-in-over-60-of-tests-according-to-new-tow-center-study/>
- *Mata v. Avianca, Inc.*, No. 22-cv-1461 (S.D.N.Y. June 22, 2023), opinion and order on sanctions: <https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf>
