
# coding: utf-8

# # Finance Data Project 
# 
# In this data project we will focus on exploratory data analysis of stock prices. Keep in mind, this project is just meant to practice your visualization and pandas skills, it is not meant to be a robust financial analysis or be taken as financial advice.
# 
# We'll focus on bank stocks and see how they progressed throughout the [financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) all the way to early 2016.

# ## Get the Data
# 
# In this section we will learn how to use pandas to directly read data from Google finance using pandas!
# 
# First we need to start with the proper imports, which we've already laid out for you here.
# 
# *Note: [You'll need to install pandas-datareader for this to work!](https://github.com/pydata/pandas-datareader) Pandas datareader allows you to [read stock information directly from the internet](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) Use these links for install guidance (**pip install pandas-datareader**), or just follow along with the video lecture.*
# 
# ### The Imports
# 
# Already filled out for you.

# In[1]:

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns

#get_ipython().magic('matplotlib inline')


# ## Data
# 
# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.
# 2. Figure out how to use datareader to grab info on the stock.
# 

start = datetime.datetime(2006, 1, 1)
end   = datetime.datetime(2016, 1, 1)
source = 'google'

#Bank of America
BAC = data.DataReader('BAC', source, start, end)

#CitiGroup
C = data.DataReader('C', source, start, end)

#Goldman Sachs
GS = data.DataReader('GS', source, start, end)

#JP Morgan Chase
JPM = data.DataReader('JPM', source, start, end)

#Morgan Stanley
MS = data.DataReader('MS', source, start, end)

#Wells Fargo
WFC = data.DataReader('WFC', source, start, end)


# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**


tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**

bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC], axis = 1, keys=tickers)


# ** Set the column name levels **

bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# ** Check the head of the bank_stocks dataframe.**

print(bank_stocks.head())

# # EDA
# 
# Let's explore the data a bit! 
# 
# ** What is the max Close price for each bank's stock throughout the time period?**

bank_close = bank_stocks.xs('Close', axis = 1, level = 1)
print(bank_close.max())


# ** Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:**
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

# ** We can use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.**


returns = pd.DataFrame()
for bank in bank_close.columns :
    returns[bank + ' Return'] = bank_close[bank].pct_change()


# ** Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?**
sns.pairplot(returns[1:])


# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?**

print(returns.idxmin())


# ** You should have noticed that Citigroup's largest drop and biggest gain were very close to one another, did anythign significant happen in that time frame? **
print(returns.idxmax())


# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?**
print(returns.std()) #citigroup riskiest

print(returns.ix['2015-01-01': '2016-01-01'].std()) #similar risk profiles


# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **
sns.set_style('whitegrid')
sns.distplot(returns.ix['2015-01-01': '2016-01-01']['MS Return'], bins = 100, color='g',hist_kws=dict(edgecolor="w"))

# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **
sns.distplot(returns.ix['2008-01-01': '2008-12-31']['C Return'], bins = 100, color='r',hist_kws=dict(edgecolor="w"))

# ____
# # More Visualization
# 
# A lot of this project will focus on visualizations. Feel free to use any of your preferred visualization libraries to try to recreate the described plots below, seaborn, matplotlib, plotly and cufflinks, or just pandas.
# 
# ### Imports

# In[14]:

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# ** Create a line plot showing Close price for each bank for the entire index of time. 

'''for bank in bank_close.columns:
    bank_close[bank].plot(figsize=(12,4),label = bank)
plt.legend()'''
# or
'''plt.figure(figsize=(12,4))
for bank in tickers:
    plt.plot(bank_close[bank],label = bank)
plt.legend()
for tick in plt.gca().xaxis.get_ticklabels():
    tick.set_rotation(45)'''
#or 
for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

print(bank_stocks.xs(key='Close', axis = 1, level = 1)) #print close column for each bank stock

bank_stocks.xs(key='Close', axis = 1, level = 1).plot(figsize=(12,4))


#using plotly
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# ## Moving Averages
# 
# Let's analyze the moving averages for these stocks in the year 2008. 
# 
# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**


BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label = '30 day moving average',figsize=(10,4))
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC Close Price')
plt.legend()


# ** Create a heatmap of the correlation between the stocks Close Price.**

sns.heatmap(bank_close.corr(),annot=True)


# ** Optional: Use seaborn's clustermap to cluster the correlations together:**

sns.clustermap(bank_close.corr(), annot=True)

#using plotly
bank_close.corr().iplot(kind='heatmap', colorscale='rdylbu')


# # Part 2 (Optional)
# 
# In this second part of the project we will rely on the cufflinks library to create some Technical Analysis plots. 

# ** Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.**

BAC.ix['2015-01-01':'2016-01-01'].iplot(kind='candle')


# ** Use .ta_plot(study='sma') to create a Simple Moving Averages plot of Morgan Stanley for the year 2015.**

MS.ix['2015-01-01':'2016-01-01']['Close'].ta_plot(study='sma')


# **Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.**

BAC.ix['2015-01-01':'2016-01-01']['Close'].ta_plot(study='boll')

