# Write a program which contains one function named as ChkNum() which accepts one parameter as number. If number is even then display "Even Number" otherwise display "Odd Number".

def ChkNum(no):

    if no%2==0:

        print("Even Number.")

    else:

        print("Odd Number.")

num=int(input("Enter the number:"))

ChkNum(num)    