class Animal:
    def __init__(self):
        print("Animal init")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal init")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird init")

class Bat(Mammal, Bird):
    def __init__(self):
        super().__init__()
        print("Bat init")

bat = Bat()
# Output:
# Animal init
# Bird init    (MRO calls Bird's init after Animal)
# Mammal init
# Bat init