# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:28:56 2017

@author: Pulkit
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(filename) :
    ''' loads data from the specfied files and returns a data frame'''
    
    df = pd.read_csv(filename)
    print(df.head())
    return df
    

def get_features_and_label(df, features, label) :
    
    ''' returns features and label subsets from data frame '''
    
    X = df[features]
    y   = df[label]     
    
    return X, y
    
def check_missing_values(df) :
    
    ''' returns a data frame containg true for missing values
        also plots the heatmap of null values to visualize if there
        are null values or not '''
    
    plt.figure()
    sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    plt.savefig('Missing Values.png', bbox_inches='tight')
    
    return df.isnull()

def get_train_test_data(features, labels) :
    
    ''' returns the training and test data for features and labels
        30% of data is will be used for testing the model'''
        
    from sklearn.model_selection import train_test_split
    
    return  train_test_split(features, labels, test_size=0.30, random_state=101)


def fit_logistic_regression_model(X_train, Y_train) :
    ''' returns a logistic regression model '''
    
    from sklearn.linear_model import LogisticRegression
    
    return LogisticRegression().fit(X_train, Y_train)


def predict_values(model, X_test) :
    ''' returns the prediction '''
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
    
    #filename = input('Enter file name/filepath :')
    adv_df = load_data('advertising.csv')
    #adv_df = adv_df[~(check_missing_values(adv_df))]
    #features = input('Enter list of features to be used :').split(',')
    #label    = input('Enter the label you want to classify :')
    
    features = ['Daily Time Spent on Site', 'Age', 'Area Income'
                ,'Daily Internet Usage', 'Male']
    label    = ['Clicked on Ad']
    
    features_df, label_df = get_features_and_label(adv_df,features, label)
    
    X_train, X_test, Y_train, Y_test = get_train_test_data(features_df,label_df)
    
    logit = fit_logistic_regression_model(X_train, Y_train)
    
    #coeffecients = coef_df(logit, X_train)
    predicted_values = predict_values(logit, X_test)
    
    classification_report = get_classification_report(Y_test, predicted_values)
    print(classification_report)

    confusion_matrix = get_confusion_matrix(Y_test, predicted_values)
    print (confusion_matrix)
    
    
    
    '''Classification Report 
              precision    recall  f1-score   support

          0       0.91      0.95      0.93       157
          1       0.94      0.90      0.92       143

avg / total       0.92      0.92      0.92       300
     
        Confusion Matrix
       [[149   8]
       [ 15 128]]
       
       Looking at the classification report, our model has an accuracy 
       of 92%. 
    
    '''
    
