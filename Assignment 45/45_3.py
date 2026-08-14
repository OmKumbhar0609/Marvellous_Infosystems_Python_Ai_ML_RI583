# Group students by gender and calculate average marks

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

df['Gender'] = ['Male', 'Male', 'Female']

result = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

print(result)

print(border)