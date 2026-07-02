# Write a lambda function which accepts one number and returns cube of that number.

cube = lambda x: x * x * x
num = int(input("Enter a number: "))
print("Cube =", cube(num))