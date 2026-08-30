# CUSTOMER LOAN APPROVAL USING VOTING CLASSIFICATION

# --------------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# --------------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score


# --------------------------------------------------------------
# STEP 2: LOAD THE DATASET
# --------------------------------------------------------------

print("-" * 70)
print("STEP 1: LOAD DATASET")
print("-" * 70)

# Change only the CSV file name if required
df = pd.read_csv("Customer_Loan_Approval.csv")

print("\nDataset Loaded Successfully!")
print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)


# --------------------------------------------------------------
# STEP 3: CHECK FOR MISSING VALUES
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 2: CHECK FOR MISSING VALUES")
print("-" * 70)

print("\nMissing Values Before Handling:")
print(df.isnull().sum())


# --------------------------------------------------------------
# STEP 4: HANDLE MISSING VALUES
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 3: HANDLE MISSING VALUES")
print("-" * 70)

# Input columns
features = [
    "Age",
    "Income",
    "CreditScore",
    "ExistingLoan",
    "EmploymentExperience",
    "LoanAmount"
]

# Convert feature columns to numeric
for column in features:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Replace missing values with the median
imputer = SimpleImputer(strategy="median")

df[features] = imputer.fit_transform(df[features])

print("\nMissing Values After Handling:")
print(df.isnull().sum())


# --------------------------------------------------------------
# STEP 5: SEPARATE INPUT AND OUTPUT VARIABLES
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 4: SEPARATE INPUT AND OUTPUT VARIABLES")
print("-" * 70)

# Input variables
X = df[features]

# Target variable
y = df["LoanApproved"]

print("\nInput Variables:")
print(X.head())

print("\nOutput Variable:")
print(y.head())


# --------------------------------------------------------------
# STEP 6: SPLIT THE DATASET
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 5: TRAIN-TEST SPLIT")
print("-" * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# --------------------------------------------------------------
# STEP 7: FEATURE SCALING
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 6: FEATURE SCALING")
print("-" * 70)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature Scaling Completed Successfully!")


# --------------------------------------------------------------
# STEP 8: TRAIN LOGISTIC REGRESSION
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 7: LOGISTIC REGRESSION")
print("-" * 70)

lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train_scaled, y_train)

lr_prediction = lr_model.predict(X_test_scaled)

lr_accuracy = accuracy_score(y_test, lr_prediction)

print("\nLogistic Regression Accuracy:",
      round(lr_accuracy * 100, 2), "%")


# --------------------------------------------------------------
# STEP 9: TRAIN DECISION TREE
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 8: DECISION TREE")
print("-" * 70)

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

dt_prediction = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_prediction)

print("\nDecision Tree Accuracy:",
      round(dt_accuracy * 100, 2), "%")


# --------------------------------------------------------------
# STEP 10: TRAIN K-NEAREST NEIGHBORS
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 9: K-NEAREST NEIGHBORS")
print("-" * 70)

knn_model = KNeighborsClassifier(
    n_neighbors=5
)

knn_model.fit(X_train_scaled, y_train)

knn_prediction = knn_model.predict(X_test_scaled)

knn_accuracy = accuracy_score(y_test, knn_prediction)

print("\nKNN Accuracy:",
      round(knn_accuracy * 100, 2), "%")


# --------------------------------------------------------------
# STEP 11: CREATE HARD VOTING CLASSIFIER
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 10: HARD VOTING CLASSIFIER")
print("-" * 70)

hard_voting = VotingClassifier(
    estimators=[
        ("Logistic Regression", lr_model),
        ("Decision Tree", dt_model),
        ("KNN", knn_model)
    ],
    voting="hard"
)

# Voting classifier will be trained on scaled data
hard_voting.fit(X_train_scaled, y_train)

hard_prediction = hard_voting.predict(X_test_scaled)

hard_accuracy = accuracy_score(
    y_test,
    hard_prediction
)

print("\nHard Voting Accuracy:",
      round(hard_accuracy * 100, 2), "%")


# --------------------------------------------------------------
# STEP 12: CREATE SOFT VOTING CLASSIFIER
# --------------------------------------------------------------

print("\n" + "-" * 70)
print("STEP 11: SOFT VOTING CLASSIFIER")
print("-" * 70)

soft_voting = VotingClassifier(
    estimators=[
        ("Logistic Regression", lr_model),
        ("Decision Tree", dt_model),
        ("KNN", knn_model)
    ],
    voting="soft"
)

soft_voting.fit(X_train_scaled, y_train)

soft_prediction = soft_voting.predict(X_test_scaled)

soft_accuracy = accuracy_score(
    y_test,
    soft_prediction
)

print("\nSoft Voting Accuracy:",
      round(soft_accuracy * 100, 2), "%")


# --------------------------------------------------------------
# STEP 13: COMPARE ALL MODELS
# --------------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL MODEL COMPARISON")
print("=" * 70)

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    
    "Accuracy": [
        round(lr_accuracy * 100, 2),
        round(dt_accuracy * 100, 2),
        round(knn_accuracy * 100, 2),
        round(hard_accuracy * 100, 2),
        round(soft_accuracy * 100, 2)
    ]
})

print(results.to_string(index=False))


# --------------------------------------------------------------
# STEP 14: FIND THE BEST MODEL
# --------------------------------------------------------------

best_model = results.loc[
    results["Accuracy"].idxmax()
]

print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print("\nModel Name:", best_model["Model"])
print("Best Accuracy:", best_model["Accuracy"], "%")


# --------------------------------------------------------------
# CONCLUSION
# --------------------------------------------------------------

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)

print("""
Three individual Machine Learning models were trained:
1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors

Two ensemble models were also created:
4. Hard Voting Classifier
5. Soft Voting Classifier

The final model comparison is displayed above.
The model with the highest accuracy is selected as the best model.
""")
