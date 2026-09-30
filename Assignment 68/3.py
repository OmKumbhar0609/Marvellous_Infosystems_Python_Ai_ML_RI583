# Demonstrate Flattening

matrix = [
    [6, 4],
    [8, 6]
]

# -----------------------------------
# Step 1: Display 2D Matrix
# -----------------------------------

print("Input Matrix:")

for row in matrix:
    print(row)


# -----------------------------------
# Step 2: Flatten Matrix
# -----------------------------------

flatten_output = []

for row in matrix:

    for value in row:

        flatten_output.append(value)


print("\nFlatten Output:")
print(flatten_output)


# -----------------------------------
# Step 3: Fully Connected Layer
# -----------------------------------

weights = [0.2, 0.3, 0.4, 0.1]
bias = 1

weighted_sum = 0

for i in range(len(flatten_output)):

    weighted_sum += flatten_output[i] * weights[i]

weighted_sum += bias


print("\nWeights:")
print(weights)

print("\nBias:", bias)

print("\nWeighted Sum:", weighted_sum)


# -----------------------------------
# Step 4: Final Output
# -----------------------------------

print("\nFinal Output:", weighted_sum)
