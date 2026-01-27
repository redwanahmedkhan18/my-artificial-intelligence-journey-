class person:

    def __init__(self,name,id,age,dept,university,passion):
        #Atttributes 
        #Instance Variables
        self.name=name
        self.id=id
        self.age=age
        self.dept=dept
        self.university=university
        self.passion=passion
    #Instance Method
    def display(self):
        
        print("Hi, This is",self.name)
        print("My ID is",self.id)
        print("I am ", self.age,"years old")
        print("I am from",self.dept,"department")
        print("I am studying in",self.university)
        print("I  am a pssionte about",self.passion)

        print("This is my fucking OOPs learning initiative in Python.I want you become a fucking pro in it and make a lots of fukcing money and become a pro AI engineer in my fuciking future life and finally want to become a fucking AI engineer in Google")
        print("Thank You")
        print("---------------------------------------------------")
        print()


person_1=person("Redwan Ahmed Khan","MIT-AI-2026",26,"Artificical Intelligence", "Massachussetts Institute of Technology","Artificial Intelligence")

person_1.display()

p2=person("RAK","mit-cs-2024",25,"CSE","MIT","AI")
p2.display()
