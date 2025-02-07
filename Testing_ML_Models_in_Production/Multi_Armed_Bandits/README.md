# Multi Armed Bandits Testing
* MAB heavily depends on two concepts: `exploration` and exploitation.` 

1. Exploration
   * This is a concept where the model explores the statistically significant results, as what is commonly seen in A/B testing.
   * The prime focus of A/B testing is to find or discover conversion rates of the two models.
   * A better way to define this is "randomness" or the probability. 

2. Exploitation
   * This is a concept where the algorithm uses a greedy approach to maximize conversion rates using the information it gained during exploring.
   * This would be 1 - probability or exploitation.
   * The goal with exploitation is to maximize the reward. 

* MAB is very flexible compared to the classical A/B testing. It can work with more than two ML models at the same time, which can increase the rate of conversion. The algorithm continuously logs the KPI score of each model based on the success with respect to the route from which the request was made. This allows the algorithm to update its score of which is best.  




# References
1. [Exploring Multi-Armed Bandit Problem: Epsilon-Greedy, Epsilon-Decreasing, UCB, and Thompson Sampling](https://medium.com/@ym1942/exploring-multi-armed-bandit-problem-epsilon-greedy-epsilon-decreasing-ucb-and-thompson-02ad0ec272ee)
2. [Model Deployment Strategies](https://neptune.ai/blog/model-deployment-strategies)
3. [Statistical Hypothesis Testing](https://medium.com/towards-data-science/statistical-hypothesis-testing-with-python-6a2f38c12486)
