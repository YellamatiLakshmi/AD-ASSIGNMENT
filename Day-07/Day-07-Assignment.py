# 1.Load and Explore the Data Load the sales_data.csv file using Pandas. Display the first 5 rows of the dataset. Print basic statistics (mean, median, min, max, etc.) of the numerical columns using .describe().

import pandas as pd
df = pd.read_csv("Path of the file/Day_7_sales_data.csv")
print("First 5 rows :")
df.head(5) # Display the first 5 rows of the dataset

print("Basic statistics of numerical columns:")
df.describe()

# 2.Data Analysis Calculate the total sales for each region. Find the most sold product (based on quantity). Compute the average profit margin for each product. (Profit margin = Profit / Sales * 100)

# The total sales for each region
df.groupby('Region')['Sales'].sum()

# The most sold product (based on quantity).
df.groupby('Product')['Quantity'].sum().idxmax()

# Compute the average profit margin for each product
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
df.groupby('Product')['Profit Margin'].mean()