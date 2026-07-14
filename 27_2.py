# # Write a python program to implement a class named BankAccount

class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):
        money = float(input("Enter Deposit Amount : "))
        self.Amount += money
        print("Amount Deposited Successfully")

    def Withdraw(self):
        money = float(input("Enter Withdrawal Amount : "))

        if money <= self.Amount:
            self.Amount -= money
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


Obj1 = BankAccount("Om", 10000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()

print("Interest :", Obj1.CalculateInterest())
Obj1.Display()