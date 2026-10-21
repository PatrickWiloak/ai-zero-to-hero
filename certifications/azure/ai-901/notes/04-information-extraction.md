---
last-updated: 2026-10-21
difficulty: beginner
reading-time: 8 min
---

# 04 Information Extraction with Content Understanding

Part of Domain 2, **Implement AI solutions by using Microsoft Foundry (55-60%)**: extract information from documents and forms, images, and audio and video with **Azure Content Understanding in Foundry Tools**, and build a lightweight app around it.

## What Content Understanding is

Microsoft describes Content Understanding as a Foundry Tool that "uses generative AI to process and ingest many types of content, including documents, images, videos, and audio, into a user-defined output format." In exam terms: **unstructured content in, structured fields out**, for any modality, through one API.

Key ideas from the official overview:

- **Analyzers** do the work. **Prebuilt analyzers** cover common and industry scenarios (for example tax preparation, procurement documents, contract analysis, call-centre analytics, media analysis). **Custom analyzers** are defined by you.
- **Field schema**: you define the fields you want (name, type, description), and the analyzer **extracts** values that appear in the content, **classifies** content into categories you list, or **generates** values (for example a summary or a reason-for-call) without you writing prompts.
- **Confidence scores and grounding**: each extracted value comes with a confidence score and a pointer to where in the content it came from, so you can send low-confidence results to human review and audit the rest.
- **Classification** can sort incoming files by type first and route each to the right analyzer.
- **Markdown output**: a clean text representation of the content, useful for search indexes and RAG.

## By modality

| Content | Example fields | Notes |
|---|---|---|
| **Documents and forms** (PDFs, scans) | Invoice number, vendor, line items, totals, due date; form checkboxes; contract parties and renewal date | Includes layout, tables and handwriting; the successor workflow to Document Intelligence-style extraction |
| **Images** | Product attributes from a photo, damage type and severity from an insurance photo, text and values from a screenshot | Generative fields can describe what is shown |
| **Audio** | Transcript plus fields: caller intent, product mentioned, sentiment, whether the issue was resolved | Built on speech recognition |
| **Video** | Scene and shot descriptions, key moments, on-screen text, topics, chapter markers | Useful for media search and compliance review |

## A lightweight extraction app

The shape of the app the exam describes:

1. Create a Foundry resource and project; Content Understanding is available as part of it.
2. Choose a **prebuilt analyzer** or create a **custom analyzer** with a field schema (for example `VendorName: string`, `InvoiceTotal: number`, `IsUrgent: boolean, "true if the letter demands payment within 7 days"`).
3. Test it in the portal on sample files and refine field descriptions.
4. From code, call the **analyze** operation with the file (or a URL), wait for the result, and read the fields with their confidence scores.
5. Apply a threshold: high confidence goes straight through; low confidence goes to a person.

## Content Understanding or a multimodal model?

You can also ask a vision- or audio-capable model "extract these fields as JSON". Content Understanding is the better exam answer when the scenario stresses **high volume, consistent schema, confidence scores, grounding (where the value came from), human review of low-confidence results, or industry prebuilt analyzers**. A direct model prompt fits one-off or highly variable tasks. See [Document processing](../../../../work/use-cases/document-processing.md) and the [structured extraction pipeline project](../../../../build/projects/structured-extraction-pipeline.md) on this site.

## Check yourself

1. You need invoice totals from 50,000 PDFs a month, with low-confidence values sent to a clerk. *(Content Understanding with an invoice analyzer; use confidence scores for routing.)*
2. You need each support call's reason, product and whether it was resolved. *(Content Understanding on audio with generated and classified fields.)*
3. Mixed incoming mail: invoices, contracts and letters, each needing different fields. *(Classify first, then route to the matching analyzer.)*
4. What does "grounding" mean for an extracted field? *(The location in the source content the value came from.)*

## Sources

- [What is Azure Content Understanding in Foundry Tools?](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) (read 2026-10-21)
- [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
