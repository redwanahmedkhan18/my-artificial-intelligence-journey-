class Student:
    def __init__(self,name):
        self.name=name
        self.dept="BBA"
    def view_info(self):
        print(f"{self.name} is studying at {self.dept}")
    
class CSStudent(Student):
    def __init__(self, name,dept):
        super().__init__(name)
        self.dept=dept
    def update_cs_info(self):
        print(f"{self.name} is studying at {self.dept} department.")



c1=CSStudent("Redwan","Artificial Intelligence")
c1.update_cs_info()

c2=Student("Alex")
c2.view_info()

