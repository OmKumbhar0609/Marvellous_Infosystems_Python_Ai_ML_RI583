# Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.

import math

# Dataset
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

# Accept new point from user
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

# Calculate Euclidean distance
distances = []

for point, px, py, label in data:
    distance = math.sqrt((x - px) ** 2 + (y - py) ** 2)
    distances.append((point, distance, label))

# Sort distances
distances.sort(key=lambda item: item[1])

# Select K = 3 nearest neighbors
k = 3
nearest = distances[:k]

print("\nNearest Neighbors:")

for point, distance, label in nearest:
    print(point, "- Distance:", round(distance, 2))

# Majority voting
votes = {}

for point, distance, label in nearest:
    votes[label] = votes.get(label, 0) + 1

predicted_class = max(votes, key=votes.get)

print("\nPredicted Class:", predicted_class)