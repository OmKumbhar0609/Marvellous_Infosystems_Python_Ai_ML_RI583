# Drop the 'English' column from original DataFrame.

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
print("Original DataFrame:")
print(df)
print(border)

# Drop the 'English' column
df = df.drop('English', axis=1)
print("\nDataFrame after dropping 'English' column:")
print(df)
print(border)