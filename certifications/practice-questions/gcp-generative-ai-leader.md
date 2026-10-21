# Google Cloud Generative AI Leader - Practice Questions

15 questions for Generative AI Leader prep. This is a business certification: expect scenario questions about value, cost, adoption, and responsible AI alongside the technical concepts.

> **Cert page:** [exams/gcp/generative-ai-leader/](../gcp/generative-ai-leader/README.md)

---

### Question 1
**Scenario:** A retailer wants an assistant that answers customer questions about its current product catalog, which changes weekly.

A. Fine-tune a model on the catalog each week so that the product knowledge is built into the model weights and answers need no extra context
B. Train a custom foundation model
C. Include the whole catalog in every prompt so the model always sees the latest products without any retrieval step
D. Ground the model on the catalog data, using retrieval

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Weekly changes make fine-tuning wrong, because fine-tuned knowledge is frozen at training time and would need retraining each week. Grounding updates instantly. Including the whole catalog exceeds practical context and cost limits. The commonest wrong answer on this exam is fine-tuning applied to a knowledge problem.
</details>

---

### Question 2
**Scenario:** An organization wants employees to draft documents and summarize meetings more quickly, with minimal engineering effort.

A. Deploy an open model with Gemma on the organization's own infrastructure, so that staff can draft and summarize with a model it controls
B. Fine-tune a model on company documents so that it learns the house style and terminology before staff start drafting
C. Build a custom application on Agent Platform (formerly Vertex AI)
D. Adopt Gemini for Google Workspace, an applied assistant that works inside the Docs, Gmail and Meet tools staff already use

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Start at the lowest rung of the ladder. An applied assistant delivers productivity gains with no build at all. Building on the platform is for differentiated experiences, and fine-tuning or self-hosting are further up the cost and effort curve.
</details>

---

### Question 3
**Scenario:** Responses to the same prompt vary too much between runs for an extraction task.

A. Increase top-k so that the model samples from a larger candidate set
B. Increase the output token limit so that the model has room to finish each extraction without being cut off and varying
C. Lower the temperature so that token selection becomes close to deterministic for the extraction task
D. Fine-tune the model on examples of the extraction output

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Temperature is the primary control over randomness in token selection, and lowering it makes output near-deterministic. Increasing top-k widens the candidate set, adding variety. Fine-tuning is an expensive answer to a parameter setting.
</details>

---

### Question 4
**Scenario:** A model must check live inventory before answering a customer question.

A. Increase the context window so that the model can hold a larger inventory export in the prompt when it answers the customer
B. Function calling, so the model can request that application code query the inventory system
C. Grounding with Google Search, so that answers about stock levels are based on current web content about the products
D. Fine-tune the model on inventory data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Live data and actions require function calling. Fine-tuning freezes a snapshot. Search grounding covers public web information, not an internal inventory system. A larger context window does not connect the model to a live system.
</details>

---

### Question 5
**Scenario:** Which Google Cloud product provides grounded search over an organization's own content with generative summaries and citations?

A. BigQuery ML, which brings generative functions to data already in the warehouse but is not a grounded enterprise search product
B. NotebookLM
C. Gemma, the family of open models that an organization can run itself, which provides a model rather than a search product with citations
D. Agent Search

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Agent Search is the enterprise product for grounded search with summaries and citations. NotebookLM is grounded research over sources an individual supplies. BigQuery ML brings generative functions to data in the warehouse. Gemma is a family of open models.
</details>

---

### Question 6
**Scenario:** A leadership team asks how to decide which generative AI use cases to pursue first.

A. Prioritize by business value against feasibility, favoring high-value, high-feasibility quick wins with demonstration value
B. Start with the most technically interesting
C. Start with the largest department
D. Pursue all candidate use cases in parallel, so that every team benefits at once and no department has to wait for the results of another team's pilot

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Value against feasibility is the standard framing, and early wins should be chosen partly for visibility, because a demonstrated success builds the organizational appetite that later, harder projects require.
</details>

---

### Question 7
**Scenario:** A project to summarize support tickets has stalled. The model works well in demos. What is the most likely cause?

A. Temperature is set incorrectly, so the model produces inconsistent summaries once real tickets replace the demo examples
B. Data readiness: access, quality, or governance of the ticket data
C. The context window is too small to hold a full ticket thread, so the summaries lose detail once the real data is used
D. The model is not capable enough for the task, so a larger foundation model should be chosen before any other change is made

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data readiness is the most common real constraint on generative AI projects. A model that performs well in a demo and stalls in delivery usually points at data access, quality, or permission problems rather than model capability.
</details>

---

### Question 8
**Scenario:** Which of these is a good candidate for generative AI?

A. Calculating monthly payroll totals exactly, because generative models are good at arithmetic and can replace the payroll engine
B. Routing tickets according to a fixed set of rules, because a model can read each ticket and apply the rules more flexibly
C. Drafting first-pass responses to customer emails, reviewed by an agent
D. Determining regulatory filing figures with no review, because the model can produce them faster than an analyst and cut costs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Good candidates involve unstructured content, have a measurable outcome, and tolerate imperfection through a review step. Exact arithmetic and deterministic rule routing are better solved conventionally. Unreviewed regulatory output requires a guarantee these models cannot give.
</details>

---

### Question 9
**Scenario:** What does grounding primarily mitigate?

A. Hallucination
B. Latency
C. Bias
D. Cost

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Grounding supplies authoritative source text so the model answers from evidence rather than from memory, which is the primary mitigation for confident wrong answers. It also enables citations so a human can verify.
</details>

---

### Question 10
**Scenario:** Which is included in total cost of ownership for a generative AI solution but commonly overlooked?

A. Inference cost, the per-token or per-request charge that appears directly on the cloud bill from the first day of the pilot
B. Network egress charged when generated content leaves the cloud region, which is itemised separately on the bill
C. Data preparation, evaluation, monitoring, and change management
D. Model licensing fees charged by the provider, which are published in the pricing page and are agreed before a project starts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Inference is visible and often not the largest line. Data preparation is usually the largest hidden cost, and ongoing evaluation, monitoring, and adoption work continue for the life of the system.
</details>

---

### Question 11
**Scenario:** Which situation calls for keeping a human in the loop?

A. Making a credit decision affecting an applicant
B. Summarizing internal meeting notes
C. Suggesting draft product descriptions
D. Categorizing support tickets by topic

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** High-stakes, regulated decisions affecting individuals require human review and an explainable rationale. The other three are low-stakes, reversible, and reviewable in aggregate.
</details>

---

### Question 12
**Scenario:** Which responsible AI theme does publishing a clear notice that users are interacting with an AI system address?

A. Privacy, which concerns how personal data is collected, protected and used rather than whether people are told they are talking to an AI
B. Transparency
C. Fairness, which concerns whether outcomes are equitable across different groups of people rather than whether the AI is disclosed
D. Accountability, which concerns a named human being responsible for the outcomes the system produces, not disclosure of AI use

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transparency means people know AI is being used and what it does. Explainability is about explaining a specific decision, accountability is about a human being responsible for outcomes, and fairness concerns equitable outcomes across groups.
</details>

---

### Question 13
**Scenario:** An organization needs to run a model on its own infrastructure, including at the edge, with full control over the weights.

A. Gemini for Google Cloud, an applied assistant offered as a managed service, so the weights are not available
B. Gemini through Agent Platform, a managed API that runs on Google's infrastructure, so the weights stay with Google
C. Gemma open models, which are released for the user to download and run on its own infrastructure, including at the edge
D. Agent Search, a managed enterprise search product with summaries and citations that does not provide downloadable model weights

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gemma is Google's family of open models intended to be run by the user, which is what "own infrastructure" and "control over the weights" require. The others are managed services or applied assistants.
</details>

---

### Question 14
**Scenario:** How should the success of a generative AI deployment be measured?

A. Number of features shipped
B. Business outcomes defined before building, plus quality, cost, and adoption metrics
C. Number of prompts submitted
D. Model size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Success criteria should be defined before building and measured afterwards, covering business outcome, output quality, operational cost, and how much of the eligible work actually flows through the new capability. Prompt counts and feature counts are activity, not outcome.
</details>

---

### Question 15
**Scenario:** A regulated customer requires that data submitted to a model is not used to train the provider's foundation models, and that inference stays within a specific region.

A. Agent Platform enterprise controls: no training on customer data, regional endpoints, and data residency options
B. Use the consumer Gemini app with a regional setting, which offers regional controls
C. Only self-hosting an open model satisfies this, because managed services always retain customer prompts to improve their models
D. This is not achievable with a managed service, because the provider's infrastructure cannot guarantee regional processing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Enterprise data governance, residency, private connectivity, and encryption controls are frequently the deciding factor in business scenarios involving regulated industries, and they are available on the managed platform rather than requiring self-hosting.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready.
- **10-12 correct (65-80%):** Review the adoption ladder and the business strategy material, which is weighted more heavily than a technical reader expects.
- **Below 10:** Read the official exam guide and study guide directly, then re-read [notes 04](../gcp/generative-ai-leader/notes/04-business-strategy.md).
