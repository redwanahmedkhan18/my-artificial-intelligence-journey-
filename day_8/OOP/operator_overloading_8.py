class Tensor:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Tensor(self.value + other.value)

    def __mul__(self, other):
        return Tensor(self.value * other.value)

    def __repr__(self):
        return f"Tensor({self.value})"

t1 = Tensor(10)
t2 = Tensor(20)
t3 = t1 + t2
t4 = t1 * t2
print(t3)  # Tensor(30)
print(t4)  # Tensor(200)