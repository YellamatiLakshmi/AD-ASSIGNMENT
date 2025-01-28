# Assignment 1: Sales and Effectiveness Analysis
# Objective:
# Explore the relationship between marketing spend, sales, and drug effectiveness across different regions and age groups. Create visualizations using matplotlib and seaborn.
# Instructions:
# Load the dataset.
# Perform data cleaning (check for missing values, duplicates).
# Create the following visualizations:
# A bar plot showing total sales per region.
# A scatter plot to visualize the relationship between Marketing_Spend and Sales.
# A boxplot comparing drug effectiveness across different age groups.
# A line plot showing the sales trend for each product over different trial periods.
# A heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness.
# Based on the visualizations, summarize any patterns or trends you observe.
# Expected Outcome:
# Insights on how marketing spend impacts sales.
# Analysis of which age groups have higher drug effectiveness.
# Regional sales distribution.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset.
df = pd.read_csv("C:\\Users\\ypras\\Downloads\\Day_13_Pharma_data.csv")

# Perform data cleaning (check for missing values, duplicates).
print("Missing values per column:")
print(df.isnull().sum())

df.dropna(inplace=True)

duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

df.drop_duplicates(inplace=True)

print("Cleaned Dataset:")
print(df.head())

# Step 3: Create Visualizations


# A bar plot showing total sales per region.
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=region_sales, palette='viridis')
plt.title('Total Sales Per Region')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.show()

# A scatter plot to visualize the relationship between Marketing_Spend and Sales.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=df, hue='Region', palette='coolwarm')
plt.title('Marketing Spend vs. Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.show()

# A boxplot comparing drug effectiveness across different age groups.
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=df, palette='Set2')
plt.title('Drug Effectiveness Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Effectiveness')
plt.show()

# A line plot showing the sales trend for each product over different trial periods.
plt.figure(figsize=(12, 8))
sns.lineplot(x='Trial_Period', y='Sales', hue='Product', data=df, palette='tab10', marker='o')
plt.title('Sales Trend for Each Product Over Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Sales')
plt.show()

# A heatmap of the correlation between Sales, Marketing_Spend, and Effectiveness.
correlation_matrix = df[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


