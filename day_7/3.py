x=3
def outer():
    x=10
    def inner():
        nonlocal x
        x+=10
        print(x)
    inner()
    print(x)


outer()

print(x)