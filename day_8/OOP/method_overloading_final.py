from multipledispatch import dispatch

class Calculator:

    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(float, float)
    def add(self, a, b):
        return a + b

    @dispatch(str, str)
    def add(self, a, b):
        return a + b

    @dispatch(int, float)
    def add(self, a, b):
        return a + b


calc = Calculator()

print(calc.add(5, 10))                 # 15
print(calc.add(5.5, 10.2))             # 15.7
print(calc.add("Hello, ", "World!"))   # Hello, World!
print(calc.add(5, 10.5))               # 15.5
