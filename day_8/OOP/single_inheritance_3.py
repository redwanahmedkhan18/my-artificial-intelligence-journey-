class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"{self.name} has balance: {self.balance}")

class SavingsAccount(Bank):
    def add_interest(self):
        self.balance+=self.balance*0.05

s1= SavingsAccount("Redwan",1000)
s1.show_balance()
s1.deposit(500)
s1.show_balance()
s1.add_interest()
s1.show_balance()
s1.withdraw(2000)
s1.withdraw(1000)
s1.show_balance()
s1.deposit(90000)
s1.show_balance()


    