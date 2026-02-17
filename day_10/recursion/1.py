def print_number(n):
    print(n)
    if n==1:
        return 1
    return print_number(n-1)


print_number(10)

