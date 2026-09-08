# ============================================================
# LOAN DEFAULT PREDICTION 
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# STEP 1: LOAD DATASET
# ============================================================

# CHANGE ONLY THIS FILE NAME
FILE_NAME = "Loan_Default.csv"

print("=" * 70)
print("LOAN DEFAULT PREDICTION USING MULTI-LAYER PERCEPTRON")
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
# STEP 2: BASIC EXPLORATORY ANALYSIS
# ============================================================

print("\nSTEP 2: EXPLORATORY DATA ANALYSIS")
print("-" * 70)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe(include="all"))


# ============================================================
# STEP 3: HANDLE MISSING VALUES
# ============================================================

print("\nSTEP 3: CHECKING MISSING VALUES")
print("-" * 70)

# Replace common missing-value symbols
df = df.replace(["?", "NA", "N/A", "na", "null", "NULL", ""], np.nan)

print("\nMissing values before handling:")
print(df.isnull().sum())


# ============================================================
# IDENTIFY COLUMNS
# ============================================================

required_columns = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm",
    "PreviousDefault",
    "HomeOwnership",
    "Default"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("\nERROR: The following columns are missing from CSV:")
    print(missing_columns)
    print("\nYour CSV column names are:")
    print(df.columns.tolist())
    raise SystemExit


# ============================================================
# NUMERICAL COLUMNS
# ============================================================

numerical_columns = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm"
]


# Convert numerical columns to numeric
for column in numerical_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# Fill numerical missing values with median
for column in numerical_columns:

    df[column] = df[column].fillna(
        df[column].median()
    )


# ============================================================
# CATEGORICAL COLUMNS
# ============================================================

categorical_columns = [
    "PreviousDefault",
    "HomeOwnership"
]

# Fill categorical missing values with mode
for column in categorical_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            df[column].mode()[0]
        )


# ============================================================
# TARGET COLUMN
# ============================================================

# Convert target to numeric
df["Default"] = pd.to_numeric(
    df["Default"],
    errors="coerce"
)

# Remove records where target is missing
df = df.dropna(subset=["Default"])

df["Default"] = df["Default"].astype(int)


print("\nMissing values after handling:")
print(df.isnull().sum())


# ============================================================
# STEP 4: CHECK TARGET CLASS BALANCE
# ============================================================

print("\nSTEP 4: CHECKING TARGET CLASS BALANCE")
print("-" * 70)

print("\nDefault Value Counts:")
print(df["Default"].value_counts())

print("\nDefault Percentages:")
print(
    df["Default"].value_counts(normalize=True) * 100
)

print("\nTarget Meaning:")
print("0 = Low default risk")
print("1 = High default risk")


# ============================================================
# STEP 5: ENCODE CATEGORICAL VARIABLES
# ============================================================

print("\nSTEP 5: ENCODING CATEGORICAL VARIABLES")
print("-" * 70)


# ------------------------------------------------------------
# PreviousDefault
# Yes = 1
# No  = 0
# ------------------------------------------------------------

if df["PreviousDefault"].dtype == "object":

    df["PreviousDefault"] = (
        df["PreviousDefault"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "yes": 1,
            "no": 0
        })
    )

else:

    df["PreviousDefault"] = pd.to_numeric(
        df["PreviousDefault"],
        errors="coerce"
    )


# Fill any remaining missing values
df["PreviousDefault"] = df["PreviousDefault"].fillna(0)


# ------------------------------------------------------------
# HomeOwnership
# Use One-Hot Encoding
# ------------------------------------------------------------

df = pd.get_dummies(
    df,
    columns=["HomeOwnership"],
    dtype=int
)


print("\nCategorical variables encoded successfully.")

print("\nColumns after encoding:")
print(df.columns.tolist())


# ============================================================
# STEP 6: SEPARATE X AND Y
# ============================================================

print("\nSTEP 6: SEPARATING INPUT AND OUTPUT")
print("-" * 70)

target_column = "Default"

X = df.drop(
    columns=[target_column]
)

y = df[target_column]


print("Input Shape :", X.shape)
print("Output Shape:", y.shape)

print("\nInput Features:")
print(X.columns.tolist())


# ============================================================
# STEP 7: TRAIN TEST SPLIT
# ============================================================

print("\nSTEP 7: TRAINING AND TESTING DATA")
print("-" * 70)

# Stratified splitting is used because Default is a
# classification target and class proportions should
# remain similar in training and testing data.

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
# STEP 8: FEATURE SCALING
# ============================================================

print("\nSTEP 8: FEATURE SCALING")
print("-" * 70)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

print("Feature scaling completed.")


# ============================================================
# STEP 9: CREATE MLP CLASSIFIER
# ============================================================

print("\nSTEP 9: CREATING MLP CLASSIFIER")
print("-" * 70)

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print("""
MLP Architecture:

Input Layer
     |
     v
Hidden Layer 1 : 32 neurons
     |
     v
Hidden Layer 2 : 16 neurons
     |
     v
Output Layer : 1 neuron
""")


# ============================================================
# STEP 10: TRAIN MODEL
# ============================================================

print("\nSTEP 10: TRAINING MODEL")
print("-" * 70)

model.fit(
    X_train_scaled,
    y_train
)

print("Model training completed successfully.")


# ============================================================
# STEP 11: NUMBER OF ITERATIONS
# ============================================================

print("\nSTEP 11: NUMBER OF ITERATIONS")
print("-" * 70)

print(
    "Number of iterations required:",
    model.n_iter_
)


# ============================================================
# STEP 12: CALCULATE ACCURACY
# ============================================================

print("\nSTEP 12: MODEL ACCURACY")
print("-" * 70)


# Training prediction
train_prediction = model.predict(
    X_train_scaled
)

# Testing prediction
test_prediction = model.predict(
    X_test_scaled
)


training_accuracy = accuracy_score(
    y_train,
    train_prediction
)

testing_accuracy = accuracy_score(
    y_test,
    test_prediction
)


print(
    "Training Accuracy:",
    round(training_accuracy * 100, 2),
    "%"
)

print(
    "Testing Accuracy :",
    round(testing_accuracy * 100, 2),
    "%"
)


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

print("""
Confusion Matrix:

[[ True Negative   False Positive ]
 [ False Negative  True Positive  ]]
""")


# ============================================================
# STEP 14: CLASSIFICATION REPORT
# ============================================================

print("\nSTEP 14: CLASSIFICATION REPORT")
print("-" * 70)

print(
    classification_report(
        y_test,
        test_prediction,
        target_names=[
            "Low Default Risk",
            "High Default Risk"
        ],
        zero_division=0
    )
)


# ============================================================
# STEP 15: PRECISION, RECALL AND F1 SCORE
# ============================================================

print("\nSTEP 15: PRECISION, RECALL AND F1 SCORE")
print("-" * 70)

precision = precision_score(
    y_test,
    test_prediction,
    zero_division=0
)

recall = recall_score(
    y_test,
    test_prediction,
    zero_division=0
)

f1 = f1_score(
    y_test,
    test_prediction,
    zero_division=0
)


print(
    "Precision:",
    round(precision, 4)
)

print(
    "Recall:",
    round(recall, 4)
)

print(
    "F1 Score:",
    round(f1, 4)
)


# ============================================================
# STEP 16: PLOT TRAINING LOSS
# ============================================================

print("\nSTEP 16: TRAINING LOSS")
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
# STEP 17: PREDICTION FUNCTION
# ============================================================

def PredictDefault(applicant_data):
    """
    Predict loan default risk for a new applicant.

    applicant_data must contain:

    Age
    Income
    LoanAmount
    CreditScore
    EmploymentYears
    ExistingLoans
    MonthlyDebt
    LoanTerm
    PreviousDefault
    HomeOwnership
    """


    # Create DataFrame
    applicant = pd.DataFrame(
        [applicant_data]
    )


    # --------------------------------------------------------
    # Convert PreviousDefault
    # --------------------------------------------------------

    if applicant["PreviousDefault"].dtype == "object":

        applicant["PreviousDefault"] = (
            applicant["PreviousDefault"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map({
                "yes": 1,
                "no": 0
            })
        )

    else:

        applicant["PreviousDefault"] = pd.to_numeric(
            applicant["PreviousDefault"],
            errors="coerce"
        )

    applicant["PreviousDefault"] = (
        applicant["PreviousDefault"].fillna(0)
    )


    # --------------------------------------------------------
    # Convert HomeOwnership
    # --------------------------------------------------------

    applicant = pd.get_dummies(
        applicant,
        columns=["HomeOwnership"],
        dtype=int
    )


    # --------------------------------------------------------
    # Make new record have exactly the same columns
    # as training data
    # --------------------------------------------------------

    applicant = applicant.reindex(
        columns=X.columns,
        fill_value=0
    )


    # --------------------------------------------------------
    # Scale
    # --------------------------------------------------------

    applicant_scaled = scaler.transform(
        applicant
    )


    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = model.predict(
        applicant_scaled
    )[0]


    probability = model.predict_proba(
        applicant_scaled
    )[0]


    # --------------------------------------------------------
    # Display result
    # --------------------------------------------------------

    print("\nApplicant Prediction")
    print("-" * 40)

    if prediction == 1:

        print("Prediction: HIGH DEFAULT RISK")

        print(
            "Default Probability:",
            round(probability[1] * 100, 2),
            "%"
        )

        print(
            "Low Risk Probability:",
            round(probability[0] * 100, 2),
            "%"
        )

    else:

        print("Prediction: LOW DEFAULT RISK")

        print(
            "Default Probability:",
            round(probability[1] * 100, 2),
            "%"
        )

        print(
            "Low Risk Probability:",
            round(probability[0] * 100, 2),
            "%"
        )

    return prediction


# ============================================================
# STEP 18: TEST NEW LOAN APPLICANTS
# ============================================================

print("\n")
print("=" * 70)
print("STEP 18: TESTING NEW LOAN APPLICANTS")
print("=" * 70)


# ------------------------------------------------------------
# Applicant 1
# ------------------------------------------------------------

applicant1 = {
    "Age": 25,
    "Income": 30000,
    "LoanAmount": 5000,
    "CreditScore": 750,
    "EmploymentYears": 4,
    "ExistingLoans": 1,
    "MonthlyDebt": 500,
    "LoanTerm": 24,
    "PreviousDefault": "No",
    "HomeOwnership": "Own"
}

print("\nApplicant 1:")
PredictDefault(applicant1)


# ------------------------------------------------------------
# Applicant 2
# ------------------------------------------------------------

applicant2 = {
    "Age": 45,
    "Income": 25000,
    "LoanAmount": 30000,
    "CreditScore": 580,
    "EmploymentYears": 3,
    "ExistingLoans": 4,
    "MonthlyDebt": 2500,
    "LoanTerm": 60,
    "PreviousDefault": "Yes",
    "HomeOwnership": "Rent"
}

print("\nApplicant 2:")
PredictDefault(applicant2)


# ------------------------------------------------------------
# Applicant 3
# ------------------------------------------------------------

applicant3 = {
    "Age": 35,
    "Income": 50000,
    "LoanAmount": 10000,
    "CreditScore": 720,
    "EmploymentYears": 10,
    "ExistingLoans": 1,
    "MonthlyDebt": 700,
    "LoanTerm": 36,
    "PreviousDefault": "No",
    "HomeOwnership": "Mortgage"
}

print("\nApplicant 3:")
PredictDefault(applicant3)


# ------------------------------------------------------------
# Applicant 4
# ------------------------------------------------------------

applicant4 = {
    "Age": 52,
    "Income": 60000,
    "LoanAmount": 15000,
    "CreditScore": 780,
    "EmploymentYears": 20,
    "ExistingLoans": 0,
    "MonthlyDebt": 400,
    "LoanTerm": 24,
    "PreviousDefault": "No",
    "HomeOwnership": "Own"
}

print("\nApplicant 4:")
PredictDefault(applicant4)


# ------------------------------------------------------------
# Applicant 5
# ------------------------------------------------------------

applicant5 = {
    "Age": 30,
    "Income": 22000,
    "LoanAmount": 25000,
    "CreditScore": 590,
    "EmploymentYears": 2,
    "ExistingLoans": 3,
    "MonthlyDebt": 2200,
    "LoanTerm": 60,
    "PreviousDefault": "Yes",
    "HomeOwnership": "Rent"
}

print("\nApplicant 5:")
PredictDefault(applicant5)


# ============================================================
# STEP 19: OVERFITTING / UNDERFITTING CHECK
# ============================================================

print("\n")
print("=" * 70)
print("OVERFITTING / UNDERFITTING ANALYSIS")
print("=" * 70)

difference = (
    training_accuracy -
    testing_accuracy
)

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
    "Difference:",
    round(difference * 100, 2),
    "%"
)


if training_accuracy < 0.70 and testing_accuracy < 0.70:

    print(
        "\nThe model may be UNDERFITTING."
    )

elif difference > 0.10:

    print(
        "\nThe model may be OVERFITTING."
    )

else:

    print(
        "\nThe model appears reasonably balanced."
    )


# ============================================================
# HYPERPARAMETER EXPERIMENTS
# ============================================================

print("\n")
print("=" * 70)
print("HYPERPARAMETER EXPERIMENTS")
print("=" * 70)


# ============================================================
# EXPERIMENT 1: ACTIVATION FUNCTION
# ============================================================

print("\n")
print("EXPERIMENT 1 - ACTIVATION FUNCTION")
print("-" * 70)

activation_functions = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

activation_results = []


for activation in activation_functions:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    activation_results.append(
        [activation, accuracy]
    )

    print(
        activation,
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# ============================================================
# EXPERIMENT 2: HIDDEN LAYERS
# ============================================================

print("\n")
print("EXPERIMENT 2 - HIDDEN LAYERS")
print("-" * 70)

hidden_layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

hidden_results = []


for layers in hidden_layers:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    hidden_results.append(
        [layers, accuracy]
    )

    print(
        "Hidden Layers:",
        layers,
        "| Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# ============================================================
# EXPERIMENT 3: LEARNING RATE
# ============================================================

print("\n")
print("EXPERIMENT 3 - LEARNING RATE")
print("-" * 70)

learning_rates = [
    0.0001,
    0.001,
    0.01
]

learning_rate_results = []


for learning_rate in learning_rates:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=learning_rate,
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy = accuracy_score(
        y_test,
        prediction
    )

    learning_rate_results.append(
        [learning_rate, accuracy]
    )

    print(
        "Learning Rate:",
        learning_rate,
        "| Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(
    "\nBase MLP Training Accuracy:",
    round(training_accuracy * 100, 2),
    "%"
)

print(
    "Base MLP Testing Accuracy :",
    round(testing_accuracy * 100, 2),
    "%"
)

print(
    "Precision:",
    round(precision, 4)
)

print(
    "Recall:",
    round(recall, 4)
)

print(
    "F1 Score:",
    round(f1, 4)
)

print(
    "Iterations:",
    model.n_iter_
)

print("\nProgram completed successfully.")

print("=" * 70)
