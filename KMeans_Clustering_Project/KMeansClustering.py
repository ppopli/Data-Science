# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 17:36:46 2017

@author: Pulkit
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data_set(filename):
    ''' returns the data set to work with '''
    return pd.read_csv(filename, index_col=0)


def check_missing_values(df) :
    ''' returns True if there are missing values
        else returns False '''
    sns.heatmap(df.isnull(),yticklabels=False,cbar = False, cmap='viridis')
    return df.isnull().sum().sum() != 0


def create_scatter(df, col_1, col_2) :
    ''' creates a scatter plot b/w the columns passed '''
    sns.set_style('whitegrid')
    plt.figure(figsize=(6,6))
    sns.lmplot(x=col_1, y = col_2, data=df, hue='Private',
               palette='coolwarm',size=6,aspect=1,fit_reg=False)
    plt.savefig((col_1 + '_vs_' + col_2 +'.png'),  bbox_inches='tight' )



def create_stacked_histogram(df, col, hue) :
    ''' creates a stacked histogram for the passed col and hue'''
    
    sns.set_style('darkgrid')
    plt.figure(figsize=(6,6))
    g = sns.FacetGrid(data = df, hue=hue, palette='coolwarm',size=6,aspect=2)
    g = g.map(plt.hist,col,bins=20,alpha = 0.5)
    plt.savefig((col + '.png'),  bbox_inches='tight' )



def fit_KMeansClustering(df) :
    ''' returns a logistic regression model '''
    
    from sklearn.cluster import KMeans
    
    return KMeans(n_clusters=2).fit(df)


def return_cluster_centers(model) :
    ''' returns the prediction '''
    return model.cluster_centers_


def converter(private):
    if private=='Yes':
        return 1
    else:
        return 0
    

def get_classification_report(Y_test, predicted_values) :
    ''' returns classification report for the model '''
    from sklearn.metrics import classification_report
    
    return classification_report(Y_test, predicted_values)

def get_confusion_matrix(Y_test, predicted_values) :
    ''' returns confusion matrix '''
    
    from sklearn.metrics import confusion_matrix
    
    return confusion_matrix(Y_test, predicted_values) 



if __name__=='__main__':
    df = load_data_set('College_Data')
    ''' check missing values '''
    
    if not check_missing_values(df) :
        ''' create a scatter plot Grad.Rate versus Room.Board '''
        create_scatter(df, 'Room.Board','Grad.Rate')
        
        ''' create a scatter plot F.Undergrad versus Outstate  '''
        create_scatter(df, 'Outstate','F.Undergrad')
        
        '''Create a stacked histogram showing 
        Out of State Tuition based on the Private column'''
        
        create_stacked_histogram(df,'Outstate', 'Private')
        
        '''Create a stacked histogram showing 
        Grad.Rate column based on the Private column'''
        
        create_stacked_histogram(df,'Grad.Rate', 'Private')
        
        ''' As we can see in Grad.Rate stacked histogram 
        one college has a Grad.Rate greater than 120% which
        doesn't make any sense, so we need to make it to 100%'''
        
        df.loc[df[df['Grad.Rate'] > 100].index,'Grad.Rate'] = 100
        
        ''' To check that it has been changed to 100% we can again plot
        the stacked histogram for Grad.Rate'''
        
        create_stacked_histogram(df,'Grad.Rate', 'Private')
        
        ''' fit the model'''
        
        kmeans = fit_KMeansClustering(df.drop('Private', axis = 1))
        
        
        ''' print cluster centers '''
        print(return_cluster_centers(kmeans))
        
        ''' evaluating the model '''
        
        '''There is no perfect way to evaluate clustering 
        if we don't have the labels, we do have the labels for this exercise,
        so we take advantage of this to evaluate our clusters '''
        
        ''' Create a new column for df called 'Cluster', 
        which is a 1 for a Private school, and a 0 for a public school ''' 

        df['Cluster'] = df['Private'].apply(converter)
        
        print(get_classification_report(df['Cluster'], kmeans.labels_))
        print(get_confusion_matrix(df['Cluster'], kmeans.labels_))
        
    
    
'''Classification report
  
             precision    recall  f1-score   support

          0       0.21      0.65      0.31       212
          1       0.31      0.06      0.10       565
 avg / total       0.29      0.22      0.16       777

 '''
 

'''Confusion Matrix 

[[138  74]
 [531  34]]

'''
''' Not bad considering the algorithm is purely using the features to
 cluster the universities into 2 distinct groups '''
        
        
        