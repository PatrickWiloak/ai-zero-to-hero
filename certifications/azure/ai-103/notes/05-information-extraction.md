---
last-updated: 2026-10-22
difficulty: intermediate
reading-time: 22 min
---

# 05 Retrieval, Grounding and Content Understanding

Domain 5 of AI-103: **Implement information extraction solutions (10-15%)**. Two skill groups: building retrieval and grounding pipelines (mostly Azure AI Search), and extracting content from documents (mostly Content Understanding). Together they are the data side of every RAG app and agent in Domain 2: if retrieval returns the wrong chunk, no prompt can save the answer.

## The shape of a grounding pipeline

A grounding pipeline has two halves that must agree with each other.

**Ingestion** (offline, repeated): read source content, crack it into text and images, run OCR and layout analysis, enrich it, split it into chunks, embed each chunk, and write chunks with their metadata into an index.

**Query** (online, per request): turn the user's question into a query (text, vector or both), retrieve the top chunks, optionally rerank, and hand them to the model or agent with their source references.

They must agree on two things. The **embedding model** used at query time must be the same one used at index time, or vectors live in different spaces and similarity means nothing. And the **chunking** must suit the questions: chunks too large dilute relevance and waste tokens; chunks too small lose context.

## Ingesting and indexing content

### Indexers, data sources and skillsets

Azure AI Search can ingest in two ways. **Push**: your code sends documents to the index through the SDK or REST, which gives full control and works with any source. **Pull**: an **indexer** connects to a supported **data source** (Blob Storage, Azure SQL, Cosmos DB, and others), reads new and changed content on a schedule, runs a **skillset**, and writes to the index. Pull is the managed default and handles change tracking for you.

A **skillset** is an ordered set of enrichment steps. Built-in skills cover OCR (text from images), language detection, entity and key phrase extraction, **Text Split** (chunking), layout-aware document parsing, and embedding. **Custom skills** call your own code through a Web API (an Azure Function, for example) when you need something the built-ins do not do, such as calling a domain classifier.

### Integrated vectorization

**Integrated vectorization** puts chunking and embedding inside the search pipeline instead of in your code. Microsoft describes the moving parts precisely:

- An **indexer** that "retrieves raw data from a supported data source and drives the pipeline engine."
- A **skillset** with a chunking strategy ("Text Split skill, Azure Content Understanding skill, or one of the document parsing modes") and an embedding skill: the **AzureOpenAIEmbedding** skill (text-embedding-ada-002, text-embedding-3-small or -3-large), a **custom skill** pointing at another model, the **Azure Vision multimodal embeddings** skill (preview, for images), or the **AML skill** for models in the Foundry catalog.
- A **vectorizer** defined in the index and assigned to the vector field, "used automatically at query time to convert a text query to a vector." It "must match the embedding model used to encode your content."

The pairs to remember: AzureOpenAIEmbedding skill with the Azure OpenAI vectorizer; custom skill with the custom Web API vectorizer; Azure Vision multimodal skill with the Azure Vision vectorizer; AML skill with the Foundry model catalog vectorizer.

Integrated vectorization also supports **index projections**: one indexer run writes parent documents to one index and their chunks to a secondary index. Microsoft's reasoning: the chunk index gives "more specific matches," and when a chunk matches, the query can return the parent for a "more complete answer."

Operational notes the exam likes: data chunking with Text Split "is free"; embedding calls are throttled by the embedding model's tokens-per-minute quota, so Microsoft recommends running the indexer on a schedule ("for example, every 5 minutes") so throttled items are picked up; and separate embedding deployments for indexing and querying avoid one starving the other.

### Images, audio and video

Retrieval is not only for text:

- **Images inside documents**: the indexer extracts them (image action), the OCR skill reads their text, and a merge step puts that text back into the document content before chunking. Without OCR a scanned PDF indexes as nearly empty.
- **Images as images**: the Azure Vision multimodal embeddings skill puts images and text in one vector space, so a text query can find a matching photo.
- **Audio and video**: run Content Understanding (as a skill or a separate step) to produce transcripts, segment descriptions and fields, then index that text and metadata with time offsets so answers can point to the moment in the recording.

## Configuring vector, hybrid and semantic search

### The index definition

A search index for RAG has a key, the chunk text (searchable), a vector field, metadata for filters and citations (title, URL, page, ACL groups), a **vector search** configuration and usually a **semantic** configuration. Microsoft's vector quickstart defines them like this:

```python
from azure.search.documents.indexes.models import (
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SemanticConfiguration,
    SemanticSearch,
    SemanticPrioritizedFields,
    SemanticField,
)

# Vector field definition with HNSW configuration
fields = [
    SearchField(
        name="DescriptionVector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="my-vector-profile"
    ),
    # ... other fields
]

vector_search = VectorSearch(
    algorithms=[HnswAlgorithmConfiguration(name="my-hnsw-vector-config-1")],
    profiles=[VectorSearchProfile(name="my-vector-profile", algorithm_configuration_name="my-hnsw-vector-config-1")]
)

semantic_search = SemanticSearch(
    configurations=[
        SemanticConfiguration(
            name="my-semantic-config",
            prioritized_fields=SemanticPrioritizedFields(
                title_field=SemanticField("HotelName"),
                content_fields=[SemanticField("Description")],
                keywords_fields=[SemanticField("Category")]
            )
        )
    ]
)
```

(From "Quickstart: Vector search" for Azure AI Search, read 2026-10-22; index model classes come from `azure.search.documents.indexes.models`.)

Things that break in exam snippets: `vector_search_dimensions` must equal the embedding model's output size (1536 for text-embedding-3-small and ada-002 at default size); the field type must be a collection of `Single`; the field must reference a **profile**, and the profile references an **algorithm** (HNSW for approximate nearest neighbour, or exhaustive KNN for exact search on small sets).

### Queries

```python
vector_query = VectorizedQuery(
    vector=vector,
    k_nearest_neighbors=5,
    fields="DescriptionVector",
    kind="vector",
    exhaustive=True
)

results = search_client.search(
    search_text="historic hotel walk to restaurants and shopping",
    vector_queries=[vector_query],
    select=["HotelId", "HotelName", "Category", "Description"],
    query_type="semantic",
    semantic_configuration_name="my-semantic-config",
    top=5,
    include_total_count=True
)
```

(Same quickstart: a semantic hybrid query. `VectorizedQuery` comes from `azure.search.documents.models`.)

Read it as three layers. `search_text` alone is **keyword** search. Adding `vector_queries` makes it **hybrid**: both run and the results merge by Reciprocal Rank Fusion. Adding `query_type="semantic"` with a semantic configuration applies the **semantic ranker** to the merged top results. Drop `search_text` and you have pure **vector** search. `VectorizedQuery` takes a vector you computed; `VectorizableTextQuery` takes text and uses the index's vectorizer.

| Situation | Query configuration |
|---|---|
| Users search part numbers and exact phrases | Keyword (maybe with filters) |
| Users ask questions in their own words | Vector or hybrid |
| General RAG over mixed documents | Hybrid with semantic ranking |
| Very small index, exact results needed | Vector with exhaustive KNN |
| Only documents the user may see | Any of the above plus a **filter** on an ACL field (security trimming) |

## Connecting retrieval to workflows and agents

Once the index exists, three ways to use it:

1. **In your own code** (Domain 2, option 1): `SearchClient.search`, then the model. Full control over filters and prompts.
2. **As an agent tool**: the Azure AI Search tool on a prompt agent, through a **project connection** and an index name, with a `query_type` (`simple`, `vector`, `semantic`, `vector_simple_hybrid`, or the default `vector_semantic_hybrid`). The agent decides when to search and returns citations. Tools can also be bundled in a **toolbox** shared by several agents.
3. **Through Foundry IQ**: Microsoft describes it as "the managed knowledge layer that transforms enterprise content into reusable, permission-aware knowledge bases for agents," built on Azure AI Search. Choose it when several agents need the same curated, permission-aware knowledge without each team building its own pipeline.

## Extracting content from documents

### Why a dedicated extraction service

OCR alone gives you characters. **Layout analysis** gives structure: reading order, paragraphs, headings, tables, checkboxes, figures. **Field extraction** gives the values you actually need: invoice number, total, due date. Real documents need all three, and they need **confidence** and **grounding** so a person can check the uncertain ones. That is what **Azure Content Understanding in Foundry Tools** packages: one service that "uses generative AI to process and ingest many types of content ... into a user-defined output format," for documents, images, audio and video.

### Prebuilt analyzers

Prebuilt analyzers cover common jobs: `prebuilt-invoice` for invoices, and `prebuilt-documentSearch`, `prebuilt-imageSearch`, `prebuilt-audioSearch` and `prebuilt-videoSearch` that produce search-ready content per modality. Microsoft's Python quickstart (GA API `2025-11-01`):

```python
import os
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, DocumentContent
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["CONTENTUNDERSTANDING_ENDPOINT"]
key = os.environ["CONTENTUNDERSTANDING_KEY"]
client = ContentUnderstandingClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Sample invoice
invoice_url = "https://raw.githubusercontent.com/Azure-Samples/azure-ai-content-understanding-assets/main/document/invoice.pdf"

poller = client.begin_analyze(
    analyzer_id="prebuilt-invoice",
    inputs=[AnalysisInput(url=invoice_url)],
)
result = poller.result()

document_content: DocumentContent = result.contents[0]
print(f"Pages: {document_content.start_page_number} to {document_content.end_page_number}")

# Extract fields
customer_name = document_content.fields.get("CustomerName")
if customer_name:
    print(f"Customer Name: {customer_name.value}")
```

(From "Quickstart: Azure Content Understanding in Foundry Tools", read 2026-10-22, trimmed. The REST equivalent posts to `{endpoint}/contentunderstanding/analyzers/prebuilt-invoice:analyze?api-version=2025-11-01` and polls the `Operation-Location` header.)

The pattern to recognise: analysis is a **long-running operation**. `begin_analyze` returns a **poller**; `.result()` waits for the `AnalysisResult`. A snippet that reads fields straight off the `begin_analyze` return value is wrong.

### Custom analyzers: extract, classify, generate

When prebuilt fields are not what you need, define an analyzer. It builds on a base analyzer, names the models it uses (a completion model and an embedding model deployed in your Foundry resource), sets options, and declares a **field schema**:

```python
from azure.ai.contentunderstanding.models import (
    ContentAnalyzer,
    ContentAnalyzerConfig,
    ContentFieldSchema,
    ContentFieldDefinition,
    ContentFieldType,
    GenerationMethod,
)

analyzer_id = f"my_document_analyzer_{int(time.time())}"

field_schema = ContentFieldSchema(
    name="company_schema",
    description="Schema for extracting company information",
    fields={
        "company_name": ContentFieldDefinition(
            type=ContentFieldType.STRING,
            method=GenerationMethod.EXTRACT,
            description="Name of the company",
            estimate_source_and_confidence=True,
        ),
        "document_type": ContentFieldDefinition(
            type=ContentFieldType.STRING,
            method=GenerationMethod.CLASSIFY,
            description="Type of document",
            enum=["invoice", "receipt", "contract", "report", "other"],
        ),
    },
)

analyzer = ContentAnalyzer(
    base_analyzer_id="prebuilt-document",
    description="Custom analyzer for extracting company information",
    field_schema=field_schema,
    models={"completion": "gpt-5.2", "embedding": "text-embedding-3-large"},
)

poller = client.begin_create_analyzer(
    analyzer_id=analyzer_id,
    resource=analyzer,
)
result = poller.result()
```

(From "Create a custom analyzer with Azure Content Understanding", read 2026-10-22.)

The three **methods** are the heart of it:

- **extract**: the value appears in the content (a company name, an invoice total). Pair with `estimate_source_and_confidence=True` to get a confidence score and the location it came from.
- **classify**: choose one value from an `enum` (document type, damage severity).
- **generate**: the model writes the value (a summary, a reason for a call, a risk note).

The equivalent JSON definition sets `"estimateFieldSourceAndConfidence": true`, `"returnDetails": true` and a `tableFormat` in `config`, and nests `array` and `object` types for line items.

### Clean, grounded output for agents and RAG

Two outputs make Content Understanding useful downstream:

- **Markdown**: a clean text rendering of the document with headings and tables preserved. Chunking markdown by heading gives far better retrieval than chunking raw OCR text, which is why the Content Understanding skill can act as the chunking strategy in integrated vectorization.
- **Structured fields with grounding**: values with confidence and source location. Agents can reason over the fields directly ("total due is 4,210.50, due 2026-11-15"), and a reviewer can click through to the source.

Route by confidence: above a threshold, straight through; below it, a person checks the value against the grounded location. That is the standard "human review of low-confidence results" answer.

### When reasoning across the document is needed

Some answers are not written anywhere: "does this invoice's total match the sum of its line items?", "is the renewal date consistent with the amendment?" The study guide still calls this **pro mode**. Microsoft now says pro mode "is only available in the `2025-05-01-preview` API, which is now retired" and points to **agentic mode** (preview, `2026-06-01-preview`): set `config.workflow` to `"agentic"` on a document analyzer for multistep reasoning, calculations, validation and visual analysis. Its preview limits: one input file per request (which may contain several related documents), document analyzers only, and no `extract`-method fields. It uses more tokens (Microsoft suggests about 400,000 TPM capacity per job) and takes longer, so use it only where standard extraction falls short, and never as a replacement for human review in high-impact decisions.

## Worked scenario: a policy assistant end to end

A health insurer wants an agent that answers members' coverage questions from 3,000 policy PDFs (many scanned), cites the clause, and never shows one employer group's plan to another.

1. **Ingestion**: Blob Storage data source; indexer on a schedule; skillset with OCR (scans) or the Content Understanding skill for layout-aware markdown, Text Split by section, AzureOpenAIEmbedding; index projections to a chunk index with `plan_id`, `clause`, `page` and `group_id` fields.
2. **Index**: vector field with an HNSW profile and the Azure OpenAI vectorizer (same embedding model), semantic configuration on title and content.
3. **Query**: the agent's Azure AI Search tool with `vector_semantic_hybrid`; for security trimming, filter on `group_id` for the member's group. Because tool-level filters may not carry per-user context, many teams call search from a function tool or their own code so the app injects the filter; that is the design to choose when the scenario stresses "users must only see their own plan."
4. **Answer**: instructions require citations and "say you don't know" when the clause is not retrieved.
5. **Monitor**: indexer run history for failed documents; Document Retrieval evaluator on a labelled question set for relevance; groundedness on sampled production traffic.

## Check yourself

1. Scanned PDFs index with almost no text. *(Add OCR, or the Content Understanding skill, to the skillset.)*
2. Vector search returns nonsense after you switched embedding models for queries only. *(Query and index embeddings must come from the same model: re-embed or revert, and keep the vectorizer matched.)*
3. Users search exact part numbers and also ask natural questions. *(Hybrid search, with semantic ranking for the top results.)*
4. Code reads `client.begin_analyze(...).contents`. What is wrong? *(It is a poller: call `.result()` first.)*
5. You need a document's type from a fixed list. Which field method? *(classify, with an enum.)*
6. You need a value plus where it came from and how sure the service is. *(extract with source and confidence estimation.)*
7. Several agents need the same permission-aware company knowledge. *(Foundry IQ knowledge base.)*

## Sources (read 2026-10-22)

- [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103)
- [Integrated vectorization overview](https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization)
- [Quickstart: Vector search](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector)
- [Connect an Azure AI Search index to Foundry agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/ai-search)
- [Content Understanding quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api)
- [Create a custom analyzer](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/tutorial/create-custom-analyzer)
- [Agentic mode overview](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/agentic-mode)
- Background on this site: [RAG explained](../../../../learn/concepts/rag-explained.md), [Embeddings and vector search](../../../../learn/concepts/embeddings-and-vector-search.md), [Advanced RAG patterns](../../../../build/patterns/advanced-rag-patterns.md), [Build a RAG pipeline](../../../../build/projects/build-rag-pipeline.md), [Document processing](../../../../work/use-cases/document-processing.md)
