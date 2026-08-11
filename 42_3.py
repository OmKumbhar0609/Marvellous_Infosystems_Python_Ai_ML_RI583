# Use KNN to predict whether a student passes or fails based on study hours and attendance.

import math

# Dataset
data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

# Accept input from user
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

# Calculate Euclidean distance
distances = []

for hours, attend, result in data:
    distance = math.sqrt(
        (study_hours - hours) ** 2 +
        (attendance - attend) ** 2
    )

    distances.append((distance, result))

# Sort distances
distances.sort(key=lambda item: item[0])

# Select K = 3 nearest neighbors
k = 3
nearest = distances[:k]

# Display nearest neighbors
print("\nNearest Neighbors:")

for distance, result in nearest:
    print("Distance:", round(distance, 2), "Result:", result)

# Majority voting
votes = {}

for distance, result in nearest:
    votes[result] = votes.get(result, 0) + 1

predicted_result = max(votes, key=votes.get)

print("\nPredicted Result:", predicted_result)