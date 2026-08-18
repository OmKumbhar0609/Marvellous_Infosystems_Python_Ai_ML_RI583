# Write a Python program to calculate the Euclidean distance between two points before
#  and after applying feature scaling, 
# and explain the difference in results.

import numpy as np
from sklearn.preprocessing import StandardScaler
from math import sqrt

data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

# Distance before scaling
d1 = sqrt((30-25)**2 + (40000-20000)**2)

# Scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(data)

# Distance after scaling
d2 = np.linalg.norm(scaled[1] - scaled[0])

print("Distance Before Scaling =", d1)
print("Distance After Scaling =", d2)


# Feature scaling brings all features to the same scale. 
# Before scaling, salary dominates the distance calculation because of its large values. 
# After scaling, both features contribute equally.