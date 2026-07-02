# Write a lambda function which accepts two numbers and returns maximum number.

maximum = lambda x, y: x if x > y else y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Maximum =", maximum(num1, num2))