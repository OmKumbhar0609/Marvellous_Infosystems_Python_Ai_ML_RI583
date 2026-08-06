# Import DecisionTreeClassifier from sklearn. Create a model object and train it using fit().

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Features and Target
X = df[["StudyHours","Attendance","PreviousScore",
        "AssignmentsCompleted","SleepHours"]]

y = df["FinalResult"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

print("Model Trained Successfully")