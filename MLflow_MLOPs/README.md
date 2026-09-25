# MLflow for MLOPs
* MLflow is a vital tool for all phases of the MLOPs project life cycle.

# Data Science Lifecycle
* The processes above are based off the Data Science Lifecycle which every Data Scientist performs when building machine learning models.
* As a reminder these are the typical phases of a Data Science project:
```
1. Data Preparation (e.g. ETL pipelines)
2. Exploratory Data Analysis 
3. Feature Engineering
4. Model Training
5. Model Validation —> ML engineering main role begins here
6. Deployment (e.g. cloud platform)
7. Monitoring
```
* This is where the fusion of Devops with Machine Learning and Data Science comes in to give us MLOPs which we will highlight below.


# Manual MLOPs Lifecycle
* This is less common but the manual components which are often done by most organizations without automation is as follows:

![image](https://github.com/user-attachments/assets/680434ab-d244-4f8b-9e9e-a8c76a5bf8af)



# Automated MLOPs Lifecycle
* A typical MLOPs life cycle that is automated looks like this [source](https://pub.towardsai.net/mlops-demystified-6bee7a44ba9a)



![image](https://github.com/user-attachments/assets/72f0bf53-b0c7-45f4-93b1-63b8168db288)


# Role Based MLOPs

## Data Scientists
* Data Scientists often/should Leverage MLFLow for:
  * Experiment tracking and hypothesis testing, Statistical analysis
  * Code structuring --> pipelines
  * Model packaging and dependency management 
  * Evaluating hyperparameter tuning of ML models
    * To train a model there are multiple parameters. 
    * MLFLow allows us to track EVERY parameter in real-time with visualizations. 
    * This is perhaps the strongest feature of MLFLow
  * Compare results of model retraining over time ---> Select the most optimal ML model for deployment 

## Prompt Engineering Users
* Prompt Engineers/Generative AI Engineers often leverage MLFLow to:

1. Evaluate and experiment with LLMs
2. Create custom prompts and experiment with them. 
2. Decide on best BASE model LLM suitable for project requirements. 


## MLOPs/MLE Professional 
* MLOPs/MLE often leverage MLFLow to:

1. Manage lifecycle of trained models both pre and post deployment.
2. Deploy models securly to production environments. 
3. Manage entire model deployment dependencies. 


# Most Common Use cases for MLFLow
1. Experiment Tracking  —> track parameters and metrics for models (e.g. accuracy, precision, recall, etc.) in User Interface
2. Model selection and deployment —> deploy the best model
3. Model performance monitoring
5. Cross-functional project collaboration with a team —-> every developer can review inputs and outputs

---
# Resources
- [Streamlining generative AI development with MLflow v3.10 on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/streamlining-generative-ai-development-with-mlflow-v3-10-on-amazon-sagemaker-ai/)
- [Advanced tracing and evaluation of generative AI agents using LangChain and Amazon SageMaker AI MLFlow](https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/)
- [MLflow Evaluation with SageMaker Jobs and Bedrock LLM-as-a-Judge](https://builder.aws.com/content/31vda6VY2m5U9xZMOhKQR3IMFkP/mlflow-evaluation-with-sagemaker-jobs-and-bedrock-llm-as-a-judge)
