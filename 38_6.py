# Plot a histogram of StudyHours. Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.hist(df["StudyHours"], bins=10)
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

