# LIME 

---
## LIME - motivation
- Surrogates for explainability: a surrogate is an intrinsically explainable ML model trained to predict the predictions of a black box model.
- The basic purpose: to understand how the black box makes the predictions.

## Surrogate model limitations
- Black box models have COMPLEX separation boundaries
- White box models have SIMPLE separation boundaries
- This makes it more difficult for a white box model to approximate a black box model through its entire feature space.  


## Motivation for LIME -- Train LOCAL Surrogate Model
- Idea is that separation boundaries in the proximity of a data point are less complex than those for the entire dataset. 
- HOWEVER, this is NOT actually what LIME is all about.
- LIME meaning:
	- Local
	- Interpretable
	- Model-agnostic
	- Explanations 

## So what is LIME? 
- Concept: train a surrogate model to the proximity of the data point or feature(s) that we want to explain in order to model (and interpret) the predictions of a black box model. 
- For multiple data or feature points --> train MULTIPLE surrogate models!


## How does LIME work?
- We know that the purpose of LIME is to better understand how a black box ML model makes certain predictions.
- The idea is NOT to understand EVERY data or feature point, but rather to "poke" the model in certain data points --> examine the output --> try to understand why and how --> repeat
- Main mechanism:
	- Identify specific data or feature points in the model (e.g. neural network)
	- Train a surrogate model to mimic the model at that point in time or at those parameters that produced that output. 
	- LIME uses synthetic data to mimic this process using local surrogates. 


### LIME - Full Mechanism
1. Choose data point, feature or observation we want to explain.
2. Generate synthetic data in proximity. 
3. Obtain black box predictions for data from step 2. 
4. Obtain distance between synthetic data and original data point. 
5. Train white box model perturbed data from step 2 to predict black box predictions in step 3, weighted by locality in step 4.
6. Interpret white box model. 

- This is the process spelled out:

```
Synthetic data + Black Box prediction + Surrogate = Local explanations

```

### LIME - what does "close" look like?
- The further away from the data point to explain, the less accurate the local model may be. 
- LIME will Weight contributions based on distance to the data point. 


### Important questions for LIME
1. How do we generate synthetic data for LIME? 
2. Which explainable model should we use? 
3. Distance calculations -- how do we get these? 




