# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:56:58 2017

@author: Pulkit
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def load_data(filename) :
    ''' returns the data frame to work with '''
    
    return pd.read_table(filename, sep=',')


def get_features_and_label(df) :
    ''' returns the features data frame and label '''
    
    return df[df.columns[:-1]],df[df.columns[-1]]

def check_missing_values(df) :
    ''' returns true if there are missing values else returns false'''
    sns.heatmap(df.isnull(),yticklabels=False,cbar = False, cmap='viridis')
    return df.isnull().sum().sum() != 0


def standardize_features(features):
    ''' returns standardised features data frame '''
    
    from sklearn.preprocessing import StandardScaler
    
    scaler = StandardScaler()
    scaler.fit(features)
    return pd.DataFrame(scaler.transform(features),columns=features.columns)


def get_train_test_data(features, labels) :
    ''' returns the training and test data for features and labels
        30% of data is will be used for testing the model'''
        
    from sklearn.model_selection import train_test_split
    
    return  train_test_split(features, labels, test_size=0.30, random_state=101)




def KNNModel(X_train, Y_train) :
    ''' returns a KNN model '''
    
    from sklearn.neighbors import KNeighborsClassifier
    K_value = np.sqrt(X_train.shape[0])
    print('K_value = ' + str(K_value))
    
    knn = KNeighborsClassifier(n_neighbors=K_value)
    return knn.fit(X_train, Y_train)
    
    

def predict_value(model, X_test) :
    '''  returns the prediction '''
    
    return model.predict(X_test)
    

def get_classification_report(Y_test, predicted_values) :
    ''' returns classification report for the model '''
    from sklearn.metrics import classification_report
    
    return classification_report(Y_test, predicted_values)


def get_confusion_matrix(Y_test, predicted_values) :
    ''' returns confusion matrix '''
    
    from sklearn.metrics import confusion_matrix
    
    return confusion_matrix(Y_test, predicted_values) 


if __name__ == '__main__' :
    
    filename = 'KNN_Project_Data'
    
    df = load_data(filename)
    print(check_missing_values(df))
    features,label = get_features_and_label(df)
    scaled_features = standardize_features(features)
    
    X_train, X_test, Y_train, Y_test = get_train_test_data(scaled_features,label)
    knn_model = KNNModel(X_train, Y_train)
    predicted_values = predict_value(knn_model,X_test)
    
    classification_report = get_classification_report(Y_test, predicted_values)
    confusion_matrix = get_confusion_matrix(Y_test, predicted_values)
    
    print(classification_report)
    print(confusion_matrix)
    

''' Classification Report 
             precision    recall  f1-score   support

          0       0.84      0.82      0.83       152
          1       0.82      0.84      0.83       148
avg / total       0.83      0.83      0.83       300


'''

''' Confusion Matrix 

[[125  27]
 [ 24 124]]

'''
    