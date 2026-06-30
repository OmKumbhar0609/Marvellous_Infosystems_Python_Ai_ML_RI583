# Write a program which accepts one number and checks whether it is divisible by 3 and 5.
def Check():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both 3 and 5.")
    else:
        print("Not divisible by both 3 and 5.")

Check()
