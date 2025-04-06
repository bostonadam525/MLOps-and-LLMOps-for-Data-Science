# DSPy - Declarative Self-improving Python
* The amazing concept here is instead of solely relying on prompting methods, you are able to write modular Python code and use DSPy to teach your LLM to produce high-quality and more precise outputs. 
* DSPy is a really cool framework for programming—rather than prompting—language models that came out of Stanford University.
* It allows you to iterate faster and build more modular AI systems.
* See the excellent [documentation here](https://dspy.ai/) to get started.


# Overview of the Concepts behind DSPy
* DSPy is not just a technical toolbox or framework, but rather an entirely different approach to working with LLMs.
* I first came across DSPy when I was building a program to perform multi-label classification on a BIG DATA set using an LLM with chain of thought prompting. I had not used DSPy and realized that DSPy is a very powerful framework that can be utilized for classifying millions of documents and much, much more!

## Basics of DSPy
1. **DSPy can replace "string based prompting"**
   * Yes that means you don't need to write detailed string based prompts with instructions to an LLM.

2. **The same prompt DOES NOT work for every LLM**
   * A prompt that works on GPT-3.5 turbo will not work the same with Claude-3.5-Sonnet, Llama, Mistral, etc.
   * The prompt config is actually called a "Signature" in DSPy.
  
3. **DSPy Optimizers**
   * Can automatically optimize prompts.
  

## What are the basic modules in DSPy?
1. Language Models
2. Signatures
3. Modules
4. Data
5. Metrics
6. Optimizers
7. Assertions


## Signatures in DSPy
* DSPy uses a "modular" approach to programming for each task completion.
* Modular programming is a paradigm many people know to better organize programs and applications using functions, classes, methods and objects.
* DSPy's modularity is to be able to **optimize prompts and LLMs to get the best outputs all the time.**

### What exactly are Signatures in DSPy?
* Building your prompts from Signature variables which provide prompt templates makes it MUCH easier to:
  * Create prompts
  * Modify and update prompts
  * Define and control behaviors of each module in your program
  * Define semantic roles
* Just about ANY NLP task can be implemented via Signatures which are fully optimized to output better results.

### What types of Signatures are there?
1. **Inline Signatures**
   * These are used directly inside modules.
   * Format is generally: `Input --> Output`
2. **Class Signatures**
   * These always start with a `Docstring` which hints the task of the class.
   * Descriptive arguments give hints of the input fields.
   * Descriptive arguments with constraints are given related to the output fields.

### How do Signatures help with programming?
1. Easily allows you to represent your programs as object oriented classes.
2. Easily assign variables.
3. Programmaticaly modify prompting rather than individual strings.
4. Can be easily used within modules as Classes.

### What are Signatures integrated with?
* The Signatures module is fully integrated within DSPy with such modules as:
  1. `Predict`
  2. `ChainOfThought`
  3. `React`
  4. `ProgramOfThought`
  5. `MultiChainComparison`
  6. `Majority`


# What are the use cases for DSPy?
* Various NLP tasks are available:
  1. Question-Answering workflows
  2. Building LLM driven Classification Models
  3. RAG pipelines (simple to very sophisticated)
  4. Agentic workflows and applications including finetuning Agents
  5. Reasoning (e.g. Chain of Thought)
  6. Entity Extraction (e.g. Named Entity Recognition or NER)
  7. Classification Finetuning
  8. Multi-Hop Search/RAG
  9. Privacy-Conscious Delegation
  10. Image Generation Prompt iteration
  11. Output Refinement
  12. Debugging & Observability
 

## Extreme Multi-label Classification
* What do you do when you have a very large number of possible classes in a dataset and you don't have a ground truth dataset/corpus?.
* This problem is actually well known and is appropriately called: "extreme classification".
* The ability to parse a BIG DATA set and extract a very large number of classes is a very challenging task because an LLM needs to be able to understand and adequately distinguish between all potential categories.
* This is somewhat similar to "Generative Pseudo Labeling" or GPL which is another approach to this problem.
* See these Resources for more background
  * This paper entitled [In-Context Learning for Extreme Multi-Label Classification](https://arxiv.org/abs/2401.12178) is a great place to begin understanding this problem better.
  * This blogpost entitled [DSPy: In-Context Learning for Extreme Multi-Label Classification](https://training.continuumlabs.ai/knowledge/retrieval-augmented-generation/dspy-in-context-learning-for-extreme-multi-label-classification) by Continuum Labs is another excellent resource.
 

# Comparing Unsupervised vs. Semi-Supervised vs. Self-Supervised Learning
* These concepts are all machine learning frameworks but are related to DSPy which is why they are here.
* All 3 frameworks can be used for information extraction, classification, and working with data that is either unlabeled or partially labeled.
* Generally speaking, Unsupervised and Self-Supervised Learning are often used for generating labels for training Supervised Machine Learning algorithms.

## Self-Supervised Learning
  * Chain of Thought Prompting where you give a zero shot or few shot example prompting to an LLM and ask it to generate labels or classification is a form of self-supervised learning.
  * DSPy (Declarative Self-improving Python) is a framework that uses a self-improving approach to optimize language model pipelines, which can be seen as a form of self-supervised learning, where the system learns to improve its performance without explicit labels.


## Semi-Supervised Learning
