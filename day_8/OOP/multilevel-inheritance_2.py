class A:
    def __init__(self,x):
        self.x=x

class B(A):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

class C(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

c1=C(10,20,30)
print(f"x: {c1.x}, y: {c1.y}, z: {c1.z}")