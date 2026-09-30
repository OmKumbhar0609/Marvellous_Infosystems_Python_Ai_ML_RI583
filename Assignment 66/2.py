# Python program to demonstrate different activation functions

import numpy as np
import matplotlib.pyplot as plt

# Input values from -10 to 10
x = np.linspace(-10, 10, 200)

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Calculate outputs
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# Plot Sigmoid
plt.figure(figsize=(8, 5))
plt.plot(x, y_sigmoid)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot ReLU
plt.figure(figsize=(8, 5))
plt.plot(x, y_relu)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot Tanh
plt.figure(figsize=(8, 5))
plt.plot(x, y_tanh)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Sigmoid:

# sigma(x)=\frac{1}{1+e^{-x}}
# Output range: 0 to 1.
# Commonly used for binary classification output.

# ReLU:

# ReLU(x)=max(0,x)
# Negative values become 0.
# Positive values remain unchanged.
# Commonly used in hidden layers.

# Tanh:

# tanh(x)
# Output range: -1 to 1.
# Zero-centered.
# Can be used in neural network hidden layers.
