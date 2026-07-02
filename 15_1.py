# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)