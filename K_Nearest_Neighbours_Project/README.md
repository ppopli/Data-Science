# K Nearest Neighbors with Python

We've been given a classified data set from a company! They've hidden the feature column names but have given you the data and the target classes. 
We'll try to use KNN to create a model that directly predicts a class for a new data point based off of the features.


## Evaluation

**Classification Report**
             
			 precision    recall  f1-score   support

          0       0.84      0.82      0.83       152
          1       0.82      0.84      0.83       148
	avg / total       0.83      0.83      0.83       300

**Confusion Matrix**
[[125  27]
 [ 24 124]]

       
**Looking at the classification report, our model has an accuracy of 83%**