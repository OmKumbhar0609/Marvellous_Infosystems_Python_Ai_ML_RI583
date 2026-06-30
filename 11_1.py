# Write a program which accepts one number and checks whether it is prime or not.

num = int(input("Enter a number: "))
flag= True
if num <=1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    flag = False
if flag:
    print("It is a prime number.")
else:
    print("It is not a prime number.")