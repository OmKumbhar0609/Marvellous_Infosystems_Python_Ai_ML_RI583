# Python program to calculate loss manually

import math

# Actual and predicted values for regression
actual = [10, 20, 30, 40]
predicted = [12, 18, 33, 37]

# Mean Squared Error
def mean_squared_error(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += (a - p) ** 2

    return total / len(actual)


mse = mean_squared_error(actual, predicted)

print("Mean Squared Error:", mse)


# Actual and predicted values for binary classification
actual_class = [1, 0, 1, 1]
predicted_prob = [0.9, 0.2, 0.8, 0.7]

# Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        # Avoid log(0)
        p = max(min(p, 1 - 1e-15), 1e-15)

        total += -(a * math.log(p) +
                   (1 - a) * math.log(1 - p))

    return total / len(actual)


bce = binary_cross_entropy(actual_class, predicted_prob)

print("Binary Cross Entropy:", bce)

# MSE is mainly used for regression problems.

# MSE=\frac{1}{n}\sum(y-\hat y)^2 

# It measures the average squared difference between actual and predicted values.

# Binary Cross Entropy is commonly used for binary classification.

# BCE=-\frac{1}{n}\sum[y\log(p)+(1-y)\log(1-p)]

# It measures how different predicted probabilities are from the actual binary labels.
