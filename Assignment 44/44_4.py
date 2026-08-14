# Display students who scored more than 85 in Science.

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

result = df[df['Science'] > 85]

print(border)
print("Students who scored more than 85 in Science:")
print(result)
print(border)