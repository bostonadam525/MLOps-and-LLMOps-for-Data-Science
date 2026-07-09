# Notes from: Stop Letting Your LLM "Find the Issues" In Your Data
- These are my notes from this excellent lecture series: https://maven.com/lls/21f487

---
# 3 Step Lifecycle 
1. Analyze your data for errors and mistake types.
2. Measure what and how prevalent the mistakes are.
   - If certain failure modes are more prevalent than others, you should prioritize measuring and fixing those. 
3. Work to improve your product to avoid making those mistakes.

NOTE: This is an ITERATIVE lifecycle!

<img width="1087" height="701" alt="image" src="https://github.com/user-attachments/assets/accb2ead-7996-44fa-9487-a2997e281601" />

## Step 1: Analyze
- The example that Shreya gave was an AI writing assistant.
- These are the analysis steps she proposed:
  - Discovery-oriented --> "mistake" is NOT easy to define, need to perform EDA and other common data analysis and data science and data modeling techniques to understand your data and its nuances. There is no perfect example of what a mistake is. It can have many levels or meanings depending on your product and use case. 
  - e.g. for this task, can you precisely defien what "AI slop" is? All writing anti-patterns? How would you parse and identify these error types?
  - Unlike traditional supervised Machine Learning, where mistake is defined as `prediction != label`, that is not the case here. 


## Step 2: Measure
- Next you need to measure how prevalent the mistakes are.
- These are the steps proposed:
  - Lots of different failure modes (e.g. emoji overuse, "its not just X, its Y", etc.)
  - Pareto principle --> 80% of mistakes are caused by 20% of failure modes -- usually...
  - Need to prioritize mistake to fix them. There is no "one size fits all".
 
## Step 3: Improve!!!!!!
- Next is to work on improving the product to fix and avoid those mistakes found above.
- This might include:
  - Change prompt (e.g. add instruction "never say its not X, its Y")
  - Switch models (e.g. switch LLM foundation models from GPT to Opus or within family)
  - Fine-tune models (e.g. train Kimi 2.6 on curated writing examples)
  - ....the list goes on....
 
---
## 3- Step Evals Lifecycle
- AI is NOT very good at automating the Analysis and the Measurement. Does that surprise you that a stochastic model is not able to analyze as well as more deterministic methods? It shouldnt.
- However, later on AI can help with automation with some measurements, prompt optimzation, coding, and improvemements.

---
# Common Mistakes that are made

## Mistake 1 -- Asking AI to "Do Evals now"
- Example of what not to do: "Check out my traces for my AI writing asst app. Can you evaluate the app? here is the jsonl file."
- We are all guilty of this at some point.

### So why is this bad?
  - Agent can discover some issues but will **miss all taste-specific issues** --> perhaps context is key here? 
  - Agents typicaly do not find the highest-priority issues
  - No reuse in this workflow --> re discover and write code to measure every issue from scratch each time. Need to build on previous efforts. **Needs previous context for this workflow to be useful each time.**
  - **What we want in our workflow is to persist intermediates of the lifecycle (failure mode definitions, code or LLM judges that measure their prevalence, and constant visibility and updates).**

### Can we ask AI to do evals correctly?
- key: Stick to "analyze-measure-improve" workflows
- AI for analyze: very human in the loop --> should not fully outsource this
- AI for measure and improve --> less needed for human in the loop.


### How to build an AI assisted eval workflow
1. Understand the data
   - load files
   - inspect 5 to 10 records
   - identify fields, content structure, variations
   - think about likely failure themes/categories
