# Plot SleepHours against FinalResult. Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["SleepHours"],
            df["FinalResult"])

plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Sleep Hours vs Final Result")
plt.show()

# sleeping more does not guarantee success. 
# Adequate sleep helps maintain health and concentration, but final performance also depends on study hours, attendance, previous scores, and assignment completion.