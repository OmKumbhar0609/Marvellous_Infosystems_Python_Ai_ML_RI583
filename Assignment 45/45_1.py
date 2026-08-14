# Normalize the 'Math' scores using Min-Max Scaling

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

border = "-"*60
print(border)
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

print(df[['Name', 'Math', 'Math_Normalized']])

print(border)
