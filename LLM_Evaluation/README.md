# LLM Evaluation
* There are various approaches, metrics, benchmarks, and frameworks to evaluating LLMs.
* This repo is devoted to experiments and overview of some of these approaches.



# LLM Evaluation Workflows
1. Logging and tracing at scale in development and production
2. Automating LLM evaluation workflows
3. Test LLM apps BEFORE DEPLOYMENT
4. Continuous monitoring in production


# Tools for LLM Evaluation
* There are multiple open and closed source evaluation frameworks and tools available. One of these is Opik.


## Opik for LLM Evaluations
* [Link to Opik github](https://github.com/comet-ml/opik)

### Opik -- Overview
* Open-sourced end-to-end platform for evalution, testing, and monitoring LLM applications.
* Supports simple, complex, and scalable tracing.
  * Need ability to scale and trace millions of users on your system!
* Allows for automating LLM evaluation workflows for variable use cases.
* Monitoring and Observability of all LLM applications you have in production.


### Opik -- LLM Evaluation Workflow
1. Build LLM application(s)
2. Log LLM calls and traces using Opik's open source integrations
3. Store and create "eval datasets" to run evaluations with
4. Using an evaluaton dataset, evaluation your application:
   * Human-in-the-loop (e.g. manual)
   * Automatic (e.g. heuristics)
   * LLM-as-a-judge
  
5. Utilize Opik's Pytest integrations to perform unit testing and compare/contrast results between outputs and runs of your application
6. Deployment and continuous monitoring of the LLM application throughout its lifecyle

### Opik for Tracing
* Logging LLM calls and traces can be performed using various methods

1. Opik's integrations (easiest method)
2. `@track` decorator
   * Tracking LLM calls
   * Tracking ANY function call in your LLM application.
   * This is most often used in tandem with Opik's integrations.
3. Python SDK
   * **Most flexible and personalization option.**
   * If you really want full control over your logging process use this approach.
4. REST API
   * If your app does not use Python, the Opik REST API is available to log traces.
