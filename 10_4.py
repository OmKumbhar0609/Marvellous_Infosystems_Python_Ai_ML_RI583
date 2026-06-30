# Write a program which accepts one number and prints all even numbers till that number.

num = int(input("Enter a number: "))
for i in range(2, num + 1, 2):
    print(i, end=" ")