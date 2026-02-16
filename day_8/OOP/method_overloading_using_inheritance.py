class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def info(self):
        print(f"{self.name} and id:{self.id}")


class CSStudent(Student):
    def __init__(self,name,id,dept):
        super().__init__(name,id)
        self.dept=dept

    def info(self):
        super().info()
        print(f"The student is from {self.dept} department")


c2=CSStudent("Redwan Ahmed Khan",265043,"CSE")
c2.info()

