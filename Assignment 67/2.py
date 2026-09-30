# Neural Network Model to Predict Loan Approval

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# -------------------------------------------------
# 1. Create Dataset
# -------------------------------------------------

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
])


# -------------------------------------------------
# 2. Display Dataset
# -------------------------------------------------

print("Input Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nInput Data:")
print(X)

print("\nTarget Data:")
print(y)


# -------------------------------------------------
# 3. Split Dataset
# -------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)


# -------------------------------------------------
# 4. Feature Scaling
# -------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -------------------------------------------------
# 5. Create FNN Model
# -------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation='relu',
    solver='adam',
    max_iter=2000,
    random_state=42
)


# -------------------------------------------------
# 6. Train Model
# -------------------------------------------------

model.fit(X_train_scaled, y_train)


# -------------------------------------------------
# 7. Test Prediction
# -------------------------------------------------

y_pred = model.predict(X_test_scaled)


# -------------------------------------------------
# 8. Calculate Accuracy
# -------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nTest Accuracy:", accuracy)


# -------------------------------------------------
# 9. Confusion Matrix
# -------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# -------------------------------------------------
# 10. Classification Report
# -------------------------------------------------

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


# -------------------------------------------------
# 11. Test New Applicant
# -------------------------------------------------

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

new_applicant_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_applicant_scaled)

print("\nNew Applicant:", new_applicant)

if prediction[0] == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")
