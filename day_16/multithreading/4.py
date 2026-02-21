from threading import *

class Comparison(Thread):
    def __init__(self, lst, lst1):
        super().__init__()
        self.lst = lst
        self.lst1 = lst1

    def run(self):
        for i in range(len(self.lst)):
            if self.lst[i] == self.lst1[i]:
                print(f"[Thread] Match:", self.lst[i])
            else:
                print(f"No match")

lst = [1,2,3,4]
lst1 = [1,2,6,7]

t1 = Comparison(lst, lst1)
t1.start()

for i in range(len(lst)):
    if lst[i] == lst1[i]:
        print("[Main] Match:", lst[i])
    else:
        print("No match")

t1.join()