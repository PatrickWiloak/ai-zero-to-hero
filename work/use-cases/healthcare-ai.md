# AI in Healthcare

**In one line:** Healthcare AI splits into administrative uses (notes, coding, scheduling, patient messages) and clinical uses (diagnosis, triage, treatment), and the second group can be a regulated medical device, so know which one you are building or buying before you start.
**Last reviewed:** 2026-11-07

---

> Not legal or medical advice. Rules differ by country and change; check with your compliance and legal teams.

## The short version

- **Administrative AI** (drafting visit notes, summarising charts, prior-authorisation paperwork, call-centre assistants) has lower risk, but still handles protected health information, so privacy law and contracts decide which tools you may use.
- **Clinical AI** that diagnoses, treats or drives care decisions can be regulated as a medical device. In the US, the Food and Drug Administration (FDA) regulates AI-enabled devices as medical devices, not as "AI", using a risk-based approach across the product lifecycle. (FDA page, read 2026-11-07)
- Software counts as a device unless it falls under an exclusion in section 520(o) of the FD&C Act. Devices reach the US market through 510(k), De Novo or premarket approval (PMA). (FDA page)
- The FDA's page reported over 1,600 AI-enabled devices authorised for US marketing as of September 2026 and keeps a searchable list. (FDA page)
- A human clinician stays accountable. Design the tool so a clinician reviews anything that affects care.

## The two lanes

| | Administrative | Clinical |
|---|---|---|
| Examples | Ambient note drafts, coding suggestions, inbox triage, scheduling | Image analysis, risk scores, insulin dosing, triage |
| Main risks | Privacy, hallucinated details in the record | Patient harm, bias across populations, drift |
| Regulatory question | Is the vendor allowed to handle PHI (in the US, usually a HIPAA business associate agreement)? | Is the function a regulated device? |
| Evidence you need | Accuracy on your real notes, clinician sign-off rate | Clinical validation and monitoring |

## How change control works (predetermined change control plans)

The FDA page says a marketing submission can include AI-enabled software functions together with a predetermined change control plan (PCCP), and links final FDA guidance on PCCP recommendations. The page does not describe the plan contents in detail, so read the guidance itself. The idea: say up front how the model may be updated, so you do not need a new submission for every retrain.

## Practical steps

1. Classify the use: administrative or clinical, and say why.
2. For administrative tools, confirm contracts and data handling. HHS HIPAA pages returned HTTP 403 during this review, so read them directly at hhs.gov/hipaa; this page does not summarise them.
3. For clinical tools, ask the vendor for their regulatory status and the evidence on populations like yours.
4. Pilot with clinician review and measure errors, not just time saved. See [set up an eval harness](../../build/projects/set-up-eval-harness.md).
5. Monitor after launch for drift and complaints. See [AI incident response](../../safety/security/ai-incident-response.md).

## Common mistakes

- Treating a clinical-sounding feature as "just a chatbot".
- Using a consumer chatbot with patient details.
- Measuring only time saved, not note errors.
- Testing only on the majority population. See [bias and fairness testing](../../safety/governance/bias-and-fairness-testing.md).

## Next steps

- [Privacy and data protection with AI](../../safety/governance/privacy-and-data-protection-with-ai.md)
- [Meetings and summaries](meetings-and-summaries.md), [document processing](document-processing.md)
- [AI risk assessment](../../safety/governance/ai-risk-assessment.md)

## Sources

- FDA, Artificial Intelligence in Software as a Medical Device: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device (fetched 2026-11-07)
- HHS HIPAA pages: attempted, HTTP 403, not cited.
