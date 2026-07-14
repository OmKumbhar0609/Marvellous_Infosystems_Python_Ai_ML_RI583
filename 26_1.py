# Write a python program to implement a class named BookStore 

class Demo:
    Value = 100          # Class Variable

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Inside Fun()")
        print("No1 :", self.no1)
        print("No2 :", self.no2)

    def Gun(self):
        print("Inside Gun()")
        print("No1 :", self.no1)
        print("No2 :", self.no2)


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()

Obj1.Gun()
Obj2.Gun()