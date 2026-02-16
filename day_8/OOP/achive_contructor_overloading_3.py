class Student:
    def __init__(self,**information):
        self.name =information['name'] 
        self.id =information.get('id')
        self.age=information['age']
        self.cgpa=information['cgpa']

    def view(self):
        print(f"Name:{self.name},ID:{self.id},Age:{self.age},CGPA:{self.cgpa}")



s1=Student(name="Redwan",age=22,cgpa=3.5)
s1.view()
s2=Student(name="Redwan",id=2345,age=22,cgpa=3.5)
s2.view()
# s3=Student()
# s3.view()
