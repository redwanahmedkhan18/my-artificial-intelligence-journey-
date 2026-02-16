class Matrix:

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.data)
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = m1 + m2
print(m3)