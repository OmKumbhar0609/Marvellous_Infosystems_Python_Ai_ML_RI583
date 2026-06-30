# Write a program which accepts one number and prints multiplication table of that number.
def PrintTable(no):
    for i in range(1, 11):
        print(no*i,end=" ")

num = int(input("Enter a number: "))
PrintTable(num)