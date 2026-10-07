# Sagemaker Multi Class Text Classification
- This is an example project using sagemaker for multi-class text classification.

---
# Dataset
- The dataset used for this: https://archive.ics.uci.edu/dataset/359/news+aggregator

```
422937 news pages and divided up into:

152746 	news of business category
108465 	news of science and technology category
115920 	news of business category
 45615 	news of health category

2076 clusters of similar news for entertainment category
1789 clusters of similar news for science and technology category
2019 clusters of similar news for business category
1347 clusters of similar news for health category

```

---
## Dataset contents
- readme.txt
- 2pageSessions.csv
- newsCorpora.csv
  - use for training
  - load to S3 bucket
 
## Data Storage
- Could load file to elastic file system (local in sagemaker) ---but expensive and takes up memory
- Instead, will use S3 bucket.
- Create S3 bucket
  - name bucket
  - create training_folder
  - upload training data
  - S3 URI needed for loading file in sagemaker
 
---
# Compute Used
- `ml.t3.2xlarge` --> see [AWS pricing here](https://aws.amazon.com/sagemaker/ai/pricing/)


---
## Multi-class vs. Multi-label classification
- Multi-class classification assigns each input to **one and only one mutually exclusive class** from three or more choices
- Multi-label classification allows a single input to be **assigned multiple, non-exclusive labels simultaneously**

### Key Differences
- Number of Labels per Instance:
  - Multi-class: Exactly one label per input (e.g., classifying an image as a dog, cat, or bird).
	- Multi-label: Zero, one, or multiple labels per input (e.g., tagging a movie with action, comedy, and sci-fi at the same time)

### Class Mutually Exclusivity:
- Multi-class: Classes are mutually exclusive; choosing one means the item cannot be any other.
- Multi-label: Labels are independent or partially dependent; the presence of one label does not exclude another.

### Output Activation Functions
- Multi-class: Typically uses a Softmax activation function to output a probability distribution summing to 1 across all classes.
- Multi-label: Typically uses independent Sigmoid activation functions for each output node to treat each label as a separate binary decision (0 or 1).

### Evaluation Metrics:
- Multi-class: Evaluated using standard accuracy, precision, recall, and confusion matrices.
- Multi-label: Requires specialized metrics like Hamming loss, subset accuracy, or micro/macro F1-score to handle partial matches

---

## Use Cases for Multi-class classification
- Other use cases:
  - Sentiment analysis
  - Topic modeling/categorization (our use case above)
  - Intent detection (eg chatbot user intent)
  - Product categorization (eg assign products to categories)
  - Legal documents
  - Content recommendation (eg recommend books, products)
---
# Use Case for our model
- Our model will read a headline and then classify into 4 categories (e.g. sports, entertainment, health, science)



---
# Resources
- [Difference between multiclass classification and multilabel classification](https://medium.com/@abhishekjainindore24/difference-between-multiclass-classification-and-multilabel-classification-4e6d8967b5f7)
