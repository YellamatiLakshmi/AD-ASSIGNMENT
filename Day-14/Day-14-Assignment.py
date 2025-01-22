#!/usr/bin/env python
# coding: utf-8

# # Assignment 2: Drug Effectiveness and Side Effects Comparison
# Objective:
# Compare drug effectiveness and side effects by different products, regions, and trial periods. Visualize these comparisons using matplotlib and seaborn.
# Instructions:
# Load the dataset.
# Perform any necessary data cleaning.
# Create the following visualizations:
# A bar plot comparing the average Effectiveness for each drug across different regions.
# A violin plot to show the distribution of Effectiveness and Side_Effects for each product.
# A pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend.
# A boxplot comparing Effectiveness for different trial periods.
# A regression plot to analyze how Marketing_Spend affects drug Effectiveness.
# Based on the visualizations, provide an analysis of:
# Which product has the best overall effectiveness.
# The correlation between effectiveness and side effects.
# Expected Outcome:
# Insights into how the effectiveness of each drug varies by region and trial period.
# Understanding the trade-off between drug effectiveness and side effects.
# 
# 

# In[11]:


import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\ypras\\OneDrive\\Desktop\\Application Development - 25\\Day_14_Pharma_data.csv") 

# Perform any necessary data cleaning.
print(df.isnull().sum())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Create the following visualizations: A bar plot comparing the average Effectiveness for each drug across different regions.

import matplotlib.pyplot as plt
import seaborn as sns

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Region', y='Effectiveness', hue='Product_Name')
plt.title('Average Effectiveness by Region')
plt.show()

# A violin plot to show the distribution of Effectiveness and Side_Effects for each product.
# Effectiveness
sns.violinplot(data=df, x='Product_Name', y='Effectiveness')
plt.title('Effectiveness by Product')
plt.show()

# Side Effects
sns.violinplot(data=df, x='Product_Name', y='Side_Effects')
plt.title('Side Effects by Product')
plt.show()

# A pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend. 
sns.boxplot(data=df, x='Trial_Period', y='Effectiveness')
plt.title('Effectiveness by Trial Period')
plt.show()

#A regression plot to analyze how Marketing_Spend affects drug Effectiveness.
sns.regplot(data=df, x='Marketing_Spend', y='Effectiveness')
plt.title('Marketing Spend vs. Effectiveness')
plt.show()



# In[ ]:




