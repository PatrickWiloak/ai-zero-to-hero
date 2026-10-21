# Pick a Chat Assistant

**In one line:** How to choose between ChatGPT, Claude, Gemini, Microsoft Copilot and the rest - what the free and paid tiers get you as of 2026-10, which strengths actually differ, what to check about your data, and a one-week test to decide for yourself.
**Last reviewed:** 2026-10-21

---

## The short version

- The leading assistants (OpenAI's **ChatGPT**, Anthropic's **Claude**, Google's **Gemini**, and **Microsoft Copilot**) are all good enough for everyday writing, summarising, explaining and brainstorming. For most people, how well you brief the assistant matters more than which one you pick.
- All of them have a **free tier**. The main paid individual plans cluster around **$20 a month** as of 2026-10, with cheaper entry plans and $100-plus plans for heavy users.
- The real differences are in **ecosystem** (which apps and files it connects to), **usage limits**, **specific strengths** (long documents, coding, research with sources, image and video generation), and **data terms**.
- If your employer provides an assistant, use that one for work. It is the one with a contract covering your data.
- Decide by testing: run the same five real tasks from your week through two assistants and keep the one whose answers you edited least.

## What they all do

As of 2026-10, every major assistant can hold a conversation, read files you upload (PDFs, documents, spreadsheets, images), search the web and cite sources, write and explain code, and work in a mobile app as well as the browser. Most offer voice conversation, some form of memory across chats, and "projects" or folders that keep files and instructions together for repeated work. Most can also use a slower "thinking" or reasoning mode for harder problems; [Reasoning models](../../explainers/concepts/reasoning-models.md) explains what that does.

Because the basics are shared, the decision comes down to a handful of differences.

## The main options

**ChatGPT (OpenAI).** The best-known assistant, with a broad set of built-in features: image generation, voice, web search, file analysis, and a large ecosystem of custom assistants. As of 2026-10 the individual plans are Free, Go ($5.50 a month), Plus ($20 a month), and Pro at higher prices for heavy use, according to a dated October 2026 pricing review (OpenAI's own pricing page blocks automated reading, so check it directly). The models behind it are described in the [GPT family explainer](../../explainers/model-families/gpt.md).

**Claude (Anthropic).** Often chosen for long-form writing, working through long documents, and coding. As of 2026-10, Anthropic lists Free, Pro at $20 a month ($17 a month billed annually; Pro includes Claude Code, Anthropic's coding tool, and Projects), and Max at $100 or $200 a month for five or twenty times Pro's usage. See the [Claude family explainer](../../explainers/model-families/claude.md).

**Gemini (Google).** The natural choice if you live in Gmail, Docs and Drive, since it connects to them directly, and built to handle very long inputs, including video. As of 2026-10 Google lists Free, Google AI Plus ($4.99 a month), Google AI Pro ($19.99 a month, with access to its top "Gemini 4 Argon" model), and Google AI Ultra ($99.99 to $199.99 a month). See the [Gemini family explainer](../../explainers/model-families/gemini.md).

**Microsoft Copilot.** Free as a standalone app, and built into Windows, Edge and Microsoft 365. For individuals, the in-app Copilot features in Word, Excel, PowerPoint and Outlook come with Microsoft 365 subscriptions; as of 2026-10 the top consumer tier, Microsoft 365 Premium, is $19.99 a month according to a 2026 plan overview. If your work happens in Office, this is the low-friction option.

**Others worth knowing.** Meta AI is built into WhatsApp, Instagram and Facebook. Mistral's Le Chat comes from a European lab. DeepSeek and Qwen offer strong assistants from Chinese labs, with data-handling terms you should read carefully if you are outside China. Perplexity focuses on search with citations. And you can run an assistant entirely on your own computer, privately and for free, with [Run a model locally](run-a-model-locally.md).

Prices and plan names change several times a year. Treat the figures above as a snapshot and confirm on each provider's pricing page.

## How to choose

**1. Start with where you work.** If your organisation provides an assistant, use it for work tasks; it is covered by a data agreement and your admins can support it. For personal use, the ecosystem question usually decides: Google Workspace users get the most from Gemini, Microsoft 365 users from Copilot, and the standalone assistants (ChatGPT, Claude) work everywhere through the browser and their apps.

**2. Match the strengths to your tasks.**

| If you mostly... | Look closely at |
|---|---|
| Work with long reports, contracts or books | Assistants with large context and good file handling; test with your longest real document |
| Write code | Claude and ChatGPT both have strong coding modes; see [coding assistants](../../tools/comparisons/coding-assistants.md) for dedicated tools |
| Research topics and need sources | Each assistant's web search or "deep research" mode; check that citations actually support the claims |
| Create images or video | ChatGPT and Gemini have built-in generation; [Diffusion models](../concepts/diffusion-models.md) explains how it works |
| Live in Gmail, Docs, Drive | Gemini |
| Live in Outlook, Word, Excel, Teams | Copilot |

**3. Check the data terms.** For any assistant, find out: is your conversation used to train future models, and can you turn that off? How long is it kept? Can you delete it? Consumer and business plans often differ here, with business plans typically excluding your data from training by contract. If you handle personal or confidential information, this question matters more than any feature. [AI for everyone](../start-here/ai-for-everyone.md) covers what not to paste in.

**4. Decide whether to pay.** The free tiers are genuinely useful but have tighter usage limits and often a smaller model by default. Pay when you hit the limits regularly, when you need the strongest model for hard tasks, or when a specific feature (longer files, more research runs, a coding tool) saves you real time. One paid assistant is enough for almost everyone; a second free one is handy for cross-checking important answers.

## The one-week test

Pick five tasks from your real work last week: say, summarising a long email thread, drafting a reply to a difficult message, explaining a spreadsheet, outlining a presentation, and researching a question you needed answered. Run each through two assistants with the **same prompt**. For each pair of answers, note:

- Which one needed less editing before you could use it?
- Did either state something false? (Check the specific facts.)
- Which one followed your instructions on length, tone and format?
- How did it handle your actual files?

Keep the one that won more often. Repeat the test once or twice a year, because models change quickly and the leader on your tasks may change too.

## Beyond the chat window

Once you are comfortable, three upgrades pay off:

- **Custom instructions or projects.** Tell the assistant once who you are and how you like answers, and attach the documents you refer to repeatedly.
- **Connectors.** Many assistants can now read your email, calendar, drive or other tools directly. Powerful, but think about what you are granting access to, and read [Prompt injection explained](../../safety/security/prompt-injection-explained.md): an assistant that reads your email can be manipulated by text inside an email.
- **The API.** If you find yourself repeating the same task dozens of times, it can be automated. [Your first LLM API call](first-llm-api-call.md) is the start. Note that API access is billed separately from chat subscriptions.

## Common mistakes

- **Choosing by leaderboard.** Benchmark rankings shift monthly and measure narrow skills ([human preference arenas](../../explainers/benchmarks/human-preference-arenas.md) explains the popular ones). Your own tasks are the better test.
- **Paying for three.** One paid assistant used well beats three used occasionally.
- **Using a personal account for work data.** Use your employer's approved tool, or ask for one.
- **Assuming the free tier is the full product.** Free tiers often use smaller models and stricter limits; judge the paid tier on a short trial before writing an assistant off.
- **Never switching.** The field moves fast. Re-run your test periodically.

## Next steps

- [AI for everyone](../start-here/ai-for-everyone.md): how to brief an assistant and check its work
- [Chat assistants comparison](../../tools/comparisons/chat-assistants.md): a detailed feature-by-feature table
- [Choosing enterprise AI tools](../../work/enablement/choosing-enterprise-ai-tools.md): for teams and organisations
- [Hallucinations](../concepts/hallucinations.md)

## Sources

- Anthropic, Claude plans and pricing (Free, Pro $20 or $17/month annual, Max $100 and $200; read 2026-10-21): https://claude.com/pricing
- Google, Google AI plans (Free, Plus $4.99, Pro $19.99, Ultra $99.99 to $199.99; read 2026-10-21): https://gemini.google/subscriptions/
- Krater, "ChatGPT Pricing 2026: Free, Go, Plus, Pro and Business Explained" (dated 3 October 2026; Go $5.50, Plus $20, Pro $100 to $200): https://krater.ai/blog/chatgpt-pricing ; OpenAI's own page: https://chatgpt.com/pricing
- Office Watch, "Microsoft 365 Plans in 2026" (Microsoft 365 Premium $19.99/month): https://office-watch.com/2026/microsoft-365-plans-overview/
