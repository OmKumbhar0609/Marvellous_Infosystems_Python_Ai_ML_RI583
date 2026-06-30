# Write a program which accepts one number and prints count of digits in that number.

num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Count of digits:", count)