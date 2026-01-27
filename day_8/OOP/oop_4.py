#default instance attributes and methods

class student:
    def __init__(self,name,id,age,dept,university,passion):
        self.name=name
        self.id=id
        self.age=age
        self.dept=dept
        self.university=university
        self.passion=passion
        self.semester="Fall 2026"

    def view(self):
        print("Hi, This is",self.name)
        print("My ID is",self.id)
        print("I am ", self.age,"years old")
        print("I am from",self.dept,"department")
        print("I am studying in",self.university)
        print("I  am a pssionte about",self.passion)
        print("I am currently in",self.semester,"semester")


s1=student("Alice Smith", "54321", 19, "Artificial Intelligence", "Massachussetts Institute of Technology", "Robotics")
s1.view()

s2=student("John Doe", "12345", 20, "Computer Science", "Harvard University", "Machine Learning")

s2.view()

