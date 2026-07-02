# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element

from functools import reduce

numbers = [10, 25, 8, 40, 15]
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print("Minimum:", minimum)