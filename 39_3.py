# Calculate model accuracy using accuracy_score. Display the result in percentage.

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy =", accuracy * 100, "%")