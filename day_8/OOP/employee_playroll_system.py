class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    
    def calculate_salary(self):
        return self.base_salary
    
class Manager(Employee):
    def calculate_salary(self):
        return super().calculate_salary()+50000

class Engineer(Employee):
    def calculate_salary(self):
        return super().calculate_salary()+60000


e1=Employee("Redwan", 50000)

e2=Manager("Ali Ahammad",40000)

e3=Engineer("Redwan Ahmed Khan",60000)

print(f"{e1.name} Salary: {e1.calculate_salary()}")
print(f"{e2.name} Salary: {e2.calculate_salary()}")
print(f"{e3.name} Salary: {e3.calculate_salary()}")