# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:24:33 2017

@author: Pulkit
"""

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, pylab as ply
plt.style.use('ggplot')


file_name='NOAAData.csv' # file to work with

df_wd = pd.read_csv(file_name)

df_wd['Month_Date'] = df_wd['Date'].apply(lambda x : x[-5:]) #creating new column from Date

'''Removing 29 feb, filtering out dates for year 2015, selecting Element as TMIN, grouping on Month_Date and agg min
   value per day.'''


df_wd_min = df_wd[~(df_wd['Date'].str[-5:]=='02-29') & (pd.to_datetime(df_wd['Date']) < '2015-01-01') &
                     (df_wd['Element']=='TMIN')].groupby('Month_Date').agg({'Data_Value':np.min})


'''Removing 29 feb, filtering out dates for year 2015, selecting Element as TMAX, grouping on Month_Date and agg max
   value per day.'''

df_wd_max = df_wd[~(df_wd['Date'].str[-5:]=='02-29') & (pd.to_datetime(df_wd['Date']) < '2015-01-01') &
                     (df_wd['Element']=='TMAX')].groupby('Month_Date').agg({'Data_Value':np.max})



'''Removing 29 feb, extracting dates for year 2015, selecting Element as TMIN, grouping on Month_Date and agg min
   value per day.'''

df_2015_min = df_wd[~(df_wd['Date'].str[-5:]=='02-29') & (pd.to_datetime(df_wd['Date']) > '2014-12-31') &
                     (df_wd['Element']=='TMIN')].groupby('Month_Date').agg({'Data_Value':np.min})



'''Removing 29 feb, extracting dates for year 2015, selecting Element as TMAX, grouping on Month_Date and agg max
   value per day.'''

df_2015_max = df_wd[~(df_wd['Date'].str[-5:]=='02-29') & (pd.to_datetime(df_wd['Date']) > '2014-12-31') &
                     (df_wd['Element']=='TMAX')].groupby('Month_Date').agg({'Data_Value':np.max})


'''Finding index of the days in year 2015 where min temprature is less than years 2005-2014 and max temprature
   is greater than years 2005-2014'''
min_break,max_break = zip( *zip(np.where(df_2015_min['Data_Value'] < df_wd_min['Data_Value']) , 
                          np.where(df_2015_max['Data_Value'] > df_wd_max['Data_Value'])))


# to be used as xtick labels
month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


plt.figure(figsize=(10,4)) #creating the canvas 
plt.plot(df_wd_min.values/10, label = 'low',color='blue') #plotting min values for the years 2005-2014
plt.plot(df_wd_max.values/10,color='red', label = 'high') #plotting max values for the years 2005-2014 

#scatter plots of points where the record of max and min tempratures were broken in the year 2015
plt.scatter(min_break,df_2015_min.iloc[min_break]/10,s=20,c = 'm', label = 'min_break') 
plt.scatter(max_break,df_2015_max.iloc[max_break]/10,s=20,c = 'g', label = 'max_break')

plt.title('Month Wise Temprature Summary from 2005-2015') #plot title
plt.xlabel('Months') #xlabel(x-axis label)
plt.ylabel('Temprature (Degree C)') #ylabel(y-axis label)
plt.xticks(range(0,len(df_wd_max.index),33), month_list) #allocating xticks and xticklabels

plt.legend() #adding legend
plt.grid() #removing grid lines

#filling the gap between min and max values
plt.gca().fill_between(range(len(df_wd_max)),df_wd_max['Data_Value']/10,df_wd_min['Data_Value']/10,facecolor='blue',alpha=0.25 )
ply.savefig('MonthlyTemperatureSummary2005-2015.png', bbox_inches='tight') #save plot to png file
plt.show() #show the plot


