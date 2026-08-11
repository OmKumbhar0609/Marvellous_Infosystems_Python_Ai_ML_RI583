# The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.

import math

# Dataset
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# New point
x = 2
y = 2

# Calculate distances
distances = []

for point, px, py, label in data:
    distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)
    distances.append((point, distance, label))

# Sort distances
distances.sort(key=lambda item: item[1])

print("Prediction Results\n")

for k in [1, 3, 5]:

    nearest = distances[:k]

    votes = {}

    for point, distance, label in nearest:
        votes[label] = votes.get(label, 0) + 1

    predicted_class = max(votes, key=votes.get)

    print("K =", k, "->", predicted_class)