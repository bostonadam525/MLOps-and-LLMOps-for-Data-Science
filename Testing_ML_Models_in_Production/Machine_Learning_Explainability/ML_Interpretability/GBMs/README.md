# GBMs - Gradient Boosting Machines/Ensembles
- GBMS are a sequence of models created by penalizing harder the errors made by the previous model. 



## Bagging vs. Boosting

<img width="496" height="254" alt="image" src="https://github.com/user-attachments/assets/93c6ae2b-c203-4d4d-952e-51855d1211a0" />

[image source](https://lewtun.github.io/hepml/lesson04_intro-to-gradient-boosting/)


### Bagging - bootstrap aggregating
- classifiers built in parallel to one another
- classifiers trained on data subsamples
- every classifier has a similar weight in making the final prediction --> end result is an ensemble classifier

### Boosting
- Differences from bagging
	- classifiers are built in sequence
	- classifiers trained on ENTIRE DATA SET
	- weighted observations introduce diversity (e.g. how difficult to classify)
	- Result: each classifier has a DIFFERENT WEIGHT in the final predictions based on their accuracy


#### Boosting - Training process
1. First classifier --> all observations given same weight, trained on all data
2. Second classifier --> observations misclassified/errored in step 1 --> given higher weight
3. Weights are adjusted in each additional iteration for each new classifier
4. Weights are also assigned based on each classifier accuracy and that assigned weight contributes to the model's overall predictions


### Gradient Boosting Machines
- AdaBoost
- Generative additive models (GBMS)
	- at each new iteration (new classifier/regressor), we minimize the difference between the predictions and the residuals of the previous classifier
	- residuals are bigger in situations where previous model was more wrong


 <img width="1536" height="864" alt="image" src="https://github.com/user-attachments/assets/c155f150-4c34-42a6-b9dd-d6baf7a5e158" />

 [image source](https://www.superdatascience.com/podcast/sds-771-gradient-boosting-xgboost-lightgbm-and-catboost-with-kirill-eremenko)



# Gradient Boosting Machines (GBM) -- Global Explainability
- In this case, global explanation == feature importance
- Feature importance quantified, two things are necessary:
	- metric to quantify the gain at each split
	- method/technique to calculate feature gain across all trees in ensemble


## Gain Metric
- Equation:

```
Gain = w x Hparent - (w x Hleft + w x Hright) 

```
- "H" is the measure of impurity --> idea is that the parent node is most impure --> the more we iterate the purer the models should be
- This example would be for a decision tree with 2 splits or paths. 


### sklearn
- GBMs are regression trees.
- We fit to residuals of former or previous trees. 
- We optimize for (quantify impurity) using these metrics in sklearn:
	- Sum of squares
	- Friedman mse

### XGBoost
- This allows us to measure:
	- **Gain - impurity decrease**: mean gain (squared error) which leverages all splits that use the feature. Can also use the TOTAL GAIN for a feature. 
	- **Weight - split count** -- number of times a feature is selected for split in a tree. 
	- **Cover** -- mean num of observations that a node splits --> this is across ALL SPLITS that use a feature. This can also be the TOTAL NUMBER of observations split across ALL NODES that use a feature.


### LightGBM
- This allows us to measure:
	- **Gain -- impurity decrease**: total gain (squared error) which takes ALL SPLITS that use the feature. 
	- **Split** -- number of times that a feature was selected for splits in a tree. 


## GBM Feature Importance
- we must consider ALL trees as if they were all 1 massive tree together (ensemble of trees as 1 big tree). 


---
# References/Resources
- [sklearn docs](https://scikit-learn.org/stable/modules/ensemble.html)
- [Feature Importance in Gradient Boosting Trees with Cross-Validation Feature Selection](https://pmc.ncbi.nlm.nih.gov/articles/PMC9140774/)
