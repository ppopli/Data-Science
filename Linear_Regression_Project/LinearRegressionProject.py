# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:46:36 2017

@author: Pulkit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(filename) :
    ''' function to read data from file and return the data frame subset
        to work with'''
    
    df = pd.read_csv(filename)
    return df[df.columns[3:]] 


def get_features_and_labels(df) :
    ''' returns features and label subsets from data frame '''
    
    labels = df['Yearly Amount Spent']
    features = df[df.columns[:-1]]
    
    return features,labels

def get_train_test_data(features, labels) :
    ''' returns the training and test data for features and labels
        30% of data is will be used for testing the model'''
    
    from sklearn.model_selection import train_test_split
    
    return  train_test_split(features, labels, test_size=0.3, random_state=101)


def fit_linear_model(X_train, Y_train) :
    ''' returns a linear model '''
    
    from sklearn.linear_model import LinearRegression
    return LinearRegression().fit(X_train, Y_train)

def coef_df(model, subset) :
    ''' returns a data frame of coefficients '''
    coef_df = pd.DataFrame(model.coef_, index = subset.columns,
                        columns = ['Coefecients'])
    coef_df.columns.name = 'Coefecient Names'
    return coef_df    


def predict_values(model, X_test) :
    ''' returns the prediction '''
    return model.predict(X_test)


def plot_residuals(predicted, Y_test) :
    ''' plot histogram of residual values '''
    sns.set_style('whitegrid')
    plt.figure()
    sns.distplot(Y_test - predicted, bins = 50, hist_kws={'edgecolor':'w'})
    plt.savefig('residuals.png', bbox_inches='tight')
    
    
def plot_predicted_vs_Y_test(predicted, Y_test) :
    
    ''' plots predicted labels from test features vs known test labels
        to check how much off are the predicted labels from known test
        labels '''
        
    plt.figure()
    plt.scatter(Y_test, predicted)
    plt.xlabel('Y_test')
    plt.ylabel('Predicted Labels')
    plt.savefig('Predicted_vs_Y_test.png', bbox_inches='tight')


def mae_mse_rmse_rsquared(Y_test, predicted) :
    ''' returns the mean absolute error,
                    mean squared error,
                    root mean squared error '''
    
    from sklearn import metrics
    
    return (metrics.mean_absolute_error(Y_test, predicted),
            metrics.mean_squared_error(Y_test, predicted),
            np.sqrt(metrics.mean_squared_error(Y_test, predicted)),
                   metrics.explained_variance_score(Y_test, predicted))

if __name__ == '__main__':
 
    ecom_df = read_data('Ecommerce Customers')  
    features,labels = get_features_and_labels(ecom_df)
    
    X_train, X_test, Y_train, Y_test = get_train_test_data(features,labels)
    
    lm = fit_linear_model(X_train, Y_train)
    
    coefecients = coef_df(lm, X_train)
    predicted_values = predict_values(lm, X_test)
    
    print(coefecients)
    print("\n\n")

    MAE, MSE, RMSE, RSquared = mae_mse_rmse_rsquared(Y_test, predicted_values)
    
    print (
    'Mean Absolute Error: {}\nMean Squared Error: {}\nRoot Mean Squared Error: {}\nRSquared: {}'
                          .format(MAE, MSE, RMSE, RSquared))
    

'''
                     Coeficients
Avg. Session Length     25.981550
Time on App             38.590159
Time on Website          0.190405
Length of Membership    61.279097

'''


''' Looking at the coefecients for "Time on App (38.590159)" and for "Time on
    website(0.190405)" it is observed that with every minute spent on App would 
    increase the "Yearly Amount Spent" by $39 approx where as every minute 
    spent on webseite would increase the "Yearly Amount Spent" by $0.19 keeping
    other coeffecints fixed. This can be interpreted in two ways :- 
    
    1.) Company can focus more on the website to enhance the user experience 
        on website so that website traffic could be increased, which would
        increase the "Yearly Amount Spent".
    
        
    2.) Company's App is doing much better than the website, Company could 
        focus more on enhancing user experience on App.        
'''