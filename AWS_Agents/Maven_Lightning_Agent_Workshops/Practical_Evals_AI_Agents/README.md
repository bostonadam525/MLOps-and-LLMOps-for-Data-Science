# Learn How To Evaluate AI Agents: A Practical Framework
- Full webinar here: https://maven.com/p/a82511/learn-how-to-evaluate-ai-agents-a-practical-framework
- Full presentation by Sol Farahmand
- These are my notes and takeaways from his lecture

---
# What is an Eval?
- Structured, repeatable testing framework of AI application performance over specific tasks or behaviors.
- **Key: Compares what the system should do vs. what system actually does.**
- **Key: There really should never be 1 size fits all evaluation, each situation is different.**
- **Key questions:*
  - **What should the application do?**
  - **What did it actually do?**
  - **Did it meet the expected behavior?** (**this is crucial -- you need to define this!)**

---
# Evals are similar to Scientific Experiments
- At a high level you:

1. **Establish a Baseline!!**
   - Run evals to measure CURRENT baseline performance and reveal where model and application fall short

2. **Change ONE thing -- iterative improvements**
   - Revise prompt(s)
   - Switch model(s)
   - or, Change logic
  
3. **Retry and compare**
   - Run same evaluation(s) again and compare results with baseline.
   - Why --> this reveals whether the change improved or reduced the performance.

---
# What Can We Evaluate?
- **One thing at a time, per agent, per system, per loop**

1. **Precision (Quality)**
   - example: If agent moves 10 emails to your spam folder, how many of those 10 are actually spam?

2. **Recall (Quantity)**
   - example: If you have 50 total spam emails in your email inbox, how many of those 50 did the agent actually catch?

3. **Latency (Speed)**
   - How long does it take for a user to receive a response from the system?

4. **Cost (Price)**
   - What is the $$$ to get a response from the system?
  
---
# What is the error rate of an agent's response?
- We need to config, optimize, and test an acceptable baseline.
- The error rate we determine is equal to or less than this baseline (e.g. <= 5%)

---
# The 4 Parts of an Evaluation Framework

## 1. The Dataset = A Collection of test cases
- Can be synthetic -- not ideal to real world data
- Most ideal --> client, domain, user data with real-world examples/cases
- Dataset composition:
  - input
  - response (expected behavior, expected category -- e.g. prompts, instructions)
  - JSON structure

- **Key: Quality over Quantity**
  - You are not setting up the agent for success, your goal is to set it up for failure (e.g. edge cases), as real-world data is never static.

## 2. The Model = The LLM (large language model)
- The flow:
  - 1) User input (request supplied to model)
    2) LLM (model processes the input)
    3) Response (generated output)

## 3. The Evaluator = The check used to decide good vs. bad
- **This is crucial**
- What we see below is that there are 3 types of evaluators:
  - Fixed rule evaluation (code logic)
  - LLM-as-judge
  - Human annotation + in the loop feedback
- The flow:

```
Type of Evaluator | Fixed Rule Evaluator            |LLM As A Judge                         | Human Annotation
When to Use       | 1 correct answer or exact value |Open-ended qualities with clear rubric |Nuance, Ambiguous, high-impact cases


```
- Rubric evaluations are not a bad idea:
  - binary vs. multi-label vs. multi-class
  - threshold (passing score)
 
---
## 4. Metrics = Show how the Agent performed across the dataset
1. **Overall Results**
  - the overall result does not show whether the Agent performs consistently across every kind of request.

2. **Segmented Results**
   - Breakdown by percent, example:

```
Deliveries: 96%
Damaged products: 92%
Account issues: 94%
Refunds: 78%

```

---
# The Process of Evaluations
1. Create Dataset with INPUT & OUTPUT --> can build this over time with user input (user data)
2. Create Evaluator with a threshold (need to calibrate this over time) --> threshold establishes standard
3. Trust the evaluator with the dataset
4. Run The Agent & The Evaluator against the dataset --> get a baseline
5. Identify the Problems
6. Fix ONE thing (start small, iterate)
7. Re-run
8. Compare re-run against baseline AND Document it --> iterate on process



---
# Resources
- [PromptFoo](https://www.promptfoo.dev/)
- 
