# Accept one number and check whether it is prime or not.

def Prime(no):

    if no <= 1:

        return False

    for i in range(2, no):

        if no % i == 0:

            return False

    return True

num = int(input("Enter number: "))

if Prime(num):
    
    print("It is Prime Number")
else:
    print("It is Not Prime Number")