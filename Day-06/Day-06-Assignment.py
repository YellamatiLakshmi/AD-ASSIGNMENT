#!/usr/bin/env python
# coding: utf-8

# # Question:
# Using the Pandas library, perform the following tasks:
# 
# 1. Create a DataFrame from the following data:
#    | Name     | Age | Department   | Salary  |
#    |----------|-----|--------------|---------|
#    | John     | 28  | HR           | 45000   |
#    | Alice    | 34  | IT           | 60000   |
#    | Bob      | 23  | Marketing    | 35000   |
#    | Diana    | 29  | Finance      | 50000   |
# 
# 2. Write code to:
#    - Display the first 2 rows of the DataFrame.
#    - Add a new column named `Bonus` where the bonus is 10% of the salary.
#    - Calculate the average salary of employees in the DataFrame.
#    - Filter and display employees who are older than 25.
# 
# 
# 

# In[4]:


import pandas as pd
Name = ["John", "Alice", "Bob", "Diana"]
Age = [28, 34, 23, 29]
Department = ["HR", "IT", "Marketing", "Finance"]
Salary = [45000, 60000, 35000, 50000]
d1 = {"Name" : Name, "Age" : Age, "Department" : Department, "Salary" : Salary}
df = pd.DataFrame(d1)
print(df)


# In[5]:


df.head(2)


# In[9]:


df["Bonus"] = df["Salary"] * 0.1
df


# In[12]:


avg = df["Salary"].mean()
print(avg)


# In[14]:


age = df[df["Age"]>25]
df

