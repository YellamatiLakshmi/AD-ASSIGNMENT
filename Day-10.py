#!/usr/bin/env python
# coding: utf-8

# # Assignment 1: Filtering Data Based on Conditions
# Tasks:
# Filter out all rows where the Transaction_Amount is greater than 2000.
# Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000.
# Extract transactions made in the "Uptown" branch.
# Objective:
# Practice filtering data using conditions and boolean indexing.
# 
# 

# In[16]:


import pandas as pd

df = pd.read_csv("Path of the file\\Day_10_banking_data.csv")

# Filter out all rows where the Transaction_Amount is greater than 2000.
filtered_amount = df[df['Transaction_Amount'] > 2000]
print("Rows where Transaction_Amount > 2000:")
print(filtered_amount)


# Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000
filtered_loan_payment = df[
    (df['Transaction_Type'] == "Loan Payment") & 
    (df['Account_Balance'] > 5000)
]
print("\nRows where Transaction_Type is 'Loan Payment' and Account_Balance > 5000:")
print(filtered_loan_payment)


# Extract transactions made in the "Uptown" branch.
uptown_transactions = df[df['Branch'] == "Uptown"]
print("\nTransactions made in the 'Uptown' branch:")
print(uptown_transactions)


# # Assignment 2: Data Transformation
# Tasks:
# Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount.
# Create a new column Balance_Status:
# If Account_Balance is greater than 5000, label it as "High Balance".
# Otherwise, label it as "Low Balance".
# Objective:
# Learn how to create new columns and apply transformations based on existing data.
# 
# 

# In[17]:


# Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount. 
df['Transaction_Fee'] = df['Transaction_Amount'] * 0.02

#  If Account_Balance is greater than 5000, label it as "High Balance". Otherwise, label it as "Low Balance". 
df['Balance_Status'] = df['Account_Balance'].apply(lambda x: "High Balance" if x > 5000 else "Low Balance")

# Display the first few rows of the updated DataFrame
print(df.head())




# In[ ]:




