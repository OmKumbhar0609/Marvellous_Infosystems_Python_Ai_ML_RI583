# Predict Marks for 6 Study Hours

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([50, 55, 60, 65, 70])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])