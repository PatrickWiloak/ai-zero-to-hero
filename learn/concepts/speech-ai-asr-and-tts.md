# Speech AI: ASR and TTS

**In one line:** Understand how speech recognition (ASR, speech-to-text) and speech synthesis (TTS, text-to-speech) work, how to measure them (word error rate, latency, naturalness), which options exist as of 2026-10 from open Whisper to hosted and realtime APIs, and the mistakes that make voice features feel broken.
**Last reviewed:** 2026-10-21

---

> Assumes [LLM basics](llm-basics.md) and [Multimodal models](multimodal-models.md). To build something, go to [Build a voice agent](../../build/projects/voice-agent.md); this page is the theory and the choices behind it.

## The short version

- **ASR (automatic speech recognition)** turns audio into text. **TTS (text-to-speech)** turns text into audio. **Speech-to-speech** models do both inside one model and can reply without a text step in between.
- Modern ASR is a neural network that turns audio into a picture of its frequencies over time (a **spectrogram**) and decodes it into text, very like a language model with ears. OpenAI's **Whisper** (2022, open weights under MIT) made high-quality, multilingual ASR free to run anywhere.
- Measure ASR with **word error rate (WER)**: substitutions, deletions and insertions divided by the number of words actually spoken. Measure it on **your** audio (accents, jargon, phone lines, noise), because published WERs come from cleaner data.
- Modern TTS also uses language-model-style generation over **audio tokens**, which is why it now sounds human, can clone a voice from seconds of audio, and can be steered with instructions like "say this warmly".
- In live conversation, **latency** decides whether it feels natural. Stream everything, start speaking at the first sentence, and handle interruptions.
- Voice is personal data and voices can be cloned. Get consent, disclose synthetic voices, and never use a voice as the only proof of identity.

## How speech recognition works

Sound is air pressure changing over time, sampled (for speech, typically 16,000 times a second). Raw samples are a poor input for a model, so ASR first computes a **log-Mel spectrogram**: slice the audio into 25-millisecond windows, measure how much energy is in each frequency band (spaced the way human hearing perceives pitch), and stack those slices into an image of time by frequency. Vowels, consonants and silence have recognisable shapes in it.

A neural network then maps that image to text. The design Whisper uses is an **encoder-decoder transformer**: the encoder reads the whole spectrogram (in 30-second chunks), and the decoder writes text tokens one at a time while attending to the audio, exactly as a translation model writes French while attending to English. See [Transformer architecture](transformer-architecture.md).

What made Whisper a step change was data, not architecture. It was trained on 680,000 hours of audio paired with transcripts collected from the web, many of them imperfect ("weak supervision"), across many languages, with tasks like translation and timestamping mixed in. The result was a model that holds up across accents, background noise and topics far better than models trained on small, clean datasets, even if it is not the best on any one clean benchmark. The [Whisper summary](../../papers/multimodal/49-whisper/summary.md) tells that story.

Two consequences matter in practice:

- **It is a language model too**, so it uses context to guess unclear words. Usually that helps ("recognise speech" not "wreck a nice beach"). Sometimes it **hallucinates**: on silence, music or noise, Whisper-style models can produce fluent text nobody said, including repeated phrases. Trim silence with **voice activity detection (VAD)** before transcribing.
- **Vocabulary is a weak spot.** Product names, surnames, drug names and internal jargon get "corrected" into common words. Most hosted services let you pass a list of expected terms or a prompt with context; use it.

## Batch versus streaming

**Batch (pre-recorded)** transcription takes a whole file and returns the text. It can look ahead and back, so it is more accurate, and it is the right choice for meetings, calls after the fact, podcasts and subtitles.

**Streaming** transcription takes audio as it arrives and returns partial results within a few hundred milliseconds, revising them as more audio comes in. It is needed for live captions and voice agents. It must also decide when the speaker has **finished** (endpointing): too eager and it cuts people off mid-thought, too patient and the agent feels slow.

Other features you will meet: **diarisation** (who spoke when), **timestamps** per word, **language identification**, **punctuation and formatting** ("twenty five dollars" to "$25"), and **redaction** of personal data.

## Measuring ASR: word error rate

WER counts the fewest word edits needed to turn the transcript into the reference, divided by the number of reference words:

`WER = (substitutions + deletions + insertions) / words in the reference`

```python
def wer(reference: str, hypothesis: str) -> float:
    """Word error rate: (substitutions + deletions + insertions) / words in reference."""
    ref, hyp = reference.lower().split(), hypothesis.lower().split()
    # d[i][j] = edits to turn the first i reference words into the first j hypothesis words
    d = [[0] * (len(hyp) + 1) for _ in range(len(ref) + 1)]
    for i in range(len(ref) + 1):
        d[i][0] = i
    for j in range(len(hyp) + 1):
        d[0][j] = j
    for i in range(1, len(ref) + 1):
        for j in range(1, len(hyp) + 1):
            same = ref[i - 1] == hyp[j - 1]
            d[i][j] = min(d[i - 1][j] + 1,                       # deletion
                          d[i][j - 1] + 1,                       # insertion
                          d[i - 1][j - 1] + (0 if same else 1))  # substitution or match
    return d[-1][-1] / len(ref)

ref = "please transfer five hundred dollars to account ending four two"
print(wer(ref, "please transfer five hundred dollars to account ending four two"))   # 0.0
print(wer(ref, "please transfer nine hundred dollars to the account ending for two"))  # 0.3
```

The second transcript has a 30% WER (two substitutions and one insertion over ten words). Notice that WER treats all errors alike: "the" inserted is harmless, "nine" for "five" moves $400. For your application, also track the errors that matter (numbers, names, negations like "can" versus "can't") separately. And normalise both texts the same way (case, punctuation, numerals) before scoring, or you will measure formatting rather than recognition; the open-source `jiwer` package and Whisper's own text normaliser help.

## How speech synthesis works

Classic TTS stitched together recorded fragments or used hand-built vocal models, and sounded robotic. Neural TTS works in two steps: a model turns text (and often phonemes) into an acoustic representation, and a **vocoder** turns that into a waveform.

The modern twist mirrors LLMs. A **neural audio codec** compresses audio into a sequence of discrete tokens, and a language model learns to generate those tokens from text, the way an LLM generates words. That is why current TTS can continue a voice from a short sample (**zero-shot voice cloning**), carry emotion and emphasis, and follow natural-language style instructions. The [VALL-E summary](../../papers/multimodal/122-vall-e/summary.md) and [AudioLM summary](../../papers/multimodal/121-audiolm/summary.md) explain the approach.

How TTS is judged:

- **Naturalness**, usually by people rating samples (mean opinion score, MOS, on a 1 to 5 scale) or by side-by-side preference tests.
- **Intelligibility**, often measured by transcribing the output with ASR and computing WER against the input text.
- **Speaker similarity** for cloned voices.
- **Time to first audio** for live use: how long before the first sound plays.

## Speech-to-speech and realtime models

The cascade (ASR, then an LLM, then TTS) is simple, debuggable and lets you swap any part, but each stage adds delay and the text step drops tone of voice. **Speech-to-speech** models take audio in and produce audio out directly, can be interrupted naturally, and keep paralinguistic cues (hesitation, emphasis, laughter). As of 2026-10, OpenAI's Realtime API and Google's Gemini Live API both offer this over persistent WebRTC or WebSocket connections with tool calling. The trade-offs are less control over exactly what is said, harder logging and evaluation, and higher cost per minute. [Build a voice agent](../../build/projects/voice-agent.md) compares the two architectures in detail.

## Options as of 2026-10-21

Products in this space change fast; OpenAI alone has announced shutdowns of several speech models it launched in 2024 and 2025. Check each provider's page before you build.

| Need | Open / self-hosted | Hosted examples |
|---|---|---|
| ASR, batch | Whisper (sizes from 39M "tiny" to 1.55B "large", plus an 809M "turbo"; MIT licence); faster-whisper for speed | OpenAI `gpt-transcribe`; Deepgram Nova-3; AssemblyAI Universal models; cloud speech services |
| ASR, streaming | Whisper variants with chunking and VAD (harder to get right) | Deepgram, AssemblyAI streaming models, cloud speech services |
| TTS | Kokoro-82M (Apache 2.0), other open models on Hugging Face | ElevenLabs (`eleven_v4` family and flash models built for low latency); OpenAI voice via its Realtime API; cloud speech services |
| Speech-to-speech | Emerging open models; mostly research-grade | OpenAI Realtime API (`gpt-realtime-2.1`); Gemini Live API |

For the cloud services (Amazon Transcribe and Polly, Azure AI Speech, Google Cloud Speech), see the speech section of [Cloud AI/ML services compared](../../tools/comparisons/cloud-ai-ml-services.md).

How to choose: run 30 to 60 minutes of **your own** audio through two or three candidates, compute WER on a hand-corrected transcript, listen to where they fail, and check cost per audio minute and latency. Vendor-reported WERs are measured on their own test sets and are not comparable across vendors.

## Common mistakes

- **Trusting a benchmark WER.** A 5% WER on read audiobooks can be 20% on a noisy call-centre line with accents and jargon.
- **Transcribing silence.** Without VAD, models invent text on silent or music-only stretches.
- **Waiting for the full reply before speaking.** Stream the LLM output and send it to TTS sentence by sentence.
- **Reading out formatting.** Markdown, URLs and bullet characters sound terrible spoken. Ask the LLM for speech-friendly text.
- **No barge-in.** People interrupt. If the agent keeps talking, it feels broken.
- **Cloning voices without consent**, or using voice alone to authenticate someone. Voice cloning makes both a fraud risk. Disclose when a caller is talking to a synthetic voice, and check local law on recording consent.

## Next steps

- [Build a voice agent](../../build/projects/voice-agent.md): the cascade in about 80 lines, with a latency budget
- [Multimodal models](multimodal-models.md): audio as one input among several
- [Meetings and summaries](../../work/use-cases/meetings-and-summaries.md): the most common ASR use at work
- Papers: [Whisper](../../papers/multimodal/49-whisper/summary.md), [VALL-E](../../papers/multimodal/122-vall-e/summary.md), [AudioLM](../../papers/multimodal/121-audiolm/summary.md), [GPT-4o](../../papers/language-models/40-gpt4o/summary.md) (native audio)

## Sources

- Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (2022), 680,000 hours: https://arxiv.org/abs/2212.04356
- OpenAI Whisper repository (model sizes, MIT licence): https://github.com/openai/whisper
- OpenAI, speech-to-text guide (current model and deprecation dates), read 2026-10-21: https://developers.openai.com/api/docs/guides/speech-to-text
- OpenAI, text-to-speech guide (deprecations, migration to Realtime), read 2026-10-21: https://developers.openai.com/api/docs/guides/text-to-speech
- OpenAI, Realtime API guide: https://developers.openai.com/api/docs/guides/realtime
- Google, Gemini Live API: https://ai.google.dev/gemini-api/docs/live
- Deepgram, "Introducing Nova-3" (2025-02-12): https://deepgram.com/learn/introducing-nova-3-speech-to-text-api
- AssemblyAI, models overview: https://www.assemblyai.com/docs/getting-started/models
- ElevenLabs, models overview: https://elevenlabs.io/docs/overview/models
- Kokoro-82M model card: https://huggingface.co/hexgrad/Kokoro-82M
- Word error rate definition: https://en.wikipedia.org/wiki/Word_error_rate
- WER function above run on 2026-10-21 (outputs shown).
