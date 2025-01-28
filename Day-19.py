import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Dataset

data = {
    "Customer_Id" : [1, 2, 3, 4],
    "Gender" : ["Male", "Female", "Feale", "Male"],
    "City" : ["Hyderabed", "Pune", "Bangalore", "Mumbai"]
}


df = pd.DataFrame(data)

print("Original data : ")
print(df)

one_hot_encoder = oneHotEncoder(Sparse_out = False)
columns_to_encode = ["gender", "city"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_Feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data,columns=encoded_columns)
print(encoded_df)
print("\nOne-Hot Encoded DataFrame with sklearn : ")