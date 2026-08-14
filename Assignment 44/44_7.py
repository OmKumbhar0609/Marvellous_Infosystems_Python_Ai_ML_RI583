# Create a bar plot of student names vs total marks.

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
df['Total'] = df['Math'] + df['Science'] + df['English']

plt.bar(df['Name'], df['Total'])

plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Student Names vs Total Marks')

plt.show()

print(border)
print("Bar plot of student names vs total marks displayed.")
print(df)
print(border)