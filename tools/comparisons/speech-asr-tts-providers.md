# Speech Providers Compared (ASR and TTS)

**In one line:** For speech-to-text and text-to-speech, choose between a hosted API (OpenAI, Deepgram, AssemblyAI, ElevenLabs) and running Whisper yourself by looking at streaming latency, diarization, domain vocabulary, language coverage and how long the model will exist.
**Last reviewed:** 2026-11-07

---

## The short version

- **ASR** (automatic speech recognition) turns audio into text. **TTS** (text to speech) does the reverse. Concepts are in [speech AI: ASR and TTS](../../learn/concepts/speech-ai-asr-and-tts.md).
- Decide: **batch or live?** Meeting transcripts can be batch. Voice agents need streaming with fast end-of-turn detection.
- Test with your own audio: accents, phone quality, jargon. Vendor claims do not transfer.
- Model lifecycles are short. OpenAI's pages announce shutdown dates for several speech models, so build behind an interface you can swap.
- No prices are given here; none were read. Check each vendor.

## Facts from vendor pages (as of 2026-11-07)

| Provider | Speech-to-text | Text-to-speech | Notes |
|---|---|---|---|
| **OpenAI** | `gpt-transcribe` recommended for recorded speech, with `prompt`, `keywords`, `languages` hints; 25 MB file limit; formats mp3, mp4, mpeg, mpga, m4a, wav, webm; `whisper-1`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` and the diarize model are deprecated, shutting down February 26, 2027 | `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd` deprecated, shutting down January 6, 2027; replacement uses the Realtime API; 13 built-in voices; custom voices need a consent recording | Usage policies require telling users the voice is AI-generated |
| **Deepgram** | Flux (streaming, built-in end-of-turn detection, English and 10 languages), Nova-3 (general, with medical and pharma English variants), Nova-2; hosted Whisper | Not covered on the page read | Concurrency caps apply to hosted Whisper (15 paid, 5 pay-as-you-go) |
| **AssemblyAI** | Pre-recorded API (99 languages, diarization, PII redaction), streaming over WebSocket (about 150 ms p50), synchronous API for audio up to 20 minutes | Not covered | Model names not on the page read |
| **ElevenLabs** | Scribe v2 (batch, word timestamps, diarization, 90+ languages), Scribe v2 Realtime (about 150 ms), Scribe v2 Medical | Eleven v4, v4 Turbo (about 100 ms median), v3, Multilingual v2, Flash v2.5 (about 100 ms, 40,000-character limit) | Latency figures are medians that exclude app and network latency |
| **Whisper (open source)** | MIT licence for code and weights; sizes tiny (39M parameters) to large (1550M) plus turbo (809M); runs locally with `pip install -U openai-whisper` and ffmpeg | n/a | Turbo is not trained for translation |

## Choosing

| Need | Lean toward |
|---|---|
| Private, offline, no per-minute fee | Whisper locally (check your hardware: the repo lists about 10 GB VRAM for large) |
| Live voice agent | A streaming model with end-of-turn detection (Deepgram Flux, ElevenLabs realtime, or OpenAI Realtime) |
| Medical dictation | A vendor with a medical variant (Deepgram Nova-3 Medical, ElevenLabs Scribe v2 Medical); validate on your clinicians |
| Many speakers, call analytics | Diarization and PII redaction (AssemblyAI lists both) |
| Expressive narration | A TTS family built for it (ElevenLabs v3 or v4 per its page) |

## How to run a bake-off

1. Collect 30 to 50 representative clips with human-checked transcripts.
2. Score word error rate on each provider, per accent and noise condition.
3. Time the first partial result for streaming.
4. Check data handling terms and retention.
5. Re-run every few months, since models change.

## Common mistakes

- Comparing providers on clean studio audio only.
- Ignoring diarization needs until the product is built.
- Cloning a real person's voice without consent. See [deepfakes and synthetic media](../../safety/security/deepfakes-and-synthetic-media.md).
- Hardcoding a model name that has a shutdown date.

## Next steps

- [Build a voice agent](../../build/projects/voice-agent.md)
- [Local LLM runners compared](local-llm-runners.md)

## Sources

- OpenAI speech-to-text and text-to-speech guides: https://developers.openai.com/api/docs/guides/speech-to-text and /text-to-speech (fetched 2026-11-07)
- Deepgram models overview: https://developers.deepgram.com/docs/models-languages-overview (fetched 2026-11-07)
- ElevenLabs models: https://elevenlabs.io/docs/overview/models (fetched 2026-11-07)
- AssemblyAI docs: https://www.assemblyai.com/docs (fetched 2026-11-07)
- OpenAI Whisper repository: https://github.com/openai/whisper (fetched 2026-11-07)
