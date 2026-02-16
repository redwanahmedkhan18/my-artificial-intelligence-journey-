class Student:
    def __init__(self,name):
        self.name=name

    def view(self):
        print(f"Student Name:{self.name}")


class Teacher:
    def __init__(self,course):
        self.course=course

    def view(self):
        print(f"Mr. Alex takes {self.course}")


def info(obj):
    obj.view()


s1=Student("Redwan")
t1=Teacher("Artificial Intelligence")

info(s1)
info(t1)