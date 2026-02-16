class Student:
    def __init__(self,name,age,grade,cgpa):
        self.name=name
        self.age=age
        self.grade=grade
        self.cgpa=cgpa
    
    def view(self,numbers):
        sum=0
        for i in numbers:
            sum+=i
        
        average=sum/len(numbers)

        if average>=90.0:
            self.grade="A"
            self.cgpa=4.0
        elif average>=80.0:
            self.grade="B"
            self.cgpa=3.0
        elif average>=70.0:
            self.grade="C"
            self.cgpa=2.0
        elif average>=60.0:
            self.grade="D"
            self.cgpa=1.0
        else:
            self.grade="F"
            self.cgpa=0.0
        print(f"Name:",self.name)
        print(f"Age:",self.age)
        print(f"Average:",average)
        print(f"Grade:",self.grade)
        print(f"CGPA:",self.cgpa)
        numbers[0]=92
        print()

numbers=[87,98,93,89,95,81,99]
s1=Student("Redwan",20,0,0)
print("Method inside class:",numbers)
print("Method outside class:",numbers)
s1.view(numbers)

