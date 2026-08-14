# Use the DataFrame from Q1 and print descriptive statistics using .describe().

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
print("Descriptive Statistics:")
print(df.describe())

print(border)