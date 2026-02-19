import math
try:
    math.exp(1000)
except OverflowError:
    print("Number too large")
