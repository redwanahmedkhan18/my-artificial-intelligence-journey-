class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    @classmethod
    def default(cls):
        return cls("Unknown",0)
    @classmethod
    def from_name(cls,name):
        return cls(name,0)
    @classmethod
    def from_id(cls,id):
        return cls("Unknown",id)
    
    @classmethod
    def from_full_info(cls,name,id):
        return cls(name,id)
    
    def view(self):
        print(f"Name:{self.name},ID:{self.id}")

s1=Student.default()
s1.view()
s2=Student.from_name("Redwan")
s2.view()
s3=Student.from_id(2345)
s3.view()
s4=Student.from_full_info("Redwan",2345)
s4.view()
