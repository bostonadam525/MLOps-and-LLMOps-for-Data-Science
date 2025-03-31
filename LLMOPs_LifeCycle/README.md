# LLMOPs LifeCycle

* Source: Udacity AI
* As we see below there are 6 main steps in a typical LLMOPs life cycel:
1. Data Prep & Exploration
2. Pretraining LLM(s)
3. Model Finetuning & Prompt Engineering
4. Model Evaluation & Debugging
5. Model Deployment
6. Model Monitoring & Maintenance

![image](https://github.com/user-attachments/assets/8edcccc1-f8e5-4a42-bfa4-ce4ce1785f1e)



## Common Frameworks
1. LLM Providers
   * OpenAI
   * Cohere
   * Anthropic

2. LLM Tools
   * These could be vector DBs, evaluation tools, experiment tools, and orchestration tools.
   * Some of these include:
     a) Pinecone (vector DB)
     b) W&B
     c) mlflow
     d) snorkel
     e) coment

3. LLM Frameworks
  * Langchain
  * Llama-index
  * Hugging Face

4. LLM Infrastructure
   * Tools for prompting, database management, etc.
   * These include but are not limited to:
     a) Databricks
     b) AWS
     c) Azure
     d) GCP
     e) snowflake


## LLMOPs vs. MLOPs
* LLMOPs common considerations

1. Fine tuning base models with high quality data and efficient techniques.
2. Evaluating and debugging LLMs
3. Optimizing prompt engineering, management, and tracking
4. Pipeline construction to chain LLM calls and operations
5. Optimization: Cost AND Latency
6. Version Control: LLM model maintenance --> cost, quality, safety, efficiency
7. Feedback incorporation: human feedback included in training data and fine-tuning over time.


# LLMOPs Pipelines
* Depending on the complexity of your application there are generally 3 main pipelines
* Source: Paul Iusztin, Alexandru Răzvanț and Pau Labarta Bajo
1. **Features Pipeline**

![image](https://github.com/user-attachments/assets/82cecf30-9c3c-4c35-be48-ca4ae36f69bf)

2. **Training Pipeline**

![image](https://github.com/user-attachments/assets/211854be-6aea-47a7-95f2-bc10cafc249d)

3. **Inference Pipeline**
![image](https://github.com/user-attachments/assets/4f87b891-484e-48f6-b101-a424d518dcc3)
