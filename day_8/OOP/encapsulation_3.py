class Student:
    def __init__(self,name,age,id,cgpa):
        self.name=name
        self.age=age
        self.__id=id
        self.__cgpa=cgpa
    
    def set_id(self,id):
        if id <0:
            raise ValueError("ID can not be negative. Please enter a valid ID.")
        else:
            self.__id=id
    
    def set_cgpa(self,cgpa):
        if cgpa <0.0 or cgpa >4.0:
            raise ValueError("CGPA must be between 0.0 and 4.0. Please enter a valid CGPA.")
        else:
         self.__cgpa=cgpa
    
    def get_id(self):
        return self.__id    
    def get_cgpa(self):
        return self.__cgpa
    
    def view_student(self):
        print(f"Student Name:{self.name}")
        print(f"Student Age:{self.age}")
        print(f"Student ID:{self.__id}")
        print(f"Student CGPA:{self.__cgpa}")

student1=Student("Alice",20,12345,3.5)
student1.view_student()
student1.set_id(54321)
student1.set_cgpa(3.8)
student1.view_student()

student1.get_id()
student1.get_cgpa()
