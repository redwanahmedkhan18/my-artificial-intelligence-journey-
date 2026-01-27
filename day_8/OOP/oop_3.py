#default instance attributes and methods

class student:
    def __init__(self):
        self.university="Massachussetts Institute of Technology"
        self.dept ="Artificial Intelligence"
        self.country="United States of America"
        self.states="Massachussetts"
        self.city="Cambridge"
        self.semester="Fall 2026"

    def view(self):
        print("I am from",self.university)
        print("I am studying in",self.dept,"department")
        print("I live in",self.city," ",self.states," ",self.country)
        print("I am currently in",self.semester,"semester")


s1=student()
s1.view()

s2=student()

s2.university="Harvard University"
s2.dept="Computer Science"

s2.city="Cambridge"

s2.view()

