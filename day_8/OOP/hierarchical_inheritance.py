class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc

c = Car("Tesla", 5)
b = Bike("Yamaha", 150)

print(c.brand, c.seats)
print(b.brand, b.cc)
