# AI for Sales

**In one line:** Use AI to research accounts, prepare for calls, write first-draft outreach and follow-ups, and fill in CRM notes faster - then put the saved time into conversations, because the relationship and the judgment are still yours.
**Last reviewed:** 2026-10-21

---

## The short version

- The best sales uses are **preparation** (account research, call plans, objection prep) and **follow-through** (call summaries, follow-up emails, CRM notes, proposal drafts).
- AI-written outreach that sounds like AI gets ignored. Use it to draft, then add something only you know: a real reason for writing to this person now.
- Never trust AI for facts about a prospect without a source. Models can invent funding rounds, executives and news. Check the company's site, filings or a news article.
- Do not paste customer personal data or confidential deal terms into unapproved tools. Use the approved tool or the AI built into your CRM, per the [acceptable use policy](../enablement/acceptable-use-policy.md).
- Disclose AI where it talks to customers directly, and stay within the email and privacy laws that apply to your outreach.

## Where it fits in the sales cycle

| Stage | AI helps with | You still own |
|---|---|---|
| Prospecting | Summarising a company's public info, drafting a first-touch email | Choosing who to contact and why now |
| Call prep | Call plan, likely objections, discovery questions | Reading the room |
| Discovery | Turning call notes into a structured summary | Asking the right follow-up |
| Proposal | First draft from your template and notes | Pricing, scope, commitments |
| Follow-up | Recap email, next steps, CRM update | The relationship |
| Pipeline review | Summarising deal notes, spotting gaps | Forecast judgment |

## Copyable prompts

**Account research brief** (paste in public sources: their website "About" page, a recent press release, the job posting you found)
```
I sell [product, one sentence] to [type of buyer]. Here is public
information about [Company]: [paste sources].

Write a one-page account brief: what they do, recent changes that might
create a need for [product], likely priorities of a [role], and 3 specific
discovery questions. Only use the information I pasted. Mark anything you
are inferring as "(inference)".
```

**First-touch email**
```
Write a first email to [name, role] at [company]. Reason for reaching out
now: [specific trigger, e.g. they posted 4 data engineer jobs this month].
What we do: [one sentence]. A relevant result: [real customer outcome you
are allowed to share]. Under 90 words. No flattery, no "I hope this finds
you well". End with one low-commitment question. Give me 3 variations.
```

**Objection prep**
```
I am meeting [role] at a [industry, size] company about [product].
List the 6 most likely objections. For each: what is usually behind it, one
question to understand it better, and a short honest response. Do not
suggest claims about competitors.
```

**Call notes to CRM and follow-up**
```
Here are my notes from a discovery call: [paste notes].
1. Fill this template: Pain, Impact, Current solution, Decision process,
   Timeline, Budget signals, Next step. Write "not discussed" where empty.
2. Draft a follow-up email that recaps their priorities in their words,
   confirms the next step, and attaches nothing I did not mention.
```

**Proposal first draft**
```
Using our proposal template [paste] and these discovery notes [paste],
draft the "Situation", "Objectives" and "Approach" sections. Use the
customer's own language where possible. Leave pricing and timeline as
[TBD]. List any assumptions you made.
```

## Before and after

**Before.** A rep with 12 first meetings this week spends 30-40 minutes per account reading the website, LinkedIn and news, then writes call notes in a notebook and updates the CRM on Friday from memory.

**After.** For each account, the rep pastes the company's About page and two recent public items into the research prompt and gets a brief in two minutes, then spends 10 minutes checking it and adding what they know. After each call, they paste raw notes into the CRM prompt and update the record the same day. The follow-up email goes out within an hour instead of the next morning.

What did not change: the rep still decides which accounts are worth the time, still runs the conversation, and still checks every claim in the brief before using it with the customer.

## Outreach at scale: be careful

It is now cheap to generate thousands of "personalised" emails. That has three costs:

- **Deliverability and reputation.** Mailbox providers filter high-volume, low-engagement sending. Generic AI-written email at scale damages your domain.
- **Law.** Commercial email is regulated (for example CAN-SPAM in the US, and stricter consent rules for marketing email in the EU and UK under GDPR and PECR). AI does not change the rules. Check with your legal or marketing operations team.
- **Trust.** Buyers increasingly recognise generated text. One wrong "personal" detail ("congratulations on your Series B" to a company that never raised one) ends the conversation.

Use AI to make each email better, not to send more bad ones.

## Where not to use it

- **Pricing, discounts, legal terms and commitments.** Draft language, maybe; decide terms, no.
- **Competitor claims.** Models can confidently state outdated or false comparisons. Use your product marketing's approved battlecards.
- **Facts about the prospect without a source.** Treat any unsourced detail as a guess.
- **Personal data** from your CRM in an unapproved tool.

## Failure modes

- **Invented facts.** The model "fills in" a plausible executive name or recent event. Prompt it to use only pasted sources and mark inferences; then check.
- **Same-sounding emails.** If your whole team uses the same prompt, prospects get near-identical emails. Vary the trigger and add a human sentence.
- **CRM summaries that drop the nuance.** "Budget: approved" when the buyer said "probably next quarter". Read before you save.
- **Over-preparation.** A perfect brief does not replace listening.

## Common mistakes

- Pasting nothing and asking "tell me about Company X". You get a mix of training-data memory and guesses.
- Copy-pasting AI emails without reading them.
- Using AI to write longer emails. Shorter is usually better; ask for under 100 words.
- Not sharing what works. Put your best prompts in the team library with a champion; see [AI champions program](../enablement/ai-champions-program.md).

## Next steps

- Marketing's side of the same funnel: [AI for marketing](for-marketing.md)
- Turning calls into summaries reliably: [meetings and summaries](../use-cases/meetings-and-summaries.md)
- Researching accounts and markets with sources: [research and analysis](../use-cases/research-and-analysis.md)
- Why AI invents facts: [hallucinations](../../learn/concepts/hallucinations.md)

## Sources

- US Federal Trade Commission, *CAN-SPAM Act: A Compliance Guide for Business*: <https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business>
- UK Information Commissioner's Office, *Guide to PECR: Electronic mail marketing*: <https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/>
