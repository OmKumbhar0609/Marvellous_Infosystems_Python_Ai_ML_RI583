# Create a DataFrame for student marks and print basic information like shape, columns, and data types.

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

border = "-"*60
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print(border)
print("DataFrame:")
print(df)

print(border)
print("\nShape:")
print(df.shape)

print(border)
print("\nColumns:")
print(df.columns)

print(border)
print("\nData Types:")
print(df.dtypes)

print(border)
