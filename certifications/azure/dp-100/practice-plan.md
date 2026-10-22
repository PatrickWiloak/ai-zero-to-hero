# Azure Data Scientist Associate (DP-100) Study Plan

> ⚠️ **DP-100 retired on 2026-06-01.** The exam can no longer be booked. This plan is kept as a structured way to learn Azure Machine Learning and language-model optimization on Azure, following the final skills outline (skills measured as of 2025-04-11). For a current Microsoft exam covering the generative AI half, see [AI-103](../ai-103/README.md).

## 10-Week Learning Schedule

> **Time Commitment**: 10-12 hours/week
> **Difficulty**: Associate

The weeks follow the four domains of the final outline, with time in proportion to their weights: design and prepare (20-25%), explore data and run experiments (20-25%), train and deploy models (25-30%), and optimize language models for AI applications (25-30%).

---

## Weeks 1-2: Design and Prepare a Machine Learning Solution (20-25%)

### Week 1: Designing the solution
- [ ] Read [notes/machine-learning-solution-design.md](notes/machine-learning-solution-design.md)
- [ ] For three example problems, write down the dataset structure and format, the compute needed, and whether you would use AutoML, the designer or code
- [ ] Create an Azure Machine Learning workspace and look at what it provisions (storage, key vault, container registry, Application Insights)

### Week 2: Workspace resources and assets
- [ ] Create a datastore pointing at a storage container
- [ ] Create a compute instance, a compute cluster, and run a job on serverless compute
- [ ] Connect the workspace to a Git repository
- [ ] Create versioned data assets and a custom environment
- [ ] Share an environment or model through a registry

---

## Weeks 3-4: Explore Data, and Run Experiments (20-25%)

### Week 3: Automated machine learning
- [ ] Read [notes/data-exploration-model-training.md](notes/data-exploration-model-training.md)
- [ ] Run AutoML on a tabular classification dataset; review featurization, the leaderboard and the explanation and fairness views
- [ ] Read how AutoML differs for computer vision and NLP tasks

### Week 4: Notebooks and hyperparameter tuning
- [ ] Configure a compute instance from its terminal and wrangle data in a notebook
- [ ] Wrangle data with serverless Spark compute
- [ ] Retrieve features from a feature store for training
- [ ] Track a training run with MLflow
- [ ] Run a sweep job: choose a sampling method, define the search space and primary metric, add an early termination policy

---

## Weeks 5-6: Train and Deploy Models (25-30%)

### Week 5: Jobs, pipelines and model management
- [ ] Submit a training script as a command job with parameters, compute and environment; troubleshoot a failure from the logs
- [ ] Build a pipeline from custom components, pass data between steps, and schedule it
- [ ] Inspect the MLmodel file and its signature; register an MLflow model
- [ ] Generate a responsible AI dashboard for a model

### Week 6: Deployment
- [ ] Read [notes/model-deployment-monitoring.md](notes/model-deployment-monitoring.md)
- [ ] Deploy a model to a managed online endpoint and test it
- [ ] Deploy a model to a batch endpoint and invoke a batch scoring job

---

## Weeks 7-9: Optimize Language Models for AI Applications (25-30%)

### Week 7: Preparing and prompting
- [ ] Read [notes/language-model-optimization.md](notes/language-model-optimization.md)
- [ ] Deploy two models from the model catalog and compare them by benchmark and in the playground
- [ ] Write down, for three scenarios, whether prompting, RAG or fine-tuning is the right first step and why
- [ ] Build a prompt flow with a template and two variants; run it in bulk and read the trace

### Week 8: Retrieval augmented generation
- [ ] Clean, chunk and embed a small document set
- [ ] Create an Azure AI Search index with vector, keyword and semantic ranking; compare results
- [ ] Add retrieval to the prompt flow and evaluate groundedness and relevance

### Week 9: Fine-tuning
- [ ] Prepare a small JSONL fine-tuning dataset with a validation split
- [ ] Run a fine-tuning job on a supported base model and watch training and validation loss
- [ ] Compare the fine-tuned model against the base model with your best prompt

---

## Week 10: Review

- [ ] Re-read the [fact sheet](fact-sheet.md) end to end
- [ ] Work through the [DP-100 practice questions](../../practice-questions/azure-data-scientist-dp-100.md), especially Questions 16-30, which follow the final outline
- [ ] Revisit whichever domain you scored lowest in

---

## 📚 Study Resources

**👉 [Complete Azure Study Resources Guide](https://cloud.noblerworks.com/provider-resources/resources-azure/)**

- **[DP-100 study guide (archived)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)** - the final outline
- **[Azure Machine Learning documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)** - workspaces, jobs, pipelines, endpoints
- **[Prompt flow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow)** - flows, variants, tracing
- **[RAG with Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)** - retrieval for generative AI
- **[Azure Free Account](https://azure.microsoft.com/en-us/free/)** - credit for hands-on practice

## 💡 Tips

- Hands-on practice matters more than reading; every week above has a lab
- Use the SDK v2 and CLI v2; SDK v1 material is out of date
- For the language-model domain, always ask which approach fixes the actual problem: missing knowledge (RAG) or wrong behaviour (fine-tuning)
- Check dates on any third-party material; much of it predates the final outline
