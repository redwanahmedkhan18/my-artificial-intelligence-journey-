from threading import *


def sum():
    lst=[1,2,3,4]
    s=0
    for i in lst:
        s+=i
        print(s)



s1=Thread(target=sum)

s1.start()

lst=[1,2,3,4]

s=0
for i in lst:
    s+=i
    print(s)

s1.join()