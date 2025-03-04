# Machine Learning Explainability
* Testing model explainability before model training, after model training, and in production are crucial to avoiding bias in machine learning model outputs.
* This repo contains resources, code, techniques and experiments related to ML model explainability.



## Data Science Metrics for Model Explainability
* There are numerous open source Python packages including: LIME, SHAP, ELI5 that give access to some important and specific bias metrics such as:
```
1. Accuracy Difference
2. Difference in Positive Proportions in Predicted Labels
3. Recall Difference
4. Recall Parity
5. False Positive Rate Parity
6. Disparate Impact formula
7. Specificity Difference
8. Difference in Ratio of Error Types
9. ...etc..
```
* Specific Python Libraries
  1. [SHAP](https://shap.readthedocs.io/en/latest/)
  2. [LIME](https://medium.com/@shreeraj260405/hands-on-lime-practical-implementation-for-image-text-and-tabular-data-95566da87f57)
  3. [ELI5](https://eli5.readthedocs.io/en/latest/)

# Resources
1. [AI Fairness 360 - AIF360 by IBM](https://github.com/Trusted-AI/AIF360)
  * The AI Fairness 360 toolkit is an extensible open-source library containing techniques developed by the research community to help detect and mitigate bias in machine learning models throughout the AI application lifecycle. AI Fairness 360 package is available in both Python and R.

2. [Fairlearn - by Microsoft](https://fairlearn.org)
   * Open source library for testing and evaluating bias and fairness in machine learning and AI models.
  
3. [Giskard - Open source testing library](https://www.giskard.ai/products/open-source)
   * [Giskard guide to evaluating for fairness and bias in ML models](https://www.giskard.ai/knowledge/guide-to-model-evaluation-eliminating-bias)
  
4. [Google Vertex AI Model Evaluation for Bias and Fairness](https://cloud.google.com/vertex-ai/docs/evaluation/intro-evaluation-fairness)

5. [SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
   * You can use Amazon SageMaker Clarify to understand fairness and model explainability and to explain and detect bias in your models.
   * The great thing about this tool is that you can configure a ageMaker Clarify processing job to compute bias metrics and feature attributions and generate reports for model explainability. SageMaker Clarify processing jobs are implemented using a specialized SageMaker Clarify container image.
  

6. [Arize AI - Bias and Fairness Metrics in Machine Learning](https://arize.com/blog/evaluating-model-fairness/#sensitive)

7. [Holistic AI - Bias and Fairness detection in AI](https://www.holisticai.com/use-case/ai-bias-assessment)

8. [Google's what-if tool](https://pair-code.github.io/what-if-tool/)

9. [Unveiling the Black Box: A Comprehensive Journey into Explainable AI](https://medium.com/epochiiits/unveiling-the-black-box-a-comprehensive-journey-into-explainable-ai-fd0bd017b70c)




# Language Translation Bias Metrics 
* While a "human-in-the-loop" is the best metric you can have, these are additional metrics/techniques that are useful for detecting bias in machine translation of one language to another.

1. Fairslator
   * This tool addresses language biases such as gender, addresses, etc.
   * [Fairslator homepage](https://www.fairslator.com/?machine=microsoft&srcLang=en&trgLang=fr&text=You%20work%20too%20much.)
   * [Fairslator tutorial-demos](https://rapidapi.com/lexiconista/api/fairslator/tutorials)
   * [Fairslator API via Rapid API](https://rapidapi.com/lexiconista/api/fairslator)

2. Bias Shield
   * This is an open-source tool for detecting and handling translation biases.
   * [Bias Shield Github](https://rapidapi.com/lexiconista/api/fairslator)
  

# Social Bias Detection
* This is a collection of social bias detection tools and datasets.

1. GUS Framework
   * [The GUS Framework: Benchmarking Social Bias Classification with Discriminative (Encoder-Only) and Generative (Decoder-Only) Language Models](https://arxiv.org/html/2410.08388v4)
   * [GUS-Net: Social Bias Classification in Text with Generalizations, Unfairness, and Stereotypes](https://huggingface.co/papers/2410.08388)
   * [GUS-Net Social Bias hugging face space](https://huggingface.co/collections/ethical-spectacle/gus-net-social-bias-ner-66edfe93801ea45d7a26a10f)
   * [social bias NER model on HF](https://huggingface.co/ethical-spectacle/social-bias-ner)

2. Building a Social Bias NER with BERT using synthetic data
   * This is an excellent blog post on hugging face that reviews how to build a social bias NER detection model using BERT and synthetic data.
   * [Link to blog](https://huggingface.co/blog/maximuspowers/bias-entity-recognition)
  
3. Hugging Face Evaluate Metrics
   * The hugging face evaluate library which we commonly use for evaluating common machine learning metrics such as accuracy, precision, recall, F1 score has tools to evaluate social bias.
   * [Link to Evaluate metrics](https://huggingface.co/blog/evaluating-llm-bias)
  
4. ROBBIE: Robust Bias Evaluation of Large Generative Language Models
   * This is an excellent framework that was developed my Meta AI.
   * [ROBBIE arxiv paper link](https://arxiv.org/abs/2311.18140)
   * [ROBBIE github](https://github.com/facebookresearch/ResponsibleNLP/tree/main/robbie)
   * [ROBBIE Meta AI blog](https://ai.meta.com/research/publications/robbie-robust-bias-evaluation-of-large-generative-language-models/)
