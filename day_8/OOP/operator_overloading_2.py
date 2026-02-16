class Operator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Operator(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Operator(self.a * other.a, self.b * other.b)

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        return f"{self.a}, {self.b}"

        

op1=Operator(10,20)
op2=Operator(23,34)


op3=op1+op2

print(op3)

print(op1*op2)

if op1 >op2 :
    print(op1,"is greater than",op2)
elif op1 < op2:
    print(op1,"is less than",op2)   
else:
    print(op1,"is equal to",op2)

print(op1,op2)