# DSPy - Declarative Self-improving Python
* The amazing concept here is instead of solely relying on prompting methods, you are able to write modular Python code and use DSPy to teach your LLM to produce high-quality and more precise outputs. 
* DSPy is a really cool framework for programming—rather than prompting—language models that came out of Stanford University.
* It allows you to iterate faster and build more modular AI systems.
* The package also has algorithms out of the box for optimizing prompts and weights, which can be used whether you are:
  1. Building LLM driven Classification Models
  2. RAG pipelines (simple to very sophisticated)
  3. Agentic workflows and applications including finetuning Agents
  4. Reasoning (e.g. Chain of Thought)
  5. Entity Extraction (e.g. Named Entity Recognition or NER)
  6. Classification Finetuning
  7. Multi-Hop Search
  8. Privacy-Conscious Delegation
  9. Image Generation Prompt iteration
  10. Output Refinement
  11. Debugging & Observability

* See the excellent [documentation here](https://dspy.ai/) to get started.


# Overview of the Concepts behind DSPy
* DSPy is not just a technical toolbox or framework, but rather an entirely different approach to working with LLMs.
* I first came across DSPy when I was building a program to perform multi-label classification on a BIG DATA set using an LLM with chain of thought prompting. I had not used DSPy and realized that DSPy is a very powerful framework that can be utilized for classifying millions of documents and much, much more!


## Extreme Multi-label Classification
* What do you do when you have a very large number of possible classes in a dataset and you don't have a ground truth dataset/corpus?.
* This problem is actually well known and is appropriately called: "extreme classification".
* The ability to parse a BIG DATA set and extract a very large number of classes is a very challenging task because an LLM needs to be able to understand and adequately distinguish between all potential categories.
* This is somewhat similar to "Generative Pseudo Labeling" or GPL which is another approach to this problem.
* See these Resources for more background
  * This paper entitled [In-Context Learning for Extreme Multi-Label Classification](https://arxiv.org/abs/2401.12178) is a great place to begin understanding this problem better.
  * This blogpost entitled [DSPy: In-Context Learning for Extreme Multi-Label Classification](https://training.continuumlabs.ai/knowledge/retrieval-augmented-generation/dspy-in-context-learning-for-extreme-multi-label-classification) by Continuum Labs is another excellent resource.
 

## Monolithic LLMs
