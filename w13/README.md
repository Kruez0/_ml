# Light gbm

In this project, I once experimented with different classifiers to find the best one for my data. After testing multiple models, LightGBM gave me the highest accuracy and best overall performance, so I decided to use this instead of other classifiers

Here’s a quick summary of what I did:

1. Explored the dataset first — I printed out the data to understand its features and distribution.

2. Implemented 10-fold cross-validation — This helps make sure the model is tested thoroughly and the results are reliable across different splits of the data.

3. Handled class imbalance with SMOTE — Since the dataset had uneven classes, I used SMOTE to oversample the minority class and prevent the model from being biased.

4. Trained the model using LightGBM — I trained and evaluated the LightGBM classifier on each fold and reported the performance.

This approach gave me a robust and accurate classification model that I’m confident in.