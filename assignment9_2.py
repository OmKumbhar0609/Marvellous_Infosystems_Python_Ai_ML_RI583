# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
def ChkGreater():
    no1 = float(input("Enter the first number: "))
    no2 = float(input("Enter the second number: "))
    if no1 > no2:
        print(f"The greater number is: {no1}")
    else:
        print(f"The greater number is: {no2}")

ChkGreater()