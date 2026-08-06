# Write a single structured Python program.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# -----------------------------
# Step 1 : Dataset Loading
# -----------------------------
df = pd.read_csv("student_performance_ml.csv")

print(df.head())

# -----------------------------
# Step 2 : Data Analysis
# -----------------------------
print(df.describe())

# -----------------------------
# Step 3 : Visualization
# -----------------------------
plt.hist(df["StudyHours"], bins=10)
plt.title("Study Hours")
plt.show()

# -----------------------------
# Step 4 : Train Test Split
# -----------------------------
X = df[["StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

# -----------------------------
# Step 5 : Model Training
# -----------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# -----------------------------
# Step 6 : Prediction
# -----------------------------
y_pred = model.predict(X_test)

print(y_pred)

# -----------------------------
# Step 7 : Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy =", accuracy * 100)

# -----------------------------
# Step 8 : Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.show()

# -----------------------------
# Step 9 : Final Conclusion
# -----------------------------
print("Model trained successfully.")
print("Decision Tree can predict whether a student will Pass or Fail.")