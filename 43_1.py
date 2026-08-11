# Design Machine Learning Application
# The application uses a Classification technique.
# The machine learning application follows these steps:
# Get Data
# Clean, Prepare & Manipulate Data
# Train Model
# Test Data
# Calculate Accuracy

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

# Encode categorical data
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()

df["Wether"] = weather_encoder.fit_transform(df["Wether"])
df["Temperature"] = temperature_encoder.fit_transform(df["Temperature"])
df["Play"] = play_encoder.fit_transform(df["Play"])

# Features and target
X = df[["Wether", "Temperature"]]
Y = df["Play"]

# Divide dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.5,
    random_state=42,
    stratify=Y
)

def CheckAccuracy(K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    correct = 0

    for i in range(len(Y_test)):
        if prediction[i] == Y_test.iloc[i]:
            correct += 1

    accuracy = (correct / len(Y_test)) * 100

    print("K =", K)
    print("Accuracy =", accuracy, "%")
    print()

# Check accuracy for different K values
CheckAccuracy(1)
CheckAccuracy(3)
CheckAccuracy(5)