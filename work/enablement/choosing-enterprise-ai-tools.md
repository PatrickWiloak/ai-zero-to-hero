# Choosing Enterprise AI Tools

**In one line:** Pick a company-wide AI assistant (ChatGPT, Claude, Gemini or Microsoft Copilot) by checking data terms, admin controls, where your work already lives, and real cost per active user - in that order - rather than by which model topped a leaderboard this month.
**Last reviewed:** 2026-10-21

---

## The short version

- The four mainstream options as of 2026-10 are **ChatGPT Business / Enterprise** (OpenAI), **Claude Team / Enterprise** (Anthropic), **Gemini in Google Workspace** (Google) and **Microsoft 365 Copilot** (Microsoft).
- All four business offerings state that your content is not used to train their models by default. The consumer versions of the same products do not all make that promise. That gap is the most important thing to get right.
- If your company lives in Microsoft 365 or Google Workspace, the assistant built into that suite has a big advantage: it can work over your email, files and meetings with your existing permissions. If people mostly need a strong general-purpose assistant for writing, analysis and code, the standalone assistants often feel more capable day to day.
- Price per seat is only part of the cost. Count base licences you must already hold, minimum seat counts, premium seats, usage-based add-ons, and the seats nobody uses.
- Run a two-to-four week bake-off with real tasks from your own teams before signing an annual contract.

## What actually differs

Models from the leading labs are close enough on most office tasks that the deciding factors are usually elsewhere. For model-level comparisons, see [chat assistants compared](../../tools/comparisons/chat-assistants.md) and [which model for which job](../../tools/decisions/which-model-for-which-job.md). This page is about buying for an organisation.

### 1. Data terms

Ask each vendor, and get it in the contract or the published business terms:

- Is our content (prompts, files, outputs) used to train models? Is the default off?
- How long are conversations retained, and can an admin set a shorter retention?
- Where is data stored and processed (region / data residency)?
- Can we get a data processing agreement, and for regulated data, a HIPAA business associate agreement or equivalent?
- Who at the vendor can access our data, and for what (abuse monitoring, support)?

As of 2026-10, the published positions are:

| Vendor | Business plans | Training on your content | Source |
|---|---|---|---|
| OpenAI | ChatGPT Business, Enterprise, Edu, API | Not used for training by default | OpenAI enterprise privacy page |
| Anthropic | Claude Team, Enterprise | "No model training on your content by default" | Claude pricing page |
| Google | Gemini in Workspace business editions | Not used to train generative models without permission | Workspace Privacy Hub |
| Microsoft | Microsoft 365 Copilot (work accounts) | Prompts, responses and Graph data not used to train foundation models | Microsoft Learn privacy page |

The consumer side differs: OpenAI's consumer ChatGPT and Anthropic's Claude Free, Pro and Max plans can use chats for training unless the user's setting is off. This is why your [acceptable use policy](acceptable-use-policy.md) must say "your company account only".

### 2. Admin and security controls

What your IT team will need, roughly in priority order:

- **Single sign-on (SSO)** with your identity provider, so leavers lose access the day they leave.
- **User provisioning (SCIM)** so accounts are created and removed automatically.
- **Admin console**: who has seats, usage reports, feature toggles (for example, turning off web browsing, third-party connectors or file upload).
- **Audit logs and an export/compliance API** so security and legal can investigate and meet eDiscovery requests.
- **Retention controls**.
- **Connector controls**: which internal systems (drive, email, CRM, code) the assistant may connect to, and who can enable them.

As of 2026-10, Claude's published plan comparison lists SSO on Team, and SCIM, audit logs, a compliance API, custom retention and IP allowlisting on Enterprise. Microsoft states that Copilot prompts and responses with enterprise data protection are logged and available for audit, eDiscovery and Purview tools. Higher tiers of every vendor generally add SCIM, audit and retention controls; check the current plan page, because the boundaries move.

### 3. Where your work already lives

This is often the deciding factor.

- **Microsoft 365 shop** (Outlook, Teams, SharePoint, OneDrive): Microsoft 365 Copilot works inside those apps and respects the permissions people already have in Microsoft Graph. That is useful, and also a warning: if your SharePoint permissions are messy, Copilot will happily surface a salary spreadsheet to someone who technically had access to it all along. Clean up oversharing before rollout.
- **Google Workspace shop** (Gmail, Docs, Drive, Meet): Gemini is included in Workspace business plans and works across those apps.
- **Mixed or neither**: a standalone assistant (ChatGPT, Claude) with connectors to your drive, email and other systems. Check which connectors exist for your stack and whether admins control them.

Many organisations end up with two: the suite assistant for in-app help, and one standalone assistant for heavier writing, analysis and coding. That is fine if both are on business terms and both are in the policy.

### 4. Cost

List prices as of 2026-10 (US dollars, per user per month; confirm on the vendor page, these change often):

| Product | Published price | Notes |
|---|---|---|
| ChatGPT Business | $20 annual / $25 monthly (Standard seat); $100 annual / $125 monthly (Premium seat) | Minimum two seats; Premium has more usage |
| ChatGPT Enterprise | Not published; contact sales | |
| Claude Team | $20 annual / $25 monthly (Standard seat); $100 annual / $125 monthly (Premium seat) | |
| Claude Enterprise | $20 per seat billed annually, 20-seat minimum, plus usage that scales with model and task | |
| Google Workspace (Gemini included) | Business Starter $7, Standard $14, Plus $22 (annual billing); Enterprise by quote | Starter has limited Gemini features; Standard and above have expanded access |
| Microsoft 365 Copilot Business (add-on) | $21 annual (promotional $18 at time of review); $25.20 monthly | Requires an eligible Microsoft 365 business plan |
| Microsoft 365 Business Standard / Premium with Copilot | $23.50 / $32.00 annual | Bundles the base licence |
| Microsoft 365 Copilot (enterprise add-on) | $30 annual | On top of an eligible enterprise licence |

To compare honestly, compute **cost per weekly active user**, not per seat:

```
monthly cost per active user = (seats x price + usage add-ons) / weekly active users
```

If you buy 200 seats at $30 and 80 people use it weekly, you are paying $75 per active user per month. That number, against the time saved per active user from [measuring AI ROI](measuring-ai-roi.md), is your real business case.

## Running a bake-off

Two to four weeks, before you sign anything annual.

1. **Shortlist two tools**, usually the one built into your suite and one standalone.
2. **Pick 10-15 real tasks** from your pilot teams, with sample inputs that contain no Restricted data. For example: summarise this 30-page report into a one-page brief; draft a reply to this customer complaint using this policy; turn this messy spreadsheet into a pivot summary with three insights; find what our drive says about our travel policy.
3. **Have 10-20 pilot users try both** on the same tasks, and score each output 1-5 on accuracy, usefulness, and edits needed. Ideally the scorer does not know which tool produced which output.
4. **Have IT score the admin side**: SSO, provisioning, logs, connector controls, data terms.
5. **Ask legal to read the data terms** and the DPA.
6. **Decide with a simple weighted table**: data terms (pass/fail), admin fit 25%, user scores 40%, integration with your systems 20%, cost per active user 15%. Adjust the weights to your situation, but decide them before you see the scores.

## Questions to ask the vendor

- What is your default for training on our data, and where is that written?
- What is the default retention, and what is the minimum we can set?
- Which features send data to third parties or to the open web (web search, plugins, connectors), and can we turn each off?
- What usage limits apply per seat, and what happens when someone hits them?
- What is included in the seat price, and what is billed by usage?
- Can we start monthly, or with a smaller seat count, and expand?
- What admin reports do we get on active usage?

## Common mistakes

- **Choosing on benchmark scores.** The leaderboard leader changes every few months. Contracts last a year. Pick on data terms, admin and fit.
- **Buying for everyone up front.** Start with the pilot cohort and expand on evidence. Unused seats are the largest hidden cost.
- **Ignoring permissions before turning on a suite assistant.** It will find every overshared file.
- **Approving the business plan but not blocking personal accounts.** Without SSO and a clear policy, people keep using their personal login out of habit.
- **Assuming the free AI features already in your apps are covered.** Check each one's terms.

## Next steps

- Write the rules that go with the tool: [acceptable use policy](acceptable-use-policy.md)
- Plan the rollout: [AI adoption playbook](ai-adoption-playbook.md)
- Compare assistants for individual use: [pick a chat assistant](../../learn/day-one/pick-a-chat-assistant.md)
- Thinking of building your own instead: [build vs buy](../../tools/decisions/build-vs-buy.md)
- Model families behind the products: [GPT](../../explainers/model-families/gpt.md), [Claude](../../explainers/model-families/claude.md), [Gemini](../../explainers/model-families/gemini.md)

## Sources

- OpenAI, *Enterprise privacy at OpenAI*: <https://openai.com/enterprise-privacy/>
- OpenAI, *ChatGPT Business pricing* and *ChatGPT Business overview* (seat prices, two-seat minimum), as of 2026-10: <https://openai.com/business/pricing/>, <https://help.openai.com/en/articles/8792828-chatgpt-business-overview>
- OpenAI, *Premium seats are coming to ChatGPT Business*: <https://openai.com/index/premium-seats-chatgpt-business/>
- OpenAI, *How your data is used to improve model performance*: <https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/>
- Anthropic, Claude plans and pricing, as of 2026-10: <https://claude.com/pricing>
- Anthropic, *Updates to Consumer Terms and Privacy Policy*: <https://www.anthropic.com/news/updates-to-our-consumer-terms>
- Google Workspace pricing, as of 2026-10: <https://workspace.google.com/pricing>
- Google, *Generative AI in Google Workspace Privacy Hub*: <https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub>
- Microsoft 365 Copilot pricing (business), as of 2026-10: <https://www.microsoft.com/en-us/microsoft-365-copilot/pricing>
- Microsoft 365 Copilot enterprise pricing, as of 2026-10: <https://www.microsoft.com/en-us/microsoft-365-copilot/enterprise>
- Microsoft, *Data, Privacy, and Security for Microsoft 365 Copilot*: <https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy>
