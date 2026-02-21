class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.value = self.start
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_range = MyRange(1, 10)

for i in my_range:
    print(i)