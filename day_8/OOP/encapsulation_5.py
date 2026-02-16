class Student:
    total_makrs = 0
    average_marks = 0

    def __init__(self, name, cs_marks, maths_marks, english_marks):
        self.name = name
        self.cs_marks = cs_marks
        self.maths_marks = maths_marks
        self.english_marks = english_marks

    def computer_science(self):
        Student.total_makrs += self.cs_marks

    def mathematics(self):
        Student.total_makrs += self.maths_marks

    def english(self):
        Student.total_makrs += self.english_marks

    def calculate_average(self):
        Student.average_marks = Student.total_makrs / 3


Student1 = Student("Redwan", 98, 68, 78)

Student1.computer_science()
Student1.mathematics()
Student1.english()
Student1.calculate_average()

print(Student.total_makrs)     
print(Student.average_marks)   
