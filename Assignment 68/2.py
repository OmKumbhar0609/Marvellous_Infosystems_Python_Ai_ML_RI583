# ReLU and Max Pooling

feature_map = [
    [3,  3,  3],
    [0,  0,  0],
    [-3, -3, -3]
]

# -----------------------------------
# Step 1: Display Feature Map
# -----------------------------------

print("Original Feature Map:")

for row in feature_map:
    print(row)


# -----------------------------------
# Step 2: Apply ReLU
# -----------------------------------

relu_output = []

for row in feature_map:

    new_row = []

    for value in row:

        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)


print("\nAfter ReLU:")

for row in relu_output:
    print(row)


# -----------------------------------
# Step 3: Apply 2x2 Max Pooling
# -----------------------------------

pool_size = 2

pooled_output = []

rows = len(relu_output)
cols = len(relu_output[0])

for i in range(rows - pool_size + 1):

    row = []

    for j in range(cols - pool_size + 1):

        maximum = relu_output[i][j]

        for x in range(pool_size):
            for y in range(pool_size):

                value = relu_output[i + x][j + y]

                if value > maximum:
                    maximum = value

        row.append(maximum)

    pooled_output.append(row)


# -----------------------------------
# Step 4: Display Max Pooling Output
# -----------------------------------

print("\nAfter 2x2 Max Pooling:")

for row in pooled_output:
    print(row)
