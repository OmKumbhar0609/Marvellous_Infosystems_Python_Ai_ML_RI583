# Advertisement Sales Prediction using Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

border = "-"*100
print(border)

# Create Dataset
df = pd.read_csv("Advertising.csv")

print("Dataset:")
print(df.head())

# Display Dataset
print("Dataset:")
print(df)

# Step 1: Get Data
print(border)
print("Step 1: Get Data")
print(border)

X = df[['TV', 'radio', 'newspaper']]
y = df['sales']
print("Data Loaded Successfully...")

# Step 2: Clean, Prepare and Manipulate Data
print(border)
print("Step 2: Clean, Prepare and Manipulate Data")
print(border)

print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Train Data
print(border)
print("Step 3: Train Data")
print(border)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
print("Data Trained Successfully...")

# Step 4: Test Data
print(border)
print("Step 4: Test Data")
print(border)

y_pred = model.predict(X_test)
print("Data Tested Successfully...")

# Step 5: Display Predicted and Actual Values
print(border)
print("Step 5: Display Predicted and Actual Values")
print(border)

result = pd.DataFrame({
    'Actual Sales': y_test.values,
    'Predicted Sales': y_pred
})

print("\nActual vs Predicted Sales:")
print(result)
print(border)
