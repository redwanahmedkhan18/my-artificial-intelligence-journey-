class Cat:
    def __init__(self, name, breed,action):
        self.name = name
        self.breed = breed
        self.action=action

    def view(self):
        print(f"Cat(name='{self.name}', breed='{self.breed}', action='{self.action}')")

    def compare(self,ct):
        if self.action==ct.action:
            print(f"Both cats are {self.action}ing")
        else:
            print(f"The cats are doing different actions: {self.name} is {self.action}ing while {ct.name} is {ct.action}ing")

c1 = Cat("Whiskers", "Siamese","play")
c2 = Cat("Mittens", "Persian","sleep")
c1.view()
c2.view()
c1.compare(c2)


