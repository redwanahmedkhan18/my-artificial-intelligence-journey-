class Dataset:

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)


d = Dataset([10,20,30,40])
print(len(d))   # 4
