# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Load the dataset (replace with actual data)
df = pd.read_csv("your_dataset.csv")

# Preprocessing: Handle NaN values and drop redundant columns
print("\n--------------- Preprocessing Stage ------------------------")
preprocessor = DataPreProcessor(df)
preprocessed_ = preprocessor.data_pre_processed()

# Retrieve the preprocessed dataframe and categorical columns list
df = preprocessed_[0]
cat_cols = preprocessed_[1]

# Print the NaN values to check preprocessing results
print("\n--------------- Post-Preprocessing Results -----------------")
print("**********************")
print("NaN values: \n", df.isnull().sum())
print("**********************\n")

# Apply transformations: Encode categorical columns using one-hot encoding
transform_ = DataTransformation(df)
df = transform_.encoding_cat(cat_cols=cat_cols)

# Print dataframe info after transformation
print("\n--------------- Transformed Data ---------------------------")
print(df.info())
print("\n------------\n")
print("NaN values after encoding: \n", df.isnull().sum())
