# Draw a boxplot for Attendance. Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.ylabel("Attendance")
plt.show()

# The boxplot helps identify outliers. Points outside the whiskers are considered outliers.
# If no points appear outside the whiskers, there are no significant outliers.