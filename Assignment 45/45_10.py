# Plot a boxplot for English marks to check distribution and outliers

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

plt.boxplot(df['English'])

plt.title("Boxplot of English Marks")
plt.ylabel("Marks")

plt.show()

print(border)