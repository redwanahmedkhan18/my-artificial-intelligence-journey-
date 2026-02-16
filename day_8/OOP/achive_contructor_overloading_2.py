class Student:
    def __init__(self,*args):
        self.name = None
        self.id = None
        
        if len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name=args[0]
            self.id=args[1]
         

    def display(self):
        print(f"Name:{self.name},ID:{self.id}")

s1=Student()
s1.display()
s2=Student("Redwan")
s2.display()
s3=Student("Redwan",2345)
s3.display()    
