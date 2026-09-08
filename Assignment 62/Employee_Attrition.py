# ============================================================
# Employee Attrition Prediction
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

import matplotlib.pyplot as plt


# ============================================================
# STEP 1: LOAD DATASET
# ============================================================

# CHANGE ONLY THIS FILE NAME
FILE_NAME = "Employee_Attrition.csv"

print("=" * 70)
print("EMPLOYEE ATTRITION PREDICTION USING DEEP LEARNING")
print("=" * 70)

df = pd.read_csv(FILE_NAME)

print("\nSTEP 1: DATASET LOADED")
print("-" * 70)

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())


# ============================================================
# STEP 2: HANDLE MISSING VALUES
# ============================================================

print("\nSTEP 2: CHECKING MISSING VALUES")
print("-" * 70)

# Replace '?' with NaN
df = df.replace("?", np.nan)

print(df.isnull().sum())

# Convert numerical columns to numeric
numerical_columns = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "NumCompaniesWorked",
    "TrainingTimesLastYear"
]

for column in numerical_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Fill missing numerical values with median
for column in numerical_columns:
    if column in df.columns:
        df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = ["OverTime", "Attrition"]

for column in categorical_columns:
    if column in df.columns:
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ============================================================
# STEP 3: IDENTIFY FEATURES
# ============================================================

print("\nSTEP 3: IDENTIFYING FEATURES")
print("-" * 70)

features = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "OverTime",
    "NumCompaniesWorked",
    "TrainingTimesLastYear"
]

target = "Attrition"

print("Input Features:")
print(features)

print("\nTarget:")
print(target)


# ============================================================
# STEP 4: CONVERT CATEGORICAL FEATURES
# ============================================================

print("\nSTEP 4: CONVERTING CATEGORICAL FEATURES")
print("-" * 70)

# Convert OverTime
# Yes = 1
# No  = 0

df["OverTime"] = df["OverTime"].map({
    "Yes": 1,
    "No": 0
})

# Convert Attrition
# Yes = 1 -> Employee likely to leave
# No  = 0 -> Employee likely to stay

df["Attrition"] = df["Attrition"].map({
    "Yes": 1,
    "No": 0
})

# Make sure there are no missing values after mapping
df["OverTime"] = df["OverTime"].fillna(0)
df["Attrition"] = df["Attrition"].fillna(0)

print("\nCategorical features converted successfully.")


# ============================================================
# STEP 5: SEPARATE INPUT AND OUTPUT
# ============================================================

print("\nSTEP 5: SEPARATING INPUT AND OUTPUT")
print("-" * 70)

X = df[features]
y = df[target]

print("Input Shape :", X.shape)
print("Output Shape:", y.shape)


# ============================================================
# STEP 6: TRAIN TEST SPLIT
# ============================================================

print("\nSTEP 6: SPLITTING DATASET")
print("-" * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training Records:", X_train.shape[0])
print("Testing Records :", X_test.shape[0])


# ============================================================
# STEP 7: FEATURE SCALING
# ============================================================

print("\nSTEP 7: FEATURE SCALING")
print("-" * 70)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Feature scaling completed.")


# ============================================================
# STEP 8: CREATE MLP CLASSIFIER
# ============================================================

print("\nSTEP 8: CREATING MLP CLASSIFIER")
print("-" * 70)

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=500,
    random_state=42,
    early_stopping=False
)

print("MLP Architecture:")
print("Input Layer")
print("     ↓")
print("Hidden Layer 1 : 32 Neurons")
print("     ↓")
print("Hidden Layer 2 : 16 Neurons")
print("     ↓")
print("Output Layer   : 1 Neuron")


# ============================================================
# STEP 9: TRAIN NETWORK
# ============================================================

print("\nSTEP 9: TRAINING NETWORK")
print("-" * 70)

model.fit(X_train_scaled, y_train)

print("Training completed successfully.")


# ============================================================
# STEP 10: NUMBER OF ITERATIONS
# ============================================================

print("\nSTEP 10: TRAINING ITERATIONS")
print("-" * 70)

print("Number of iterations required:", model.n_iter_)


# ============================================================
# STEP 11: TRAINING ACCURACY
# ============================================================

print("\nSTEP 11: TRAINING ACCURACY")
print("-" * 70)

train_prediction = model.predict(X_train_scaled)

training_accuracy = accuracy_score(
    y_train,
    train_prediction
)

print("Training Accuracy:",
      round(training_accuracy * 100, 2), "%")


# ============================================================
# STEP 12: TESTING ACCURACY
# ============================================================

print("\nSTEP 12: TESTING ACCURACY")
print("-" * 70)

test_prediction = model.predict(X_test_scaled)

testing_accuracy = accuracy_score(
    y_test,
    test_prediction
)

print("Testing Accuracy:",
      round(testing_accuracy * 100, 2), "%")


# ============================================================
# STEP 13: CONFUSION MATRIX
# ============================================================

print("\nSTEP 13: CONFUSION MATRIX")
print("-" * 70)

cm = confusion_matrix(
    y_test,
    test_prediction
)

print(cm)

print("\nConfusion Matrix Format:")
print("[[True Negative  False Positive]")
print(" [False Negative True Positive ]]")

print("\nDetailed Classification Report:")
print(
    classification_report(
        y_test,
        test_prediction,
        target_names=["Stay", "Leave"]
    )
)


# ============================================================
# STEP 14: LOSS CURVE
# ============================================================

print("\nSTEP 14: DISPLAYING LOSS CURVE")
print("-" * 70)

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_,
    linewidth=2
)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.grid(True)

plt.show()


# ============================================================
# STEP 15: PREDICT ATTRITION FUNCTION
# ============================================================

def PredictAttrition(employee_data):
    """
    Predict whether an employee is likely to stay or leave.

    employee_data should contain values in this order:

    Age
    MonthlyIncome
    YearsAtCompany
    TotalWorkingYears
    DistanceFromHome
    JobSatisfaction
    WorkLifeBalance
    OverTime
    NumCompaniesWorked
    TrainingTimesLastYear
    """

    # Convert input into DataFrame
    employee_df = pd.DataFrame(
        [employee_data],
        columns=features
    )

    # Convert OverTime
    employee_df["OverTime"] = employee_df["OverTime"].map({
        "Yes": 1,
        "No": 0
    })

    # Handle numeric OverTime if 0 or 1 is provided
    employee_df["OverTime"] = employee_df["OverTime"].fillna(0)

    # Scale input
    employee_scaled = scaler.transform(employee_df)

    # Prediction
    prediction = model.predict(employee_scaled)[0]

    # Probability
    probability = model.predict_proba(employee_scaled)[0]

    if prediction == 1:

        print("\nPrediction: Employee is likely to LEAVE.")

        print(
            "Probability of Leaving:",
            round(probability[1] * 100, 2),
            "%"
        )

        return 1

    else:

        print("\nPrediction: Employee is likely to STAY.")

        print(
            "Probability of Staying:",
            round(probability[0] * 100, 2),
            "%"
        )

        return 0


# ============================================================
# STEP 16: TEST WITH 5 NEW EMPLOYEE RECORDS
# ============================================================

print("\n")
print("=" * 70)
print("STEP 16: TESTING WITH NEW EMPLOYEE RECORDS")
print("=" * 70)


# Employee 1
employee1 = [
    25,       # Age
    3000,     # MonthlyIncome
    1,        # YearsAtCompany
    2,        # TotalWorkingYears
    20,       # DistanceFromHome
    2,        # JobSatisfaction
    2,        # WorkLifeBalance
    "Yes",    # OverTime
    3,        # NumCompaniesWorked
    2         # TrainingTimesLastYear
]

print("\nEmployee 1:")
PredictAttrition(employee1)


# Employee 2
employee2 = [
    40,
    8000,
    10,
    15,
    5,
    4,
    4,
    "No",
    2,
    4
]

print("\nEmployee 2:")
PredictAttrition(employee2)


# Employee 3
employee3 = [
    30,
    4500,
    3,
    6,
    15,
    2,
    2,
    "Yes",
    4,
    3
]

print("\nEmployee 3:")
PredictAttrition(employee3)


# Employee 4
employee4 = [
    50,
    10000,
    20,
    25,
    3,
    4,
    4,
    "No",
    1,
    5
]

print("\nEmployee 4:")
PredictAttrition(employee4)


# Employee 5
employee5 = [
    28,
    3500,
    2,
    4,
    25,
    1,
    1,
    "Yes",
    5,
    2
]

print("\nEmployee 5:")
PredictAttrition(employee5)


# ============================================================
# STEP 17: OVERFITTING / UNDERFITTING
# ============================================================

print("\n")
print("=" * 70)
print("STEP 17: OVERFITTING / UNDERFITTING ANALYSIS")
print("=" * 70)

difference = training_accuracy - testing_accuracy

print(
    "\nTraining Accuracy:",
    round(training_accuracy * 100, 2),
    "%"
)

print(
    "Testing Accuracy :",
    round(testing_accuracy * 100, 2),
    "%"
)

print(
    "Difference        :",
    round(difference * 100, 2),
    "%"
)


if training_accuracy < 0.70 and testing_accuracy < 0.70:

    print("\nResult: The model may be UNDERFITTING.")

elif difference > 0.10:

    print("\nResult: The model may be OVERFITTING.")

else:

    print("\nResult: The model appears to be reasonably balanced.")


# ============================================================
# FINAL RESULT
# ============================================================

print("\n")
print("=" * 70)
print("FINAL RESULT")
print("=" * 70)

print(
    "Training Accuracy :",
    round(training_accuracy * 100, 2),
    "%"
)

print(
    "Testing Accuracy  :",
    round(testing_accuracy * 100, 2),
    "%"
)

print(
    "Iterations         :",
    model.n_iter_
)

print("\nEmployee Attrition Prediction completed successfully.")
print("=" * 70)
