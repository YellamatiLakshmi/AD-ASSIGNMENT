#!/usr/bin/env python
# coding: utf-8

# # Assignment 1: Data Exploration
# Tasks:
# Load the banking_data.csv file using Pandas.
# Display the first 5 rows of the dataset.
# Use .describe() to generate basic statistics of the numerical columns (e.g., Transaction_Amount, Account_Balance).
# Check for missing values in the dataset.
# Objective:
# Understand how to load and inspect the dataset.
# Use basic descriptive statistics and data integrity checks.
# 

# In[3]:


import pandas as pd

# Load the banking_data.csv file using Pandas.
df = pd.read_csv("C:\\Users\ypras\\OneDrive\\Desktop\\Application Development - 25\\Day_9_banking_data.csv")

print(df)

# Display the first 5 rows of the dataset.
print(df.head())

# Use .describe() to generate basic statistics of the numerical columns (e.g., Transaction_Amount, Account_Balance).
print(df.describe())

# Check for missing values in the dataset.
print(df.isnull().sum())


# # Assignment 2: Data Aggregation and Grouping
# Tasks:
# Group the data by Account_Type and calculate:
# The total sum of Transaction_Amount.
# The average Account_Balance for each account type.
# Group the data by Branch and calculate:
# The total number of transactions per branch.
# The average transaction amount per branch.
# Objective:
# Learn to use groupby() for aggregating data by categories.
# Gain skills in calculating grouped statistics.
# 
# 

# In[6]:


# Group the data by Account_Type and calculate: The total sum of Transaction_Amount. The average Account_Balance for each account type.
account_group = df.groupby('Account_Type').agg(
    Total_Transaction_Amount=('Transaction_Amount', 'sum'),
    Average_Account_Balance=('Account_Balance', 'mean')
)

# Group the data by Branch and calculate: The total number of transactions per branch. The average transaction amount per branch.
branch_group = df.groupby('Branch').agg(
    Total_Transactions=('Transaction_Amount', 'count'),
    Average_Transaction_Amount=('Transaction_Amount', 'mean')
)


print(account_group)
print(branch_group)


# In[ ]:




