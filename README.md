# MLOps-and-LLMOps-for-Data-Science
* A repo devoted to MLOps and LLMops related to the Data Science Life cycle.

# MLOps Overview
* *"Machine Learning and operations (MLOps) is the combination of people, processes, and technology to productionize machine learning (ML) solutions efficiently. To achieve this, a combination of teams and personas need to collaborate, as illustrated in the following figure." ~Kartakis et al. (See figure below from AWS)*
* The image below is sourced directly from an excellent article written by Kartakis et al. from AWS Machine Learning which breaks down the MLOps life cycle by role and processes. Here is the [full article link](https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/)

![image](https://github.com/user-attachments/assets/c3f4eb62-95ec-41bf-9824-3bda70dd5dbd)



# 4 Main Principles of MLOPs
1. **Documentation**
   * Important infrastructure: People and Processes
   * While documentation is often time consuming, it is paramount to ensure reproducibility and communication among team members.
   * Common things that should be documented:
       1) KPIs and Business goals
       2) Data Definitions
       3) Machine Learning System Architecture and Design
       4) Machine Learning models in development, production, and legacy
2. **Code Quality**
   * Important infrastructure: People and Processes
   * Another important aspect of all MLOPs pipelines. Bad code == Bad results.
   * Important considerations for code quality:
       1) Regular and Standard Code Review processes
       2) Regular and Standard Code Quality Checks
       3) Unit and Integration tests
       4) Source Control/Version Control
3. **Traceability and Reproducibility**
   * Important infrastructure: Tools
   * Traceability
     * For ANY MACHINE LEARNING MODEL you run or deploy you need to know:
       1) Code and Source Control commit history
       2) Training and Service infrastructure
       3) Machine Learning Model Artifacts
       4) Dataset(s) used for model training, testing and validation
    * Reproducibility
       1) Every model's results should be reproducible with the SAME data and SAME code regardless of the environment.
       2) Machine Learning Explainability may also fit into this category.
       3) Rollback should be easy (e.g. changes can be made seamlessly)
4. **Monitoring and Alerting**
   * Important infrastructure: Tools
      * ML pipeline costs and health
      * Application response time, scalability, health, and response codes
      * ML model evaluation metrics and business metrics
      * Data drift
      * Model drift
    
## Code Traceability and Reproducibility
1. Version Control
   * GitLab
   * GitHub
   * Azure DevOps
2. CI/CD
   * Github actions
   * Azure pipelines
   * Jenkins
3. Orchestration
   * Airflow
   * AWS Step functions
   * Databricks workflows
  
## Model Traceability and Reproducibility
1. ML Model Registry
   * MLFlow
   * Comet ML

2. Experiment Tracking
   * Weights & Biases
   * neptune.ai
   * MLFlow
  
## Data Traceability & Reproducibility
1. Feature Stores
   * Feast
   * Tecton
   * Databricks

2. Data Version Control
   * DVC
   * Delta Tables
  
## Environment Traceability and Reproducibility
1. Container Registries
   * ACR --> Azure
   * ECR --> AWS
   * Docker Hub

# MLOps Overview
* *"Machine Learning and operations (MLOps) is the combination of people, processes, and technology to productionize machine learning (ML) solutions efficiently. To achieve this, a combination of teams and personas need to collaborate, as illustrated in the following figure." ~Kartakis et al. (See figure below from AWS)*
* The image below is sourced directly from an excellent article written by Kartakis et al. from AWS Machine Learning which breaks down the MLOps life cycle by role and processes. Here is the [full article link](https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/)

![image](https://github.com/user-attachments/assets/c3f4eb62-95ec-41bf-9824-3bda70dd5dbd)


## Minimum Set of Tools for MLOPs
* This is a good overview of the minimum tools needed for MLOPs (source: Maria Vechtomova, LinkedIn Learning Course: "MLOPs with DataBricks")

![image](https://github.com/user-attachments/assets/54c706de-82b8-4bf2-83e1-e060199a4a2e)


## Larger Solution Requirements for MLOPs
* Same source as above, other considerations:

![image](https://github.com/user-attachments/assets/27398a28-fa15-4c0a-a68c-3ff0e13b8ef5)





# LLMOps Overview
* Kartakis et al. from AWS expanded upon this excellent model in a new updated article about LLMOPS, see their full writeup here: [FMOps/LLMOps: Operationalize generative AI and differences with MLOps](https://aws.amazon.com/blogs/machine-learning/fmops-llmops-operationalize-generative-ai-and-differences-with-mlops/)
* As the authors note, MLOps is now extended today to include productionalizing Generative AI use cases. This involves extending the MLOps domain to include:

1. **FM operations (FMOps)** – This can productionize generative AI solutions, including any use case type.
2. **LLM operations (LLMOps)** – This is a subset of FMOps focusing on productionizing LLM-based solutions, such as text-to-text.

* The Authors have an excellent diagram that compares and contrasts all 3 processes below. I recommend reading the full article for the excellent points they make about these processes and how to extend them from classical MLOps and fine tune them for your Generative AI use cases in production:


![image](https://github.com/user-attachments/assets/f1b04138-cd49-4d71-a62b-ee4aec8c8a2c)







# References
* A collection of awesome resources for MLOps and LLMops

1. [ml-ops.org](https://ml-ops.org/)
2. [Machine Learning Operations (MLOps)](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2)
3. [Key LLMOps and MLOps Topics You Need to Know!](https://medium.com/aimonks/interview-ready-key-llmops-and-mlops-topics-you-need-to-know-f938f49f0d1f)
4. [Google MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
5. [MLOps Principles and How to Implement Them](https://neptune.ai/blog/mlops-principles)


