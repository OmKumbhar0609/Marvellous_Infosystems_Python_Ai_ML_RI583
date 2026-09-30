# Python program to show how weights are updated in ANN

# Input values
x = 2

weight = 0.5

bias = 0.1

target = 1

learning_rate = 0.1

prediction = (x * weight) + bias

error = target - prediction

old_weight = weight

# Update weight using gradient descent logic
weight = weight + learning_rate * error * x

# Update bias
bias = bias + learning_rate * error

# Display results
print("Input:", x)
print("Target:", target)
print("Prediction:", prediction)
print("Error:", error)
print("Old Weight:", old_weight)
print("Updated Weight:", weight)
print("Updated Bias:", bias)

# Prediction:

# prediction=(2)(0.5)+0.1 $$ $$ prediction=1.1 

# Error:

#  error=1-1.1=-0.1 

# Weight update:

#  new\ weight=old\ weight+learning\ rate\times error\times input 
#  =0.5+(0.1)(-0.1)(2) 
#  =0.48
