# Error Analysis for AI/ML Engineering
* These are notes from an open webinar put on by Hamel Husain and Shreya Shankar via Maven Analytics.


# What is Error Analysis
1. Involves finding **specific errors** in an AI/ML application.
2. Helps teams determine what/when they should:
   - Invest time in....
   - Measure & Evaluate (e.g. what metrics?!?)
3. This is NOT NEW. This has been in Data Science & Machine Learning for decades!

# Workflow for Error Analysis
1. **Annotate**
   * Look at and evaluate the AI/ML application outputs.
     * This number can vary based on your data. Start with 20 to 30 and go from there. 
   * Make notes. You can do this with just about any tool (e.g. open source tools such as LangSmith, RAGAS, Langflow), or build your own. 
2. **Categorize**
   * LLM as a judge can be used to categorize or classify your annotations/notes.
   * Merge/rename categories as needed.
   * Use well-known Data Science techniques (e.g. clustering, topic modeling, etc..) to analyze the categories. 
3. **Analyze**
   * Perform statistical analysis of the categories from step 2. Count them, do a dive deep into what is there!
   * This should be "Sanity Check".
   * Make a pivot table of the most common and least common errors. Make data visualizations. 
   * Again, you can use an LLM to do this (e.g. ChatGPT, Claude, etc.) as a quick way to get answers. Then you can always run more refined or specific analysis using algorithms if needed. 
4. **Ship Improvements & Evaluations**
   * Fix issues
   * Create evaluation metrics or evaluate current eval metrics in place. Do the current eval metrics make sense for your application & data? 
5. **Iterate, Iterate, Iterate**
   * As with any application in production and engineering, work should be agile and cyclical NOT waterfall.
   * No application is perfect --> iterate, go back and iterate over various steps in the process.
   * Aim to improve your error analysis
  

# Common Problems
1. Avoid "whack a mole".
   * This means attempting to fix something by ONLY using prompt engineering or tuning 1 or 2 parameters in your RAG pipeline.
   * As with the "whack a mole game", fix 1 thing and another mole will pop up.

2. Not looking at your data
   * If you aren't evaluating and looking at your data, thats a big problem.
  
3. Not doing a "holistic" or "global" evaluation.
   * Don't "whack a mole", look at the problem from a big picture perspective and if you need to iterate over time to fix it then do so.

4. Not having evaluation metrics or the "correct" eval metrics
   * Evaluation metrics still apply in LLMOPs just as they do in MLOPs and all Data Science model deployments. 
