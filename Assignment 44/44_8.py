# Plot a line chart of marks for 'Amit' across all subjects.

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

amit = df[df['Name'] == 'Amit'].iloc[0]

subjects = ['Math', 'Science', 'English']
marks = [amit['Math'], amit['Science'], amit['English']]

plt.plot(subjects, marks, marker='o')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title("Amit's Marks Across Subjects")

plt.show()

print(border)
print("Line chart of Amit's marks across subjects displayed.")
print(df)
print(border)