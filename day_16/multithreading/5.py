from threading import *

def display(str1):
    with l:
        for x in str1:
            print(x)




l=Lock()

s1=Thread(target=display,args=("Hello World",))
s2=Thread(target=display,args=("You are Welcome",))
s1.start()
s2.start()

s1.join()
s2.join()