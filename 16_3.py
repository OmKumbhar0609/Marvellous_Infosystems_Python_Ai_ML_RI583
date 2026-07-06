# Write a program which contains one function named as Add() which accepts two numbers and returns addition.

def Add(no1, no2):
    return no1 + no2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

ans = Add(a, b)
print("Addition =", ans)