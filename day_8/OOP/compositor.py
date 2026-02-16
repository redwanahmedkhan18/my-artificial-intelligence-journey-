class Student:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
    
    def student_info(self):
        print(f"Name: {self.name} Id: {self.id} Department: {self.dept}")


class Department:
    def __init__(self,name,id,dept,cgpa):
        self.student=Student(name,id,dept)
        self.cgpa=cgpa

    def student_informations(self):
        self.student.student_info()
        print(f"CGPA: {self.cgpa}")

c1=Department("Redwan",263024,"AI",3.75)
c1.student_informations()