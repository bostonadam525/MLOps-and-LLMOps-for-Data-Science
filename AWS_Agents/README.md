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

---
## 4. Safety and reliability: Behavioral boundaries

1. **Guardrail violations**
   - **AWS Bedrock Guardrails -- built-in metrics in CloudWatch**
   - Important to consider:
     - **How many requests were blocked or modified by AWS bedrock guardrails?**
     - **A spike can signal a shift in the input distribution -- such as adversarial prompts entering the system or other.**
     - **Do you need to customize or change the guardrails? Change keywords or rules?**

2. **Error Recovery Rate**
   - Tool call failures --> does agent recover and complete task or does it give up and crash?
   - Agent with low error recovery becomes a BIG reliability at scale.
   - Consider:
     - **Instrument try/except in tool handlers**
     - **Emit success/failure metric**
    
3. **Timeout Behavior**
   - Agent reaches its maximum iteration count without completing the task --> does it produce a useful partial result or a confusing error?
   - Important to define graceful degradation policy explicitly.
   - Consider:
     - **Set max_iterations in agent loop**
     - **Emit timeout metric to AWS CloudWatch**
    
4. **Policy Adherence Rate**
   - What percent of agent task executions are completed without attempting an action outside of the agent's authorized scope and role based access control?
   - Measure this by checking the tool call logs against an allowed action list.
   - Consider:
     - **Custom CloudWatch metrics**
     - **Emit per task with outcome label**

#### AWS Marketplace Safety Options
- Bedrock guardrails configure before first production deployment -- not AFTER
- Content filtering, topic restrictions, PII redaction are all available out of the box.


---
# Building Eval Pipeline on AWS

## Eval Pipeline Architecture
- The idea is to separate the classes of evals you need to do:

1. Layer 1 - Rule based (deterministic)
   - Deterministic gating --> you don't move to layer 2 until you pass this layer.
   - This doesn't cost anything.
2. Layer 2 - LLM as judge
   - Non-deterministic evaluations (probabilistic)
   - Only run the LLM-as-judge on cases that pass rule-based deterministic checks. This will cut the cost by 30-50% on typical agent workloads. DO NOT RUN LLM judge on EVERY CASE. 

<img width="723" height="365" alt="Screenshot 2026-09-28 150626" src="https://github.com/user-attachments/assets/2947412d-6f88-45f6-b775-5ab9a2f0ce28" />

---
## Designing a Test Dataset
- 3 things are required:

1. **Input goals**
   - Tasks you want agent to complete.
   - These might include (not just the "happy path" or most common expert based inputs): 
     - common inputs
     - edge cases
     - adversarial prompts
    

2. **Expected outputs**
   - For each input: what does a correct response look like?
   - This can be:
     - Specific artifact
     - Report format
     - Set of conditions output must satsify
    

3. **Evaluation criteria**
   - Per input/output pair --> rubric used to judge agent
   - Some criteria are binary (pass/fail)
   - Other criteria scored 1 to 5. 
       

<img width="698" height="344" alt="Screenshot 2026-09-28 151023" src="https://github.com/user-attachments/assets/d8545ad9-9fdf-433a-b0a3-fe96a2fcebce" />

---
## Failures -- Turn BAD results into REAL IMPROVEMENTS!
- Test cases that fail are actually signals to real important patterns in your data and application to help you improve it over time.

1. **Example Pattern: Same tool fails 80% of the time**
   - Diagnosis: Tool's description is ambiguous or schema unclear.

2. **Example Pattern: Failures cluster on 1 input class**
   - Diagnosis: System prompt doesn't handle input class explicitly

3. **Example Pattern: High tool call count on failing tasks**
   - Diagnosis: Agent is confused -- looping and retrying instead of reasoning to a conclusion.

4. **Failures appear random, no clear pattern.**
   - Diagnosis: Agent is operating near its capability boundary, or task definition is underspecified.

---
## Evaluation Driven Development -- The Improvement Cycle
- This is where you turn failures into improvements in your data flywheel using this process:

1. **Establish baseline**
2. **Identify weakest signal**
3. **Make 1 targeted change**
4. **Re-run and compare**

<img width="676" height="352" alt="Screenshot 2026-09-28 152806" src="https://github.com/user-attachments/assets/0053ab71-72de-4f49-93ee-59988071225f" />

---
## LLM-as-judge -- Design best practices for quality results
- **Critical Design Rules**

1. **Use different model as judge**
   - Self eval bias is real.
   - Use different model or model from different family. NEVER USE SAME MODEL FOR BOTH.

2. **Ground rubric in observable evidence**
   - Criteria such as "is this good" result in **inconsistent scores**.
   - Criteria such as "does this output include a valid VPC CIDR block" lead to **more reliable results.**

3. **Include rationale requirement**
   - Ask LLM judge to explain its score in 2-3 sentences with citations/references --> **expose rationale of LLM judge**
   - A rationale reveals when the judge is confused which pure scores cannot!

4. **Periodically calibrate with human scores**
   - Run human spot-checks on 10% of judge outputs at least quarterly.
   - Calibrate rubric when human and judge scores diverge by more than 15% (depends on your data, domain, use case). 


---
# Routing Agents + Decision Patterns

## Intent Classification and Routing Architecture

### What does a routing agent do?
- Routing agent receives request --> Classifies intent and directs it to appropriate specialist agent
- Routing agent DOES NOT need to be full agent with an entire reasoning loop -- single model call is enough for CLASSIFICATION

### Classifier Prompt should include:
1. **Clear category definitions**
   - describe each destination agent in 1 sentence.
   - ambiguous descriptions --> lead to ambiguous routing.
  
2. **Per-category examples**
   - 2 to 3 example inputs per category can calibrate model without fine-tuning it! (e.g. in-context learning)
  
3. **Handling ambiguous inputs**
   - define explicit "unknown" or "multi-intent" category and decide in advance what should be done to route those requests.
  
4. **Confidence scoring**
   - Ask classifier to return confidence score with category.
   - Route low-confidence requests to fallback path.
  

<img width="365" height="360" alt="Screenshot 2026-09-28 154303" src="https://github.com/user-attachments/assets/5c5b5339-52c0-4b7c-a35e-e0e0963b4e39" />



<img width="670" height="363" alt="Screenshot 2026-09-28 153518" src="https://github.com/user-attachments/assets/070a08bf-ff88-4cda-8ccf-1e127ee706ac" />

## Routing strategy selection
- Easy path: Start with AWS knowledge bases + embedding based routing -- this allows embedding semantic routing to work with intent matching using the Bedrock knowledge bases. You can add an LLM as the fallback or final tiered layer based on a confidence threshold.
  - You don't need a fine-tuned classifier model unless you have specific data or A LOT OF IT. 
- Different routing strategies include the following below:

1. Keyword rules (e.g. BM25, TF-IDF, regex, dictionary, or can even use a sparse encoder such as SPLADE)
2. Embedding routing (**recommended start for semantic matching**)
3. Classifier model (e.g. GliClass, Jev)
4. NER model (e.g. GliNER)
5. LLM routing
6. Hybrid (rules + LLM)
7. Graph routing (entity + relation classification, knowledge graph, ontology -- supplements embedding routing)


<img width="694" height="349" alt="Screenshot 2026-09-28 154855" src="https://github.com/user-attachments/assets/a27da028-8abc-4a8e-8238-202441fe8c05" />

---
## Evaluations: Can also be used for Agentic self-correction 
- Agent can go back and self-correct its responses.
- "offline" vs. "online"?
- online self-improvement --> higher latency, higher token usage, etc...

---
# Agent Evaluation Tooling
1. **Amazon Bedrock AgentCore Evaluations**
   - managed on-demand evaluation runs
   - built-in evaluators (fluency, correctness, helpfulness)
   - CloudWatch integration -- zero infra to manage
   - Custom evaluators using Amazon Bedrock model prompts

2. **Patronus AI**
   - Custom eval criteria (define our own!)
   - Automated regression tracking across versions
   - Hallucination and faithfulness scoring
   - Enterprise compliance and audit trails

3. **Deepchecks**
   - Automated hallucination detection
   - Data drift detection for RAG pipelines
   - CI/CD integrations -- runs as pipeline setup
   - Open source core + enterprise features






