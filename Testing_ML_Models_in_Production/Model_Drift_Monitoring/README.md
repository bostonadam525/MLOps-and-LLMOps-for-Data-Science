# Model Drift Monitoring
- Monitoring model drift in production with frameworks such as MLflow prevent silent accuracy loss and ensures your AI systems remain reliable as real-world data and user behavior evolve.


## Overview - Why Monitor Model Drift
- **Catch Silent Degradation:** Models trained on frozen snapshots of data lose accuracy over time when real-world distributions shift, often without crashing infrastructure or throwing server errors.
- **Trigger Automated Retraining:** Tracking drift metrics allows teams to set up alerts and automatically kick off retraining workflows as soon as statistical thresholds (like Population Stability Index or PSI) are crossed.
- **Maintain Compliance and Governance:** Active monitoring fulfills legal and regulatory post-market oversight requirements (such as the EU AI Act) by keeping historical records of model health.


## How frameworks such as MLflow Help
- **Log Metrics Over Time:** You can log distribution statistics, PSI values, and prediction drift rates as time-series metrics against specific registered model versions.
- **Connect to Model Registry:** Tracked drift thresholds can trigger governed, auditable stage transitions (from Staging to Production) when a newly retrained model passes validation

## AI Monitoring Use Cases
- **Hallucination detection in RAG systems:** Run groundedness scorers on production traces to catch when retrieval quality degrades or the model starts generating claims unsupported by the retrieved context.
- **Agent tool selection monitoring:** Track whether agents pick the right tools and complete tasks efficiently. Detect loops, unnecessary retries, and incorrect tool selections that waste tokens and degrade user experience.
- **Cost optimization:** Identify expensive queries, track per-model spend trends, and find opportunities to switch to cheaper models for low-complexity requests without sacrificing quality.
- **Safety regression detection:** After model or prompt updates, compare safety scores against pre-deployment baselines to catch regressions before they affect users at scale.
- **A/B testing prompt changes:** Compare quality scores, latency, and cost across prompt variants using production trace data to make data-driven decisions about which version to keep.
- **Compliance and audit in regulated industries:** Healthcare, finance, and legal teams need to prove their AI systems behave correctly and safely. AI monitoring provides full audit trails of every input, output, and model interaction for regulatory review.
- **Latency SLA monitoring:** For user-facing chatbots, coding assistants, and real-time agents where response time directly impacts user experience. Track p50/p95/p99 latency and time-to-first-token to catch performance regressions before they affect retention.

---
# What are the most common types of model drift? 
1. **Data drift (covariate shift)**: the statistical distribution of input features changes after deployment, even if the underlying relationship between inputs and outputs stays the same

2. **Concept drift**: the relationship between inputs and outputs changes over time.

3. **Prediction drift**: detected shifts in the model's output distribution, regardless of course. It often surfaces before you can confirm concept drift, making it a useful early warning signal. 

4. **Training-serving skew:** Feature engineering applied differently at training time versus inference time produces systematic prediction errors that mimic drift but require pipeline fixes, not retraining.

5. **Upstream schema drift:** A column rename, a unit change, or a new null pattern in a data pipeline can cause apparent model degradation that looks like concept drift but resolves with a pipeline patch.
  - **Root cause triage matters here. Retraining a model to fix a schema bug wastes compute and delays the real fix.*
---
# What Metrics detect Model Drift? 

1. **Population Stability Index (PSI)** :
   - This compares a feature's current distribution to the training baseline.
     - A PSI below 0.1 signals stability
     - A PSI between 0.1 and 0.25 indicates moderate drift worth investigating
     - A PSI above 0.25 signals significant drift requiring fast action.
  - PSI is VERY common in financial services because it was originally developed for credit scorecard monitoring.

2. **Kolmogorov-Smirnov (KS) test**
   - KS measures the maximum distance between two cumulative distribution functions.
   - This works well for continuous features and is sensitive to shifts in the tails of a distribution, where fraud signals and anomalies often live.

3. **Pearson's Chi-Squared test**
   - This handles categorical features.
   - If your AI/ML model ingests encoded categorical variables like product category or geographic region, Chi-Squared lets you test whether the category frequency distribution has shifted meaningfully.

---
## Monitoring Drift in Production Pipelines
- Establish your monitoring baseline at model deployment time, not retroactively (after the fact).
  - During initial deployment you need to know:
    - **Training data distribution**
    - **Validation prediction distribution**, and
    - **Key feature statistics**
  - **All of these are logged as key artifacts along with the model config versions. If you try to reconstruct a baseline six months later it will be error-prone and is often impossible to do!**
- **A basic Drift pipeline should look like this:**

1. **Continuous data ingestion:** you should collect inference inputs and outputs at every prediction, or at batch intervals for high-volume systems.
2. **Statistical computations:** Run PSI, KS, or Chi-Squared comparisons against the baseline on a schedule that matches your use case, from every few minutes for real-time systems to daily for batch pipelines.
3. **Threshold evaluation:** Compare computed metrics against configured thresholds and emit structured events when limits are exceeded.
4. **Automated response:** Trigger retraining jobs, open incident tickets, or page on-call engineers depending on severity.
5. **Feedback loop:** Feed newly labeled data back into the training pipeline so retraining uses current ground truth, not stale historical data.
  
---
# References
- [Machine learning model monitoring: Best practices](https://www.datadoghq.com/blog/ml-model-monitoring-in-production-best-practices/)
- [MLflow - AI monitoring for LLMs and Agents](https://mlflow.org/ai-monitoring)
- [ML Lifecycle Management Explained for Engineers](https://mlflow.org/articles/ml-lifecycle-management-explained-for-engineers/)
- [Monitoring discriminative ML models using Amazon SageMaker AI with MLflow](https://aws.amazon.com/blogs/machine-learning/monitoring-discriminative-ml-models-using-amazon-sagemaker-ai-with-mlflow/)
- [Why Monitor Model Drift in Production: A Practical Guide](https://mlflow.org/articles/why-monitor-model-drift-production/)
