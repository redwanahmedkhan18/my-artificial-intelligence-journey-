class Student:
    school_name = "OpenAI Academy"   # Class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Method
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {Student.school_name}")

    # Class Method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static Method
    @staticmethod
    def is_pass(marks):
        return marks >= 40


# Creating objects
s1 = Student("Redwan", 85)
s2 = Student("Ahmed", 35)

s1.display()
s2.display()

# Calling class method
Student.change_school("MIT AI School")

print("\nAfter changing school name:\n")

s1.display()
s2.display()

# Calling static method
print("\nResult:")
print("Redwan Passed?", Student.is_pass(s1.marks))
print("Ahmed Passed?", Student.is_pass(s2.marks))
