#Import all the required packages

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
import seaborn as sns


# Load the data set

location = "/Users/chiranjibighimire/Desktop/TM_finalProject/TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx"

df_existing = pd.read_excel(location, sheet_name='Existing employees')
df_nonexisting = pd.read_excel(location, sheet_name='Employees who have left')

#print(df_existing.head)
#print(df_nonexisting.head)
#print(df_existing.columns)

# Print the dimension of the data sets
#print(df_existing.shape)
#print(df_nonexisting.shape)

#print(df_existing.dtypes)

#Check If there are any missing values

#print(df_existing.isnull().any())

#print(df_nonexisting.isnull().any())
#Our data set is clean, no missing values in both excel sheets

#Calculate the mean for each columns


#print('Average of Existing Employee:', df_existing.mean())
print('Average of Ex-employee:', df_nonexisting.mean())


##Calculate categorical mean for categorical columns 'department' and 'salary'.
#For existing employee

#print(df_existing.groupby('dept').mean())

#print(df_existing.groupby('salary').mean())

#For ex-employee

#print(df_nonexisting.groupby('dept').mean())
#print(df_nonexisting.groupby('salary').mean())

##matplotlib inline
import matplotlib.pyplot as plt
pd.crosstab(df_existing.dept,df_nonexisting.dept).plot(kind='bar')
plt.title('Turnover Frequency for Department')
plt.xlabel('Department')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')
plt.show()

# Visualize the histogram of numerical variables
#For existing employees
num_bins = 10
df_existing.hist(bins=num_bins, figsize=(20,15))
plt.savefig("df_existing_histogram_plots.png")
#plt.show()

# Histogram for ex-employees
num_bins = 10
df_nonexisting.hist(bins=num_bins, figsize=(20,15))
plt.savefig("df_nonexisting_histogram_plots.png")
plt.show()