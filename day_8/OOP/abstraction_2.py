from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid via card:", amount)

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid via UPI:", amount)


payments = [CardPayment(), UPIPayment()]

for p in payments:
    p.pay(1000)
