# US State AI Laws

**In one line:** There is no single US AI law; states are passing their own, with Colorado's automated decision-making act (SB26-189) among the broadest, so list which states your users and decisions touch and check each state's current text before you rely on any date on this page.
**Last reviewed:** 2026-11-07

---

> **As of 2026-11-07, from the pages read for this review.** This is a map, not legal advice. State AI law changes fast, bills get amended and dates get delayed. Confirm every date on the official legislature or attorney general site.

## The short version

- The National Conference of State Legislatures (NCSL) reported, on a page updated July 10, 2025, that in the 2025 session all 50 states, Puerto Rico, the US Virgin Islands and Washington, D.C. introduced AI-related legislation, and 38 states adopted or enacted about 100 measures.
- The biggest compliance question for most businesses is **"consequential decisions"** (hiring, lending, housing, health care, education, insurance) made or shaped by AI, because that is where laws like Colorado's SB26-189 apply.
- Many state laws also cover **disclosure** (telling people they are dealing with AI), **deepfakes and intimate imagery**, **government use**, and **chatbots**.
- Building a general AI governance program ([ISO 42001](iso-42001.md), [NIST AI RMF](nist-ai-rmf.md)) is the cheapest way to meet several state laws at once. Colorado's original SB24-205 included an affirmative defence for following a recognised framework; it was repealed and replaced in 2026, so check whether the new act keeps one.

## What was read, state by state

| State | What the official page said | Not verified |
|---|---|---|
| **Colorado** (SB24-205, repealed and reenacted by SB26-189, Automated Decision-Making Technology) | SB24-205 was signed May 17, 2024 with duties from February 1, 2026. The 2026 session then repealed and reenacted it as SB26-189, signed May 14, 2026 (Chapter 131). The enacted text says the act takes effect January 1, 2027 (a few sections, including the effective-date clause, take effect on passage) and applies to consequential decisions made on or after January 1, 2027. The new act covers automated decision-making technology in consequential decisions (education, employment, housing, financial services, insurance, health care, essential government services). Developers give deployers technical documentation starting January 1, 2027, and the attorney general must adopt rules on or before January 1, 2027; deployers give consumers notice and, after an adverse outcome, a plain-language explanation of the technology's role; consumers gain rights to access, correct and request meaningful human review. The attorney general enforces under the Colorado Consumer Protection Act and, where a cure is deemed possible, must first issue a notice of violation; the developer or deployer then has 60 days to cure. No cure period is required for a knowing or repeated violation, and the cure subsection is repealed effective January 1, 2030. | The detailed duty lists in the enacted text were not read line by line. Earlier duty lists for SB24-205 (impact assessments, risk management program, affirmative defence) no longer describe current law |
| **Texas** (HB 149, Texas Responsible Artificial Intelligence Governance Act) | The legislature page shows it signed by the Governor on June 22, 2025 and takes effect **January 1, 2026**; the caption says it regulates AI systems and provides civil penalties; it names the Attorney General and a proposed Texas Artificial Intelligence Council | Specific requirements; the page gave only caption and subjects |
| **Utah** (SB 149, AI Amendments) | Governor signed March 13, 2024 | Disclosure rules and effective date; the page did not include the text |
| **California** | SB 53 (Transparency in Frontier Artificial Intelligence Act) was signed September 29, 2025 (Governor's press release: large frontier developers must publish a framework on their website, there is a mechanism to report critical safety incidents to the Office of Emergency Services, whistleblowers are protected, and the Attorney General enforces civil penalties; the release gives no effective date). A January 1, 2026 effective date comes from secondary summaries, and SB 243 (companion chatbots) was signed in October 2025 with main provisions effective January 1, 2026 (per EPIC and law-firm summaries, not the statute; leginfo returned HTTP 403, including in a browser). NCSL's 2025 table showed many AI bills still pending then, including A 1018 (automated decision systems), S 243 (companion chatbots) and S 53 (CalCompute). The Attorney General's CCPA page describes the privacy law and its regulations (effective March 29, 2023) and did not mention automated decision-making or risk assessments | Statute text and effective dates for SB 53 and SB 243 (leginfo returned HTTP 403), and the current status of automated decision rules |
| **New York** | NCSL listed a 2025 measure requiring state agencies to publish an inventory of automated decision-making tools. For New York City, the Department of Consumer and Worker Protection (DCWP) page says Local Law 144 of 2021 lets employers and employment agencies use an automated employment decision tool only if a bias audit was completed within one year before use, information about the audit is publicly available, and the required notices were given (10 business days before use, per DCWP's June 2023 clarification). DCWP began enforcing on July 5, 2023 | Rules for the other states' hiring tools and any 2026 New York State action |

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
- Colorado General Assembly, SB26-189: https://leg.colorado.gov/bills/sb26-189 (fetched 2026-11-07)
- EPIC, California tech legislation roundup: https://epic.org/california-tech-legislation-roundup-numerous-privacy-and-ai-laws-enacted-and-six-vetoed/ (secondary, 2026-11-07)
- Texas Legislature Online, HB 149 (89R): https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149 (fetched 2026-11-07)
- Colorado General Assembly, SB26-189 session law (Chapter 131): https://leg.colorado.gov/laws/session-laws/SB26-189/131/download (read 2026-11-07)
- Office of the Governor of California, SB 53 signing: https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/ (fetched 2026-11-07)
- NYC Department of Consumer and Worker Protection, automated employment decision tools: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page (fetched 2026-11-07)
- Utah Legislature, SB 149 (2024): https://le.utah.gov/~2024/bills/static/SB0149.html (fetched 2026-11-07)
- NCSL, AI 2025 legislation: https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation (fetched 2026-11-07, first 100,000 characters; page dated July 10, 2025)
- California Attorney General, CCPA: https://oag.ca.gov/privacy/ccpa (fetched 2026-11-07)
