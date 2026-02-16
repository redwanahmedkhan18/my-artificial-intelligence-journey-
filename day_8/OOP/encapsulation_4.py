class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    def update_student(self, name, age):
        self.__student_update(name, age)

    def __student_update(self, name, age):
        self.__name = name
        self.__age = age   
        if age <= 0:
            print("Age must be positive.")
            self.__age = 0  # Set to default value if invalid
    
    def view_student(self):
        self.__student_update(self.__name, self.__age)  # Call the private method to update student information
        print(f"Student Name: {self.__name}")
        print(f"Student Age: {self.__age}")

student1 = Student("Alice", 20)
student1.view_student()
student1.update_student("Bob", 25)
student1.view_student() 
student1.update_student("Charlie", -5)  # Invalid age
student1.view_student()