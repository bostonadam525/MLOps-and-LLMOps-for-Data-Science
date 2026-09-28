# AWS Agents 
- Everything related to using Agents on AWS.
- A good resource to start from: [Building agentic systems on AWS](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/?trk=4dccf88d-b255-470f-82d0-13e00449c5f4&sc_channel=el&refid=bf3e7bdd-12f2-4e8b-a20f-efc016685f96)

---
# Four Dimensions of Agentic Evaluation

1. **Task Completion**
   - Did the agent complete FULLY the stated or intended goal?
   - **VERY CRITICAL: binary pass/fail or graded as "partial credit"**
   - This CANNOT be the only signal you evaluate.
  

2. **Reasoning Quality**
   - Did the agent take "the right path" to reason over its answer/response?
   - Which tools? Which data?
   - Agents that reach the "right answer" via hallucinated or fabricated intermediate steps will fail on novel or unseen inputs.

3. **Operational Metrics**
   - Is the agent practical to run -- is it efficient?
   - These might include:
     - **Latency** -- are agents pausing too long to get human feedback? is this a problem? 
     - **Cost per task, request**
     - **Tool call counts**
     - **Loop iterations**
     - ...etc...
    
4. **Safety and Reliability**
   - Is the agent following directions and staying within defined boundaries?
   - These include but are not limited to:
     - **Guardrail violations**
     - **Policy adherence**
     - **Error recovery**
     - **Timeout behavior**
     - **PII adherence**
     - **Role based access control**
    
---
## 1. Task Completion -- Measure it right

### 3 approaches by task complexity:
1. **Binary pass/fail**
   - Most recommended for tasks with **single correct output** -- e.g. did CDK stack deploy?
   - **Deterministic**
   - **Cheap**
   - **Fast and efficient to run**
  
2. **Partial credit scoring**
   - Score 0-5 on pre-defined criteria when many valid outputs exist.
   - This requires a rubric and LLM-as-a-judge.
   - **Use Case:** open-ended report generation

3. **Human Spot Check**
   - Important for calibrating LLM judges.
   - Periodic sampling 10% of system outputs --> domain expert scores those outputs.
   - **Judge drift detection: use divergences from sample**

### What makes a good test dataset?
1. **Input variety**
   - All expected task types INCLUDING edge cases.
   - If you only have a core set of "happy path examples" you will miss ~80% of real failures

2. **Adversarial prompts**
   - include inputs designed to confuse the agent:
     - **ambiguous goals**
     - **missing context**
     - **contradictory instructions and information**

3. **Expected output spec**
   - Define expected outputs in terms of CONDITIONS not exact strings such as:
     - "CDK stack includes Amazon ECS" not "output equals X".
     - This is NOT the same as unit testing.....

4. **Start small, grow with purpose**
   - Begin with every 20-50 high-quality test examples.
   - **Add new cases every time you find a new failure mode in production data.**
---
#### AWS Marketplace example
- Patronus AI is good for custom eval criteria and regression tracking across agentic versions -- most ideal when output formats evolve over time.

---
## 2. Reasoning quality - Inspecting Agent Traces

1. **Correct tool sequence**
   - Did the agent invoke tools in the correct order?
   - If the agent is using tools out of order it could mean the agent is guessing, hallucinating, fabricating, or confused and NOT actually reasoning and acting (ReAct).
  
2. **Evidence-grounded reasoning**
   - Does the agent's reasoning text align with the tool results it actually received?
   - **If agent is ignoring results from tools --> precursor to hallucinations and fabrications!**
  
3. **Valid tool parameters**
   - Are tool parameter arguments well-formed and sensible?
   - Invalid parameters lead to prompt ambiguity in tool description.
  
4. **No claims are supported**
   - Can you trace all of the agents factual assertions to actual context?
   - **Traces and spans are critical**
   - If you can't trace the assertions to context --> hallucinations and fabrications are an issue!
  
#### AWS Tools for trace inspection
- LangSmith, LangFuse, MLflow have trace Us.
- DeepChecks -- automates hallucination detection in agent pipelines.

---
## 3. Operational Metrics -- Running agents efficiently
- These are common operational metrics you should track with each agent:

<img width="686" height="335" alt="Screenshot 2026-09-28 144650" src="https://github.com/user-attachments/assets/7eb2d67e-7bbf-419b-954a-7ab0aa839cf9" />

