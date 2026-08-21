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
# What about using XGBoost to evaluate and rank your RAG retrieval engine in Gen AI?
- In this setup, XGBoost acts as a reranker or a learned evaluation metric that grades how well the retrieval system performs.
- This is how you can use it to evaluate and optimize RAG retrieval:

1. Approach: Learning to Rank
   - Instead of relying on a single metric like cosine similarity, XGBoost allows you to combine multiple retrieval signals into a single score.
   - You train the model on historical queries where you know the "ground truth" (which documents were actually helpful).

2. Features to Feed into XGBoost
- To evaluate retrieval, you convert the relationship between a query and a retrieved document into numerical features:
  - Lexical Scores: BM25, TF-IDF, or exact keyword match counts.
  - Semantic Scores: Cosine similarity from multiple different embedding models.
  - Contextual Features: Chunk length, position of the chunk in the original document, and document authority/recency.
  - Graph/Metadata Features: Number of shared tags or category matches.
  
3. How to Measure and Evaluate
   - Once trained, XGBoost outputs a probability or relevance score for each chunk.
   - You can evaluate your retrieval system using standard ranking metrics:
     - NDCG (Normalized Discounted Cumulative Gain): Measures if the most relevant chunks are successfully pushed to the very top.
     - Mean Reciprocal Rank (MRR): Evaluates how deep down the list the first truly helpful chunk appears.
     - Precision at K (P@K): Measures what percentage of the top K retrieved chunks are actually relevant.

4. The Benefits
   - Blends Sparse and Dense Search: It bridges the gap between keyword search (BM25) and vector search (embeddings) by learning exactly how much to trust each one.
   - Highly Interpretable: You can use XGBoost’s feature importance to see if your embedding model is actually contributing to good retrieval, or if simple keyword matching is doing all the heavy lifting.
   - Lightweight: It runs in milliseconds, making it fast enough to evaluate thousands of retrieved documents in real-time before passing them to the LLM.

## Limitations of using GBMs like XGBOOST for RAG evaluation
- While using XGBoost as a ranker or evaluator for RAG retrieval is highly effective, it introduces several distinct bottlenecks and architectural downsides.

1. High Data Collection Burden
   - Requires Ground Truth: You need a large, labeled training dataset of query-document pairs explicitly marked as relevant or irrelevant.
   - Expensive Labeling: Gathering these labels usually requires manual human annotation or using an expensive LLM (like GPT-4) as a judge to grade thousands of samples.

2. Information Loss via Manual Feature Engineering
   - No Raw Text Understanding: XGBoost cannot read the raw text of your query or document.
   - Relies on Proxies: It only looks at the numerical features you give it (e.g., BM25 scores, embedding similarities). If your embedding model fails to capture a nuance, XGBoost cannot fix it because it never sees the underlying words.

3. Increased Pipeline Complexity and Maintenance
   - Two-Stage Latency: You add an extra step to your pipeline. You must first fetch documents, compute all the numerical features, and then run the XGBoost inference before passing data to your LLM.
   - Data Drift: If your users start asking completely new types of questions, or if you update your underlying vector database embedding model, your XGBoost model will suffer from data drift and must be entirely retrained.

4. Cold Start Problem for New Content
   - Metadata Dependent: If XGBoost learns to heavily favor specific document metadata features (like "clicks," "author rank," or "recency"), newly added documents will naturally score poorly simply because they lack historical metadata, even if their text content is a perfect match.

5. Pointwise/Pairwise Limitations vs. Listwise Reality
   - Misses the Big Picture: Most standard XGBoost implementations evaluate chunks individually (pointwise) or in pairs.
   - Redundancy Blindness: It struggles to realize that Chunk B is useless if it contains the exact same information as Chunk A. It evaluates them in isolation, which can lead to filling your LLM context window with repetitive information.
  
---
## XGBoost forecasting

---
# References/Resources
- [sklearn docs](https://scikit-learn.org/stable/modules/ensemble.html)
- [Feature Importance in Gradient Boosting Trees with Cross-Validation Feature Selection](https://pmc.ncbi.nlm.nih.gov/articles/PMC9140774/)
- [XGBoost Feature Importance](https://zg104.github.io/ML/XGBoost.html#how-can-you-interpret-the-output-of-an-xgboost-model-in-terms-of-feature-importance)
- 
