# Write a program which accepts one number and checks whether it is perfect number or not.

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")