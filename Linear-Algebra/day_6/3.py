import math
def power(base,pow):
    return math.pow(base,pow)


print(int(power(2,3)))

print(int(power(5,0)))


#Another solution

def power(base, pow):
    return base ** pow

print(power(2, 3))
print(power(5, 0))