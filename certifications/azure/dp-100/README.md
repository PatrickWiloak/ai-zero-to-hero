# Microsoft Azure Data Scientist Associate (DP-100) - RETIRED

## Important Notice

**The DP-100 exam and its certification were retired on June 1, 2026.** It can no longer be taken and the certification can no longer be earned or renewed. Credentials already earned stay on the holder's Microsoft Learn transcript. This guide is kept as historical reference. 

**No one-for-one successor.** Microsoft did not name a direct replacement. For the generative AI half of this exam (language models, prompt flow, RAG, fine-tuning on Azure), the closest current exam is [AI-103, Azure AI Apps and Agents Developer Associate](../ai-103/README.md). The classic machine learning half (Azure Machine Learning workspaces, jobs, pipelines, endpoints) has no current Microsoft associate exam of its own.

**This guide follows the final skills outline** (skills measured as of 2025-04-11, the version live until retirement; checked 2026-10-22 against the [archived study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)). Older DP-100 material, including earlier versions of this page, describes an older four-domain outline (with "explore data and train models" at 35-40%) that predates the language-model domain.

Source: [Microsoft Learn - exam retirement](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

---

## Exam Overview

The Azure Data Scientist Associate certification validated subject matter expertise in applying data science and machine learning to implement and run machine learning workloads on Azure, and, in its final outline, knowledge of optimizing language models for AI applications using Azure AI. The tools named in the audience profile were Azure Machine Learning, MLflow, Azure AI services including Azure AI Search, and Azure AI Foundry.

**Exam Details:**
- **Exam Code:** DP-100
- **Duration:** 180 minutes
- **Number of Questions:** 40-60 questions
- **Passing Score:** 700 out of 1000
- **Question Types:** Multiple choice, multiple select, drag and drop, case studies
- **Cost:** $165 USD
- **Prerequisites:** Data science and ML experience with Azure

## Exam Domains (final outline, skills measured as of 2025-04-11)

| Domain | Weight | Notes in this repo |
|---|---|---|
| 1. Design and prepare a machine learning solution | 20-25% | [machine-learning-solution-design.md](notes/machine-learning-solution-design.md) |
| 2. Explore data, and run experiments | 20-25% | [data-exploration-model-training.md](notes/data-exploration-model-training.md) |
| 3. Train and deploy models | 25-30% | [data-exploration-model-training.md](notes/data-exploration-model-training.md), [model-deployment-monitoring.md](notes/model-deployment-monitoring.md) |
| 4. Optimize language models for AI applications | 25-30% | [language-model-optimization.md](notes/language-model-optimization.md) |

The big change in DP-100's last revisions was the fourth domain. Language-model work went from absent to a quarter or more of the exam, and the classic data-science domains were compressed to make room for it.

### 1. Design and Prepare a Machine Learning Solution (20-25%)

This domain is about setting up before any training happens. **Designing the solution** means identifying the structure and format of the datasets (tabular, image, text; files, tables or folders), determining the compute the workload needs (CPU or GPU, single node or cluster, instance or serverless), and selecting the development approach (automated ML, the designer, or code in notebooks and scripts). **Creating and managing workspace resources** covers the Azure Machine Learning workspace itself, datastores (connections to storage such as Blob or Data Lake), compute targets (compute instances for development, compute clusters and serverless compute for training), and Git integration for source control. **Managing assets** covers data assets (versioned references to data), environments (the Docker image and Python dependencies a job runs in) and registries, which share models, environments and components across workspaces.

### 2. Explore Data, and Run Experiments (20-25%)

**Automated machine learning** runs many algorithm and preprocessing combinations and ranks them by a primary metric. The outline covers AutoML for tabular data, computer vision and natural language processing; selecting training options such as featurization, allowed algorithms and limits; and evaluating a run, including the responsible AI guidance (model explanations and fairness). **Custom training in notebooks** covers configuring a compute instance from its terminal, accessing and wrangling data in notebooks, wrangling interactively with attached Synapse Spark pools and serverless Spark compute, retrieving features from a feature store, tracking training with MLflow, and evaluating a model against responsible AI guidelines. **Hyperparameter tuning** (sweep jobs) means choosing a sampling method (grid, random or Bayesian), defining the search space, setting the primary metric and its goal, and choosing an early termination policy (bandit, median stopping or truncation selection) so poor runs stop early.

### 3. Train and Deploy Models (25-30%)

**Running training scripts as jobs** means consuming data in a job, configuring its compute and environment, tracking it with MLflow, defining job parameters, submitting the script as a command job and using the logs to troubleshoot failures. **Training pipelines** chain reusable components: create custom components, build a pipeline, pass data between steps, run and schedule it, and monitor and troubleshoot runs. **Managing models** covers defining the signature in the MLmodel file, packaging a feature retrieval specification with the model artifact, registering an MLflow model, and assessing the model with the responsible AI dashboard. **Deploying** covers managed online endpoints (configure the deployment, deploy, test the live service) and batch endpoints (configure compute for batch deployment, deploy, invoke the endpoint to start a batch scoring job).

### 4. Optimize Language Models for AI Applications (25-30%)

The late addition to the outline, and the domain most worth studying even now that the exam is retired, because it maps directly onto current Azure generative AI work. It has four groups.

**Prepare for model optimization.** Select and deploy a language model from the model catalog, compare models using benchmarks, test a deployed model in the playground, and select an optimization approach. The core judgment is the order of approaches: start with prompt engineering, add retrieval augmented generation (RAG) when the model lacks your data, and fine-tune only when the model needs a consistent style, format or behaviour that prompting cannot reliably produce.

**Optimize through prompt engineering and prompt flow.** Test prompts with manual evaluation, define and track prompt variants, create prompt templates, define chaining logic with the prompt flow SDK, and use tracing to evaluate the flow.

**Optimize through RAG.** Prepare data for RAG (cleaning, chunking and embedding), configure a vector store, configure an Azure AI Search-based index, and evaluate the RAG solution for groundedness and relevance.

**Optimize through fine-tuning.** Prepare fine-tuning data (usually JSONL conversations), select an appropriate base model, run a fine-tuning job, and evaluate the fine-tuned model against the base model.

The full teaching treatment is in [notes/language-model-optimization.md](notes/language-model-optimization.md).

## Key Azure ML Components

### Development
- **Notebooks** - Interactive development with Jupyter
- **Automated ML** - No-code ML training
- **Designer** - Drag-and-drop ML pipelines
- **VS Code Integration** - Local development

### Training
- **Compute Instances** - Development environments
- **Compute Clusters** - Scalable training
- **Experiments** - Training run tracking
- **Pipelines** - ML workflow automation

### Deployment
- **Managed Online Endpoints** - Real-time inference without managing infrastructure
- **Batch Endpoints** - Asynchronous scoring over large data
- **Kubernetes Online Endpoints** - Real-time inference on your own AKS or Arc cluster
- **Registries** - Share models and environments across workspaces

### MLOps
- **Model Registry** - Version management
- **Environments** - Dependency management
- **Pipelines** - CI/CD automation
- **Monitoring** - Model performance tracking

## Study Tips

### Recommended Study Timeline (for reference use): 10-12 weeks
- **Weeks 1-2:** Azure ML fundamentals and workspace setup
- **Weeks 3-4:** Data exploration, AutoML and hyperparameter tuning
- **Weeks 5-6:** Training jobs, pipelines and model management
- **Week 7:** Deployment to online and batch endpoints
- **Weeks 8-10:** Language models: model catalog, prompt flow, RAG with Azure AI Search, fine-tuning
- **Weeks 11-12:** Review

### Key Study Resources
- **Microsoft Learn:** DP-100 learning path (FREE)
- **Azure ML Documentation:** Technical reference
- **Sample Notebooks:** Azure ML examples on GitHub
- **Hands-on Labs:** Build end-to-end ML solutions

### Hands-on Practice Requirements
- Create and manage Azure ML workspaces
- Prepare data for machine learning
- Train models using various methods (AutoML, custom scripts)
- Implement hyperparameter tuning
- Deploy models to various targets
- Monitor model performance and data drift
- Build ML pipelines

### Python Libraries to Master
- **Azure ML SDK** - Python SDK for Azure ML
- **scikit-learn** - ML algorithms
- **pandas** - Data manipulation
- **matplotlib/seaborn** - Visualization
- **numpy** - Numerical computing

## 📚 Comprehensive Study Resources

**👉 [Complete Azure Study Resources Guide](https://cloud.noblerworks.com/provider-resources/resources-azure/)**

### Quick Links (DP-100 Specific)
- **[DP-100 Official Exam Page](https://learn.microsoft.com/en-us/certifications/exams/dp-100/)** - Registration
- **[Microsoft Learn - DP-100 Learning Path](https://learn.microsoft.com/en-us/certifications/azure-data-scientist/)** - FREE study path
- **[Azure Machine Learning Documentation](https://docs.microsoft.com/en-us/azure/machine-learning/)** - Complete documentation
- **[Azure ML SDK Reference](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/)** - Python SDK docs
- **[Azure Free Account](https://azure.microsoft.com/en-us/free/)** - $200 free credit

## Prerequisites and Next Steps

### Prerequisites
- Experience with Python programming
- Understanding of ML concepts and algorithms
- Knowledge of data science fundamentals
- Familiarity with Jupyter notebooks
- Basic Azure knowledge helpful

### Career Path
- **Role Focus:** Data Scientist, ML Engineer, AI Engineer
- **Skills Development:** MLOps, responsible AI, model optimization
- **Next Steps:** For Azure generative AI work, [AI-103](../ai-103/README.md) (AI Apps and Agents Developer, the successor to AI-102) is the closest current Microsoft exam

DP-100 is retired. Use this guide as a structured tour of Azure Machine Learning and of language-model optimization on Azure, not as exam preparation.
