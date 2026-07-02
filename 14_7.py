# Write a lambda function which accepts one number and returns True if number is positive otherwise False.

is_positive = lambda x: x > 0
num = int(input("Enter a number: "))
print("Is positive:", is_positive(num))
