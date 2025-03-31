# Data Validation in Machine Learning Pipelines
* These are notes, experiments, and techniques from the open-source course by Weights & Biases on Data Validation for ML pipelines.


# Most Common Scenario: Pre-Production
1. Developer writes code in a notebook or a script.
2. Notebook script usually does:
   * loads features
   * train-test splits
   * trains model(s) on train dataset
   * evaluates model(s) on test set
  
3. Deploy model to production!

# Most Common Scenario: Post-Deployment
* This is where things often change quite a bit.

1. You may have to rewrite or refactor your code logic to work in an ML pipeline
2. You may have to change the libraries, hardware, etc. to deploy the  model(s)
3. **Serving pipeline data != training pipeline data**


# ML Pipelines (common setup)
* Source: Weights & Biases Data Validation in ML pipelines
* The pipeline below is typical for ML pipelines. The end result is the Model outputs a result to the user.

![image](https://github.com/user-attachments/assets/e49f6352-9e13-4886-add5-3d43155c4eb7)


# Data Drift through Retraining
* **Drift is a change in the distribution of the data over time while in production.**
* While your model(s) might do very well on the train set and the test set in the pre-productio environment, the real-world production environment changes constantly.
* How do we deal with this? 
  * Some drift is **natural and expected**! This may include factors such as:
      1) Time
      2) Seasonality
      3) Geographic
      4) User Behavior
   
## Simple Solultion to Drift?
* Frequently Retrain the models in your ML pipelines usually through schedueld orchestration (e.g. daily, weekly, monthly).
