# Write a Python program that calculates the variance and standard deviation of the dataset

import numpy as np

data = [6, 7, 8, 9, 10, 11, 12]

variance = np.var(data)
std_dev = np.std(data)

print("Variance =", variance)
print("Standard Deviation =", std_dev)