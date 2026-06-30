# Write a program which accepts one number and prints all odd numbers till that number.

num = int(input("Enter a number: "))
for i in range(1, num + 1, 2):
    print(i, end=" ")