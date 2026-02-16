class Vector:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, index):
        return self.values[index]
v = Vector([10,20,30])
print(v[0])
print(v[1])
