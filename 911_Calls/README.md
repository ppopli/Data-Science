# 911 Calls

For this we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:

* lat : String variable, Latitude
* lng: String variable, Longitude
* desc: String variable, Description of the Emergency Call
* zip: String variable, Zipcode
* title: String variable, Title
* timeStamp: String variable, YYYY-MM-DD HH:MM:SS
* twp: String variable, Township
* addr: String variable, Address
* e: String variable, Dummy variable (always 1)

Based on this data set we will be answering some questions as follows: -

### Question 1
What are the top 5 zipcodes for 911 calls?

### Question 2
What are the top 5 townships (twp) for 911 calls? 

### Question 3
how many unique title codes are there? 

##  Creating new features
** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value. ** 

** For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

### Question 4
Create a countplot of 911 calls by Reason.

** We noticed that data was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

* Create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame.
* Create a simple plot off of the dataframe indicating the count of calls per month 
* Create a linear fit on the number of calls per month

### Question 5
Create a countplot of the Day of Week column with the hue based off of the Reason column.

### Question 6
create a countplot of the Month column with the hue based off of the Reason column.

### Question 7 
Create a new column called 'Date' that contains the date from the timeStamp column.
Use Date column with the count() aggregate and create a plot of counts of 911 calls.

### Question 8 
Recreate the plot in Question 7 but create 3 separate plots with each plot representing a Reason for the 911 call.