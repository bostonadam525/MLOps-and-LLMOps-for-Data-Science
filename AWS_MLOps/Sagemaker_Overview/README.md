# Sagemaker Overview for Data Science + ML
- General run down of Sagemaker

---
# Machine Learning Lifecycle (MLOps)
- Excellent rundown of this full lifecycle: https://mlflow.org/articles/ml-lifecycle-management-explained-for-engineers/

1. Data Aggregation + Exploration (EDA)
2. Data preparation/Feature Engineering
3. Model Training
4. Model Deployment/hosting/inference
   - Exposing model as API

5. Monitoring + Evaluation + Observability

---
# Sagemaker - Managed ML Service
- This has 2 main components

1. **Hardware**
   - takes care of universal hardware needs vs. using EC2 to manually handle (eg health checks, patching, networking, scaling)
   - networking
   - logging
   - monitoring

2. **Features tailored for ML lifecyle**
   - Data prep: Spark
   - Model training: PyTorch
   - Managed Docker Containers for workflows
   - Features provided for each ML lifecyle component (none are prebuilt in EC2 or other frameworks, Sagemaker does this all)

---
## Sagemaker Component Mapping
- **Data Engineering**
  - feature store
  - data wrangler
  - processsing jobs (spark jobs)

- **Model Training**
  - Training jobs
  - Hyperpod (nodes to train LLMs)
 
- **Model Hosting**
  - Real-time inference
  - Multi-model inference
  - Batch transforms
 
- **Monitoring/Evaluation**
  - Clarify (explanatory ML)
  - Model monitoring (eg MLflow)

- **MLOps**
  - Pipelines stitch all of this together.
  - Hardware + features
  - Tools/services/frameworks
 
---
# Sagemaker JumpStart

## Model Deployment/Hosting
- Exposing trained model as API
- There are 2 factors:
  1. Hardware
     - compute/memory
     - GPU instances
  2. Model server (containers)
     - orchestrator to load model into memory
     - handle concurrent requests
     - protocol between client + endpoint hardware
     - Examples: Triton, TorchServe, DJL serving (AWS), TGI



---
# Resources
- [Sagemaker crash course](https://www.youtube.com/watch?v=pSu-aVC7UCw&list=PLThJtS7RDkOchq0_dwjQkzzb5idzOxN7l)
- 
