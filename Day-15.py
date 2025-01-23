import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer 

# dataset - house price with missing values


data= {
  'square_feet_area' : [8500,9600, np.nan,11250,np.nan,9550,14260,np.nan,13830,11500], #numeric
  'Year_built':[2003,1976,2001,np.nan,1998,2000,1978,1950,np.nan,1947], #numeric
  'over_all_condition': [5,8,6,7,np.nan,7,8,6,np.nan,7], #numeric
  'ready_to_move':['Yes','No','No',np.nan,'No',np.nan,'No','Yes',np.nan,'Yes'], #categorical value
  'Sale_price':[200000,180000,215000,250000,210000,190000,230000,225000,220000,215000] #target variable
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print(df.isnull().sum())

# Create a SimpleImputer object for numeric columns
numeric_imputer = SimpleImputer(strategy='mean')

# Replacing missing values with mean for numeric columns
df['square_feet_area'] = df['square_feet_area'].fillna(df['square_feet_area'].mean())
df['Year_built'] = df['Year_built'].fillna(df['Year_built'].mean())
df['over_all_condition'] = df['over_all_condition'].fillna(df['over_all_condition'].mean())

# Apply the imputer on the numeric columns
df[['square_feet_area', 'Year_built', 'over_all_condition']] = numeric_imputer.fit_transform(df[['square_feet_area', 'Year_built', 'over_all_condition']])

# Create an imputer for categorical columns to replace NaN wth mode
categorical_imputer = SimpleImputer(strategy='most_frequent') #use most_frequent

# Apply the imputer on the categorical column
df[['ready_to_move']] = categorical_imputer.fit_transform(df[['ready_to_move']])

# Print DataFrame after imputation
print("\nDataFrame after replacing missing values with SimpleImputer (mean for numeric, mode for categorical):")

print(df)