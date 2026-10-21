---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 10 min
---

# 03 Text, Speech and Vision in Foundry

Part of Domain 2, **Implement AI solutions by using Microsoft Foundry (55-60%)**: text analysis apps, speech apps, spoken prompts to a multimodal model, visual input, image generation and vision apps.

The recurring exam decision in this note: **a deployed multimodal model, or a specialised Foundry Tool?**

| Use a multimodal model when | Use a specialised Foundry Tool when |
|---|---|
| The task is open-ended (describe, answer questions, reason about the content) | You need a specific, well-defined output at scale (sentiment scores, entities, word-level timestamps, OCR coordinates) |
| You want one call to understand text, images or audio together | You need features the model does not offer: real-time streaming transcription, custom neural voices, SSML, speaker diarisation |
| Prototyping fast | Cost, latency, consistency and predictable output schemas matter |

## Text analysis apps

Two ways to analyse text in Foundry:

1. **Azure Language in Foundry Tools**: prebuilt endpoints for sentiment analysis and opinion mining, key phrase extraction, named entity recognition, PII detection, language detection and summarisation. Output is structured JSON with confidence scores. Deterministic per input, cheap at volume.
2. **A deployed language model** with a prompt: "Return JSON with the sentiment (positive/negative/neutral) and the three main complaints in this review." Flexible, handles nuance and custom categories, but costs per token and needs [structured outputs](../../../../learn/concepts/structured-outputs.md) or careful prompting for consistent format.

A "lightweight application that includes text analysis" in the skills outline means: read input text, call either option with the project's endpoint and credential, and use the result (for example route negative reviews to a human).

Know the difference between **extractive** summarisation (selects sentences from the text) and **abstractive** summarisation (writes new sentences), and between **sentiment** (overall feeling) and **opinion mining** (feeling about each aspect).

## Speech apps

**Azure Speech in Foundry Tools** covers:

| Capability | What it does | Typical use |
|---|---|---|
| Speech to text (real-time) | Streams audio, returns text as you speak | Live captions, voice commands |
| Speech to text (batch / fast transcription) | Transcribes recorded files | Call recordings, meetings |
| Text to speech | Neural voices; control with **SSML** (Speech Synthesis Markup Language) for pronunciation, pauses, emphasis, speaking style | Read-aloud, IVR, accessibility |
| Speech translation | Recognise and translate speech | Multilingual meetings |
| Custom speech / custom voice | Adapt recognition to your vocabulary; build a brand voice (with consent requirements) | Domain jargon, brand assistant |

Concepts: **diarisation** (who spoke when), **custom vocabulary / phrase lists** for names and jargon, **word error rate** as the quality measure. See [Speech AI: ASR and TTS](../../../../learn/concepts/speech-ai-asr-and-tts.md).

**Responding to spoken prompts with a deployed multimodal model**: an audio-capable model takes the spoken question directly as audio input and returns text (or audio). This skips a separate transcription step and keeps tone of voice; choose it for conversational assistants. Choose Azure Speech when you need the specific speech features above.

## Visual input in prompts

A vision-capable deployed model accepts images in the prompt alongside text: "What is wrong with this wiring?", "Summarise this chart", "Which product is on the shelf?". In code, the image is sent as an input item (a URL or base64 data) in the same request as the text. Use it for open-ended understanding; image quality, resolution and a specific question all improve results. See [Multimodal models](../../../../learn/concepts/multimodal-models.md).

## Image generation

Image-generation models in the Foundry catalog create images from text prompts (and some edit images). Exam points:

- Prompts should describe subject, style, composition and details; iterate.
- **Content filters** apply to both prompts and generated images; some requests are refused.
- Generated images can carry **content credentials** (provenance metadata) indicating they are AI-generated, which supports the transparency principle.
- Responsible use: avoid generating real people, trademarks or misleading imagery.

## Vision apps with Azure Vision

**Azure Vision in Foundry Tools** provides prebuilt image analysis: captions, dense captions, tags, object detection (with bounding boxes), people detection, smart cropping and **OCR** ("Read") for printed and handwritten text. Choose it for predictable, structured output at volume (for example, tagging a photo library or reading text from street signs). For structured fields from documents and forms, use Content Understanding ([note 04](04-information-extraction.md)).

Terminology:

- **Image classification** assigns a label to the whole image.
- **Object detection** finds each object and its location (bounding box).
- **Semantic segmentation** labels every pixel.
- **OCR** turns text in an image into machine-readable text.
- **Face** detection is available, but identification and verification are **limited access** under Microsoft's responsible AI policy.

## Check yourself

1. You need live captions for a webinar. Which capability? *(Azure Speech, real-time speech to text.)*
2. You need to control how a product name is pronounced in synthesised speech. *(SSML.)*
3. A user photographs an error on a machine and asks what to do. *(A vision-capable multimodal model with the image in the prompt.)*
4. You need sentiment scores for one million reviews a day, cheaply and consistently. *(Azure Language sentiment analysis.)*
5. Which capability finds and locates every car in a traffic image? *(Object detection.)*

## Sources

- [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
- [Get started with AI applications and agents on Azure](https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/) (modules on text analysis, speech and computer vision)
- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) (Foundry Tools naming)
