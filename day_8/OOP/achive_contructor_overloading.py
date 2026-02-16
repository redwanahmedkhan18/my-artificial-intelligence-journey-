class Student:
    def __init__(self,name=None,Id=None):
        self.name=name
        self.id=Id

    def view(self):
        print(f"Name:{self.name},ID:{self.id}")



s1=Student()
s1.view()
s2=Student("Redwan",2345)
s2.view()

