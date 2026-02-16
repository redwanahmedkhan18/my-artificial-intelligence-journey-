class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return other + self.value

num = Number(10)
print(num + 5)  # 15
print(5 + num)  # 15   