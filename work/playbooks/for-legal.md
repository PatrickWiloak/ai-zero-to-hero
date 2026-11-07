# AI for Legal Teams

**In one line:** Use AI to speed up first drafts, contract comparison, summarising and research triage, but treat every output as an unverified junior draft: you must check citations and facts yourself, protect client confidentiality, and follow your bar's rules.
**Last reviewed:** 2026-11-07

---

## The short version

- Good uses: summarising long documents, comparing a contract to your standard playbook, drafting routine clauses and plain-language explanations, organising discovery material, preparing deposition outlines.
- **Never file or send anything citing a case, statute or quote you have not opened yourself.** Models can produce convincing citations that do not exist. See [hallucinations](../../learn/concepts/hallucinations.md).
- **Confidentiality comes first.** Do not paste client or privileged material into a tool unless you know where the data goes, who can see it, and whether it is kept or used for training.
- Professional-conduct rules apply to lawyers who use these tools (competence, confidentiality, supervision, candour to the court). Read your own jurisdiction's bar guidance. The American Bar Association published formal ethics guidance on generative AI in July 2024; its page could not be fetched for this review, so read it directly and do not rely on this page for its content.
- This is a judgment guide for working with AI, not legal advice.

## Where it fits

| Task | AI helps with | You still own |
|---|---|---|
| Contract review | Flagging deviations from a playbook, summarising obligations | Risk calls, negotiation |
| Drafting | First drafts of routine clauses, letters, policies | Final wording and accuracy |
| Research | Finding leads and explaining a doctrine in plain English | Reading the primary source |
| Discovery | Grouping and summarising documents | Privilege calls, defensible process |
| Compliance | Mapping a regulation to controls as a checklist | Interpreting what applies to you |
| Client communication | Plain-language summaries | What is promised and advised |

## Copyable prompts

**Contract against a playbook** (use an approved, confidential-safe tool)
```
Here is our standard position on [clause types]: [paste playbook].
Here is the counterparty's contract: [paste].
For each clause in the playbook, quote the matching text, say whether it
matches, deviates or is missing, and rate the deviation low/medium/high
with one sentence why. Do not give advice beyond what is in the text.
```

**Research triage**
```
Explain the general legal question below in plain English and list the
kinds of authority I should look for. Do NOT cite specific cases or
statutes; I will find those in a legal database. Question: [question]
```

## A verification routine

1. Open every cited source in a legal database and confirm it says what the draft claims.
2. Check the quoted text word for word.
3. Confirm the authority is still good law.
4. Record which parts were AI-assisted, per your firm or department policy.

## Common mistakes

- Trusting a citation because it looks formatted correctly.
- Using a free consumer tool with client facts.
- Not telling a supervising attorney or client when the policy or engagement terms require it.
- Letting a tool "summarise" a contract and relying on the summary without reading the risky clauses.

## Next steps

- [Acceptable use policy](../enablement/acceptable-use-policy.md)
- [Document processing](../use-cases/document-processing.md)
- [Privacy and data protection with AI](../../safety/governance/privacy-and-data-protection-with-ai.md)

## Sources

- No page for the ABA guidance could be fetched on 2026-11-07 (HTTP 403). The claims about professional-conduct duties above are general and unverified here; check your jurisdiction's bar guidance.
