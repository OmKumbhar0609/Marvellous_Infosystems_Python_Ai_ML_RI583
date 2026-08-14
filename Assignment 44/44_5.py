# Replace 'Pooja' with 'Puja' in the 'Name' column.

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
df['Name'] = df['Name'].replace('Pooja', 'Puja')

print(border)
print("DataFrame with Updated Names:")
print(df)
print(border)