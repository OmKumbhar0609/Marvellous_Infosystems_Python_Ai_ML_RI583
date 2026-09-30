# Manually Perform Convolution

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

image_size = 5
kernel_size = 3

output_size = image_size - kernel_size + 1

feature_map = []

print("Input Image:")
for row in image:
    print(row)

print("\nKernel:")
for row in kernel:
    print(row)

print("\nConvolution Calculations:")

for i in range(output_size):

    output_row = []

    for j in range(output_size):

        total = 0

        print(f"\nRegion at position ({i}, {j}):")

        for x in range(kernel_size):
            for y in range(kernel_size):

                image_value = image[i + x][j + y]
                kernel_value = kernel[x][y]

                multiplication = image_value * kernel_value

                print(
                    f"{image_value} * {kernel_value} = {multiplication}"
                )

                total += multiplication

        print("Output =", total)

        output_row.append(total)

    feature_map.append(output_row)


print("\nFeature Map:")

for row in feature_map:
    print(row)
