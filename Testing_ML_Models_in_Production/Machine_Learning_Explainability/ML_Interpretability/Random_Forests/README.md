# Random Forests
- RFs fall into **ensemble learning**.

---
# Ensembles - Bagging
- As a review, we should remember that ensemble modeling is:
  - **Different partitions of data**
  - Train multiple classifiers/algorithms on each partition -->
  - Obtain predictions -->
  - Aggregate them into a single prediction or outcome
- **You can use any type of classifier here such as:** Decision Tree, Logistic Regression, SVM, and more.

---
# Ensembles - Boosting
- Boosting is quite different from bagging, it works as follows:
  - **Same dataset is used for all models/algorithms.** -->
  - Train multiple classifiers/algorithms -->
  - Obtain predictions -->
  - **Assign weights to predictions** -->
  - Aggregate predictions -->
  - **Final prediction***
---
## Ensemble Models - Summary
- The important thing about ensemble models is that you can explain each individual model.
- This allows you to understand how these models are aggregated/combined to obtain a final prediction.
- **This makes these models very explainable and interpretable and gives full transparency into the ensembles.**
---
# Ensemble Learning - Overview
- **Goal**: model performance improvement!
- **Concept:** several classifiers are combined so that their combination/aggregation will outperform every individual model or component.
- **How do we do this?:** Data used to build several classifiers --> decisions/outputs are aggregated/combined to 1 output/prediction.
- **Example:**
  - A new unseen prediction is obtained by sending it to the aggregate of classifiers and then the predictions of all the models are pooled to get the final prediction.

---
## Inspiration for Ensemble Learning
- Human behavior is what drives this method!
- When making a decision, we very often ask several experts before deciding on the best option.

## Why combine classifiers?
- The goal is to improve the ability of classification models to generalize on unseen data from training.
- Classifier models have known errors --> thus, if we train multiple versions of these models we will have a variety of errors/misclassified examples
- The resulting models "complement" one another's weaknesses to make the best predictions(s) possible.

## How do we build a variety of classifiers that are different from each other?
- To do this we implement different model training procedures:
- This is where **Bagging** and **Boosting** are most useful. They make different errors and thus give us different outcomes.
- **Bagging example:** Random Forests
- **Boosting:** AdaBoost, GBMs (e.g. XGboost)

---
# What is Bagging?!
- Bagging simply defined is **Bootstrap Aggregating**. The process here is as follows:
  - Create different datasets by bootstrapping replacements with original data.
  - Train classifier model on each bootstrap sample.
  - Combine predictions --> average or majority voting


<img width="1050" height="520" alt="image" src="https://github.com/user-attachments/assets/cc4f56b2-f7d1-4844-82c0-1a9a37ae6ee6" />
- [Source](https://www.analyticsvidhya.com/blog/2023/01/ensemble-learning-methods-bagging-boosting-and-stacking/)

---
# References
- [Bagging, Boosting and Stacking: Ensemble Learning in ML Models](https://www.analyticsvidhya.com/blog/2023/01/ensemble-learning-methods-bagging-boosting-and-stacking/)
- [What is Bagging in Machine Learning?](https://www.analyticsvidhya.com/blog/2024/06/bagging-in-machine-learning/)
