# Use value_counts() to analyze the distribution of FinalResult. Calculate the percentage of Pass and Fail students. Is the dataset balanced?

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

counts = df["FinalResult"].value_counts()
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("Counts:")
print(counts)

print("\nPercentage:")
print(percentage)