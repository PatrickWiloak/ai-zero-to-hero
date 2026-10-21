# AI for Marketing

**In one line:** Use AI to brainstorm, draft, repurpose and test marketing content faster, while a human owns the strategy, the facts, the brand voice and anything legally risky - because generic AI copy is easy to make and easy for your audience to ignore.
**Last reviewed:** 2026-10-21

---

## The short version

- Good uses: **ideation**, **first drafts**, **repurposing** one asset into many formats, **variant generation** for tests, **editing** for clarity and length, **summarising research** and customer feedback.
- Weak uses: strategy, positioning, and anything that needs real customer insight or claims you have not verified.
- Give it your brand voice guide, audience description and real examples. Without them you get the average of the internet.
- Every factual or comparative claim needs a source you can show. Advertising law applies to AI-written copy exactly as it does to human-written copy.
- Check image and content rights, and label AI-generated media where your policy or the platform requires it.

## Where it fits

| Work | AI is good for | Human must own |
|---|---|---|
| Campaign planning | Brainstorming angles, outlining a content calendar | Choosing the strategy |
| Copywriting | First drafts, headlines, variants for A/B tests | Final voice and claims |
| Repurposing | Blog post to email, social posts, short script | Platform judgment |
| SEO content | Outlines, briefs, meta descriptions | Original insight, expertise, accuracy |
| Research | Summarising interviews, reviews, survey comments | Interpreting what it means |
| Editing | Shortening, simplifying, tone adjustment | Approval |
| Images | Concepts, mood boards, simple assets | Rights, brand fit, disclosure |

## Set it up once: a brand context block

Write this once, store it in your prompt library, and paste it at the top of marketing prompts (or put it in your tool's project or custom-instructions feature, if it has one):

```
BRAND CONTEXT
Company: [name], [one-sentence what we do]
Audience: [who, role, what they care about, what they are sick of hearing]
Voice: [3-5 traits, e.g. plain, specific, a little dry; never hype]
We never say: [banned words/phrases, e.g. "revolutionary", "unlock", "seamless"]
Proof we can cite: [real customer outcomes, approved stats with sources]
Products: [names and one line each]
Style: [sentence case headings, US spelling, no exclamation marks]
Example of our best writing: [paste 2-3 short samples]
```

## Copyable prompts

**Angles before copy**
```
[Brand context]
We are launching [feature] for [audience]. The real customer problem, in
their words, from interviews: [paste 3-5 quotes].
Give me 8 distinct campaign angles. For each: a one-line hook, which customer
quote it builds on, and who it would NOT work for. No copy yet.
```

**Repurpose one asset**
```
[Brand context]
Here is our blog post: [paste].
Create: (1) a 120-word email for existing customers, (2) three LinkedIn
posts under 80 words each with different hooks, (3) a 45-second video
script. Keep every factual claim exactly as stated in the post. Do not add
statistics.
```

**Headline variants for a test**
```
[Brand context]
Landing page for [offer], audience [who]. Current headline: "[...]".
Write 10 alternatives across these approaches: outcome, problem, question,
specific number from our approved proof, and plain description. Max 9 words.
Label each with its approach.
```

**Customer feedback synthesis**
```
Here are [N] open-text survey responses: [paste, with personal details removed].
Group them into themes. For each theme: a count, two representative quotes
copied exactly, and what it suggests we test. List responses that fit no
theme separately. Do not paraphrase the quotes.
```

**Edit for clarity**
```
[Brand context]
Edit this for clarity and length. Target [N] words. Keep the meaning and all
claims. Show the edited version, then list what you cut and why: [paste].
```

## Before and after

**Before.** A two-person marketing team turns each webinar into a recap blog post, an email and a week of social posts. It takes most of two days, so it only happens for half the webinars.

**After.** They paste the webinar transcript (from an approved transcription tool) with the brand context into a repurposing prompt, get drafts of all the pieces in minutes, and spend half a day editing: cutting generic lines, checking every claim against the transcript, adding one original insight per piece. Every webinar gets repurposed. The pieces that perform best are the ones where they added the most of their own view.

## Claims, rights and disclosure

- **Claims need substantiation.** Advertising rules in many jurisdictions require evidence for objective claims. In the US, the FTC has said there is no AI exemption from the laws on deceptive practices, and has brought cases over AI-related claims. If AI suggests "3x faster", you need the data or you delete it.
- **Fake reviews and testimonials.** Never generate reviews or testimonials. The FTC's rule on fake reviews, effective October 2024, covers AI-generated fake reviews.
- **Copyright.** The US Copyright Office's position is that material generated by AI without sufficient human authorship is not protected by copyright, so purely AI-generated assets may not be yours to protect. Check your image tool's licence for commercial use, and do not prompt for a named artist's style or a competitor's trademark.
- **Disclosure.** Some platforms require labelling AI-generated or altered realistic media. Follow your policy and the platform rules.

## Where not to use it

- Positioning and strategy from scratch. AI will give you the industry average.
- Statistics, quotes and case studies it produces without a source. Assume they are invented.
- Customer data in unapproved tools. Remove names and identifiers from feedback before pasting, or use an approved tool.
- Sensitive topics (health, finance, crisis communications) without expert and legal review.

## Failure modes

- **Sameness.** Everyone's AI copy converges on the same phrases. Your banned-words list and real examples are the defence.
- **Volume over quality.** Producing three times the content does not triple results. Search engines and readers reward usefulness.
- **Quiet claim drift.** In repurposing, "up to 30% faster in one customer's test" becomes "30% faster". Compare claims line by line against the source.
- **Hallucinated sources.** Ask for sources and you may get plausible links that do not exist. Click every one.

## Common mistakes

- No brand context, then complaining the output is bland.
- Asking for "a blog post about X" instead of feeding it your expertise.
- Publishing without a fact check.
- Not measuring: test AI-assisted variants against your current best, not against nothing.

## Next steps

- The other half of the funnel: [AI for sales](for-sales.md)
- Analysing campaign and survey data: [AI for analysts](for-analysts.md)
- Research with sources: [research and analysis](../use-cases/research-and-analysis.md)
- Image generation background: [diffusion models](../../learn/concepts/diffusion-models.md)
- Rules for your team: [acceptable use policy](../enablement/acceptable-use-policy.md)

## Sources

- US FTC, *FTC Announces Crackdown on Deceptive AI Claims and Schemes* (Operation AI Comply, September 2024): <https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes>
- US FTC, *Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials* (August 2024): <https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials>
- US Copyright Office, *Copyright and Artificial Intelligence, Part 2: Copyrightability* (January 2025): <https://www.copyright.gov/ai/>
