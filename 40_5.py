# Without using accuracy_score, manually calculate accuracy.
# Verify whether it matches sklearn accuracy.

from sklearn.metrics import accuracy_score
import pandas as pd

correct = (y_test == y_pred).sum()

total = len(y_test)

accuracy = (correct/total)*100

print("Manual Accuracy =",accuracy,"%")