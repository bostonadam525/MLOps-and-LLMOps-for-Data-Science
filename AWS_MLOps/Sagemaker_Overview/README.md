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
     - this is the protocol between client + model endpoint hardware
     - Example servers: Triton (NVIDIA), TorchServe, DJL serving (AWS), TGI

## JumpStart
- Abstracts out HARDWARE + CONTAINER
- Example:
  - Model: Llama-3-8b
  - Optimal configuration provided by Sagemaker
  - Benchmarks configured by Sagemaker
- **NOT SERVERLESS this is REAL-TIME inference** --> still deploys on instance (pre-selected for you) -- can change this (flexible)

### JumpStart SDK Options
- **boto3**
  - Purpose: The official, comprehensive AWS SDK to control 100% of the APIs for every AWS service (S3, EC2, Lambda, and raw SageMaker API calls)
  - Best Use Case: Production infrastructure automation, general cloud management, and tasks outside of machine learning
- **SageMaker Python SDK (JumpStart & ML Workflows)**
  - Purpose: Built specifically to simplify machine learning experimentation, model training, and deployment on SageMaker
  - Best Use Case: data science notebooks and ML development.

---
# Containers on SageMaker
- Allows you to port a lightweight software package with all code, dependencies and configurations and execute it anywhere.
- Portable, lightweight
- if you containerize packages you use such as torch, spacy, nltk

## Terms
1. Container
   - Instance of image.
2. Image
   - blueprint or instructions of how to execute code.
   - Dockerfile --> code, dependencies, configs
   - Build Dockerfile --> Docker images
   - Repositories on AWS: Elastic Container Registry (host it)
   - Services such as SageMaker are direct examples of ECR

3. kubernetes
   - allows you to scale 100s and 1000s of docker images.

## Sagemaker Managed ML Service
- Provides lists of managed deep learning containers and exposes these publicly as docker image runtimes so you can use all available packages for training and inference. 
- including: Torch, TensorFlow, HuggingFace, TGI
- Available images: https://aws.github.io/deep-learning-containers/reference/available_images/

## Bring your own container (BYOC)
- Use the Sagemaker managed containers if it has what you need.
- BYOC if what you need is unsupported --> Build your own image --> push to ECR which has your own app code/dependencies/docker image --> Sagemaker
- [Build Your Own Container for SageMaker AI Multi-Model Endpoints](
https://docs.aws.amazon.com/sagemaker/latest/dg/build-multi-model-build-container.html)
- [Adapt your own inference container for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-inference-container.html)
- Things to consider:
  - have to expose your own port
  - use your own scripts


---
# Resources
- [Sagemaker crash course](https://www.youtube.com/watch?v=pSu-aVC7UCw&list=PLThJtS7RDkOchq0_dwjQkzzb5idzOxN7l)
