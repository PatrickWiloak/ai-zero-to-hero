# Google Cloud Professional Machine Learning Engineer Certification

> **Older product names:** AutoML Tables, Vision and Natural Language are the pre-Vertex names. Google now documents one AutoML under its [agent platform docs](https://cloud.google.com/automl-tables/docs), so check the current page before relying on a per-product detail here.

## Exam Overview

The Google Cloud Professional Machine Learning Engineer certification demonstrates your ability to design, build, and productionize ML models to solve business challenges using Google Cloud technologies and knowledge of proven ML models and techniques.

**Exam Code:** Professional Machine Learning Engineer
**Exam Duration:** 2 hours
**Number of Questions:** ~50-60 questions
**Exam Format:** Multiple choice and multiple select
**Passing Score:** No official passing score published (estimated 70%)
**Cost:** $200 USD
**Validity:** 2 years
**Prerequisites:** None; Google recommends 3+ years of industry experience including 1+ year designing and managing solutions on Google Cloud
**Languages:** English, Japanese

## Exam Domains

From Google's exam guide, dated "as of June 1, 2026" on its `_new` copy (re-checked 2026-11-06). The guide uses only the Gemini Enterprise Agent Platform names, so this guide does too ("Agent Platform" for short, formerly Vertex AI).

> **Which PDF:** the certification page links two different guides. "View exam guide" opens the current one below. "See current exam guide", further down the same page, opens an older PDF from September 2024 with different weights (Section 3 ~18%, Section 5 ~22%) and Vertex AI names. Use the weights here.

### Section 1: Architecting low-code AI solutions (~13%)
- 1.1 Developing ML models using BigQuery ML or AutoML on Gemini Enterprise Agent Platform, including fine-tuning Gemini models using BigQuery
- 1.2 Building AI solutions using Google Cloud AI APIs or foundational models (selecting from Model Garden; Gemini, Imagen, Veo, models as a service; Document AI, Vision, Translate; optimising Gemini applications for cost, latency and availability)

### Section 2: Collaborating within and across teams to manage data and models (~16%)
- 2.1 Exploring and preprocessing data for ML (including Agent Platform Feature Store and handling PII)
- 2.2 Model prototyping using notebooks (Agent Platform Workbench, Colab Enterprise, models from Model Garden)
- 2.3 Tracking and running ML experiments (Experiments on Agent Platform, Agent Platform Pipelines, Kubeflow Pipelines, ML Metadata; evaluating predictive and generative solutions, including LLM-as-a-judge)

### Section 3: Scaling prototypes into ML models (~21%)
- 3.1 Building models given the task, considering cost, complexity, latency and scalability
- 3.2 Training models, including fine-tuning foundational models and when tuning should be considered
- 3.3 Choosing appropriate hardware for training

### Section 4: Serving and scaling models (~20%)
- 4.1 Serving models (Agent Platform, Model Garden, Cloud Run, GKE; Model Registry; A/B and canary rollouts)
- 4.2 Scaling online model serving

### Section 5: Automating and orchestrating ML pipelines (~18%)
- 5.1 Developing end-to-end ML pipelines (Agent Platform Pipelines, Managed Service for Apache Airflow, Ray on Agent Platform)
- 5.2 Automating model retraining (CI/CD/CT, for example Cloud Build)

### Section 6: Monitoring AI solutions (~13%)
- 6.1 Identifying risks to AI solutions (data exfiltration, malicious prompting, sensitive data sent to LLMs; Regex, safety filters, Model Armor; bias monitoring; model explainability)
- 6.2 Monitoring, testing and troubleshooting AI solutions (Model Monitoring on Agent Platform; training-serving skew, data drift, concept drift, feature attribution drift; generative AI evaluation)

Source: [Professional Machine Learning Engineer exam guide](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english.pdf) and [certification page](https://cloud.google.com/learn/certification/machine-learning-engineer). The guide also notes that the exam "does not directly assess coding skills"; minimum Python and SQL proficiency is enough to read code snippets.

## Notes

The notes are organised by topic, not by exam section, so this table shows where each section lives.

| Notes | Exam sections | Covers |
|---|---|---|
| [ML Foundation Models and Tuning](notes/ml-foundation-models-and-tuning.md) | 1.1, 1.2, 2.2, 3.2, 4.1 | Model Garden, serving routes, when to tune, Gemini tuning in BigQuery, Gemini cost, latency and availability |
| [ML Data and Features](notes/ml-data-and-features.md) | 2.1, 4.2, 5.1 | Preprocessing, feature engineering, Feature Store, data validation |
| [ML Development and Training](notes/ml-development-and-training.md) | 1.1, 2.2, 2.3, 3.1, 3.2, 3.3 | BigQuery ML, AutoML, notebooks, experiments, frameworks, tuning, distributed hardware |
| [ML Deployment and Operations](notes/ml-deployment-and-operations.md) | 4.1, 4.2, 5.1, 5.2, 6.1, 6.2 | Serving, scaling, rollouts, Model Registry, pipelines, Ray, Airflow, CI/CD/CT, explainability, monitoring code |
| [Monitoring AI Solutions](notes/ml-monitoring-ai-solutions.md) | 2.3, 6.1, 6.2 | Security risks, Model Armor, bias, skew and drift types, Model Monitoring v1 and v2, generative AI evaluation |

The [practice bank](../../practice-questions/gcp-machine-learning-engineer.md) maps each question to its objective.

## Key Technologies and Services

### Core ML Platform
- **Agent Platform (formerly Vertex AI):** Unified ML platform
- **AutoML:** Automated machine learning
- **BigQuery ML:** SQL-based machine learning
- **Agent Platform Workbench and Colab Enterprise:** Jupyter-based development environments
- **Explainable AI:** Model interpretability and fairness

### Pre-trained AI Services
- **Vision AI:** Image and video analysis
- **Natural Language AI:** Text analysis and understanding
- **Speech-to-Text/Text-to-Speech:** Audio processing
- **Translation AI:** Language translation
- **Document AI:** Document processing and extraction

### ML Infrastructure
- **Agent Platform Managed Training:** Custom model training
- **Agent Platform Inference:** Model serving and inference
- **Agent Platform Pipelines:** ML workflow orchestration
- **Agent Platform Feature Store:** Feature management
- **Agent Platform Model Registry:** Model versioning and management

### Data and Analytics
- **BigQuery:** Data warehouse and analytics
- **Cloud Storage:** Data lake and model storage
- **Dataflow:** Data preprocessing and transformation
- **Pub/Sub:** Real-time data streaming
- **Dataprep:** Data preparation and cleaning

## Core Skills Required

### Machine Learning Fundamentals
- **Supervised Learning:** Classification, regression, time series
- **Unsupervised Learning:** Clustering, dimensionality reduction
- **Deep Learning:** Neural networks, CNNs, RNNs, Transformers
- **Reinforcement Learning:** Policy learning, reward systems
- **Feature Engineering:** Selection, transformation, encoding

### MLOps and Production ML
- **Model Deployment:** Batch prediction, online serving, edge deployment
- **Model Monitoring:** Performance tracking, drift detection, alerting
- **Pipeline Automation:** CI/CD for ML, automated retraining
- **Experiment Management:** A/B testing, model comparison
- **Model Governance:** Versioning, lineage, compliance

### Data Engineering for ML
- **Data Preprocessing:** Cleaning, transformation, validation
- **Feature Engineering:** Creation, selection, transformation
- **Data Pipeline Development:** ETL/ELT for ML workloads
- **Real-time Processing:** Streaming data for online inference
- **Data Quality:** Validation, monitoring, anomaly detection

### Cloud-Native ML Development
- **Agent Platform Workbench:** Notebook-based development
- **Custom Training:** Distributed training, hyperparameter tuning
- **AutoML:** No-code/low-code model development
- **Pre-trained Models:** API integration, customization
- **Edge Deployment:** Mobile, IoT, edge computing

## Study Areas by Domain

### Low-Code ML Solutions (Section 1)
**BigQuery ML:**
- Creating models with SQL (LINEAR_REG, LOGISTIC_REG, etc.)
- Feature preprocessing and engineering in SQL
- Model evaluation and hyperparameter tuning
- Integration with Agent Platform and other services

**AutoML:**
- AutoML Tables for structured data
- AutoML Vision for image classification and object detection
- AutoML Natural Language for text classification
- AutoML Video Intelligence for video analysis

**AI APIs:**
- Vision API: image analysis, OCR, face detection
- Natural Language API: sentiment, entity, syntax analysis
- Speech-to-Text: audio transcription with customization
- Translation API: text and document translation

**Foundation models:**
- Selecting a model from Model Garden, and MaaS versus self-deployment
- Fine-tuning Gemini in BigQuery with a remote model
- When tuning beats prompting, and when neither replaces grounding
- Optimising Gemini applications for cost, latency and availability

### Data and Model Management (Section 2)
**Data Exploration:**
- Exploratory data analysis (EDA) techniques
- Data profiling and quality assessment
- Statistical analysis and visualization
- Feature correlation and importance analysis

**Collaboration:**
- Agent Platform Workbench for team collaboration
- Shared notebooks and version control
- Data access controls and security
- Resource sharing and cost management

**Model Artifacts:**
- Model versioning and registry
- Metadata tracking and lineage
- Model comparison and selection
- Artifact storage and organization

### Production ML Systems (Sections 3, 4 and 5)
**Serving Infrastructure:**
- Online prediction with Agent Platform Endpoints
- Batch prediction for large datasets
- Autoscaling and load balancing
- Multi-model serving and routing

**Training Pipelines:**
- Agent Platform Pipelines for workflow orchestration
- Custom training jobs with distributed computing
- Hyperparameter tuning and optimization
- Automated pipeline triggers and scheduling

**Monitoring and Observability:**
- Model performance monitoring
- Data drift and feature drift detection
- Prediction quality and business metrics
- Alerting and incident response

### Scaling and Automation (Sections 4 and 5)
**Production Deployment:**
- Blue-green and canary deployment strategies
- A/B testing for model comparison
- Traffic splitting and gradual rollout
- Rollback and disaster recovery procedures

**Pipeline Automation:**
- Continuous integration/continuous deployment (CI/CD)
- Automated testing for ML models and pipelines
- Infrastructure as code for ML resources
- Event-driven pipeline execution

### Monitoring AI Solutions (Section 6)
**Risks:**
- Data exfiltration, malicious prompting and sensitive data sent to LLMs
- Regex, safety filters and Model Armor, and which fits which risk
- Monitoring for bias, and model explainability

**Monitoring and evaluation:**
- Training-serving skew, data drift, concept drift and feature attribution drift
- Model Monitoring on Agent Platform and continuous evaluation metrics
- Monitoring, testing and evaluating generative AI

## Hands-On Practice Areas

### Project 1: End-to-End ML Pipeline
- Build complete ML pipeline from data ingestion to serving
- Implement feature engineering and model training
- Deploy model with monitoring and alerting
- Automate retraining based on performance metrics

### Project 2: Computer Vision Application
- Develop custom vision model using AutoML or custom training
- Implement real-time image processing pipeline
- Deploy model for edge inference
- Monitor model performance and accuracy

### Project 3: Natural Language Processing Solution
- Build text classification or sentiment analysis model
- Implement document processing pipeline
- Integrate with business applications
- Scale for high-volume text processing

### Project 4: Time Series Forecasting System
- Develop forecasting model for business metrics
- Implement real-time prediction pipeline
- Create automated retraining based on new data
- Build dashboard for predictions and monitoring

## Study Strategy

### Phase 1: ML Fundamentals Review (Weeks 1-2)
- Review machine learning concepts and algorithms
- Practice with scikit-learn and TensorFlow
- Understand evaluation metrics and validation techniques
- Study feature engineering best practices

### Phase 2: GCP ML Services (Weeks 3-6)
- Deep dive into Agent Platform platform components
- Practice with AutoML for different data types
- Explore pre-trained AI APIs and customization
- Learn BigQuery ML for SQL-based machine learning
- Work through [ML Foundation Models and Tuning](notes/ml-foundation-models-and-tuning.md)

### Phase 3: MLOps and Production (Weeks 7-10)
- Study ML pipeline development and orchestration
- Practice model deployment and serving strategies
- Implement monitoring and alerting systems, then work through [Monitoring AI Solutions](notes/ml-monitoring-ai-solutions.md) (Section 6)
- Learn about model governance and compliance

### Phase 4: Advanced Topics and Practice (Weeks 11-12)
- Study advanced ML techniques and optimization
- Practice with complex, multi-step ML pipelines
- Take practice exams and review weak areas
- Build portfolio projects demonstrating skills

## 📚 Comprehensive Study Resources

**👉 [Complete GCP Study Resources Guide](https://cloud.noblerworks.com/provider-resources/resources-gcp/)**

For detailed information on courses, practice tests, hands-on labs, communities, and more, see our comprehensive GCP study resources guide which includes:
- Google Cloud Skills Boost (Qwiklabs) hands-on labs
- Top-rated video courses with specific instructors
- Practice test platforms with pricing and comparisons
- Free tier details and $300 credit information
- Community forums and study groups
- Essential gcloud CLI and tools
- Pro tips and budget-friendly study strategies

### Quick Links (Professional Machine Learning Engineer Specific)
- **[Professional Machine Learning Engineer Official Exam Page](https://cloud.google.com/certification/machine-learning-engineer)** - Registration and exam details
- **[Google Cloud Skills Boost Learning Path](https://www.cloudskillsboost.google/paths)** - Official hands-on labs
- **[Google Cloud Documentation](https://cloud.google.com/docs)** - Complete service documentation
- **[Google Cloud Free Tier](https://cloud.google.com/free)** - $300 credit for 90 days + always free services

## Exam Preparation Tips

### Technical Skills Focus
- **Hands-on experience** with Agent Platform platform
- **Model development** using multiple approaches (AutoML, custom, BigQuery ML)
- **Pipeline implementation** with real datasets
- **Production deployment** and monitoring experience

### Business Context Understanding
- **Use case selection** for different ML approaches
- **Cost optimization** for ML workloads
- **Performance trade-offs** between accuracy and efficiency
- **Stakeholder communication** of ML results and limitations

### Exam Strategy
- **Practice with time constraints** to improve speed
- **Focus on scenario-based questions** requiring practical knowledge
- **Understand service capabilities** and appropriate use cases
- **Review error patterns** from practice exams

## Career Benefits

### Job Opportunities
- Machine Learning Engineer
- Senior ML Engineer
- Principal ML Engineer
- AI/ML Solutions Architect
- Data Scientist (ML focused)
- ML Platform Engineer

### Skills Validation
- **End-to-end ML development**
- **Production ML systems**
- **Cloud-native ML engineering**
- **MLOps and automation**
- **Cross-functional collaboration**

### Professional Growth
- **Access to cutting-edge AI projects**
- **Leadership opportunities** in ML initiatives
- **Consulting and advisory roles**

## Maintaining Certification

### Continuous Learning
- **Stay updated** with new Agent Platform features
- **Practice with emerging ML techniques**
- **Contribute to open source** ML projects
- **Attend ML conferences** and workshops

### Recertification
- **Renew within the eligibility period** - see Google's [Renewal FAQs](https://support.google.com/cloud-certification/answer/9907853) for the process and timeline
- **Maintain hands-on experience** with evolving technologies
- **Participate in professional development** activities