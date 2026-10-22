---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 20 min
---

# 04 Text Analysis, Translation and Speech

Domain 4 of AI-103: **Implement text analysis solutions (10-15%)**. Two skill groups: language-model text analysis (extraction, sentiment and safety, translation, domain customisation) and speech (speech to text and back, speech as an agent modality, audio reasoning, speech translation).

The recurring question in this domain is **"a model prompt or a Foundry Tool?"** Both can extract entities, detect sentiment and translate. The exam rewards knowing when each is the better answer, so this page keeps coming back to the trade-off.

## Two ways to analyse text

**Generative prompting** uses a deployed language model with instructions and, ideally, a JSON Schema for the output. Strengths: handles any schema you can describe, understands context and nuance, adapts to new tasks without training, follows domain instructions ("summarise for a compliance officer, quoting clause numbers"). Weaknesses: cost per token, variable output unless constrained, possible fabrication, and no built-in confidence scores.

**Foundry Tools** (Azure Language, Azure Translator, Azure AI Content Safety) are purpose-built services with fixed capabilities: named entity recognition, key phrase extraction, PII detection and redaction, sentiment with opinion mining, summarisation, language detection, translation. Strengths: consistent categories, confidence scores and offsets, predictable cost, compliance-friendly behaviour (PII categories mapped to regulations), low latency. Weaknesses: you get the categories the service defines; customising means training custom models.

A rule that answers most questions: **if the requirement names a fixed, standard output (PII categories, sentiment labels with scores, character offsets for redaction, 100+ languages at scale), choose the Foundry Tool; if it needs a custom schema, reasoning or a domain-specific style, choose a model with structured output.** Many production systems use both: the tool for the regulated, consistent part, the model for the open-ended part.

## Extracting entities, topics, summaries and structured JSON

### With a model and structured output

Asking a model for "JSON" in prose is fragile. Supplying a **JSON Schema** as the response format makes the output conform:

```python
response = openai.responses.create(
    model="gpt-5-mini",
    instructions=("Extract the fields from the support ticket. "
                  "Use null when a value is not stated. Do not infer."),
    input=ticket_text,
    text={
        "format": {
            "type": "json_schema",
            "name": "ticket",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "product": {"type": ["string", "null"]},
                    "topics": {"type": "array", "items": {"type": "string"}},
                    "urgency": {"type": "string", "enum": ["low", "medium", "high"]},
                    "summary": {"type": "string"},
                },
                "required": ["product", "topics", "urgency", "summary"],
                "additionalProperties": False,
            },
        }
    },
)
ticket = json.loads(response.output_text)
```

(Built on the Foundry SDK client from Domain 2 and the Responses API's JSON Schema output format.)

Three design choices carry the reliability: the **enum** for `urgency` (classification with a closed set), **"use null when not stated"** (stops the model inventing values), and **strict** mode with `required` and `additionalProperties: False` (the parser never meets a surprise field). Topics and summaries are where the model shines; a Foundry Tool cannot produce "topics in our taxonomy" without training.

### With Azure Language

Azure Language in Foundry Tools handles the standard analyses with one client. Microsoft's PII quickstart:

```python
import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

language_key = os.environ.get("LANGUAGE_KEY")
language_endpoint = os.environ.get("LANGUAGE_ENDPOINT")

def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def pii_recognition_example(client):
    documents = [
        "The employee's SSN is 859-98-0987.",
        "The employee's phone number is 555-555-5555."
    ]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))
pii_recognition_example(client)
```

(From "Quickstart: Detect personally identifiable information (PII)", read 2026-10-22. In production, pass an Entra ID credential such as `DefaultAzureCredential()` instead of a key.)

The output shows why a tool wins for PII: each entity has a **category** (`USSocialSecurityNumber`, `PhoneNumber`), a **confidence score**, and an **offset and length**, and the service returns **redacted text** ready to store. The same client exposes `analyze_sentiment` (with opinion mining that ties sentiment to aspects such as "battery" or "screen"), `recognize_entities`, `extract_key_phrases` and `detect_language`. Note the `is_error` check: batch calls return per-document results, and one bad document does not fail the batch.

## Sentiment, tone, safety issues and sensitive content

These four sound alike and are tested as a set:

- **Sentiment**: positive, negative, neutral or mixed, with scores; opinion mining for aspect-level sentiment. Azure Language does this consistently and cheaply at volume.
- **Tone**: polite, frustrated, sarcastic, urgent, formal. Not a fixed category set, so a model prompt with an enum fits better ("classify tone as one of ...").
- **Safety issues**: hate, sexual, violence and self-harm content, and prompt attacks. That is **Azure AI Content Safety**, either as the guardrails on a deployment (automatic) or the Content Safety API on text that never goes to a model (for example user comments you publish).
- **Sensitive content**: PII and other confidential data. Azure Language PII detection for redaction pipelines; the **PII guardrail control** (preview) to annotate or block PII in model inputs and outputs.

**Worked scenario.** A product team wants a dashboard of customer emails: overall sentiment, the features people complain about, and an escalation flag for abusive or threatening messages, with personal data removed before analysts see it. Build it as: Azure Language PII redaction first (so nothing downstream sees personal data), Azure Language sentiment with opinion mining for the features, Content Safety for the abuse flag, and a model with structured output only for "suggested next action", which needs reasoning.

## Translation

Two approaches, and the exam asks you to choose.

**Azure Translator in Foundry Tools** is a dedicated machine translation service: text translation across a large set of languages, automatic language detection, transliteration, **document translation** that preserves the file's formatting, and **custom translator** models trained on your parallel data for domain terminology. It is consistent, fast and priced per character. Microsoft's Python quickstart (it pins a beta package, `azure-ai-translation-text==1.0.0b1`):

```python
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

key = "<your-key>"
endpoint = "<your-endpoint>"
region = "<region>"

credential = TranslatorCredential(key, region)
text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

try:
    source_language = "en"
    target_languages = ["es", "it"]
    input_text_elements = [ InputTextItem(text = "This is a test") ]

    response = text_translator.translate(content = input_text_elements, to = target_languages, from_parameter = source_language)
    translation = response[0] if response else None

    if translation:
        for translated_text in translation.translations:
            print(f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")

except HttpResponseError as exception:
    print(f"Error Code: {exception.error.code}")
    print(f"Message: {exception.error.message}")
```

(From "Quickstart: Azure Translator client libraries", read 2026-10-22. Note that one call translates into several target languages, and that a regional resource needs the region alongside the key.)

**LLM-powered translation** sends the text to a language model with instructions. It handles tone, register, idiom and context ("translate this marketing email for a Brazilian audience, keep it informal, keep product names in English") and can translate and adapt in one step. It costs more per word, can drift from the source, and needs evaluation.

| Requirement | Better choice |
|---|---|
| Millions of product descriptions, consistent terminology, low cost | Translator (custom translator for the terminology) |
| Translate a Word or PDF file keeping its layout | Translator document translation |
| Marketing copy that must sound native and keep a brand voice | LLM translation, with human review |
| Translate and summarise a long thread for an executive in one step | LLM |

## Customising outputs for domain tasks

"Compliance summarisation and domain extraction" are about getting a general model to behave like a specialist. The levers, cheapest first:

1. **Instructions** that define the audience, the required sections, what to quote verbatim, and what never to infer.
2. **Few-shot examples** of input and ideal output.
3. **Structured output** with domain field names and enums.
4. **Grounding** in domain references (the regulation text, the company glossary) through retrieval.
5. **Evaluation** with domain-specific criteria (a custom evaluator that checks every obligation is cited).
6. **Fine-tuning** when examples in the prompt are not enough and you have hundreds or thousands of good examples; or a custom model in Azure Language for custom entity categories.

**Worked scenario.** A bank must summarise regulator letters into "obligations, deadlines, owners" with every obligation linked to a paragraph number. A generic summary prompt loses the paragraph links. The fix is a schema with `obligation`, `deadline`, `paragraph` fields, an instruction to quote the paragraph number from the source, grounding on the letter only, and a groundedness evaluation before release.

## Speech

### Speech to text and text to speech for agentic interactions

**Azure Speech in Foundry Tools** converts speech to text (STT) and text to speech (TTS). Microsoft's STT quickstart:

```python
import os
import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), endpoint=os.environ.get('ENDPOINT'))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))

recognize_from_microphone()
```

(From "Quickstart: Recognize and convert speech to text", read 2026-10-22. For a file, use `AudioConfig(filename="YourAudioFile.wav")`.)

What the exam picks at: `recognize_once_async` handles a single utterance (up to about 30 seconds or until silence), so a call-centre recording or a long dictation needs **continuous recognition** (or batch transcription for stored files). Always handle `NoMatch` and `Canceled`; `Canceled` with an error usually means a wrong key, endpoint or region. TTS is the mirror image: a `SpeechSynthesizer` with a voice name, and **SSML** when you need control over pronunciation, pauses, speaking rate or style.

The classic voice agent chains the three: STT turns the caller's words into text, the agent responds, TTS speaks the reply. It is flexible (any agent, any voice) but each hop adds latency and the agent never hears tone of voice.

### Speech as an agent modality

The objective says "integrate speech as an agent modality, including custom speech models." Two routes:

- **Chained**: Speech STT, then the agent, then Speech TTS, as above. Use it when you need a specific agent, full control of each step, or batch processing.
- **Voice Live API** (Azure Speech in Foundry Tools): "a solution that enables low-latency, high-quality speech-to-speech interactions for voice agents ... By integrating speech recognition, generative AI, and text-to-speech functionalities into a single, unified interface." It adds noise suppression, echo cancellation, interruption detection, advanced end-of-turn detection, avatars and function calling, over WebSockets compatible with the Azure OpenAI Realtime API. You choose the model (real-time models with native audio, or text models with Azure STT and TTS around them), and the model choice sets the pricing tier (Pro, Standard, Lite). Use it for contact-centre bots and in-car assistants where perceived latency matters.

**Customisation**: a **phrase list** is a lightweight, just-in-time way to boost recognition of names and jargon; a **custom speech** model is trained on your audio and text when accuracy on domain vocabulary or acoustic conditions (factory noise, accents) must improve; **custom voice** gives a brand voice for output and is limited access (you apply, because of impersonation risk).

### Multimodal reasoning from audio

Audio-capable models (the real-time and audio model families) take **audio itself** as input, so they can respond to tone, hesitation and non-speech sounds that a transcript loses. Use them when how something is said matters ("is the caller getting angry?") or when you want speech-to-speech without a transcript step. Use transcription first when you need a searchable record, compliance archiving, or processing at batch scale; Content Understanding on audio then turns calls into fields such as intent, resolution and sentiment (Domain 5).

### Translating speech

Speech translation has the same two options as text:

- **Azure Speech translation**: recognises speech in one language and returns text (and optionally synthesised speech) in one or more target languages in real time. One service, low latency, consistent.
- **A pipeline with a language model**: STT, then LLM translation (with tone and context instructions), then TTS in the target language's voice. Better adaptation and terminology control; more latency and more pieces.

Choose Speech translation for live captions and real-time conversations; choose the LLM pipeline when the translation must be adapted (marketing, culturally sensitive support) and a second of extra latency is acceptable.

## Check yourself

1. Redact Social Security numbers from 2 million chat logs with character offsets. *(Azure Language PII detection: categories, offsets, redacted text.)*
2. Classify tickets into your company's 14 internal topic codes. *(A model with structured output and an enum, or a custom Language model if you have labelled data.)*
3. A model's JSON sometimes has extra fields that break parsing. *(Strict JSON Schema output with `additionalProperties: False`.)*
4. Translate 40,000 PDFs keeping layout. *(Translator document translation.)*
5. Recognition stops after the first sentence of a 10-minute recording. *(`recognize_once_async` handles one utterance; use continuous or batch transcription.)*
6. A voice bot feels slow and talks over users. *(Voice Live API: end-of-turn and interruption detection, lower latency.)*
7. Product names are misrecognised. *(Phrase list first; custom speech if that is not enough.)*

## Sources (read 2026-10-22)

- [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Quickstart: Detect PII (Azure Language)](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/quickstart)
- [Quickstart: Azure Translator client libraries](https://learn.microsoft.com/en-us/azure/ai-services/translator/text-translation/quickstart/client-library-sdk)
- [Quickstart: Recognize speech to text](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text)
- [Voice Live API overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/voice-live)
- [Guardrails and controls overview](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview)
- Background on this site: [Speech AI](../../../../learn/concepts/speech-ai-asr-and-tts.md), [Structured outputs](../../../../learn/concepts/structured-outputs.md), [Prompt engineering](../../../../learn/concepts/prompt-engineering.md), [Voice agent project](../../../../build/projects/voice-agent.md)
