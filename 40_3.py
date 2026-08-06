# Train the model using only:
# StudyHours
# Attendance
# Compare the accuracy with the full-feature model.
# Is the model still performing well?

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

X_small = df[["StudyHours","Attendance"]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X_small,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("Accuracy using only StudyHours and Attendance =",accuracy*100)


# Accuracy is usually lower than the full-feature model.
# Using fewer features reduces prediction performance.