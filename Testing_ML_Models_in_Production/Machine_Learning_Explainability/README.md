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
