class Animal:
    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Dog(Mammal):
    def bark(self):
        print("Barking...")
d1 = Dog()
d1.eat()
d1.walk()
d1.bark()

