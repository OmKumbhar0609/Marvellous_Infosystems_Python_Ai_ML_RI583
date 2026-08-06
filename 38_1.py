import pandas as pd

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# First 5 records
print("First 5 Records:")
print(df.head())

# Last 5 records
print("\nLast 5 Records:")
print(df.tail())

# Shape
print("\nRows and Columns:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Data Types
print("\nData Types:")
print(df.dtypes)