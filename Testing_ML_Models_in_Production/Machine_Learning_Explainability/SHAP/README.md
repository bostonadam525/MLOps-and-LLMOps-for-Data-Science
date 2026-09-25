# Shapley Values and SHAP

## Overview
- SHAP (Shapley Additive exPlantions) is a game-theory approach used to explain the output of a machine learning model.
- SHAP uses adaptation of Shapley values.
- Shapley values are the unique solution to the best way of allocating a reward in cooperative game theory, given certain properties/assumptions/axioms.

---
## Motivation - Why the heck do we need SHAP?
- We have a black box model.
- We pass features to the black box --> model makes prediction
- Example:
```
Age=40
Income=10000
Profession=Lawyer

output --> life expectancy=92

```


- **Biggest question: How the heck did the features contribute to that prediction?**
- **SHAP is NOT a silver bullet method, its just yet another method to try and explain/interpret features in machine learning.**

## Feature Attribution
- Other methods we've seen to determine feature attribution include these seen below:

1. Effects in linear models --> coefficient x feature value
2. Effects in tree path --> additive change in output at each node
3. LIME --> weighted local linear model based on synthetic data

- **The 3 methods above are all ADDITIVE.**
  - This means we add contributions of each feature (aggregation) and then obtain value of prediction.

## **SHAP is ALSO ADDITIVE**
- SHAP will explain the contribution of each feature such as this:

```
Model output = baseline + attribution(feature) + attribution(feature2) + attribution(feature_n)

```

## Why choose an additive model?
- Additive models are SIMPLE --> they provide simple explanations.
- We humans are great at understanding additive models.
- SHAP has a unique solution based on GAME THEORY. 

---
## Cooperative Game Theory



---
# Resources/References
- [AI Explainability in 2026: Tools, Techniques, and Frameworks to Build Transparent AI Systems](https://futureagi.com/blog/ai-explainability-tools-techniques-2025/)



---
# Papers
- [AgentSHAP: Interpreting LLM Agent Tool Importance with Monte Carlo Shapley Value Estimation](https://arxiv.org/html/2512.12597v1)
- [From Features to Actions: Explainability in Traditional and Agentic AI Systems](https://arxiv.org/abs/2602.06841)
- [Understanding and Optimizing Agentic Workflows via Shapley value](https://arxiv.org/html/2502.00510v3)
