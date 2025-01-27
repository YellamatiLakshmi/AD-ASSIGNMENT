import pandas as pd
from sklearn.preprocessing import MinMaxScaler # Changed minmaxscalar to MinMaxScaler

data = { # Added dictionary initialization
    "age":[25,30,35,40,45],
    "height":[150,160,170,180,190],
    "weight":[50,60,70,80,90]
}

df = pd.DataFrame(data)
print(df)

scalar = MinMaxScaler() # Changed minmaxscalar to MinMaxScaler
scaled_data = scalar.fit_transform(df) # Changed scaled_dataq to scaled_data
print(scaled_data)

scaled_df = pd.DataFrame(scaled_data,columns=df.columns)
print(scaled_df)

# Convert the dictionary 'data' to a DataFrame first
df_data = pd.DataFrame(data)

# Perform the min-max scaling using the DataFrame
scaled_data = (df_data - df_data.min()) / (df_data.max() - df_data.min())

print(scaled_data)


