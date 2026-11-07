# Deepfakes and Synthetic Media

**In one line:** Assume anyone can now fake a voice, face or document cheaply, so protect yourself with verification habits (call back, code words, second approvers) rather than hoping to spot fakes by eye, and label and log the synthetic media you make.
**Last reviewed:** 2026-11-07

---

> Judgment guide, not legal advice. Laws on synthetic media are changing and differ by place.

## The short version

- **Detection by eye or ear is not reliable.** Use process: verify out-of-band, require two approvals for money moves, and agree a verification phrase with executives and family.
- **Provenance helps but is partial.** C2PA is an open standards effort, a project of the Joint Development Foundation that combined the Content Authenticity Initiative and Project Origin, building specifications for content provenance (C2PA About page, read 2026-11-07). Google's Gemini image docs state that all generated images include a SynthID watermark. Metadata can be stripped and not all generators mark output, so absence of a label proves nothing.
- **Impersonation is already regulated.** The US FTC's rule on impersonation of government and businesses took effect April 1, 2024; the release links a proposal to extend protections to impersonating individuals (comments were due April 30, 2024). Whether that extension was finalised was not checked. (FTC release, read 2026-11-07)
- **Intimate synthetic imagery is a focus of new laws.** NCSL's 2025 table lists Colorado S 288 on intimate digital depictions as enacted. The federal TAKE IT DOWN Act (Public Law 119-12, approved May 19, 2025) makes it a crime to knowingly publish nonconsensual intimate images, including digital forgeries, and requires covered platforms to set up a notice process within one year of enactment and remove a depiction within 48 hours of a valid request; the FTC enforces the platform duties (GovInfo, read 2026-11-07).
- If you **make** synthetic media: get consent for anyone's likeness or voice, disclose it, and keep records. OpenAI's text-to-speech guide says its usage policies require telling users the voice is AI-generated, and that custom voices need a consent recording. (read 2026-11-07)

## Common threat scenarios

| Scenario | Defence |
|---|---|
| Cloned voice of an executive asks finance for an urgent transfer | Call back on a known number; two approvers; no urgent exceptions |
| Fake video call with a "colleague" | Verification phrase; confirm on a separate channel |
| Fake job candidate or identity documents | Live checks, document verification services, reference checks |
| Fake news image about your company | Monitoring, a rapid-response page, provenance on your own media |
| Intimate image abuse | Platform takedown channels, legal help, support for the victim |
| Voice cloning of family members for scams | Family code word; hang up and call back |

## Controls for organisations

1. **Money and data requests** need out-of-band verification regardless of how convincing the person sounds.
2. **Train staff** with real examples and a no-blame way to report.
3. **Adopt provenance** for your own published media (C2PA tools, vendor watermarks) and record which model made what.
4. **Set a policy** on synthetic spokespeople, voices and likenesses: consent, disclosure, approval, retention.
5. **Plan the response** to a fake about you. See [AI incident response](ai-incident-response.md).
6. **Check vendor safeguards** when you choose generation tools. See [image and video generation compared](../../tools/comparisons/image-and-video-generation.md) and [speech providers compared](../../tools/comparisons/speech-asr-tts-providers.md).

## Common mistakes

- Relying on a "deepfake detector" score as proof.
- Believing a watermark's absence means authentic.
- Using a real person's voice or face without written consent.
- Forgetting that scams use ordinary phone calls, not just video.

## Next steps

- [AI threat modeling](ai-threat-modeling.md)
- [Responsible AI basics](../governance/responsible-ai-basics.md)
- [US state AI laws](../governance/us-state-ai-laws.md)

## Sources

- C2PA, About: https://c2pa.org/about/ (fetched 2026-11-07)
- Google AI Studio docs, image generation (SynthID statement): https://aistudio.google.com/docs/image-generation (fetched 2026-11-07)
- FTC, impersonation rule takes effect: https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-announces-impersonation-rule-goes-effect-today (fetched 2026-11-07)
- TAKE IT DOWN Act, Public Law 119-12 (GovInfo): https://www.govinfo.gov/content/pkg/PLAW-119publ12/html/PLAW-119publ12.htm (fetched 2026-11-07)
- NCSL, AI 2025 legislation: https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation (fetched 2026-11-07)
- OpenAI text-to-speech guide: https://developers.openai.com/api/docs/guides/text-to-speech (fetched 2026-11-07)
