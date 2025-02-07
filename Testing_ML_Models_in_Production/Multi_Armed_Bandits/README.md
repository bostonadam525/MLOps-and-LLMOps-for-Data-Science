# Multi Armed Bandits Testing
* MAB heavily depends on two concepts: `exploration` and `exploitation`.

1. Exploration
   * This is a concept where the model explores the statistically significant results, as what is commonly seen in A/B testing.
   * The prime focus of A/B testing is to find or discover conversion rates of the two models.
   * A better way to define this is "randomness" or the probability. 

2. Exploitation
   * This is a concept where the algorithm uses a greedy approach to maximize conversion rates using the information it gained during exploring.
   * This would be 1 - probability or exploitation.
   * The goal with exploitation is to maximize the reward. 

* MAB is very flexible compared to the classical A/B testing. It can work with more than two ML models at the same time, which can increase the rate of conversion. The algorithm continuously logs the KPI score of each model based on the success with respect to the route from which the request was made. This allows the algorithm to update its score of which is best.

# A/B Testing vs. MAB Testing

## A/B Testing
1. Fixed allocation
   * Population is split into equal groups (A, B, C, etc.), with each group seeing a different product or content variant. The allocation to each group stays fixed throughout the experiment.

2. Statistical significance
   * A/B testing uses a set sample size and duration.
   * Statistical methods are then used to see if there’s a significant difference in performance metrics (like conversion rates) between variants.

3. Exploitation over exploration
  * A/B testing mainly concentrates on finding the best-performing option based on predetermined criteria.
  * It doesn’t emphasize exploring new options, instead exploiting the known variants.

4. Suitable for stable environments
   * A/B testing works well in stable situations where user preferences or other factors aren’t expected to change rapidly during the experiment.
  

## MAB Testing
1. Dynamic allocation
   * Site or application traffic is allocated in real-time based on how well each option performs.
   * Successful options get more traffic while underperforming ones receive less.

2. Continuous optimization
   * Multi-armed bandits constantly adjust resource allocation, enabling ongoing exploration and exploitation.
   * This means they adapt in real time.

3. Balanced exploration and exploitation
   * These systems balance exploring new options to gather data and exploiting known working options by allocating more traffic to them.

4. Suitable for dynamic environments
   * Multi-armed bandits are suitable for changing situations where conditions can shift. They are adaptive and respond effectively to dynamic changes.

# Variants of Multi-Armed Bandits
1. Semi-Uniform
   * All of these are considered "greedy" where the best option based on previous observations is always chosen when a unform random action is taken.
   * The algorithms include:
     ```
     1. Epsilon-Greedy
     2. Epsilon-First
     3. Epsilon-Decreasing (Decay)
     4. Adaptive Epsilon-greedy (Value differences or VDBE)
     5. Adaptive Epsilon-greedy (Bayesian Ensembles or Epsilon-BMC)
     6. Probability Matching (Thompson Sampling or Bayesian Bandits)
     7. Pricing Strategies


     ```

2. Contextual Bandit
   * Generalization of the multi-armed bandit is known as the `contextual multi-armed bandit`.
   * At each iteration an agent still has to choose between arms, but they also see a d-dimensional feature vector, the context vector they can use together with the rewards of the arms played in the past to make the choice of the arm to play.
   * Over time, the learner's aim is to collect enough information about how the context vectors and rewards relate to each other, so that it can predict the next best arm to play by looking at the feature vectors
   * Types of contextual bandits
  ```
    Online Linear Bandits
    1. LinUCB (Upper Confidence Bound)
    2. LinRel (Linear Associative Reinforcement Learning)

    Online non-linear Bandits
    1. UCBogram algorithm
    2. Generalized linear algorithms
    3. KernelUCB algorithm
    4. Bandit Forest algorithm
    5. Oracle-based algorithm

    Constrained contextual bandit
    1. UCB-ALP algorithm

  ```
3. Adversarial Bandit
   * At each iteration, an agent chooses an arm and an adversary simultaneously chooses the payoff structure for each arm.
   * This is one of the strongest generalizations of the bandit problem as it removes all assumptions of the distribution and a solution to the adversarial bandit problem is a generalized solution to the more specific bandit problems.
4. Infinite Armed Bandit
5. Non-Stationary Bandit
6. Dueling Bandits
7. Collaborative Bandit
8. Combinatorial Multiarmed Bandit

# References
1. [Exploring Multi-Armed Bandit Problem: Epsilon-Greedy, Epsilon-Decreasing, UCB, and Thompson Sampling](https://medium.com/@ym1942/exploring-multi-armed-bandit-problem-epsilon-greedy-epsilon-decreasing-ucb-and-thompson-02ad0ec272ee)
2. [Model Deployment Strategies](https://neptune.ai/blog/model-deployment-strategies)
3. [Multi-Armed Bandits](https://gibberblot.github.io/rl-notes/single-agent/multi-armed-bandits.html)
4. [Multi-Armed Bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit)
5. [Statistical Hypothesis Testing](https://medium.com/towards-data-science/statistical-hypothesis-testing-with-python-6a2f38c12486)
