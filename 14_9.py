# Write a lambda function which accepts two numbers and returns subtraction.

subtract = lambda x, y: x - y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Subtraction =", subtract(num1, num2))