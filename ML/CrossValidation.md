# Cross Validation
The number of data for traing should be between 70-80% of the total historical data. 
If we have less data, perhaps you should use more data (up to 90%) for training.

## purpose
- evaluate how well a model will perform on unseen data, helping to detect and prevent overfitting
- used to select the model parameters with the best score in hyperparameter tuning
- ts-cross-val: efficiently use all training data to get the best performance evaluation
  
## sliding window 
The total training and test data points are the same but move to the future.

## expanding window
The training window expands while the test window slides.
