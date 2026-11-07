# Image and Video Generation Compared

**In one line:** Pick an image or video generator by what you need to control (editing precision, text in images, reference consistency, audio), by licence and provenance rules, and by how stable the model line is, because model names here change within months.
**Last reviewed:** 2026-11-07

---

## The short version

- Model names and lineups in this area change fast. Everything below is what the vendor docs said on **2026-11-07**; recheck before you commit.
- Decide first what you need: new images, **editing** existing ones, **consistent characters** across shots, **text rendered in the image**, or **video with sound**.
- Check the licence and the output rules (watermarks, provenance, allowed uses) before using output commercially. See [deepfakes and synthetic media](../../safety/security/deepfakes-and-synthetic-media.md).
- Prices are left out on purpose: none were read for this page. Check each vendor's pricing page.
- For how image models work, see [diffusion models](../../learn/concepts/diffusion-models.md).

## What the vendor docs said (as of 2026-11-07)

| Vendor / API | Image | Video | Notes from the docs |
|---|---|---|---|
| **OpenAI** (Image API, Responses API) | GPT Image models (`gpt-image-2.5-sunburst` for editing precision, `gpt-image-2.5-flare` for fast everyday generation; 2.6 versions add complexity control, markup-guided edits, SVG and animated GIF output) | Not on the image guide page | Generate and edit endpoints; masks guide edits but are prompt-based so exact shapes may not be followed; streaming partial images |
| **Google** (Gemini API, "Nano Banana" family) | Nano Banana 2.1, 2 Lite, 2, Pro and a legacy model; text-to-image, multi-turn editing, up to 14 reference images depending on model, 1K to 4K output | Gemini Omni Flash: 3 to 15 second videos with native audio, text/image/video inputs, up to 6 reference images for character consistency | Docs state all generated images include a SynthID watermark. The Veo 3.1 preview models listed were shut down on October 22, 2026 |
| **Stability AI** (platform API) | Stable Diffusion 3.5 and Stable Image services; generate and edit | Not mentioned on the docs home page | Also lists 3D and Stable Audio; licensing and self-hosting terms were not on the page, so check them |
| **Midjourney** | Not verified | Not verified | Its help-centre page returned HTTP 403; no facts claimed |

## How to choose

| If you need | Start with |
|---|---|
| Careful edits to an existing image | A model with edit and mask endpoints (OpenAI edits, Gemini multi-turn editing) |
| Same character across many images | A model that takes several reference images (Gemini lists up to 14, model dependent) |
| Short video with sound | Gemini Omni Flash per the docs above |
| Open weights you can run yourself | Check the Stability and Hugging Face model licences; not verified here |
| A brand-safe, provenance-labelled workflow | Prefer vendors that watermark or attach provenance, and keep your own log |

## Provenance in one paragraph

C2PA is an open standards effort (a project of the Joint Development Foundation, combining the Content Authenticity Initiative and Project Origin) that develops technical specifications for content provenance. A watermark such as SynthID is a different approach, embedded in the content by the generator. Neither stops misuse, and metadata can be stripped. (C2PA about page and Google docs, read 2026-11-07)

## Common mistakes

- Choosing on a demo reel instead of running your own 10 real prompts.
- Assuming an editing model will follow an exact mask.
- Shipping output without checking the vendor's terms for commercial use and likeness.
- Treating a model name as permanent. Two names on the Google video page were already shut down.

## Next steps

- [Multimodal models](../../learn/concepts/multimodal-models.md)
- [Which model for which job](../decisions/which-model-for-which-job.md)

## Sources

- OpenAI image generation guide: https://developers.openai.com/api/docs/guides/image-generation (fetched 2026-11-07, first 100,000 characters)
- Google AI Studio docs, image generation: https://aistudio.google.com/docs/image-generation and video: https://aistudio.google.com/docs/video (fetched 2026-11-07)
- Stability AI docs: https://docs.stability.ai/ (fetched 2026-11-07)
- C2PA, About: https://c2pa.org/about/ (fetched 2026-11-07)
