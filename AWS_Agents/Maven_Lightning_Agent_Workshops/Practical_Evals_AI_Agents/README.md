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
- **One thing at a time!**

1. **Precision (Quality)**
   - example: If agent moves 10 emails to your spam folder, how many of those 10 are actually spam?

2. **Recall (Quantity)**
   - example: If you have 50 total spam emails in your email inbox, how many of those 50 did the agent actually catch?

3. **Latency (Speed)**
   - How long does it take for a user to receive a response from the system?

4. **Cost (Price)**
   - What is the $$$ to get a response from the system?
