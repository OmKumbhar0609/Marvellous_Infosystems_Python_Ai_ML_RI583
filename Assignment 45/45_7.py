# Export the final DataFrame to a CSV file

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

df.to_csv("Student_Marks.csv", index=False)

print("CSV file saved successfully.")

print(border)