# AWS Bedrock Evaluations

---
# What is Evaluation?
- **Tradeoff between:**
  - Quality
  - Cost
  - Latency

## Why is Evaluation Important?
- Quality, Cost, Latency tradeoffs
- Align to company's style and brand voices
- Evaluate specific domain use cases
- Evaluate on your company/domain specific data
- Monitor biases, safety, trust --> **Responsible AI**

---
# Bedrock Model Evaluation
- Eval, compare, select best foundation models for your use cases:
  - Public API
  - Eval custom models
  - Eval distilled models
  - Eval imported models
  - Eval prompt routers
  - Any model hosted outside of Bedrock
  - Use LLM-as-a-judge

- **Workflows and use cases:**

1. Curated datasets or bring your own data for tailored results
2. Automatic (algorithmic or LLMs) or human evaluation methods
3. Leverage in-house team or AWS-managed reviewers
4. Predfined and CUSTOM metrics
5. Evaluate ANY model/app hosted ANYWHERE

# Bedrock Built-in Evaluation Methods

## 1. **Programmatic/Automatic Evaluation**
   - Accuracy
   - Robustness
   - Toxicity

## 2. **Algorithms**
   - BERTScore
   - Classification accuracy
   - F1 score
   - Real-world knowledge score
  
## 3. **Human Evaluation**
   - Creativity
   - Style
   - Tone
   - Accuracy
   - Consistency
   - Brand voice

## 4. **Rating Methods**
   - Thumbs up/down
   - 5-point Likert Scaless
   - Binary choice buttons
   - Ordinal/Preference ranking
  
```
Supported rating methods include:
• Comparison Likert Scale (comparisonLikertScale): A scale for rating relative quality or preference between two model outputs.
• Choice / Radio Buttons (comparisonChoice): Direct selection options to pick a preferred response.
• Ordinal Rank / Preference Rank (comparisonRank): Ranking multiple model outputs in order of performance.
• Thumbs Up / Down (thumbsUpDown): Binary rating for acceptable or unacceptable outputs.
• Single Model Response Likert Scale (individualLikertScale): Individual score rating for a single model's response

```

## 5. LLM-as-a-judge - Multiple metrics out of the box
1. Correctness
2. Completeness
3. Faithfulness
4. Helpfulness
5. Coherence
6. Relevance
7. Following instructions
8. Professional style and tone
9. Readability
10. Harmfulness -- responsible AI
11. Stereotyping -- responsible AI
12. Answer refusal -- responsible AI
13. Custom Metrics -- customize to your data/domain/company

### How correctness works
- **NOTE: Correctness can be WITH or WITHOUT ground truth.**
- Judge gives a score similar to MLflow scorers

- Example input:

```
prompt: What is the capital of Spain?
referenceResponse: Madrid
Model response: Barcelona
```
- **Judge prompt (simplified version)**

```
You are a helpful assistant...
You are given a question, a candidate response from an LLM, and reference response.
Your task is to check if the candidate response is correct compared to the reference response...

Here is the actual task:
Question: {prompt}
Reference Response: {referenceResponse}
Candidate Response: {Model response}

Explain your response, followed by your evaluation:
2) Correct
1) Partially correct
0) Incorrect

```

## 6. LLM reasoning
- Multistep reasoning
- Correlation with expert human evaluators
  
---
### Accuracy & Quality
- **Example RAG metrics:** Separately evaluates retrieval-only steps (context relevance and coverage) as well as combined retrieve-and-generate workflows (hallucination detection and faithfulness)

```
• Builtin.Correctness: Measures response accuracy against a ground truth.
• Builtin.Completeness: Assesses whether all parts of the prompt question are answered.
• Builtin.Faithfulness: Checks if the response relies strictly on provided context without unsupported external info or hallucinations.
• Builtin.Helpfulness: Evaluates overall coherence, instruction adherence, and implicit user needs.
• Builtin.Coherence: Detects logical gaps and contradictions.
• Builtin.Relevance: Measures direct alignment with the prompt.
• Builtin.FollowingInstructions: Checks exact adherence to multi-step or rigid directions.
• Builtin.ProfessionalStyleAndTone: Evaluates appropriateness of the voice
```

### Responsible AI & Safety

```
• Builtin.Harmfulness: Detects toxic or harmful content.
• Builtin.Stereotyping: Identifies cultural, social, or demographic biases.
• Builtin.Refusal: Tracks whether the model appropriately declines out-of-bounds or unsafe requests

```

### Built-in Task Types & Datasets
- Jobs can be configured around standard generation tasks using curated open-source datasets (such as BoolQ, Natural Questions, TriviaQA, WikiText2, Gigaword, and RealToxicityPrompts) mapped to:

```
• General text generation
• Text summarization
• Question and answer (Q&A)
• Text classification
```

---
# Workflow for Automatic Evaluations

## 1. Go to Bedrock Evaluations

<img width="828" height="590" alt="Screenshot 2026-10-08 152438" src="https://github.com/user-attachments/assets/56786985-4e5c-4977-88d2-605caaa35275" />

## 2. Choose judge vs.programmatic

<img width="760" height="285" alt="Screenshot 2026-10-08 152535" src="https://github.com/user-attachments/assets/e61e0730-550b-414b-8ddc-3561aae0ad1a" />

## 3. Select Model
- Pick model from pop up

<img width="811" height="605" alt="Screenshot 2026-10-08 152835" src="https://github.com/user-attachments/assets/cc876f7c-514f-46fc-b29b-782dda84a485" />

## 4. Inference Source
- Select **Bedrock** vs. **Choose your own**
- If you select Bedrock --> pick model via API list
- If select bring your own:

```
Bring your own inference responses
With Bring your own inference responses, you provide both the input prompt and the generated response in your input JSONL file.
Name the file 
```

## 5. Metrics 
- Select from 9 Quality metrics
<img width="1083" height="531" alt="Screenshot 2026-10-08 153509" src="https://github.com/user-attachments/assets/fe968c23-2a64-4fb0-98e8-7d031f944d73" />


- Select from 3 Responsible AI metrics

<img width="1079" height="487" alt="Screenshot 2026-10-08 153604" src="https://github.com/user-attachments/assets/d6f5b42c-265c-4227-8537-34307c3e1b25" />



- Custom metrics -- 3 methods to select from:

1. Import JSON file
2. Use a template
3. Custom -- with custom you can edit an existing prompt template and customize it, or create your own from scratch


## 6. Dataset
- Add custom dataset (JSONL) from S3 bucket.
- Limit is ~1000 lines or conversations for each job (human curated data). 
- Fields:
  - input -->
  - output reference response (optional) -->
  - model response (optional) -->
  - model identifier

## 7. IAM Role permissions
- Add your IAM role

---
# Reviewing Evaluations
- You can review the traces in the console from each judgement, prompt, and score for each set of responses from the model.
- You can comment on the scores and add feedback. 

---
# Bedrock RAG Evaluations


---
# Resources
- [AI evaluations on Amazon Bedrock | AWS Show and Tell - Generative AI | S1 E16](https://www.youtube.com/watch?v=Qbgl9Ttugug&list=PLYd-r9uJ9Y-Q&index=44)
- [Create a human-based model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create-human.html)
- [Review a human-based model evaluation job in Amazon Bedrock (console)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-human-customer.html)
- [LLM-as-a-judge on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
- [MLflow Evaluation with SageMaker Jobs and Bedrock LLM-as-a-Judge](https://builder.aws.com/content/31vda6VY2m5U9xZMOhKQR3IMFkP/mlflow-evaluation-with-sagemaker-jobs-and-bedrock-llm-as-a-judge)
- [Use metrics to understand model performance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html)
- [Use built-in prompt datasets for automatic model evaluation in Amazon Bedrock](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-evaluation-prompt-datasets-builtin.html)
