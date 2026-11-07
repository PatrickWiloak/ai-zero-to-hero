# AI for Finance Teams

**In one line:** Use AI to draft commentary, reconcile and explain variances, summarise contracts and filings, and speed up spreadsheet work, while keeping numbers in tools that calculate (not in a model's memory) and following the rules that already govern your records and customer data.
**Last reviewed:** 2026-11-07

---

## The short version

- **A language model is not a calculator.** Have it write the formula, the SQL or the Python, then run that. Do not accept a total it produced in prose.
- Strong uses: variance commentary, board-pack drafts, invoice and contract extraction, policy Q&A, formula help, forecasting scaffolding you then check.
- Financial records and customer financial data carry legal duties. Use approved tools only, and keep an audit trail of what was generated and who approved it.
- In regulated firms, existing rules still apply to AI. FINRA's Regulatory Notice 24-09 says its rules and the federal securities laws apply when member firms use generative AI, whether the tool is built in-house, bought, or embedded in existing software, and that the notice creates no new requirements. (read 2026-11-07)
- Judgment page: this is not accounting, tax or legal advice.

## Where it fits

| Task | AI helps with | You still own |
|---|---|---|
| Month-end | Variance explanations, journal descriptions, checklists | Posting, sign-off, controls |
| FP&A | Scenario scaffolding, commentary drafts, formula writing | Assumptions and the forecast |
| AP/AR | Extracting fields from invoices, drafting chase emails | Approvals and payment release |
| Audit support | Summarising evidence, mapping controls | Conclusions and judgment |
| Compliance | First-pass policy Q&A, reviewing marketing text against internal rules | Final compliance call |

## Copyable prompts

**Variance commentary** (give the numbers as a table you computed)
```
Here are actual vs budget by line for [period]: [table]. Write a 150-word
commentary for a non-finance executive. Use only these figures. For each
variance over [threshold] list the likely drivers as questions for the
budget owner; do not invent causes.
```

**Formula or script**
```
In a spreadsheet, column A is invoice date, B is amount, C is customer.
Write a formula that sums amounts per customer for the last calendar
quarter. Explain it in two sentences and give one test case I can check by
hand.
```

## Controls to keep

- Separate the person who generates from the person who approves.
- Keep prompts and outputs for anything that reaches a filing, a customer or an auditor.
- Never let an AI agent release a payment without a human approval step. See [agent security](../../safety/security/agent-security.md).
- Customer financial data: the US FTC's Safeguards Rule page says covered companies must run a formal information security program with administrative, technical and physical safeguards. (read 2026-11-07)

## Common mistakes

- Pasting a model's arithmetic into a report.
- Sending account-level customer data to an unapproved tool.
- Treating a forecast from a model as an analysis rather than a draft.

## Next steps

- [Document processing](../use-cases/document-processing.md) and [research and analysis](../use-cases/research-and-analysis.md)
- [Privacy and data protection with AI](../../safety/governance/privacy-and-data-protection-with-ai.md)

## Sources

- FINRA Regulatory Notice 24-09: https://www.finra.org/rules-guidance/notices/24-09 (fetched 2026-11-07)
- FTC, Gramm-Leach-Bliley Act business guidance: https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act (fetched 2026-11-07; page summary was short)
- CFPB, Circular 2022-03 (issued May 26, 2022): https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ (fetched 2026-11-07). It says ECOA and Regulation B "do not permit creditors to use complex algorithms when doing so means they cannot provide" accurate reasons for adverse action. Secondary summaries say the CFPB withdrew this circular on May 12, 2025 (90 Fed. Reg. 20084, not fetched); the statute and Regulation B still apply, so treat the circular as background and check its current status.
