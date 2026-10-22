# OCI AI Foundations Associate (1Z0-1122) - Practice Questions

30 questions for OCI AI Foundations prep. Two categories dominate: concept definitions and OCI service selection.

> **Cert page:** [exams/oracle/oci-ai-foundations/](../oracle/oci-ai-foundations/README.md)

---

### Question 1
**Scenario:** A model must predict whether a customer will churn. What type of problem is this?

A. Regression
B. Binary classification
C. Dimensionality reduction with PCA
D. Clustering of similar customers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Churn is a category (will churn, will not churn), so it is classification. Regression predicts a continuous value such as a price. Clustering and dimensionality reduction are unsupervised techniques that require no labels.
</details>

---

### Question 2
**Scenario:** A fraud model scores 99.9% accuracy on a dataset where 99.9% of transactions are legitimate, but catches almost no fraud. What metric should be used instead?

A. Mean squared error, because it penalizes large prediction errors more heavily and so exposes the missed fraud cases
B. Accuracy is fine, because 99.9% is close to perfect; the model only needs more fraud examples collected over time
C. R-squared, because it shows how much of the variation in the fraud label the model explains
D. Recall, or F1, because accuracy is misleading on imbalanced data

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A model predicting "not fraud" every time scores 99.9% and is useless. Recall measures what proportion of actual fraud was caught, which is the business concern. MSE and R-squared are regression metrics.
</details>

---

### Question 3
**Scenario:** A model performs excellently on training data and poorly on new data. What is happening, and what is one fix?

A. Class imbalance; resample the training set
B. Data drift; retrain on the latest production data
C. Overfitting; use more data, regularization, or early stopping
D. Underfitting, where the model is too simple to learn the pattern; switch to a more complex model with more layers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** High training performance with low test performance is the signature of overfitting: the model memorized the training data including its noise. Underfitting performs poorly on both. Drift is degradation over time in production, not a train-test gap at the outset.
</details>

---

### Question 4
**Scenario:** A company wants to analyze sentiment in thousands of product reviews. It has no machine learning staff.

A. OCI Data Labeling
B. OCI Generative AI custom fine-tuned model
C. OCI Data Science with notebook sessions
D. OCI Language sentiment analysis

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI Language is a ready-made service providing sentiment analysis with no model building. "Without machine learning expertise" points at the ready-made layer. Data Science is for building your own model, and Data Labeling prepares training data.
</details>

---

### Question 5
**Scenario:** A company must extract totals and dates from scanned supplier invoices.

A. OCI Language, which analyzes text for entities and sentiment once the text is extracted
B. OCI Document Understanding, which extracts key-value fields and tables from invoices and forms
C. OCI Vision, which classifies images and detects objects
D. OCI Speech, which transcribes recorded audio into text

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Document Understanding is purpose-built for extracting structured fields from forms, invoices, receipts, and identity documents. Vision handles general image classification and object detection, including OCR, but Document Understanding is the service for form field extraction.
</details>

---

### Question 6
**Scenario:** A chatbot must answer employee questions grounded in internal policy documents, with citations.

A. OCI Generative AI Agents, using a knowledge base built over the policy documents
B. Base model prompting alone, with the policies pasted into each prompt
C. Fine-tune a model on the policy documents
D. OCI Language text classification to route each question to a topic

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Generative AI Agents provides retrieval-augmented answering over enterprise data with citations. Prompting alone gives the model no access to the documents. Fine-tuning changes behavior rather than knowledge, freezes the content at training time, and cannot cite sources.
</details>

---

### Question 7
**Scenario:** What is the difference between a parameter and a hyperparameter?

A. Parameters are learned during training; hyperparameters are set before training
B. They are synonyms for the model's learned weights
C. Hyperparameters are learned from the data during training, while parameters are fixed constants chosen up front
D. Parameters are for deep learning only, hyperparameters for classical

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Weights and biases are parameters, learned by the training process. Learning rate, epochs, batch size, and layer count are hyperparameters, chosen before training begins.
</details>

---

### Question 8
**Scenario:** Which architecture is most appropriate for image classification?

A. Convolutional neural network
B. RNN
C. Transformer decoder with attention layers
D. Autoencoder with a bottleneck layer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Convolutional neural networks detect local spatial patterns and reuse filters across an image, which suits vision. RNNs handle sequences, transformer decoders generate text (though transformers are increasingly used for vision too), and autoencoders compress and reconstruct.
</details>

---

### Question 9
**Scenario:** A model gives a confident, plausible, factually wrong answer. What is this called, and what most reduces it?

A. Drift; retraining on newer data
B. Bias; rebalancing the dataset
C. Hallucination; grounding the model in retrieved source text
D. Overfitting, where the model memorizes noise in its training data; applying regularization to the weights

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hallucination arises because the model predicts likely text rather than retrieving verified facts. Grounding supplies authoritative context and instructs the model to answer only from it, which is the primary mitigation, usually alongside citations and an explicit escape hatch.
</details>

---

### Question 10
**Scenario:** A team needs distributed training across many GPUs. Which OCI capability is specifically relevant?

A. OCI Language custom models, which train a text classifier on labeled data using a managed service
B. RDMA cluster networking on AI infrastructure
C. Autonomous Database, which provides managed storage and SQL processing for transactional workloads
D. OCI Data Labeling, which lets people annotate images and text to build supervised training sets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Once training spans more than one node, the interconnect becomes the bottleneck. RDMA cluster networking provides the low-latency, high-throughput node-to-node communication distributed training needs.
</details>

---

### Question 11
**Scenario:** Which describes unsupervised learning?

A. Learning a policy from reward feedback, where an agent is scored on each outcome
B. Learning to predict a label from labeled examples, such as spam
C. Learning from a teacher model that supplies target outputs
D. Finding structure in unlabeled data without target labels, such as clustering or anomaly detection

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unsupervised learning has no labels and finds structure. Supervised learning uses labeled data to predict a label. Reinforcement learning learns a policy from environmental reward.
</details>

---

### Question 12
**Scenario:** Why is a separate test set held back rather than reusing the validation set?

A. Because validation sets cannot be used for classification problems, only for regression tasks
B. To reduce memory use, since the validation set is too large to keep loaded during the final evaluation of the model
C. Because tuning against a set contaminates it, so an untouched set is needed for an honest final estimate
D. To speed up training, since the model can stop sooner when it only reports one single final score at the very end

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The validation set is used to tune hyperparameters, so performance on it is optimistically biased. The test set is used once, at the end, to estimate real-world performance.
</details>

---

### Question 13
**Scenario:** A team wants semantic search over data that already lives in Oracle Autonomous Database, without operating a separate vector store.

A. AI Vector Search in Autonomous Database
B. OCI Vision, which could index images as vectors but does not store or search your relational rows
C. OCI Speech, which converts audio to text and so can feed a transcript into a search index
D. OCI Data Science model deployment, which serves a model endpoint but needs a separate vector store for search

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AI Vector Search stores embeddings as a native column type and performs similarity search in SQL, so vectors sit beside the relational data with no second system to operate or secure.
</details>

---

### Question 14
**Scenario:** Which responsible AI principle is addressed by being able to explain to a rejected loan applicant why the decision was made?

A. Privacy, covering personal data protection
B. Availability, keeping the service up
C. Explainability of each decision to the applicant
D. Fairness, which checks that approval rates are equitable across demographic groups of applicants

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Explainability is the ability to explain a decision to the person it affects. Fairness concerns whether outcomes are equitable across groups, and privacy concerns protection of personal data. Both matter here, but the stated requirement is explanation.
</details>

---

### Question 15
**Scenario:** A team wants to train a custom model in a managed notebook environment and serve it as an API endpoint.

A. OCI Document Understanding, which extracts fields from invoices and forms but is not a place to train your own model
B. OCI Data Science, using notebook sessions, the model catalog, and model deployment
C. OCI Language custom models, which train a text classifier through a managed service rather than in a notebook
D. OCI Generative AI, which hosts and fine-tunes foundation models and serves them through managed endpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Train a custom model" and "notebook" both point at the ML platform layer. OCI Data Science provides notebook sessions, a versioned model catalog, and model deployment as scalable HTTP endpoints. Generative AI serves foundation models rather than your own trained model.
</details>

---

### Question 16
**Scenario:** A call center wants text transcripts of thousands of recorded customer calls so it can search them. It has no machine learning staff.

A. OCI Language
B. OCI Vision
C. OCI Data Science with a custom model
D. OCI Speech

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI Speech is the pretrained service that converts audio to text. OCI Language analyzes text once it exists, and OCI Vision works on images. Building a custom speech model in Data Science is unnecessary work when a ready service exists and nobody on staff builds models.
</details>

---

### Question 17
**Scenario:** A manufacturer wants to detect and locate scratches in photos of products on an assembly line, using its own labeled images.

A. OCI Vision, with a custom object detection model
B. OCI Document Understanding, reading the photos as documents
C. OCI Speech, describing each photo as audio
D. OCI Language, classifying the photo file names

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OCI Vision handles image analysis, and its custom models can be trained on labeled images to detect and locate specific objects such as defects. Document Understanding extracts text and fields from documents, Speech handles audio, and Language works on text, not pixels.
</details>

---

### Question 18
**Scenario:** Business analysts want to ask questions such as "which region had the highest sales last quarter?" in plain English against data in Oracle Autonomous Database, without writing SQL.

A. OCI Vision, reading charts exported from the database
B. A custom chatbot trained from scratch on the database tables
C. Select AI in Autonomous Database
D. OCI Speech, so the questions can be spoken aloud

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Select AI uses a large language model to turn a natural language question into SQL and run it in Autonomous Database. Training a chatbot from scratch is far more work and goes stale, Vision analyzes images, and Speech transcribes audio without querying anything.
</details>

---

### Question 19
**Scenario:** A support team receives tickets in Spanish, French and German and wants them translated into English automatically before routing.

A. OCI Vision, with text detection on screenshots of each ticket
B. OCI Language, using its text translation capability
C. OCI Document Understanding, extracting a table of words
D. OCI Data Science, training a translation model from scratch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Language includes pretrained text translation along with sentiment, entity and classification features. Vision and Document Understanding extract text from images and documents but do not translate it, and building a translation model from scratch is unnecessary when a managed service exists.
</details>

---

### Question 20
**Scenario:** A real estate firm wants a model that predicts the sale price of a house from its size, location and age.

A. Binary classification
B. Clustering
C. Multi-class classification
D. Regression

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Predicting a continuous numeric value such as a price is regression. Classification predicts categories, binary for two classes and multi-class for more. Clustering groups unlabeled data and does not predict a target at all.
</details>

---

### Question 21
**Scenario:** An email filter moves suspected spam to a junk folder. Users are most upset when an important real email is wrongly marked as spam. Which metric should the team prioritize?

A. Recall for the spam class
B. Training loss
C. Precision for the spam class
D. Number of emails processed per second

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Precision measures how many emails flagged as spam really are spam, so high precision means few real emails are wrongly flagged, which is the costly error here. Recall measures how much spam is caught and favors flagging more. Training loss and throughput say nothing about this trade-off.
</details>

---

### Question 22
**Scenario:** A model scores poorly on both the training data and new data. What is the most likely problem?

A. Underfitting; use a more capable model or better features
B. Overfitting; collect a smaller training dataset
C. Data leakage; the test set is too similar to training
D. Nothing; poor training scores are normal

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Poor performance on training data itself means the model is too simple to capture the pattern, which is underfitting. The fix is a more capable model, better features or longer training. Overfitting shows strong training and weak test results, and leakage inflates scores rather than lowering them.
</details>

---

### Question 23
**Scenario:** Why did transformers largely replace recurrent neural networks (RNNs) for language tasks?

A. Transformers need no training data, so they can be used straight away
B. Transformers process one word at a time, which makes them more accurate
C. Transformers only work on images, which frees RNNs for other tasks
D. Self-attention relates all tokens at once, so training runs in parallel

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Self-attention lets every token attend to every other token directly, which captures long-range relationships and allows parallel processing across a sequence. RNNs process tokens one step at a time, which is slower and loses information over long sequences. Transformers still need training data and are used for text, images and more.
</details>

---

### Question 24
**Scenario:** A user pastes a very long contract into a chat with an LLM, and the model ignores the beginning of the document. What limit has most likely been exceeded?

A. The model's temperature setting
B. The model's context window, measured in tokens
C. The number of layers in the model
D. The model's training data cutoff

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The context window is the maximum number of tokens a model can consider at once, so text beyond it is cut off or dropped. Temperature controls randomness, the number of layers is a fixed part of the architecture, and the training cutoff is about what the model learned, not what it can read in one request.
</details>

---

### Question 25
**Scenario:** A team uses an LLM to answer factual questions about company policies and wants the answers to be consistent and focused rather than creative.

A. Increase the temperature
B. Increase the maximum output tokens
C. Lower the temperature
D. Remove the system prompt

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Temperature controls how random token selection is; a low value makes outputs more focused and consistent, which suits factual answers. A high temperature makes them more varied and creative. Output length does not affect consistency, and removing the system prompt removes guidance.
</details>

---

### Question 26
**Scenario:** What are embeddings in the context of LLM applications?

A. Encrypted copies of documents stored inside the model weights
B. The prompts that are hidden inside a chatbot's system settings
C. Images inserted into a document alongside the text they describe
D. Numeric vectors where texts with similar meaning lie close together

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An embedding model turns text into a vector of numbers, positioned so that similar meanings are near each other, which enables semantic search and retrieval for RAG. Embeddings are not encrypted documents, hidden prompts or pictures.
</details>

---

### Question 27
**Scenario:** A team's LLM gives answers in the wrong format and tone. What is usually the cheapest and fastest thing to try first?

A. Improve the prompt with clear instructions and examples
B. Fine-tune the model on thousands of labeled examples
C. Pretrain a new model on the company's own documents
D. Move the workload to a larger GPU cluster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prompt engineering, with clear instructions and a few examples, changes format and tone with no training cost and is the standard first step. Fine-tuning is the next option if prompting is not enough, pretraining is vastly more expensive, and bigger hardware does not change what the model writes.
</details>

---

### Question 28
**Scenario:** A hiring model trained on ten years of past decisions recommends far fewer women than men for technical roles. Which responsible AI concern does this show?

A. Transparency
B. Fairness, from bias in the training data
C. Reliability under heavy load
D. Privacy of the applicants' data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model trained on historically biased decisions learns and repeats that bias, which is a fairness problem. Fixing it means testing outcomes across groups and addressing the data and model. Transparency is about explaining decisions, reliability about consistent operation, and privacy about protecting personal data.
</details>

---

### Question 29
**Scenario:** A robot learns to walk by trying movements and getting a reward when it moves forward and a penalty when it falls. What kind of learning is this?

A. Supervised learning
B. Unsupervised learning
C. Reinforcement learning
D. Transfer learning

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In reinforcement learning an agent learns from rewards and penalties received for its actions in an environment. Supervised learning uses labeled examples, unsupervised learning finds structure in unlabeled data, and transfer learning reuses a model trained on another task.
</details>

---

### Question 30
**Scenario:** Why are GPUs generally preferred over CPUs for training deep learning models?

A. GPUs have more storage space for training datasets
B. GPUs run any single instruction much faster than a CPU can
C. GPUs are needed to connect a model to the internet
D. GPUs run many matrix operations in parallel

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Deep learning is dominated by large matrix multiplications, and GPUs have thousands of cores that perform these in parallel. A CPU has fewer, faster cores suited to sequential work, so a single instruction is not faster on a GPU. Storage and internet access are unrelated to the choice.
</details>

---

## Scoring guide

- **26-30 correct (85%+):** Ready. The pass mark is 65%, so this puts you well clear.
- **20-25 correct (65-84%):** Drill the service selection table in the [fact sheet](../oracle/oci-ai-foundations/fact-sheet.md#the-service-selection-table); those are the fastest marks on the paper.
- **Below 20:** Work through the free Oracle University learning path and the [domain notes](../oracle/oci-ai-foundations/README.md#notes).
