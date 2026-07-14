# # Write a python program to implement a class named Numbers

class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        total = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i

        return total == self.Value

    def Factors(self):
        print("Factors are :")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i

        return total


num = int(input("Enter Number : "))

Obj = Numbers(num)

print("Prime :", Obj.ChkPrime())
print("Perfect :", Obj.ChkPerfect())
Obj.Factors()
print("Sum of Factors :", Obj.SumFactors())