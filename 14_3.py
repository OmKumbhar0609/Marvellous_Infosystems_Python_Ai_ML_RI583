# Write a lambda function which accepts two numbers and returns minimum number.

minimum = lambda x, y: x if x < y else y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Minimum =", minimum(num1, num2))