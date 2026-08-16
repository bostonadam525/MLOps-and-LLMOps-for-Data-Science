# Machine Learning Interpretability


## What is interpretability in Machine Learning?
- what the model has learned and the reasons for the outputs
- examples:
1. Reject customer for loan --> why? (e.g. debt)
2. Insurance premiums high or low --> why? (features)
3. Clinical/Medical - diagnose disease --> why? (features)

---
## Important takeaway
- ML models are used to predict things -- this could be predict quarterly profits, forecast things, and yes in today's world this applies to Gen AI predictions.
- However, the models "interpretations" are what we can use to understand knowledge, characteristics, and features that drive specific predictions in the domain the model is trained on. 

## Why do we want to understand ML model outputs?
- We need to know regardless of the domain or industry or use case, is the model discriminatory? is it biased? is it fair? 
- Is the model making things up? (e.g. hallucinating or fabrications)


### There are Applications in MANY fields
- medicine
- finance and banking
- science
- legal
- and more...
- Thus, **Auditing ML models is paramount to ethical machine learning!!**
---
## Why is interpretability so IMPORTANT?
- Interpretable ML models -- this is important to extract knowledge from relationships in the data it is trained on.
- Interpretable ML models follow domain specific sets of rules to allow predictions to be comprehended and understood by the users of the model (e.g. humans)
- As we know, TRUST in AI/ML is a big factor and even bigger today given the advent of LLMs being used for everything. 
- **Interpretability is paramount because:**

1. Allows us to learn more about the data -- data and features to train a model on, the outputs, the evaluations, and the entire data flywheel that drives ML training and use. 
2. Gives us detailed insights into biases and "how fair" the model is to specific use cases, domains, knowledge, customers, groups, cultures and more. This helps us answer the question: "is the model ethical and following domain specific regulations?" 
3. Model performance improvements --> to improve a model you need to remove noisy data, noisy features, and more. This helps avoid overfitting the model but also helps avoid model drift and degradation over time. In the age of LLMs this includes hallucinations and fabrications that can be harmful.


## So what are the Consequences of poor ML model interpretability?
- model biases exist for black box vs. white box models -- this includes classical ML, Generative AI/LLMs and Agents to name a few. 
- ethnic, domain, and cultural biases ML models are trained on -- this is very common and crucial to understand
- models that are trained to optimize to a specific metric can and will bias a model preventing it from generalizing on unseen data better seen with other metrics. This can have catastrophic outcomes if most domains if the model is predicting things it shouldn't. 

### Algorithmic consequences
- Remember --> Algorithms scale and thus their biases and errors scale with them. 
 

## So What happens if you don't audit an ML model for interpretability?
- If you don't know what drives your ML model outputs and why, this will make your model more vulnerable to:

1. Failure in production (real-world deployments)
2. Attacks and injections (people can attack or inject and manipulate your model to do bad things)
3. Model drift
4. Model overfitting
5. Data contamination -- if you use garbage model outputs to re-train the model this cycle will continue. 

### Summary -- why ML Interpretability is SO IMPORTANT
1. Helps to improve knowledge of model inner workings and the domain data the model is trained on, produces, and is evaluated.
2. Helps us improve model performance over time
3. Prevent model biases, hallucinations, fabrications
4. Laws, regulations, and rules that apply to specific domains are paramount in machine learning -- if we don't know if the model is following these it is a BIG PROBLEM
5. Guardrails and Security -- we want to prevent a model from predicting unwanted or undesired outputs 
6. Regardless of the domain or focus of the model, you want to prevent "attacks" where users can make your model do things it should not, and prevent your company from losing money and customers over time and even worse prevent catastrophic errors. 

---






---
# Resources and References
- [CVS Health - uqlm: Uncertainty Quantification for Language Models](https://github.com/cvs-health/uqlm)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/interpretability.html)
- [Stiglic et al, 2020. Interpretability of machine learning based prediction models in healthcare](https://arxiv.org/abs/2002.08596)
