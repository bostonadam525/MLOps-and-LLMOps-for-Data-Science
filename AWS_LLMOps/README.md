# AWS LLMOps on Bedrock
* Generative AI LLMOps on AWS is important to understand the process and general workflow before you build anything.

## Generative AI LLMOps Workflow
1. **Define Scope**
  * Define and narrow your use case(s).
  * Define requirements 

2. **Choose the right Model(s)** —> This has 2 parts
  * a. Foundation Models
      * Model examples: OpenAI, Google Gemini, Claude, etc..
      * Fine tune foundation models (e.g. LoRA, QLoRA)
  * b. Custom LLMs
      * Build your own LLM from scratch!
      * Significant resources are required (e.g. training data, compute resources, etc..)
   
  * Great post from hugging face on linked-in about model size vs. performance and cost:

![image](https://github.com/user-attachments/assets/14fe766a-efeb-4911-81ea-739e54406ea9)




3. **3 Main Tasks**
  * a. Prompt Engineering
  * b. Fine Tuning
  * c. Train with human feedback (RLHF)

4. **Evaluation**
  * a. Metrics
  * note: Steps 3 and 4 you can combine —> "adapt and align models"

![image](https://github.com/user-attachments/assets/7cdc8ed5-1790-4fbd-846d-0c9b142a72ab)


5. **Deployment**

6. **Application Integration into AWS Cloud**
  * a. Optimize and Deploy Models for inferencing —> LLMOps
      * Example: GROQ uses LPU for inferencing 
  * b. Build LLM Powered Application


* Image from [AWS blog](https://aws.amazon.com/blogs/machine-learning/fmops-llmops-operationalize-generative-ai-and-differences-with-mlops/)
![image](https://github.com/user-attachments/assets/fbdd2af0-9504-453c-8911-40f8dbce81d1)
