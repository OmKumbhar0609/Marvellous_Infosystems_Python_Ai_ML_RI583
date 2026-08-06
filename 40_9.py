# Create a new column: PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df["PerformanceIndex"] = (df["StudyHours"]*2)+df["Attendance"]

X = df.drop("FinalResult",axis=1)

y = df["FinalResult"]

X_train,X_test,y_train,y_test = train_test_split(
X,y,
test_size=0.2,
random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)

print("Accuracy =",acc*100,"%")