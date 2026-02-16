class Student:
    def __init__(self,name,id,cgpa):
        self.name=name
        self.__id=id
        self.__cgpa=cgpa
    
    def update_id(self,id):
        self.__id=id
        if self.__id<0:
            raise ValueError("ID can not be negative. Please enter a valid ID.")
        else:
            self.__id=id
    
    def update_cgpa(self,cgpa):
        if cgpa <0.0 and cgpa >4.0:
            raise ValueError("CGPA must be between 0.0 and 4.0. Please enter a valid CGPA.")
        else:
         self.__cgpa=cgpa
    def view_student(self):
        print(f"Student Name:{self.name}")
        print(f"Student ID:{self.__id}")
        print(f"Student CGPA:{self.__cgpa}")

student1=Student("Alice",12345,3.5)
student1.view_student()
student1.update_id(54321)
student1.update_cgpa(3.8)
student1.view_student()

    

