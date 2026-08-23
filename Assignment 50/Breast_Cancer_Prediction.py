# Breast Cancer Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

Border = '-' * 70
# --------------------------------------------------
# STEP 1: LOAD DATASET
# --------------------------------------------------

print(Border)
print("STEP 1: LOAD DATASET")
print(Border)

df = pd.read_csv("breast-cancer-wisconsin.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# STEP 2: HANDLE MISSING VALUES
# --------------------------------------------------

print(Border)
print("STEP 2: HANDLE MISSING VALUES")
print(Border)

df.fillna(df.mean(numeric_only=True), inplace=True)

# --------------------------------------------------
# STEP 3: EXPLORATORY DATA ANALYSIS (EDA)
# --------------------------------------------------

print(Border)
print("STEP 3: EXPLORATORY DATA ANALYSIS (EDA)")
print(Border)

print("\nSummary Statistics:")
print(df.describe())

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True),
            cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# --------------------------------------------------
# STEP 4: FEATURES AND TARGET
# --------------------------------------------------

print(Border)
print("STEP 4: FEATURES AND TARGET")
print(Border)

# Replace 'target' with your actual target column name
X = df.drop(["CodeNumber", "CancerType"], axis=1)
y = df["CancerType"]

# --------------------------------------------------
# STEP 5: FEATURE SCALING
# --------------------------------------------------

print(Border)
print("STEP 5: FEATURE SCALING")
print(Border)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------------------------
# STEP 6: TRAIN TEST SPLIT
# --------------------------------------------------

print(Border)
print("STEP 6: TRAIN TEST SPLIT")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# STEP 7: BUILD MACHINE LEARNING MODEL
# --------------------------------------------------

print(Border)
print("STEP 7: BUILD MACHINE LEARNING MODEL")
print(Border)

model = LogisticRegression(max_iter=5000)

model.fit(X_train, y_train)

# --------------------------------------------------
# STEP 8: PREDICTIONS
# --------------------------------------------------

print(Border)
print("STEP 8: PREDICTIONS")
print(Border)

y_pred = model.predict(X_test)

# --------------------------------------------------
# STEP 9: MODEL EVALUATION
# --------------------------------------------------

print(Border)
print("STEP 9: MODEL EVALUATION")
print(Border)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(accuracy)

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

plt.figure(figsize=(6,4))
sns.heatmap(cm,
            annot=True,
            fmt="d",
            cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# --------------------------------------------------
# STEP 10: OBSERVATIONS & CONCLUSION
# --------------------------------------------------

print(Border)
print("STEP 10: OBSERVATIONS & CONCLUSION")
print(Border)

print("\nOBSERVATIONS:")
print("1. Dataset loaded successfully.")
print("2. Missing values handled.")
print("3. Features scaled using StandardScaler.")
print("4. Logistic Regression model trained.")
print("5. Model evaluated using Accuracy, Confusion Matrix and Classification Report.")

print("\nCONCLUSION:")
print("The model predicts whether the tumor is Benign or Malignant based on the given features.")
