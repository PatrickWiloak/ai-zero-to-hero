---
last-updated: 2026-10-22
difficulty: advanced
---

# AWS Certified Generative AI Developer - Professional (AIP-C01) - Practice Questions

30 questions for AIP-C01 prep, weighted toward foundation model integration, data management, and compliance (31%), implementation and integration (26%), and AI safety, security, and governance (20%), then operational efficiency (12%) and testing and troubleshooting (11%).

> **Cert page:** [exams/aws/professional/genai-developer-aip-c01/](../aws/professional/genai-developer-aip-c01/README.md)

---

### Question 1
**Scenario:** An application must call several foundation models through one API with no infrastructure to manage.

A. Amazon Bedrock with its unified API
B. Amazon Comprehend
C. Amazon SageMaker training jobs on dedicated instances
D. EC2 with self-hosted models behind a load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Bedrock is the managed multi-model API covering Anthropic, Meta, Mistral, Amazon, and others behind a single interface, with no capacity to provision. SageMaker is the platform for training and hosting your own models, and Comprehend is a task-specific NLP service.
</details>

---

### Question 2
**Scenario:** A chatbot must answer from a corpus of internal PDFs stored in S3, with citations.

A. A Bedrock Knowledge Base over the S3 corpus, with retrieval and generation returning source attribution
B. Paste the full text of every PDF into the prompt on each request, so that the model always has the source documents available to quote
C. Fine-tune the model on the PDFs so that it learns the content of the documents and can cite the source file it learned each fact from
D. Use Amazon Textract alone to extract the text of each PDF, then return the matching extract directly to the user as the answer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Knowledge Bases handle ingestion, chunking, embedding, vector storage, and retrieval with citations, which is the managed RAG path. Fine-tuning teaches style rather than facts and gives no citations. Textract extracts text, which is one input step rather than the solution.
</details>

---

### Question 3
**Scenario:** Model responses must be blocked when they contain a defined set of denied topics and PII.

A. A prompt instruction telling the model never to discuss the denied topics or output personal data, repeated at the start of every request
B. Post-hoc log review by the security team, searching the invocation logs each day for denied topics
C. Lower the temperature so the model's responses become more deterministic and so less likely to stray
D. Bedrock Guardrails with denied topics, content filters, and sensitive information filters on input and output

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Guardrails apply to both input and output independently of the model, and they can mask or block PII and enforce topic policies. A prompt instruction is advisory and can be argued with by injected content, and log review is detection rather than prevention.
</details>

---

### Question 4
**Scenario:** An agent must call internal APIs to complete multistep tasks.

A. A single prompt that describes every API and asks the model to write out the calls to run in order
B. A Knowledge Base alone, which retrieves documents about each internal API but has no way to invoke the APIs on behalf of the user
C. Bedrock Agents with action groups defined by an OpenAPI schema and backed by Lambda functions that hold the permissions
D. Step Functions alone, which runs a fixed workflow of API calls but has no model choosing the next action

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Bedrock Agents orchestrate the loop, decide which action to invoke, and call the Lambda implementations described by the action group schema. The IAM role on those Lambdas is what actually bounds the agent's authority, which is where the security design belongs.
</details>

---

### Question 5
**Scenario:** Guaranteed throughput is required for a latency-sensitive Bedrock workload.

A. Provisioned Throughput for the model
B. A larger model, since it has more capacity and so serves each request quickly even when other customers are using the service
C. Batch inference, which processes a file of prompts asynchronously at a lower price but does not give predictable latency
D. On-demand invocation with a retry policy, which scales automatically with traffic and so avoids any throttling during peak periods

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Provisioned Throughput reserves model units for predictable capacity and is required for custom models. On-demand is elastic but subject to throttling under contention, and batch inference trades latency for a lower price on offline work.
</details>

---

### Question 6
**Scenario:** Prompts and completions must never traverse the public internet.

A. An internet gateway with a security group that only allows HTTPS, so the traffic is encrypted and restricted to Bedrock's address ranges
B. A NAT gateway in a public subnet, so that instances in the private subnet can call Bedrock without being reachable
C. VPC interface endpoints (PrivateLink) for Bedrock, with the application in a private subnet and no route to the internet
D. TLS is sufficient, because the encrypted traffic cannot be read in transit even if it crosses the public internet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** PrivateLink keeps the traffic on the AWS network with a private IP in your VPC. TLS protects confidentiality in transit but the traffic still leaves your VPC, which is what a network isolation requirement usually means. NAT and internet gateways route to the internet by definition.
</details>

---

### Question 7
**Scenario:** A model must be customized on proprietary examples without that data being used to train the base model.

A. Prompt engineering only, placing the proprietary examples in every prompt as few-shot context, which keeps the base model untouched
B. Bedrock custom model fine-tuning, where the customized model is private to your account
C. Sharing the data with the provider so their team can train a private variant
D. Public fine-tuning through the provider's shared model program, where the improved model is then offered to all customers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fine-tuned models in Bedrock are private copies encrypted with your key, and the training data is not used to improve the base model. Being able to state that precisely is part of the compliance domain, because it is usually the first question legal asks.
</details>

---

### Question 8
**Scenario:** Costs are high because a long system prompt repeats on every request.

A. Increase max tokens so that the model can accept the longer system prompt in one pass and spend fewer requests on it
B. Add more replicas of the application, which spreads the repeated prompt across more instances and lowers the cost per request
C. Prompt caching for the stable prefix
D. Switch to a larger model, which follows the long system prompt more reliably and so needs fewer retries

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Caching the unchanging prefix cuts both cost and time to first token, and it requires the stable content to sit at the front of the prompt. Combine it with model routing so simple requests go to a cheaper model, which is the other major lever.
</details>

---

### Question 9
**Scenario:** A retrieval system must not return documents the requesting user is not entitled to see.

A. Rely on the model's safety training to refuse to reveal documents the user is not entitled to read, and treat that as sufficient
B. Instruct the model in the system prompt to refuse any question about documents outside the user's entitlements
C. Post-process the answer with a classifier that redacts content the user is not allowed to see before it is displayed
D. Filter at retrieval time using metadata filters bound to the user's entitlements, so that unauthorized chunks never enter the prompt context

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Authorization has to happen before content enters the context window, because once it is in the prompt the model may reveal it. Metadata filtering on the Knowledge Base query, driven by the caller's identity, is the enforcement point.
</details>

---

### Question 10
**Scenario:** A generative feature must be evaluated for quality and safety before launch and on every change.

A. Latency tests that measure response time under load before each release, which show speed but not whether answers are correct or safe
B. Manual review of a sample of outputs by the product team before launch, repeated whenever someone remembers
C. A single smoke test that sends one representative prompt and checks that a response comes back before each release, failing the release if nothing is returned
D. An automated and human evaluation suite for accuracy, groundedness, refusals and adversarial prompts, run in the pipeline

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Prompt edits and model version changes both alter behavior, so evaluation must be a gate rather than a launch activity. Bedrock model evaluation supports automatic and human workflows, and adversarial cases belong in the same suite because injection resistance regresses silently.
</details>

---

### Question 11
**Scenario:** An indirect prompt injection is embedded in a retrieved document.

A. Assume it may succeed: scope tools to the user's rights, confirm irreversible actions, and treat model output as untrusted
B. Filter the retrieved text for suspicious phrases such as "ignore previous instructions" before it reaches the prompt, and block any match
C. Increase the guardrail strictness only, raising the content filter thresholds so that injected instructions are blocked on input and output
D. Use a larger model, which follows the system prompt more reliably and so is less likely to obey instructions found in retrieved text

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** No classifier reliably distinguishes instructions from data in natural language, so the design goal is bounding consequence rather than achieving perfect detection. Guardrails help at the margin, but the tool boundary and output handling are what make a successful injection survivable.
</details>

---

### Question 12
**Scenario:** Which service converts documents into vectors and stores them for similarity search on AWS?

A. Amazon Kinesis, which ingests streaming data in real time but does not create embeddings
B. Amazon OpenSearch Serverless (or Aurora pgvector, or another supported vector store) fed by Bedrock embedding models
C. Amazon RDS for MySQL, a relational database that stores rows and supports SQL queries but has no vector index for similarity search
D. Amazon DynamoDB Streams, which captures item-level changes and is not a vector store

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The embedding model produces the vectors and a vector-capable store indexes them. Bedrock Knowledge Bases supports several backends, and the choice usually comes down to existing operational familiarity and whether you already run OpenSearch or Postgres.
</details>

---

### Question 13
**Scenario:** A regulated workload must record every prompt and response for audit.

A. Rely on application logs written by the service code, which record whatever the developers chose to log at each call
B. Enable Bedrock model invocation logging to CloudWatch Logs or S3, with retention and access controls
C. No logging is possible, because Bedrock does not retain or expose prompts and completions for customer inspection
D. Log only errors from the invocation API, which keeps volume low

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Invocation logging captures request and response data at the service level, independent of the application. Because it captures potentially sensitive content, it needs the same encryption, retention, and access restriction as the underlying data, which is part of the compliance design rather than an afterthought.
</details>

---

### Question 14
**Scenario:** A model upgrade is available. What is the safe rollout?

A. Switch all traffic to the new version on release day, because newer models are expected to match or exceed the old one
B. Evaluate the new version against the suite, then canary a small share while comparing quality, latency, and cost before full cutover
C. Wait for complaints from users and roll back only if enough tickets arrive to show a real problem
D. Run the old and new versions side by side at random permanently, never retiring either version after the upgrade

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model version change is a behavior change, and a newer model can regress on the specific prompts your application depends on. Offline evaluation catches most of it and the canary catches what the eval set does not represent.
</details>

---

### Question 15
**Scenario:** An application must choose between fine-tuning, RAG, and prompt engineering.

A. Always fine-tune, because training the model on your data gives the best accuracy for every kind of application
B. Prompt engineering first, RAG when the need is current or proprietary knowledge, fine-tuning when the need is consistent format, style, or task behavior
C. They are interchangeable, because each one changes the model's output and so any of them solves any problem equally well
D. Always use RAG, because retrieval adds current knowledge to every request and so also fixes output format and style

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The three address different problems, and cost and iteration speed rise in that order. RAG updates when your documents update; fine-tuning requires a retraining cycle. Many production systems end up using all three for different aspects of the same feature.
</details>

### Question 16
**Scenario:** A Bedrock knowledge base indexes long engineering manuals with nested sections. Answers need precise matches on a specific procedure but also the surrounding section for context.

A. Fixed-size chunking at 2,000 tokens with no overlap, so each chunk holds as much as possible
B. No chunking, so each manual is stored as a single vector
C. Hierarchical chunking (small child chunks, larger parent chunks)
D. Semantic chunking with the smallest possible buffer so chunks are very short

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hierarchical chunking is built for this: small child chunks give precise retrieval, and the parent chunk supplies the wider context to the model. Very large fixed chunks blur relevance. One vector per manual cannot match a specific procedure. Tiny semantic chunks are precise but lose the context the scenario asks for.
</details>

### Question 17
**Scenario:** Users search a knowledge base with exact part numbers such as "XR-7731-B". Semantic search often returns similar-looking but wrong parts.

A. Hybrid search (keyword plus semantic)
B. Switch to a larger embedding model so that the part numbers are understood better
C. Lower the number of results returned to one
D. Fine-tune the generation model on the part catalog

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Exact identifiers are a keyword problem; embeddings capture meaning and can treat near-identical codes as close. Hybrid search adds lexical matching while keeping semantic recall. A bigger embedding model has the same weakness. Returning one result just returns one wrong part. Fine-tuning the generator does not change what is retrieved.
</details>

### Question 18
**Scenario:** Retrieval returns the right document somewhere in the top 20 results, but the top 5 that reach the prompt are often only loosely related.

A. Increase the chunk size so that more text fits into each of the five results
B. Send all 20 results to the model on every request, whatever the cost
C. Replace the vector store with a relational database
D. Retrieve more candidates, then apply a reranking model

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Reranking scores the query against each candidate more precisely than vector similarity, pushing the truly relevant chunks to the top before the cut. Bigger chunks dilute relevance. Sending all 20 raises cost and adds noise. A relational database does not do semantic ranking.
</details>

### Question 19
**Scenario:** A team must choose a foundation model for analysing 300-page scanned contracts with tables and images. Three Bedrock models look suitable on paper.

A. Pick the model with the highest score on a public leaderboard
B. Filter on context length and modality, then run a model evaluation job on real contracts
C. Pick the cheapest model, since all three are described as suitable and quality differences between them will be small
D. Fine-tune all three models first and choose afterwards

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hard requirements (context length, image and document input) narrow the field, and evaluation on the team's own data shows which model actually performs best for the cost. Public leaderboards measure other tasks. Choosing on price alone ignores quality. Fine-tuning before knowing whether it is needed is expensive and premature.
</details>

### Question 20
**Scenario:** A European bank wants Bedrock to absorb traffic bursts by using capacity in more than one Region, but inference must stay within the EU.

A. An EU geographic cross-Region inference profile
B. Use the global cross-Region inference profile, which offers the most capacity
C. Call the model only in one EU Region and accept throttling during bursts
D. Deploy the model in a US Region and encrypt the traffic with a customer managed key

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Geographic inference profiles spread requests across Regions within a defined geography such as the EU, which meets both needs. A global profile can route anywhere. A single Region meets residency but fails the burst requirement. Encryption does not change where the data is processed.
</details>

### Question 21
**Scenario:** A Bedrock agent decides an action is needed, but the action must run inside the customer's application using that user's own session and credentials, not in a Lambda function.

A. Give the agent's Lambda function the user's password
B. Turn off the agent's action groups and hard-code the action in the prompt
C. Return of control to the application
D. Add a knowledge base that describes how the action works

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Return of control hands the chosen action and its parameters back to the calling application instead of invoking a Lambda function, so the app can execute it in the user's context. Sharing a password with a function is a security failure. A prompt cannot execute anything. A knowledge base supplies information, not actions.
</details>

### Question 22
**Scenario:** A chat UI should show the answer as it is generated instead of waiting several seconds for the full response.

A. Call the model with a lower max token limit so it finishes sooner
B. A streaming API such as ConverseStream, relayed to the client
C. Poll the model every second for the latest partial answer
D. Use batch inference and display the results when the job completes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Streaming APIs return tokens as they are produced, and a transport that supports streaming delivers them to the browser. Fewer tokens shortens answers rather than streaming them. Polling is not how model responses work. Batch inference is asynchronous and slower, the opposite of what the UI needs.
</details>

### Question 23
**Scenario:** A claims workflow must extract fields with a model, validate them, wait up to three days for a human adjuster's approval, retry failed steps, and then update a core system, in a fixed order.

A. One Lambda function that calls each step in sequence and sleeps while waiting for approval
B. A Bedrock agent with no other components, trusting it to remember the approval for three days
C. A cron job that checks a spreadsheet for approvals every hour
D. AWS Step Functions with retries and a task token for the approval

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Step Functions provides fixed ordering, built-in retries and long waits via the callback (task token) pattern, and it can call Bedrock directly. Lambda has a 15-minute limit, so it cannot sleep for days. An agent alone is not a durable workflow engine. A spreadsheet poller has no retries, ordering or audit trail.
</details>

### Question 24
**Scenario:** An application must be able to switch between models from different providers on Bedrock without rewriting request and response handling for each one.

A. The Converse API
B. Write a separate InvokeModel payload builder for each provider and keep them in sync
C. Use only one provider's models forever to avoid the issue
D. Call each provider's own public API directly instead of Bedrock

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Converse API normalises requests and responses across models, so switching is mostly a model ID change. Per-provider payload builders are the maintenance burden the scenario wants to avoid. Locking to one provider removes the choice. Calling each vendor directly multiplies integrations and loses Bedrock's controls.
</details>

### Question 25
**Scenario:** A RAG assistant sometimes adds details that are not in the retrieved documents. The team wants such answers blocked at run time.

A. A denied topic in Bedrock Guardrails listing "made-up facts"
B. A contextual grounding check in Bedrock Guardrails, with grounding and relevance thresholds
C. A word filter that blocks the words "maybe" and "probably"
D. A higher temperature, so the model explores more of the source

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Contextual grounding checks score whether the response is supported by the reference source and relevant to the query, and block it below the thresholds. Denied topics block subjects, not unsupported claims. Word filters match strings, not meaning. Higher temperature increases invention.
</details>

### Question 26
**Scenario:** A call-centre summariser must keep summaries useful but must not reveal customers' phone numbers or email addresses.

A. Block every response that contains any personal information
B. A denied topic named "contact details"
C. A Guardrails sensitive information filter set to mask phone numbers and email addresses
D. Tell the model in the prompt never to include contact details

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sensitive information filters can either block or mask detected PII; masking replaces the values while keeping the rest of the summary. Blocking whole responses loses the useful content. Denied topics are for subjects, not entity types. A prompt instruction is not an enforced control.
</details>

### Question 27
**Scenario:** A company uses a model hosted on Amazon SageMaker and another outside AWS, and wants the same safety policies it applies on Bedrock to cover both.

A. Call the ApplyGuardrail API with the existing guardrail
B. Move both models into Bedrock before any safety controls can be used
C. Recreate the policies as regular expressions in each application
D. Rely on each model provider's built-in safety settings

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** ApplyGuardrail runs a guardrail on any text without invoking a Bedrock model, so one policy can cover models hosted anywhere. Migrating models is unnecessary. Hand-written regexes drift from the central policy and miss semantic checks. Vendor defaults are different policies, not the company's.
</details>

### Question 28
**Scenario:** Two million archived documents must be summarised once. Nobody needs the results before tomorrow, and cost matters most.

A. Provisioned Throughput sized for the full job
B. On-demand InvokeModel calls from a loop, as fast as quotas allow
C. A streaming API, so each summary starts sooner
D. Bedrock batch inference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Batch inference suits large, latency-tolerant jobs and is priced at a discount to on-demand for supported models. Provisioned Throughput is a commitment for steady traffic. A tight on-demand loop pays full price and fights throttling. Streaming improves perceived latency for one user, not bulk cost.
</details>

### Question 29
**Scenario:** An on-demand Bedrock workload hits ThrottlingException errors during daily peaks. Traffic outside peaks is light.

A. Buy Provisioned Throughput sized for the peak and leave it running all day
B. Lower the temperature so each request is cheaper to serve
C. Backoff retries plus a cross-Region inference profile
D. Cache every response forever so the model is called less

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Backoff absorbs short spikes, cross-Region inference adds capacity during bursts, and a quota increase covers sustained growth. Provisioned capacity sized for a short peak sits idle most of the day. Temperature does not affect throttling. Caching every response is wrong for varied prompts and can serve stale answers.
</details>

### Question 30
**Scenario:** A RAG chatbot gives wrong answers to some questions. The team needs to know whether retrieval or generation is at fault.

A. Swap the generation model for a bigger one and see if answers improve
B. Inspect what was retrieved for the failing questions (for example with the Retrieve API) and evaluate retrieval and generation separately, such as with a knowledge base evaluation job
C. Increase the number of results returned and redeploy
D. Rewrite the system prompt until the failing answers are right

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separating the two stages shows where the error starts: if the right chunks are not retrieved, the model never had a chance; if they are, the issue is in generation or the prompt. Swapping models, adding results or rewriting prompts are guesses that may hide the real cause.
</details>

---

## Where to go deeper

- [AIP-C01 cert page](../aws/professional/genai-developer-aip-c01/README.md) - notes, practice plan, strategy
- [AI Practitioner practice questions](aws-ai-practitioner.md) - the foundational AI exam
- [Prompt injection defense](../../safety/security/prompt-injection-defense.md) - question 11 in depth
- [AI security topic index](../../safety/README.md) - the security domain across the repo
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
