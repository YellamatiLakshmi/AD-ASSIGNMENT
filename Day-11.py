# Assignment 1: Sorting and Ranking Data
# Tasks:
# Sort the dataset by Account_Balance in descending order and display the first 10 rows.
# Create a ranking column for Transaction_Amount within each Branch:
# Use rank() to give ranks for transactions based on their amounts within each branch.
# Objective:
# Learn how to sort data and apply ranking based on certain columns.



import pandas as pd

df = pd.read_csv("C:\\Users\\yp\\Downloads\\\Day_12_banking_data.csv")


# Sort the dataset by Account_Balance in descending order and display the first 10 rows.
sorted_df = df.sort_values(by='Account_Balance', ascending=False)
print(sorted_df.head(10))

# Create a ranking column for Transaction_Amount within each Branch:
# Use rank() to give ranks for transactions based on their amounts within each branch.
df['Transaction_Rank'] = df.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print(df)


