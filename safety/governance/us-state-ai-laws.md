# US State AI Laws

**In one line:** There is no single US AI law; states are passing their own, with Colorado's high-risk AI act the broadest, so list which states your users and decisions touch and check each state's current text before you rely on any date on this page.
**Last reviewed:** 2026-11-07

---

> **As of 2026-11-07, from the pages read for this review.** This is a map, not legal advice. State AI law changes fast, bills get amended and dates get delayed. Confirm every date on the official legislature or attorney general site.

## The short version

- The National Conference of State Legislatures (NCSL) reported, on a page updated July 10, 2025, that in the 2025 session all 50 states, Puerto Rico, the US Virgin Islands and Washington, D.C. introduced AI-related legislation, and 38 states adopted or enacted about 100 measures.
- The biggest compliance question for most businesses is **"consequential decisions"** (hiring, lending, housing, health care, education, insurance) made or shaped by AI, because that is where laws like Colorado's apply.
- Many state laws also cover **disclosure** (telling people they are dealing with AI), **deepfakes and intimate imagery**, **government use**, and **chatbots**.
- Building a general AI governance program ([ISO 42001](iso-42001.md), [NIST AI RMF](nist-ai-rmf.md)) is the cheapest way to meet several state laws at once. Colorado's act includes an affirmative defence for following a recognised AI risk management framework and taking steps to find and fix violations (per its legislature page).

## What was read, state by state

| State | What the official page said | Not verified |
|---|---|---|
| **Colorado** (SB24-205, Consumer Protections for AI) | Signed May 17, 2024. The legislature page lists developer and deployer duties for high-risk AI systems beginning **February 1, 2026**. Developers owe deployers documentation and a public summary and must report known discrimination risks to the attorney general and known deployers within 90 days. Deployers must keep a risk management program, complete impact assessments, review annually, notify consumers of consequential decisions, allow correction and appeal with human review where technically feasible, and report discovered discrimination to the attorney general. Anyone deploying a consumer-facing AI system must make sure consumers are told they are interacting with AI. The attorney general has exclusive enforcement authority and rulemaking; violations are deceptive trade practices. | The page showed no change to the February 1, 2026 date, but it reflects the act as enacted and lists nine amendments. Check the legislature site for any later delay. NCSL's 2025 table also lists Colorado S 318 (AI consumer protections) as failed after adjournment |
| **Texas** (HB 149, Texas Responsible Artificial Intelligence Governance Act) | The legislature page shows it signed by the Governor on June 22, 2025 and takes effect **January 1, 2026**; the caption says it regulates AI systems and provides civil penalties; it names the Attorney General and a proposed Texas Artificial Intelligence Council | Specific requirements; the page gave only caption and subjects |
| **Utah** (SB 149, AI Amendments) | Governor signed March 13, 2024 | Disclosure rules and effective date; the page did not include the text |
| **California** | NCSL's 2025 table showed many AI bills still pending then, including A 1018 (automated decision systems), S 243 (companion chatbots) and S 53 (CalCompute). The Attorney General's CCPA page describes the privacy law and its regulations (effective March 29, 2023) and did not mention automated decision-making or risk assessments | Whether those bills passed, and the current status of automated decision rules. SB 53's page returned HTTP 403 |
| **New York** | NCSL listed a 2025 measure requiring state agencies to publish an inventory of automated decision-making tools | NYC's hiring-tool bias audit law: its page was unreachable |

## How to handle it as a business

1. **Map exposure**: where are your users and the people your system makes decisions about?
2. **Classify use**: does any AI output feed a consequential decision? If yes, treat it as high risk.
3. **Build the common core once**: inventory, risk assessment, impact assessment, human review and appeal path, user disclosure, testing for discrimination, incident reporting. See [AI risk assessment](ai-risk-assessment.md) and [bias and fairness testing](bias-and-fairness-testing.md).
4. **Add state-specific items** from counsel's review.
5. **Calendar a review** every quarter. Laws and dates move.

## Common mistakes

- Quoting an effective date from a news article instead of the statute.
- Assuming a vendor's compliance covers your use.
- Ignoring disclosure duties for chatbots.
- Treating the federal picture as settled; this page did not research federal law.

## Next steps

- [EU AI Act compliance](eu-ai-act-compliance.md) for the other big regime
- [AI governance program](ai-governance-program.md)
- [Privacy and data protection with AI](privacy-and-data-protection-with-ai.md)

## Sources

- Colorado General Assembly, SB24-205: https://leg.colorado.gov/bills/sb24-205 (fetched 2026-11-07)
- Texas Legislature Online, HB 149 (89R): https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149 (fetched 2026-11-07)
- Utah Legislature, SB 149 (2024): https://le.utah.gov/~2024/bills/static/SB0149.html (fetched 2026-11-07)
- NCSL, AI 2025 legislation: https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation (fetched 2026-11-07, first 100,000 characters; page dated July 10, 2025)
- California Attorney General, CCPA: https://oag.ca.gov/privacy/ccpa (fetched 2026-11-07)
