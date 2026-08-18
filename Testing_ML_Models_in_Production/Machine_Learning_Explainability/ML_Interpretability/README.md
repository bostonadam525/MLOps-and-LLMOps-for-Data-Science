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
# IML methods
- allow us to extract info from ML models and explain outputs
- Two main groups:

1. Model Specific (during training)
- directly analyze model components or parameters

2. Model agnostic/post-hoc (after model training)
- study sensitivity to data input perturbation
- use surrogate approximations of the models

---
## Intrinsic Explainable Models
- Examples of these include:
1. Linear models (linear regression, logistic regression)
2. GAMS (Generalized additive models)
- https://christophm.github.io/interpretable-ml-book/extend-lm.html#gam
- Comparison of generalised additive models and neural networks in applications: A systematic review: https://arxiv.org/html/2510.24601v1
3. Decision Trees
4. Constrained GBMS
5. Rule-based models
6. KNNs

### Model Components Interpretation
- model parameters analysis help us understand what they predict and why. 
- These include:

1. Linear Models --> coefficients
2. Decision Trees --> splits, information gain
3. Rule based --> rules


## Sensitivity Methods 
- after train the model --> alter/manipulate input data and then critically analyze effect on model prediction
- Rule of thumb: Greater change in output --> more relevant the manipulation
- Most common Sensitivity methods/techniques include:

1. Permutation Feature Importance (PMI)
2. Partial Dependency Plots (PDPs)
3. Feature hiding
4. SHAP


## Surrogate Models
- This method attempts to predict a "black box" models predictions using a trained "intrinsically interpretable model"
- Examples: Linear models, Decision Trees
- Analyze results of surrogate models to attempt to better understand the black box models.
- How this works

1. Train black box model: X,y --> black box --> predictions
2. Train surrogate model: X, preds --> surrogate --> output

- Assumption: White box model represents the black box model, this is not always true though. 
- There is no true way to determine if the white box model represents the black box model on the same data and features. 


## MIXED Models
- LIME --> combines surrogate AND perturbation methods. 


----
# Global and Local Model Explainability
- NOTE: interpretability means the same as explainability


## Global explainability
- A global assessment of feature's contribution or importance to the outputs of an ML model
- Global means "AGGREGATED" feature contribution -- thus it considers a features contribution to the ENTIRE dataset. Classic example: Decision Trees
- Global interpretation answers questions:
1. Do features make sense for the specific domain?
2. Does feature ordering influence the outputs?
3. Increased vulnerability: is the model placing too much weight on specific feature(s) and this changes or biases the outputs?

### Statistical testing for Global interpretability
1. Correlation (linear and non-linear)
2. Regression

- We can use model parameters to understand the predictions:
1. Linear models --> coefficients
2. Decision trees --> splits, information gain (entropy)
3. Rule based --> Rules

### Post-hoc method for Global interpretability
- Permutation feature importance (PMI)
- Feature elimination (hiding, occlusion, explain)
- Partial dependency plots (PDP)
- Counterfactual explanations
- Surrogates

---
# Local explainability
- Focuses on which features impacted a specific prediction.
- Examples:
1. Why did the model predict a hospital re-admission given the input diagnosis?
2. Why was the insurance claim predicted as fraudulent?
3. Why did the CV model predict a dog and not a cat? 

## Model components for LOCAL interpretation
- Coefficients (linear models)
- Tree branches or rules navigation (e.g. Decision Trees, Random Forest)

## Post-hoc methods for LOCAL interpretation
1. Shapley
2. LIME
3. Accumulated local effects

## LOCAL to GLOBAL post-hoc methods
- We are able to aggregate local effects to obtain global interpretable explanations --> Shapley is the best algorithm for this
---
## Mapping Classical ML Interpretability Frameworks to Large Language Models (LLMs)
- The classical division of machine learning (ML) interpretability into intrinsic vs. extrinsic (post-hoc) and black-box vs. white-box systems directly maps to Large Language Models (LLMs).
- However, because LLMs manipulate vast embedding spaces instead of discrete tabular rows, the core unit of feature analysis shifts from variables to tokens, hidden layers, and circuits. [1, 2, 3] 
------------------------------
## 1. Intrinsic vs. Extrinsic (Post-Hoc) Frameworks in LLMs

## Intrinsic Explainability (White-Box Systems)
- In classical ML, intrinsic interpretability belongs to simple "white-box" algorithms (e.g., shallow Decision Trees or Linear Coefficients) where a human can directly read the mathematical weights to understand logic.

* The LLM Dilemma: No purely "intrinsic" LLMs exist. Looking at the raw weights of billions of dense parameters is completely uninterpretable to humans. [1] 
* The LLM Transition (Mechanistic Interpretability): To achieve internal understanding, researchers bypass raw parameters and look at internal representations. A prominent approach trained during or after optimization is the use of Sparse Autoencoders (SAEs). Pioneered by researchers at [Anthropic](https://transformer-circuits.pub/2024/scaling-monosemanticity/), SAEs reconstruct complex, overlapping internal activations into a highly sparse, expanded dictionary of human-understandable "concepts" or "features" (e.g., finding a sub-network circuit that exclusively fires when handling text about legal compliance). [4, 5, 6, 7] 

## Extrinsic / Post-Hoc Explainability (Black-Box & White-Box)
- Post-hoc methods analyze the system after training has concluded. In language systems, these split cleanly by access level: [2, 8] 

* Black-Box Extrinsic: The analyst has access only to prompt inputs and raw generated text tokens. Interpretability relies purely on text manipulation (perturbation) to test how changes alter output text probability. [2, 3]
 
* White-Box Extrinsic: The analyst leverages full access to the network architecture. After a token is generated, they calculate the gradient flow backwards through the attention layers to determine token attribution. [2, 8] 

------------------------------
## 2. Applicability of Classical ML Methods to LLMs
- Classical post-hoc methods can technically be adapted to LLMs, but they face acute structural limitations, as outlined in this summary of a comprehensive [survey on LLM explainability](https://dl.acm.org/doi/full/10.1145/3639372): [2] 

| Classical Method | Application to LLMs | Architectural Challenge / Limitation |
|---|---|---|
| LIME & SHAP | Local / Black-Box: Treat every token/word in the input prompt as a distinct feature. Randomly mask or drop tokens to see how output probability shifts. | Combinatorial Explosion: Running SHAP requires thousands of distinct forward passes per prompt. Scaled to autoregressive windows, it becomes computationally prohibitive. |
| Permutation Feature Importance (PFI) | Global / Black-Box: Shuffling or replacing broad token types (e.g., masking all proper nouns across an entire evaluation dataset) to observe accuracy degradation. | Syntax Destruction: Randomly shuffling text strings breaks grammar structures, pushing the model into unnatural out-of-distribution spaces that yield unreliable error metrics. |
| Partial Dependence Plots (PDP) | Not Viable: Classically measures the marginal effect of 1 or 2 isolated variables while holding all other features at an average baseline. | Non-Marginal Text Properties: Tokens cannot be isolated cleanly on a continuous axis while "holding the rest of the sentence constant" without altering semantics. |
| Surrogate Models | Local / Global / Black-Box: Training a white-box surrogate (like a shallow decision tree) on paired [LLM Prompt $\rightarrow$ LLM Target Output] sequences. | Loss of Contextual Nuance: Linear or simple rule-based models fail entirely to capture long-range contextual associations and complex syntactic patterns. |

------------------------------
## 3. The LLM Evolutionary Upgrade
- To bypass the costs and context-breaking failures of classical tabular tools, specialized interpretability protocols have emerged for deep language systems:

* Instead of SHAP/LIME $\rightarrow$ Gradient-Saliency (Integrated Gradients): White-box testing uses approaches like Integrated Gradients (IG) to compute continuous mathematical vectors from output tokens back to input embedding tensors. This yields precise, token-by-token local attribution instantly without running thousands of separate text mutations.
* Instead of Feature Selection $\rightarrow$ Attention Visualization: Engineers map internal attention matrices directly to identify exactly which previous words an attention head prioritized when picking the subsequent token.
* Instead of Global Surrogates $\rightarrow$ Linear Probing: Researchers freeze the layers of an LLM and train minimal linear classifiers against internal hidden state vectors. If the probe successfully categorizes an abstract trait (e.g., identifying factual truth vs falsehood), it mathematically confirms that the LLM's layer natively encoded that feature. [2, 8, 9, 10, 11] 

------------------------------
## References & Further Reading

* Christoph Molnar. (2020). [Interpretable Machine Learning: A Guide for Making Black Box Models Explainable](https://www.google.com/search?q=interpretable+machine+learning:+a+guide+for+making+black+box+models+explainable&kgmid=/g/11h80lspn2). [Interpretable Machine Learning Book](https://christophm.github.io/interpretable-ml-book/).
* Zhao, H., et al. (2024). Explainability for Large Language Models: A Survey. ACM Computing Surveys. ACM Digital Library.
* Bricken, T., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. Anthropic Transformer Circuits Research. Transformer Circuits Publication.
* Lin, Z., et al. (2025). A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models. arXiv preprint. [arXiv:2502.17516](https://arxiv.org/abs/2502.17516). [2, 4, 12] 

[1] [https://www.anthropic.com](https://www.anthropic.com/research/natural-language-autoencoders)
[2] [https://dl.acm.org](https://dl.acm.org/doi/full/10.1145/3639372)
[3] [https://mindfulmodeler.substack.com](https://mindfulmodeler.substack.com/p/the-practical-way-to-explain-llms)
[4] [https://transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
[5] [https://dl.acm.org](https://dl.acm.org/doi/10.1145/3787104)
[6] [https://openreview.net](https://openreview.net/forum?id=F76bwRSLeK)
[7] [https://arxiv.org](https://arxiv.org/html/2506.23845v1)
[8] [https://arxiv.org](https://arxiv.org/html/2504.00125v1)
[9] [https://ar5iv.labs.arxiv.org](https://ar5iv.labs.arxiv.org/html/2309.01029)
[10] [https://www.techrxiv.org](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177031352.23132160)
[11] [https://www.preprints.org](https://www.preprints.org/manuscript/202607.1441)
[12] [https://arxiv.org](https://arxiv.org/abs/2502.17516)


----


----
# BIG Challenges to ML model Interpretation
- This is even an issue with white box models (internal parameters available), these include but are not limited to:
1. INPUT DATA (e.g. correlation biases)
2. ML models (e.g. complexity, performance)
3. Human bias (e.g. data in and bias interpretations)

## Correlation
- correlation breaks the principle of independence which makes it more difficult to interpret features on their own. 
- Another problem:
  - Correlation effects coefficients in linear models and importance in decision trees are affected by correlation. 
  - So, if we remove or "perturb" a feature, a correlated feature takes its place in the model --> thus masking the full effect of removal/perturbation. 
- Methods that are effected by this:

1. Permutation feature importance
2. Feature elimination methods

## Bias in the Data
- The saying "garbage in == garbage out" applies here.
- If the training data for your models is not an adequate representation of the population or use case(s) your model will be used on, then we know the model outputs cannot be accurate or trusted. 

## Confirmation Bias
- **THIS IS VERY IMPORTANT**
- Humans are prone to this as we very often have a high bias towards a specific feature or features and thus select a specific model/post-hoc method that distorts and shows that bias. This could be due to domain/field expertise rather than relying on a data driven approach.  
  - An example of this might be that you choose a specific evaluation metric or technique or even modeling approach to amplify a feature that you have a bias towards. This is obviously non-scientific and why a scientific approach to evaluation and modeling should often included blinding and removing this bias. 

## Poor model performance
- If the data doesn't fit your model well at all --> the predictions will be meaningless and irrelevant. 


## Black Box Models
- Deep learning and LLMs are a good example of this. 
- These models are virtually impossible to scrutinize and interpret because we genuinely don't know whats going on under the hood. 
- However, using post-hoc methods to explain black box models can lead to misleading or flat out wrong interpretations because we genuinely don't know the inner workings of the model. 

## White Box models -- limitations?
- The trade-off here is to leverage ML models that can be simple enough to understand and interpret for technical and business stakeholders, yet needs to be complex enough to appropriately fit and model your data. 
- Examples:

1. Too many features --> model is hard to interpret/explain/make sense of

2. Highly complex models --> TOO MANY PARAMETERS --> very difficult to explain:
  - Deeper Decision trees (should prune them?)
  - Non-monotonic relationships
  - Feature interactions


## Rashomon Sets
1. There are multiple almost-equally accurate models
2. These models that are high performing are called a "Rashomon Set"
3. Definition of "Rashomon effect": multiple descriptions (models) of the SAME event
4. See this paper: https://arxiv.org/html/2407.04846v2
---
## Question: Are Rashomon Sets the same as Mixture of Experts?
- Simply put, No, a Mixture of Experts (MoE) is not the same as a Rashomon set. They describe entirely different concepts in machine learning: one is a single cooperative network architecture used for efficient computation, and the other is a statistical phenomenon where many separate, standalone models achieve similar predictive accuracy.

### Mixture of Experts (MoE)
- What it is: A single, large neural network architecture where specific layers are split into multiple smaller subnetworks ("experts") managed by a gating router.
- How it works: For every incoming piece of data or token, the router dynamically activates only a small subset of the experts to process that specific input collaboratively.
- Goal: Scale up model capacity and speed up training and inference by making the model sparse rather than running every parameter for every task.

### Rashomon Sets
- What it is: A collection of distinct, independent models from a model class that all score nearly identical, high predictive accuracy on a given dataset.
- How it works: Named after the film Rashomon (where different characters tell conflicting versions of the same event), it highlights that multiple different internal rules or reasoning paths can explain the same data equally well.
- Goal: A theoretical and practical tool used in explainable AI to choose simpler, fairer, or more interpretable models from a pool of equally accurate alternative

---
# Making models more interpretable

## Challenges to interpretability

### Data and Features
- if the training data is not transparent then how can the model(s) be transparent? To make the models more transparent we want to avoid overly complex feature engineering techniques such as use of autoencoders, PCA, polynomial combinations, and complex encodings.
	- Yes these techniques are interesting and sometimes genuinely useful, but in the end they do not help make the training data more transparent or even usable.
	- PCA is actually NOT an ideal feature selection algorithm. It is better as an unsupervised tool for understanding and exploring the data NOT for building the features for a training set. 

### Selecting Data and Features
- These should "make sense" for a given domain and use case(s).
- Avoid using features that introduce bias and discrimination.
- Make sure the data accurately represents the population and use case(s). 
- Monotonic features are KEY --> easier to understand
	- Monotonic features in machine learning refer to an input variable that has a consistent, unidirectional relationship with the target prediction. 
	- As the value of a monotonic feature goes up, the predicted output value will either exclusively go up (increasing) or exclusively go down (decreasing), without reversing direction.
	- Monotonically Increasing: As the feature value increases, the model's prediction also increases or stays flat.
	- Monotonically Decreasing: As the feature value increases, the model's prediction decreases or stays flat.


## Feature Selection
1. Simpler models are EASY to understand
	- use less features
	- remove noisy or non-relevant features
	- use: Lasso, Ridge, and other feature selection methods if possible. 
	- Other approaches include but are not limited to: Filter methods, Wrapper methods, and Tree-based embedded methods

### Feature Selection for RAG (Retrieval Augmented Generation)
- Feature selection in Retrieval-Augmented Generation (RAG) optimizes which metadata tags, text attributes, or retrieved context chunks are passed to the language model to maximize accuracy while minimizing token cost and latency.
- Core Selection Approaches include:

1. **Metadata Filtering:** Restrict vector searches using structured attributes (e.g., date, category, author) before executing semantic retrieval.
2. **Context Re-ranking:** Use cross-encoder models to score and select only the highest-relevance passages from an initial broad retrieval set.
3. **Diversity & Conflict Reduction:** Apply matrix-based subset selection (like Determinantal Point Processes) to remove redundant or conflicting chunks.
4. **Ablation & Attribution:** Measure downstream evaluation degradation when individual feature signals or context fields are removed.



## Methods
1. Intrinsically explainable models are most ideal when possible. 
2. Constraints are paramount to limit complexity
	- Monotonic constraints (in decision trees) --> more understandable to human interpretation, easier to troubleshoot and use in practice
3. Optimize for PERFORMANCE METRIC(s)/fit and model interpretability
	- however, be careful optimizing to 1 metric as it can and will overfit the model to that 1 condition. 


## Black Box Models
- Make sure to use more than 1 interpretable metrics or results if possible. 


---
# Resources and References
- [CVS Health - uqlm: Uncertainty Quantification for Language Models](https://github.com/cvs-health/uqlm)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/interpretability.html)
- [Stiglic et al, 2020. Interpretability of machine learning based prediction models in healthcare](https://arxiv.org/abs/2002.08596)
- [Rudin et al, 2024. Amazing Things Come From Having Many Good Models](https://arxiv.org/html/2407.04846v2)
- [Train in Data - ML model interpretability](https://github.com/trainindata/machine-learning-interpretability)
- [NLP based feature selection](https://www.emergentmind.com/topics/nlp-based-feature-engineering)
- [Elevating RAG from Novelty to Strategic Imperative](https://pub.towardsai.net/elevating-rag-from-novelty-to-strategic-imperative-e7010b3ef16f)
