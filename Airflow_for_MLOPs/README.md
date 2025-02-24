# Airflow for MLOPs and Big Data
* This repo contains everything related to using Airflow for MLOPs and Big Data. 




## Apache Airflow - key concepts
1. **DAG (Directed Acyclic Graph)**
  * A Collection of tasks that you want to schedule and run in your ML pipeline or Data Science project.
  * Airflow is a DAG. 
2. **Two important components of DAG**
  * **Directed** —-> tasks must have a specific sequence or flow (e.g. A —> B —> C)
  * **Acyclic** --> no task should be dependent on itself!!
  * Example of a DAG in Airflow, [source](https://medium.com/thefork/a-guide-to-mlops-with-airflow-and-mlflow-e19a82901f88)

![image](https://github.com/user-attachments/assets/76946e71-5570-466a-b3a6-8b0599e9d80d)



## Tasks 
* These are individual units of work in a DAG. 
* Examples include but are not limited to:
  * Data ingestion
  * Feature engineering
  * Python functions
  * Database queries
  * Sending API or HTTP requests 



## Dependencies 
* All tasks in DAGs have dependencies.
* This means that 1 task might need to be completed before other tasks can begin. 
* These dependencies allow you to personalize and control the order in which specific tasks are executed. 
* Airflow gives you tools such as `set_upstream` and `set_downstream` to define these dependencies between tasks. 


# Why would you use Airflow for MLOPs? 
* In Machine Learning Operations (MLOPs), orchestrating and directing ML workflows in an efficient manner is crucial for ensuring that seamless automation of certain tasks occur such as:
  * Data pipelines (e.g. ETL)
  * Feature engineering 
  * Model training
  * Deployment
* These are the key pillars in most ML pipelines, [source](https://medium.com/thefork/a-guide-to-mlops-with-airflow-and-mlflow-e19a82901f88)

![image](https://github.com/user-attachments/assets/c37bca60-e05d-4672-9796-93be910bec1b)

* Airflow allows you to define —> automate —> monitor every step of a standard Machine learning pipeline.
* The ML engineering hierarchy of "needs" as defined by this [source](https://medium.com/thefork/a-guide-to-mlops-with-airflow-and-mlflow-e19a82901f88):

![image](https://github.com/user-attachments/assets/fbd1a885-bf19-4dd3-a36f-b3dc50f6358c)



## 1. Orchestrating ML and ETL Pipelines 
* With Airflow you can define “DAG” (directed acyclic graph) which are the TASKS and DEPENDENCIES for each of these crucial steps in the pipelines. 
```
Data Ingestion —> Data pre-processing —> Model Training & Evaluation —> Model Deployment
```

## 2. Task Automation


## 3. Monitoring AND Alerts
  * Real-time monitoring in the Airflow UI for:
      * ETL Pipelines —> Weekly? Daily? Hourly? …etc.. 
      * Model retraining  —> 
  * Task Logs
      * Shows specific details for debugging and problem solving. 
  * Alerts and Notifications 
      * Automatically sends email alerts, slack alerts, etc…
  * Retry Mechanism
      * Based on pre-defined rules-logic it will retry the task(s) that failed again. 






# References & Resources
* [A Guide to MLOps with Airflow and MLflow](https://medium.com/thefork/a-guide-to-mlops-with-airflow-and-mlflow-e19a82901f88)
* [Airflow MLOps documentation](https://airflow.apache.org/use-cases/mlops/)
* [MLOps github](https://chicagodatascience.github.io/MLOps/logistics/)
