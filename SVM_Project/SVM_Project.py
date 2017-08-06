# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:15:56 2017

@author: Pulkit
"""

import seaborn as sns


def load_data() :
    ''' this function is problem specific 
        for this example this would return
        dataset from seaborn '''
        
    return sns.load_dataset('iris')
    

def get_features_and_label(df) :
    ''' returns the features data frame and label '''
    
    return df[df.columns[:-1]],df[df.columns[-1]]


def check_missing_values(df) :
    ''' returns true if there are missing values else returns false'''
    sns.heatmap(df.isnull(),yticklabels=False,cbar = False, cmap='viridis')
    return df.isnull().sum().sum() != 0


def get_train_test_data(features, labels) :
    ''' returns the training and test data for features and labels
        30% of data is will be used for testing the model'''
        
    from sklearn.model_selection import train_test_split
    
    return  train_test_split(features, labels, test_size=0.30)


def SVMModel(X_train, Y_train, grid_search = False) :
    ''' returns a SVM Classifier (SVC Model) 
        return a model after doing grid search to fit 
        the model with best values of gamma and c 
        if grid_search set to true else uses default values'''
    from sklearn.svm import SVC
    
    if(grid_search == False):
        return SVC(kernel='linear').fit(X_train, Y_train)
    
    param_grid = {'C': [0.1,1, 10, 100, 1000],
                  'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}
    
    from sklearn.model_selection import GridSearchCV
    return GridSearchCV(SVC(kernel='linear'),param_grid,refit=True,verbose=3).fit(X_train,Y_train)



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
    


if __name__ == '__main__':
    df = load_data()
    print(check_missing_values(df))
    features, label = get_features_and_label(df)
    X_train, X_test, Y_train, Y_test = get_train_test_data(features,label)
    SVM_model = SVMModel(X_train,Y_train,True)
    
    # comment the below line if not using the third parameter of SVMModel func
    print("Best Values  C = {one} and Gamma = {two}".format(one=
          SVM_model.best_params_['C'], two = SVM_model.best_params_['gamma']))
    predicted_values = predict_value(SVM_model,X_test)
    classification_report = get_classification_report(Y_test, predicted_values)
    confusion_matrix = get_confusion_matrix(Y_test, predicted_values)
    
    print(classification_report)
    print(confusion_matrix)
    
    
''' Classification Report
             precision    recall  f1-score   support

     setosa       1.00      1.00      1.00        17
 versicolor       1.00      1.00      1.00        13
  virginica       1.00      1.00      1.00        15

avg / total       1.00      1.00      1.00        45


 '''
 
 
''' Confusion Matrix 
[[17  0  0]
 [ 0 13  0]
 [ 0  0 15]]

'''
