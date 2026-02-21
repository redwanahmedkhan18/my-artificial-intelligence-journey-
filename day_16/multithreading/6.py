from threading import Thread, Lock

class String_check(Thread):
    def __init__(self, text,lock):
        super().__init__()
        self.text = text
        self.lock=lock
    def display(self):
        with self.lock:
            print(f"\n[{self.name}] started")
            for ch in self.text:
                print(ch, end='', flush=True)
            print(f"\n[{self.name}] finished")





lock=Lock()

s1=String_check("Hello World",lock)
s2=String_check("You are Welcome",lock)
s1.start()
s2.start()
s1.display()
s2.display()
s1.join()
s2.join()