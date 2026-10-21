# Azure AI Fundamentals (AI-900) Practice Questions

40 scenario-based questions weighted by exam domain.

## Exam Domain Breakdown
| Domain | Weight | Questions |
|--------|--------|-----------|
| Describe Artificial Intelligence workloads and considerations | 15-20% | 7 |
| Describe fundamental principles of machine learning on Azure | 20-25% | 9 |
| Describe features of computer vision workloads on Azure | 15-20% | 7 |
| Describe features of Natural Language Processing workloads on Azure | 15-20% | 7 |
| Describe features of generative AI workloads on Azure | 15-20% | 10 |

> **Cert page:** [exams/azure/ai-900/](../azure/ai-900/README.md)

---

## Domain 1: Describe Artificial Intelligence Workloads and Considerations (Questions 1-7)

### Question 1
**Scenario:** A company wants to use AI to automate customer support responses. Before implementing AI, leadership asks: "What types of problems can AI actually solve?" Which answer best describes the types of workloads suitable for AI?

A. AI only works for mathematical calculations
B. AI can solve any problem without limitations
C. AI cannot be used for business problems
D. AI is best suited for tasks involving prediction, classification, pattern recognition, and automation of cognitive tasks like language understanding and image analysis

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AI excels at tasks that involve learning patterns from data: predicting outcomes (sales forecasting), classifying items (spam detection), recognizing patterns (anomaly detection), and automating cognitive tasks (understanding language, analyzing images). Understanding appropriate use cases is fundamental to AI implementation.

**Key Concept:** [What is AI?](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/1-introduction)
</details>

### Question 2
**Scenario:** A healthcare organization wants to use AI to assist with medical diagnoses. A team member raises concerns about the AI making unfair decisions. What AI principle addresses this concern?

A. Fairness - ensuring AI systems treat all people equitably and don't discriminate
B. Speed - ensuring the diagnostic system returns results quickly enough for busy clinics to use it
C. Cost reduction - lowering the price of each diagnosis for the clinic and for its patients
D. Performance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fairness is a core principle of responsible AI. AI systems should not discriminate based on gender, ethnicity, or other factors. In healthcare, this means ensuring the AI performs equally well across different patient populations and doesn't perpetuate existing biases in training data.

**Key Concept:** [Responsible AI Principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

### Question 3
**Scenario:** A financial services company implements an AI system for loan approvals. Regulators require the company to explain why any loan application is rejected. Which responsible AI principle does this requirement address?

A. Transparency and Explainability - being able to understand and explain AI decisions
B. Performance
C. Privacy
D. Security - protecting the model and its data from unauthorized access, tampering, and adversarial attacks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Transparency and explainability require that AI systems can explain their decisions in understandable terms. For loan approvals, this means being able to tell applicants why they were rejected - not just "the AI decided" but specific factors like income, credit history, etc.

**Key Concept:** [AI Transparency](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

### Question 4
**Scenario:** A company is considering AI to automate a task currently done by employees. Management wants to ensure humans remain in control of important decisions. Which responsible AI principle requires this?

A. Accountability and human oversight - humans can monitor and control AI
B. Fairness - treating every group of people equitably in the decisions the system makes
C. Privacy - protecting the personal data that is used to train and run the system
D. Reliability - ensuring the system performs consistently and recovers gracefully when conditions change

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Accountability requires that people are responsible for AI system behavior. Human oversight ensures that humans can intervene, override, or stop AI systems. This is especially important for high-stakes decisions where AI should assist rather than replace human judgment.

**Key Concept:** [AI Accountability](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

### Question 5
**Scenario:** A retail company wants to use customer purchase data to train an AI model for product recommendations. A data protection officer asks about protecting customer privacy. Which responsible AI consideration applies?

A. Privacy and Security - ensuring personal data is protected and used appropriately
B. Cost of implementation
C. Model accuracy
D. Speed of recommendations

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Privacy and security are fundamental responsible AI principles. AI systems must handle personal data appropriately, comply with data protection regulations (like GDPR), and ensure data used for training doesn't expose sensitive information. This includes data minimization and secure handling.

**Key Concept:** [AI Privacy](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

### Question 6
**Scenario:** An AI system for detecting manufacturing defects occasionally misses defective products, and sometimes incorrectly flags good products as defective. Which responsible AI principle requires the system to perform consistently and handle these situations predictably?

A. Transparency - being able to explain why the system flagged or missed a specific product to plant engineers
B. Fairness - treating all groups of people equitably in what the system decides
C. Reliability and Safety - systems work dependably and do no harm
D. Inclusiveness - designing the system so that people of all abilities can use it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reliability and safety mean AI systems perform consistently under various conditions and fail gracefully when errors occur. For defect detection, this means understanding and communicating the system's accuracy, having safeguards for missed defects, and not causing safety issues from false positives/negatives.

**Key Concept:** [AI Reliability](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

### Question 7
**Scenario:** A company's AI chatbot is only effective for users who speak formal English. Users who speak with regional dialects or non-native speakers have poor experiences. Which responsible AI principle is being violated?

A. Inclusiveness - designing AI to work for people with diverse abilities, languages, and backgrounds
B. Security
C. Transparency - publishing documentation that explains how the chatbot language model was trained and tested
D. Reliability

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Inclusiveness ensures AI systems are designed to engage and empower everyone, regardless of ability, language proficiency, or background. An English-only chatbot that fails for dialects excludes many users. Responsible AI should accommodate diverse users through broader language support and understanding.

**Key Concept:** [AI Inclusiveness](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)
</details>

---

## Domain 2: Describe Fundamental Principles of Machine Learning on Azure (Questions 8-16)

### Question 8
**Scenario:** A real estate company wants to predict house prices based on features like size, location, and number of bedrooms. The price is a continuous numeric value. What type of machine learning task is this?

A. Regression - predicting a continuous numeric value
B. Reinforcement learning - an agent learns by trial and error from rewards
C. Classification
D. Clustering - grouping similar houses together without using labels

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Regression predicts continuous numeric values. Since house prices can be any dollar amount (not discrete categories), this is a regression problem. The model learns relationships between features (size, location) and the target variable (price) to predict prices for new houses.

**Key Concept:** [Regression](https://docs.microsoft.com/learn/modules/create-regression-model-azure-machine-learning-designer/)
</details>

### Question 9
**Scenario:** A bank wants to build a model that predicts whether a loan application will be approved or denied. The outcome is one of two categories. What type of machine learning task is this?

A. Regression
B. Computer vision
C. Binary Classification - predicting one of two categories (approved/denied)
D. Clustering

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Binary classification predicts one of two possible classes (yes/no, approved/denied, spam/not spam). The model learns patterns in historical loan data (features like income, credit score) to predict which class new applications belong to.

**Key Concept:** [Classification](https://docs.microsoft.com/learn/modules/create-classification-model-azure-machine-learning-designer/)
</details>

### Question 10
**Scenario:** A marketing team has customer data but doesn't know how many customer segments exist or what defines them. They want the model to find natural groupings in the data. What type of machine learning task is this?

A. Regression
B. Classification - assigning each customer to a predefined, labeled category
C. Clustering - finding natural groupings in unlabeled data
D. Object detection

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Clustering is unsupervised learning that finds natural groups in data without predefined labels. The algorithm identifies patterns and similarities, grouping similar customers together. Unlike classification, you don't tell the model what groups exist - it discovers them.

**Key Concept:** [Clustering](https://docs.microsoft.com/learn/modules/create-clustering-model-azure-machine-learning-designer/)
</details>

### Question 11
**Scenario:** A data scientist is building a machine learning model. They split their data into training data (to train the model) and test data (to evaluate it). Why is this split important?

A. To evaluate performance on data the model has not seen, measuring how well it generalizes
B. To speed up training
C. The split is not important because the model learns the same patterns whichever rows are used for training
D. To reduce storage costs by keeping only a small sample of the data in the workspace after training

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The train/test split evaluates how well a model generalizes to new data. If you evaluate on training data, you can't tell if the model learned patterns or just memorized. Test data simulates real-world scenarios where the model sees new data. This reveals overfitting problems.

**Key Concept:** [Model Training and Evaluation](https://docs.microsoft.com/learn/modules/create-regression-model-azure-machine-learning-designer/6-evaluate-model)
</details>

### Question 12
**Scenario:** After training a classification model to detect email spam, a data scientist evaluates it and finds: 95% accuracy, but the model correctly identifies only 60% of actual spam emails. Which metric captures this spam detection performance?

A. Accuracy
B. F1 score
C. Recall (Sensitivity) - the percentage of actual positive cases correctly identified
D. Precision

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Recall (also called sensitivity or true positive rate) measures what percentage of actual positive cases (spam) the model correctly identifies. High accuracy can be misleading when classes are imbalanced. If 95% of emails are not spam, predicting "not spam" always gives 95% accuracy but 0% recall for spam.

**Key Concept:** [Model Metrics](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/5-binary-classification)
</details>

### Question 13
**Scenario:** A company wants to build machine learning models but doesn't have data scientists who can write code. They want a visual interface to create models. What Azure service provides this capability?

A. Azure Machine Learning Designer - a visual drag-and-drop interface for building ML models
B. Azure Virtual Machines - rent compute where data scientists install and run ML frameworks themselves
C. Azure SQL Database
D. Azure Blob Storage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Machine Learning Designer provides a visual, drag-and-drop interface for building machine learning pipelines. Users connect data, preprocessing, training, and evaluation components without writing code. This enables non-programmers to build and deploy ML models.

**Key Concept:** [Azure ML Designer](https://docs.microsoft.com/azure/machine-learning/concept-designer)
</details>

### Question 14
**Scenario:** A company has domain experts who understand their business data well but aren't machine learning experts. They want to build a model where the system automatically selects the best algorithm and parameters. What Azure capability helps with this?

A. No automation available
B. Manual hyperparameter tuning - experts run repeated training jobs and adjust every setting by hand in notebooks
C. Write your own custom algorithms from scratch in Python and compare their results against each other by hand
D. Automated Machine Learning (AutoML) that automatically tests algorithms and optimizes performance

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Automated Machine Learning (AutoML) automatically tests multiple algorithms (regression, classification models), performs feature engineering, and tunes hyperparameters. It finds the best performing model for your data without requiring ML expertise to select and configure algorithms.

**Key Concept:** [Automated ML](https://docs.microsoft.com/azure/machine-learning/concept-automated-ml)
</details>

### Question 15
**Scenario:** A trained machine learning model needs to be made available for applications to make predictions. The model should handle multiple simultaneous prediction requests. What is the process of making a model available for predictions called?

A. Training
B. Model Deployment - making a trained model available as a service for inference/predictions
C. Data cleaning
D. Feature engineering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Deployment makes a trained model available for inference (predictions) on new data. Azure Machine Learning can deploy models as web services (endpoints) that applications call via REST APIs. This enables real-time predictions at scale with multiple concurrent requests.

**Key Concept:** [Model Deployment](https://docs.microsoft.com/azure/machine-learning/concept-endpoints)
</details>

### Question 16
**Scenario:** A data scientist notices their model performs perfectly on training data but poorly on test data. What problem does this indicate?

A. Insufficient training data - the model has too few rows to learn any pattern, so it fails on training data too
B. Good generalization - the model scores about as well on unseen data as it does on its training data, as expected
C. Overfitting - the model memorized training data patterns instead of learning generalizable patterns
D. Underfitting

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Overfitting occurs when a model learns training data too well, including noise and outliers, failing to generalize to new data. Signs include high training accuracy with poor test accuracy. Solutions include more training data, simpler models, regularization, or cross-validation.

**Key Concept:** [Overfitting](https://learn.microsoft.com/en-us/azure/machine-learning/concept-manage-ml-pitfalls)
</details>

---

## Domain 3: Describe Features of Computer Vision Workloads on Azure (Questions 17-23)

### Question 17
**Scenario:** A security company wants to detect when people enter a restricted area using camera footage. They need to identify that a person is present in the frame. What computer vision capability is this?

A. Optical character recognition
B. Object Detection - identifying and locating objects (people) within an image
C. Image generation
D. Image classification

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Object detection identifies objects in images and provides their locations (bounding boxes). Unlike classification which labels entire images, object detection finds multiple objects and where they are. For security, this detects and locates people within camera footage.

**Key Concept:** [Object Detection](https://docs.microsoft.com/learn/modules/detect-objects-images/)
</details>

### Question 18
**Scenario:** A factory wants to automatically read serial numbers printed on products passing on a conveyor belt. The serial numbers are text printed on product labels. What computer vision capability is needed?

A. Face detection
B. Optical Character Recognition (OCR) - extracting text from images
C. Image classification - assigning one category label to the entire image rather than reading text
D. Image segmentation - labeling every pixel to outline each region of the picture

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Optical Character Recognition (OCR) extracts text from images, converting printed or handwritten text into machine-readable text. Azure AI Vision provides OCR capabilities that can read serial numbers, labels, signs, and documents from images.

**Key Concept:** [OCR with Azure AI Vision](https://docs.microsoft.com/azure/cognitive-services/computer-vision/overview-ocr)
</details>

### Question 19
**Scenario:** A medical imaging company wants to categorize X-ray images as "normal" or "showing pneumonia" to assist radiologists. Each image receives a single overall label. What computer vision task is this?

A. Image segmentation - labeling each pixel of the image to outline regions such as organs
B. Object detection
C. OCR
D. Image Classification - assigning a category label to an entire image

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Image classification assigns one or more category labels to an entire image. The model learns to associate visual patterns with categories. For X-rays, it learns patterns associated with "normal" vs "pneumonia" to classify new images. This differs from detection which locates specific areas.

**Key Concept:** [Image Classification](https://docs.microsoft.com/learn/modules/classify-images/)
</details>

### Question 20
**Scenario:** A retail company wants to implement a checkout system that recognizes when known employees approach. The system should identify individuals based on their faces. What Azure service provides this capability?

A. Azure AI Document Intelligence - extracting fields and tables from invoices and receipts
B. Azure AI Face - face detection, recognition and identification
C. Computer Vision image analysis - tagging and describing generic objects in photos without identity matching
D. Custom Vision - training your own image classifier from labeled images

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure AI Face service provides face detection and recognition capabilities. It can detect faces in images, identify individuals by comparing faces against enrolled persons, and verify if two faces belong to the same person. Note: Face API usage for identification requires approval due to ethical considerations.

**Key Concept:** [Azure AI Face](https://docs.microsoft.com/azure/cognitive-services/face/overview)
</details>

### Question 21
**Scenario:** A company wants to train a custom model to identify their specific products (not general objects) from images. They have their own labeled training images. What Azure service allows training custom image classification models?

A. Custom Vision - for training custom image classification and object detection models with your own data
B. Azure AI Language
C. Azure AI Vision (general API)
D. Azure AI Document Intelligence

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Custom Vision allows training custom image classification and object detection models using your own labeled images. Upload images, label them, train, and deploy. This is ideal when pre-built models don't recognize your specific objects (custom products, industry-specific items). Custom Vision remains supported until its planned retirement on September 25, 2028. For new work Microsoft recommends Azure Machine Learning automated ML for custom image models.

**Key Concept:** [What is Custom Vision?](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview)
</details>

### Question 22
**Scenario:** A company receives thousands of scanned invoices daily. They need to automatically extract vendor name, invoice number, total amount, and line items from these invoices. What Azure service specializes in this document extraction?

A. Computer Vision OCR only - reads the raw text lines but does not return labeled invoice fields such as vendor or total
B. Translator
C. Azure AI Language
D. Azure AI Document Intelligence (Form Recognizer) - for extracting structured data from documents

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure AI Document Intelligence (formerly Form Recognizer) extracts structured data from documents. Pre-built models handle invoices, receipts, and business cards. Custom models can be trained for specific document types. It goes beyond OCR by understanding document structure and extracting key-value pairs.

**Key Concept:** [Document Intelligence](https://docs.microsoft.com/azure/cognitive-services/form-recognizer/overview)
</details>

### Question 23
**Scenario:** A content platform wants to automatically moderate user-uploaded images, detecting adult content, violence, or other inappropriate material. What Azure AI capability addresses this?

A. Face detection - finding human faces and returning their positions in each image
B. Azure AI Content Safety - detecting inappropriate content in images
C. Custom Vision - training your own image classifier from labeled examples of the company's products and logos
D. OCR - reading printed and handwritten text out of the images that users upload

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure AI Content Safety (and Azure AI Vision's content moderation features) detect inappropriate content including adult content, violence, and other harmful material in images. This enables platforms to automatically moderate user-generated content at scale before human review.

**Key Concept:** [Content Safety](https://docs.microsoft.com/azure/cognitive-services/content-safety/overview)
</details>

---

## Domain 4: Describe Features of Natural Language Processing Workloads on Azure (Questions 24-30)

### Question 24
**Scenario:** A company receives customer reviews in multiple languages and wants to understand the overall sentiment (positive, negative, neutral) of each review. What NLP capability is this?

A. Sentiment Analysis - determining the emotional tone of text
B. Translation
C. Entity recognition
D. Speech recognition

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Sentiment analysis determines the emotional tone of text - positive, negative, neutral, or mixed. It analyzes text to understand opinions, attitudes, and feelings expressed. Azure AI Language provides sentiment analysis that returns sentiment labels and confidence scores.

**Key Concept:** [Sentiment Analysis](https://docs.microsoft.com/azure/cognitive-services/language-service/sentiment-opinion-mining/overview)
</details>

### Question 25
**Scenario:** A legal firm wants to automatically identify and extract names of people, organizations, dates, and locations mentioned in contracts. What NLP capability extracts these specific pieces of information?

A. Text summarization - producing a short abstract of the contract instead of pulling out individual named items
B. Sentiment analysis - scoring whether each clause reads as positive, negative or neutral
C. Translation
D. Named Entity Recognition (NER) - finding people, places and organizations

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Named Entity Recognition (NER) identifies and classifies named entities in text into predefined categories: people, organizations, locations, dates, quantities, etc. Azure AI Language's NER can extract these entities to structure information from unstructured text like contracts.

**Key Concept:** [Named Entity Recognition](https://docs.microsoft.com/azure/cognitive-services/language-service/named-entity-recognition/overview)
</details>

### Question 26
**Scenario:** A global company wants to automatically translate their product documentation from English to Spanish, French, and German. What Azure service provides this translation capability?

A. Speech service - converting spoken audio to text and back into synthesized speech
B. Azure AI Translator - translates text between languages
C. Content Moderator - flagging offensive text and images in uploaded content
D. Language Understanding - interpreting user intent and entities in a spoken or typed request

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure AI Translator provides text translation between 100+ languages. It can translate documents while preserving formatting, detect source language automatically, and provide custom translation trained on domain-specific terminology. This enables multilingual content at scale.

**Key Concept:** [Azure AI Translator](https://docs.microsoft.com/azure/cognitive-services/translator/translator-overview)
</details>

### Question 27
**Scenario:** A company wants to build a chatbot that understands user requests in natural language. For example, "Book a meeting room for tomorrow at 2pm" should be interpreted as a room booking intent with specific time entities. What Azure capability enables this understanding?

A. Speech synthesis - turning the chatbot's response text into natural-sounding spoken audio for the user
B. Text translation - converting the user's request from one language into another before processing it elsewhere in the app
C. Conversational Language Understanding (CLU) - finding intent and entities in requests
D. OCR - extracting the printed text from scanned documents and photographs before processing them

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Conversational Language Understanding (CLU), part of Azure AI Language, trains models to understand user intent and extract entities from natural language. You define intents (book_room) and entities (date, time, room) and train with example utterances. The model then interprets new user inputs.

**Key Concept:** [Conversational Language Understanding](https://docs.microsoft.com/azure/cognitive-services/language-service/conversational-language-understanding/overview)
</details>

### Question 28
**Scenario:** A customer service center wants to transcribe recorded phone calls to text for analysis. They need to convert spoken audio to written text. What Azure service provides speech-to-text conversion?

A. Azure AI Document Intelligence
B. Translator
C. Azure AI Language
D. Azure AI Speech (Speech-to-Text) - converting spoken audio to text

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure AI Speech service includes Speech-to-Text (speech recognition) that converts audio to text. It supports real-time and batch transcription, multiple languages, and can be customized for specific vocabularies (industry terms, product names). This enables analysis of voice interactions.

**Key Concept:** [Speech-to-Text](https://docs.microsoft.com/azure/cognitive-services/speech-service/speech-to-text)
</details>

### Question 29
**Scenario:** An accessibility application needs to read text content aloud to visually impaired users. The system should convert written text into natural-sounding speech. What capability is this?

A. Speech-to-text - transcribing spoken audio into written text for captions and meeting notes
B. Sentiment analysis - scoring whether the text reads as positive, negative or neutral
C. Text-to-Speech (Speech Synthesis) - converting text to spoken audio
D. Translation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Text-to-Speech (speech synthesis) converts written text to spoken audio. Azure AI Speech provides neural voices that sound natural, with various voice options, languages, and the ability to control speaking style, speed, and pitch. This enables accessibility and voice-enabled applications.

**Key Concept:** [Text-to-Speech](https://docs.microsoft.com/azure/cognitive-services/speech-service/text-to-speech)
</details>

### Question 30
**Scenario:** A company wants to build a Q&A system where users ask questions and get answers from their product documentation. Users should be able to ask questions in natural language and receive relevant answers. What Azure service enables this?

A. Speech service - converting spoken questions to text and reading answers back as synthesized audio output to the caller
B. Computer Vision
C. Translator
D. Azure AI Language Question Answering (Custom Question Answering) - building knowledge bases from documents for Q&A

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Question Answering (part of Azure AI Language) creates knowledge bases from documents, FAQs, and URLs. Users ask natural language questions and the service returns relevant answers with confidence scores. This powers FAQ bots and documentation assistants without requiring exact phrase matching.

**Key Concept:** [Question Answering](https://docs.microsoft.com/azure/cognitive-services/language-service/question-answering/overview)
</details>

---

## Domain 5: Describe Features of Generative AI Workloads on Azure (Questions 31-40)

### Question 31
**Scenario:** A marketing team wants to use AI to generate creative product descriptions based on product features. The AI should write original text that sounds natural and engaging. What type of AI capability is this?

A. Classification
B. Clustering
C. Generative AI - AI that creates new content (text, images, code)
D. Object detection

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Generative AI creates new content - text, images, code, music - rather than just analyzing existing content. Large language models like GPT can generate product descriptions, marketing copy, and other creative text based on prompts describing the desired output.

**Key Concept:** [Generative AI Overview](https://docs.microsoft.com/learn/modules/fundamentals-generative-ai/)
</details>

### Question 32
**Scenario:** A company wants to deploy OpenAI's GPT models within their Azure environment, ensuring enterprise security, compliance, and integration with their existing Azure services. What Azure service provides this?

A. Azure AI services only - prebuilt vision and language APIs that do not host GPT models
B. Azure Functions - serverless code that runs small event-driven tasks and does not host models
C. Azure OpenAI Service - GPT and DALL-E models within Azure
D. Azure Blob Storage - object storage that holds files and has no model hosting features

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure OpenAI Service provides REST API access to OpenAI's models (GPT-4, GPT-3.5, DALL-E, Embeddings) within Azure's secure cloud. It includes enterprise features: private networking, managed identity, content filtering, and compliance certifications. Models run on Azure infrastructure.

**Key Concept:** [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/overview)
</details>

### Question 33
**Scenario:** A developer is using a generative AI model and wants to give it instructions for how to respond. They write: "You are a helpful customer service agent. Respond politely and concisely." What is this instruction called?

A. Embedding
B. A Prompt (specifically a system prompt/message) - instructions given to guide the model's behavior
C. Training data
D. Fine-tuning - retraining the model weights on a labeled dataset so that it permanently changes its style

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A prompt is input text that guides a generative AI model's response. System prompts (or system messages) set the model's behavior, role, or personality. User prompts contain the actual request. Effective prompt engineering is crucial for getting desired outputs from generative AI.

**Key Concept:** [Prompt Engineering](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/prompt-engineering)
</details>

### Question 34
**Scenario:** A company wants their generative AI chatbot to answer questions using only their internal company documentation, not general internet knowledge. The AI should cite sources from company documents. What capability enables this?

A. Use the model without any context from the company documents, relying only on what it learned in training
B. Use a larger model with more parameters, which still would have no access to the internal documentation
C. Fine-tuning only - retraining the model on the documents once, which cannot cite sources or reflect any later changes to the documents
D. Retrieval Augmented Generation (RAG) - search over company data grounds the answers in sources

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Retrieval Augmented Generation (RAG) combines a large language model with search/retrieval from your data. When a user asks a question, relevant documents are retrieved and provided to the model as context. The model generates answers grounded in these documents, reducing hallucination and enabling source citations.

**Key Concept:** [RAG Pattern](https://docs.microsoft.com/azure/search/retrieval-augmented-generation-overview)
</details>

### Question 35
**Scenario:** Users are asking an AI assistant questions, but sometimes the AI generates confident-sounding but incorrect information. What is this behavior called?

A. Overfitting
B. Hallucination - when AI generates plausible but factually incorrect content
C. Classification error - the model assigns an input to the wrong category in a supervised task
D. Underfitting

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hallucination occurs when generative AI produces content that sounds plausible but is factually incorrect. The model generates based on patterns, not factual verification. Mitigation strategies include RAG (grounding in data), prompt engineering, temperature reduction, and content filtering.

**Key Concept:** [AI Limitations and Hallucinations](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/)
</details>

### Question 36
**Scenario:** A company using Azure OpenAI wants to prevent their AI from generating harmful, offensive, or inappropriate content. What Azure OpenAI feature helps with this?

A. Manual review of all outputs - staff read every response before it is shown to the end user in a queue
B. Use the model without restrictions
C. No safety features exist for Azure OpenAI, so the application team must build every filter itself
D. Content Filtering - built-in filters that detect and block harmful prompts and responses

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Azure OpenAI includes content filtering that detects and filters harmful content in both user prompts and model outputs. Categories include hate, violence, self-harm, and sexual content. Configurable severity thresholds let you set appropriate levels for your use case.

**Key Concept:** [Content Filtering](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/content-filter)
</details>

### Question 37
**Scenario:** A software company wants to use AI to help developers write code. The AI should suggest code completions, explain code, and help with debugging. What Microsoft product provides this AI coding assistance?

A. Microsoft Word - a word processor for writing, formatting and sharing documents
B. Azure DevOps - boards, repos and pipelines for planning and shipping software
C. GitHub Copilot - AI pair programmer for code suggestions and debugging
D. Visual Studio without AI - a code editor and debugger that offers no generative suggestions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GitHub Copilot uses generative AI to assist with coding. It suggests code completions, generates code from comments, explains code, helps with debugging, and can write tests. It integrates into IDEs like VS Code and Visual Studio, acting as an AI pair programmer.

**Key Concept:** [GitHub Copilot](https://docs.github.com/copilot)
</details>

### Question 38
**Scenario:** A company wants to create an AI assistant that can search their SharePoint documents, answer questions about company policies, and help employees find information. What Microsoft product enables this enterprise AI assistant?

A. Microsoft Paint - a simple drawing tool for editing pictures and screenshots on Windows
B. Microsoft Word
C. Microsoft Excel only - a spreadsheet for calculations that cannot search SharePoint documents or summarize them
D. Microsoft 365 Copilot - AI assistant built into Microsoft 365 apps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Microsoft 365 Copilot integrates generative AI across Microsoft 365 apps (Word, Excel, Teams, Outlook). It can access organizational data the user is permitted to see, search documents, summarize meetings, draft emails, and answer questions grounded in company content through Microsoft Graph.

**Key Concept:** [What is Microsoft 365 Copilot?](https://learn.microsoft.com/en-us/microsoft-365-copilot/microsoft-365-copilot-overview)
</details>

### Question 39
**Scenario:** When using a generative AI model, a user notices that setting "temperature" higher produces more creative but less predictable outputs, while lower temperature produces more focused and deterministic outputs. What does temperature control?

A. The cost of the API call - higher temperature makes each request more expensive to bill and process per token
B. The randomness and creativity of the output - higher means more varied responses
C. How fast the model runs, since higher values make the model generate tokens more quickly
D. The size of the model, since higher values load a larger set of parameters into memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Temperature is a parameter that controls randomness in generative AI outputs. Low temperature (0-0.3) produces more deterministic, focused responses - good for factual Q&A. High temperature (0.7-1.0) produces more creative, varied responses - good for creative writing. It affects the probability distribution of token selection.

**Key Concept:** [Model Parameters](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/advanced-prompt-engineering)
</details>

### Question 40
**Scenario:** A company wants to use AI to generate images from text descriptions for their marketing campaigns. They describe a scene in words and want the AI to create a corresponding image. What type of generative AI model does this?

A. Language model for text only - a model that outputs written descriptions and cannot produce pictures
B. Image Generation model (like DALL-E) - creating images from text descriptions
C. Sentiment analysis
D. Speech recognition

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Image generation models like DALL-E (available through Azure OpenAI) create images from text descriptions (prompts). You describe what you want ("a cat wearing a spacesuit on Mars") and the model generates a corresponding image. This is text-to-image generative AI.

**Key Concept:** [DALL-E Image Generation](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/models#dall-e)
</details>
