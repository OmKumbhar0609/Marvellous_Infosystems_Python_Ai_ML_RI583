# Salary Prediction and Regression Line

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    'Experience':[1,2,3,4,5],
    'Salary':[20000,25000,30000,35000,40000]
}

df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X,y)

pred = model.predict([[6]])

print("Predicted Salary for 6 Years Experience:", pred[0])

plt.scatter(X,y)
plt.plot(X,model.predict(X))
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction")
plt.show()