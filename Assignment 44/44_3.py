# Add a new column 'Total' to the DataFrame as the sum of all subject marks.

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
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

print(border)
print("DataFrame with Total Marks:")
print(df)
print(border)