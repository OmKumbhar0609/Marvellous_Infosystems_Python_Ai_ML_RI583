# Multiple Linear Regression

from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'SleepHours': [7, 6, 7, 6, 8],
    'Marks': [50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)

X = df[['StudyHours', 'SleepHours']]
y = df['Marks']

model = LinearRegression()
model.fit(X, y)

print("StudyHours Coefficient:", model.coef_[0])
print("SleepHours Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)