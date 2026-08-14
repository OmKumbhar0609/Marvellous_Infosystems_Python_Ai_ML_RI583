# Count how many students passed

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

df['Total'] = df['Math'] + df['Science'] + df['English']

df['Status'] = np.where(df['Total'] >= 250, 'Pass', 'Fail')
print(df[['Name', 'Total', 'Status']])

passed_students = (df['Status'] == 'Pass').sum()

print("Number of Passed Students:", passed_students)

print(border)