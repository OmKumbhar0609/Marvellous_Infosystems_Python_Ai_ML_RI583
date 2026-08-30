# FRAUDULENT TRANSACTION DETECTION

# =============================================================
# STEP 1: IMPORT LIBRARIES
# =============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt


# ============================================================
# STEP 2: LOAD THE DATASET
# ============================================================

# CHANGE ONLY YOUR CSV FILE NAME HERE
FILE_NAME = "Fraudulent_Transaction_Detection.csv"

df = pd.read_csv(FILE_NAME)

print("\n" + "=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ============================================================
# STEP 3: CHECK MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# STEP 4: DEFINE THE TARGET COLUMN
# ============================================================

# Change this only if your target column has a different name
TARGET_COLUMN = "Fraud"

if TARGET_COLUMN not in df.columns:
    print(f"\nERROR: Target column '{TARGET_COLUMN}' was not found!")
    print("Available columns are:")
    print(df.columns.tolist())
    exit()


# ============================================================
# STEP 5: SEPARATE INPUT AND OUTPUT VARIABLES
# ============================================================

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

print("\n" + "=" * 60)
print("INPUT AND OUTPUT VARIABLES")
print("=" * 60)

print("\nInput Features:")
print(X.columns.tolist())

print("\nTarget:")
print(TARGET_COLUMN)

print("\nTarget Value Counts:")
print(y.value_counts())


# ============================================================
# STEP 6: HANDLE STRING VALUES LIKE '?'
# ============================================================

# Replace common missing value symbols with NaN
X = X.replace(["?", "NA", "N/A", ""], np.nan)


# ============================================================
# STEP 7: IDENTIFY NUMERICAL AND CATEGORICAL COLUMNS
# ============================================================

numerical_features = X.select_dtypes(
    include=["int64", "float64", "int32", "float32"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("\nNumerical Columns:")
print(numerical_features)

print("\nCategorical Columns:")
print(categorical_features)


# ============================================================
# STEP 8: DATA PREPROCESSING
# ============================================================

# Numerical data:
# Fill missing values with median
numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


# Categorical data:
# Fill missing values with most frequent value
# Convert categories into numbers
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# Combine numerical and categorical preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


# ============================================================
# STEP 9: SPLIT TRAINING AND TESTING DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 60)
print("TRAINING AND TESTING DATA")
print("=" * 60)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ============================================================
# STEP 10: CREATE MODELS
# ============================================================

# 1. Decision Tree
decision_tree = DecisionTreeClassifier(
    random_state=42
)


# 2. Bagging Classifier
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=100,
    random_state=42
)


# 3. Random Forest
random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 4. AdaBoost
adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)


# ============================================================
# STEP 11: CREATE VOTING CLASSIFIER
# ============================================================

# We use three different models for voting
logistic = LogisticRegression(
    max_iter=1000,
    random_state=42
)

voting_classifier = VotingClassifier(
    estimators=[
        ("lr", logistic),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("rf", RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ))
    ],
    voting="hard"
)


# ============================================================
# STEP 12: CREATE PIPELINES
# ============================================================

models = {
    "Decision Tree": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", decision_tree)
        ]
    ),

    "Bagging": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", bagging)
        ]
    ),

    "Random Forest": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", random_forest)
        ]
    ),

    "AdaBoost": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", adaboost)
        ]
    ),

    "Voting": Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", voting_classifier)
        ]
    )
}


# ============================================================
# STEP 13: TRAIN AND EVALUATE ALL MODELS
# ============================================================

results = {}

print("\n" + "=" * 60)
print("MODEL TRAINING AND EVALUATION")
print("=" * 60)


for name, model in models.items():

    print("\n" + "-" * 60)
    print(f"TRAINING: {name}")
    print("-" * 60)

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # Store results
    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1
    }

    # Print metrics
    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    # Plot Confusion Matrix
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot()

    plt.title(f"Confusion Matrix - {name}")

    plt.show()


# ============================================================
# STEP 14: FINAL COMPARISON TABLE
# ============================================================

results_df = pd.DataFrame(results).T

results_df = results_df.sort_values(
    by="F1",
    ascending=False
)

print("\n" + "=" * 60)
print("FINAL MODEL COMPARISON")
print("=" * 60)

print(results_df)


# ============================================================
# STEP 15: SAVE COMPARISON RESULTS
# ============================================================

results_df.to_csv(
    "fraud_model_comparison.csv"
)

print("\nComparison table saved as:")
print("fraud_model_comparison.csv")


# ============================================================
# STEP 16: FIND THE BEST MODEL
# ============================================================

best_model = results_df["F1"].idxmax()

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Best Model: {best_model}")

print(f"Best F1 Score: {results_df.loc[best_model, 'F1']:.4f}")

print(f"Best Accuracy: {results_df.loc[best_model, 'Accuracy']:.4f}")

print("\nPROGRAM COMPLETED SUCCESSFULLY!")
