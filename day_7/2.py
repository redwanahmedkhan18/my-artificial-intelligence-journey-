x=30
def fun():
    global x
    print(x)
    x=40
    x+=20
    print(x)

fun()
print(x)
