# Write a program to:
# Display total number of students
# Count Passed students (FinalResult = 1)
# Count Failed students (FinalResult = 0)

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Total Students:", len(df))
print("Passed Students:", (df["FinalResult"] == 1).sum())
print("Failed Students:", (df["FinalResult"] == 0).sum())