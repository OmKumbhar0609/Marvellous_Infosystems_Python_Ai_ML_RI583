# Plot a pie chart of subject marks for 'Sagar'

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

sagar = df[df['Name'] == 'Sagar'].iloc[0]

marks = [sagar['Math'], sagar['Science'], sagar['English']]
subjects = ['Math', 'Science', 'English']

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Sagar's Subject Marks")
plt.show()

print(border)