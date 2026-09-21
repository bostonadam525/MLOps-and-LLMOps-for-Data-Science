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
## Random Forest Bagging
- Random Forests (RFS) use decision trees at each node --- where the best data split is obtained based on a random subset of features.
- Thus with a RF, we can consider ALL angles/opinions before coming to a final decision.

### Bootstrap Aggregation (Bagging)
- By injecting "randomness" we can create de-correlated or de-coupled classifiers.
- **When we combine them we can improve the overall generalization of the predictions.**
- Bagging can be applied to any CLASSIFIER:
  - Logistic Regression
  - Decision Trees --> Random Forests
---
# Random Forests - Global vs. Local Interpretation
- For a Decision Tree classifier, we measure **how often a feature is chosen** in the tree --> **we do this by measuring HOW LARGE the increase in purity is.**

## Global Intepretation of RFs
- To create RF models we extract random samples from the dataset --> train a decision tree model on this random sample --> then take the AVERAGE OF ALL TREES

## Local Interpretation of RFs
- This is the same process as used with Decision Trees.
- We simply follow the "path" that is taken down the tree at each node split decision process to understand the "local" intpretation and feature contribution importance.
- At the end of this we take the average of all trees given the local importance of the features. 

<img width="480" height="360" alt="image" src="https://github.com/user-attachments/assets/5a673193-5cde-4750-b4b6-c452a10219cc" />


---
# References
- [Bagging, Boosting and Stacking: Ensemble Learning in ML Models](https://www.analyticsvidhya.com/blog/2023/01/ensemble-learning-methods-bagging-boosting-and-stacking/)
- [NVIDIA - Random Forest](https://www.nvidia.com/en-us/glossary/random-forest/)
- [What is Bagging in Machine Learning?](https://www.analyticsvidhya.com/blog/2024/06/bagging-in-machine-learning/)
