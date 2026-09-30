# Python program to simulate a single artificial neuron

import math

# Input values
x1 = 2
x2 = 3

w1 = 0.4
w2 = 0.6

bias = 0.5

weighted_sum = (x1 * w1) + (x2 * w2) + bias

# Sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

print("Weighted Sum:", weighted_sum)
print("Sigmoid Output:", output)

if output >= 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")

# The neuron first calculates the weighted sum:

# z = x1w1+x2w2+b 
# z=(2)(0.4)+(3)(0.6)+0.5=3.1 

# The sigmoid function converts 3.1 into approximately 0.957, which is close to 1.
