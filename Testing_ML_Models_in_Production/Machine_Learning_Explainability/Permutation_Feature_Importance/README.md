# Permutation Feature Importance (PFI)
- It has the following characteristics:

1. Post-hoc interpretability method: used AFTER we train an ML model.

2. Global interpretation method: determines the feature importance on avg for given dataset.

3. MODEL AGNOSTIC: especially for opaque estimators:
- This means we can use it for BOTH white box and black box models!


## What is Permutation Feature Importance Used for?
1. Model inspection technique
  - Explains how a model makes decisions on which feature(s) contribute to the final prediction outputs.

2. Feature selection technique
  - Can select features with higher importance.


## What is the Importance Value?
- To determine this we RANDOMLY shuffle the features in a model (this is expected to decrease model performance).
- Shuffling will ultimately break the relationship between a feature and the TARGET variable.
- We can use basically ANY performance metric for this. 
	- Classification: AUC/ROC
	- Regression: MSE (mean squared error)



### Importance Value Calculation

```
Importance = Model performance - performance after shuffling feature(s)
```
- KEY POINT: The HIGHER the drop in performance of the model after shuffling a specific feature, the more important that feature is. 


## Important Points
- Bad ML Model --> feature may show low importance
- Good ML Model --> feature may show HIGH importance

- Thus the model performance is important to check first, if its a BAD model to begin with, calculating the permutation feature importance is not going to actually give you any valuable information.

- So, PFI is relative to the model performance to begin with. 

- PFI does NOT reflect the INTRINSIC predictive value of a particular feature or features


## PFI Mechanisms
- This is the main overview of how PFI works:

Train set --> ML model (intrinsically explainable or a black box model)


Test set --> ML model --> FULL model performance 

Next, we apply PFI:
- Step 1: shuffle 1 of features in test set
  - shuffle test set --> ML model --> DROP in ML model performance (if important it will drop from original raw test set performance)
  - Drop in performance is the PFI measurement


- Step 2: shuffle a 2nd feature in test set
  - shuffle test set --> ML model --> measure drop in performance
  - Drop is performance is the PFI measurement

- We do this again and again. 


### Drop in performance
- The higher performance drop is the best performing feature(s).
- There is an element of randomness that will contribute to PFI value. 


## Randomness in PFI
- As mentioned above, PFI is the measure of the DROP in performance when a feature is randomly shuffled. 
- Randomness or random seeds will return different values.
- To account for the randomness we can and should consider the following:
  - Shuffle features multiple times and take the average and if possible the standard deviation.
  - There are multiple libraries/modules in Python we can use for this:
   

1. Shuffle THE SAME feature multiple times, then take the average:
  - SKLEARN
  - Eli5

2. Importance with Cross-Validation
  - Feature-engine (allows feature selection out of the box) --> takes portion of train set and then evaluates model on held out samples


---
# Resources
- [Explainable AI: Demystifying the Black Box Models](https://www.analyticsvidhya.com/blog/2023/10/explainable-ai-demystifying-the-black-box-models/)
- [Permutation feature importance](https://christophm.github.io/interpretable-ml-book/feature-importance.html)
