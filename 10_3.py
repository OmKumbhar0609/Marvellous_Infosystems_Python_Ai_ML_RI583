# Write a program which accepts one number and prints factorial of that number.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact*i
print("Factorial=",fact)