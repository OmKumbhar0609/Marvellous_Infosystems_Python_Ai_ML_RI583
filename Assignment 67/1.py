# Neural Network Model to Predict Customer Churn

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# -------------------------------------------------
# 1. Create Dataset
# -------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
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
# 7. Prediction
# -------------------------------------------------

y_pred = model.predict(X_test_scaled)


# -------------------------------------------------
# 8. Accuracy
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
# 11. Test New Customer
# -------------------------------------------------

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

print("\nNew Customer:", new_customer)

if prediction[0] == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")
