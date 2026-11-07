# Embedding Models Compared

**In one line:** Pick an embedding model by language and content type, context length, vector size and your retrieval test results, not by a leaderboard rank, and plan for the fact that changing models means re-embedding everything.
**Last reviewed:** 2026-11-07

---

## The short version

- Embeddings turn text (or images) into vectors so you can search by meaning. Start with [embeddings and vector search](../../learn/concepts/embeddings-and-vector-search.md).
- **Switching models re-embeds your whole corpus**, so choose with a retrieval test on your own data first.
- Dimensions trade accuracy against storage and speed. Several vendors let you shorten vectors.
- Leaderboards (such as the MTEB leaderboard on Hugging Face) are a starting list. The page fetched for this review did not describe MTEB, so read its documentation yourself before relying on a score.
- Prices are not included; none were read.

## Facts from vendor docs (as of 2026-11-07)

| Provider | Models named | Dimensions | Context / input | Notes |
|---|---|---|---|---|
| **OpenAI** | `text-embedding-3-small`, `text-embedding-3-large`, `text-embedding-ada-002` | 1536, 3072, not stated | 8192 tokens | v3 models take a `dimensions` parameter; the page lists MTEB scores of 62.3%, 64.6% and 61.0%. If you shorten manually, normalise to unit length |
| **Cohere** | `embed-v5.0-pro`, `embed-v5.0-fast`, `embed-v4.0`, v3 English/multilingual and light variants | v5: 256 to 2048 (default 2048); v4: 256 to 1536; v3: 1024 or 384 | 128k tokens for v5 and v4; 512 for v3 | v5 and v4 handle text, images and mixed; v5 models share an embedding space so you can index with Pro and query with Fast; 100+ languages on v5 |
| **Voyage AI** | `voyage-4-large`, `voyage-4`, `voyage-4-lite`, `voyage-code-4`, `voyage-finance-2`, `voyage-law-2`; open-weight `voyage-4-nano` | 1024 default (256, 512, 2048 for the 4 series) | 32,000 tokens (16,000 for law-2) | Domain models for code, finance and law; voyage-4, voyage-4-large, voyage-4-lite and voyage-4-nano are compatible with each other (voyage-code-4 not stated) |

Open-source models (for example those on Hugging Face) are another route when you must run on your own hardware; none were fetched for this page.

## How to choose

1. List your needs: languages, text only or images too, code or legal content, self-hosting, data-residency rules.
2. Build a small test set: 50 to 100 real questions with the document passages that answer them.
3. Embed with two or three candidates, measure recall at the top 5 or 10 results, and compare.
4. Test a shorter vector size if storage or latency matters.
5. Record the model name and version with every stored vector so you know what needs re-embedding.

## Common mistakes

- Picking the top leaderboard model without a test on your content.
- Mixing vectors from different models in one index. Only compatible families (Voyage 4 series except voyage-code-4 which the page does not state, Cohere v5 per their docs) can mix.
- Forgetting that queries and documents may need different input settings; check the vendor's reference.
- Chunking badly and blaming the model. See [advanced RAG patterns](../../build/patterns/advanced-rag-patterns.md).

## Next steps

- [Vector database decision guide](../decisions/vector-database.md)
- [Build a RAG pipeline](../../build/projects/build-rag-pipeline.md)

## Sources

- OpenAI embeddings guide: https://developers.openai.com/api/docs/guides/embeddings (fetched 2026-11-07)
- Cohere Embed: https://docs.cohere.com/docs/cohere-embed (fetched 2026-11-07)
- Voyage AI embeddings: https://docs.voyageai.com/docs/embeddings (fetched 2026-11-07)
- MTEB leaderboard (Hugging Face Space): https://huggingface.co/spaces/mteb/leaderboard (fetched 2026-11-07; page gave no description)
