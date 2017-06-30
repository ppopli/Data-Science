# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:18:32 2017

@author: Pulkit
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt, pylab as ply

file = '911.csv'

df_911 = pd.read_csv(file, converters= {'timeStamp':pd.to_datetime})


def top_5_zip():
    ''' returns top 5 zip codes for 911 calls'''
    
    return df_911['zip'].value_counts().iloc[:5]



def top_5_twp():
    ''' returns top 5 townships for 911 calls'''
    
    return df_911['twp'].value_counts().iloc[:5]



def unique_title_codes():
    ''' returns number of unique title codes'''
    
    return df_911['title'].nunique()



def add_reasons():
    ''' adds a new columns Reasons for call'''
    
    df_911['Reasons'] = df_911['title'].apply(lambda x: x[:x.find(':')])
     


def most_common_reasons():
    ''' returns the most common reasons for 911 calls'''
    
    add_reasons()
    return df_911['Reasons'].value_counts()



def plot_911_call_reasons():
    '''plots the counts for 911 calls based on reason'''
    
    sns.set_style('whitegrid')
    sns.countplot(x='Reasons',data=df_911)
    ply.savefig('plot_911_call_reasons.png',bbox_inches='tight')



def add_hour_month_day():
    '''add three columns Hour, Month and Day of the week and 
       maps days of the week to corresponding names using dmap dictionary.'''
    
    df_911['Hour'],df_911['Month'],df_911['DayOfTheWeek'] = zip(
            *map(lambda x : (x.hour, x.month, x.dayofweek),
                 df_911['timeStamp']))
    dmap = {0:'Mon',
            1:'Tue',
            2:'Wed',
            3:'Thu',
            4:'Fri',
            5:'Sat',
            6:'Sun'}
    
    df_911['DayOfTheWeek'] = df_911['DayOfTheWeek'].map(dmap)


def number_of_calls_per_day_per_reason():
    ''' Presents the graphical representation of number of calls made
        per day of week'''
    
    sns.countplot(x='DayOfTheWeek',data=df_911, hue='Reasons', 
                  palette='viridis')
    plt.gca().legend(loc= 'upper right', bbox_to_anchor=(1.15,1.0))
    plt.xlabel('Day of Week')
    ply.savefig('numberOFCallsPerReasons.png',bbox_inches='tight')
    plt.show()

def number_of_calls_per_day_month_reason():
    
    ''' presents the graphical representation of number of calls made
        per month'''
    
    ''' dmonth_map = {1:'Jan',
                  2:'Feb',
                  3:'Mar',
                  4:'Apr',
                  5:'May',
                  6:'Jun',
                  7:'Jul',
                  8:'Aug',
                  9:'Sep',
                  10:'Oct',
                  11:'Nov',
                  12:'Dec'}'''
    
#    df_911['Month'] = df_911['Month'].map(dmonth_map)
    sns.countplot(x='Month',data=df_911, hue='Reasons', 
                 palette='viridis')
    plt.gca().legend(loc= 'upper right', bbox_to_anchor=(1.15,1.0))
    plt.xlabel('Month')
    plt.show()
    ply.savefig('number_of_calls_per_day_month_reason.png',bbox_inches='tight')




def plot_of_counts_of_calls_per_month():
    ''' fills the info for missing months and plots the count of calls
        per month'''
        
    temp_df = df_911.groupby('Month').count()
    plt.plot(temp_df['twp'])
    plt.xlabel('Month')
    plt.show()
    ply.savefig('plot_of_counts_of_calls_per_month.png',bbox_inches='tight')



def plot_linear_fit_for_calls_per_month():
    ''' plots lmplot for calls per month'''
    
    temp_df = df_911.groupby('Month').count()
    temp_df.reset_index(inplace=True)
    sns.lmplot(x='Month',y='twp',data=temp_df)
    ply.savefig('plot_linear_fit_for_calls_per_month.png',bbox_inches='tight')
    


def add_date_column():
    ''' adds a new column date'''
    
    df_911['Date'] = df_911['timeStamp'].apply(lambda x : x.date())
    print(df_911.head())



def plot_by_day():
    '''groups the data set by Date column and plots the count of calls 
        per date'''
        
    df_911.groupby('Date').count()['twp'].plot()
    ply.savefig('plot_by_day.png',bbox_inches='tight')
    
    

def plot_by_reason_Traffic():
    '''plot the call count for Traffic reason'''
    
    df_911[df_911['Reasons']=='Traffic'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('Traffic')
    ply.savefig('plot_by_reason_Traffic.png',bbox_inches='tight')




def plot_by_reason_Fire():
    '''plot the call count for Fire reason'''
    
    df_911[df_911['Reasons']=='Fire'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('Fire')
    ply.savefig('plot_by_reason_Fire.png',bbox_inches='tight')
    
    

def plot_by_reason_EMS():
    '''plot the call count for EMS reason'''
    
    df_911[df_911['Reasons']=='EMS'].groupby('Date').count()['twp'].plot()
    plt.tight_layout()
    plt.title('EMS')
    ply.savefig('plot_by_reason_EMS.png',bbox_inches='tight')



def plot_heatmap_calls_per_day_corresponding_to_hour():
    ''' creates a heatmap for calls per day Vs hours of a day'''
    
    temp = df_911.groupby(['DayOfTheWeek','Hour'])['Reasons'].count().unstack(level=-1)
    plt.figure(figsize=(12,4))
    sns.heatmap(data=temp, cmap='viridis')
    plt.ylabel('Day of Week')
    ply.savefig('plot_heatmap_calls_per_day_corresponding_to_hour.png',bbox_inches='tight')
    


def plot_clustermap_calls_per_day_corresponding_to_hour():
    ''' creates a clustermap for calls per day Vs hours of a day'''
    
    temp = df_911.groupby(['DayOfTheWeek','Hour'])['Reasons'].count().unstack(level=-1)
    plt.figure(figsize=(12,4))
    sns.clustermap(data=temp, cmap='viridis')
    plt.ylabel('Day of Week')
    ply.savefig('plot_clustermap_calls_per_day_corresponding_to_hour.png',bbox_inches='tight')
    


def plot_heatmap_calls_per_day_corresponding_to_month():
    ''' creates a heatmap for calls per day Vs months'''
     
    temp = df_911.groupby(['DayOfTheWeek','Month'])['Reasons'].count().unstack(level=-1)
    plt.figure(figsize=(12,4))
    sns.heatmap(data=temp, cmap='viridis')
    plt.ylabel('Day of Week')
    ply.savefig('plot_heatmap_calls_per_day_corresponding_to_month.png',bbox_inches='tight')

     
    
    
def plot_clustermap_calls_per_day_corresponding_to_month():
    ''' creates a clustermap for calls per day Vs months'''
    temp = df_911.groupby(['DayOfTheWeek','Month'])['Reasons'].count().unstack(level=-1)
    plt.figure(figsize=(12,4))
    sns.clustermap(data=temp, cmap='viridis')
    plt.ylabel('Day of Week')
    ply.savefig('plot_clustermap_calls_per_day_corresponding_to_month.png',bbox_inches='tight')





if __name__=='__main__':
    add_reasons()
    add_hour_month_day()
    add_date_column()
  
    
    
    
                                          