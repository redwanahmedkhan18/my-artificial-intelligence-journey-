def calculate_digits(n):
    n=abs(n)
    if n<10:
        return 1
    return 1+calculate_digits(n//10)


print(calculate_digits(12345))