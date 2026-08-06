# Create a plot showing the relationship between AssignmentsCompleted and FinalResult. Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

plt.scatter(df["AssignmentsCompleted"],
            df["FinalResult"])

plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Assignments Completed vs Final Result")
plt.show()

# Students who complete more assignments generally have a higher chance of passing. 
# Assignment completion positively affects the final result.