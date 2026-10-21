# AI for Everyone

**In one line:** If you work with documents, email, spreadsheets or customers, this page shows you how to use AI assistants well in your actual job, what to never paste into them, and how to tell when an answer cannot be trusted.
**Last reviewed:** 2026-10-21

---

## The short version

- An AI assistant (ChatGPT, Claude, Gemini, Copilot and others) is a very fast, very widely read first-draft writer and explainer. It is not a database of facts and it does not know your company.
- It is best at **turning one kind of text into another**: long into short, rough into polished, technical into plain, notes into a structured document, a question into a first answer you then check.
- It is worst at **facts you cannot check**: precise numbers, quotes, citations, legal or medical specifics, and anything that happened after its training data was collected. It will state these confidently whether or not they are right.
- Give it what a new colleague would need: who you are, what the task is, who the result is for, and an example of what good looks like. Short vague prompts get generic answers.
- Follow your employer's rules about what data can go into which tool. If there are none, assume customer data, personal data, passwords and unreleased financials do not go into a personal account.
- You stay responsible for what you send. "The AI wrote it" is not a defence for a wrong number in a client email.

## What these tools actually are

When you type into a chat assistant, your message goes to a **large language model**: a program trained on a huge amount of text to predict what words come next. Through that training, and a second stage where people rated its answers, it learned to write, summarise, explain, translate, reason through problems and follow instructions. You can read the longer version in [What is machine learning?](../concepts/what-is-machine-learning.md) and [LLM basics](../concepts/llm-basics.md), but you do not need to in order to use one well.

Two consequences matter for your daily work.

First, the model's goal during training was to produce **plausible** text. Most of the time plausible and true line up. When they do not, the model still produces something plausible. That is why AI can invent a reference to a report that does not exist, with a realistic title and author. The technical name is **hallucination**, and [Hallucinations](../concepts/hallucinations.md) explains why it happens and how to work around it.

Second, the model only knows what was in its training data and what you put in the conversation. It does not know your customers, your internal processes, last week's meeting, or what your manager meant. Many assistants can now search the web or connect to your files, and when they do, they are reading those sources in the moment, which is much more reliable than asking from memory.

## Where it helps most

Here are tasks that work well for almost any office job, with the kind of prompt that gets a good result.

**Summarising long material.** Paste a long document, email thread or meeting transcript and ask for the parts you need.

```
Here is a 14-page vendor contract. I am the office manager and I need to know:
1. When does it renew, and how much notice do we need to give to cancel?
2. Are there any fees beyond the monthly price?
3. Anything unusual compared to a standard services contract?
Quote the clause number for each answer so I can check it.
```

The last line is the important habit: asking for the location of each claim lets you verify in seconds.

**Drafting.** First drafts of emails, announcements, job descriptions, policies, reports. Tell it the audience and the tone, and give it the facts. Do not let it supply the facts.

```
Draft a short email to our customers saying the office will be closed
on 24 and 25 December and reopen on 26 December at 9am. Support emails
will be answered on the 26th. Friendly but brief, no exclamation marks.
```

**Rewriting.** Make this shorter, make this friendlier, make this suitable for a non-expert, turn these bullet notes into a paragraph, fix the grammar without changing the meaning.

**Explaining.** "Explain this spreadsheet formula", "what does this error message mean", "explain this clause as if I have never read a contract". Ask follow-up questions; that is where the value is.

**Structuring.** Turn messy notes into a table, a checklist, a project plan, or a set of meeting minutes with owners and dates.

**Thinking partner.** "Here is my plan for the team offsite. What could go wrong?" Models are good at listing risks and counterarguments you did not think of. They are less good at deciding which ones matter for your situation; that part stays with you.

For role-specific examples, see the playbooks for [managers](../../work/playbooks/for-managers.md), [sales](../../work/playbooks/for-sales.md), [marketing](../../work/playbooks/for-marketing.md), [analysts](../../work/playbooks/for-analysts.md) and [support and operations](../../work/playbooks/for-support-and-ops.md).

## How to write a good prompt

You do not need special tricks. You need to brief the model the way you would brief a capable new colleague who knows nothing about your situation. A good prompt usually has four parts:

1. **Context:** who you are and what the situation is. "I run a 12-person accounting practice."
2. **Task:** what you want done, in one sentence. "Write a one-page checklist for onboarding a new client."
3. **Audience and format:** who will read it and what shape it should take. "For our junior staff. A numbered list, no more than 15 items."
4. **An example or constraints:** what good looks like, or what to avoid. "Here is our current checklist for tax returns, match its style."

Compare the result of "write an onboarding checklist" with the four-part version. The difference is large and it costs you thirty seconds.

When the first answer is not right, do not start over. Say what is wrong: "too formal", "you missed the part about engagement letters", "make item 4 into two separate steps". Iterating in the same conversation is how experienced users get good results.

[Prompt engineering](../concepts/prompt-engineering.md) goes deeper if you want it.

## Where it goes wrong

Treat these as the warning signs.

**Specific facts from memory.** Ask "what is the current VAT rate in Ireland?" and you may get an answer that was true when the model was trained, or one that was never true. If the assistant searched the web and shows sources, click them. If it did not, check elsewhere.

**Citations and quotes.** Never send a quote, statistic or reference from an AI answer without finding the original. Fabricated legal citations have already led to sanctions for lawyers who filed them in court.

**Maths in long chains.** Modern models are much better at arithmetic than they were, especially the "reasoning" models that work through a problem before answering ([Reasoning models](../../explainers/concepts/reasoning-models.md) explains these). For anything that matters, ask it to show its working, or use a spreadsheet.

**Agreeing with you.** Models tend to go along with the framing of the question. "Why is our plan a good idea?" gets a list of reasons it is good. Ask "what are the strongest arguments against this plan?" as well.

**Sounding sure.** Confidence in the wording tells you nothing about accuracy. A model says "the deadline is 31 March" in exactly the same tone whether it read that in your document or made it up.

A simple rule: **use AI output as a draft that you check, never as a source you cite.**

## What not to paste in

This is the part that can get you or your employer in trouble.

- **Check your organisation's policy first.** Many employers now have an [acceptable use policy](../../work/enablement/acceptable-use-policy.md) that lists approved tools and what data can go into them. Business and enterprise versions of these tools usually come with contractual promises that your data is not used for training; free personal accounts often have different terms.
- **Personal data** about customers, patients, students or employees: names with account details, health information, addresses, ID numbers. Even when a tool is approved, data protection law may limit what you can do.
- **Secrets:** passwords, API keys, access codes.
- **Confidential business information** you would not email to an outside contractor without an agreement: unreleased financials, deal terms, legal advice, source code you do not own.

If you need AI help with sensitive material and there is no approved tool, remove the identifying details first ("Customer A", "Company X", round numbers) and ask about the structure of the problem instead.

## Choosing a tool

If your employer provides one, use that; it is the one with the data agreement. Otherwise [Pick a chat assistant](../day-one/pick-a-chat-assistant.md) compares the main options and their free and paid tiers. The differences between the leading assistants matter less than how well you brief them. Pick one, use it every day for two weeks, and you will be ahead of most of your colleagues.

## Common mistakes

- **One-line prompts.** "Write a report on our sales" gives a generic template. Paste the numbers, say who reads it, and say what decision it supports.
- **Trusting the first answer.** Read it as a colleague's first draft. Push back where it is wrong.
- **Pasting everything in.** More context helps, but irrelevant context can distract. Give it what the task needs.
- **Using it to avoid understanding.** If you send an AI-written analysis you cannot explain, the first follow-up question will expose that. Use it to learn faster, not to skip learning.
- **Giving up after a bad experience.** Tools improve fast, and most bad results come from vague prompts. Try the four-part prompt before deciding AI cannot help with a task.

## Next steps

- [Pick a chat assistant](../day-one/pick-a-chat-assistant.md)
- [Hallucinations](../concepts/hallucinations.md): why models invent things, and the habits that protect you
- [Meetings and summaries](../../work/use-cases/meetings-and-summaries.md) and [Document processing](../../work/use-cases/document-processing.md): two of the highest-value everyday uses
- Curious how it works? [The Zero to Hero path](zero-to-hero-path.md), Phases 0 and 1, need no code
- Leading a team? [AI for leaders](ai-for-leaders.md)

## Sources

- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT, 2022), the training approach behind chat assistants: https://arxiv.org/abs/2203.02155 (summary: [InstructGPT](../../papers/language-models/05-instructgpt-rlhf/summary.md))
- Kalai et al., "Why Language Models Hallucinate" (2025): https://arxiv.org/abs/2509.04664 (summary: [Why Language Models Hallucinate](../../papers/techniques/149-why-language-models-hallucinate/summary.md))
- Mata v. Avianca, Inc., No. 22-cv-1461 (S.D.N.Y. June 22, 2023), sanctions for fabricated AI-generated citations: https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
- Anthropic, "Prompt engineering overview": https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
