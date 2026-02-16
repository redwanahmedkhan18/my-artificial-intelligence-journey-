class Student:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, CGPA: {self.cgpa}")


class CSStudent(Student):
    def __init__(self, name, id, cgpa, programming_language):
        super().__init__(name, id, cgpa)   
        self.programming_language = programming_language

    def CompetitiveProgramming(self):
        print(f"{self.name} is using: {self.programming_language} for competitive programming.")
    

s1 = CSStudent("Redwan", 18103220, 3.75, "Python")

s1.display()
s1.CompetitiveProgramming()
