#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("C:\\Users\\ypras\\OneDrive\\Desktop\\Application Development - 25\\Day_12_banking_data.csv")

print(df.head())


# In[4]:


account_type_sum = df.groupby('Account_Type')['Transaction_Amount'].sum()

account_type_sum.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.xticks(rotation=45) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[5]:


branch_sum = df.groupby('Branch')['Transaction_Amount'].sum()

branch_sum.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='viridis')
plt.title('Percentage of Transactions per Branch')
plt.ylabel('') 
plt.show()


# In[ ]:




