# AI Acceptable Use Policy

**In one line:** Give your staff a short, plain-language AI policy that says which tools are approved, which data can go into them, and who is responsible for the output - and copy the template on this page to get there in an afternoon.
**Last reviewed:** 2026-10-21

---

## The short version

- A good AI policy fits on one or two pages and answers four questions: **which tools**, **which data**, **what review**, and **who to ask**.
- The biggest real risk for most organisations is not rogue robots. It is staff pasting confidential or personal data into consumer chatbots whose default settings may let the vendor keep or train on it.
- Write the data rules around your existing data classification (public, internal, restricted), not around AI jargon.
- The person who uses AI owns the output. Say so explicitly.
- Pair the policy with a sanctioned tool on day one. A ban with no alternative pushes usage out of sight.
- Review the policy every six months. Vendor terms and features change faster than most policies do.

## Why you need one, even if you are small

In April 2023, Samsung engineers pasted internal source code and meeting notes into ChatGPT while trying to get work done. Samsung responded by banning generative AI tools on company devices in May 2023. Nobody at Samsung was trying to leak anything. They had no clear rule and no approved alternative.

That pattern repeats. Consumer AI products and business products often have **different data terms**. As of 2026-10:

- OpenAI says data from ChatGPT Business, Enterprise and the API is not used for training by default, while content in consumer ChatGPT accounts may be used to improve models unless the user turns that off.
- Anthropic's consumer terms (Claude Free, Pro and Max) let Anthropic train on chats when the user's model-training setting is on, with retention of up to five years in that case; Claude's Team and Enterprise plans state no model training on your content by default.
- Microsoft states that prompts and responses in Microsoft 365 Copilot with a work account are not used to train foundation models, and are logged and available for audit and eDiscovery.
- Google states that Gemini in Workspace does not use your prompts or content to train generative models without permission.

So the same employee, doing the same task, can be inside or outside your data protection depending on which login they used. The policy's main job is to make the safe path the obvious one.

There is also a legal reason in some places. The EU AI Act's Article 4 has required, since 2 February 2025, that organisations deploying AI systems take measures to ensure a sufficient level of AI literacy among staff who use them. A policy plus training is the simplest way to show you have done that. See [EU AI Act compliance](../../safety/governance/eu-ai-act-compliance.md).

## How to write it in four steps

1. **Inventory.** Find out what tools people already use (an anonymous survey works; see the [adoption playbook](ai-adoption-playbook.md)).
2. **Classify data.** If you already have a data classification policy, reuse its levels. If not, three levels are enough: Public, Internal, Restricted.
3. **Approve tools.** For each tool, record the plan (consumer or business), whether training on your data is off, retention, and who administers it. Only business or enterprise plans with contractual data terms should be approved for Internal data.
4. **Fill in the template**, get sign-off from legal or privacy and from leadership, and publish it with a 30-minute walkthrough.

## The template

Copy everything inside the block, replace the bracketed parts, and delete what does not apply. It is written to be read by everyone in the organisation, not only by lawyers.

```markdown
# [Company] AI Acceptable Use Policy

Version [1.0] - effective [date] - owner: [name, role] - next review: [date + 6 months]

## 1. Why this exists
AI tools can save time on writing, summarising, analysis and coding. They can
also leak confidential data, produce confident mistakes, and create legal risk.
This policy tells you how to get the benefit safely. If something is unclear,
ask [contact/channel] before you act.

## 2. Who this covers
All employees, contractors and temporary staff using AI tools for [Company]
work, on any device or account.

## 3. Approved tools
| Tool | Plan | Allowed data | Admin |
|---|---|---|---|
| [e.g. Claude / ChatGPT / Copilot / Gemini] | [Business/Enterprise] | Public + Internal | [IT] |
| [Coding assistant] | [Business] | Public + Internal code | [Eng lead] |
| AI features built into [CRM/helpdesk] | [plan] | As per that system | [owner] |

Any tool not on this list is NOT approved for [Company] data, including free
or personal accounts of the tools above. To request a new tool, use [form].
Browser extensions, meeting bots and "AI note takers" count as tools.

## 4. What data you may use
- PUBLIC (published website content, public documents): any approved tool.
- INTERNAL (non-public business information, internal docs, code without
  secrets): approved tools only, signed in with your [Company] account.
- RESTRICTED - never in any AI tool unless the tool is listed as approved for
  it in writing:
  - personal data about customers, patients, employees or candidates
  - payment card, bank or government ID numbers
  - passwords, API keys, credentials, private keys
  - legally privileged material, unreleased financial results
  - information we hold under a client NDA or contract that limits its use
  - [add: health data, export-controlled data, etc.]
If you are not sure which bucket something is in, treat it as Restricted.
Removing names is not enough if the person can still be identified.

## 5. You own the output
- You are responsible for anything you send, publish, ship or decide using AI
  output, exactly as if you wrote it yourself.
- Check facts, numbers, names, quotes, links and citations against a real
  source before use. AI tools can invent them convincingly.
- Code generated by AI goes through the same review, testing and security
  checks as any other code.

## 6. Things you must not do
- Use AI to make or materially decide hiring, firing, promotion, pay, credit,
  or other decisions about individuals without [HR/legal] approval.
- Present AI output to a customer, regulator or court as verified fact
  without human review.
- Generate content that impersonates a real person, or deceptive, harassing
  or discriminatory content.
- Record or transcribe a meeting with AI without telling everyone present
  (and getting consent where the law requires it).
- Connect an AI tool or agent to company systems (email, drive, CRM, code
  repositories) unless IT has approved that connection.

## 7. Being open about AI use
- Tell customers when they are talking to an AI system rather than a person.
- Label substantially AI-generated external content where [our policy/law]
  requires it. [Decide your rule, e.g. marketing images.]
- Internally, you do not need to label every AI-assisted email.

## 8. If something goes wrong
If you think you have put Restricted data into an AI tool, or AI output has
caused a problem with a customer, report it to [security contact] within
[24 hours]. Reporting quickly will not get you in trouble; hiding it might.

## 9. Training
Everyone completes [the 90-minute AI basics session] before getting access to
approved tools, and the refresher every [12 months].

## 10. Changes
This policy is reviewed every six months and when we adopt a new tool.
Questions: [channel/email].
```

## Notes on the hard clauses

**"Removing names is not enough."** People often think anonymising means deleting the customer's name. A job title, a city and a complaint date can identify someone. If the task truly needs personal data, the answer is an approved tool with the right contract, not a half-scrubbed paste.

**Meeting recorders.** AI note-takers join calls and record everyone. In the United States, some states, including California, Florida and Illinois, require consent from every party to a recorded conversation. Your policy should require telling attendees, and external attendees in particular. See [meetings and summaries](../use-cases/meetings-and-summaries.md).

**Decisions about people.** Hiring, performance and credit decisions are where AI bias causes real harm and where laws such as the EU AI Act treat AI systems as high-risk. Keep these out of casual use and route them through a proper [AI risk assessment](../../safety/governance/ai-risk-assessment.md).

**Agents and connectors.** Newer assistants can read your email or drive and take actions. That expands what can leak and adds prompt injection risk, where text in a document or web page instructs the AI to do something you did not ask. Treat each connection like granting a new employee access. See [prompt injection explained](../../safety/security/prompt-injection-explained.md).

**Customer-facing AI.** In *Moffatt v. Air Canada* (2024), a Canadian tribunal held Air Canada liable for wrong refund information its website chatbot gave a customer, rejecting the argument that the chatbot was responsible for its own words. Your organisation owns what your AI says.

## Rolling it out

- Publish it in the same week as the sanctioned tool goes live.
- Walk through it in 30 minutes with real examples from your company: "Can I paste this customer email? No. Can I paste this internal process doc? Yes, in the approved tool."
- Put a one-line summary in the tool's login banner or welcome message if your tool supports it.
- Track questions people ask in the first month. Each recurring question is a sentence missing from the policy.

## Common mistakes

- **Writing a ten-page legal document.** Nobody reads it. Keep the policy short and put detail in an FAQ.
- **Listing banned tools by name.** There is a new one every week. List approved tools and say everything else is not approved.
- **Forgetting AI features inside tools you already have.** Your CRM, helpdesk, video call and document tools may have added AI features. They count.
- **Not saying who owns the output.** Without that sentence, mistakes become "the AI did it".
- **Never reviewing it.** Vendor data terms changed several times between 2023 and 2025. Put a review date at the top.

## Next steps

- Put the policy into practice: [AI adoption playbook](ai-adoption-playbook.md)
- Pick tools with the right data terms: [choosing enterprise AI tools](choosing-enterprise-ai-tools.md)
- Teach it: [training your team](training-your-team.md)
- Build the wider program around it: [AI governance program](../../safety/governance/ai-governance-program.md) and [responsible AI basics](../../safety/governance/responsible-ai-basics.md)
- Frameworks behind it: [NIST AI RMF](../../safety/governance/nist-ai-rmf.md), [ISO 42001](../../safety/governance/iso-42001.md)

## Sources

- Bloomberg, *Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak* (2 May 2023): <https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak>
- OpenAI, *Enterprise privacy at OpenAI*: <https://openai.com/enterprise-privacy/>
- OpenAI, *How your data is used to improve model performance*: <https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/>
- Anthropic, *Updates to Consumer Terms and Privacy Policy*: <https://www.anthropic.com/news/updates-to-our-consumer-terms>
- Claude pricing and plan features (Team, Enterprise: no model training on your content by default), as of 2026-10: <https://claude.com/pricing>
- Microsoft, *Data, Privacy, and Security for Microsoft 365 Copilot*: <https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy>
- Google, *Generative AI in Google Workspace Privacy Hub*: <https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub>
- EU AI Act, Article 4 (AI literacy): <https://artificialintelligenceact.eu/article/4/>
- Digital Media Law Project, *Recording Phone Calls and Conversations*: <https://www.dmlp.org/legal-guide/recording-phone-calls-and-conversations>
- McCarthy Tetrault, *Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot* (2024 BCCRT 149): <https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot>
