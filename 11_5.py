# Write a program which accepts one number and checks whether it is palindrome or not.
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")