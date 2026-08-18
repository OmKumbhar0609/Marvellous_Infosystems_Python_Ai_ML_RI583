# Write a Python program using scikit-learn to generate a classification report

from sklearn.metrics import classification_report

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

report = classification_report(actual, predicted)

print(report)