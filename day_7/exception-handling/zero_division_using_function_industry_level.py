def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b

try:
    print(divide(10,5))
    print(divide(5, 0))
except ZeroDivisionError as e:
    print("Caught error:", e)
