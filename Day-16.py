# Find the max, min, median, first quartile, third quartile for the data set : 23, 42, 12, 10, 15, 14, 9
data = [23, 42, 12, 10, 15, 14, 9]

# display sorted data
data.sort()
print("Sorted Data :",data)

# display min and max value
print("Min value :",min(data))
print("Max value :",max(data))


# display median

import statistics
median = statistics.median(data)
print("Median:", median)

# Calculate Q1 and Q3
import numpy as np

# First quartile (25th percentile)
q1 = np.percentile(data, 25)  
print("First Quartile (Q1):", q1)

# Third quartile (75th percentile)
q3 = np.percentile(data, 75)  
print("Third Quartile (Q3):", q3)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dataset with outliers
np.random.seed(10)
data = pd.DataFrame( {
    'value' : np.concatenate([np.random.normal(0, 1, 100), np.random.normal(10, 1, 10)]) # add outliers at right hand
})

# calculate the IQR for the box plot-based outlier detection
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1

# define outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# identify outliers
outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]

# print outliers
print(outliers)
